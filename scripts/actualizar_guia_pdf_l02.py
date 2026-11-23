#!/usr/bin/env python3
"""Actualiza las páginas 6 y 7 del PDF docente conservando el resto del original.

Requiere PyMuPDF. No reconstruye ni reduce el documento de 23 páginas.
Uso: python scripts/actualizar_guia_pdf_l02.py 01_ALUMNOS/GUIA_ALUMNADO_CLAUDE_GITLAB_VSCODE_ALM_2026.pdf
"""
import os
import sys
import tempfile
from pathlib import Path

import fitz

NAVY = (0.13, 0.24, 0.36)
INK = (0.16, 0.20, 0.25)
MUTED = (0.36, 0.42, 0.49)
LINE = (0.78, 0.84, 0.90)
BLUE_BG = (0.94, 0.965, 0.99)
LEFT, RIGHT, BOTTOM = 46, 46, 785


class Writer:
    def __init__(self, page, number):
        self.page = page
        self.y = 83
        self.width = page.rect.width - LEFT - RIGHT
        w = page.rect.width
        page.draw_rect(page.rect, fill=(1, 1, 1), color=(1, 1, 1))
        page.insert_text((LEFT, 35), "CLAUDE / GITLAB / VS CODE", fontsize=9.2,
                         fontname="hebo", color=NAVY)
        page.insert_text((w / 2 - 47, 35), "Jaime Gallo García", fontsize=8.8,
                         fontname="helv", color=MUTED)
        page.insert_text((w - 139, 35), "GUÍA DEL ALUMNADO", fontsize=8.8,
                         fontname="hebo", color=NAVY)
        page.draw_line((LEFT, 49), (w - RIGHT, 49), color=LINE, width=.65)
        page.draw_line((LEFT, 801), (w - RIGHT, 801), color=LINE, width=.65)
        page.insert_text((LEFT, 817), "ALM GENERATIVO  •  EDICIÓN 2026  |  REVISIÓN OPERATIVA",
                         fontsize=8, fontname="helv", color=MUTED)
        page.insert_text((w - 65, 817), str(number), fontsize=8, fontname="helv", color=MUTED)

    def _wrap(self, msg, font="helv", size=9.4):
        words = msg.strip().split()
        lines, current = [], ""
        for word in words:
            proposed = f"{current} {word}".strip()
            if fitz.get_text_length(proposed, fontname=font, fontsize=size) <= self.width:
                current = proposed
            else:
                if current:
                    lines.append(current)
                current = word
                if fitz.get_text_length(word, fontname=font, fontsize=size) > self.width:
                    raise ValueError(f"Palabra demasiado ancha: {word!r}")
        if current:
            lines.append(current)
        return lines

    def _line(self, s, size=9.4, height=13.2, font="helv", color=INK):
        if self.y > BOTTOM:
            raise ValueError(f"Desbordamiento de página: y={self.y}")
        self.page.insert_text((LEFT, self.y), s, fontname=font, fontsize=size, color=color)
        self.y += height

    def title(self, s):
        self._line(s, 15.2, 23, "hebo", NAVY)
        self.y += 2

    def subtitle(self, s):
        self.y += 4
        self._line(s, 11.5, 18, "hebo", NAVY)

    def p(self, s, gap=7):
        for line in self._wrap(s):
            self._line(line)
        self.y += gap

    def step(self, n, s):
        self.y += 3
        self._line(f"{n}. {s}", 10.0, 16, "hebo", NAVY)

    def code(self, lines):
        # Los comandos deben copiarse directamente, sin saltos automáticos.
        h = 12 * len(lines) + 16
        if self.y + h > BOTTOM:
            raise ValueError("Desbordamiento del bloque PowerShell")
        self.page.draw_rect(fitz.Rect(LEFT - 6, self.y - 4,
                                     self.page.rect.width - RIGHT + 5, self.y + h),
                            fill=BLUE_BG, color=LINE, width=.4)
        for line in lines:
            if fitz.get_text_length(line, fontname="cour", fontsize=9.2) > self.width:
                raise ValueError(f"Línea PowerShell demasiado larga: {line}")
            self.y += 12
            self.page.insert_text((LEFT, self.y), line, fontname="cour",
                                  fontsize=9.2, color=INK)
        # Separar visualmente el bloque de código del párrafo siguiente.
        self.y += 25


def page6(page):
    w = Writer(page, 6)
    w.title("3. Publicar la plantilla en tu GitLab desde Windows")
    w.p("Abre PowerShell. Usa tu proyecto privado de GitLab, creado sin README como indica la página 5. "
        "Si ya tienes el commit de una ejecución anterior, conserva la carpeta del proyecto.")
    w.step("1", "Comprueba que Git reconoce tu nombre y tu correo")
    w.code(["git --version", "git config --get user.name", "git config --get user.email"])
    w.p("Si falta algún dato, ejecuta la línea correspondiente y escribe tu respuesta cuando la pida.")
    w.code(['git config --global user.name (Read-Host "Tu nombre")',
            'git config --global user.email (Read-Host "Tu correo")'])
    w.step("2", "Obtén la versión de clase del curso")
    w.p("Si es tu primera vez en este ordenador, ejecuta estas dos líneas:")
    w.code(["cd $HOME", "git clone --branch main https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO.git"])
    w.p("Si ya tienes el curso clonado en tu carpeta de usuario, actualiza solo los materiales. "
        "Ejecuta cada línea por separado. Si Git muestra un error, detente y conserva el mensaje.")
    w.code(['$curso = Join-Path $HOME "CLAUDE-ALM-GENERATIVO"',
            'git -C $curso switch main', 'git -C $curso pull --ff-only origin main'])
    w.step("3", "Publica en tu proyecto personal")
    w.p("En GitLab abre tu proyecto y copia Code > Clone with HTTPS. Ejecuta la línea siguiente, "
        "pega la dirección cuando PowerShell la pida y pulsa Intro.")
    w.code(['$repo = (Read-Host "URL HTTPS de tu proyecto GitLab").Trim()'])
    w.p("Ejecuta estas dos líneas. Sirven también si la guía anterior dejó el mensaje 'No se ha hecho push'.")
    w.code([r'$script = Join-Path $HOME "CLAUDE-ALM-GENERATIVO\scripts\Preparar-L02.ps1"',
            '& $script -GitLabRepoUrl $repo -CarpetaTrabajo $HOME -Publicar'])
    w.p("Si se abre el navegador, entra con la cuenta propietaria del proyecto y vuelve a PowerShell. "
        "Espera a leer 'Plantilla publicada'. En la página 7 comprobarás el resultado.", gap=0)
    return w.y


def page7(page):
    w = Writer(page, 7)
    w.title("3.3 Comprobar la publicación y empezar la práctica")
    w.step("4", "Comprueba que tu proyecto ya contiene la plantilla")
    w.p("En GitLab actualiza la página del proyecto y selecciona main. Deben aparecer CLAUDE.md y las "
        "carpetas alm/, docs/, .gitlab/, app/ y tests/. En Code > Branches verás main y practica/manual. "
        "En Code > Tags verás base-alm.")
    w.p("Para comprobarlo desde la misma ventana de PowerShell, ejecuta:")
    w.code([r'$nombre = ($repo.TrimEnd("/") -split "/")[-1] -replace "\.git$", ""',
            "cd (Join-Path $HOME $nombre)", "git ls-remote --heads origin", "git ls-remote --tags origin"])
    w.p("En un proyecto recién importado aparecen tres líneas con el mismo identificador de commit: "
        "refs/heads/main, refs/heads/practica/manual y refs/tags/base-alm.")
    w.step("5", "Abre el proyecto en la rama del alumnado")
    w.code(["git switch practica/manual", "git status", "code ."])
    w.p("Comprueba que git status indica practica/manual y que el árbol está limpio. Si PowerShell no reconoce "
        "code, abre VS Code y selecciona Archivo > Abrir carpeta. Elige la carpeta del proyecto GitLab.")
    w.subtitle("3.4 Si te quedaste a mitad")
    w.p("Si ves 'No se ha hecho push', tu commit ya está guardado. Vuelve al paso 2 de la página 6, elige la "
        "opción para un curso ya clonado y ejecuta el paso 3. Puedes hacerlo en una ventana nueva. "
        "El script reutiliza el commit existente.")
    w.p("Si GitLab rechaza la publicación, comprueba que la URL pertenece a tu proyecto y que has entrado "
        "con la cuenta que puede escribir en él. Si indica que main está protegida, muestra el error al formador. "
        "Una vez resuelto, repite el paso 3.")
    w.p("El aviso 'cloned an empty repository' es normal al clonar un proyecto nuevo. Si en cambio el script "
        "detecta cambios locales, entra en el proyecto, ejecuta git status y revisa esos cambios con el formador.")
    w.p("Si Windows indica que la ejecución de scripts está deshabilitada, consulta al formador. "
        "En un equipo propio donde se permita, ejecuta la siguiente línea en la ventana actual y repite el paso 3. "
        "En un equipo gestionado sigue la política de tu organización.")
    w.code(["Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned"])
    w.subtitle("3.5 Si utilizas macOS o Linux")
    w.p("Sigue el apartado 5.1 de la guía GitLab paso a paso de L02 para la importación con Bash.", gap=0)
    return w.y


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Uso: actualizar_guia_pdf_l02.py RUTA_PDF")
    src = Path(sys.argv[1])
    if not src.is_file():
        raise SystemExit(f"No existe el PDF original: {src}")
    doc = fitz.open(src)
    if len(doc) != 23:
        raise ValueError(f"Se esperaban 23 páginas, hay {len(doc)}; revisar antes de alterar.")
    original_first_page = doc[0].get_text()
    original_last_page = doc[22].get_text()
    for idx, writer in [(5, page6), (6, page7)]:
        replacement = fitz.open()
        new_page = replacement.new_page(width=doc[idx].rect.width, height=doc[idx].rect.height)
        last_y = writer(new_page)
        if last_y >= BOTTOM:
            raise ValueError(f"Desbordamiento de contenido en página {idx + 1}: {last_y}")
        doc.delete_page(idx)
        doc.insert_pdf(replacement, from_page=0, to_page=0, start_at=idx)
        replacement.close()
    doc.set_metadata({"title": "Guía alumnado Claude, GitLab y ALM generativo - revisión operativa",
                      "author": "Jaime Gallo García",
                      "subject": "Corrección verificada de importación GitLab en Windows, L02-L03"})
    with tempfile.NamedTemporaryFile(suffix=".pdf", dir=src.parent, delete=False) as fp:
        tmp = Path(fp.name)
    try:
        doc.save(str(tmp), garbage=4, deflate=True)
        doc.close()
        check = fitz.open(tmp)
        assert len(check) == 23
        assert check[0].get_text() == original_first_page
        assert check[22].get_text() == original_last_page
        t6, t7 = check[5].get_text(), check[6].get_text()
        for fragment in ("Preparar-L02.ps1", "git clone", "base-alm"):
            if fragment not in t6 + t7:
                raise ValueError(f"Falta texto esencial del PDF: {fragment}")
        assert t6.splitlines().count("& $script -GitLabRepoUrl $repo -CarpetaTrabajo $HOME -Publicar") == 1
        for fragment in ("git ls-remote", "practica/manual"):
            if fragment not in t7:
                raise ValueError(f"Falta texto de comprobación del PDF: {fragment}")
        for n in (5, 6):
            # Guardar vistas de las dos páginas como evidencia visual de maquetación.
            pix = check[n].get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
            pix.save(str(src.parent / f"revision_guia_pagina_{n+1}.png"))
        check.close()
        os.replace(tmp, src)
    finally:
        if tmp.exists():
            tmp.unlink()
    print(f"PDF revisado: {src}, 23 páginas; originales 1 y 23 intactas.")


if __name__ == "__main__":
    main()
