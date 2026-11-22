# L08 · PRÁCTICA: una petición de negocio reabre el ALM

**Continuidad:** utiliza Claude Code sobre los requisitos, diseño, código y tests existentes. Si has empleado Claude web + MCP, sincroniza antes la rama para no sobrescribir cambios. Ver [guía de integración](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md).

**60 min:** cambio/análisis 10, prompt operativo 10, modificación 15, pruebas/CI 15, revisión 10.

## Petición del cliente
«A partir de ahora una reserva de sala no puede durar más de cuatro horas consecutivas. Las reservas de exactamente cuatro horas sí están permitidas. El resto de reglas se mantiene».

No se modifica nada más. Si el equipo quiere añadir excepciones para directivos o fines de semana, se explica que **están fuera de alcance**.

## Paso 1 — crear issue de cambio
Registra en GitLab **CAM-01: limitar duración máxima a cuatro horas** con contexto, criterios de aceptación, prioridad, impacto previsto y relación con requisitos anteriores. Anota el número real de issue.

## Paso 2 — hacer análisis de impacto
Claude debe leer especificación, diseño, implementación y tests actuales. Pídele que liste:
- qué documentos deben actualizarse;
- qué archivos de código están implicados;
- qué pruebas cambian o se añaden;
- qué no necesita cambiar;
- qué incertidumbres requieren aprobación humana.

Si propone reescribir toda la aplicación, solicita una reducción razonada del alcance.

## Paso 3 — generar prompt operativo de evolución
Ejecuta **METAPROMPT.md** y crea **alm/prompts-generados/06-evolucion.md**. Revisa que el prompt haga volver a los requisitos antes de tocar el código, que incluya tests nuevos y que mantenga las reglas de solapamiento y cancelación.

## Paso 4 — ejecutar el cambio
En una rama nueva, autoriza:
1. editar RF/CA afectado y su historia;
2. actualizar diseño/ADR solo si una decisión realmente cambia;
3. incorporar validación de duración máxima;
4. añadir pruebas de 3h59, 4h y 4h01 y ejecutar regresión;
5. revisar docs y README;
6. crear MR asociada a CAM-01.

No debe ajustarse un test antiguo para «acomodar» una regresión.

## Paso 5 — comprobar resultado real
~~~bash
python -m pytest -q
git diff
git status
~~~
Comprueba desde el endpoint real el límite de cuatro horas. Si la base contiene reservas antiguas de mayor duración, **documenta el comportamiento previsto**; no inventes una migración de producción dentro del taller.

## Paso 6 — CI y cierre
Sube cambios, observa pipeline remoto GitLab y registra: issue CAM-01, commits, MR, tests nuevos, pruebas antiguas y estado CI. Si no hay runner, anota bloqueo; no anuncies «CI verde».

**Resultado esperado:** el equipo puede explicar por qué un cambio de negocio vuelve a abrir requisitos, implementación, testing y documentación. Una MR es evidencia del proceso, no solo un mecanismo de subir archivos.
