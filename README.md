# Taller de 16 horas · Vibe Coding y ALM generativo con Claude y GitLab

> **Curso de 16 horas en cuatro jornadas de cuatro horas, adaptable a junior y senior.** Cada alumno crea un GitLab personal; el formador ejecuta una sola vez el ALM automático central del L10.

## Qué es este repositorio

Este es el **curso del alumno**, no una simple guía de 16 páginas ni un conjunto de prompts aislados. Cada laboratorio incluye **teoría explicada, práctica guiada y metaprompt operativo**, más resultados esperados y criterios verificables. Todo se organiza alrededor de un solo caso: **gestionar las reservas de salas de un coworking**.

**Objetivo:** comprobar cómo una IA generativa produce artefactos enlazados de ALM: requisitos → diseño → código → tests → pipeline CI/CD → mantenimiento, con revisión humana y trazabilidad en GitLab.

La IA del curso será Claude Code; los contratos y metaprompts se redactan para poder adaptarlos a otro agente. Claude **no** necesita escribir el manual: el manual ya forma parte de este repositorio. Claude ejecutará las fases ALM en el taller.

## Cómo encontrar los contenidos

Para preparar tu equipo, abre la guía inicial. Durante las cuatro jornadas puedes seguir el [manual del alumno (PDF)](./01_ALUMNOS/Manual_Alumno_ALM_Generativo_16h_2026.pdf) o el [índice de los once laboratorios](./01_ALUMNOS/README.md).

- **[Guía inicial Claude + GitLab + VS Code (PDF)](./01_ALUMNOS/GUIA_ALUMNADO_CLAUDE_GITLAB_VSCODE_ALM_2026.pdf)**: lectura inicial para instalar Git, VS Code, Python, Claude Code y entender las conexiones con GitLab antes de L02.
- **[Ciclo continuo ALM + CI/CD](./00_PROGRAMA/DIAGRAMAS/CICLO_CONTINUO_ALM_CICD.md)**: diagrama de necesidades, requisitos, diseño, código, revisión, entrega y mantenimiento.
- **[Itinerario de 16 horas](./00_PROGRAMA/ITINERARIO_16H.md)**: tiempos, nivel junior, objetivos y entregables.
- **[Cómo se conectan Claude Code, Git, GitLab MCP y glab](./01_ALUMNOS/GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md)**: mecanismos, permisos, sincronización, tests, MRs y CI.
- **[Guía de alta individual en GitLab](./01_ALUMNOS/L02/GUIA_GITLAB_PASO_A_PASO.md)**: cuenta personal, proyecto privado y permisos.
- **[Nuevo laboratorio de ALM automático](./01_ALUMNOS/L10/PRACTICA.md)**: segunda ejecución del mismo caso.
- **[Material del alumno](./01_ALUMNOS/README.md)**: índice de los once laboratorios; **cada laboratorio tiene TEORIA, PRACTICA y METAPROMPT**.
- **[Plantilla para GitLab](./03_GITLAB_PLANTILLA/README.md)**: en L02 copia **solo el contenido** de esta carpeta a la raíz de tu proyecto personal, incluidos los archivos ocultos. Sigue la guía de L02 para hacerlo en Windows o Bash.

## Qué debe hacer el alumno

1. Crear o utilizar una cuenta GitLab personal y un proyecto privado propio, siguiendo L02.
2. Leer **TEORIA.md** del laboratorio en curso.
3. Ejecutar **PRACTICA.md** con Claude y GitLab.
4. Usar **METAPROMPT.md** para producir un prompt específico, que Claude después ejecuta.
5. Verificar resultados y evidencias antes de avanzar.
6. Registrar las salidas verificadas en su proyecto GitLab.

Los **metaprompts** están versionados y son reutilizables. Los **prompts operativos** y **artefactos de fase** se crean durante el taller; no se entregan resueltos al alumno.

## Alcance invariable del producto

- Listar salas de reunión.
- Reservar una sala en un intervalo horario.
- Rechazar reservas solapadas.
- Cancelar reservas.
- Evolución final: duración máxima de cuatro horas.

Stack de referencia: Python, FastAPI, SQLite, pytest, GitLab CI/CD. Evitamos autenticación compleja, membresías, facturación, Kubernetes y despliegue productivo. La entrega se verifica mediante ejecución local y pipeline GitLab.

## Dos formas de ejecutar el ALM y un pipeline de CI/CD

- **Modo guiado (L01–L09):** Claude Code en VS Code/terminal con Git para sincronizar el proyecto es el recorrido principal de desarrollo y pruebas. Claude web + MCP es una alternativa remota para documentación, requisitos y diseño; ambos respetan contratos y gates.
- **Modo automático (L10):** GitLab encadena seis contratos y metaprompts mediante Claude API. El alumno estudia su diseño, pero **solo el formador ejecuta una vez** el pipeline en su GitLab y distribuye los resultados versionados mediante la rama `referencia/alm-automatico`.
- **GitLab CI/CD (L07):** pipeline diferente definido por `.gitlab-ci.yml`, que valida tests y artefactos tras los pushes. No debe confundirse con el pipeline ALM.

En L10 se estudia y puede generarse el YAML, pero la ejecución real se realiza **solo en el GitLab del formador**, con API y presupuesto propios. Los alumnos no requieren clave API para este taller. Si no hay ejecución validada, se registra como NO EJECUTADO.

## Recursos y costes

Claude Code requiere un plan compatible; Claude Free web no equivale a Claude Code. El curso está dimensionado para una cuenta Pro por alumno, con límites de uso. Las llamadas de API del L10 son un coste separado que debe autorizarse antes de ejecutar. Se prevén puntos de recuperación si un alumno alcanza los límites.

## Qué hacer con `.github/workflows` y `scripts`

GitHub Actions usa `.github/workflows/` para comprobar los enlaces y la continuidad de los laboratorios, probar la preparación de L02 en Windows y Bash y verificar los dos PDF del alumnado. Estas tareas son de mantenimiento del curso. Para el proyecto GitLab personal utiliza la plantilla indicada en L02. En L07 crearás allí tu propio archivo `.gitlab-ci.yml` para comprobar la aplicación.

Si trabajas en Windows, la práctica de L02 utiliza [Preparar-L02.ps1](./scripts/Preparar-L02.ps1). Ejecútalo desde la copia local del curso siguiendo esa guía.
