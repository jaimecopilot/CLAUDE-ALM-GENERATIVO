# Itinerario — Taller ALM generativo con Claude y GitLab (16 horas)

**Cuatro jornadas de cuatro horas.** Un mismo programa para grupos junior y senior, ajustando profundidad, complejidad y autonomía.

## Estrategia

El caso práctico único es Coworking Norte: salas, reservas, prevención de solapamientos y cancelación. En la evolución CAM-01 se limita la duración máxima a cuatro horas.

**Modo guiado (L01–L09).** Cada alumno utiliza Claude Code en su ordenador y su GitLab personal privado. Genera un prompt operativo a partir del metaprompt y del contrato de fase, revisa el resultado y lo valida con evidencias. Todas las fases consumen los artefactos aprobados de las anteriores.

**Modo automático (L10).** Los alumnos estudian y revisan la definición GitLab CI/CD que ejecuta seis jobs generativos. **Solo el profesor realiza una ejecución central en su propio proyecto GitLab con su Anthropic API key**, previa validación técnica y autorización del presupuesto. Distribuye después el resultado versionado a los proyectos privados de los alumnos mediante la rama `referencia/alm-automatico`. Esta copia no consume API y no representa doce ejecuciones independientes.

**Cierre (L11).** Comparación de resultados propios con la referencia central, trazabilidad y defensa.

## Distribución en cuatro jornadas

| Jornada | Actividades | Resultado verificable |
|---|---|---|
| **1** | L01 Vibe Coding, L02 cuentas y herramientas, L03 requisitos e introducción a L04 | GitLab personal con plantilla, tag `base-alm`, rama `practica/manual`, necesidades y criterios de aceptación |
| **2** | Final de L04 diseño y L05 desarrollo iterativo | Arquitectura/ADR y aplicación con reservas, validación y cancelación |
| **3** | L06 testing, L07 CI/CD del producto, L08 cambio, L09 trazabilidad | Tests, logs GitLab cuando existan, evolución CAM-01 y matriz de trazabilidad |
| **4** | L10 orquestación ALM automática, L11 comparación y evaluación | Pipeline central real si ha sido validado, artifacts versionados, rama de referencia y defensa |

La profundidad de los laboratorios se ajusta por nivel: juniors reciben instrucciones y comprobaciones guiadas; seniors estudian decisiones de diseño, concurrencia, seguridad, gobierno, riesgos y costes.

## Trabajo con GitLab

Cada alumno crea un proyecto privado `coworking-alm-junior`, copia exclusivamente la carpeta `03_GITLAB_PLANTILLA` desde GitHub, crea el primer commit, el tag `base-alm` y la rama `practica/manual`. Invita al profesor con rol **Developer** mediante Manage → Members → Invite members y le envía la URL del proyecto. El profesor escribirá solo en la rama `referencia/alm-automatico`; no toca `main` ni el trabajo individual.

## Condiciones de calidad y preparación

El pipeline normal de **CI/CD del producto** (L07) no equivale al **pipeline de ALM generativo** (L10). GitLab gestiona issues, ramas, Merge Requests y jobs; Claude genera propuestas y artefactos, que requieren revisión. Nunca se afirman pruebas o pipelines ejecutados sin logs reales.

Antes del taller se comprueban Git, Python, editor, autenticación Claude Code, cuentas GitLab y runners. El formador debe validar por separado su acceso a GitLab, la clave Anthropic API protegida, su presupuesto, el pipeline central y la publicación de artifacts. **El archivo de metaprompt por sí solo no constituye un pipeline probado.**
