# Instrucciones persistentes a Claude Code para el taller

## Identidad y objetivo
Trabajas sobre un repositorio didáctico de GitLab de Coworking Manager. El objetivo es **aprender ALM generativo**, no maximizar autonomía ni cantidad de código.

## Alcance
Listar salas, reservar por intervalos, rechazar solapamientos y cancelar; una evolución posterior limitará a cuatro horas. Tecnologías: Python, FastAPI, SQLite, pytest. No integrar pagos, usuarios reales, notificaciones, cloud, Kubernetes o microservicios.

## Metodología obligatoria
1. Lee el contrato de fase y el contexto mínimo.
2. Primero genera **alm/prompts-generados/NN-fase.md** según el metaprompt de fase. Detente.
3. Solicita aprobación humana del prompt antes de ejecutar.
4. Una vez aprobado, implementa los archivos de salida y muestra diff.
5. Ejecuta comandos de validación autorizados y muestra salida real. «Parece correcto» no es evidencia.
6. Documenta resultados en alm/evidencias/registro.md; solicita segundo gate para terminar la fase.

## Reglas de seguridad y control
- No accedas a secretos, contraseñas ni datos personales.
- No borres historial, repositorio, ramas ni carpetas ajenas al alcance.
- No hagas merge ni despliegues sin aprobación expresa.
- No alteres tests correctos para ocultar fallos.
- No modifiques requisitos sin registrar cambio de negocio.
- No generes cifras de cobertura, enlaces GitLab, estados de pipeline o logs que no existan.
- Mantén cambios mínimos y presenta riesgos conocidos.
