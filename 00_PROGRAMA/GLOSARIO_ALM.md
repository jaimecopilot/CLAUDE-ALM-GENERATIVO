# Glosario compartido ALM: junior y senior

Este glosario unifica términos en los dos talleres y evita confundir el lenguaje de IA con la ingeniería de software.

| Término | Definición que usaremos | Ejemplo coworking |
|---|---|---|
| Vibe Coding | Construcción y refinamiento exploratorios mediante lenguaje natural con IA | «Hazme un formulario de reservas» |
| LLM | Modelo de lenguaje que genera respuestas, no verificador de verdad por sí mismo | Puede proponer código y documentos |
| Asistente | Sugiere o explica sin necesariamente actuar sobre archivos | Chat explica un error |
| Agente | Con permisos autorizados puede modificar archivos y ejecutar herramientas | Claude Code cambia servicio y test |
| ALM | Gestión del ciclo de vida completo de una aplicación y sus artefactos | RF → test → MR → CI |
| SDLC | Fases del desarrollo del software | Análisis, diseño, código, pruebas, entrega |
| Pipeline ALM | Secuencia de fases y gates, con intercambio de artefactos | Especificación alimenta diseño |
| CI/CD | Jobs automatizados de integración y entrega | pytest en GitLab Runner |
| Metaprompt | Instrucción para producir otro prompt operativo | «lee contrato y redacta el plan de diseño» |
| Prompt operativo | Instrucción detallada sobre entradas, acciones, salidas, validación | «genera diagramas desde RF aprobados» |
| Contrato de fase | Especifica precondiciones, salidas y aceptación de una etapa | docs/requisitos y validación RF |
| Gate | Punto de aprobación humana o automatizada explícita | No avanzar con tests fallidos |
| Requisito funcional (RF) | Comportamiento exigido del sistema | Rechazar reservas solapadas |
| Criterio de aceptación (CA) | Condición observable para aprobar comportamiento | HTTP 409 en solapamiento |
| Gherkin | Formato Dado/Cuando/Entonces para describir escenarios | Reserva duplicada |
| Especificación implementable | Documento suficientemente detallado para implementar y testear; no garantiza éxito | RF/CA y restricciones del MVP |
| Backlog | Trabajo priorizado y ordenado por dependencias | Salas antes de reservas |
| Issue | Registro identificable de trabajo o incidente | RF-03 o CAM-01 |
| ADR | Registro de decisión arquitectónica y sus consecuencias | SQLite y monolito |
| Diagramas como código | Representación textual versionable como Mermaid | Componentes FastAPI y SQLite |
| Rama | Línea de cambios aislada | feature/gestion-reservas |
| Commit | Cambio versionado con autor y mensaje | feat: rechazar solapamientos |
| Merge Request | Propuesta revisable de integración | MR que implementa RF-03 |
| Test unitario | Verificación aislada de función/regla | Intersección de intervalos |
| Test de integración | Verifica interacción de componentes | POST reserva + SQLite |
| Regresión | Reejecución para detectar roturas tras cambio | CAM-01 sin perder cancelación |
| Cobertura | Medida de código ejecutado por tests, no garantía de corrección | Rama de reserva cancelada |
| Job CI | Trabajo concreto de un pipeline | pytest |
| Runner | Ejecutor de jobs de GitLab CI | Contenedor Python autorizado |
| Release | Versión identificada para entrega | MVP etiquetado |
| Trazabilidad | Relación demostrable entre RF, código y pruebas | RF-03 → test → MR |
| Gobernanza | Reglas sobre permisos, supervisión, evidencia y riesgos | Gate y revisión antes de merge |
| Deuda técnica | Coste futuro de compromisos de diseño/calidad | Validaciones duplicadas |
| Cambio de requisito | Nueva necesidad que altera comportamiento esperado | Máximo 4h |
| Bug | Implementación incumple un requisito ya aprobado | Aceptar dos reservas solapadas |
| Refactorización | Cambio de estructura sin cambio funcional previsto | Extraer validador de intervalos |

**Regla pedagógica:** los términos se explican justo antes de utilizarlos en las prácticas; el curso es intensivo, no un diccionario de definiciones para memorizar.