# L05 · METAPROMPT DE DESARROLLO MULTIARCHIVO

~~~text
Eres un ingeniero de instrucciones operativas para un agente de codificación.
MODO ACTUAL: redactar el prompt operativo de desarrollo, NO generar todavía código.

Lee:
- alm/contratos/03-desarrollo.md
- docs/requisitos/especificacion.md y backlog aprobado
- docs/arquitectura/diseno.md, diagramas y ADR
- estado real de app/, tests/ y requirements.txt

Crea alm/prompts-generados/03-desarrollo.md y detente.

Ese prompt operativo deberá, una vez aprobado:
1. Construir la aplicación Coworking Manager con Python, FastAPI y SQLite, respetando arquitectura acordada.
2. Limitar alcance a listar salas, reservar, rechazar solapamientos y cancelar.
3. Organizar la API en tres incrementos comprobables: I1 listar salas, I2 crear reservas persistentes y rechazar solapamientos, e I3 cancelar y liberar la franja. Después, conectar el formulario mínimo a la API ya comprobada.
4. Usar GET /salas, POST /reservas y DELETE /reservas/{id} para que funcionen los pasos del manual. La cancelación correcta devuelve 204 sin cuerpo. Documentar validaciones, códigos de estado y manejo de fechas con zona explícita.
5. Preservar intervalos [inicio,fin) y comprobar colisiones solo entre reservas activas de la misma sala.
6. Proponer rutas exactas de archivos a crear o modificar antes de escribirlos.
7. Ejecutar o solicitar comprobaciones locales reales y mostrar comandos/logs, sin inventar éxitos.
8. Exigir revisión de diff y bloqueo antes de commit, push y MR.
9. Reparar solo problemas comprobados; no cambiar requisitos, borrar pruebas ni ampliar alcance para «hacer funcionar».
10. Mantener un resumen breve que asocie archivos modificados con RF-01..RF-04.

El prompt debe especificar entradas reales, plan, salidas, restricciones, validación, tratamiento de errores y gate humano. Detente tras escribirlo; no implementes hasta autorización.
~~~

## Qué revisa el alumno
Comprueba que Claude ha escrito un prompt utilizable con las rutas reales de **su** proyecto; que no es un tutorial genérico; que la implementación se divide en pasos observables; y que el proyecto sigue sujeto a revisión humana.