# L02 · PRÁCTICA: crear tu propia cuenta y proyecto GitLab y preparar Claude

**Antes de iniciar L02:** lee la [**guía del alumnado Claude + GitLab + VS Code (PDF)**](../GUIA_ALUMNADO_CLAUDE_GITLAB_VSCODE_ALM_2026.pdf). Instala y comprueba Git, Python, VS Code y Claude Code con tu cuenta Pro siguiendo esa guía. **Este laboratorio comienza verificando herramientas y creando el proyecto GitLab; no exige configurar MCP o `glab` obligatoriamente.**

**Cómo se conectan las herramientas:** GitLab almacena el proyecto; Claude Code trabaja sobre su clon en VS Code y **Git** sincroniza los cambios. Claude web + MCP y GitLab Web IDE son alternativas. Consulta la [guía transversal](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md) antes de comenzar.

**Duración: 90 minutos.** Se trabaja individualmente; no hay repositorios de equipo facilitados por el profesor.

## Objetivo
Utilizar una cuenta GitLab existente o abrir una nueva, crear un **proyecto personal privado**, importar la plantilla del curso y dejar un estado inicial versionado sobre el que podrán ejecutarse dos recorridos ALM: guiado y automático.

La guía técnica completa está en **[GUIA_GITLAB_PASO_A_PASO.md](./GUIA_GITLAB_PASO_A_PASO.md)**. Para Windows, el procedimiento principal utiliza [**Preparar-L02.ps1**](../../scripts/Preparar-L02.ps1), validado en runners Windows por GitHub Actions con dos nombres de proyecto. Copia siempre la URL HTTPS exacta desde GitLab, ejecuta el script con `-Publicar` desde el principio y comprueba en GitLab las dos ramas y la etiqueta. La verificación con GitHub Actions no equivale a verificar permisos del GitLab privado.

## Reloj de la sesión

| Tiempo | Actividad | Evidencia |
|---|---|---|
| 0–15 min | Conceptos cuenta, proyecto, namespace, privacidad y permisos | URL del proyecto personal |
| 15–35 min | Login o registro, verificación y proyecto privado | Proyecto `coworking-alm-junior` |
| 35–60 min | Git y Claude Code; clonar e importar la plantilla | Archivos en el directorio GitLab |
| 60–75 min | Primer commit, tag `base-alm`, rama `practica/manual` | Historial Git visible |
| 75–85 min | Revisar issues, MR y runners e invitar al formador con rol **Developer** | Acceso confirmado |
| 85–90 min | Aprobar la preparación y publicar entrada-l02 | Entorno aprobado o bloqueo |

## Qué tiene que existir al acabar

En GitLab debe existir un repo `TU_USUARIO/coworking-alm-junior`, privado, con `CLAUDE.md`, `alm/`, `docs/`, `app/`, `tests/`. Esos directorios **son plantillas**: ni la especificación ni la API están resueltas.

El tag `base-alm` apunta a la plantilla inicial. `practica/manual` inicia la primera implementación; en L10 se creará `practica/automatica` desde la plantilla y se avanzará hasta la entrega común `entrada-l02`. Este detalle es imprescindible para comparar resultados de forma justa.

## Interpretación de la metodología

Lee el contrato `alm/contratos/01-requisitos.md` y el metaprompt `alm/metaprompts/01-requisitos.md`. Todavía no los ejecutes para generar requisitos. En L03 Claude generará primero el prompt operativo y después la especificación, partiendo del mismo caso de negocio. En L10 estudiarás el pipeline automático de GitLab, que **solo ejecutará el formador**. Recibirás su resultado como referencia en otra rama de tu propio proyecto.

## Entrega común de L01 y L02

Al cerrar la preparación técnica, sitúate en `practica/manual` todavía en `base-alm`. Copia los dos archivos aprobados de L01 en `evidencias/`: `L01.md` y `prompt-L01.md`. Abre el [metaprompt maestro de L02](METAPROMPT.md) en Claude. Genera y revisa `evidencias/prompt-L02.md`. Autoriza su ejecución y revisa `evidencias/L02.md`, con la URL del proyecto, el SHA de la plantilla y las referencias que se han comprobado. Con el resultado aprobado, publica esos cuatro archivos como entrada común. En el primer ensayo de cada proyecto:

~~~sh
git add evidencias/L01.md evidencias/prompt-L01.md evidencias/prompt-L02.md evidencias/L02.md
git diff --cached --stat
git commit -m "docs: entregar exploración y preparación aprobadas"
git tag entrada-l02
git push --atomic origin practica/manual refs/tags/entrada-l02
git ls-remote origin refs/heads/practica/manual refs/tags/entrada-l02
~~~

Las dos referencias deben mostrar el mismo SHA. Si retomas una entrega publicada, comprueba la etiqueta existente y sus archivos antes de seguir. La etiqueta `base-alm` conserva la plantilla inicial. L03 y el recorrido automático de L10 reciben exactamente la versión marcada `entrada-l02`.

## Gate L02
El alumno demuestra la URL real de GitLab, el resultado de `git ls-remote --heads origin` y `git ls-remote --tags origin`, y la rama; comprueba que base-alm contiene la plantilla y que entrada-l02 contiene los cuatro archivos aprobados antes de generar requisitos; el formador revisa que no se haya subido toda la documentación docente a GitLab. El alumno debe **invitarlo con rol Developer** y enviarle la URL de su proyecto, siguiendo el [apartado 7 de la guía](./GUIA_GITLAB_PASO_A_PASO.md#7-invitar-al-formador-como-developer-obligatorio). Si una cuenta o runner no está disponible, registrar el bloqueo: nunca declararlo configurado por suposición.
