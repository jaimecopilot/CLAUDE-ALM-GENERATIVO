# L02 · TEORÍA: cómo se ejecuta realmente un ALM generativo

**Duración total: 90 min.**

## 1. No confundas tres sistemas

**GitHub del curso:** contiene la documentación que estudias, preparada por el formador. **GitLab del equipo:** contiene el proyecto que desarrolla el alumno, su historial, sus issues, sus MRs y sus pipelines. **Claude Code:** es el motor generativo que trabaja con los archivos del clon local y, cuando tiene autorizaciones adecuadas, puede leerlos, modificarlos y ejecutar comandos. Tener estos tres sistemas en el mismo ordenador no los convierte en un servicio automáticamente conectado.

La estructura de trabajo de GitLab será **alm/** (metaprompts, contratos, prompts generados y evidencias), **docs/** (requisitos, arquitectura, calidad y trazabilidad), **app/** (implementación), **tests/** y **.gitlab-ci.yml**. Antes de comenzar cada fase, Claude debe comprobar la existencia de las entradas esperadas.

## 2. Contrato de fase

Una fase formal posee: 1) identificación; 2) entradas reales; 3) actividad; 4) archivos de salida; 5) restricciones; 6) evidencia de aceptación; 7) criterio para avanzar. Un contrato de requisitos, por ejemplo, no describe el código: indica que debe producir **docs/requisitos/especificacion.md** y **docs/requisitos/backlog.md**, con cuatro requisitos identificados y escenarios comprobables.

## 3. Por qué dos generaciones

**Primera generación (metaprompt):** se lee el contrato y el estado real, y Claude crea **alm/prompts-generados/01-requisitos.md** para ese proyecto y ese momento. **Segunda generación (prompt operativo):** el alumno revisa y aprueba ese prompt; Claude lo ejecuta y genera los documentos de requisitos. Repetimos la cadena con arquitectura, código, calidad, entrega y evolución. No hay que generar diez versiones decorativas de un mismo documento.

El **gate de aprobación** es una decisión humana documentada, no un botón mágico. Debe constar por qué se aprueba una salida y qué prueba o revisión la justifica. La fase documental requiere validación de contenido; la técnica precisa comandos y resultados reales.

## 4. GitLab no genera automáticamente el ALM

GitLab registra issues, commits, Merge Requests y ejecuta **CI/CD** mediante jobs. Es un soporte de colaboración y verificación. El pipeline de ALM generativo es el **orden lógico** de metaprompts y contratos. Si en este taller Claude Code se ejecuta localmente, GitLab por sí solo no lo invoca al cerrar una issue. Automatizar esa invocación exigiría otra integración y posiblemente facturación API. No la incluimos.

## 5. Seguridad y control de costes

El agente recibe acceso únicamente al proyecto didáctico; no debe leer credenciales, borrar ramas o ejecutar comandos destructivos sin revisión. Evita enviar toda la documentación docente como contexto para cada fase. Reutiliza solo documentos aprobados y relevantes. Este principio reduce coste, ambigüedad y tiempo.


---


## 6. Cómo funcionan las herramientas de IA generativa

Cuando usas un chat de IA —ChatGPT, Claude, Gemini— o un asistente integrado en el IDE —Copilot, Codeium, Amazon Q Developer—, estás utilizando esencialmente la misma tecnología base: grandes modelos de lenguaje. Sin embargo, no son el mismo producto ni funcionan exactamente igual. La diferencia fundamental está en el contexto y la especialización. Un chat generalista está diseñado para mantener diálogos sobre casi cualquier tema. Un asistente de código está especializado en programación e integrado en tu entorno de desarrollo, utilizando el contexto de tu editor para generar sugerencias relevantes.

Los **chats generalistas** funcionan como sistemas de diálogo. Tú escribes un prompt y el modelo genera una respuesta token a token, prediciendo en cada paso cuál es la palabra más probable. No buscan la respuesta en una base de datos: basándose en todo lo que han leído durante su entrenamiento, generan una respuesta estadísticamente probable. Esa generación no es determinista. Existe un parámetro llamado **temperatura** que controla cuánta aleatoriedad introduce el modelo. Con temperatura baja, tiende a elegir las palabras más probables (respuestas predecibles y conservadoras). Con temperatura alta, explora opciones menos probables (respuestas más creativas pero más arriesgadas).

Los **asistentes de código integrados en el IDE** van un paso más allá. No dependen solo del prompt que escribes, sino que inyectan automáticamente una enorme cantidad de contexto adicional: el archivo actual, las pestañas abiertas, el tipo de proyecto, los imports, el historial reciente de cambios e incluso, en versiones empresariales, otros repositorios de tu organización. Esto hace que sus sugerencias sean mucho más relevantes para tu tarea concreta. La diferencia con un chat generalista es que no necesitas explicarle tu proyecto: ya lo está viendo.

La **ventana de contexto** es otro concepto fundamental. Es la cantidad máxima de tokens que el modelo puede tener en cuenta a la vez. Los modelos modernos tienen ventanas de contexto de cientos de miles de tokens, equivalentes a libros enteros. Esto significa que pueden mantener conversaciones largas o analizar archivos de código extensos sin perder el hilo. Cuando la ventana de contexto se llena, el modelo "olvida" las partes más antiguas de la conversación, lo que explica por qué a veces pierde coherencia en diálogos muy largos.

Las diferencias clave entre herramientas determinan cuándo usar cada una. Los chats generalistas son mejores para exploración conceptual, aprendizaje de nuevos temas y tareas que no requieren integración con tu código. Los asistentes de IDE son mejores para productividad inmediata durante la codificación. La práctica más efectiva no es elegir uno, sino saber cuándo usar cada uno: el asistente de IDE para autocompletado y consultas contextuales, el chat generalista para aprendizaje, exploración de ideas y tareas de arquitectura.

En el resto de este curso aplicarás principios de prompting que funcionan en cualquier herramienta, pero te centrarás en el ecosistema de asistentes de desarrollo por su integración directa con el flujo de trabajo. Los fundamentos que aprenderás —claridad, contexto, rol, formato, ejemplos, iteración— son universales y se aplican igualmente a cualquier IA generativa.


---


## 7. GOBIERNO DE LA IA: AUDITORÍA, TRAZABILIDAD Y CUMPLIMIENTO NORMATIVO

El uso de IA generativa en el desarrollo de software no es solo una cuestión técnica, sino también de gobernanza. A medida que los agentes de IA asumen tareas cada vez más autónomas, las organizaciones necesitan mecanismos para auditar lo que estos agentes hacen, mantener la trazabilidad de las decisiones y demostrar el cumplimiento normativo ante reguladores y auditores.

### 7.1 La trazabilidad es el pilar fundamental del gobierno de la IA
Cada acción de un agente —un plan generado, un código implementado, un test ejecutado, una PR creada— debe quedar registrada. Debes poder responder preguntas como: ¿quién aprobó este cambio?, ¿fue generado por un agente o escrito manualmente?, ¿qué modelo se usó?, ¿qué instrucciones se le dieron? La trazabilidad de extremo a extremo —desde el requisito hasta el despliegue— es lo que permite auditar el trabajo de los agentes.

### 7.2 La auditoría de decisiones de IA
La auditoría de decisiones de IA es especialmente relevante en sectores regulados (banca, seguros, salud). Cada decisión de diseño debe estar justificada y documentada. Los ADRs generados por IA deben ser revisados y aprobados por humanos. Los cambios en módulos críticos deben requerir aprobación adicional.

### 7.3 El cumplimiento normativo
El cumplimiento normativo varía según la industria y la región. Regulaciones como el AI Act de la Unión Europea imponen requisitos sobre el uso de IA en procesos críticos. Las organizaciones deben poder demostrar que mantienen supervisión humana sobre las decisiones automatizadas y que tienen procesos de validación establecidos.

### 7.4 La gestión del riesgo de IA
La gestión del riesgo de IA incluye la evaluación y mitigación de riesgos específicos: alucinaciones, sesgos, vulnerabilidades de seguridad y dependencia excesiva de la IA. Las organizaciones pueden establecer políticas que requieran revisión humana para ciertos tipos de cambios, limitar el uso de agentes autónomos a repositorios no críticos o exigir aprobación adicional para PRs que afecten a módulos de seguridad.

### 7.5 La prevención de shadow AI
La prevención de shadow AI —el uso de herramientas de IA no autorizadas por la organización— es otro aspecto del gobierno. Los desarrolladores pueden verse tentados a usar herramientas externas que no cumplen con las políticas de seguridad. Las organizaciones deben establecer políticas claras sobre qué herramientas están autorizadas y educar a los desarrolladores sobre los riesgos.

### 7.6 La medición del impacto de la IA
La medición del impacto de la IA en el ciclo de desarrollo es una capacidad emergente. Métricas como el tiempo de ciclo, la frecuencia de despliegue, la tasa de fallos en CI y la cobertura de tests permiten evaluar el retorno de inversión de la IA y ajustar las políticas de uso. El gobierno de la IA no es un obstáculo a la productividad, sino un habilitador que permite usar la IA de forma segura, auditable y alineada con los requisitos normativos.

## Integración técnica del entorno

Claude Code puede ejecutar las prácticas sobre el clon del proyecto GitLab abierto en VS Code. **Git realiza la sincronización de código**, mientras que GitLab web, MCP o `glab` (opcionales) proporcionan acceso a issues, Merge Requests y pipelines. Claude web + MCP permite editar directamente archivos remotos, pero no ofrece terminal para ejecutar el código. Consulta la [guía transversal](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md) para alternar las herramientas sin pisar cambios.
