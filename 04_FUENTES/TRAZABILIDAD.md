# Trazabilidad de contenidos al repositorio fuente

**Origen revisado:** https://github.com/jaimecopilot/ia-alm-2026 (nueve módulos de teoría, prácticas y metaprompts). **Destino:** este repositorio, taller junior 16h. No se ha modificado el original.

## Principio editorial
No se reutilizan los nueve módulos como nueve clases independientes: las prácticas originales son numerosas y varias están redactadas como **instrucciones al formador para generar ejercicios**. Aquí se reestructuran en **diez laboratorios que son fases de un único caso**. El alumno recibe teoría original reproducida y explicación aplicada, práctica ejecutable y metaprompt **operativo** que no resuelve la aplicación hasta aprobación humana.

## Correspondencia de ejercicios principales

| Laboratorio nuevo | Conceptos del origen | Archivo original exacto | Qué cambiamos para el taller |
|---|---|---|---|
| L01 | M1: fundamentos de IA, prompt engineering y riesgos; M9: fundamentos ALM | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-1-fundamentos/meta-prompts/p1.2-comparacion-estilos.md) · `modulo-1-fundamentos/meta-prompts/p1.2-comparacion-estilos.md` | Comparar un prototipo generado desde una petición vaga con una petición refinada; no usar seis conversaciones distintas |
| L02 | M1: herramientas; M8: gobierno; M9: agentes | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo%209/p9.4b.md) · `modulo 9/p9.4b.md` | Mostrar el papel de Claude Code como agente, protocolo de metaprompt y diferencia con GitLab CI |
| L03 | M2: elicitación, generabilidad, backlog, trazabilidad | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-2-analisis-requisitos/meta-prompts/p2.1-idea-a-especificacion-ejecutable.md) · `modulo-2-analisis-requisitos/meta-prompts/p2.1-idea-a-especificacion-ejecutable.md` | Del brief a especificación revisada, Gherkin, issues reales; preguntas al formador como stakeholder |
| L03 | M2: backlog detallado | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-2-analisis-requisitos/meta-prompts/p2.2-especificacion-a-backlog.md) · `modulo-2-analisis-requisitos/meta-prompts/p2.2-especificacion-a-backlog.md` | Descomposición RF → historias con criterios y orden por dependencias |
| L03 | M2: trazabilidad | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-2-analisis-requisitos/meta-prompts/p2.6-requisito-a-issue-trazabilidad.md) · `modulo-2-analisis-requisitos/meta-prompts/p2.6-requisito-a-issue-trazabilidad.md` | Adaptación a GitLab Issues; no simulaciones de otras plataformas |
| L04 | M3: decisiones arquitectónicas | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-3-diseno-software/meta-promts/p3.5%20documentar%20con%20ADRs.md) · `modulo-3-diseno-software/meta-promts/p3.5 documentar con ADRs.md` | Generación de ADR acotado, diagrama Mermaid y modelo de datos desde requisitos aprobados |
| L05 | M4: API y desarrollo multiarchivo | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-4-desarrollo-codificacion/meta-promts/p4.2-%20crud%20api%20rest.md) · `modulo-4-desarrollo-codificacion/meta-promts/p4.2- crud api rest.md` | MVP de reservas con FastAPI, revisión por incrementos, sin exponer solución al alumno |
| L05 | M4: ciclo completo de código | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-4-desarrollo-codificacion/meta-promts/p4.8-ciclo%20completo.md) · `modulo-4-desarrollo-codificacion/meta-promts/p4.8-ciclo completo.md` | Plan → código → validación → diff → tests → documentación |
| L06 | M5: tests desde requisitos | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-5-testing%20y%20calidad/meta-promts/p5.6-ciclo%20completo.md) · `modulo-5-testing y calidad/meta-promts/p5.6-ciclo completo.md` | Criterios Gherkin → tests pytest → logs reales → corrección supervisada |
| L06 | M8: validación en 7 niveles | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-8-riesgos%20y%20buenas%20practicas/meta-promts/p8.4-protocolo%20validacion.md) · `modulo-8-riesgos y buenas practicas/meta-promts/p8.4-protocolo validacion.md` | Aplicación del protocolo a un cambio generado y revisión humana |
| L07 | M6: pipelines por IA | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-6-ia%20en%20devops/meta-promts/p6.1-pipeline%20lenguaje%20natural.md) · `modulo-6-ia en devops/meta-promts/p6.1-pipeline lenguaje natural.md` | Traducir lenguaje natural a GitLab CI real, sin GitHub Actions ni cloud de pago |
| L07 | M6: diagnóstico de fallos | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-6-ia%20en%20devops/meta-promts/p6.3-diagnostico%20fallos%20cdci.md) · `modulo-6-ia en devops/meta-promts/p6.3-diagnostico fallos cdci.md` | Analizar logs reales de CI y corregir sin desactivar pruebas |
| L08 | M7: mantenimiento y refactorización | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-7-mantenimineto%20software/meta-promts/p7.4-refactorizacion.md) · `modulo-7-mantenimineto software/meta-promts/p7.4-refactorizacion.md` | Cambio funcional CAM-01; propagación por especificación, código, pruebas y CI |
| L09 | M8: documentación y gobernanza | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-8-riesgos%20y%20buenas%20practicas/meta-promts/p8.8-documentacion.md) · `modulo-8-riesgos y buenas practicas/meta-promts/p8.8-documentacion.md` | Documentación as-built y matriz enlazada con archivos, tests, issues y MRs |
| L10 | M8: retrospectiva y cierre | [Abrir en GitHub](https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-8-riesgos%20y%20buenas%20practicas/meta-promts/p8.10-retrospectiva%20y%20cierre.md) · `modulo-8-riesgos y buenas practicas/meta-promts/p8.10-retrospectiva y cierre.md` | Demostración sin métricas inventadas, retrospectiva y evaluación del flujo |

## Referencias teóricas
Los archivos **01_ALUMNOS/Lxx/TEORIA.md** incluyen secciones de contexto aplicadas y los **textos completos** de los capítulos del original que sustentan cada laboratorio, con su enlace y ruta. Los nombres no se han inventado: fueron leídos de la rama main del repositorio fuente.

## Qué hemos excluido intencionalmente
- Ejercicios aislados con comparativas de múltiples IAs para cada fase: duplican cuota sin mejorar el objetivo de 16 h.
- Kubernetes, infraestructura cloud, Terraform y Bicep: fuera del MVP y de los recursos junior.
- GitLab Duo, GitHub Actions y agentes de múltiples proveedores como requisito de ejecución: la herramienta fijada es Claude Code y el repositorio de ejecución es GitLab.
- Pruebas de despliegue de producción, seguridad empresarial, facturación y autenticación: no son entregables del caso de 16h.
- Generación de manuales durante la jornada: el alumno estudia el material publicado y utiliza Claude para ejecutar ALM.

## La cadena generativa que conserva la intención de los metaprompts
1. Metaprompt de fase (instrucción de segundo orden).
2. Prompt operativo generado con el estado y contratos actuales.
3. Aprobación humana del plan.
4. Artefactos ALM generados en rutas concretas.
5. Pruebas y evidencias registradas.
6. Aprobación humana de resultado; inicio de fase posterior.

**Esto no implica** que Claude Code y GitLab estén conectados como servicio desatendido: Claude trabaja sobre el clon y GitLab registra/ejecuta CI conforme a sus permisos y runners.