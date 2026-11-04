# L07 · TEORÍA: un pipeline CI/CD generado por IA no es todo el ALM

**Duración:**

## 1. Dos pipelines que deben distinguirse

El **pipeline ALM generativo** es el flujo lógico que produce especificaciones, arquitectura, código, pruebas, entrega y cambios, gobernado por contratos y metaprompts. El **pipeline de CI/CD** es una automatización más concreta, ejecutada por GitLab a partir de **.gitlab-ci.yml**. CI/CD no inventa requisitos de negocio ni decide que un ADR es correcto: ejecuta jobs definidos, devuelve estados y almacena logs y artefactos.

En L07 queremos que el alumno use un metaprompt para que Claude redacte un prompt operativo y, una vez aprobado, genere un **pipeline real de GitLab** capaz de verificar su proyecto: instalar dependencias, lint con ruff si está disponible, ejecutar pytest y empaquetar un artefacto utilizable. No añadimos producción cloud ni Kubernetes en el nivel junior.

## 2. Qué ejecuta GitLab y qué ejecuta Claude

**Claude Code:** puede escribir y modificar YAML, explicar un fallo y proponer una reparación. **GitLab Runner:** ejecuta los jobs en un entorno de CI. Claude no puede declarar «pipeline verde» si nadie ha comprobado el resultado remoto. La evidencia correcta es el enlace de pipeline, su estado, los logs y, cuando se genera, el artefacto.

Una **Merge Request (MR)** propone integrar una rama con cambios a otra. En ella se revisan diff, relación con issues, aprobación humana y estado de CI. No equivale a un commit; una rama puede tener varios commits y una MR puede requerir correcciones.

## 3. Anatomía de un job

En un pipeline GitLab reconocemos una imagen/entorno de ejecución, etapas (stages), jobs, comandos (script), condiciones de disparo, cache y artefactos. Un error clásico es crear un YAML sintácticamente válido que asume un entorno inexistente, una ruta equivocada o dependencias no instaladas. Por eso se debe probar el pipeline en GitLab, no solo revisarlo conversando con la IA.

**Lint** identifica inconsistencias de estilo y algunas clases de errores. **Tests** comprueban comportamiento. **Build/packaging** prepara artefactos para entrega. En el taller el «deploy» se limita a ejecución local y a un artefacto reproducible; no se publicará un servidor cloud sin autorización.

## 4. Cómo diagnosticar un fallo

Recoge el job que falló y la porción pertinente del log. Distingue:
- **Fallos de configuración:** etapas, nombres o rutas mal declarados.
- **Fallos de dependencias:** faltan paquetes o versiones.
- **Fallos reales de calidad:** un test demuestra que el código no cumple el requisito.
- **Fallos externos temporales:** runner no disponible, descarga interrumpida.

Claude puede ayudar a clasificar y reparar, pero el alumno comprobará el cambio y volverá a ejecutar. No se permite «self-healing» con merges automáticos: en este taller la reparación siempre desemboca en revisión humana.

## 5. Un GitLab vacío no equivale a infraestructura disponible

Sin proyecto GitLab, permisos, runners y cuotas efectivas no hay pipeline remoto probado. La plantilla docente incluye **.gitlab-ci.yml** únicamente si se decide suministrar un esqueleto; en esta versión preferimos que el archivo final se genere en clase. Los recursos de GitLab pueden variar por instancia, por lo que el formador revisará la configuración concreta antes de la jornada.


---


## 6. IA EN CI/CD: DEL PIPELINE MANUAL AL PIPELINE GENERADO

La configuración de pipelines de CI/CD ha sido tradicionalmente uno de los puntos más dolorosos del desarrollo de software. Requiere conocimientos especializados de sintaxis YAML, comprensión de las herramientas de integración y despliegue, y una depuración tediosa cuando algo falla. La IA generativa transforma este proceso permitiendo describir lo que necesitas en lenguaje natural y obtener una configuración completa y funcional.

### 6.1 Ecosistema de plataformas

El ecosistema de CI/CD incluye múltiples plataformas: GitHub Actions, GitLab CI, Jenkins, Azure Pipelines, CircleCI. Cada una tiene su propia sintaxis y particularidades. La IA conoce todas ellas y puede generar la configuración adecuada para la plataforma que uses. Solo tienes que especificar: *"Genera un pipeline de GitHub Actions que ejecute lint con ruff, tests con pytest y construya una imagen Docker"*.

### 6.2 Flujo de generación de pipelines

El flujo de generación de pipelines es simple: describes los stages que necesitas, el trigger (push, PR, schedule), el entorno (sistema operativo, versiones de lenguaje) y las herramientas específicas. La IA genera el archivo YAML completo. Puedes refinarlo iterativamente:

- *"Añade un stage de seguridad con CodeQL"*
- *"Configura caché para las dependencias de Python"*
- *"Añade notificaciones a Slack si el pipeline falla"*

### 6.3 Buenas prácticas aplicadas automáticamente

Las buenas prácticas que la IA aplica automáticamente incluyen:

- Usar versiones específicas de las actions (no `@latest`)
- Configurar caché para dependencias
- Separar stages para paralelizar
- Establecer timeouts
- Usar secrets para información sensible

Si la IA no las aplica, puedes pedírselo explícitamente.

### 6.4 Personalización para el stack tecnológico

La personalización para el stack tecnológico es una ventaja clave. La IA detecta el lenguaje y el framework de tu proyecto y adapta el pipeline en consecuencia:

- **Python**: usará `pip`, `pytest` y `ruff`
- **Node.js**: usará `npm`, `jest` y `eslint`

La IA conoce las herramientas estándar de cada ecosistema.

### 6.5 Múltiples entornos

La generación de pipelines para múltiples entornos (desarrollo, staging, producción) es otra capacidad valiosa. Puedes pedir:

> *"Genera un pipeline con tres entornos: dev (automático en cada push), staging (manual con aprobación) y producción (manual con aprobación de dos revisores)"*

La IA generará la configuración con las condiciones y protecciones adecuadas.

### 6.6 Validación de pipelines generados

La validación de pipelines generados es un paso importante. Pide a la IA que revise el pipeline generado en busca de errores de sintaxis, dependencias faltantes entre stages, o configuraciones inseguras. La IA puede actuar como revisor de su propio output.


---


## 7. INFRAESTRUCTURA COMO CÓDIGO CON IA: DOCKER, KUBERNETES Y MÁS

La creación de infraestructura de despliegue —Dockerfiles, manifiestos Kubernetes, configuraciones de red, scripts de aprovisionamiento— requiere conocimientos especializados de cada herramienta. La IA generativa democratiza este conocimiento permitiendo generar configuraciones profesionales desde descripciones en lenguaje natural. No necesitas conocer la sintaxis exacta de cada herramienta: describes lo que necesitas y la IA genera la configuración.

### 7.1 Generación de Dockerfiles

La generación de Dockerfiles es uno de los flujos más inmediatos. Describe tu aplicación:

> *"Aplicación Python con FastAPI, puerto 8000, necesita PostgreSQL y Redis"*

La IA genera un Dockerfile multietapa optimizado:
- Stage de builder para instalar dependencias
- Stage de runtime para ejecutar la aplicación
- Usuario no-root
- Healthcheck
- Variables de entorno

Puedes refinarlo: *"Añade un volumen para los datos"*, *"Usa una imagen base slim"*, *"Optimiza las capas para mejor caché"*.

### 7.2 Docker Compose para desarrollo

La generación de `docker-compose` para entornos de desarrollo es otra aplicación práctica. Describes los servicios que necesitas (API, base de datos, caché, worker) y la IA genera el archivo `docker-compose.yml` con redes, volúmenes, variables de entorno y dependencias entre servicios. Esto permite levantar un entorno de desarrollo completo con un solo comando.

### 7.3 Manifiestos Kubernetes

La generación de manifiestos Kubernetes cubre deployments, services, configmaps, secrets, ingress y más. Puedes pedir:

> *"Genera un deployment Kubernetes para una API FastAPI con 3 réplicas, health checks, resource limits y auto-scaling"*

La IA generará el YAML con las mejores prácticas:
- Probes de liveness y readiness diferenciados
- `securityContext` para ejecutar como non-root
- Resource requests y limits
- Pod anti-affinity

### 7.4 Infraestructura como código (Terraform / Bicep)

La generación de infraestructura como código (IaC) con Terraform o Bicep permite aprovisionar recursos cloud desde prompts. Describe la infraestructura:

> *"Una aplicación web en Azure con App Service, PostgreSQL Flexible Server y Redis Cache"*

La IA genera los archivos Terraform o Bicep con los recursos, las conexiones entre ellos y las mejores prácticas de seguridad (red privada, firewall, identidades administradas).

### 7.5 Buenas prácticas de seguridad

Las buenas prácticas de seguridad que la IA debe aplicar incluyen:

- Nunca hardcodear secretos (usar variables de entorno o servicios de secrets)
- Ejecutar contenedores como non-root
- Usar imágenes base oficiales y actualizadas
- Minimizar el tamaño de las imágenes (multi-stage builds, alpine/slim)
- Configurar health checks

Si la IA no las aplica, debes pedírselo explícitamente y revisar el resultado.

### 7.6 Validación de configuraciones generadas

La validación de configuraciones generadas es esencial. Las alucinaciones en infraestructura pueden ser peligrosas: una imagen Docker que no existe, una versión de API de Kubernetes incorrecta, un recurso de cloud deprecado. **Siempre verifica contra la documentación oficial antes de aplicar.**


---


## 8. DIAGNÓSTICO DE FALLOS Y AUTO-REPARACIÓN DE PIPELINES

Los fallos en los pipelines de CI/CD son uno de los mayores drenajes de productividad. Un test que pasa en local pero falla en CI, una dependencia que se actualiza y rompe la compilación, un error de configuración que solo se manifiesta en el entorno de integración. La IA generativa puede diagnosticar estos fallos analizando los logs y sugiriendo correcciones, y en el contexto del ALM generativo, puede incluso aplicar las correcciones automáticamente.

### 8.1 Diagnóstico de fallos con IA

El diagnóstico de fallos con IA sigue un proceso simple: copias el log de error del pipeline fallido, lo pegas en la IA junto con el código relevante, y pides un diagnóstico. La IA analiza el error, identifica la causa raíz y sugiere una corrección concreta.

**Ejemplo:** *"El pipeline falla porque pytest-cov no está instalado. Añade `pip install pytest-cov` al stage de test"*

La IA puede diagnosticar errores de dependencias, fallos de compilación, timeouts, problemas de permisos y configuraciones incorrectas.

### 8.2 Análisis de logs complejos

El análisis de logs complejos es donde la IA realmente brilla. Los logs de CI pueden ser extensos y ruidosos. La IA puede filtrar el ruido, identificar el error relevante entre cientos de líneas y explicar por qué ocurrió. Puedes preguntar:

- *"¿Por qué falló este pipeline?"*
- *"¿Es un error transitorio o permanente?"*
- *"¿Cómo puedo prevenirlo en el futuro?"*

### 8.3 Self-Healing CI

El concepto de **Self-Healing CI** es la culminación del ALM generativo en DevOps. Cuando un pipeline falla, un agente de IA analiza automáticamente los logs, diagnostica la causa, genera una corrección, la aplica en una nueva rama y abre una Pull Request. El desarrollador solo tiene que revisar y aprobar. Este flujo reduce el tiempo de resolución de fallos de horas a minutos.

### 8.4 Protecciones del Self-Healing CI

Las protecciones del Self-Healing CI son esenciales para evitar bucles infinitos. El sistema debe:

- Verificar que no existe ya una issue abierta para el mismo fallo (**deduplicación**)
- Limitar el número de reintentos automáticos (máximo 3, luego requiere intervención humana)
- Nunca intentar reparar el propio workflow de self-healing (**prevención de bucles**)

Estas protecciones aseguran que el sistema sea un apoyo fiable, no una fuente de ruido.

### 8.5 Clasificación de fallos

La clasificación de fallos es una capacidad avanzada. La IA puede distinguir entre:

| Tipo de fallo | Ejemplos | Acción recomendada |
|---------------|----------|--------------------|
| **Transitorios** | Timeout de red, servicio externo temporalmente no disponible | Reintentar |
| **Permanentes** | Error de compilación, dependencia rota | Generar corrección |

Esta capacidad de discernimiento reduce el ruido y evita correcciones innecesarias.

### 8.6 Supervisión humana

La supervisión humana sigue siendo necesaria. La IA puede diagnosticar y corregir muchos fallos, pero no todos. Fallos que requieren conocimiento del dominio de negocio, cambios arquitectónicos o decisiones de diseño deben ser revisados por un humano. El **Self-Healing CI es una red de seguridad, no un piloto automático completo.**
