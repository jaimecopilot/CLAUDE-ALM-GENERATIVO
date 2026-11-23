# L10 · PRÁCTICA: crear un pipeline GitLab que ejecute los metaprompts

**No confundir L07 y L10:** L10 estudia **Claude Code no interactivo dentro de seis jobs GitLab**. Solo el formador ejecuta el pipeline ALM central con API y presupuesto propios. Los alumnos recibirán la referencia por Git. Ver [arquitectura transversal](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md).

**180 min:** explicación 20, rama/credenciales 20, generar pipeline 45, revisión 25, ejecución y observación 50, comparación 20.

## Preparación
Usa tu proyecto GitLab **personal y privado**, creado en L02. No mezcles la rama manual con la automática. GitHub contiene los contratos y el metaprompt de construcción. El YAML ejecutable se genera en el paso 2 y se revisa antes de publicarlo en el proyecto docente. **Solo el formador ejecutará una vez el ALM automático en su propio GitLab**, con su API y presupuesto. El alumno estudia el pipeline, ve sus logs y recibe una copia del resultado; no debe configurar ni consumir una clave API para este taller.

## Paso 1 — segunda rama desde el mismo estado inicial
~~~bash
git fetch origin --tags
git switch -c practica/automatica base-alm
~~~
La rama de estudio debe tener los seis contratos y metaprompts, pero no las especificaciones/código generados en L03–L09. El resultado compartido llegará a otra rama independiente: `referencia/alm-automatico`.

## Paso 2 — crear el pipeline con Claude
Abre Claude Code sobre esta rama y utiliza [METAPROMPT.md](./METAPROMPT.md). Claude genera el archivo **`.gitlab-ci.yml`** y los scripts de apoyo necesarios. Incluye jobs **alm_requisitos, alm_diseno, alm_desarrollo, alm_testing, alm_devops y alm_evolucion**.

Cada job lee su contrato y metaprompt, genera un prompt operativo y lo ejecuta; los posteriores reciben los archivos reales de las fases anteriores como artefactos. **No se crea una especificación independiente para desarrollo**.

## Paso 3 — revisar antes de publicar
Comprueba rutas y orden, `needs`/artifacts, validaciones de salida, pruebas, uso restringido de permisos, timeout y ausencia de disparos recursivos. El job DevOps genera un YAML de **CI de producto separado**, no sobrescribe el pipeline orquestador activo. No contiene claves ni hace merge automático.

## Paso 4 — configurar credenciales autorizadas
**Solo como aprendizaje para una repetición futura:** una ejecución autónoma utilizaría `ANTHROPIC_API_KEY` como variable enmascarada en **GitLab → Settings → CI/CD → Variables**, usando una clave API personal y presupuesto autorizado. Durante este taller **no tienes que configurar ni pagar API**; la única ejecución la realizará el formador en su proyecto.

## Paso 5 — lanzar desde GitLab
**El formador** ejecutará el pipeline en su GitLab y mostrará sus jobs, logs y artefactos; anota qué recibió cada fase y qué produjo. Después publicará la salida revisada y versionada en la rama `referencia/alm-automatico` de **cada GitLab personal**, usando el acceso Developer que concediste en L02. Recibir estos archivos por Git **no consume Anthropic API** y no sustituye tu rama `practica/manual`. Comprueba la procedencia de la nueva rama y conserva intacto `main`.

## Paso 6 — comparar ambos recorridos
En una tabla final contrasta tu rama guiada y la rama **automática distribuida desde la única ejecución del formador**: la necesidad de partida, los requisitos, el diseño, el código, las pruebas, las intervenciones humanas, los fallos y los costes reales registrados. No atribuyas un resultado GitLab a una simulación local.

**Evidencia final:** YAML del pipeline del curso, ejecución real del formador (o bloqueo documentado), rama `referencia/alm-automatico` distribuida, trazabilidad y comparación de los dos modos. No presentes la copia como si se hubiera ejecutado el pipeline en tu propio GitLab.