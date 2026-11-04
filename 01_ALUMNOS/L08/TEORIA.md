# L08 · TEORÍA: mantenimiento y propagación de un cambio por todo el ALM

**Duración: 60 min.**

## 1. Por qué mantenimiento no equivale a «cambia una línea»

Un cambio pequeño de negocio puede atravesar el ciclo completo. El cliente añade una norma: **ninguna reserva puede superar cuatro horas de duración**. Este límite afecta a la especificación, quizá al modelo o servicio, a la validación de entrada, a las pruebas de frontera, a la documentación y a la evidencia CI. Si solo se modifica el endpoint y no se actualizan pruebas y requisitos, el sistema deja de ser trazable.

**Cambio de requisito:** modifica el comportamiento esperado. **Bug:** la implementación no cumple un requisito ya aprobado. **Refactorización:** modifica estructura interna sin cambiar comportamiento. **Deuda técnica:** coste futuro derivado de compromisos de calidad. No son sinónimos y tienen efectos distintos sobre las pruebas.

## 2. Análisis de impacto como primera generación

El ALM generativo no significa ejecutar nuevamente todas las fases a ciegas. Primero Claude debe identificar qué RF/CA son afectados, qué módulos y tests dependen de ellos y qué decisiones de arquitectura siguen vigentes. Se pide un **plan de impacto** breve y revisable. Después se actualizan solo artefactos necesarios y se vuelve a verificar.

Una regla nueva que limita duración debería incluir casos límite:
- de 3 h 59 min → aceptada si no colisiona con otra;
- exactamente 4 h → aceptada;
- 4 h 01 min → rechazada;
- intervalo inválido → rechazado por la validación ya existente.
La zona horaria y los intervalos [inicio,fin) se mantienen.

## 3. Versionado y regresión

Un cambio se desarrolla en rama propia e issue nueva, para observar la diferencia frente a la versión inicial. Los tests anteriores deben seguir pasando; se añaden casos específicos de duración máxima. Se revisa el diff y se ejecuta de nuevo CI. La MR debe explicar qué requisito cambió, qué fue modificado, qué tests nuevos lo comprueban y qué quedó intacto.

## 4. Qué puede automatizar Claude

Puede redactar análisis de impacto, modificar documentación, editar código, generar tests y preparar el resumen de MR. No debería saltarse una decisión de negocio ambigua ni afirmar haber ejecutado GitLab si no lo ha hecho. Que la IA sea capaz de cambiar archivos no significa que esté autorizada a publicar una versión sin revisión humana.

## 5. El ejemplo como mecanismo de homogeneización

Todos los juniors y seniors partirán del mismo cambio de cuatro horas. En junior se revisa el flujo y sus evidencias; en senior se pueden introducir concurrencia real, estrategias de migración, revisión de agentes o gobernanza más exigente. Así se comparte vocabulario y resultado observable.


---


## 6. ANÁLISIS DE CÓDIGO LEGADO CON IA: EXPLICACIÓN Y COMPRENSIÓN

El código legado es una realidad en prácticamente cualquier organización que lleve más de unos años desarrollando software. Se caracteriza por la falta de documentación actualizada, la ausencia de los desarrolladores originales y una estructura que puede parecer caótica a primera vista. La IA generativa se ha convertido en una herramienta de primera línea para abordar este desafío: puede explicar qué hace un fragmento de código, en qué contexto opera, cómo se relaciona con el resto del proyecto y generar diagramas visuales de su estructura.

La explicación de código con IA es el punto de partida. Proporcionas el código que quieres entender —una función, una clase o un módulo completo— y pides a la IA que lo explique. La IA analiza la sintaxis, infiere la lógica de negocio subyacente y te devuelve una explicación en lenguaje natural. Puedes pedir diferentes niveles de profundidad: una visión general de alto nivel, una explicación línea por línea, o una explicación orientada a la lógica de negocio (ignorando los detalles de implementación).

La explicación para diferentes audiencias es una capacidad valiosa. Puedes pedir a la IA que explique el mismo código a un desarrollador senior (con detalles técnicos), a un desarrollador junior (con más contexto y menos jerga) o a un stakeholder no técnico (con analogías de negocio). Esto facilita la comunicación entre equipos y la incorporación de nuevos miembros al proyecto.

La generación de diagramas desde código legacy es ingeniería inversa visual. Puedes pedir a la IA: "Analiza este código y genera un diagrama de clases UML de su estructura actual" o "Genera un diagrama de flujo de esta función". La IA extraerá clases, métodos, atributos y relaciones, y generará un diagrama en Mermaid o PlantUML que refleja la implementación real. Esto es invaluable para documentar sistemas que nunca fueron documentados formalmente.

La identificación de dependencias ocultas es otra faceta crucial. El código legacy a menudo tiene acoplamientos no documentados entre módulos. Puedes pedir a la IA: "Analiza este código y dime qué dependencias tiene con otros módulos del proyecto". La IA examinará los imports, las referencias a clases y funciones externas y las dependencias de datos, proporcionando un mapa de conexiones que el código original no documenta.

La identificación de código muerto es una tarea tediosa pero esencial. Puedes pedir a la IA: "Analiza este archivo y señala funciones, clases o bloques de código que parezcan no ser utilizados en ninguna parte del proyecto". La IA buscará referencias a esos elementos y te indicará qué partes son candidatas a eliminación. Sin embargo, debes verificar manualmente: la IA puede no detectar usos dinámicos como reflection o imports condicionales.

La generación de tests de caracterización es una técnica poderosa para código legacy sin tests. Consiste en generar tests que capturen el comportamiento actual del código, incluyendo posibles bugs. Estos tests sirven como red de seguridad para futuras refactorizaciones: si la refactorización cambia el comportamiento, los tests lo detectarán. Puedes pedir a la IA: "Genera tests de caracterización para esta función, basados en su comportamiento actual, no en el comportamiento esperado".


---


## 7. DOCUMENTACIÓN AUTOMÁTICA Y DETECCIÓN DE DEUDA TÉCNICA

La documentación desactualizada es uno de los problemas más persistentes en el mantenimiento de software. La IA generativa aborda este problema permitiendo generar documentación directamente desde el código fuente, asegurando que lo documentado refleja lo implementado. Además, la IA puede analizar el código en busca de deuda técnica —code smells, duplicación, complejidad excesiva— y sugerir refactorizaciones priorizadas.

La generación de docstrings es la forma más básica de documentación automática. Proporcionas una función o clase sin documentar y la IA genera docstrings en el formato que prefieras (Google, NumPy, Sphinx). Los docstrings incluyen descripción, parámetros con tipos, valor de retorno y excepciones. Puedes pedir que se generen para un archivo completo o para todo el proyecto.

La generación de READMEs y documentación de módulo va un paso más allá. Puedes pedir a la IA: "Genera un README.md para este módulo explicando su propósito, estructura, dependencias y ejemplos de uso". La IA analiza el código y genera documentación contextualizada que facilita la incorporación de nuevos desarrolladores.

La generación de diagramas de arquitectura desde código es documentación visual viva. Puedes pedir: "Genera un diagrama C4 de contenedores basado en el código actual" o "Genera un diagrama de secuencia del flujo principal". La IA analiza la estructura del proyecto y genera diagramas que reflejan la arquitectura real, no la idealizada. Al estar en formato Mermaid, pueden versionarse y regenerarse cuando el código cambia.

La detección de deuda técnica es otra faceta del mantenimiento asistido por IA. Puedes pedir a la IA que analice tu código en busca de: métodos demasiado largos, alta complejidad ciclomática, acoplamiento excesivo, falta de cohesión, duplicación de código, dependencias circulares y falta de tests. La IA devuelve un informe detallado con sugerencias de mejora priorizadas.

La cuantificación de deuda técnica es útil para comunicar la necesidad de refactorización a stakeholders. Puedes pedir a la IA que estime el tiempo necesario para resolver cada code smell identificado. Esto permite construir un business case para dedicar tiempo a la mejora del código.

La generación de ADRs retrospectivos es una práctica valiosa. Si el código implementa patrones o decisiones arquitectónicas que nunca fueron documentadas, puedes pedir a la IA: "Analiza este código y genera ADRs documentando las decisiones arquitectónicas que infieras de la implementación". Esto crea documentación histórica que ayudará a futuros desarrolladores a entender por qué el código es como es.


---


## 8. ACTUALIZACIÓN DE DEPENDENCIAS Y MODERNIZACIÓN DE CÓDIGO

La gestión de dependencias es una de las tareas de mantenimiento más críticas y a menudo descuidadas. Las dependencias desactualizadas pueden contener vulnerabilidades de seguridad conocidas, bugs ya corregidos en versiones posteriores o incompatibilidades con otras librerías. La IA puede ayudar a identificar dependencias problemáticas y planificar actualizaciones seguras.

La auditoría de dependencias con IA consiste en pedir a la IA que analice tu archivo de dependencias (requirements.txt, package.json, etc.) y señale: versiones desactualizadas, vulnerabilidades conocidas, dependencias sin versión fija (rangos abiertos) y dependencias aparentemente no utilizadas. La IA contrasta con su conocimiento de ecosistemas y patrones de uso.

La planificación de actualizaciones seguras es el siguiente paso. La IA puede sugerir un plan de actualización priorizado: primero vulnerabilidades críticas, luego actualizaciones menores sin breaking changes y finalmente actualizaciones mayores con breaking changes. Para cada paso puede indicar riesgos y tests de validación necesarios.

La modernización de código es una de las tareas más ambiciosas del mantenimiento. Consiste en migrar entre frameworks (Flask a FastAPI), lenguajes (Java a Python), versiones (Python 2 a Python 3) o estilos (JavaScript ES5 a TypeScript). La IA acelera la traducción mecánica y estructural del código.

La modernización con tests de caracterización es la estrategia más segura. Primero se generan tests que capturan el comportamiento actual del sistema. Luego la IA genera la versión modernizada. Finalmente, los tests verifican que el comportamiento se mantiene intacto. Actúan como red de seguridad.

La modernización incremental es preferible a las grandes reescrituras. Se migra módulo a módulo, validando cada paso. La IA puede ayudar a ordenar la migración según dependencias internas del sistema.

Los riesgos de la modernización automática deben gestionarse. La IA puede introducir errores sutiles en concurrencia, tipos o manejo de excepciones. Además, el código resultante puede ser funcional pero no idiomático en el nuevo entorno. La revisión humana y los tests siguen siendo imprescindibles.
