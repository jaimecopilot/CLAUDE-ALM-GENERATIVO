# L02 · PRÁCTICA: crear tu propia cuenta y proyecto GitLab y preparar Claude

**Duración: 90 minutos.** Se trabaja individualmente; no hay repositorios de equipo facilitados por el profesor.

## Objetivo
Utilizar una cuenta GitLab existente o abrir una nueva, crear un **proyecto personal privado**, importar la plantilla del curso y dejar un estado inicial versionado sobre el que podrán ejecutarse dos recorridos ALM: guiado y automático.

La guía técnica completa está en **[GUIA_GITLAB_PASO_A_PASO.md](./GUIA_GITLAB_PASO_A_PASO.md)**, con las operaciones de GitLab.com y los comandos de PowerShell para Windows. Sigue los pasos en orden.

## Reloj de la sesión

| Tiempo | Actividad | Evidencia |
|---|---|---|
| 0–15 min | Conceptos cuenta, proyecto, namespace, privacidad y permisos | URL del proyecto personal |
| 15–35 min | Login o registro, verificación y proyecto privado | Proyecto \`coworking-alm-junior\` |
| 35–60 min | Git y Claude Code; clonar e importar la plantilla | Archivos en el directorio GitLab |
| 60–75 min | Primer commit, tag \`base-alm\`, rama \`practica/manual\` | Historial Git visible |
| 75–85 min | Revisar issues, MR y runners e invitar al formador con rol **Developer** | Acceso confirmado |
| 85–90 min | Interpretar contrato 01 y registrar gate | Entorno aprobado o bloqueo |

## Qué tiene que existir al acabar

En GitLab debe existir un repo \`TU_USUARIO/coworking-alm-junior\`, privado, con \`CLAUDE.md\`, \`alm/\`, \`docs/\`, \`app/\`, \`tests/\` y \`scripts/\`. Esos directorios **son plantillas**: ni la especificación ni la API están resueltas.

El tag \`base-alm\` apunta a la plantilla inicial. \`practica/manual\` inicia la primera implementación; en L10 se creará \`practica/automatica\` desde el tag. Este detalle es imprescindible para comparar resultados de forma justa.

## Interpretación de la metodología

Lee el contrato \`alm/contratos/01-requisitos.md\` y el metaprompt \`alm/metaprompts/01-requisitos.md\`. Todavía no los ejecutes para generar requisitos. En L03 Claude generará primero el prompt operativo y después la especificación, partiendo del mismo caso de negocio. En L10 estudiarás el pipeline automático de GitLab, que **solo ejecutará el formador**. Recibirás su resultado como referencia en otra rama de tu propio proyecto.

## Gate L02
El alumno demuestra el URL de GitLab y la rama; confirma que el tag base precede a cualquier generación; el formador revisa que no se haya subido toda la documentación docente a GitLab. El alumno debe **invitarlo con rol Developer** y enviarle la URL de su proyecto, siguiendo el [apartado 7 de la guía](./GUIA_GITLAB_PASO_A_PASO.md#7-invitar-al-formador-como-developer-obligatorio). Si una cuenta o runner no está disponible, registrar el bloqueo: nunca declararlo configurado por suposición.
