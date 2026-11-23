# L01 · PRÁCTICA: dos maneras de pedir lo mismo

**Duración: 30 min.** 5 para la petición inicial, 5 para revisar supuestos, 15 para los criterios y 5 para el cierre.

## Objetivo y precondición
Comprender mediante una experiencia pequeña por qué el ALM generativo necesita especificaciones y validaciones. Para esta demostración puedes usar Claude web o Claude Code. El manual muestra la vía de Claude Code en un directorio temporal. En las prácticas posteriores, consulta la herramienta indicada en cada laboratorio. No subir datos reales a ningún modelo.

## Actividad A — petición vaga (5 min)
Introduce exactamente esta petición: «Crea un sistema web para gestionar reservas de salas de coworking». Pide una implementación pequeña, sin complicar el entorno. No entregues todavía las reglas de negocio. Si se genera una aplicación ejecutable, intenta reservar dos veces la misma sala a la misma hora, cancelar y volver a reservar, e introducir un intervalo invertido. Registra qué ocurre en cada caso.

Anota en una tabla: ¿qué atributos tiene una sala?, ¿cómo se representa la reserva?, ¿hay persistencia?, ¿impide reservas simultáneas?, ¿qué hace cuando falta un campo?, ¿qué pruebas propone? **No marques como verificado algo que solo aparece en la explicación de Claude.**

## Actividad B — identificar las decisiones implícitas (5 min)
Revisa el resultado anterior. Solicita: «enumera todos los supuestos de negocio que has introducido sin que te los pidiera; clasifica cada uno en decisión explícita, supuesto y duda pendiente». El alumno debe encontrar al menos cinco. Compara con la respuesta de otro compañero.

## Actividad C — petición con criterios (15 min)
Abre [METAPROMPT.md](METAPROMPT.md). Abre una conversación nueva y pega el bloque de texto completo como primer mensaje, con tus notas de A y B. Así podrás enlazar por separado el prototipo inicial y la ejecución del metaprompt. La primera respuesta debe ser un prompt de exploración de menos de 500 palabras. Guárdalo en `evidencias/prompt-L01.md`. Revisa que pida supuestos, propuesta mínima, tres errores y una tabla de observado, supuesto y pendiente. Si requiere correcciones, revisa la nueva versión antes de aprobarla.

En el mismo hilo escribe «Apruebo este prompt. Ejecútalo sobre el prototipo observado y entrégame los resultados». Para delimitar los criterios, fija exclusivamente cuatro comportamientos: listar salas, crear una reserva, rechazar solapamientos y cancelar una reserva. No habrá autenticación, facturación ni eventos. Pide a Claude que prepare una lista de criterios Gherkin de comportamiento observable; **todavía no es el análisis formal del laboratorio L03**.

Ejemplo esperado de criterio:
~~~gherkin
Dado que la sala S1 tiene una reserva de 10:00 a 11:00
Cuando intento reservar S1 de 10:30 a 11:30
Entonces el sistema rechaza la nueva reserva y conserva la original
~~~

Compara ambas peticiones. ¿Qué cambió de manera demostrable y qué sigue sin comprobarse?

## Actividad D — evidencia y cierre (5 min)
Crea el archivo **evidencias/L01.md** (en el cuaderno del equipo o repositorio local) con cuatro apartados: petición inicial, supuestos detectados, criterios revisados y tres riesgos. Incorpora la tabla de exploración, referencia el prompt guardado y los mensajes de generación, aprobación y ejecución. Identifica cada hallazgo como L01-01, L01-02, etc. Entrega el cuaderno y el prompt al comenzar L02. Registra la herramienta utilizada; no es necesario copiar conversaciones completas ni consumos personales.

**Criterio de terminación:** el alumno puede explicar Vibe Coding, ALM, metaprompt, prompt operativo, artefacto y evidencia usando ejemplos distintos, e identifica al menos un supuesto que haría fallar una aplicación real.

**Problemas habituales:** Claude presenta un «proyecto completo» sin ejecutarlo; el alumno confunde la respuesta con un archivo; un test pasa porque no valida ninguna condición. **Solución didáctica:** preguntar «¿dónde está la evidencia?», no aceptar afirmaciones verbales.
