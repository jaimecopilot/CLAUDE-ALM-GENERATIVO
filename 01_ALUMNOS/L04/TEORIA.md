# L04 · TEORÍA: diseñar con IA sin perder el control arquitectónico

**Duración:** 60 min.

## 1. Diseño como transformación de requisitos aprobados

La fase no comienza diciendo «proponme una gran arquitectura». Comienza leyendo **docs/requisitos/especificacion.md** y preguntando qué componentes mínimos cumplen esos criterios. Un diseño que ignore RF-03 (solapamiento) es incorrecto aunque tenga un diagrama elegante.

El curso fija el stack **FastAPI + SQLite + pytest** para que equipos junior no gasten tiempo eligiendo tecnologías. La IA sí puede proponer cómo dividir responsabilidades entre módulos: endpoints, servicio de reservas, persistencia, validaciones y tests. La arquitectura se evalúa por adecuación y legibilidad, no por número de capas o patrones.

## 2. Arquitectura, diagrama y decisión son cosas distintas

**Arquitectura:** componentes y responsabilidades que limitan la implementación. **Diagrama C4:** vista de actores, sistemas y contenedores; no representa necesariamente cada clase del código. **UML de clases:** entidades, asociaciones y atributos. **ADR:** registro corto de una decisión, alternativas descartadas y consecuencias. El *sparring arquitectónico* consiste en pedir a Claude que critique una decisión bajo restricciones concretas y luego decidir con criterio humano.

Para Coworking Manager un diseño razonable contempla los conceptos Sala y Reserva y una función de disponibilidad. No necesitamos Kubernetes ni mensajería. Un ADR útil puede justificar SQLite para un taller local y describir cuándo habría que reconsiderarlo; no deben inventarse beneficios que no existen.

## 3. Dónde debe vivir la regla de solapamiento

Un endpoint que guarda solicitudes sin comprobar el intervalo viola el requisito. La regla debe estar en una función o servicio verificable, no escondida en la interfaz. La condición de intersección entre intervalos activos permite diseñar tests independientes. La implementación concreta puede variar, pero el comportamiento de negocio es fijo.

## 4. La paradoja de los diagramas generados

Claude puede producir diagramas que parecen correctos, pero no corresponden al código finalmente generado. En L04 el diagrama es **diseño propuesto**; en L09 se comparará contra la implementación real. Si hay cambios, se documentan: no se «arregla» el diagrama borrando decisiones incómodas.

## 5. Criterio de paso

Solo avanza la fase cuando hay: modelo de entidades coherente, diagrama legible versionable, al menos un ADR y correspondencia explícita con RF-01..RF-04. No hay que desarrollar la aplicación aquí; el output de diseño alimentará L05.


---


## 6. LA IA COMO SPARRING ARQUITECTÓNICO

Diseñar la arquitectura de un sistema es una de las tareas más desafiantes en el desarrollo de software. Implica tomar decisiones que afectarán a todo el proyecto: ¿monolito o microservicios? ¿SQL o NoSQL? ¿Arquitectura hexagonal o en capas? La IA generativa, usada correctamente, puede actuar como un sparring arquitectónico: un compañero de diseño que te ayuda a explorar alternativas, evaluar trade-offs, identificar riesgos y documentar decisiones. No sustituye tu criterio, pero lo amplifica.

El concepto de sparring arquitectónico se basa en un principio simple: la IA no toma decisiones por ti, pero puede generar un abanico de opciones que quizás no habías considerado. Puedes plantearle un trade-off —"¿monolito modular o microservicios para un equipo de 5 desarrolladores?"— y pedirle que analice ambas opciones desde múltiples perspectivas: escalabilidad, complejidad operativa, velocidad de desarrollo, curva de aprendizaje y coste de infraestructura. La IA te devolverá un análisis estructurado que puedes usar como base para tu decisión.

Una de las capacidades más potentes del sparring arquitectónico es la evaluación comparativa de alternativas. Puedes pedir a la IA que compare dos arquitecturas, dos stacks tecnológicos o dos patrones de diseño, y que lo haga considerando no solo factores técnicos sino también organizacionales: tamaño del equipo, experiencia existente, restricciones de tiempo y presupuesto. La IA puede incluso simular cómo evolucionaría cada opción a medida que el sistema crece, ayudándote a pensar a largo plazo.

El sparring arquitectónico también puede ayudarte a identificar riesgos y puntos ciegos. Después de describir tu arquitectura propuesta, puedes preguntar: "¿Qué puede fallar con este diseño?" o "¿Qué casos de uso no estoy considerando?". La IA analizará tu propuesta y señalará posibles problemas: cuellos de botella, puntos únicos de fallo, problemas de escalabilidad o inconsistencias. Esta capacidad de "abogado del diablo" es especialmente valiosa antes de comprometerte con una arquitectura.

La generación de múltiples escenarios es otra técnica potente. Puedes pedir a la IA: "Genera tres arquitecturas diferentes para este sistema: una mínima viable (MVP), una escalable para crecimiento futuro y una de alta disponibilidad". Cada opción vendrá con sus pros, contras y costes asociados. Esto te permite presentar alternativas a los stakeholders y tomar decisiones informadas.

El sparring arquitectónico con IA también puede conectar los requisitos con el diseño. Si le proporcionas una especificación ejecutable (como las que aprendiste a crear en el Módulo 2), la IA puede inferir la arquitectura implícita en esos requisitos y proponer un diseño coherente. Por ejemplo, si la especificación menciona "notificaciones asíncronas" y "tolerancia a fallos", la IA puede sugerir un patrón de cola de mensajes o un outbox pattern.

Una práctica recomendada es usar múltiples IAs para la misma decisión de diseño. Diferentes modelos (ChatGPT, Claude, Gemini) tienen diferentes sesgos y fortalezas. ChatGPT puede ser más directo y práctico, Claude más analítico y matizado, Gemini puede ofrecer perspectivas actualizadas. Comparar sus recomendaciones te da una visión más completa y te ayuda a identificar sesgos en las respuestas.

Es importante entender las limitaciones del sparring arquitectónico con IA. La IA no tiene experiencia real desplegando sistemas en producción, no conoce las restricciones específicas de tu organización y puede sesgar sus recomendaciones hacia patrones populares en GitHub. No sustituye la experiencia de un arquitecto humano ni el conocimiento del dominio de negocio. La decisión final, con todo su contexto y responsabilidad, sigue siendo tuya.

El resultado del sparring arquitectónico no debería quedarse solo en una conversación. Debe materializarse en artefactos concretos: diagramas de arquitectura (C4, UML), Architecture Decision Records (ADRs) que documenten las decisiones y su justificación, y prototipos o pruebas de concepto. La IA puede ayudarte a generar todos estos artefactos a partir de la conversación de diseño.


---


## 7. GENERACIÓN DE DIAGRAMAS UML Y C4 CON IA

Los diagramas de arquitectura y UML han sido tradicionalmente un punto de fricción en el desarrollo de software. Se dibujan al inicio del proyecto, se desactualizan rápidamente y rara vez reflejan lo que realmente hay en producción. La IA generativa, combinada con lenguajes de diagramación como código —Mermaid y PlantUML—, cambia esta realidad: ahora puedes generar diagramas directamente desde descripciones en lenguaje natural, mantenerlos versionados junto al código y regenerarlos automáticamente cuando la arquitectura evoluciona.

El concepto de diagramas como código es fundamental. Mermaid y PlantUML son lenguajes que permiten definir diagramas mediante texto plano. Esto significa que los diagramas no son imágenes binarias (PNG, JPEG) sino artefactos de texto que pueden versionarse en Git, revisarse en Pull Requests y regenerarse con un simple comando. La IA puede generar el código Mermaid o PlantUML, y tú puedes refinarlo conversacionalmente hasta que refleje fielmente la arquitectura deseada.

Los diagramas C4 (Context, Container, Component, Code) son un estándar de facto para documentar arquitectura de software en cuatro niveles de abstracción. El nivel de Contexto muestra el sistema y sus relaciones con usuarios y sistemas externos. El nivel de Contenedor muestra las aplicaciones y bases de datos que componen el sistema. El nivel de Componente muestra los módulos dentro de cada contenedor. El nivel de Código muestra clases y funciones. La IA puede generar cada uno de estos niveles a partir de una descripción textual.

Los diagramas UML (clases, secuencia, casos de uso, estados, actividades) complementan a los diagramas C4. Un diagrama de clases muestra las entidades del dominio y sus relaciones. Un diagrama de secuencia muestra cómo los componentes interactúan en un flujo concreto. Un diagrama de estados muestra el ciclo de vida de una entidad. La IA puede generar cualquiera de estos diagramas a partir de una especificación ejecutable o de una descripción en lenguaje natural.

La iteración visual conversacional es el flujo de trabajo más productivo. Describes el diagrama que necesitas, la IA genera el código Mermaid, lo renderiza, y tú pides cambios: "Añade un balanceador de carga delante de la API", "Muestra la relación entre el servicio de reservas y el de notificaciones", "Cambia la cardinalidad de esta relación". Cada iteración es inmediata y no requiere tocar una herramienta de dibujo.

La generación de diagramas desde requisitos cierra el círculo entre análisis y diseño. Si has creado una especificación ejecutable en el Módulo 2, puedes pedir a la IA: "Basándote en esta especificación, genera un diagrama C4 de contenedores". La IA extraerá los componentes mencionados en los requisitos (APIs, bases de datos, servicios externos) y los organizará en un diagrama coherente. Esto asegura que el diseño está alineado con lo que se pidió.

La ingeniería inversa visual es otra capacidad valiosa. Puedes pedir a la IA: "Analiza este código y genera un diagrama de clases UML de su estructura actual". La IA leerá el código, extraerá clases, atributos, métodos y relaciones, y generará un diagrama que refleje la implementación real. Esto es especialmente útil para documentar código legacy que nunca fue documentado.

La comparación entre diseño e implementación es una práctica recomendada. Genera un diagrama desde la especificación (diseño previsto) y otro desde el código real (diseño implementado). Compara ambos. ¿Hay diferencias? ¿El código se desvió del diseño? ¿El diseño era inviable y el código tomó un camino diferente? Esta comparación es invaluable para mantener la integridad arquitectónica.


---


## 8. EVALUACIÓN DE DECISIONES TÉCNICAS CON IA

Tomar decisiones técnicas es una de las responsabilidades más delicadas del desarrollo de software. Una mala decisión temprana —elegir la base de datos equivocada, una arquitectura que no escala, un framework que limita— puede lastrar el proyecto durante años. La IA generativa puede actuar como un comité de evaluación que te ayuda a analizar opciones, identificar trade-offs ocultos y documentar el razonamiento detrás de cada decisión.

La técnica de evaluación multi-perspectiva consiste en pedir a la IA que analice una decisión desde múltiples ángulos: técnico (rendimiento, escalabilidad, mantenibilidad), organizacional (curva de aprendizaje, adecuación al equipo), económico (coste de infraestructura, licencias) y temporal (tiempo de implementación, deuda técnica futura). Por ejemplo: "Compara PostgreSQL y MongoDB para un sistema de reservas con alta concurrencia, considerando el modelo de datos, las consultas de solapamiento, las transacciones y la experiencia del equipo".

La evaluación con múltiples IAs es una práctica que reduce el sesgo. Diferentes modelos tienen diferentes sesgos de entrenamiento. ChatGPT puede favorecer soluciones más populares, Claude puede ser más analítico y señalar matices que otros pasan por alto, Gemini puede ofrecer información más actualizada. Plantear la misma decisión a varias IAs y comparar sus análisis te da una visión más completa y te ayuda a identificar sesgos.

Los Architecture Decision Records (ADRs) son el formato estándar para documentar decisiones técnicas. Un ADR incluye: contexto (por qué se necesita tomar esta decisión), decisión (qué se ha decidido), alternativas consideradas (con pros y contras de cada una) y consecuencias (qué implica esta decisión a futuro). La IA puede generar ADRs automáticamente a partir de la conversación de evaluación.

La evaluación de riesgos es una extensión natural de la evaluación de decisiones. Después de analizar las opciones y tomar una decisión, puedes pedir a la IA: "Para la arquitectura que hemos elegido, identifica los 3 principales riesgos y sugiere estrategias de mitigación". Esto te ayuda a anticipar problemas antes de que ocurran.

La verificación de coherencia es una técnica avanzada. Después de tomar varias decisiones técnicas, puedes pedir a la IA: "Revisa estas decisiones y dime si hay alguna incoherencia o conflicto entre ellas". Por ejemplo, elegir una arquitectura de microservicios pero también elegir una base de datos compartida sería una incoherencia que la IA puede detectar.

La documentación automática de decisiones cierra el ciclo. Cada decisión evaluada debe quedar documentada en un ADR versionado en el repositorio. La IA puede generar estos ADRs y mantener una tabla de contenido actualizada. Esto es especialmente valioso en entornos regulados donde cada decisión de diseño debe ser auditable.
