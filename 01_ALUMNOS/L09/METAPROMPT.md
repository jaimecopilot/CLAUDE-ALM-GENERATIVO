# L09 · METAPROMPT: documentación y trazabilidad del ALM ejecutado

~~~text
Actúa como diseñador de un prompt de documentación «as built» y trazabilidad.
MODO: genera el prompt operativo, no reescribas todavía la documentación.

Lee el proyecto real: docs/requisitos/, docs/arquitectura/, app/, tests/, docs/calidad/, docs/entrega/, alm/evidencias/ y referencias de GitLab disponibles.

Escribe alm/prompts-generados/07-documentacion.md para que Claude, tras aprobación humana:
1. Actualice README.md a partir de comandos y rutas reales.
2. Compare diagramas de diseño y estructura del código actual.
3. Actualice docs/arquitectura/diagramas.md o registre discrepancias justificadas.
4. Genere docs/trazabilidad/matriz.md enlazando RF/CA/CAM, issues, archivos, tests, MRs, pipelines.
5. Distinga cualquier evidencia local de evidencia remota en GitLab.
6. Etiquete como PENDIENTE lo que no pueda comprobar, sin inventar URLs o estados.
7. Resuma qué material es salida de Claude y qué fue aprobado por personas.
8. Registre una revisión humana sobre exactitud y completitud.

No alteres funcionalidades de negocio ni vuelvas a generar toda la aplicación. Detente tras preparar el prompt operativo.
~~~

## Verificación
Se aprueba si el prompt produce documentación contrastable con el repositorio real, no una descripción idealizada.