# Programa oficial — Taller junior de ALM generativo (16 horas)

## Dos modalidades de ejecución sobre el mismo caso
**Modo A (L01-L09):** los alumnos recorren el ALM fase a fase con Claude Code, revisan cada prompt y validan salidas. **Modo B (L10):** crean la configuración de un **pipeline ALM automático ejecutado por GitLab**; GitLab ejecuta la secuencia con los mismos metaprompts y contratos, guardando estado, logs y bloqueos. **L11:** evalúa resultados de ambas modalidades.

El caso no cambia: Coworking Norte, con listado de salas, creación y cancelación de reservas y prevención de solapamientos. En evolución se incorpora el máximo de cuatro horas.

## Dos jornadas de ocho horas lectivas

| Día | Laboratorio | Min | Entrega |
|---|---|---:|---|
| 1 | L01 Vibe Coding y sus límites | 30 | Identificar supuestos |
| 1 | L02 Cuenta GitLab personal y entorno Claude | 90 | Proyecto privado y plantilla importada |
| 1 | L03 Requisitos generativos | 90 | RF/CA, Gherkin, backlog, issues |
| 1 | L04 Diseño generativo | 60 | Modelo, Mermaid, ADR |
| 1 | L05 Desarrollo guiado | 210 | API de reservas ejecutable |
| 2 | L06 Testing y calidad | 75 | pytest y matriz de pruebas |
| 2 | L07 GitLab CI/CD | 75 | Pipeline y logs |
| 2 | L08 Cambio de requisito | 60 | Regresión y MR |
| 2 | L09 Trazabilidad | 30 | Documentación y matriz |
| 2 | L10 **ALM automático** | 180 | Pipeline ALM ejecutado en otra rama |
| 2 | L11 Defensa comparada y evaluación | 60 | Comparación manual/automático |
| | **Total** | **960** | **16 h** |

Las pausas no forman parte de las horas lectivas.

## Repositorios de cada alumno
1. **GitHub del curso:** teoría, prácticas y metaprompts, solo lectura.
2. **GitLab personal:** cada alumno utiliza su cuenta existente o crea una nueva. Genera proyecto privado `coworking-alm-junior`, importa la plantilla y mantiene dos ramas de trabajo con el mismo punto de partida: `practica/manual` y `practica/automatica`.
3. **Claude Code local:** cada alumno inicia sesión en su propia cuenta con plan compatible. No se copian tokens a prompts ni repositorios.

## Continuidad de artefactos (regla obligatoria)
Las fases NO usan nuevas especificaciones inconexas. Cada contrato declara entradas generadas y aprobadas en las anteriores. Desarrollo utiliza requisitos **y** diseño; testing utiliza requisitos **y** código; CI utiliza código **y** tests; evolución reutiliza todo lo anterior. El pipeline automático parte del mismo brief y aplica exactamente esos contratos en una rama separada.

## Límite de coste
El modo A utiliza Claude Code con la cuenta del alumno. El modo B requiere, además, acceso a la API de Anthropic facturada por tokens y los minutos de runner que correspondan. La modalidad B consume API por tokens en GitLab; la cuota Pro corresponde únicamente a la modalidad interactiva. El presupuesto de API para L10 debe fijarse por separado; no está incluido en el coste de Claude Pro. No se configura `ANTHROPIC_API_KEY` en las prácticas locales.

## Criterios de evaluación
Requisitos 20%, MVP 25%, pruebas y CI 25%, GitLab 15%, explicación crítica 15%. El L11 exige contrastar resultados y evidencias de ambos modos, sin afirmar que el automático pasó si sus gates fallaron.
