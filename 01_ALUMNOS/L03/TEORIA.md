# L03 · TEORÍA: del cliente al backlog generativo

**Duración del laboratorio:** 90 minutos. Procedencia principal: Módulo 2, prácticas originales P2.1, P2.2, P2.3 y P2.6.

## Por qué la IA no puede «inventar» al cliente

Elicitar es obtener y clarificar necesidades, no rellenar una plantilla con términos técnicos. Un LLM puede sugerir preguntas, detectar contradicciones y escribir especificaciones, pero **no es el stakeholder**. El formador asumirá el papel de responsable del coworking y resolverá un conjunto limitado de preguntas de negocio. Sin este paso todos los equipos podrían producir aplicaciones incompatibles aunque las pantallas se parezcan.

Distingue un **objetivo** («evitar dobles reservas»), un **requisito funcional** («rechazar solapamientos en la misma sala») y un **criterio de aceptación** («se rechaza una solicitud que se cruza 30 minutos con una reserva existente»). El criterio tiene que poder convertirse en test, pero Gherkin no se convierte automáticamente en una prueba ejecutable: alguien deberá implementarlo o mapearlo a un test.

## Modelo mínimo de trazabilidad

Utilizaremos identificadores estables: RF-01 listar salas, RF-02 reservar, RF-03 controlar solapamiento y RF-04 cancelar. Cada RF tendrá uno o más criterios CA-xx y su issue en GitLab. La cadena es:
**necesidad → RF → criterio Gherkin → issue GitLab → archivo → test → MR y pipeline**.
No confundas una issue con una historia de usuario: GitLab registra la unidad de trabajo; la historia explica la necesidad desde un rol.

## Especificación implementable y límites

En el GitHub original se usa el término *especificación ejecutable*. En este curso significa un documento detallado que un agente puede interpretar para construir y verificar, **no una garantía** de generación correcta. Debe separar las restricciones de negocio (no solapar) de decisiones técnicas (FastAPI, SQLite), salvo que sean restricciones impuestas. El formador fija el stack, para evitar perder tiempo comparando frameworks.

Para reservas semantiza:
- Intervalos horarios **[inicio, fin)**: si una reserva acaba a las 11:00, otra puede empezar a las 11:00.
- Dos reservas colisionan cuando **inicioA < finB y inicioB < finA**, siempre que pertenezcan a la misma sala y sigan activas.
- El inicio debe ser anterior al final; una reserva cancelada no bloquea.
- Una reserva para una sala inexistente no debe crearse.
- La entrada debe incluir zona horaria o normalizarse a una convención acordada.

Estas reglas se validarán con el stakeholder antes de entrar en diseño; después servirán para testear las implementaciones independientes de cada equipo.

## Errores típicos de Claude en requisitos

Puede convertir «gestionar reservas» en facturación, login y calendarios externos; puede definir «solapamiento» de forma inconsistente; puede mezclar una decisión técnica con una condición de negocio o generar criterios que no observan resultados. El alumno debe eliminar lo que está fuera de alcance y señalar dudas reales.

**Lecturas originales completas incorporadas debajo:** elicitación, prompting para historias y ecosistema de análisis.

---

---

## Lectura original: modulo-2-analisis-requisitos/teoria/t2.1-ia-elicitacion-requisitos.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-2-analisis-requisitos/teoria/t2.1-ia-elicitacion-requisitos.md

# T2.1 – CÓMO LOS LLM ASISTEN EN LA ELICITACIÓN DE REQUISITOS

La elicitación de requisitos es la fase más temprana del desarrollo de software. Tradicionalmente consiste en reuniones con stakeholders, análisis de necesidades, tormentas de ideas y mucha documentación. Es un proceso propenso a malentendidos, omisiones y ambigüedades. Los grandes modelos de lenguaje, usados correctamente, pueden acelerar y mejorar esta fase actuando como un facilitador que ayuda a hacer las preguntas adecuadas, estructurar la información y generar borradores de documentos que luego validarás con personas reales.

El primer gran aporte de un LLM en esta fase es la generación de preguntas. Imagina que recibes una idea de negocio muy vaga: "Quiero una app para gestionar las salas de reuniones de la oficina". En lugar de empezar a escribir requisitos desde cero, puedes pedirle a una IA que actúe como analista y te formule las preguntas que deberías hacer al stakeholder. Esto te da un punto de partida estructurado y reduce el riesgo de olvidar aspectos importantes como la gestión de conflictos de horario, la cancelación de reservas o los permisos de usuario.

El segundo aporte es la descomposición de objetivos en requisitos. Un stakeholder suele expresar deseos generales, no requisitos técnicos. "Quiero que sea fácil de usar" no es un requisito, es una expectativa. Puedes pedirle a la IA que tome frases de ese estilo y las descomponga en requisitos funcionales y no funcionales concretos, medibles y verificables. Por ejemplo, "fácil de usar" podría descomponerse en "el usuario debe poder reservar una sala en menos de tres clics" o "la interfaz debe seguir las directrices de accesibilidad WCAG 2.1 nivel AA".

El tercer aporte es la identificación de casos límite y escenarios alternativos. Cuando piensas en un flujo principal —un usuario reserva una sala— es fácil olvidar los escenarios secundarios: ¿qué pasa si la sala ya está reservada? ¿y si el usuario quiere modificar la reserva? ¿y si la reserva es para dentro de un año? La IA puede generar una lista sistemática de casos límite si le proporcionas el flujo principal y le pides que los identifique. Esta capacidad de barrido es muy valiosa porque los bugs más costosos suelen nacer de requisitos no contemplados.

El cuarto aporte, y quizás el más transformador, es la generación de especificaciones ejecutables. Una especificación ejecutable no es solo un documento de requisitos: es un prompt de alta calidad que contiene suficiente contexto técnico, criterios de aceptación en formato Gherkin y restricciones explícitas como para que una IA de codificación (Copilot, ChatGPT, Claude) pueda generar una implementación funcional sin ambigüedades. Este concepto cambia radicalmente el flujo de trabajo: los requisitos no son solo artefactos para comunicarse entre personas, sino instrucciones directas para agentes de IA que van a implementar el código.

El quinto aporte es la estandarización de formatos. Cada equipo tiene su forma de escribir historias de usuario, criterios de aceptación o especificaciones. La IA puede adaptarse al formato que le proporciones. Si le muestras un ejemplo de cómo escribe historias de usuario tu equipo, podrá generar nuevas historias siguiendo exactamente ese patrón. Esto ahorra tiempo y asegura consistencia en el backlog. Además, un formato consistente es esencial cuando múltiples agentes de IA van a consumir esos requisitos para generar código.

El sexto aporte es la detección temprana de ambigüedades. Si escribes un requisito como "el sistema debe ser rápido", la IA puede señalarte que "rápido" no es medible y sugerirte que lo especifiques: "el 95% de las respuestas deben servirse en menos de 200 milisegundos". Esta función de revisor de requisitos ayuda a elevar la calidad de la especificación antes de que llegue a desarrollo, donde los requisitos ambiguos son mucho más costosos de corregir. En el contexto del ALM generativo, una ambigüedad en el requisito se traduce directamente en código incorrecto generado por la IA.

El séptimo aporte es la conexión con la generación de código. Un requisito bien redactado puede alimentar directamente a un agente de IA para que genere el código correspondiente. El flujo es: idea → elicitación con IA → especificación ejecutable → issue en GitHub/Jira/Azure DevOps → agente de IA genera código → Pull Request. Los requisitos dejan de ser un artefacto estático para convertirse en el punto de partida de un flujo automatizado de desarrollo.

Es importante que entiendas los límites de esta asistencia. La IA no sustituye las conversaciones con stakeholders reales. No tiene acceso a las particularidades de tu organización, no conoce las restricciones legales de tu sector, ni puede negociar prioridades con los responsables de negocio. Lo que genera no son requisitos validados, sino borradores que tú debes revisar, completar y contrastar con las personas adecuadas. La IA es un facilitador del proceso de análisis, un sparring que te ayuda a pensar mejor y más rápido, pero la responsabilidad de entender el problema y validar la solución sigue siendo completamente tuya.


---

## Lectura original: modulo-2-analisis-requisitos/teoria/t2.2-prompting-historias-usuario.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-2-analisis-requisitos/teoria/t2.2-prompting-historias-usuario.md

# T2.2 – TÉCNICAS DE PROMPTING PARA HISTORIAS DE USUARIO Y BACKLOG

Una historia de usuario tradicional describe una funcionalidad desde la perspectiva de quien la necesita. Pero cuando esa historia va a ser procesada por una IA para generar un backlog, documentación o incluso código, deja de ser solo un artefacto de comunicación entre personas: se convierte en un prompt ejecutable. La forma en que la redactes determina directamente la calidad del resultado. Si escribes "quiero un botón para guardar", la IA hará suposiciones que probablemente no coincidan con lo que necesitas. Si escribes una historia precisa, con contexto técnico, criterios Gherkin y restricciones explícitas, el resultado estará mucho más cerca de lo esperado.

El concepto fundamental que debes interiorizar es la generabilidad: un requisito es generable cuando una IA de codificación puede leerlo y producir código funcional sin necesidad de hacer preguntas adicionales. Una historia tradicional como "Como empleado quiero reservar una sala para poder reunirme" no es generable porque carece de detalles técnicos. Una historia generable especificaría: el endpoint REST a crear, el método HTTP, los parámetros de entrada, el formato de respuesta, las validaciones necesarias y los códigos de error esperados.

El formato base que mejor funciona mantiene la estructura clásica "Como [rol] quiero [funcionalidad] para [beneficio]", pero añade tres elementos que la convierten en un prompt de alta calidad: contexto técnico (qué parte del sistema se afecta, qué tecnologías se usan, qué archivos se modifican), criterios de aceptación ejecutables en formato Gherkin (Given-When-Then), y restricciones explícitas (lo que NO debe hacer la implementación, patrones a seguir, librerías a evitar). Estos tres elementos son los que transforman una historia de usuario en una instrucción que un agente de IA puede ejecutar.

Los criterios de aceptación en formato Gherkin son el puente entre la especificación y la verificación automática. Cuando escribes criterios en formato Given-When-Then, estás proporcionando al agente no solo una descripción del comportamiento esperado, sino también casos de prueba que puede utilizar para validar su propia salida. Si escribes "Given una sala disponible en el horario solicitado, When el usuario reserva, Then la sala queda ocupada y se devuelve un código 201", el agente entiende que debe generar el código de la reserva, la lógica de verificación de disponibilidad, la actualización del estado y la respuesta HTTP correcta. Un buen conjunto de criterios Gherkin cubre: el caso feliz, al menos dos casos de error, casos límite y escenarios de autorización.

La técnica de descomposición de épicas es otra aplicación potente cuando trabajas con IAs. Una épica es una historia de usuario grande que necesita ser dividida en historias más pequeñas. Puedes pedir a la IA: "Descompón esta épica en historias de usuario siguiendo el formato INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable), incluyendo criterios Gherkin y detalles técnicos para cada una". La IA analizará la épica y generará un conjunto de historias más pequeñas y manejables. Lo importante es que cada historia resultante sea independiente y generable por sí misma: un agente de IA debería poder implementarla sin consultar otras historias.

La ordenación por dependencias es crucial cuando el backlog va a ser procesado por agentes de IA. Los agentes implementan las tareas en el orden en que se les asignan. Si una historia depende de otra que aún no se ha implementado, el agente puede generar código incorrecto o hacer suposiciones erróneas. Puedes pedir a la IA: "Ordena estas historias de usuario por dependencias técnicas (modelos antes que servicios, servicios antes que endpoints) y marca con [P] las que pueden ejecutarse en paralelo". Esta práctica asegura que el backlog sea procesable secuencialmente.

La plantilla ideal para un prompt de análisis de requisitos que alimentará a un agente de IA incluye: título descriptivo con verbo y entidad, sección de contexto que explique el problema y la solución propuesta, sección de detalles técnicos con endpoint, método HTTP, parámetros, framework, archivos donde implementar, sección de criterios de aceptación en Gherkin (mínimo 4-5 escenarios), y sección de restricciones con lo que NO se debe hacer. Esta estructura no solo funciona para nuevas funcionalidades, sino también para bugs, refactorizaciones o mejoras de rendimiento.

La habilidad que estás desarrollando es nueva en la industria: la de escribir requisitos que son, simultáneamente, especificaciones para humanos y prompts para máquinas. En el contexto del ALM generativo, el rol del analista de requisitos evoluciona: ya no solo describe funcionalidades para que un desarrollador las implemente, sino que redacta instrucciones precisas que un agente de IA puede ejecutar directamente. Quien domine esta doble vertiente será un perfil extraordinariamente demandado.


---

## Lectura original: modulo-2-analisis-requisitos/teoria/t2.3-ecosistema-herramientas-analisis.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-2-analisis-requisitos/teoria/t2.3-ecosistema-herramientas-analisis.md

# T2.3 – ECOSISTEMA DE HERRAMIENTAS PARA ANÁLISIS DE REQUISITOS

El mercado de herramientas de IA para análisis de requisitos es amplio y diverso. No existe una herramienta única que sea la mejor para todos los casos. La elección depende del stack tecnológico de tu organización, del nivel de integración que necesites con tus herramientas de gestión de proyectos, y de si tu objetivo es solo documentar requisitos o convertirlos directamente en código mediante agentes de IA.

La primera categoría son los chats generalistas (ChatGPT, Claude, Gemini). Son la opción más flexible y accesible para elicitación conversacional, generación de historias de usuario, refinamiento iterativo y generación de documentación. Su ventaja principal es que no requieren integración con ninguna plataforma. Su desventaja es que el contexto se pierde entre sesiones y no están integrados con tus herramientas de gestión de proyectos. Son ideales para las fases iniciales de análisis, cuando estás explorando requisitos y refinando especificaciones.

La segunda categoría son los asistentes integrados en IDEs (GitHub Copilot Chat, Amazon Q Developer, Codeium). Añaden la ventaja del contexto: conocen tu repositorio, tu código y tu estructura de proyecto. Pueden generar historias de usuario que referencian archivos concretos y tienen en cuenta la arquitectura existente. Son ideales cuando el análisis de requisitos está estrechamente ligado a la implementación y necesitas que los requisitos generados sean inmediatamente accionables por el equipo de desarrollo.

La tercera categoría son los plugins de IA para gestores de proyectos. Para Jira existen herramientas como Storygenie, FastPlan, Ragent y EpicStory, que generan backlogs completos a partir de descripciones en lenguaje natural y los publican directamente en el tablero. Para Azure DevOps, la integración con GitHub Copilot permite crear Work Items y, desde ellos, disparar la generación automática de Pull Requests. Para GitLab, GitLab Duo permite generar issues y merge requests desde descripciones textuales. Estas herramientas cierran el círculo entre la planificación y la ejecución.

La cuarta categoría son los agentes autónomos (Copilot Workspace, Copilot Coding Agent, GitLab Duo Workflow). Estas herramientas representan la culminación del ALM generativo: no solo generan requisitos, sino que los transforman directamente en planes de implementación y código. El flujo es: issue con requisitos → agente analiza el repositorio → plan de implementación → código generado en múltiples archivos → tests → Pull Request. El requisito se convierte en el prompt que dispara todo el proceso.

La quinta categoría son las herramientas de especificación formal (Spec Kit, Spec-driven development). Permiten definir especificaciones estructuradas con comandos como /speckit.specify, /speckit.plan y /speckit.implement. La especificación se versiona junto al código y actúa como fuente de verdad para los agentes de IA. Son ideales para equipos que quieren un alto grado de formalismo y trazabilidad en sus requisitos.

Los criterios de elección entre estas herramientas dependen de varios factores: la integración con tu stack existente (¿usas Jira, Azure DevOps, GitLab o GitHub Issues?), el nivel de automatización deseado (¿solo quieres documentar o quieres que la IA genere código?), la trazabilidad requerida (¿necesitas auditar el camino desde el requisito hasta el despliegue?), y las restricciones de privacidad (¿puedes enviar tus requisitos a servicios cloud o necesitas soluciones on-premise?).

La tendencia en 2026 es hacia la convergencia total: las herramientas de gestión de proyectos, los repositorios de código y los asistentes de IA se están integrando en flujos unificados. Un requisito escrito en Jira puede disparar la generación de código en GitHub, que a su vez actualiza el estado del ticket automáticamente. Un Work Item en Azure DevOps puede invocar a Copilot para que genere una PR. Un issue en GitLab puede ser procesado por GitLab Duo para generar un merge request. Entender este ecosistema te permitirá elegir la combinación adecuada para tu organización y diseñar flujos de trabajo donde los requisitos fluyen sin fricción hasta convertirse en código.
