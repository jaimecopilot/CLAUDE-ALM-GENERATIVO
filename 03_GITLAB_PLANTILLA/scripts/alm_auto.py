#!/usr/bin/env python3
"""Pipeline ALM local: ejecuta contratos mediante Claude Code CLI.

La configuración alm/pipeline_auto.json la GENERA el alumno con Claude en L10.
No almacena credenciales, no llama a Anthropic API directamente y no hace git push.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".alm-run" / "estado.json"
LOGS = ROOT / ".alm-run" / "logs"
EVIDENCE = ROOT / "alm" / "evidencias" / "pipeline-automatico.md"
PIPELINE = ROOT / "alm" / "pipeline_auto.json"

# Estas rutas son una política del taller; el modelo no puede cambiarlas en JSON.
PHASES = (
    ("01", "requisitos", (
        "docs/requisitos/especificacion.md",
        "docs/requisitos/backlog.md",
    )),
    ("02", "diseno", (
        "docs/arquitectura/diseno.md",
        "docs/arquitectura/diagramas.md",
        "docs/arquitectura/ADR-001.md",
    )),
    ("03", "desarrollo", ("app/**/*.py", "requirements.txt")),
    ("04", "testing", (
        "tests/test_*.py",
        "docs/calidad/matriz-pruebas.md",
        "docs/calidad/informe.md",
    )),
    ("05", "devops", (".gitlab-ci.yml", "docs/entrega/informe.md")),
    ("06", "evolucion", (
        "docs/requisitos/especificacion.md",
        "app/**/*.py",
        "tests/test_*.py",
        "docs/entrega/cambio-CAM-01.md",
    )),
)

class Blocked(Exception):
    """Se detiene el pipeline sin declarar fases posteriores completadas."""

def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def phase_paths(number: str, name: str) -> dict[str, str]:
    return {
        "contract": f"alm/contratos/{number}-{name}.md",
        "metaprompt": f"alm/metaprompts/{number}-{name}.md",
        "prompt_out": f"alm/prompts-generados/{number}-{name}.md",
    }

def load_pipeline() -> list[dict]:
    if not PIPELINE.is_file():
        raise Blocked("Falta alm/pipeline_auto.json: debe generarlo Claude en L10.")
    try:
        data = json.loads(PIPELINE.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        raise Blocked(f"JSON inválido: {exc}") from exc
    if type(data) is not dict or data.get("version") != 1:
        raise Blocked("La configuración debe tener version: 1.")
    if data.get("mode") != "automatico-local":
        raise Blocked("El modo debe ser automatico-local.")
    steps = data.get("stages")
    if not isinstance(steps, list) or len(steps) != len(PHASES):
        raise Blocked("El pipeline debe definir exactamente seis fases.")
    for step, (number, name, outputs) in zip(steps, PHASES):
        expected = {"id": number, "name": name, **phase_paths(number, name), "outputs": list(outputs)}
        if not isinstance(step, dict) or step != expected:
            raise Blocked(f"Contrato de fase {number} inválido. Compara con la especificación de L10.")
        for rel in (expected["contract"], expected["metaprompt"]):
            if not (ROOT / rel).is_file():
                raise Blocked(f"Entrada inexistente: {rel}")
    return steps

def log(label: str, value: str):
    LOGS.mkdir(parents=True, exist_ok=True)
    (LOGS / f"{label}.log").write_text(value, encoding="utf-8", errors="replace")

def call_claude(label: str, message: str, turns: int):
    binary = shutil.which("claude")
    if not binary:
        raise Blocked("Claude Code CLI no está instalado o no está en PATH.")
    cmd = [
        binary, "-p", message, "--permission-mode", "dontAsk",
        "--tools", "Read,Write,Edit,Glob,Grep",
        "--allowedTools", "Read,Write,Edit,Glob,Grep",
        "--max-turns", str(turns), "--output-format", "text",
    ]
    try:
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired as exc:
        raise Blocked(f"Tiempo agotado en {label}; verifica logs y cuota.") from exc
    log(label, result.stdout + "\n\nSTDERR:\n" + result.stderr)
    if result.returncode != 0:
        raise Blocked(f"Claude devolvió código {result.returncode} en {label}. Lee el log.")
    if "rate limit" in (result.stdout + result.stderr).lower():
        raise Blocked(f"Posible límite de cuota en {label}; revisión necesaria.")

def check_outputs(step: dict):
    for rel in step["outputs"]:
        matches = list(ROOT.glob(rel)) if "*" in rel else [ROOT / rel]
        valid = [p for p in matches if p.is_file() and p.stat().st_size >= 30]
        if not valid:
            raise Blocked(f"{step['id']}: falta el artefacto obligatorio {rel}")
    number = step["id"]
    if number == "01":
        specification = (ROOT / "docs/requisitos/especificacion.md").read_text(encoding="utf-8")
        for rid in ("RF-01", "RF-02", "RF-03", "RF-04"):
            if rid not in specification:
                raise Blocked(f"La especificación no contiene {rid}")
    if number == "05":
        yml = (ROOT / ".gitlab-ci.yml").read_text(encoding="utf-8")
        if "stages:" not in yml or "pytest" not in yml:
            raise Blocked("No se reconoce un pipeline GitLab con pruebas.")
    if number == "06":
        change = (ROOT / "docs/entrega/cambio-CAM-01.md").read_text(encoding="utf-8")
        if "CAM-01" not in change:
            raise Blocked("No se documenta CAM-01.")

def run_tests(number: str):
    if number not in ("04", "06"):
        return
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q"],
            cwd=ROOT, capture_output=True, text=True, timeout=240,
        )
    except subprocess.TimeoutExpired as exc:
        raise Blocked(f"pytest superó el tiempo de L{number}.") from exc
    log(f"{number}-pytest", result.stdout + "\n" + result.stderr)
    if result.returncode != 0:
        raise Blocked(f"pytest falló en la fase {number}. Revisar {number}-pytest.log.")

def check_auth():
    # No se guarda ni lee ningún token. Se usan credenciales del CLI del alumno.
    if os.environ.get("ANTHROPIC_API_KEY"):
        raise Blocked("ANTHROPIC_API_KEY está definida: riesgo de facturación API. Desactívala.")
    binary = shutil.which("claude")
    if not binary:
        raise Blocked("Instala Claude Code e inicia sesión antes de ejecutar.")
    try:
        auth = subprocess.run([binary, "auth", "status"], capture_output=True, text=True, timeout=20)
        method = json.loads(auth.stdout).get("authMethod", "")
    except (subprocess.TimeoutExpired, ValueError, OSError) as exc:
        raise Blocked("No se ha podido verificar la autenticación de Claude Code.") from exc
    if auth.returncode or method not in ("claude.ai", "oauth_token"):
        raise Blocked("Inicia sesión con tu cuenta Claude compatible; no con API facturada.")

def append_evidence(line: str):
    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    if not EVIDENCE.exists():
        EVIDENCE.write_text("# Ejecución automática local del ALM\n\n", encoding="utf-8")
    with EVIDENCE.open("a", encoding="utf-8") as file:
        file.write(line + "\n")

def main():
    parser = argparse.ArgumentParser(description="Pipeline automático local ALM: sin API ni merge.")
    parser.add_argument("--plan", action="store_true", help="Validar y mostrar el plan sin ejecutar IA.")
    parser.add_argument("--run", action="store_true", help="Pedir autorización global y ejecutar.")
    parser.add_argument("--resume", action="store_true", help="Continuar desde fase no completada.")
    args = parser.parse_args()
    try:
        if not (ROOT / ".git").exists() or not (ROOT / "CLAUDE.md").is_file():
            raise Blocked("Ejecutar dentro de un clon GitLab del alumno con la plantilla.")
        steps = load_pipeline()
        for step in steps:
            print(f"{step['id']} {step['name']} -> {', '.join(step['outputs'])}")
        if args.plan or not args.run:
            print("Plan validado; no se ha invocado Claude ni ejecutado ninguna fase.")
            return 0
        check_auth()
        if input("Para ejecutar en ESTA rama escribe AUTORIZO: ").strip() != "AUTORIZO":
            raise Blocked("Ejecución no autorizada.")
        if STATE.exists() and not args.resume:
            raise Blocked("Existe estado anterior: usar --resume tras revisar el bloqueo.")
        state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {"completed": []}
        if not isinstance(state.get("completed"), list):
            raise Blocked("Estado de ejecución inválido.")
        STATE.parent.mkdir(parents=True, exist_ok=True)
        for step in steps:
            number, name = step["id"], step["name"]
            if number in state["completed"]:
                continue
            print(f"\nFASE {number}: {name}")
            files = phase_paths(number, name)
            Path(ROOT / files["prompt_out"]).parent.mkdir(parents=True, exist_ok=True)
            request_meta = (
                f"Lee {files['metaprompt']} y {files['contract']}, CLAUDE.md y "
                "alm/maestro.md. Genera SOLO el prompt operativo indicado "
                f"en {files['prompt_out']}. Usa las entradas reales aprobadas "
                "de fases previas. No ejecutes todavía el prompt. "
                "Si faltan decisiones de negocio, describe el bloqueo."
            )
            call_claude(f"{number}-metaprompt", request_meta, turns=8)
            prompt_file = ROOT / files["prompt_out"]
            if not prompt_file.is_file() or prompt_file.stat().st_size < 120:
                raise Blocked(f"Falta prompt operativo válido: {files['prompt_out']}")
            request_run = (
                f"El alumno ha preaprobado globalmente la secuencia del ALM para "
                f"este laboratorio y estos contratos. Lee {files['prompt_out']} y "
                f"{files['contract']}; EJECUTA únicamente las instrucciones "
                "compatibles con CLAUDE.md. Reutiliza los artefactos reales "
                "de las fases anteriores, sin inventar una especificación nueva. "
                "Crea los archivos de salida exigidos. No hagas push, merge, "
                "acceso a secretos ni deploy. Si existe una duda de negocio "
                f"sin resolver, escribe alm/evidencias/BLOQUEO-{number}.md y detente."
            )
            call_claude(f"{number}-ejecucion", request_run, turns=22)
            if (ROOT / f"alm/evidencias/BLOQUEO-{number}.md").exists():
                raise Blocked(f"Claude declaró bloqueo de negocio en fase {number}.")
            check_outputs(step)
            run_tests(number)
            state["completed"].append(number)
            STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")
            append_evidence(f"- {now()} · Fase {number} ({name}): archivos exigidos presentes"
                            + ("; pytest OK" if number in ("04", "06") else "")
                            + "; ejecución LOCAL, revisión humana posterior pendiente.")
            print(f"FASE {number} SUPERADA (gates técnicos mínimos).")
        print("\nSECUENCIA COMPLETADA localmente. Revisa requisitos, diffs y trazabilidad.")
        print("Después crea commit, push, MR y verifica por separado CI remoto de GitLab.")
        return 0
    except Blocked as exc:
        append_evidence(f"- {now()} · BLOQUEADO: {exc}")
        print(f"\nBLOQUEADO: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
