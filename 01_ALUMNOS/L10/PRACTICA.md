# L10 · PRÁCTICA: crear un pipeline GitLab que ejecute los metaprompts

**180 min:** explicación 20, rama/credenciales 20, generar pipeline 45, revisión 25, ejecución y observación 50, comparación 20.

## Preparación
Usa tu proyecto GitLab **personal y privado**, creado en L02. No mezcles la rama manual con la automática. Comprueba con el formador que existe acceso a Anthropic API con límite de gasto, o que la ejecución se realizará como demostración en un proyecto docente controlado.

## Paso 1 — segunda rama desde el mismo estado inicial
~~~bash
git fetch origin --tags
git switch -c practica/automatica base-alm
~~~
La rama debe tener los seis contratos y metaprompts, pero no las especificaciones/código generados en L03–L09.

## Paso 2 — crear el pipeline con Claude
Abre Claude Code sobre esta rama y utiliza [METAPROMPT.md](./METAPROMPT.md). Claude genera el archivo **`.gitlab-ci.yml`** y los scripts de apoyo necesarios. Incluye jobs **alm_requisitos, alm_diseno, alm_desarrollo, alm_testing, alm_devops y alm_evolucion**.

Cada job lee su contrato y metaprompt, genera un prompt operativo y lo ejecuta; los posteriores reciben los archivos reales de las fases anteriores como artefactos. **No se crea una especificación independiente para desarrollo**.

## Paso 3 — revisar antes de publicar
Comprueba rutas y orden, `needs`/artifacts, validaciones de salida, pruebas, uso restringido de permisos, timeout y ausencia de disparos recursivos. El job DevOps genera un YAML de **CI de producto separado**, no sobrescribe el pipeline orquestador activo. No contiene claves ni hace merge automático.

## Paso 4 — configurar credenciales autorizadas
La integración documentada requiere `ANTHROPIC_API_KEY` como variable CI/CD de GitLab, enmascarada y restringida. **No está incluida en Claude Pro**: necesita un presupuesto API separado. Si no hay financiación o permiso, se completa la revisión del YAML y se documenta **NO EJECUTADO**, sin fingir que GitLab ha llamado a Claude.

## Paso 5 — lanzar desde GitLab
Tras commit y push del YAML a la rama automática, abre **GitLab → Build → Pipelines → New pipeline**; selecciona esa rama y ejecútalo. Observa cada job y descarga los resultados. GitLab mostrará logs y fallos; si las pruebas fallan, no se aprobará la fase siguiente. Anota qué artefactos recibió cada job y qué produjo.

## Paso 6 — comparar ambos recorridos
En una tabla final contrasta la rama guiada y la automática: la necesidad de partida, los requisitos, el diseño, el código, las pruebas, las intervenciones humanas, los fallos y los costes reales registrados. No atribuyas un resultado GitLab a una simulación local.

**Evidencia final:** YAML generado con Claude, revisión de arquitectura, GitLab pipeline y sus artefactos reales cuando esté financiado, y comparativa verificable de dos modos.