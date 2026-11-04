# Guía del formador — Taller de 16 horas de Vibe Coding y ALM generativo

**Destinatarios:** desarrolladores junior; conocimiento básico de programación. **Motor:** Claude Code. **Gestión:** GitLab. **Caso:** Coworking Norte.

## 1. Tesis que debe quedar clara

Este no es un curso para «hacer prompts mejores» ni una sesión de creación rápida de aplicaciones. El alumno debe ver cómo **la IA genera las especificaciones y demás artefactos de cada fase** y cómo esos resultados se relacionan mediante una cadena verificable de ALM. Vibe Coding introduce la experiencia de interacción; la ingeniería generativa aporta disciplina, trazabilidad, criterios de aprobación y control humano.

No confundas un **metaprompt** con un prompt directo: el metaprompt fabrica **alm/prompts-generados/NN-fase.md** a partir del estado real y del contrato de fase. El prompt generado, aprobado por el alumno, produce el artefacto. Hay dos aprobaciones: del plan y del resultado.

## 2. Material que recibe cada participante

El **GitHub del curso** contiene para cada laboratorio TEORIA, PRACTICA y METAPROMPT. En TEORIA se desarrollan los conceptos y sus aplicaciones prácticas. PRACTICA incluye tiempos, comandos, pasos, casos de comprobación y criterios. METAPROMPT es el texto que el alumno ejecuta para generar instrucciones operativas, no el resultado final. Todos los archivos están a la vista; los alumnos no dependen del manual abreviado de la versión anterior.

El **GitLab personal de cada alumno** recibe exclusivamente el contenido de **03_GITLAB_PLANTILLA/**: CLAUDE.md, alm/contratos/, alm/metaprompts/, estructura vacía de docs y app, plantillas de issue/MR. El código y la especificación de negocio **no** se proporcionan como solución ya escrita.

## 3. Preparación obligatoria antes de la primera clase

- Confirmar que todos pueden abrir los recursos de teoría y prácticas de GitHub. No se facilitan cuentas GitLab compartidas: cada alumno inicia sesión en la suya.
- Cada alumno crea su proyecto GitLab personal privado y copia 03_GITLAB_PLANTILLA a la raíz, con acompañamiento del formador; debe poder clonar, subir ramas y abrir MR.
- Comprobar que Claude Code se abre en el directorio y reconoce CLAUDE.md; se utiliza cuenta personal con acceso autorizado, no credenciales compartidas.
- Reservar un GitLab Runner accesible para la fase CI/CD y verificar que la instancia admite jobs según sus límites. No prometer CI remoto sin runner.
- Preparar una solución exclusiva del formador fuera del repositorio que ven los alumnos y una serie de checkpoints marcados como **ayuda docente**.
- Acordar previamente la convención de datos temporales, no esperar a que la IA improvise una diferente en cada equipo.
- No lanzar los jobs de Claude dentro de GitLab hasta tener presupuestos API delimitados; Pro no cubre ese consumo.

## 4. Agenda docente y ejecución de los laboratorios

**La jornada tiene dos experiencias deliberadamente distintas:** ejecución manual supervisada de L01–L09 y pipeline ALM automatizado en GitLab en L10, con la misma especificación inicial. La ejecución en runner GitLab requiere API de Anthropic o un proveedor compatible, facturada separadamente de Claude Pro; debe aprobarse un presupuesto antes de ejecutarla.

| Día | Bloque | Duración | Objetivo | Archivo de sesión |
|---|---|---:|---|---|
| 1 | L01 Vibe Coding | 30 min | Supuestos y validación | [L01](./SESIONES/L01.md) |
| 1 | L02 GitLab personal y Claude | 90 min | Cuenta, proyecto privado y etiqueta inicial | [L02](./SESIONES/L02.md) |
| 1 | L03 Requisitos | 90 min | RF, Gherkin, backlog e issues | [L03](./SESIONES/L03.md) |
| 1 | L04 Diseño | 60 min | Arquitectura, Mermaid, ADR | [L04](./SESIONES/L04.md) |
| 1 | L05 Desarrollo | 210 min | API, pruebas y revisión | [L05](./SESIONES/L05.md) |
| 2 | L06 Testing | 75 min | Tests y corrección | [L06](./SESIONES/L06.md) |
| 2 | L07 GitLab CI/CD | 75 min | Pipeline de pruebas remoto | [L07](./SESIONES/L07.md) |
| 2 | L08 Evolución | 60 min | Cambio de cuatro horas | [L08](./SESIONES/L08.md) |
| 2 | L09 Trazabilidad | 30 min | Matriz y documentación | [L09](./SESIONES/L09.md) |
| 2 | L10 ALM automático | 180 min | Segunda ejecución orquestada | [L10](./SESIONES/L10.md) |
| 2 | L11 Evaluación | 60 min | Comparación y defensa individual | [L11](./SESIONES/L11.md) |

**Total: 960 minutos lectivos.** Pausas no incluidas.

## 5. Cómo hablar durante cada laboratorio

No conviertas la clase en lectura de Markdown proyectado. Usa la teoría para desarrollar el concepto (qué es y por qué importa), muestra una demostración pequeña, pide al alumnado ejecutar el metaprompt, revisa públicamente un prompt operativo y después permite el trabajo por equipos con una lista clara de evidencias. El error es un recurso docente: si Claude inventa una ruta, cambia un criterio o asegura falsamente que algo ha pasado, muéstralo y explica por qué se bloquea esa fase.

Repite tres preguntas en todas las fases:
- **¿Qué entrada real utilizó la IA?** (ruta y versión, no «lo sabe del chat»).
- **¿Qué salida exactamente produjo?** (archivo y contenido comprobable).
- **¿Qué evidencia autoriza continuar?** (revisión humana, test, log o pipeline).

## 6. Gestión de costes y contingencias

El curso se ha diseñado para un MVP pequeño y pocos ciclos largos de regeneración. Con Claude Pro el tiempo de uso disponible no está garantizado; si un alumno se queda sin cuota, el formador entrega un checkpoint docente con su procedencia indicada y el alumno prosigue verificando e integrando, pero **no** se afirma que ejecutó las generaciones que sustituyó. Mantén un registro de fallos de cuota independiente de los fallos de código. No se obliga a generar documentos varias veces por estilo.

Si falla **GitLab**, distingue: permisos, red, runner, YAML o tests. El bloqueo de infraestructura no justifica declarar un pipeline «pasado». Los alumnos pueden practicar la validación local, y el formador marca como pendiente la prueba remota.

## 7. Condiciones de calidad de una fase

La fase documental exige requisitos no ambiguos, diseño relacionado, decisiones explícitas y aprobación. La técnica exige prueba local reproducible; la CI requiere pipeline remoto real. El alumno explica qué aprobó, qué rechazó y por qué. No premiar número de prompts, número de clases o cantidad de código.

## 8. Evaluación y relación con senior

Aplicar rúbrica: requisitos 20%, MVP 25%, tests y CI 25%, GitLab 15%, explicación crítica de IA 15%. El senior reutilizará el caso y glosario, aumentando autonomía y complejidad de controles; el junior necesita aprender a dirigir y verificar el flujo que ya existe.

**Material adicional:** [soluciones conceptuales](./SOLUCIONES_CONCEPTUALES.md), [rúbrica](./EVALUACION.md), las **once sesiones** con minutaje y preguntas técnicas.