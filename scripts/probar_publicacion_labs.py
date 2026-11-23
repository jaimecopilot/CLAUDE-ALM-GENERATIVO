"""Ejecuta los bloques de publicación de las guías contra un remoto Git temporal."""
import re
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path

CURSO = Path(__file__).resolve().parents[1]
MANUAL = "practica/manual"
FEATURE = "feature/gestion-reservas"
ARCHIVOS = {
    "L05": (
        "app/ejemplo.py", "tests/test_ejemplo.py", "docs/arquitectura/diseno.md",
        "alm/prompts-generados/03-desarrollo.md", "alm/evidencias/registro.md",
        "README.md", "requirements.txt",
    ),
    "L07": (
        ".gitlab-ci.yml", "docs/entrega/informe.md",
        "alm/prompts-generados/05-devops.md", "alm/evidencias/registro.md",
    ),
}


def git(carpeta, *argumentos):
    return subprocess.check_output(
        ["git", *argumentos], cwd=carpeta, text=True, stderr=subprocess.PIPE
    ).strip()


def comandos_publicacion(lab):
    guia = (CURSO / "01_ALUMNOS" / lab / "PRACTICA.md").read_text(encoding="utf-8")
    bloques = re.findall(r"^~~~bash\n(.*?)^~~~", guia, re.MULTILINE | re.DOTALL)
    bloque, = [b for b in bloques if re.search(r"^git commit ", b, re.MULTILINE)]
    for linea in bloque.strip().splitlines():
        programa, *argumentos = shlex.split(linea)
        if programa != "git" or argumentos[0] not in {"add", "diff", "commit", "push"}:
            raise ValueError(f"Comando inesperado en {lab}: {linea}")
        yield argumentos


def probar(rama, labs):
    with tempfile.TemporaryDirectory() as temporal:
        raiz = Path(temporal)
        remoto, alumno = raiz / "remoto.git", raiz / "alumno"
        git(raiz, "init", "--bare", "-b", "main", str(remoto))
        shutil.copytree(CURSO / "03_GITLAB_PLANTILLA", alumno)
        git(alumno, "init", "-b", "main")
        git(alumno, "config", "user.name", "Ensayo de publicación")
        git(alumno, "config", "user.email", "ensayo@example.invalid")
        git(alumno, "add", ".")
        git(alumno, "commit", "-m", "Plantilla inicial")
        base = git(alumno, "rev-parse", "HEAD")
        git(alumno, "remote", "add", "origin", str(remoto))
        git(alumno, "tag", "base-alm")
        git(alumno, "switch", "-c", MANUAL)
        git(alumno, "push", "-u", "origin", "main", MANUAL, "base-alm")
        if rama == FEATURE:
            git(alumno, "switch", "-c", rama)

        for lab in labs:
            for nombre in ARCHIVOS[lab]:
                with (alumno / nombre).open("a", encoding="utf-8") as archivo:
                    archivo.write(f"\n# Control de publicación para {lab}\n")
            for argumentos in comandos_publicacion(lab):
                git(alumno, *argumentos)
            lector = raiz / f"segundo-clon-{lab}"
            git(raiz, "clone", "--branch", rama, str(remoto), str(lector))
            assert git(lector, "rev-parse", "HEAD") == git(alumno, "rev-parse", "HEAD")
            for nombre in ARCHIVOS[lab]:
                assert (lector / nombre).read_bytes() == (alumno / nombre).read_bytes(), nombre
            assert git(remoto, "rev-parse", "main") == git(remoto, "rev-parse", "base-alm") == base
            if rama == FEATURE:
                assert git(remoto, "rev-parse", MANUAL) == base
            print(f"OK {lab}: {len(ARCHIVOS[lab])} archivos recuperados desde {rama}.")


if __name__ == "__main__":
    probar(MANUAL, ["L05", "L07"])
    probar(FEATURE, ["L05"])
