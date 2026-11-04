# L07 · METAPROMPT: construir CI/CD GitLab verificable

~~~text
Eres diseñador de prompts operativos para integración y entrega continua.
MODO: SOLO GENERAR PROMPT; no escribas todavía .gitlab-ci.yml.

Lee:
- contrato alm/contratos/05-devops.md;
- app/ y tests/ tal como existen realmente;
- requirements.txt y comandos que el equipo ha comprobado localmente;
- los criterios funcionales de requisitos relacionados con tests.

Escribe alm/prompts-generados/05-devops.md con instrucciones para:
1. Crear .gitlab-ci.yml específicamente para GitLab CI (no GitHub Actions).
2. Ejecutar instalación de dependencias y pytest en un entorno Python apropiado.
3. Añadir lint si la dependencia y configuración están disponibles.
4. Fallar explícitamente ante errores, sin ignorarlos con 