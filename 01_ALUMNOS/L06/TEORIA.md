# L06 · TEORÍA: asegurar calidad del código generado por IA

**Duración: 120 min.** Basado en módulo 5, P5.1–P5.6 y módulo 8, P8.4.

## Una prueba es una afirmación comprobable

Cuando Claude produce código también puede producir tests, pero ambos pueden compartir una interpretación equivocada del requisito. Por eso los tests del taller parten **primero de los criterios Gherkin aprobados**. En lugar de preguntar únicamente «¿pasan los tests?», pregunta «¿qué criterio demuestra cada test?». Una prueba que únicamente verifica HTTP 200 ante una petición de listado puede ser válida para listar, pero no demuestra que se impidan reservas dobles.

**Unitario:** aísla una función o regla como el solapamiento. **Integración:** atraviesa endpoint, validación y almacenamiento. **Regresión:** comprueba que un cambio nuevo no rompe capacidades anteriores. Los tres tipos aparecen en nuestro caso, sin configurar una plataforma empresarial de pruebas.

## Casos importantes y falsos positivos

Debemos cubrir reserva válida, colisión, contigüidad, salas diferentes, cancelación, sala desconocida, intervalos inválidos y entrada con datos incompletos. El hecho de tener veinte tests no equivale a cobertura de negocio si todos prueban el mismo caso feliz. **Cobertura de líneas** mide ejecución de líneas; **cobertura de ramas** aproxima caminos de decisión; ninguna de las dos garantiza corrección semántica. El alumno debe señalar qué criterio RF/CA verifica cada test.

## Depuración y bucle de reparación supervisada

Un bucle sensato es *ejecutar → registrar fallo → diagnosticar → modificar la causa → volver a ejecutar*. Una reparación peligrosa es cambiar el test para que acepte el comportamiento equivocado. Si Claude propone relajar la condición de no solapamiento, el alumno la rechaza aunque todo pase después. El agente no puede presentarse como fuente independiente de confianza sobre su propio resultado; necesitamos prueba de ejecución y, preferentemente, revisión cruzada.

## El protocolo de validación de siete niveles del GitHub fuente

1. Visual: ¿comprendo lo que se ha modificado?
2. Dependencias: ¿existen versiones y bibliotecas utilizadas?
3. Ejecución: ¿arranca el programa y corren los tests?
4. Requisitos: ¿se satisfacen RF/CA y se mantiene el alcance?
5. Seguridad: ¿hay secretos, validación de entradas y tratamiento seguro de errores?
6. Calidad: ¿son claros los nombres y las responsabilidades?
7. Documentación: ¿los ejemplos y diagramas reflejan la implementación?

No se aplica a ciegas: cada nivel produce observación, decisión y evidencia. No inventar una puntuación de cobertura ni una ausencia de vulnerabilidades sin herramientas de comprobación.

## Seguridad con alcance acotado

El MVP no usa identidades reales. Por tanto, no se afirmará «seguro en producción». Sí puede verificarse que no hay credenciales hardcodeadas, que las entradas se validan, que no se concatena SQL inseguro y que los errores no exponen trazas sensibles en respuestas públicas. Los riesgos de autorización y concurrencia se documentan como **límites del MVP**, sin implantar en 16h un sistema de seguridad empresarial.

## De la validación local a CI

L06 establece pruebas reproducibles y una lista de comandos. L07 incluirá esas comprobaciones en jobs de GitLab. Es la diferencia entre validar en mi portátil y lograr que la misma verificación se ejecute en el flujo de integración.

**Lecturas completas reproducidas debajo:** testing inteligente, cobertura, seguridad y protocolo de validación.

---

---

## Lectura original: modulo-5-testing y calidad/teoria/t5.1-test inteligente.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-5-testing%20y%20calidad/teoria/t5.1-test%20inteligente.md

# T5.1 – TESTING INTELIGENTE CON IA: DEL PROMPT AL TEST EJECUTABLE

El testing de software ha sido tradicionalmente una de las tareas más infravaloradas y a la vez más críticas del desarrollo. Escribir tests unitarios, de integración y end-to-end requiere tiempo, disciplina y un conocimiento profundo del código. La IA generativa transforma este panorama permitiendo generar tests a partir de descripciones en lenguaje natural, código fuente o especificaciones ejecutables. La clave no está en delegar completamente el testing en la IA, sino en encontrar el equilibrio adecuado entre la generación automatizada y la supervisión humana.

La generación de tests unitarios con IA sigue un principio simple: proporcionas el código a testear (o la especificación de lo que debe hacer) y la IA genera los tests correspondientes. Puedes pedir tests para una función específica, para una clase completa o para un módulo entero. La IA analiza el código, identifica los parámetros, el tipo de retorno, las dependencias y la lógica interna, y genera tests que cubren el caso feliz, casos de error y casos límite. El formato del prompt determina la calidad de los tests generados.

El prompt estructurado para generación de tests debe incluir: el código a testear, el framework de testing a usar (pytest, Jest, JUnit), los tipos de tests deseados (unitarios, integración), y los casos específicos a cubrir (caso feliz, errores, límites). Un prompt típico sería: "Genera tests unitarios con pytest para esta función. Incluye: caso feliz con datos válidos, caso de error con parámetros inválidos, caso límite con lista vacía, y mock para la dependencia externa". Cuanto más específico seas sobre los casos a cubrir, más completos serán los tests.

La generación de tests desde especificaciones ejecutables es el flujo natural del ALM generativo. Si has creado una especificación con criterios Gherkin (como aprendiste en el Módulo 2), puedes pedir a la IA que genere tests que verifiquen cada criterio. Por ejemplo: "Basándote en estos criterios Gherkin, genera tests de integración que verifiquen cada escenario". Esto asegura que los tests están directamente vinculados a los requisitos, cerrando el círculo de trazabilidad.

La generación de datos de prueba es otra capacidad valiosa. Puedes pedir a la IA que genere fixtures, datos mock o datos de ejemplo en formato JSON que cubran diferentes escenarios. Por ejemplo: "Genera datos de prueba para una API de reservas: usuarios con diferentes roles, salas con diferentes capacidades, reservas con diferentes estados (confirmada, cancelada, pendiente)". La IA generará conjuntos de datos realistas y variados.

La detección de bugs mediante tests es una aplicación avanzada. Puedes pedir a la IA que analice el código y genere tests específicamente diseñados para detectar posibles bugs: "Analiza este código y genera tests que intenten romperlo. Prueba valores extremos, combinaciones inesperadas y escenarios de error". La IA actuará como un tester malicioso, intentando encontrar puntos débiles.

Las limitaciones del testing con IA deben entenderse. Los tests generados pueden no cubrir todos los escenarios posibles, especialmente aquellos que requieren conocimiento profundo del dominio de negocio. La IA puede generar tests que pasan pero que no verifican realmente el comportamiento correcto (aserciones débiles). La cobertura puede ser superficial si no se especifican los casos a cubrir. La revisión humana de los tests generados sigue siendo esencial.


---

## Lectura original: modulo-5-testing y calidad/teoria/t5.2-estrategias cobertura.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-5-testing%20y%20calidad/teoria/t5.2-estrategias%20cobertura.md

# T5.2 – ESTRATEGIAS DE COBERTURA Y VALIDACIÓN EN EL ALM GENERATIVO

La cobertura de código es una métrica que indica qué porcentaje del código fuente está siendo ejecutado por los tests. En el contexto del ALM generativo, la cobertura adquiere una nueva dimensión: no solo mide la calidad de los tests, sino también la calidad del código generado por la IA. Un código generado con baja cobertura es una señal de que la IA no generó tests adecuados o de que el código tiene ramas innecesarias.

La cobertura como conversación es el enfoque recomendado. No se trata de lanzar un comando y esperar un resultado mágico. El flujo es: ejecutar tests con cobertura, visualizar las líneas no cubiertas, pedir a la IA que genere tests específicos para esas líneas, ejecutar los nuevos tests, y repetir. La IA te ayuda en cada paso: identificando brechas, generando tests orientados a líneas concretas y verificando que la cobertura aumenta.

La cobertura de ramas (branch coverage) es más importante que la cobertura de líneas. La cobertura de líneas te dice qué líneas se ejecutaron, pero la cobertura de ramas te dice si se evaluaron todas las condiciones lógicas (if/else, bucles, excepciones). Puedes pedir a la IA: "Analiza la cobertura de ramas de este código y genera tests para las condiciones que no se han evaluado". Esto asegura que todos los caminos de decisión están probados.

El bucle de auto-reparación es una de las capacidades más potentes del ALM generativo. Cuando un agente de IA ejecuta tests y detecta fallos, no se detiene: analiza los logs, diagnostica la causa raíz, modifica el código y vuelve a ejecutar los tests. Este ciclo continúa hasta que todos los tests pasan. El desarrollador supervisa el proceso a través de los logs y valida el resultado final. Entender este bucle es fundamental para trabajar eficazmente con agentes autónomos.

La validación de tests generados por IA es un paso crítico. No basta con que los tests pasen: deben verificar el comportamiento correcto. Preguntas que debes hacer ante cada test generado: ¿este test fallaría si alguien introduce un bug en esta lógica?, ¿las aserciones son lo suficientemente específicas?, ¿el test cubre un escenario relevante o es redundante? La IA puede ayudar a responder estas preguntas: "Revisa estos tests y dime si hay aserciones débiles o escenarios no cubiertos".

La personalización de la estrategia de testing es posible mediante instrucciones explícitas. Puedes definir reglas como: "La cobertura mínima para nuevo código es del 85%", "Los tests deben cubrir todas las ramas de decisión", "Los servicios críticos requieren 95% de cobertura". La IA aplicará estas reglas al generar tests, asegurando consistencia en todo el proyecto.


---

## Lectura original: modulo-5-testing y calidad/teoria/t5.3-seguridad testing.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-5-testing%20y%20calidad/teoria/t5.3-seguridad%20testing.md

# T5.3 – SEGURIDAD EN TESTING: DETECCIÓN DE VULNERABILIDADES EN CÓDIGO GENERADO POR IA

El código generado por IA no es inherentemente seguro. Al entrenarse con repositorios públicos que contienen abundantes malas prácticas de seguridad, las IAs pueden sugerir código con vulnerabilidades. La seguridad en el testing no consiste solo en probar la funcionalidad, sino en verificar activamente que el código generado no introduce nuevos vectores de ataque. Esta verificación debe ser parte del ciclo de testing en el ALM generativo.

Las vulnerabilidades más comunes en código generado por IA incluyen: falta de validación de entradas (permite inyección SQL, XSS), uso de algoritmos criptográficos obsoletos (MD5, SHA1), inclusión de secretos hardcodeados (claves API, contraseñas), falta de controles de autorización en endpoints, y exposición de datos sensibles en mensajes de error o logs. La IA puede generar estos patrones porque los ha visto en su entrenamiento.

La detección de vulnerabilidades con IA es un proceso de dos pasos. Primero, pides a la IA que analice el código en busca de problemas de seguridad: "Revisa este código en busca de vulnerabilidades según OWASP Top 10". La IA identificará posibles problemas y sugerirá correcciones. Segundo, validas esas sugerencias manualmente y aplicas las correcciones. La IA puede detectar patrones conocidos, pero puede pasar por alto vulnerabilidades sutiles que requieren conocimiento del contexto.

La validación de dependencias es un aspecto crítico. La IA puede sugerir imports de librerías con vulnerabilidades conocidas. Antes de aceptar cualquier dependencia generada por IA, verifica: ¿la librería existe?, ¿la versión es correcta?, ¿tiene vulnerabilidades conocidas?, ¿tiene mantenimiento activo? Herramientas como pip-audit, npm audit o Dependabot pueden automatizar parte de esta verificación.

El análisis de superficie de ataque consiste en identificar todos los puntos de entrada de tu aplicación y evaluar qué controles de seguridad tiene cada uno. Puedes pedir a la IA: "Analiza este módulo y dime qué endpoints están expuestos sin autenticación, qué datos sensibles se envían en las respuestas y qué parámetros no están validados". La IA te dará un mapa de la superficie de ataque que puedes usar para reforzar la seguridad.

La automatización de la seguridad en el ALM generativo es la capa final. En un flujo completo, cada PR generada por un agente debería pasar automáticamente por verificaciones de seguridad: análisis de dependencias, detección de secretos, análisis estático de código (SAST) y revisión de seguridad por IA. El pipeline de CI/CD actúa como guardián, rechazando automáticamente el código que introduzca vulnerabilidades.


---

## Lectura original: modulo-8-riesgos y buenas practicas/teoria/t8.3-validacion output.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-8-riesgos%20y%20buenas%20practicas/teoria/t8.3-validacion%20output.md

# T8.3 – CÓMO VALIDAR Y SUPERVISAR EL OUTPUT GENERADO POR LA IA

La pregunta fundamental que todo desarrollador debe hacerse ante cada output de IA es: ¿cómo sé que esto es correcto? La validación del código generado por IA no es opcional ni secundaria: es la responsabilidad principal del desarrollador que usa herramientas de IA generativa. La IA es un copiloto, no un piloto automático.

El protocolo de validación de 7 niveles es un método sistemático aplicable a cualquier output de cualquier IA:

Nivel 1 - Verificación visual: ¿entiendo cada línea? ¿la lógica es correcta a simple vista? ¿hay imports sospechosos?

Nivel 2 - Verificación de dependencias: ¿todas las librerías importadas existen? ¿las versiones son correctas? ¿las librerías tienen mantenimiento activo?

Nivel 3 - Ejecución de tests: ¿el código compila o se ejecuta sin errores? ¿los tests existentes siguen pasando? ¿los tests generados por IA son correctos?

Nivel 4 - Validación contra requisitos: ¿cumple todos los criterios de aceptación? ¿implementa funcionalidad no solicitada? ¿falta alguna validación?

Nivel 5 - Revisión de seguridad: ¿hay secretos hardcodeados? ¿las entradas de usuario están validadas? ¿se usa el ORM en lugar de SQL directo?

Nivel 6 - Revisión de calidad: ¿tiene type hints? ¿tiene docstrings? ¿los nombres son descriptivos?

Nivel 7 - Validación de documentación: ¿los diagramas reflejan el código real? ¿los docstrings son correctos? ¿la documentación está actualizada?

La validación en el contexto del ALM generativo adquiere una dimensión adicional. Cuando un agente autónomo genera código multi-archivo, no basta con revisar el código: debes revisar también el plan de implementación, verificar que las decisiones arquitectónicas son coherentes y asegurarte de que el código se integra correctamente con el existente.

La supervisión del bucle de auto-reparación es otro aspecto crítico. Cuando un agente corrige sus propios errores, no asumas que la corrección es correcta. Revisa los cambios: ¿la corrección aborda la causa raíz o solo ajusta el test para que pase? La supervisión humana del bucle de auto-reparación es esencial.

La validación de documentación generada no debe descuidarse. Si la IA generó documentación —docstrings, READMEs, ADRs, diagramas— verifica que refleja fielmente el código implementado. La documentación incorrecta es quizás peor que la falta de documentación, porque induce a error a futuros desarrolladores.

La cultura de "piloto automático supervisado" es la mentalidad correcta. La IA acelera las tareas mecánicas; el desarrollador mantiene la supervisión crítica. No se trata de confiar ciegamente ni de desconfiar sistemáticamente, sino de verificar de forma inteligente, dedicando más tiempo a lo crítico y menos a lo trivial.
