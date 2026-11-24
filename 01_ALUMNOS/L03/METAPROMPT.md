# L03 · METAPROMPT OPERATIVO: construir la fase de requisitos

## Qué debe pasar
Este texto NO solicita «haz la aplicación». Obliga a Claude a **escribir primero un prompt de trabajo**, que un humano revisará y luego ejecutará.

~~~text
Rol: ingeniero de requisitos especializado en ALM generativo.
MODO AHORA: GENERACIÓN DE PROMPT OPERATIVO; no ejecutes todavía la fase.

Lee CLAUDE.md, alm/maestro.md, alm/contratos/01-requisitos.md, alm/metaprompts/01-requisitos.md y docs/instrucciones/CASO_NEGOCIO.md, junto con este metaprompt L03. Lee también evidencias/L01.md y evidencias/L02.md. Haz que el prompt exija una correspondencia entre los hallazgos L01 y las decisiones, descartes o preguntas de la especificación. Detecta qué información del cliente ya está aprobada y qué dudas siguen abiertas.

Produce alm/prompts-generados/01-requisitos.md con estas secciones:
1. Objetivo de la fase e IDs RF-01 a RF-04.
2. Entradas reales y dudas que impiden implementar (máximo seis preguntas).
3. Pasos para generar una especificación funcional y backlog verificables.
4. Archivos de salida docs/requisitos/especificacion.md y docs/requisitos/backlog.md.
5. Criterios: listar, reservar, impedir solapamientos, cancelar; intervalos [inicio,fin), comportamiento observable, casos límite y códigos de error.
   Para RF-04, incluye en la especificación y en la historia de cancelación un criterio de aceptación ya fijado por el taller: cuando DELETE /reservas/{id} cancela una reserva, devuelve HTTP 204 sin cuerpo y la franja queda libre. El formulario confirma la cancelación al recibir el 204, sin leer un mensaje de la respuesta.
6. Exclusiones: pagos, membresías, eventos, autenticación compleja, microservicios.
7. Revisión: escenarios Gherkin verificables, dependencias de historias, trazabilidad a issues.
8. Plan de corrección si falta una regla de negocio.
9. Solicitud de autorización humana antes de ejecutar.

No rellenes campos con supuestos silenciosos; enumera las hipótesis. No declares que has creado issues si no las has creado realmente.
Detente después de guardar el prompt operativo. Deja intacto docs/requisitos/ (ya contiene .gitkeep) y no crees issues; solicita aprobación explícita del Gate A. Antes de cualquier commit o push de artefactos finales, presenta los cambios para el Gate B.
~~~

## Checklist de revisión humana
El alumno revisa el prompt y comprueba que produce documentos versionados y que diferencia «pregunta a stakeholder» de «requisito aceptado». Solo entonces autoriza su ejecución.