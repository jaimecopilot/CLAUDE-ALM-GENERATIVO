# L07 · METAPROMPT: crear un prompt para CI/CD de GitLab

**Objetivo:** pedir a Claude un prompt operativo específico. No crear aún `.gitlab-ci.yml` ni editar código sin autorización.

~~~text
Eres diseñador de prompts operativos para integración continua de una aplicación FastAPI en GitLab.

Lee estas entradas reales:
- CLAUDE.md y alm/maestro.md;
- alm/contratos/05-devops.md;
- código de app/, tests/, requirements.txt y scripts existentes;
- requisitos y criterios de aceptación; y
- comandos de instalación y pruebas verificados localmente.

Genera exclusivamente alm/prompts-generados/05-devops.md.
El prompt operativo que redactes deberá solicitar, tras aprobación humana:
1. Crear un .gitlab-ci.yml válido para GitLab CI (no GitHub Actions).
2. Definir tres etapas: quality, test y package. Usar Python 3.12 para instalar las dependencias. Comprobar sintaxis en quality, ejecutar pytest en test y producir en package un .tar.gz descargable con código e instrucciones.
3. Incorporar lint con ruff cuando sea compatible con la configuración real.
4. Propagar errores de los comandos y fallar el job si falla una prueba obligatoria.
5. No desactivar tests, no usar allow_failure: true ni expresiones que ignoren errores.
6. Evitar secretos en archivos, logs y prompts; L07 no necesita Anthropic API.
7. Evitar trabajos recursivos, despliegues cloud no aprobados y generación inconexa de requisitos.
8. Crear docs/entrega/informe.md y documentar los pasos commit → push → GitLab Build/Pipelines → inspección de job y log.
9. Explicar cómo diagnosticar fallos de runner, dependencias, descubrimiento de pruebas o YAML.
10. Registrar el gate de salida: YAML revisado, job ejecutado realmente, estado y logs comprobados o bloqueo explícito.

El prompt producido debe incluir entradas con rutas verificadas, plan mínimo, archivos a generar, restricciones, comandos de validación, criterios y solicitud de autorización.
No inventes URLs, resultados de pytest, pipelines verdes ni despliegues.
Detente tras guardar el prompt operativo.
~~~

**Revisión del alumno:** antes de autorizar, confirma que el prompt se basa en la aplicación real, que GitLab será el ejecutor, que un test fallido detendrá el job y que no invoca la API de Claude. Solo un pipeline remoto ejecutado permite declarar CI verificado.
