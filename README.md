# Taller de 16 horas · Vibe Coding y ALM generativo con Claude y GitLab

> **Curso de 16 horas.** Cada alumno crea su proyecto GitLab. El uso de runners y la automatización local se documentan en L02, L07 y L10.

## Qué es este repositorio

Este es el **curso del alumno**, no una simple guía de 16 páginas ni un conjunto de prompts aislados. Cada laboratorio incluye **teoría explicada, práctica guiada y metaprompt operativo**, más resultados esperados y criterios verificables. Todo se organiza alrededor de un solo caso: **gestionar las reservas de salas de un coworking**.

**Objetivo:** comprobar cómo una IA generativa produce artefactos enlazados de ALM: requisitos → diseño → código → tests → pipeline CI/CD → mantenimiento, con revisión humana y trazabilidad en GitLab.

La IA del curso será Claude Code; los contratos y metaprompts se redactan para poder adaptarlos a otro agente. Claude **no** necesita escribir el manual: el manual ya forma parte de este repositorio. Claude ejecutará las fases ALM en el taller.

## Cómo encontrar los contenidos

- **[Ciclo continuo ALM + CI/CD](./00_PROGRAMA/DIAGRAMAS/CICLO_CONTINUO_ALM_CICD.md)**: diagrama de necesidades, requisitos, diseño, código, revisión, entrega y mantenimiento.
- **[Itinerario de 16 horas](./00_PROGRAMA/ITINERARIO_16H.md)**: tiempos, nivel junior, objetivos y entregables.
- **[Guía de alta individual en GitLab](./01_ALUMNOS/L02/GUIA_GITLAB_PASO_A_PASO.md)**: cuenta personal, proyecto privado y permisos.
- **[Nuevo laboratorio de ALM automático](./01_ALUMNOS/L10/PRACTICA.md)**: segunda ejecución del mismo caso.
- **[Material del alumno](./01_ALUMNOS/README.md)**: índice de los once laboratorios; **cada laboratorio tiene TEORIA, PRACTICA y METAPROMPT**.
- **[Guía del formador](./02_FORMADOR/GUIA_FORMADOR.md)**: explicaciones, demostraciones, intervenciones y evaluación.
- **[Plantilla para GitLab](./03_GITLAB_PLANTILLA/README.md)**: archivos iniciales que se copiarán al proyecto GitLab cuando esté disponible.

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

- **Modo guiado (L01–L09):** el alumno solicita a Claude cada fase, revisa el prompt operativo y valida la salida.
- **Modo automático (L10):** un pipeline de **GitLab CI/CD** encadena los mismos seis contratos y metaprompts, genera prompts operativos y artefactos, ejecuta validaciones y se detiene si falla un gate. Se prepara en una rama limpia del mismo proyecto y GitLab lo ejecuta en runners.
- **GitLab CI/CD (L07):** pipeline diferente definido por `.gitlab-ci.yml`, que valida tests y artefactos tras los pushes. No debe confundirse con el pipeline ALM.

En L10 el alumno genera el YAML con Claude Code y **GitLab ejecuta los metaprompts en sus runners**. La ejecución remota consume API de Anthropic (se factura aparte de Pro) y minutos del runner: debe habilitarse con presupuesto y permisos explícitos. Sin ellos se enseña el diseño pero no se afirma una ejecución completa.

## Recursos y costes

Claude Code requiere un plan compatible; Claude Free web no equivale a Claude Code. El curso está dimensionado para una cuenta Pro por alumno, con límites de uso. Las llamadas de API del L10 son un coste separado que debe autorizarse antes de ejecutar. Se prevén puntos de recuperación si un alumno alcanza los límites.

## Fase 2

Quedará pendiente la **ejecución real en las cuentas GitLab de los alumnos**: ellos crearán sus proyectos y comprobarán sus runners, permisos, Merge Requests y pipelines. Hasta entonces la plantilla es material preparado, no infraestructura desplegada.

**No subir las soluciones del formador al repositorio del alumno.**
