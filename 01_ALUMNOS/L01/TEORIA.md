# L01 · TEORÍA: Vibe Coding y límites del código generado

**Tiempo de lectura y explicación:** 5 minutos de la sesión de 30.

## 1. Qué va a aprender el alumno

**Vibe Coding** es una forma de construir prototipos mediante interacción en lenguaje natural con un modelo generativo, observando los resultados y refinándolos. En este taller empleamos esa interacción como una puerta de entrada, no como excusa para prescindir de requisitos, pruebas o revisión. Una petición como «crea un gestor de salas» deja sin resolver las reglas de disponibilidad, el significado de «cancelar», el formato de fechas y las respuestas de error. La IA completará esos huecos mediante supuestos, a veces de forma convincente y equivocada.

**ALM** (Application Lifecycle Management) designa el conjunto de actividades, decisiones y evidencias que acompañan a una aplicación desde su concepción hasta su evolución. En este curso su secuencia visible será requisitos, diseño, construcción, verificación, integración/entrega, mantenimiento y trazabilidad. **SDLC** describe el ciclo de desarrollo; ALM incluye además organización, seguimiento y gobierno de sus artefactos.

## 2. Tres papeles que no debemos confundir

1. **Chat conversacional:** propone texto o código en una conversación. Puede redactar buenas ideas sin ejecutar nada.
2. **Asistente de IDE:** utiliza el contexto del editor para sugerir o modificar partes de un proyecto.
3. **Agente de codificación:** con permisos concretos puede leer archivos, cambiar varios módulos, invocar herramientas y ejecutar pruebas. Que el agente diga «funciona» no constituye prueba de que se ejecutó correctamente.

Los **metaprompts** de este taller son instrucciones para que la IA fabrique *prompts operativos* adecuados a la fase y a sus entradas. El prompt operativo, una vez revisado, indica las acciones concretas y los archivos de salida. Esta separación será imprescindible en L02-L09.

## 3. Ejemplo que se utiliza en clase

El usuario solicita «quiero reservar una sala de reunión». A partir de eso la IA podría ofrecer un formulario con botón «Reservar» y mostrar «Reserva confirmada». ¿Qué no sabemos? Si dos reservas pueden coincidir, si el intervalo es inclusivo o exclusivo, si deben introducirse fechas en UTC, si pueden cancelarse reservas, qué sucede cuando la sala no existe y si los datos deben persistir. Un prototipo visual no demuestra ninguna de estas condiciones.

**Diagnóstico inicial:** diferencia la *apariencia de funcionamiento* de un comportamiento verificable. La prueba objetiva de una reserva no solapada debe indicar entradas, estado previo y resultado esperado, por ejemplo: «si la sala 2 tiene una reserva de 10:00 a 11:00, otra reserva de 10:30 a 11:30 se rechaza»; las reservas contiguas pueden aceptarse si se define la regla de intervalo semiabierto.

## 4. Riesgos a reconocer

Las alucinaciones pueden producir imports falsos, dependencias inexistentes, respuestas HTTP incoherentes o tests que no comprueban los requisitos. También existe riesgo de exponer claves, datos reales o secretos al copiar material en el chat. La medida de calidad no es cuánto código escribe Claude, sino qué evidencias conservamos: criterio de aceptación, prueba que falla o pasa, commit, revisión y pipeline.


---


## 5. Conceptos básicos de inteligencia artificial

Imagina que estás sentado frente a tu editor de código y, antes de terminar de escribir una línea, la herramienta te sugiere exactamente lo que ibas a escribir. Esa sugerencia no viene de una bola de cristal, sino de un sistema de inteligencia artificial. La inteligencia artificial, o IA, es la capacidad de un sistema informático para realizar tareas que normalmente requieren inteligencia humana: comprender lenguaje, reconocer patrones, tomar decisiones o generar contenido nuevo. No se trata de una máquina que "piensa" como nosotros, sino de un sistema que procesa cantidades masivas de información y encuentra patrones que le permiten hacer predicciones útiles.

Cuando usas cualquier asistente de IA generativa —ChatGPT, Claude, Copilot, Gemini— estás interactuando con un tipo de IA llamada **inteligencia artificial estrecha o débil**. Esto significa que está especializada en un dominio concreto —lenguaje y código— y no tiene conciencia, emociones ni intenciones propias. No quiere sustituirte como desarrollador, simplemente está entrenada para ayudarte a escribir código más rápido, explicar conceptos o generar documentación. La IA fuerte o general —una máquina con inteligencia comparable a la humana en cualquier dominio— no existe hoy.

Dentro de la IA, la rama que hace posible los asistentes actuales se llama **machine learning** o aprendizaje automático. En la programación tradicional, un desarrollador escribe reglas explícitas: "si ocurre A, entonces haz B". En machine learning, el sistema aprende esas reglas a partir de ejemplos. Si quisieras clasificar incidencias como "bug", "feature" o "consulta", con programación tradicional escribirías decenas de condiciones analizando palabras clave. Con machine learning, mostrarías miles de incidencias ya clasificadas y el sistema inferiría por sí mismo qué patrones distinguen cada categoría.

Dentro del machine learning existe una subrama llamada **deep learning** o aprendizaje profundo. Utiliza estructuras inspiradas en el cerebro humano —redes neuronales artificiales— con múltiples capas de procesamiento. Cada capa aprende un nivel de abstracción distinto: las primeras capas detectan patrones simples (bordes en una imagen, palabras frecuentes), las capas intermedias combinan esos patrones (formas, frases), y las capas profundas reconocen conceptos complejos (rostros, intenciones). Los modelos de lenguaje modernos tienen cientos de capas y miles de millones de parámetros ajustables.

El tipo concreto de IA que usas como desarrollador es un **LLM**, siglas de **Large Language Model** o gran modelo de lenguaje. Un LLM es una red neuronal entrenada con cantidades inmensas de texto y código fuente público. Durante ese entrenamiento, el modelo aprende a predecir cuál es la palabra o token más probable que debe aparecer a continuación en una secuencia determinada. Cuando escribes `function suma(a, b)` y el asistente sugiere `return a + b`, no lo hace porque alguien le haya programado esa regla, sino porque ha visto ese patrón millones de veces.

Es fundamental entender que la IA actual no razona como una persona. No comprende el significado profundo del código, no tiene experiencia real desarrollando software y no conoce las particularidades de tu proyecto. Todo lo que genera es fruto de patrones estadísticos. Por eso puede sugerir código que parezca correcto pero contenga errores sutiles, usar librerías obsoletas o incluso inventar funciones que no existen. La herramienta es un copiloto, no un piloto automático. La responsabilidad de revisar, entender y validar cada línea generada sigue siendo del desarrollador.


---


## 6. Principios de prompt engineering

El prompt engineering es el conjunto de técnicas para redactar instrucciones que guíen a un modelo de lenguaje hacia el resultado que necesitas. La calidad de lo que obtienes depende directamente de la calidad de lo que escribes. Un prompt ambiguo produce respuestas genéricas. Un prompt bien estructurado produce código preciso, explicaciones útiles y soluciones adaptadas a tu contexto. Estos principios son universales: funcionan en ChatGPT, Claude, Copilot, Gemini y cualquier otro LLM.

El primer principio es la **claridad y especificidad**. Debes decir exactamente qué quieres, sin dar nada por supuesto. Si necesitas una función que valide un email, no escribas "crea una función para validar emails". Especifica el lenguaje de programación, el formato de entrada y salida, y los criterios de validación. Por ejemplo: "Crea una función en Python que reciba un string y devuelva True si es un email válido según RFC 5321, False en caso contrario". Cuanto más concreta sea tu instrucción, más se ajustará el resultado a lo que esperas.

El segundo principio es **proporcionar contexto y asignar un rol**. Los modelos de lenguaje ajustan su tono y precisión según el papel que les asignes. Iniciar tu prompt con frases como "Actúa como un desarrollador senior de Python" o "Eres un arquitecto de software experto en microservicios" orienta al modelo hacia un estilo más profesional y técnico. Además de asignar un rol, añade contexto sobre tu proyecto: qué framework usas, qué versión de lenguaje, qué restricciones tienes.

El tercer principio es **especificar el formato de salida y las restricciones**. No es lo mismo pedir "una función de ordenación" que pedir "una función de ordenación con type hints, docstring en español y que devuelva una nueva lista sin modificar la original". Puedes indicar cómo quieres estructurar la respuesta: solo código, código más explicación, o primero la explicación y luego el código. También puedes establecer restricciones explícitas: no usar ciertas librerías, no exceder cierta complejidad o seguir un estilo de código concreto.

El cuarto principio es el uso de **ejemplos, o few-shot prompting**. Consiste en incluir uno o varios ejemplos del resultado que esperas antes de hacer tu petición real. Esto es especialmente útil cuando necesitas un formato de salida muy concreto o un estilo de código que se aparta de lo más común. Por ejemplo, puedes mostrar cómo conviertes un objeto JSON en otro formato y luego pedir que aplique la misma transformación a un conjunto nuevo. El modelo capta el patrón y lo replica fielmente.

El quinto principio es la **cadena de pensamiento o chain-of-thought**. Para problemas complejos, pide al modelo que razone paso a paso antes de escribir el código. Esta técnica reduce las alucinaciones y produce soluciones más sólidas porque obliga al modelo a descomponer el problema en etapas lógicas. Puedes escribir: "Analiza primero qué entradas recibe este sistema, después qué transformaciones necesita y finalmente escribe la función". El razonamiento intermedio que el modelo genera te sirve además para verificar que ha entendido correctamente el problema antes de ejecutar la solución.

El sexto principio es la **iteración y refinamiento**. No esperes el resultado perfecto a la primera. El chat es una conversación, no un comando único. Después de recibir una respuesta, puedes refinarla con instrucciones adicionales: "Ahora modifica la función para que acepte un parámetro opcional que ignore mayúsculas", o "Añade control de errores para cuando el archivo no existe". Cada iteración mejora la salida porque el modelo incorpora el historial de la conversación como contexto adicional. Trata cada prompt como el primer mensaje de un diálogo, no como una orden definitiva.

El séptimo principio es la **validación crítica**. Todo lo que genera una IA debe ser revisado, probado y comprendido antes de integrarlo en tu proyecto. No copies código sin leerlo. Ejecuta los tests que hayas solicitado o los que vengan generados. Comprueba que las librerías que importa existen y están actualizadas. Verifica que no haya vulnerabilidades evidentes como contraseñas hardcodeadas o consultas sin sanitizar. El modelo es un asistente, no un responsable. La decisión final sobre qué código entra en producción es siempre tuya.

Estos siete principios —claridad, contexto, formato, ejemplos, razonamiento, iteración y validación— forman la base del prompt engineering efectivo. Aplicarlos sistemáticamente transforma cualquier IA generativa de un simple generador de texto a un verdadero compañero de desarrollo. Con la práctica, interiorizarás estos patrones y los aplicarás sin esfuerzo cada vez que interactúes con una IA.

Un último consejo práctico: guarda tus prompts efectivos. Crea un archivo de referencia con aquellos que te han dado buenos resultados en tareas recurrentes. Puede ser un simple documento Markdown dentro de tu repositorio o un snippet de tu editor. Reutilizar prompts probados te ahorrará tiempo y te garantizará consistencia en tus interacciones con la IA.


---


## 7. LIMITACIONES Y RIESGOS DE LA IA

1. Has visto lo potente que puede ser una IA generativa cuando le das un buen prompt. Pero ahora toca hablar de la otra cara: sus limitaciones y los riesgos de usarla sin supervisión. La IA no es infalible. Comete errores que a simple vista pueden parecer correctos. Conocer esos errores y saber cómo detectarlos es tan importante como saber escribir buenos prompts. Exploraremos los tres grandes riesgos: alucinaciones, sesgos y problemas de seguridad.

2. El riesgo más frecuente son las alucinaciones. Una alucinación ocurre cuando el modelo genera información que parece correcta pero es total o parcialmente falsa. En código, esto se traduce en funciones que no existen, librerías inventadas, parámetros que no corresponden a la realidad de una API o ejemplos de configuración que apuntan a servicios inexistentes. El modelo no "miente": simplemente predice tokens que estadísticamente podrían aparecer en ese contexto, sin acceso a la documentación real ni capacidad de verificar lo que genera.

3. Las alucinaciones más comunes en desarrollo incluyen: importar librerías que no existen (from oracle_light import Connection), usar métodos que no están en la API real (json.auto_fix()), o inventar información técnica (un RFC que nunca existió). La única defensa eficaz es la verificación sistemática: comprueba siempre que la librería existe, consulta la documentación oficial y ejecuta el código antes de integrarlo.

4. El segundo riesgo son los sesgos. Un modelo aprende de los datos con los que fue entrenado, y esos datos contienen los sesgos del mundo real. En código, esto puede manifestarse en ejemplos que asumen un perfil de usuario concreto (nombres anglosajones, formatos de fecha estadounidenses) o en validaciones que excluyen a usuarios legítimos (nombres con tildes, apóstrofes o caracteres no latinos). La mitigación consiste en usar prompts inclusivos que especifiquen explícitamente la diversidad deseada.

5. El tercer riesgo es la seguridad. El código generado por IA puede contener vulnerabilidades: falta de sanitización de entradas, uso de algoritmos criptográficos obsoletos, inclusión accidental de secretos o omisión de controles de acceso. Los modelos aprenden del código público, que contiene abundantes malas prácticas. Si aceptas sugerencias sin revisarlas con mentalidad de seguridad, puedes introducir vulnerabilidades reales.

6. Un riesgo adicional es la posible fuga de información sensible. No incluyas claves de API reales, tokens de acceso, contraseñas o datos personales en un prompt. Trata el chat como una conversación profesional con un colega: compartes lógica y estructura, pero nunca credenciales. La mayoría de servicios de IA no usan tus datos para entrenar, pero la información viaja por la red.

7. La mitigación de estos riesgos se basa en tres pilares: verificación (comprobar cada salida), buenas prácticas (no incluir secretos, revisar seguridad) y actitud crítica (no confiar ciegamente en el output). En los siguientes módulos aplicarás estos principios a fases concretas del desarrollo, empezando por el análisis de requisitos.
