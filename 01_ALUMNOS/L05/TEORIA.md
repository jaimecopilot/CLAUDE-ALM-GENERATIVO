# L05 · TEORÍA: código multiarchivo generado desde una especificación

**Duración: 210 minutos (3 h 30 min).** El bloque más largo del curso. Procedencia: módulo 4, ejercicios P4.2 «CRUD API REST» y P4.8 «ciclo completo», junto a P9.4b «agentes de codificación».

## El código es un producto derivado, no el punto de partida

Hasta ahora hemos descrito necesidades, generado una especificación revisada, creado un backlog y aprobado un diseño. Esos documentos son **entradas** de la generación de código. Si Claude se desvía de la especificación, no «arreglamos» el requisito para que el código parezca correcto. Marcamos la discrepancia y corregimos el código o elevamos una decisión de cambio formal.

Un agente trabaja sobre archivos, no solo sobre un mensaje. La diferencia importante con un chat es que debe inspeccionar la estructura real del repositorio, proponer un plan multiarchivo, editar módulos, invocar pruebas y mostrar el diff. El alumno debe aprender los conceptos de **working tree**, **rama**, **commit**, **diff** y **Merge Request**, aunque Claude escriba la mayor parte de las líneas de Python.

## Arquitectura objetivo y mínima de las capas

FastAPI expone endpoints HTTP. El servicio aplica las reglas de negocio; la persistencia guarda salas y reservas; los esquemas validan entradas y salidas; las pruebas verifican comportamientos. **No imponemos clases por cada sustantivo** ni un patrón Repository excesivo, a menos que mejore la separación y permita probar la lógica. Una solución en una decena de archivos razonables es preferible a un mini ecosistema de microservicios.

La especificación del curso define de forma deliberada un perímetro pequeño: consulta de salas, creación de reservas, detección de colisión y cancelación. Se admite almacenamiento SQLite local para el MVP. La pantalla puede ser una página HTML sencilla; no se requiere frontend con build complejo.

## API, validación y semántica de errores

El equipo acordará rutas concretas a partir del contrato: por ejemplo **GET /salas**, **POST /reservas** y **DELETE /reservas/{id}**. Una solicitud válida se representa con inicio y fin inequívocos, ambos con zona horaria. La operación de alta puede devolver 201; la solicitud que solapa otra reserva, 409; sala desconocida, 404; datos inválidos, 422. Estos códigos describen comportamientos que los tests comprobarán, no adornos en una tabla.

La comprobación de solapamiento debe realizarse para reservas activas de la **misma** sala. Una reserva cancelada libera el intervalo; los extremos contiguos no se solapan cuando el contrato usa [inicio,fin). Para bases con acceso concurrente real hay riesgos de carrera: en el nivel junior se estudian conceptualmente y no se promete resistencia a cargas de producción.

## Desarrollo asistido: plan → cambio → inspección → prueba

1. **Plan:** Claude expone qué archivos creará y qué RF cubrirá.
2. **Generación:** solo implementa el alcance autorizado.
3. **Revisión:** alumno inspecciona diff, imports, nombres, validación y rutas.
4. **Ejecución:** se prueba localmente con comandos reproducibles; una descripción de Claude no sirve de evidencia.
5. **Control de versiones:** se crea commit descriptivo y MR; se solicita revisión humana.

La iteración es intencionada: no esperamos el código perfecto a la primera. Tampoco damos a Claude permiso para «resolver» un fallo eliminando tests o relajando criterios. La reparación se registra y vuelve a verificarse.

## Dónde entra GitLab

El trabajo debe aparecer asociado a issues concretas. La rama de implementación deja un historial; una MR expone cambios, motivación y evidencias. El pipeline CI de L07 aún no existe, por lo que L05 registra pruebas locales y evita afirmar que la integración continua ha pasado.

## Consejos para gestionar la cuota de Claude

Delimita contexto: incluye solo contrato, diseño y requisito específico; ejecuta por incremento (salas, reservas, conflictos, cancelación). Conserva resultados y no pidas regeneraciones cosméticas. Reutiliza pruebas y logs de la ejecución que ya ha realizado el agente. Pide una corrección concreta ante un error en lugar de «reescribe toda la aplicación».

## Criterio de aprobación

Funciona la API local con las cuatro operaciones exigidas; hay demostración y pruebas básicas, sin funcionalidades añadidas, y una rama versionada con diff revisado. No es requisito que todas las pruebas de seguridad o CI estén completas: L06 y L07 profundizarán en esos aspectos.

**Lecturas originales completas:** generación de código, técnicas de prompting, refactorización y buenas prácticas.

---

---

## Lectura original: modulo-4-desarrollo-codificacion/teoria/t4.1- generacion codigo.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-4-desarrollo-codificacion/teoria/t4.1-%20generacion%20codigo.md

# T4.1 – IA EN GENERACIÓN DE CÓDIGO: DEL PROMPT AL CÓDIGO FUNCIONAL

La generación de código es la aplicación más visible y transformadora de la IA en el desarrollo de software. Lo que antes requería horas de escritura manual —implementar una función, crear una clase, montar un endpoint— ahora puede obtenerse en segundos mediante un prompt bien redactado. Pero la diferencia entre un código mediocre y uno profesional no está en la IA, sino en la calidad del prompt que le proporcionas y en tu capacidad para validar y refinar el resultado.

El ecosistema de IAs para generación de código es amplio y diverso. Los asistentes inline (GitHub Copilot, Codeium, Amazon Q Developer, CodeWhisperer) se integran en el IDE y sugieren código mientras escribes, utilizando el contexto del archivo y las pestañas abiertas. Los chats de código (ChatGPT, Claude, Gemini, Copilot Chat) permiten interacciones más ricas: puedes describir lo que necesitas, iterar sobre el resultado y pedir explicaciones. Los agentes autónomos (Copilot Workspace, Coding Agent, GitLab Duo Workflow) van un paso más allá: toman una especificación completa y generan código multi-archivo con tests.

La generación de código desde comentarios es la forma más directa de interacción con asistentes inline. Escribes un comentario descriptivo —"Función que valida un email según RFC 5321, devuelve True/False"— y el asistente te sugiere la implementación. La calidad de la sugerencia depende de la precisión del comentario. Un comentario vago produce código genérico. Un comentario que especifica parámetros, validaciones, formato de retorno y casos límite produce código mucho más cercano a lo que necesitas.

La generación de código desde especificaciones ejecutables es el siguiente nivel. Si has creado una especificación con criterios Gherkin y detalles técnicos (como aprendiste en el Módulo 2), puedes usarla directamente como prompt para generar el código. La IA leerá la especificación, entenderá los requisitos, los criterios de aceptación y las restricciones, y generará una implementación coherente. Este es el flujo del ALM generativo: los requisitos se convierten directamente en código.

La generación multi-archivo es una capacidad que diferencia a los agentes autónomos de los chats simples. Mientras que un chat genera una función a la vez, un agente como Copilot Workspace puede generar simultáneamente el modelo de datos, el schema de validación, el repositorio, el servicio, el controlador y los tests, todo ello coherente entre sí y siguiendo las convenciones del proyecto. El prompt para un agente autónomo debe ser una especificación completa, no una simple pregunta.

La generación de código con contexto de proyecto es una ventaja de los asistentes integrados en el IDE. Cuando escribes código en VS Code con Copilot, el asistente no solo lee tu prompt: conoce los imports, los modelos, los servicios existentes y las convenciones del proyecto. Esto le permite generar código que se integra limpiamente con lo que ya existe, usando los mismos patrones y librerías. En un chat generalista, tendrías que proporcionar todo ese contexto manualmente.

Es importante entender las limitaciones. El código generado por IA puede contener errores sutiles, usar librerías obsoletas, omitir validaciones de seguridad o no cubrir todos los casos límite. La generación de código es rápida, pero la validación sigue siendo necesaria. El desarrollador no desaparece: su rol evoluciona de escribir cada línea a revisar, validar y refinar el código generado.


---

## Lectura original: modulo-4-desarrollo-codificacion/teoria/t4.2-tecnicas promting.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-4-desarrollo-codificacion/teoria/t4.2-tecnicas%20promting.md

# T4.2 – TÉCNICAS DE PROMPTING PARA FUNCIONES, CLASES Y ALGORITMOS

Generar una función o una clase con IA es mucho más que pedir "escribe una función que haga X". La diferencia entre un código mediocre y uno profesional está en la cantidad de contexto y especificidad que proporcionas en tu prompt. Una función no vive aislada: pertenece a un módulo, usa ciertas dependencias, sigue convenciones de nomenclatura y debe manejar errores. Cuando incluyes estos elementos en tu prompt, la IA genera código que se integra limpiamente en tu proyecto.

La técnica base para generar una función es el prompt estructurado en capas. Empieza siempre por la firma: nombre de la función, parámetros con tipos, tipo de retorno. Luego añade el comportamiento esperado: qué debe hacer, qué validaciones debe realizar, qué casos límite debe manejar. Finalmente, especifica el formato: type hints, docstring en formato Google, estilo de código. Un prompt típico sería: "Crea una función calcular_precio que reciba una sala, las horas de reserva y el tipo de cliente. Valida que las horas sean positivas y que la sala exista. Aplica un 20% de descuento si el cliente es premium. Retorna el precio final como float. Incluye type hints y docstring en formato Google".

Para clases, la técnica es similar pero con consideraciones adicionales. Una clase tiene estado (atributos), comportamiento (métodos) y relaciones con otras clases. Al generar una clase, especifica: el propósito de la clase, los atributos principales con sus tipos, los métodos clave con sus firmas y comportamiento, y las dependencias o relaciones con otras clases. Por ejemplo: "Crea una clase ReservaService que gestione la lógica de negocio de reservas. Debe usar ReservaRepository y SalaService como dependencias inyectadas en el constructor. Métodos: crear_reserva, cancelar_reserva, listar_reservas_usuario".

Para algoritmos complejos, la técnica de cadena de pensamiento es especialmente efectiva. Pide a la IA que razone paso a paso antes de escribir el código. Por ejemplo: "Necesito una función que calcule la disponibilidad de salas en una franja horaria. Primero analiza qué entradas recibe, después explica cómo detectarías solapamientos entre reservas, y finalmente escribe la función con la lógica completa". Esta técnica reduce errores porque obliga a la IA a descomponer el problema antes de implementarlo.

Los ejemplos few-shot son otra técnica potente. Si ya tienes código similar en tu proyecto, inclúyelo como referencia en el prompt: "Siguiendo el mismo estilo que esta función get_salas_disponibles, crea una función get_salas_por_capacidad que filtre por capacidad mínima". La IA captará el patrón y replicará el estilo, las convenciones y la estructura.

La generación de tests junto con el código es una práctica recomendada. Puedes añadir al prompt: "Incluye tests unitarios con pytest que cubran el caso feliz, al menos dos casos de error y un caso límite". La IA generará tanto la función como los tests, ahorrándote tiempo y asegurando que el código tiene cobertura desde el primer momento.


---

## Lectura original: modulo-4-desarrollo-codificacion/teoria/t4.3-refactorizacion asistida.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-4-desarrollo-codificacion/teoria/t4.3-refactorizacion%20asistida.md

# T4.3 – REFACTORIZACIÓN ASISTIDA Y TRADUCCIÓN ENTRE LENGUAJES

La refactorización es el arte de mejorar la estructura interna del código sin cambiar su comportamiento externo. Tradicionalmente, es una tarea costosa y arriesgada: mover código, extraer métodos, renombrar variables o aplicar patrones de diseño puede introducir bugs sutiles. La IA transforma esta realidad. Con un prompt adecuado, puedes pedirle que analice un bloque de código y lo mejore en segundos, manteniendo la semántica original. La refactorización asistida no elimina la necesidad de revisar, pero reduce drásticamente el tiempo mecánico de reescritura.

La refactorización mediante prompts sigue una estructura simple: proporcionas el código original, describes la transformación deseada y especificas las restricciones. Por ejemplo: "Refactoriza esta función para que use el patrón Repository en lugar de acceso directo a la base de datos. Mantén la misma interfaz pública, los mismos tipos de retorno y los mismos mensajes de error". La IA analizará el código, identificará las dependencias y generará una versión refactorizada.

La refactorización hacia patrones de diseño es una capacidad avanzada. Puedes tomar una clase con lógica condicional compleja y pedir: "Refactoriza esta clase aplicando el patrón Strategy, extrayendo cada algoritmo a una clase separada". La IA identificará las variantes del algoritmo, creará la interfaz Strategy, implementará cada estrategia concreta y modificará la clase original. El resultado será más extenso pero mucho más mantenible.

La refactorización hacia Clean Code es una de las aplicaciones más prácticas. Puedes pedir a la IA que aplique principios específicos: "Renombra todas las variables con nombres descriptivos", "Extrae métodos para que ninguna función supere las 10 líneas", "Elimina código duplicado", "Añade type hints y docstrings". La IA aplicará estas transformaciones de forma sistemática.

La traducción entre lenguajes es una extensión natural de la refactorización. Puedes seleccionar una función en Java y pedir: "Traduce esta función a Python, manteniendo exactamente la misma lógica, los mismos nombres de variables y el mismo comportamiento ante entradas inválidas". La IA traducirá la sintaxis, adaptará las convenciones idiomáticas (camelCase a snake_case), convertirá las estructuras de datos al equivalente en el lenguaje destino y ajustará el manejo de errores.

La traducción con adaptación idiomática va más allá de la traducción sintáctica. No es lo mismo traducir palabra por palabra que adaptar el código al estilo idiomático del lenguaje destino. Por ejemplo, un bucle for en Java puede convertirse en una list comprehension en Python. Los getters y setters de Java simplemente desaparecen en Python. La IA conoce estas diferencias idiomáticas y las aplica automáticamente si se lo pides: "Traduce este código Java a Python adaptando las convenciones idiomáticas".

La regla de oro para refactorización y traducción es: nunca sin tests. Antes de refactorizar o traducir, asegúrate de que existen tests que cubren el comportamiento actual. Después, ejecuta los tests sobre el código resultante. Si los tests pasan, la probabilidad de haber introducido un error es mucho menor. Si no tienes tests, pide a la IA que los genere antes de refactorizar.


---

## Lectura original: modulo-4-desarrollo-codificacion/teoria/t4.4-buenas practicas.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-4-desarrollo-codificacion/teoria/t4.4-buenas%20practicas.md

# T4.4 – BUENAS PRÁCTICAS Y VALIDACIÓN EN EL DESARROLLO CON IA

La IA generativa puede producir código asombrosamente bueno en segundos. Pero la regla de oro del desarrollo con IA es: nunca aceptes código que no entiendas. La IA no es un oráculo infalible. Es un modelo estadístico que predice tokens. A veces acierta con precisión milimétrica. Otras veces genera código incorrecto, inseguro o simplemente absurdo que parece correcto a simple vista. La diferencia entre un desarrollador que usa IA de forma profesional y uno que la usa de forma peligrosa está en el hábito de revisar y comprender cada línea antes de aceptarla.

El protocolo de validación para código generado por IA debe cubrir al menos estos niveles:

Nivel 1 - Verificación visual: ¿entiendo cada línea? ¿la lógica es correcta?

Nivel 2 - Verificación de dependencias: ¿las librerías importadas existen? ¿las versiones son correctas?

Nivel 3 - Ejecución de tests: ¿el código compila? ¿los tests pasan?

Nivel 4 - Validación contra requisitos: ¿cumple los criterios de aceptación?

Nivel 5 - Revisión de seguridad: ¿hay vulnerabilidades? ¿secretos hardcodeados?

Nivel 6 - Revisión de calidad: ¿type hints? ¿docstrings? ¿nombres descriptivos?

La validación en el contexto del ALM generativo adquiere una dimensión adicional. Cuando un agente autónomo genera código multi-archivo a partir de una especificación, no basta con revisar el código: debes revisar también el plan de implementación que el agente siguió, verificar que las decisiones arquitectónicas son coherentes con el resto del sistema, y asegurarte de que el código generado se integra correctamente con el existente. La trazabilidad desde el requisito hasta el código es tu mejor aliada para esta validación.

Los riesgos específicos del código generado por IA incluyen: alucinaciones de dependencias (importar librerías que no existen), código funcionalmente incorrecto (la lógica parece correcta pero produce resultados erróneos en ciertos casos), vulnerabilidades de seguridad (consultas SQL sin parametrizar, falta de validación de entradas), y desalineación con los requisitos (el código implementa algo que no se pidió u omite algo que sí se pidió).

La cultura de "piloto automático supervisado" es la mentalidad correcta. La IA acelera la parte mecánica del desarrollo —escribir código, tests, configuraciones— y el desarrollador se concentra en la parte creativa y crítica: entender el problema, tomar decisiones de diseño, validar la solución. La IA es un copiloto, no un piloto automático. La responsabilidad última de cada línea de código que llega a producción sigue siendo del desarrollador.
