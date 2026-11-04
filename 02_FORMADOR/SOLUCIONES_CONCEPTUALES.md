# Orientaciones del formador: respuestas conceptuales y casos de comprobación

> Material de apoyo docente. **No contiene ni sustituye una solución de aplicación completa.** Si los alumnos tienen acceso de lectura a este mismo repositorio, podrán leerlo: nunca guardar aquí credenciales, respuestas privadas o claves de evaluación.

## Modelo de negocio común

Los requisitos del caso son RF-01 (listar salas), RF-02 (crear reserva), RF-03 (rechazar solapamiento de reservas activas de la misma sala) y RF-04 (cancelar para liberar intervalo). El cliente fija intervalo semiabierto [inicio,fin), fechas inequívocas y ausencia de facturación, eventos y autenticación avanzada en el MVP.

## Respuestas conceptuales por fase

### L01 — Vibe Coding

Ejemplos de supuestos que Claude puede inventar: horarios, zona temporal, identidad de solicitante, política de cancelación, persistencia, si se admiten intervalos contiguos, política de salas inexistentes y estados de reserva. No existe un único prompt «correcto»; el aprendizaje es reconocer los supuestos no autorizados.

### L02 — Generación en dos niveles

Metaprompt: fabrica un prompt operativo concreto a partir de contrato y entradas. Prompt operativo: produce artefactos del ALM cuando ha sido aprobado. Debe existir un gate antes de la ejecución y otro antes de avanzar de fase.

### L03 — Requisitos y backlog

Un criterio bueno dice qué estado previo existe, qué acción se realiza y cuál es el resultado observable. Para solapamiento: dada una reserva activa de S1 de 10:00 a 11:00, solicitar S1 de 10:30 a 11:30 debe devolver conflicto y no crear un segundo registro. La solicitud para S2 a la misma hora no debe bloquearse por ese motivo.

### L04 — Diseño

Una arquitectura pequeña puede separar endpoints HTTP, servicio de negocio y persistencia SQLite. Un ADR explica por qué se usa SQLite local y cuáles son sus límites. Una arquitectura que requiera microservicios, Kubernetes y proveedores de terceros sin justificación es incorrecta para este alcance.

### L05 — Implementación

La intersección de dos intervalos [a,b) y [c,d) se produce si a < d y c < b. Esta expresión se aplica a reservas activas de la misma sala. Una solicitud de inicio igual al final de la reserva anterior es contigua, no solapada. Antes de declarar éxito se comprueba el estado de la base, no solo el código HTTP.

### L06 — Pruebas y calidad

Una aserción débil comprueba únicamente que el endpoint responde. Una aserción fuerte comprueba el código, la respuesta y el estado persistido. Los tests deben partir de CA y registrar ejecución real. El protocolo de siete niveles añade revisión de dependencias, requisitos, seguridad y documentación.

### L07 — GitLab CI/CD

El YAML de GitLab describe jobs pero no prueba que se hayan ejecutado. Un pipeline verde exige URL, jobs y logs reales. Si el runner falta, la causa es infraestructura. Si una dependencia falta en requirements, es reproducibilidad. Si pytest falla por un criterio de negocio, es defecto de implementación.

### L08 — Evolución

CAM-01 permite exactamente cuatro horas y rechaza duraciones superiores. Deben probarse 3 h 59 min, 4 h y 4 h 01 min, además de regresión de solapamiento y cancelación. No hay que regenerar sin motivo todo el sistema.

### L09 — Trazabilidad

Una fila válida vincula RF-03, su CA de conflicto, issue real, módulo de reserva, test, commit, MR y ejecución de CI. Si falta la evidencia, anotarlo explícitamente; no completar el cuadro con números inventados.

### L10 — Defensa

El estudiante debe poder explicar qué decisiones y verificaciones hizo él aun cuando Claude haya generado todo el código. La calidad se demuestra con la cadena de evidencias y límites conocidos del MVP.

## Casos de contraste para la demostración

| Estado inicial | Petición | Resultado esperado |
|---|---|---|
| S1 sin reservas | S1 10:00–11:00 | Aceptación |
| S1 reservada 10:00–11:00 | S1 10:30–11:30 | Conflicto (409 según API acordada) |
| S1 reservada 10:00–11:00 | S1 11:00–12:00 | Aceptación por contigüidad |
| S1 reservada 10:00–11:00 | S2 10:30–11:30 | Aceptación si S2 existe |
| S1 reservada 10:00–11:00 y cancelada | S1 10:30–11:30 | Aceptación |
| Sala inexistente | Reserva en esa sala | Error coherente con contrato |
| S1 libre y CAM-01 aplicada | 3 h 59 min | Aceptación |
| S1 libre y CAM-01 aplicada | 4 h 00 min | Aceptación |
| S1 libre y CAM-01 aplicada | 4 h 01 min | Rechazo |

## Errores a evitar durante la docencia

No suministrar la solución como artefacto supuestamente generado por el alumno; no inventar resultados de pytest o GitLab; no corregir una prueba válida para que pase; no otorgar a Claude permiso de merge sin revisión; no presentar la ejecución local como desplegada en producción.

## Ubicación de soluciones técnicas privadas

La solución completa, checkpoints y respuestas sensibles del formador deben custodiarse en un **repositorio privado distinto**, o como archivos locales no compartidos con los alumnos. Las protecciones de rama Git no impiden leer archivos a miembros con acceso. No añadir aquí una implementación final.