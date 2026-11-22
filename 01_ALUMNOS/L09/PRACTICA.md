# L09 · PRÁCTICA: unir todas las piezas del ALM

**Evidencias:** los enlaces a issues, MR y pipelines deben ser reales. GitLab web, MCP o `glab` permiten consultarlos; Git gestiona los commits del clon. Ver [guía transversal](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md).

**30 min:** teoría 5, generar documentación 10, trazar 10, revisión/gate 5.

## Paso 1 — recuperar evidencias verdaderas
Recupera RF/CA de L03, diagrama/ADR de L04, archivos y commit de L05, tests y resultados de L06, CI de L07 y cambio CAM-01 de L08. No uses pantallazos fabricados.

## Paso 2 — metaprompt y prompt de documentación
Utiliza **METAPROMPT.md** para generar **alm/prompts-generados/07-documentacion.md**. En esta fase la numeración 07 es un paso de cierre documental y no altera la secuencia principal de seis contratos ALM. El prompt debe leer archivos existentes, no inventar componentes, y producir un README útil y una matriz de trazabilidad.

## Paso 3 — generar y revisar README
Claude actualiza **README.md** del proyecto GitLab: propósito, límites del MVP, requisitos para instalar, comandos de ejecución de API, prueba con pytest, alcance de CI y limitaciones conocidas. El alumno ejecuta al menos un comando del README y corrige cualquier desajuste.

## Paso 4 — matriz de extremo a extremo
Genera **docs/trazabilidad/matriz.md** con estas columnas:
| RF/CAM | CA | Issue real | Archivo(s) | Test(s) | MR real | Pipeline/estado |
|---|---|---|---|---|---|---|
| RF-03 | CA-03-* | ... | ... | ... | ... | ... |
| CAM-01 | CA-CAM-* | ... | ... | ... | ... | ... |

Los puntos suspensivos se reemplazan por pruebas reales o la palabra **pendiente** con motivo. La tabla debe poderse seguir desde una necesidad hasta la ejecución que la valida.

## Paso 5 — revisar diagramas y ADR
Pide a Claude comparar el diagrama original con los módulos actuales. Identifica toda diferencia con explicación. No atribuyas al ADR una decisión que nadie tomó; si se añadió una capa diferente, se documenta la decisión o se corrige el dibujo.

## Paso 6 — cierre y evidencia
Guarda matriz, README y diferencias de diseño. Si falta prueba remota, deja esa celda marcada. Presenta al compañero una fila completa de trazabilidad y pídele que llegue desde el requisito hasta el test concreto.

**Criterio de fin:** el alumno sabe reconstruir el ciclo de una funcionalidad sin consultar el historial del chat. La documentación se basa en el código real.
