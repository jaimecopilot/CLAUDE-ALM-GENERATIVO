# L03 · PRÁCTICA: generar requisitos, Gherkin e issues en GitLab

**Herramienta de trabajo:** requisitos y Gherkin pueden generarse con Claude Code o con Claude web + MCP. Ambas vías deben leer los mismos contratos y dejar el prompt operativo guardado antes de producir documentos. Si alternas herramientas, sincroniza la rama; ver [guía transversal](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md).

**90 min:** teoría 20, preguntas y contrato 15, generación 25, revisión/GitLab 20, gate 10.

## Entrada de negocio común (no es la especificación final)
«Coworking Norte dispone de varias salas. Necesitamos ver las salas, reservarlas por intervalo y cancelarlas. Dos clientes no pueden ocupar la misma sala a la vez. Queremos algo sencillo que funcione como prototipo interno».

El formador hace de cliente y responde a las cuestiones sobre formato horario, existencia de salas, códigos de error y conservación de cancelaciones. Los alumnos documentan las respuestas. No se añaden pagos, login ni eventos.

## Paso 1 — abre el contrato (10 min)
Localiza **alm/contratos/01-requisitos.md** y explica al compañero por qué describe *qué archivos debe producir Claude* y no *cuál es la especificación ya decidida*. Comprueba el directorio **alm/prompts-generados/** y reutiliza el prompt creado en L02 si supera la checklist.

## Paso 2 — preguntas de elicitación (10 min)
Pide a Claude que enumere **máximo seis preguntas críticas**, no cincuenta. Selecciona las que bloquean la implementación y pide respuesta al formador. Escribe decisiones e hipótesis en un apartado propio de **docs/requisitos/especificacion.md** cuando se ejecute la fase. No ocultes decisiones sin responder: márcalas como pendiente, y no avances si impiden implementar.

## Paso 3 — ejecuta la fase de requisitos (15 min)
Aprueba el prompt operativo y solicita a Claude generar **docs/requisitos/especificacion.md** y **docs/requisitos/backlog.md**, siguiendo los límites del contrato. Deben figurar RF-01..RF-04, historias de usuario, casos felices y de error, validaciones, formatos de petición/respuesta y criterios Gherkin identificados.

~~~gherkin
Escenario: rechazar reserva solapada
  Dado que existe una reserva activa para la sala S1 de 10:00 a 11:00
  Cuando se pide reservar S1 de 10:30 a 11:30
  Entonces no se crea la reserva
  Y se devuelve un conflicto HTTP 409
~~~

Este escenario sirve de referencia docente; el alumno debe producir el conjunto completo y comprobarlo.

## Paso 4 — revisión cruzada (15 min)
Intercambia el documento con otro equipo. El revisor busca contradicciones: ¿qué significa cancelar?, ¿se permiten reservas contiguas?, ¿qué hace el sistema con una sala desconocida?, ¿cómo rechaza intervalos inválidos?, ¿qué pasa con las diferencias horarias? Exige una mejora por observación y corrige el documento. Guarda una breve nota de revisión.

## Paso 5 — issue y prioridad GitLab (15 min)
Crea de forma manual una **issue por historia implementable**, con título, descripción, Gherkin, alcance técnico aproximado y etiquetas del equipo. Las issues deben estar ordenadas por dependencias. En la especificación, anota enlaces reales a las issues o «pendiente de acceso remoto» si GitLab no está disponible. No inventes números de issue.

## Paso 6 — gate de calidad (10 min)
Comprueba y registra:
- RF-01..RF-04 y criterios etiquetados.
- Escenarios de éxito, límite y fallo.
- Ausencia de nuevas funcionalidades fuera del MVP.
- Decisiones de negocio validadas por el formador.
- Vinculación entre backlog e issues reales o pendiente explícito.

**Evidencia:** commit que añada requisitos y backlog, más la referencia a issues y el prompt operativo usado. **Salida a L04:** únicamente la especificación aprobada, no todo el historial del chat.

## Si no llega la cuota de Claude
No se generan más variantes. Se utiliza la especificación de referencia entregada por el docente como **checkpoint externo**, marcado como tal y sin fingir autoría del equipo.
