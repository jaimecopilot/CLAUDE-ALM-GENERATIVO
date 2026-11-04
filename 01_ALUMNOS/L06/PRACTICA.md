# L06 · PRÁCTICA: tests desde Gherkin y revisión de seguridad

**120 min:** teoría 20, metaprompt y diseño de pruebas 20, tests y ejecución 45, fallos y seguridad 25, gate 10.

## Entrada
Recupera **docs/requisitos/especificacion.md** (criterios CA), el código real de L05 y **alm/contratos/04-testing.md**. Identifica los tests que ya existen y comprueba su resultado antes de modificarlos.

## Paso 1 — preparar el prompt operativo
Ejecuta **METAPROMPT.md** y revisa **alm/prompts-generados/04-testing.md**. El prompt no puede limitarse a «genera tests». Debe producir una matriz CA → prueba → archivo y ordenar casos por riesgo.

## Paso 2 — diseñar la matriz de pruebas
Para cada RF, marca al menos un caso de éxito y uno de fallo o límite. En RF-03 deben aparecer:
- colisión parcial;
- inicio exacto en el fin de reserva previa;
- otra sala a la misma hora;
- reserva cancelada;
- fecha fin anterior al inicio.

La matriz puede guardarse como **docs/calidad/matriz-pruebas.md**. Los nombres de test deben describir comportamiento, no números aleatorios.

## Paso 3 — generar y ejecutar
Autoriza generar pruebas con pytest para servicios y API, ajustadas al código real. En una terminal del entorno del proyecto ejecuta:
~~~bash
python -m pytest -q
~~~
Si la dependencia no está instalada, sigue el README/requirements y registra la instalación. Guarda salida, número de pruebas y fallos en **docs/calidad/informe.md**. No copies cifras de otro equipo.

## Paso 4 — depurar un fallo real
Si falla un test, aporta a Claude el error relevante y el criterio original. Pide diagnosis causa-raíz antes de modificar. Comprueba diff de la reparación; confirma que no se ha cambiado el test correcto para eliminar el fallo. Si no hay fallo natural, el formador puede proponer un defecto didáctico aislado, siempre documentando que fue introducido.

## Paso 5 — cobertura y revisión básica
Si se dispone de pytest-cov autorizado:
~~~bash
python -m pytest --cov=app --cov-branch -q
~~~
Comenta qué partes faltan; **no fijes un porcentaje inventado**. Si la herramienta no está disponible, deja cobertura como «no medida» y no detengas toda la actividad. Pide a Claude una revisión básica de secretos, dependencias, validaciones y SQL; el alumno verifica los hallazgos en el código, uno por uno.

## Paso 6 — protocolo de siete niveles
Documenta cada nivel (observación, resultado, evidencia). No basta poner siete checks verdes. En seguridad incluye dos límites conocidos del MVP: autenticación omitida por alcance y resistencia a concurrencia de producción no demostrada.

## Gate de calidad
Hay pruebas ejecutadas, resultados comprobados, correspondencia con criterios CA y hallazgos anotados. Si falla un test exigido, la fase queda BLOQUEADA; el alumno realiza corrección controlada. Registra el commit de pruebas y prepara la MR para L07.
