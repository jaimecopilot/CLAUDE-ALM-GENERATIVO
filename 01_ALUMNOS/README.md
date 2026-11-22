# Material del alumno: teoría + prácticas + metaprompts

Este directorio es el **manual técnico completo del alumno**. No hay que acudir a una guía corta para conocer el contenido: cada uno de los once laboratorios tiene sus archivos `TEORIA.md`, `PRACTICA.md` y `METAPROMPT.md`.

| Laboratorio | Conceptos que se estudian | Entrada a la práctica |
|---|---|---|
| [L01](./L01/TEORIA.md) | Vibe Coding, LLM, asistencia vs agencia, validación | Idea de negocio sin especificar |
| [L02](./L02/TEORIA.md) | ALM as Code, metaprompt y prompt operativo, repositorio | Plantilla GitLab y Claude Code |
| [L03](./L03/TEORIA.md) | Elicitación, historias, criterios Gherkin, issues | Necesidades del coworking |
| [L04](./L04/TEORIA.md) | Diagramas como código, arquitectura, modelo, ADR | Requisitos aprobados |
| [L05](./L05/TEORIA.md) | Generación multiarchivo, API, servicios, revisión | Especificación y diseño |
| [L06](./L06/TEORIA.md) | Tests unitarios/integración, aserciones, 7 validaciones | Código ejecutable |
| [L07](./L07/TEORIA.md) | GitLab CI/CD, runners, pipelines, MRs, release | Tests locales |
| [L08](./L08/TEORIA.md) | Mantenimiento, regresión y propagación de cambios | Requisito de máximo 4 h |
| [L09](./L09/TEORIA.md) | Trazabilidad y documentación viva | Repositorio completo |
| [L10](./L10/TEORIA.md) | **Pipeline ALM automático en GitLab**, jobs, artifacts, logs, presupuestos y comparación | Los seis contratos, metaprompts y brief |
| [L11](./L11/TEORIA.md) | Cierre, evidencia, retrospectiva y responsabilidad | Resultado guiado y automático |

## Cómo se conectan las herramientas

Lee la [**guía transversal Claude Code + Git + GitLab MCP + glab**](./GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md). Aclara qué hace Git frente a MCP, dónde ejecuta pruebas Claude Code y cómo se pasa de una issue a una MR y al pipeline. MCP y `glab` son opciones, no requisitos simultáneos.

## Dos ejecuciones complementarias

**L01–L09 (guiada):** Claude Code con VS Code y Git es el flujo principal para implementar y probar. Claude web + GitLab MCP puede apoyar requisitos, diseño o trabajo remoto. En todos los casos se mantienen dos aprobaciones por contrato. **L10 (automática):** los alumnos revisan el pipeline GitLab que encadena los contratos y metaprompts. El formador realiza **una única ejecución central con Claude API** y distribuye una copia en `referencia/alm-automatico` a cada proyecto privado. **L11:** compara ambas ejecuciones y defiende lo aprendido. No mezclar artefactos de dos ramas para simular continuidad.

## Orden de trabajo por laboratorio

1. **Lee TEORIA.md**, no solo los títulos: contiene explicaciones del concepto y su aplicación concreta.
2. **Lee PRACTICA.md** y sigue los pasos y las comprobaciones, sin saltar fases.
3. **Utiliza METAPROMPT.md** para que Claude elabore el prompt operativo de esa actividad.
4. **Revisa y autoriza** la ejecución: un metaprompt no sustituye al juicio del desarrollador.
5. **Guarda en GitLab** el resultado real y enlaza issue, commit, test y MR cuando existan.

## Qué no debes entregar

No se entregan soluciones cerradas ni capturas fingidas de GitLab. El código, la especificación y los logs serán producidos en clase. Si no hay accesos a GitLab, el docente señalará claramente qué parte es local o simulada.

## Material complementario

Consulta el [glosario ALM](../00_PROGRAMA/GLOSARIO_ALM.md) y el contenido completo de cada laboratorio.
