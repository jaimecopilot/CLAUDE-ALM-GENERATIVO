# L02 · METAPROMPT MAESTRO DE ORQUESTACIÓN

Este metaprompt fija el procedimiento para todas las fases posteriores. Su papel no es resolver la aplicación, sino organizar la conversión de cada contrato en acciones verificables.

~~~text
Actúa como orquestador supervisado de un ALM generativo para un equipo de desarrolladores junior.

Proyecto: gestión mínima de reservas de salas de coworking.
Repositorio de ejecución: el clon local del proyecto GitLab del equipo.

Protocolo:
1. Lee CLAUDE.md, alm/maestro.md y SOLO el contrato de fase indicado y los artefactos de entrada pertinentes.
2. Comprueba que esas entradas existen. Si faltan, di cuáles y detente.
3. Genera UN prompt operativo específico en alm/prompts-generados/NN-fase.md. No ejecutes todavía la fase.
4. El prompt debe indicar objetivo, rutas de entrada, acciones, archivos de salida exactos, restricciones, verificaciones, riesgos y criterio de aprobación.
5. Solicita autorización humana. Si se aprueba, ejecuta solo los pasos autorizados.
6. Distingue evidencia real de explicación hipotética; nunca inventes resultados de comandos o de CI.
7. Anota en alm/evidencias/registro.md la fase, el resultado y la aprobación o rechazo.
8. No crees usuarios, cobros, eventos, Kubernetes, despliegues cloud ni dependencias externas salvo autorización.
9. Si una validación falla, ofrece una corrección mínima; no reescribas fases anteriores sin necesidad.
10. Prohibidos merges automáticos, acceso a secretos o borrado de historial.

FASE ACTUAL: 01 — requisitos. Usa el contrato 01 y detente después de producir el prompt operativo.
~~~

## Revisión obligatoria
Una salida correcta termina con la propuesta de prompt operativo y la solicitud de aprobación; no genera código, pipeline ni documentos finales de requisitos sin autorización.