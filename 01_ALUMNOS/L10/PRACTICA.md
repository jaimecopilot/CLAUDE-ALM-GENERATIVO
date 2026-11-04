# L10 · PRÁCTICA: defensa, evaluación y retrospectiva

**60 min:** preparación 10, demostraciones 35, preguntas cruzadas 10, cierre 5.

## Preparación
En equipo, prepara una demostración de máximo siete minutos con URL de GitLab y terminal del entorno. Si hay cuatro equipos, la suma de demostraciones es 28 min y quedan siete para incidencias y transición. No generes código nuevo durante la presentación.

## Guion obligatorio de demostración
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

## Rúbrica común a todos los equipos
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
Repositorio GitLab con documentos y código; issues/commits/MRs; pruebas; CI real o bloqueo documentado; matriz de trazabilidad; versión final y conclusiones.
