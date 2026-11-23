# Auditoría operativa del taller ALM generativo — 23/11/2026

## Revisión para impartición del 23 de noviembre

La [PR #2](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/pull/2) parte de `ef1604a`. La PR #1 ya estaba integrada en ese punto. Para esta revisión se han leído los logs de los siete trabajos de aquella ejecución y se han lanzado pruebas nuevas. El ensayo HTTPS real se solicita aparte. Un trabajo omitido no acredita conectividad ni permisos.

| Lab | Incidencia, corrección o control | Prueba y evidencia disponible | Pendiente en el entorno del taller |
|---|---|---|---|
| L01 | Las cuatro actividades sumaban 35 min dentro de una sesión de 30. Se distribuyen en 5, 5, 15 y 5 min. | Revisión de la práctica y comprobación del total. | Demostración real y cuaderno de cada alumno. |
| L02 | Un clon nuevo podía crear `practica/manual` desde main aunque en el servidor ya estuviera adelantada. El script recupera la rama remota, compara el árbol íntegro, crea la etiqueta sobre main y publica las tres referencias de forma atómica. Comprueba la identidad antes de copiar. | Windows 5.1 y 7, repetición, archivos ocultos y lectura remota de refs. Bash ejecuta el bloque docente y comprueba que una segunda importación se detiene sin cambios. [Logs de Windows y Bash](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45148295481) | Clon HTTPS y publicación en el proyecto privado desde un runner Windows, y cotejo con la interfaz de GitLab. |
| L03 | El texto de clase omitía el metaprompt versionado y la plantilla aludía al caso sin su ruta. Se explicitan las cinco entradas, el prompt único y la parada en Gate A. | Comprobación estática de ambas instrucciones. Commit, push y recuperación de la rama adelantada en un segundo clon con datos de prueba. [Log de Git y segundo clon](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45148295481/job/137602966962) | Lectura por Claude, prompt producido, decisión de Gate A, especificación, backlog, issues y Gate B. |
| L04 | El manual pedía un nombre distinto para el diagrama. Manuales y práctica remiten a `docs/arquitectura/diagramas.md`, diseño y ADR. | Contraste con el contrato 02. | Render Mermaid del diseño generado y aprobación del ADR. |
| L05 | El bloque podía olvidar README y dependencias. Usado desde una feature podía publicar la rama manual equivocada. Se incluye staging explícito y publicación de la rama activa en el recorrido opcional. | Revisión del bloque y de los destinos de MR. | Generación real, arranque de la API, respuestas y MR. |
| L06 | La práctica presentaba como opcional la matriz obligatoria del contrato. Se alinearon el texto y ambos manuales. | Contraste con `04-testing.md`. | Pytest del MVP generado, revisión y evidencias de calidad. |
| L07 | El bloque añadía solo el YAML y el manual pedía otro nombre para el informe. Ahora versiona el prompt, el registro y `docs/entrega/informe.md`. | Revisión del bloque y del contrato 05. | Ejecución de la CI de producto en el GitLab del alumno. |
| L08 | Se explicitan el informe de cambio, la MR hacia la rama guiada y el retorno para L09. | Contraste con el contrato 06 y las pruebas de frontera 3h59, 4h y 4h01. | Regresión y merge aprobado de CAM-01 en el proyecto real. |
| L09 | El prompt documental requiere revisión humana antes de redactar el README y la matriz. | Revisión de la secuencia entre L08, L09 y L11. | Verificar la traza de RF-03 y CAM-01 con enlaces reales. |
| L10 | Se aclara dónde se genera el YAML. Se mantienen los seis jobs centrales, el YAML separado de CI de producto y la distribución por Git. | Revisión de los seis nombres, la transferencia de artefactos y el alcance del formador. | Una ejecución central con API, permisos y presupuesto autorizados, y comprobación de la distribución. |
| L11 | Se añaden comprobaciones sobre `origin/practica/manual`, la MR integrada y la procedencia independiente de la referencia. | Revisión documental de comandos y rúbrica. | Defensa sobre las dos ramas reales. |

### Ejecuciones y límites

- **Windows con remoto Git local.** En los logs de [5.1](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45148295481/job/137602967021) y [PowerShell 7](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45148295481/job/137602966951) constan clonación, importación, publicación y segunda ejecución.
- **Bash/Linux.** [Bloque de la guía en Ubuntu](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45148295481/job/137602967165). También se reprodujo en un segundo entorno Linux con remoto bare, 29 archivos, tres referencias al mismo commit y rechazo de la repetición. macOS solo se revisó documentalmente.
- **GitLab.com.** El navegador llegó al inicio de sesión. Tras el segundo factor de Google, una apertura nueva del proyecto volvió al login. No se observó su contenido ni se realizó escritura desde esta auditoría. La ejecución Windows real figura [omitida](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45148295481/job/137602966517). Para habilitarla, el propietario configura en el entorno Actions `ensayo-gitlab` la variable `GITLAB_ENSAYO_URL` y un secreto de escritura Git de alcance de proyecto y caducidad corta, `GITLAB_ENSAYO_TOKEN`. En la ejecución manual del workflow existente se seleccionan la rama revisada y el ensayo GitLab. El script inspecciona refs y árbol antes del primer push y repite en un clon independiente. El cotejo en la interfaz sigue siendo una comprobación separada.
- **Claude Code.** La CLI oficial 2.1.330 se ejecutó en el entorno de auditoría. `claude auth status` devolvió `loggedIn: false` y `authMethod: none`. No se emitió una petición al modelo. Los documentos simulados del job Git no cuentan como generación, revisión ni autorización.
- **Documentos.** Se localizaron las fuentes Word de los dos manuales del 4 de noviembre. Los originales tenían 34 y 53 páginas. Los manuales corregidos y reexportados tienen 40 y 62. Los bloques completos de comandos, los controles de fase y la repaginación de las fuentes editables explican el cambio. El PDF general sigue en 23 páginas. La portada y las páginas 6–7 se corrigieron. Las otras 20 coinciden píxel a píxel con la versión previa de la guía. Se comprobó lectura estructural, páginas, destinos internos, numeración, marcadores y límites del texto. El material del profesor se entrega en privado.
- **Revisión de los laboratorios.** El auditor comprueba los tres materiales de cada laboratorio, enlaces relativos, entradas en los dos textos de L03 y comandos destructivos en bloques de ejemplo. Las menciones explicativas a opciones prohibidas se conservan. La revisión estática cubre los materiales del curso, no el código que el alumno generará durante el taller.

## Registro histórico de la primera auditoría

**Ámbito:** repositorio de materiales `jaimecopilot/CLAUDE-ALM-GENERATIVO`, laboratorios L01–L11, plantilla y guía general PDF.

**Rama de corrección inicial:** `audit/l02-windows-actions-20261123`, revisión en la [Pull Request #1](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/pull/1). El estado de publicación y merge debe consultarse allí; la auditoría distingue siempre pruebas automáticas de ejecución real en GitLab.

## Evidencia real de GitHub Actions

- [L02 validado en Windows PowerShell 7, Windows PowerShell 5.1 y Bash/Ubuntu, más Git simulado de L03](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions/runs/45138979234). Se utilizan repositorios Git bare locales simulados, sin credenciales ni proyecto GitLab privado.
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

No confundir el éxito de Actions con una prueba de sistema completa. La guía PDF ya se revisó visualmente; queda pendiente la comprobación de autenticación y del flujo real de Claude/GitLab por el formador antes de declarar completada la práctica docente.
