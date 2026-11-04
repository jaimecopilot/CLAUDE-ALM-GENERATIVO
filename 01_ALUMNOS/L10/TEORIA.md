# L10 · TEORÍA: evaluar un ALM completo, no una demostración llamativa

**Duración: 60 minutos.** Procedencia: Módulo 8, P8.10, y módulo 9, P9.1a.

## Qué se evalúa

El examen final no consiste en que Claude programe delante del docente. Se valora que el estudiante pueda explicar por qué existe cada artefacto, cómo se generó, qué problemas detectó, qué verificaciones se ejecutaron y qué aprobó una persona. Un equipo que ha obtenido un MVP vistoso pero no sabe mostrar su requisito y test correspondiente no ha demostrado ALM.

## Demostración guiada por evidencia

El equipo parte de una necesidad de negocio y muestra RF, criterio de aceptación, prompt operativo, código de la función, ejecución de prueba, MR e informe CI. Debe poder reproducir una reserva válida y una colisión, y explicar cómo la petición de máximo cuatro horas modificó las fases afectadas. No se exige introducir nuevas funcionalidades durante el cierre.

## Métricas con honestidad

Se puede medir número de RF, CA, pruebas ejecutadas, MRs revisadas, pipelines verificados y defectos encontrados. **No** se debe inferir «porcentaje de código escrito por Claude» sin un procedimiento de medición explícito, ni afirmar ahorros económicos o de tiempo sin línea base comparable. Una demostración en clase es un ejercicio de aprendizaje, no un estudio de productividad empresarial.

## Responsabilidades profesionales

La IA prepara propuestas, genera código y explica errores. El desarrollador conserva responsabilidad sobre requisitos, seguridad, calidad y aprobación. GitLab permite registrar decisiones y ejecuciones, pero no certifica automáticamente que la solución de negocio sea buena. La defensa final debe presentar también limitaciones: autenticación deliberadamente ausente, escala/concurrencia no probada y ausencia de despliegue productivo.

## Continuidad con el taller senior

El mismo Coworking Manager puede reutilizarse para debatir arquitectura, transacciones y concurrencia, despliegue, secretos, gobernanza de agentes y revisión cruzada. El junior debe salir dominando terminología y capacidad de inspección, no con expectativas de autonomía ilimitada del agente.

**Lecturas del curso original completas a continuación:** fundamentos del ALM generativo y retrospectiva final.

---

---

## Lectura original: modulo 9/p9.1a.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo%209/p9.1a.md

# P9.1a – LABORATORIO GUIADO: FUNDAMENTOS DEL ALM GENERATIVO

## Visión en el ALM generativo

El ALM (Application Lifecycle Management) generativo redefine el ciclo de desarrollo tradicional. En lugar de depender exclusivamente de escritura manual de código, introduce sistemas de IA que acompañan y automatizan partes del flujo: diseño, implementación, testing, DevOps y mantenimiento.

En esta fase inicial, el objetivo es entender cómo la IA se integra en el ciclo de vida del software como un acelerador de productividad y calidad.

---

## Objetivo del laboratorio

En este laboratorio aprenderás a:

- Identificar las fases del ALM generativo
- Comprender cómo la IA impacta en cada fase
- Diferenciar asistentes, agentes y plataformas
- Construir un flujo conceptual completo de desarrollo con IA

---

## Paso 1 – Identificar el ciclo ALM tradicional

Antes de introducir IA, define el ciclo clásico:

- Planificación
- Análisis
- Diseño
- Desarrollo
- Testing
- Despliegue
- Mantenimiento

**Ejercicio:**
Escribe una breve descripción de cada fase aplicada a una aplicación simple (por ejemplo: gestor de tareas).

---

## Paso 2 – Introducción del ALM generativo

Ahora reescribe el mismo ciclo, pero incorporando IA.

**Prompt sugerido:**

> “Reescribe el ciclo ALM tradicional incorporando herramientas de IA en cada fase y explica su impacto”

Observa cómo cambian los roles:

- El desarrollador deja de ser ejecutor puro
- La IA actúa como copiloto o agente
- El flujo se vuelve continuo y automatizado

---

## Paso 3 – Diferencia entre asistentes y agentes

Define claramente:

- Asistentes: herramientas que sugieren código (Copilot, Codeium)
- Agentes: sistemas que ejecutan tareas completas (Cursor Agent, Copilot Workspace)

**Ejercicio:**
Clasifica estos ejemplos:

- Autocompletado de función
- Generación de PR automática
- Explicación de código
- Implementación multiarchivo

---

## Paso 4 – Flujo completo de ALM generativo

Construye un flujo conceptual:

1. Idea o requerimiento
2. Especificación generada con IA
3. Implementación asistida o autónoma
4. Testing automático
5. Revisión con IA
6. Despliegue automatizado
7. Mantenimiento continuo

**Prompt sugerido:**

> “Diseña un flujo completo de desarrollo de software usando IA en todas las fases del ALM”

---

## Paso 5 – Reflexión técnica

Responde:

- ¿Qué fases se automatizan completamente?
- ¿Cuáles requieren supervisión humana?
- ¿Qué riesgos introduce la automatización?

---

## Conexión con el ALM generativo

Este laboratorio introduce la base conceptual sobre la que se construyen:

- Asistentes de IDE
- Agentes autónomos
- Testing automatizado
- DevOps generativo
- Gobernanza de IA

---

## Tabla conceptual

| Elemento | ALM tradicional | ALM generativo |
|----------|----------------|----------------|
| Desarrollo | Manual | Asistido por IA |
| Testing | Manual | Automatizado + IA |
| DevOps | Scripts | Generación IA |
| Mantenimiento | Reactivo | Continuo |
| Rol dev | Programador | Supervisor de IA |

---

## Reflexión final

El ALM generativo no elimina al desarrollador, pero transforma su rol: de escribir cada línea de código a diseñar sistemas que generan, validan y mantienen software.

El valor se desplaza desde la implementación hacia la supervisión, la arquitectura y la definición de intención.


---

## Lectura original: modulo-8-riesgos y buenas practicas/meta-promts/p8.10-retrospectiva y cierre.md

Fuente: https://github.com/jaimecopilot/ia-alm-2026/blob/main/modulo-8-riesgos%20y%20buenas%20practicas/meta-promts/p8.10-retrospectiva%20y%20cierre.md

# P8.10 – PROYECTO INTEGRADOR: CIERRE, RETROSPECTIVA Y REFLEXIÓN FINAL

## Herramientas cubiertas
Genérico (cualquier IA)

## Laboratorio generado por IA
Instrucción: El formador debe copiar este meta-prompt y pegarlo en ChatGPT, Claude o Gemini. La IA generará un laboratorio guiado completo listo para entregar al alumno.

## Actúa como un arquitecto de ALM Generativo
Estás diseñando el ejercicio de cierre del curso, donde los alumnos reflexionan sobre todo el ciclo de vida que han ejecutado, consolidan sus aprendizajes y generan un dashboard de calidad del proyecto.

## Objetivo del ejercicio
Que los alumnos realicen una retrospectiva completa del proyecto integrador y del curso, generen un dashboard de calidad con métricas, documenten sus aprendizajes y establezcan un plan de acción para aplicar el ALM generativo en su trabajo diario.

## Escenario
Los alumnos han completado todas las fases del proyecto integrador: análisis, diseño, implementación, testing, documentación y DevOps. Es el momento de cerrar y reflexionar.

## Estructura que debes generar

### 1. Introducción
Explica que la reflexión es parte del aprendizaje. El ALM generativo no es solo un conjunto de herramientas, sino un cambio de mentalidad sobre cómo se desarrolla software.

### 2. Técnica 1: Generar retrospectiva del proyecto
Proporciona un prompt para que el alumno pida a la IA que le ayude a estructurar una retrospectiva con secciones: qué funcionó bien, qué fue difícil, qué aprendió, qué haría diferente.

### 3. Técnica 2: Generar dashboard de calidad
Proporciona un prompt para generar un dashboard con métricas del proyecto: cobertura de tests, número de tests, endpoints implementados, ADRs documentados, diagramas generados, porcentaje de código generado por IA vs manual.

### 4. Técnica 3: Generar plan de acción post-curso
Proporciona un prompt para que el alumno pida a la IA que le ayude a crear un plan para aplicar lo aprendido en su trabajo diario: qué prácticas incorporará, qué herramientas configurará, qué compartirá con su equipo.

### 5. Técnica 4: Generar resumen ejecutivo para stakeholders
Proporciona un prompt para generar un resumen de una página sobre el valor del ALM generativo, con métricas cuantitativas y recomendaciones para adoptarlo en la organización.

### 6. Técnica 5: Reflexión personal guiada
Incluye preguntas de reflexión para el alumno: ¿cómo ha cambiado tu percepción del desarrollo con IA? ¿Qué fase del ALM generativo te resultó más valiosa? ¿Qué reservas tienes? ¿Cómo crees que evolucionará tu rol como desarrollador?

### 7. Producto final
Indica al alumno que debe entregar: retrospectiva, dashboard de calidad, plan de acción y resumen ejecutivo.

### 8. Cierre
Incluye un mensaje de cierre que felicite al alumno por completar el curso y le anime a seguir explorando el ALM generativo en su carrera profesional.
