# Auditoría operativa del taller ALM generativo — 23/11/2026

**Ámbito:** repositorio de materiales `jaimecopilot/CLAUDE-ALM-GENERATIVO`, laboratorios L01–L11, plantilla y guía general PDF.

**Rama de corrección:** `audit/l02-windows-actions-20261123`, presentada mediante una Pull Request **en borrador**. No se han fusionado estas correcciones a `main`.

## Evidencia real de GitHub Actions

- [L02 validado en Windows PowerShell 7, Windows PowerShell 5.1 y Bash/Ubuntu](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45138841793). Se utilizan repositorios Git bare locales simulados, sin credenciales ni proyecto GitLab privado.
- [Enlaces internos y continuidad de ramas](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45138841753): 56 archivos Markdown examinados, 46 enlaces relativos, 0 incidencias.
- [PDF de 23 páginas corregido](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45138089460). Las páginas 6 y 7 se han sustituido conservando las restantes, y se han inspeccionado sus vistas.
- La prueba complementaria L03 de commits y push utiliza **datos simulados**, no genera requisitos ni issues reales ni consume Claude API; consultar el último workflow de L02.

## Matriz de revisión

| Material | Corrección / comprobación | Estado verificado | Pendiente real |
|---|---|---|---|
| Guía PDF general | Sustituidos los comandos frágiles de páginas 6 y 7 y preservadas las otras 21 páginas | PDF creado, abierto, páginas comprobadas visualmente | Ejecución real con GitLab y Claude |
| L01 | Enlaces internos dentro de auditoría general | Estática | Validación docente |
| L02 | Script de importación, nombre de proyecto dinámico, copia oculta, branch main, base-alm, practica/manual, push y repetición | Git en runners Windows 7/5.1 y Ubuntu/Bash | Credenciales, permisos y ramas reales en GitLab.com |
| L03 | Reglas de Gate A/B, caso de negocio real, creación del primer prompt y commit/push sobre practica/manual | Rutas y consistencia estática; comandos Git simulados | Generación real mediante Claude, stakeholder, issues y gate |
| L04 | Se exige trabajo y publicación en practica/manual | Documental | Ejecutar diseño y aprobar ADR |
| L05 | Corregida contradicción rama feature vs practica/manual; MR borrador a main | Documental | Generar y probar API y MR real |
| L06 | Pruebas y commit en practica/manual, actualización de MR | Documental | Ejecutar pytest sobre aplicación real |
| L07 | Pipeline de producto desde practica/manual y MR en borrador | Documental | Probar GitLab Runner y CI real |
| L08 | CAM-01 desde practica/manual, MR feature hacia manual y retorno antes de L09 | Documental | Implementar evolución y ejecutar regresión |
| L09 | Verifica CAM-01 integrado y conserva documentación en practica/manual | Documental | Generar matriz con referencias reales |
| L10 | Se conserva la separación entre CI de producto y orquestación ALM de 6 jobs, ejecutada solo por el formador | Revisado, sin modificaciones innecesarias | Ejecución central API con presupuesto y credenciales del formador |
| L11 | Comparación de la rama manual completa contra referencia/alm-automatico | Documental | Defensa con ambas evidencias reales |

## Incidencias que sí demostraron las pruebas

1. **PowerShell 5.1:** Git podía emitir un error de HEAD sin commits que la combinación de stderr y `ErrorActionPreference=Stop` trataba como terminante. Se ha reparado y vuelto a ejecutar en Windows PowerShell 5.1.
2. **Comandos PDF:** copiar una línea dividida podía perder el separador `|`, además de presuponer el nombre fijo `coworking-alm-junior`. La guía utiliza ahora el script verificado y copia la URL de GitLab.
3. **Incoherencia ALM:** L05 podía dejar el código únicamente en `feature/gestion-reservas`, mientras L11 solicita `practica/manual`. Se ha alineado el recorrido L03–L09, con MR en borrador o ramas feature que regresan a `practica/manual`.
4. **Primer metaprompt:** L03 no debe presuponer que L02 lo generó; debe comprobarlo, producirlo si falta y detenerse para Gate A.

## Alcance exacto de la validación

**Probado automáticamente:** operaciones Git/PowerShell/Bash en remotos locales simulados, integridad de la estructura, idempotencia básica de L02, rutas y enlaces, y conservación de ramas iniciales.

**No probado todavía:** acceso real al GitLab privado del alumno, OAuth/SSH/HTTPS y permisos, ejecución interactiva de Claude Code, preguntas al cliente, issues GitLab, API generada, pruebas funcionales del MVP, GitLab CI, ni los 6 jobs ALM automáticos.

No confundir el éxito de Actions con una prueba de sistema completa. No fusionar hasta revisar la guía PDF y decidir cómo registrar/verificar los pasos reales con el formador.
