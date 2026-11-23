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
            if fitz.get_text_length(line, fontname="cour", fontsize=8.0) > self.width:
                raise ValueError(f"Línea PowerShell demasiado larga: {line}")
            self.y += 12
            self.page.insert_text((LEFT, self.y), line, fontname="cour",
                                  fontsize=8.0, color=INK)
        # Separar visualmente el bloque de código del párrafo siguiente.
        self.y += 25


def page6(page):
    w = Writer(page, 6)
    w.title("3. GitLab e importación: procedimiento Windows")
    w.subtitle("3.2 Verificar Git y preparar la identidad")
    w.p("Instala Git for Windows desde git-scm.com y abre una terminal PowerShell nueva. "
        "Configura la identidad real antes del primer commit; no copies literalmente los ejemplos.")
    w.code([
        "git --version",
        'git config --global user.name "Nombre Apellido"',
        'git config --global user.email "correo@ejemplo.com"',
        "git config --global init.defaultBranch main",
    ])
    w.subtitle("3.3 Importación reproducible con PowerShell")
    w.p("El alumno crea en GitLab un proyecto personal Private, SIN README inicial. "
        "Copia su dirección exacta desde Code > Clone with HTTPS. El nombre real "
        "de la carpeta será el slug del proyecto, no un nombre supuesto.")
    w.step("1", "Sitúate en la carpeta de trabajo y clona el curso una sola vez")
    w.code([
        "cd $HOME",
        "git clone https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO.git",
    ])
    w.p("Si el curso ya está clonado en esa carpeta, omite el segundo comando. "
        "No clones el repositorio del curso dentro del repositorio GitLab.")
    w.step("2", "Define la URL de GitLab y la ruta del script")
    w.code([
        '$repo = "https://gitlab.com/TU_USUARIO/NOMBRE_REAL_DEL_PROYECTO.git"',
        '$script = Join-Path $HOME "CLAUDE-ALM-GENERATIVO\scripts\Preparar-L02.ps1"',
    ])
    w.p("Sustituye toda la URL entre comillas por la URL HTTPS copiada de GitLab. "
        "No incluyas contraseñas ni tokens en la dirección.")
    w.step("3", "Prepara localmente la plantilla, sin publicar todavía")
    w.code(["& $script -GitLabRepoUrl $repo -CarpetaTrabajo $HOME"])
    w.p("El script clona GitLab vacío, determina la carpeta de destino y copia únicamente "
        "03_GITLAB_PLANTILLA (incluyendo archivos ocultos). Comprueba los contratos, "
        "metaprompts, README y evidencias. Crea el primer commit, main, "
        "base-alm y practica/manual. Si encuentra archivos o commits inesperados, se detiene.")
    return w.y


def page7(page):
    w = Writer(page, 7)
    w.title("3.3 Importación: comprobación y publicación")
    w.step("4", "Examina los resultados antes de hacer push")
    w.code([
        '$nombre = ($repo.TrimEnd("/") -split "/")[-1] -replace "\.git$", ""',
        "cd (Join-Path $HOME $nombre)",
        "Get-ChildItem -Force",
        "git status",
        "git log -1 --oneline",
        "git branch --list",
        "git tag --list",
    ])
    w.p("Comprueba en la raíz CLAUDE.md, alm/, docs/, app/, tests/ y .gitlab/. "
        "El primer commit debe contener solo la plantilla; no debe existir código "
        "de aplicación resuelto ni un pipeline CI ya implementado.")
    w.step("5", "Publica main, la etiqueta y la rama de trabajo")
    w.code([
        "cd $HOME",
        "& $script -GitLabRepoUrl $repo -CarpetaTrabajo $HOME -Publicar",
    ])
    w.p("Esta segunda ejecución comprueba el estado anterior sin duplicar commits. "
        "Publica main, base-alm y practica/manual. GitLab puede solicitar "
        "autenticación segura con Git Credential Manager o el navegador.")
    w.step("6", "Comprueba el remoto y pasa a la rama de práctica")
    w.code([
        "cd (Join-Path $HOME $nombre)",
        "git ls-remote --heads origin",
        "git ls-remote --tags origin",
        "git switch practica/manual",
        "git status",
    ])
    w.p("Recarga GitLab y verifica main, practica/manual y base-alm. "
        "No comiences L03 en main. El tag base-alm debe apuntar al mismo "
        "commit inicial que main; no lo muevas ni fuerces un push.")
    w.subtitle("3.4 Interpretar errores y repetir de forma segura")
    w.p("Un aviso 'cloned an empty repository' es normal al comienzo. "
        "'nothing to commit' significa que no hay cambios pendientes; no demuestra por sí solo "
        "que se haya importado la plantilla. Si origin/main no existe, verifica el "
        "primer push. Si el script detecta otro historial o cambios pendientes, "
        "no los sobrescribas: revisa git status con el formador.")
    w.subtitle("3.5 Alternativas y alcance de las pruebas")
    w.p("En macOS/Linux o sin ejecución de scripts, el formador puede utilizar el "
        "procedimiento manual de L02. GitLab Web IDE sirve para editar y commitear, "
        "pero no importa automáticamente una única subcarpeta del curso.")
    w.p("GitHub Actions valida en Windows las operaciones de clonación, copia, "
        "commit, ramas, etiqueta y push contra un remoto de prueba. "
        "La autenticación y permisos del GitLab privado deben comprobarse "
        "en la cuenta real del alumno.", gap=0)
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
        for fragment in ("-Publicar", "git ls-remote", "practica/manual"):
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
