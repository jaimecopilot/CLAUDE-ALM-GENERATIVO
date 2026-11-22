# Instrucciones persistentes a Claude Code para el taller

## Identidad y objetivo
Trabajas sobre un repositorio didáctico de GitLab de Coworking Manager. El objetivo es **aprender ALM generativo**, no maximizar autonomía ni cantidad de código.

## Alcance
Listar salas, reservar por intervalos, rechazar solapamientos y cancelar; una evolución posterior limitará a cuatro horas. Tecnologías: Python, FastAPI, SQLite, pytest. No integrar pagos, usuarios reales, notificaciones, cloud, Kubernetes o microservicios.

## Modo de ejecución

Estas aprobaciones fase a fase corresponden al recorrido guiado L03–L09. En L10 los alumnos aprenden a revisar el pipeline global, pero **solo el formador lo lanza en su GitLab** y reparte una copia del resultado. GitLab controla los jobs y la revisión humana final permanece obligatoria. Claude Code en GitLab CI requiere una API autorizada, que **no** se factura dentro de Pro.

## Metodología obligatoria
1. Lee el contrato de fase y el contexto mínimo.
2. Primero genera **alm/prompts-generados/NN-fase.md** según el metaprompt de fase. Detente.
3. Solicita aprobación humana del prompt antes de ejecutar.
4. Una vez aprobado, implementa los archivos de salida y muestra diff.
5. Ejecuta comandos de validación autorizados y muestra salida real. «Parece correcto» no es evidencia.
6. Documenta resultados en alm/evidencias/registro.md; solicita segundo gate para terminar la fase.

## Conexión al proyecto y sincronización

En L03–L09, el agente trabaja sobre el clon Git del alumno: **Git gestiona los commits y ramas**; GitLab web, GitLab MCP o `glab` pueden consultar issues, Merge Requests y pipelines. Estos mecanismos no reemplazan los gates. Si otra herramienta ha generado cambios directamente en GitLab, revisa `git status` y sincroniza con `git fetch` y `git pull --ff-only` antes de continuar. No uses `push --force` ni sobrescribas trabajo ajeno.

## Reglas de seguridad y control
- No accedas a secretos, contraseñas ni datos personales.
- No borres historial, repositorio, ramas ni carpetas ajenas al alcance.
- No hagas merge ni despliegues sin aprobación expresa.
- No alteres tests correctos para ocultar fallos.
- No modifiques requisitos sin registrar cambio de negocio.
- No generes cifras de cobertura, enlaces GitLab, estados de pipeline o logs que no existan.
- Mantén cambios mínimos y presenta riesgos conocidos.
