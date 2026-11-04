# L04 · PRÁCTICA: generar y aprobar la arquitectura del coworking

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
- **docs/arquitectura/diagramas.md**: diagramas Mermaid (contexto/contenedores y modelo).
- **docs/arquitectura/ADR-001.md**: decisión sobre la estructura del sistema y almacenamiento.

El estudiante debe poder explicar las relaciones: *Sala tiene varias Reservas; una Reserva pertenece a una sala, posee inicio, fin y estado*. Comprueba que el tratamiento de reservas solapadas sigue visible.

## Paso 4 — prueba de coherencia del diseño
Pide al compañero que señale en el diagrama dónde se:
1. verifica la existencia de una sala;
2. comprueba el intervalo;
3. rechaza una colisión;
4. cancela una reserva.

Si no puede ubicar la responsabilidad, el diseño necesita revisión. El ADR debe contener **contexto, alternativas, decisión y consecuencias**; «Claude lo recomienda» no es argumento técnico.

## Paso 5 — aprobar la fase
Guarda el prompt, el diseño, el diagrama y el ADR en una rama; registra revisión y gate en **alm/evidencias/registro.md**. No marques el diseño «aprobado» si la especificación aún tiene dudas bloqueantes.

**Resultado esperado:** la implementación del L05 puede partir del diseño sin redefinir reglas de negocio. **Errores típicos:** patrones innecesarios, módulos inventados, base de datos remota para un taller local, Mermaid que no renderiza, diagrama sin relación con RF-03. Corrige el diseño, no el requisito para justificar el dibujo.
