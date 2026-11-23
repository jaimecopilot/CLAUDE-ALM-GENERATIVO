# L11 · PRÁCTICA: defensa, evaluación y retrospectiva

**Comparación:** el trabajo guiado del alumno puede utilizar Claude Code y Git, Claude web + MCP, o ambos con sincronización. La rama automática recibida proviene de la ejecución central del formador. No atribuyas a tu GitLab una ejecución ajena. Ver [guía de integración](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md).

**60 min:** preparación 10, demostraciones individuales 36, preguntas cruzadas 9, cierre 5.

## Preparación
Cada alumno prepara una demostración de tres minutos con su GitLab personal. En un grupo de 12 personas, 12 × 3 son 36 minutos. Muestra tu rama **`practica/manual` con todo el trabajo L03–L09, incluido CAM-01** y la copia de la ejecución central del formador en `referencia/alm-automatico`. Antes de la defensa, verifica que ninguna funcionalidad aprobada haya quedado solo en una rama `feature` no integrada. Si existe una rama `practica/automatica` con YAML de estudio, explica que no constituye una ejecución de API. No generes código nuevo durante la defensa.

## Guion obligatorio de demostración
0. **Dos recorridos:** muestra los resultados manual y automático, o el bloqueo real del pipeline GitLab.
1. **Negocio:** muestra RF-03 y explica qué significa solapamiento.
2. **Metaprompt:** señala el metaprompt y el prompt operativo concreto que se generó.
3. **Código:** abre el archivo que implementa la regla.
4. **Test:** ejecuta o muestra el resultado reproducible del caso de colisión.
5. **CI/CD:** abre el pipeline real GitLab y explica qué jobs ejecutó.
6. **Cambio:** muestra CAM-01 y la prueba que distingue exactamente 4 h de 4 h 01.
7. **Traza:** sigue una fila de la matriz hasta la MR.

## Preguntas del formador
- ¿Qué diferencia hay entre el pipeline de ALM y GitLab CI?
- ¿Qué harías si Claude propone una funcionalidad no pedida?
- ¿Qué evidencia tienes de que una prueba pasó?
- ¿Qué harías si falla la CI pero las pruebas locales pasan?
- ¿Cuándo puedes aprobar una fase y cuándo necesitas volver a requisitos?

## Rúbrica común a todos los alumnos
| Criterio | Puntuación |
|---|---:|
| Requisitos y especificación trazable | 20 |
| Funcionalidad real del MVP | 25 |
| Tests y CI/CD verificados | 25 |
| Buen uso de issues, ramas y Merge Requests | 15 |
| Explicación crítica de IA y decisiones | 15 |
| **Total** | **100** |

No se penaliza por fallos de infraestructura ajenos al alumno si están claramente identificados, pero tampoco se les atribuye un resultado remoto que no ocurrió.

## Retrospectiva en 3 preguntas
1. ¿Qué error de Claude detectó una persona o una prueba?
2. ¿Qué fase necesitaría mayor supervisión en un proyecto real?
3. ¿Qué elementos del flujo transferirías a tu trabajo diario y cuáles no?

## Evidencias finales
Repositorio GitLab personal con dos ramas y sus evidencias; issues/commits/MRs; pruebas; CI real o bloqueo documentado; matriz de trazabilidad; versión final y conclusiones.

Antes de presentar, ejecuta `git fetch origin` y `git log -1 origin/practica/manual`. Usa `git ls-tree -r --name-only origin/practica/manual` para localizar especificación, diagramas, aplicación, pruebas, CI de producto, cambio CAM-01 y matriz. Contrasta el SHA con la MR integrada en GitLab y el pipeline que validó ese cambio. Si hubo squash, consulta el SHA resultante de la MR. Comprueba por separado la procedencia de `origin/referencia/alm-automatico`.
