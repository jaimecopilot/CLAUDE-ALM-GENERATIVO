# Evaluación del taller junior de ALM generativo — 16 horas

> Documento de evaluación del formador. No presupone que el proyecto GitLab o Claude Code se hayan ejecutado antes del taller.

## Principio de evaluación

Se valora la capacidad de explicar, producir, verificar y conectar artefactos de un ALM generativo. No se califican el número de prompts ni la cantidad de código generado. Una afirmación de Claude no sustituye a una ejecución comprobada.

## Rúbrica (100 puntos)

| Dimensión | Puntos | Evidencias observables |
|---|---:|---|
| Requisitos y criterios de aceptación | 20 | RF-01 a RF-04 identificados; criterios Gherkin verificables; decisiones del stakeholder; backlog e issues |
| MVP funcional | 25 | Listar salas, crear reservas, impedir solapamiento, cancelar; ejecución local y revisiones de código |
| Pruebas y CI/CD | 25 | Tests unitarios/de integración asociados a criterios; logs pytest; GitLab pipeline real o bloqueo identificado |
| Uso de GitLab y control de cambios | 15 | Rama, commits, issues, Merge Request, relación entre cambios y aprobación humana |
| Uso crítico de IA y explicación | 15 | Distingue metaprompt/prompt operativo/artefacto; identifica supuestos; muestra validaciones y riesgos |
| **Total** | **100** | |

## Escala por dimensión

- **Excelente (90–100 % de la dimensión):** evidencia completa, reproducible y explicada; identifica límites y valida cada afirmación.
- **Competente (70–89 %):** cumple lo esencial; hay pequeñas lagunas documentales pero las reconoce.
- **En progreso (50–69 %):** funciona parcialmente o no demuestra la cadena completa; necesita apoyo para explicar artefactos.
- **Insuficiente (<50 %):** no existe prueba verificable del requisito, o confunde generación textual con ejecución.

## Control de evidencias por laboratorio

| Lab | Qué debe inspeccionar el docente | Cómo comprobarlo |
|---|---|---|
| L01 | Supuestos de una petición vaga | Al menos cinco supuestos clasificados y una condición verificable |
| L02 | Proyecto GitLab personal | Cuenta, proyecto privado, tag base-alm y rama de trabajo |
| L03 | RF, CA, backlog e issues | Inspección de Gherkin y enlaces reales de GitLab |
| L04 | Modelo, diagramas y ADR | Rastrear RF-03 en diagrama; ADR con alternativas y consecuencias |
| L05 | API y revisiones de código | Ejecutar caso válido, rechazo 409 y cancelación |
| L06 | Pruebas y correcciones | Ejecutar pytest; cotejar tests con CA; registrar fallos |
| L07 | CI/CD | Ver estado y logs del pipeline asociado a MR/commit |
| L08 | Cambio CAM-01 | 3h59 y 4h permitidas; 4h01 rechazada; regresión |
| L09 | Trazabilidad | Seguir una fila RF → CA → issue → archivo → test → MR |
| L10 | Pipeline ALM automático | JSON, ejecución completa o bloqueo real y comparación de ramas |
| L11 | Defensa final | Demostración individual y explicación de los dos modos |

## Tres tipos de estado que jamás deben confundirse

1. **Ejecutado y verificado:** existe evidencia de comando, resultado o pipeline real.
2. **Ejecutado con fallo:** se conoce el defecto y queda registrado; no se etiqueta como éxito.
3. **No ejecutado por bloqueo:** no hay cuota, permisos, runner o conectividad; puede continuar pedagógicamente con checkpoint, pero la ejecución pendiente no se contabiliza como realizada.

Cuando un bloqueo sea externo al alumno, separar la evaluación de competencia (sabe interpretar logs y definir jobs) de la prueba de infraestructura remota, que no se declarará completada.

## Preguntas de examen oral con respuesta esperada

**¿Qué diferencia hay entre un metaprompt y un prompt operativo?** El metaprompt usa el contrato/contexto para generar la instrucción particular; el prompt operativo se revisa y luego se ejecuta para producir el artefacto de fase.

**¿GitLab CI/CD es todo el ALM?** No. CI/CD automatiza comprobaciones, construcción y entrega; el ALM incluye requisitos, decisiones, mantenimiento, gobierno y trazabilidad.

**¿Por qué no basta con que los tests pasen?** Un test débil puede no observar el requisito; los tests se rastrean hasta CA y se revisan sus aserciones.

**¿Por qué no debemos fusionar automáticamente una MR generada por Claude?** Porque una ejecución técnica no aprueba el comportamiento, seguridad o alcance de negocio; hace falta revisión autorizada.

**¿Qué cambia con CAM-01?** Se actualizan criterios de aceptación, validación de duración, tests y documentación afectada. Solo se cambia arquitectura si existe motivo real.

## Acta breve de evaluación (duplicar por alumno)

| Campo | Resultado |
|---|---|
| Alumno / usuario GitLab | |
| Proyecto GitLab y rama | |
| Versión o commit de demostración | |
| RF/CA | /20 |
| MVP | /25 |
| Pruebas y CI/CD | /25 |
| GitLab y cambios | /15 |
| Uso crítico de IA | /15 |
| **TOTAL** | **/100** |
| Bloqueos externos | |
| Comentarios formador | |

## Cierre

La evaluación debe quedar reproducible con enlaces a evidencias reales, no con una apreciación subjetiva de que «la IA programó muy rápido».