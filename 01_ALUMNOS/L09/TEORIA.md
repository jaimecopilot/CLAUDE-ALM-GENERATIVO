# L09 · TEORÍA: trazabilidad y documentación viva como salida del ALM

**Duración: 60 minutos.**

## 1. Qué demuestra que una funcionalidad está terminada

Una funcionalidad no termina con «Claude dice que la ha escrito». Debe existir un camino que permita a otra persona comprender **qué necesidad se atendió**, **qué requisito la describe**, **qué código la implementa**, **qué pruebas la verifican** y **qué versión se entregó**. Esa relación se llama trazabilidad. Es bidireccional: del requisito al código y de un cambio de código a la necesidad que lo motivó.

La trazabilidad no es recopilar enlaces por estética. Si RF-03 prohíbe el solapamiento, debe poderse localizar el CA que define el conflicto, el test que fuerza dos reservas incompatibles, la implementación de la comprobación y la MR donde se revisó. Si falta uno de esos eslabones, hay deuda documental o de verificación.

## 2. Matriz de trazabilidad práctica

Para cada RF mantenemos columnas:
**RF → CA → issue GitLab → archivos de código → tests → commit/MR → pipeline**.
La fila CAM-01 incluirá además el cambio de duración máxima y los tres nuevos tests frontera. Un vínculo que todavía no existe se escribe como «pendiente» con su causa. No debe inventarse un enlace ni asociarse una MR ajena.

## 3. ¿Qué significa documentación viva?

Un README que explica cómo ejecutar el proyecto, diagramas Mermaid versionados, un ADR que registra decisiones y un informe de calidad actualizado pueden evolucionar junto al código. La IA puede regenerar descripciones y dibujos a partir de la implementación, pero el desarrollador debe comparar la salida con el código real; los diagramas generados desde textos hipotéticos pueden estar obsoletos desde el primer día.

La **documentación original de diseño** expresa una intención. La **documentación as-built** describe lo construido. Puede haber diferencias legítimas, pero necesitan explicación y decisión, no ocultación. En este laboratorio se toma el diagrama de L04 y se comprueba si el código de L05/L08 lo refleja.

## 4. Gobernanza de agentes

El repositorio debe permitir saber qué hizo la IA y qué decidió una persona. El control puede ser sencillo: mantener prompt operativo, ruta de artefactos, criterios de aceptación, logs de comandos, revisión de diff y aprobación de fase. No es necesario guardar conversaciones completas ni información personal. Se registran versiones o nombres del motor cuando se conozcan, sin inventarlos.

## 5. Alcance de un equipo junior

No aspiramos a una auditoría formal de sectores regulados. Sí exigimos disciplina mínima: documentos Markdown versionados, MRs revisadas, resultados de tests verificables y trazabilidad consistente. El senior podrá extender la matriz hacia controles más avanzados sin cambiar el caso práctico.


---


## 6. GOBIERNO DE LA IA: AUDITORÍA, TRAZABILIDAD Y CUMPLIMIENTO NORMATIVO

El uso de IA generativa en el desarrollo de software no es solo una cuestión técnica, sino también de gobernanza. A medida que los agentes de IA asumen tareas cada vez más autónomas, las organizaciones necesitan mecanismos para auditar lo que estos agentes hacen, mantener la trazabilidad de las decisiones y demostrar el cumplimiento normativo ante reguladores y auditores.

### 6.1 La trazabilidad es el pilar fundamental del gobierno de la IA
Cada acción de un agente —un plan generado, un código implementado, un test ejecutado, una PR creada— debe quedar registrada. Debes poder responder preguntas como: ¿quién aprobó este cambio?, ¿fue generado por un agente o escrito manualmente?, ¿qué modelo se usó?, ¿qué instrucciones se le dieron? La trazabilidad de extremo a extremo —desde el requisito hasta el despliegue— es lo que permite auditar el trabajo de los agentes.

### 6.2 La auditoría de decisiones de IA
La auditoría de decisiones de IA es especialmente relevante en sectores regulados (banca, seguros, salud). Cada decisión de diseño debe estar justificada y documentada. Los ADRs generados por IA deben ser revisados y aprobados por humanos. Los cambios en módulos críticos deben requerir aprobación adicional.

### 6.3 El cumplimiento normativo
El cumplimiento normativo varía según la industria y la región. Regulaciones como el AI Act de la Unión Europea imponen requisitos sobre el uso de IA en procesos críticos. Las organizaciones deben poder demostrar que mantienen supervisión humana sobre las decisiones automatizadas y que tienen procesos de validación establecidos.

### 6.4 La gestión del riesgo de IA
La gestión del riesgo de IA incluye la evaluación y mitigación de riesgos específicos: alucinaciones, sesgos, vulnerabilidades de seguridad y dependencia excesiva de la IA. Las organizaciones pueden establecer políticas que requieran revisión humana para ciertos tipos de cambios, limitar el uso de agentes autónomos a repositorios no críticos o exigir aprobación adicional para PRs que afecten a módulos de seguridad.

### 6.5 La prevención de shadow AI
La prevención de shadow AI —el uso de herramientas de IA no autorizadas por la organización— es otro aspecto del gobierno. Los desarrolladores pueden verse tentados a usar herramientas externas que no cumplen con las políticas de seguridad. Las organizaciones deben establecer políticas claras sobre qué herramientas están autorizadas y educar a los desarrolladores sobre los riesgos.

### 6.6 La medición del impacto de la IA
La medición del impacto de la IA en el ciclo de desarrollo es una capacidad emergente. Métricas como el tiempo de ciclo, la frecuencia de despliegue, la tasa de fallos en CI y la cobertura de tests permiten evaluar el retorno de inversión de la IA y ajustar las políticas de uso. El gobierno de la IA no es un obstáculo a la productividad, sino un habilitador que permite usar la IA de forma segura, auditable y alineada con los requisitos normativos.


---


## 7. CÓMO VALIDAR Y SUPERVISAR EL OUTPUT GENERADO POR LA IA

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
