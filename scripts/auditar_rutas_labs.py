#!/usr/bin/env python3
"""Comprueba enlaces Markdown y dependencias entre laboratorios."""
from __future__ import annotations

import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [ROOT / "README.md"]
DOCS += list((ROOT / "00_PROGRAMA").rglob("*.md"))
DOCS += list((ROOT / "01_ALUMNOS").rglob("*.md"))
DOCS += list((ROOT / "03_GITLAB_PLANTILLA").rglob("*.md"))
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
errors = []
checked = 0

def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()

for file in DOCS:
    in_code = False
    fence_marker = None
    for lineno, line in enumerate(file.read_text(encoding="utf-8").splitlines(), start=1):
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)[0]
            if not in_code:
                in_code = True
                fence_marker = marker
            elif marker == fence_marker:
                in_code = False
                fence_marker = None
            continue
        if in_code:
            if re.search(r"^\s*(?:git\s+(?:reset\s+--hard|clean\s+-[^ ]*f|push\b.*(?:--force|-f\b)|tag\s+-f)|rm\s+-rf|Remove-Item\b.*-Recurse)", line, re.I):
                errors.append(f"{rel(file)}:{lineno}: revisar comando destructivo ejecutable")
            continue
        for match in LINK.finditer(line):
            target = match.group(1).strip().strip("<>").strip()
            if not target or target[0] == "#" or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            if ' "' in target:
                target = target.split(' "', 1)[0]
            path = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not path:
                continue
            checked += 1
            resolved = (file.parent / path).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"{rel(file)}:{lineno}: enlace roto: {target}")

    if in_code:
        errors.append(f"{rel(file)}: bloque de código sin cierre al final del archivo")

required = [
    "03_GITLAB_PLANTILLA/CLAUDE.md",
    "03_GITLAB_PLANTILLA/alm/maestro.md",
    "03_GITLAB_PLANTILLA/alm/contratos/01-requisitos.md",
    "03_GITLAB_PLANTILLA/alm/metaprompts/01-requisitos.md",
    "03_GITLAB_PLANTILLA/docs/instrucciones/CASO_NEGOCIO.md",
    "scripts/Preparar-L02.ps1",
    "01_ALUMNOS/L02/GUIA_GITLAB_PASO_A_PASO.md",
    "01_ALUMNOS/L03/METAPROMPT.md",
]
for lab in range(1, 12):
    for material in ("TEORIA.md", "PRACTICA.md", "METAPROMPT.md"):
        required.append(f"01_ALUMNOS/L{lab:02}/{material}")

entradas = ("CLAUDE.md", "alm/maestro.md", "alm/contratos/01-requisitos.md",
            "alm/metaprompts/01-requisitos.md", "docs/instrucciones/CASO_NEGOCIO.md")
for ruta in ("01_ALUMNOS/L03/METAPROMPT.md", "03_GITLAB_PLANTILLA/alm/metaprompts/01-requisitos.md"):
    prompt = (ROOT / ruta).read_text(encoding="utf-8").split("~~~text", 1)[1].split("~~~", 1)[0]
    for entrada in entradas:
        if entrada not in prompt:
            errors.append(f"{ruta}: falta en el texto para Claude: {entrada}")

for target in required:
    if not (ROOT / target).exists():
        errors.append(f"prerrequisito no encontrado: {target}")

manual = (ROOT / "01_ALUMNOS/L05/PRACTICA.md").read_text(encoding="utf-8")
l08 = (ROOT / "01_ALUMNOS/L08/PRACTICA.md").read_text(encoding="utf-8")
l09 = (ROOT / "01_ALUMNOS/L09/PRACTICA.md").read_text(encoding="utf-8")
l11 = (ROOT / "01_ALUMNOS/L11/PRACTICA.md").read_text(encoding="utf-8")
if "git push -u origin feature/gestion-reservas" in manual:
    errors.append("L05 sigue publicando el trabajo guiado solo en rama feature")
if "git push -u origin HEAD" not in manual:
    errors.append("L05 debe publicar la rama activa elegida en el paso 1")
if "practica/manual" not in l08 or "feature/CAM-01" not in l08:
    errors.append("L08 no explica retorno de CAM-01 a practica/manual")
if "practica/manual" not in l09 or "CAM-01" not in l09:
    errors.append("L09 no verifica cierre de CAM-01")
if "referencia/alm-automatico" not in l11 or "practica/manual" not in l11:
    errors.append("L11 no identifica las ramas comparadas")

print(f"Documentos inspeccionados: {len(DOCS)}")
print(f"Enlaces relativos comprobados: {checked}")
print(f"Incidencias detectadas: {len(errors)}")
for error in errors:
    print("ERROR:", error)
if errors:
    sys.exit(1)
print("OK: enlaces internos y coherencia de ramas L05-L11 comprobados.")
