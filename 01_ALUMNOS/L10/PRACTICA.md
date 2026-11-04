# L10 · PRÁCTICA: generar y ejecutar un pipeline ALM automático local

**180 min:** explicación 20, rama limpia 20, generación de pipeline 35, validación del plan 20, ejecución automática 60, revisión/comparación 25.

## Preparación

Necesitas tu propio GitLab con la plantilla del L02, Git configurado, Claude Code CLI autenticado y dependencias Python instaladas. Haber completado L03–L09 en \`practica/manual\` ayuda a interpretar los resultados, pero **no se deben copiar los artefactos de esa rama**.

## Paso 1 — abrir una rama distinta desde la misma plantilla

La etiqueta \`base-alm\` debió guardarse en L02 después de importar la plantilla, antes de generar requisitos o código. Desde la raíz del clon manual:

~~~powershell
git fetch origin --tags
git worktree add ../coworking-alm-auto -b practica/automatica base-alm
cd ../coworking-alm-auto
git status
~~~

Si la rama ya existe, no repitas el comando: abre su directorio de trabajo. Comprueba que aquí están los contratos/metaprompts iniciales pero todavía **no** existen especificaciones o código generados. Este aislamiento permite comparar dos implementaciones independientes de la misma necesidad.

## Paso 2 — generar la configuración de pipeline con Claude

Abre Claude Code en el directorio automático. Pide que lea:
- \`alm/ESPECIFICACION_PIPELINE_AUTO.md\` (esquema y reglas).
- \`alm/contratos/01..06\` y \`alm/metaprompts/01..06\`.
- \`CLAUDE.md\` y \`alm/maestro.md\`.
- el **METAPROMPT.md** de L10 (este laboratorio).

Claude debe crear \`alm/pipeline_auto.json\`. Este es el **artefacto de orquestación que el alumno genera**, no un archivo entregado con la solución.

El JSON define seis etapas en orden y sus entradas/salidas. No permite comandos arbitrarios ni claves de API. Solicita a Claude que te explique el flujo como diagrama Mermaid; el diagrama es una ayuda visual, no una sustitución del archivo ejecutable.

## Paso 3 — validar sin consumir cuota

Ejecuta desde el directorio automático:

~~~powershell
python scripts/alm_auto.py --plan
~~~

El plan comprueba que son seis fases y que los contratos y rutas del JSON coinciden con los del taller. Si falla, corrige la configuración con Claude. **\`--plan\` no llama a la IA ni genera software**.

Antes de ejecutar guarda el JSON en una confirmación versionada si está configurada la rama:

~~~powershell
git add alm/pipeline_auto.json
git commit -m "alm: definir pipeline automatico de seis fases"
~~~

## Paso 4 — ejecutar el pipeline completo

En la misma carpeta, desde PowerShell:

~~~powershell
claude auth status
python -m pip install -r requirements.txt
python scripts/alm_auto.py --run
~~~

El ejecutor pide una sola confirmación: **AUTORIZO**. A partir de ahí invoca a Claude dos veces por fase y avanza automáticamente cuando se cumplen los controles. Verás líneas \`FASE 01\`, \`FASE 02\`, etc. No intervengas modificando manualmente documentos mientras el pipeline esté trabajando.

**Importante:** no definas \`ANTHROPIC_API_KEY\` y no utilices \`--bare\`. Si el CLI informa de cuota agotada, la ejecución se bloquea; no se supone que el plan Pro incluya llamadas ilimitadas.

## Paso 5 — examinar el recorrido

Los artefactos se generan en las mismas rutas que en el modo manual. Consulta:

- \`alm/prompts-generados/\`: prompts operativos realmente generados por Claude.
- \`docs/requisitos/\`, \`docs/arquitectura/\`, \`app/\`, \`tests/\`, \`.gitlab-ci.yml\`.
- \`alm/evidencias/pipeline-automatico.md\`: fases cuya validación técnica mínima terminó.
- \`.alm-run/estado.json\` y \`.alm-run/logs/\`: registro local de fases y llamadas (no subir secretos ni conversaciones enteras).

Ejecuta \`python -m pytest -q\` y revisa \`git diff\`. Las comprobaciones automáticas de existencia y pytest **no demuestran por sí solas** todos los criterios funcionales: coteja al menos RF-03 y CAM-01 con el código generado.

## Paso 6 — cómo recuperarse de un bloqueo

Si una fase falla, el ejecutor detiene las posteriores y escribe el motivo. Conserva el log; corrige el problema en la rama automática bajo revisión humana y ejecuta:

~~~powershell
python scripts/alm_auto.py --resume --run
~~~

No declares fases incompletas como aprobadas. El curso no exige gastar créditos ilimitados para reintentar una y otra vez; el formador puede mostrar una ejecución propia como demostración, claramente diferenciada del resultado del alumno.

## Paso 7 — registrar y observar GitLab

Cuando el resultado sea aceptable, sube esta **rama automática** y abre una MR sin fusionarla:

~~~powershell
git status
git add .
git commit -m "alm: generar coworking mediante pipeline automatico"
git push -u origin practica/automatica
~~~

Si el pipeline generó \`.gitlab-ci.yml\`, GitLab podrá disparar su **pipeline CI/CD** al recibir el push según las reglas de ese archivo. Comprueba los jobs desde GitLab; que el pipeline ALM local haya terminado no acredita una ejecución CI remota.

## Paso 8 — comparar los dos modos

En \`docs/entrega/comparativa-modalidades.md\` registra una tabla:

| Aspecto | Manual L03–L09 | Automático L10 |
|---|---|---|
| Entradas iniciales | Brief de Coworking Norte | El mismo brief |
| Generación de prompts | Fase a fase con aprobación | Orquestada por script |
| Control de avance | Humano por fase | Gates técnicos y revisión final |
| Requisitos, diseño y código | Vínculos reales | Vínculos reales |
| Tests | pytest y CI de la rama manual | pytest y CI de la rama automática |
| Intervenciones humanas | Observadas | Observadas |
| Errores/bloqueos | Observados | Observados |

**Criterio de terminación:** hay un JSON de pipeline creado con Claude, una ejecución o bloqueo **real** con logs, y comparación fundamentada. No se evalúa como éxito completo un pipeline que solo pasó \`--plan\`.

## Advertencia sobre la alternativa remota

Ejecutar Claude dentro de jobs de GitLab y que toda la secuencia ocurra en sus runners sería otra arquitectura: requiere API de Anthropic facturada o proveedor empresarial. Este laboratorio ejecuta el ALM automático **localmente**, pero publica sus artefactos en el GitLab personal del alumno.