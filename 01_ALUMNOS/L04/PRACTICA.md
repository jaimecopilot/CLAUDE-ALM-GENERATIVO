# L04 · PRÁCTICA: generar y aprobar la arquitectura del coworking

**Herramienta de trabajo:** diseño y ADR pueden crearse con Claude Code o Claude web + MCP a partir de requisitos aprobados. Al alternar herramientas, sincroniza los commits y evita ediciones simultáneas. Ver [guía transversal](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md).

**60 min:** teoría 15, prompt de diseño 10, generación 20, revisión/ADR 10, gate 5.

## Entradas
- Requisitos aprobados de L03, incluidos RF/CA identificados.
- **alm/contratos/02-diseno.md**.
- Stack fijado: FastAPI, SQLite, pytest, una sola API y una UI mínima.
- No hay decisión de autenticación compleja o cloud.

## Paso 1 — inspección del contexto
Abre el contrato de diseño y pregunta a Claude qué documentos son necesarios. Si solicita un documento que no existe, debe comunicar la ausencia y no inventar contenido. Esta comprobación evita «arquitecturas» sin relación con los requisitos reales.

## Paso 2 — metaprompt de arquitectura
Utiliza **METAPROMPT.md** para producir **alm/prompts-generados/02-diseno.md**. Revisa que el prompt solicite una única arquitectura pequeña, su modelo de datos y decisiones trazables, y no un catálogo de cinco arquitecturas.

## Paso 3 — ejecutar el prompt aprobado
Claude producirá:
- **docs/arquitectura/diseno.md**: responsabilidades y restricciones.
- **docs/arquitectura/diagramas.md**: diagramas Mermaid (contexto/contenedores y modelo). Abre el archivo renderizado y comprueba que también está en el commit que vas a publicar.
- **docs/arquitectura/ADR-001.md**: decisión sobre la estructura del sistema y almacenamiento.

El estudiante debe poder explicar las relaciones: *Sala tiene varias Reservas; una Reserva pertenece a una sala, posee inicio, fin y estado*. Comprueba que el tratamiento de reservas solapadas sigue visible.

## Paso 4 — prueba de coherencia del diseño
Pide al compañero que señale en el diagrama dónde se:
1. verifica la existencia de una sala;
2. comprueba el intervalo;
3. rechaza una colisión;
4. cancela una reserva con `DELETE /reservas/{id}`, devuelve 204 sin cuerpo y libera la franja. Es la ruta que comprobarás en L05.

Si no puede ubicar la responsabilidad, el diseño necesita revisión. El ADR debe contener **contexto, alternativas, decisión y consecuencias**; «Claude lo recomienda» no es argumento técnico.

## Paso 5 — aprobar la fase
Guarda el prompt, el diseño, el diagrama y el ADR en la **misma rama `practica/manual`** de L03; registra la revisión y el **Gate B** en **alm/evidencias/registro.md**. **Tras la aprobación**, realiza commit y push de los archivos de diseño, prompt y evidencia, sin modificar `main`. No marques el diseño «aprobado» si la especificación aún tiene dudas bloqueantes.

**Resultado esperado:** la implementación del L05 puede partir del diseño sin redefinir reglas de negocio. **Errores típicos:** patrones innecesarios, módulos inventados, base de datos remota para un taller local, Mermaid que no renderiza, diagrama sin relación con RF-03. Corrige el diseño, no el requisito para justificar el dibujo.
