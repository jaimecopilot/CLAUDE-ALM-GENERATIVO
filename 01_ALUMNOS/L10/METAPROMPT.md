# L10 · METAPROMPT: crear el pipeline ALM declarativo

## Objetivo
Claude debe **generar la configuración ejecutable**, no limitarse a explicar cómo sería el pipeline. El ejecutor Python ya existe y pone las restricciones de seguridad.

~~~text
Eres ingeniero de automatización de ALM generativo.

Tenemos seis contratos de fase en alm/contratos y sus metaprompts correspondientes en alm/metaprompts. A partir de ellos vamos a crear un SEGUNDO MODO de trabajo: pipeline automático local. No cambia el caso Coworking Norte ni sustituye los artefactos por ejemplos hipotéticos.

Lee primero alm/ESPECIFICACION_PIPELINE_AUTO.md y scripts/alm_auto.py, en particular la constante PHASES y la función load_pipeline. Lee CLAUDE.md, alm/maestro.md y los seis contratos y metaprompts.

Crea alm/pipeline_auto.json con EXACTAMENTE el esquema previsto, sin campos adicionales, y con las seis fases en este orden:
01 requisitos → 02 diseno → 03 desarrollo → 04 testing → 05 devops → 06 evolucion.

Para cada fase:
- id y name según la constante PHASES;
- contract = alm/contratos/NN-nombre.md;
- metaprompt = alm/metaprompts/NN-nombre.md;
- prompt_out = alm/prompts-generados/NN-nombre.md;
- outputs = los archivos/globs obligatorios fijados en PHASES.

No ejecutes aún el pipeline ni generes código, requisitos, diseño o pruebas. No modifiques el ejecutor Python ni los seis contratos. No añadas claves, comandos Bash, URLs o acciones de merge/push.

Después de escribir JSON, explica brevemente en lenguaje natural y con un diagrama Mermaid cómo se transmiten los artefactos entre las seis etapas. Indica cómo se bloquea el avance y qué requiere revisión final.
~~~

## Comprobación
El alumno ejecuta \`python scripts/alm_auto.py --plan\`. Un JSON que no supera ese control debe corregirse. La ejecución real solo comienza después de la aprobación global del alumno.