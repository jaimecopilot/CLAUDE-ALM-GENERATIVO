# Taller de 16 horas · Vibe Coding y ALM generativo con Claude y GitLab

> **Curso de 16 horas.** La ejecución con GitLab requiere configurar el proyecto y sus runners.

## Qué es este repositorio

Este es el **curso del alumno**, no una simple guía de 16 páginas ni un conjunto de prompts aislados. Cada laboratorio incluye **teoría explicada, práctica guiada y metaprompt operativo**, más resultados esperados y criterios verificables. Todo se organiza alrededor de un solo caso: **gestionar las reservas de salas de un coworking**.

**Objetivo:** comprobar cómo una IA generativa produce artefactos enlazados de ALM: requisitos → diseño → código → tests → pipeline CI/CD → mantenimiento, con revisión humana y trazabilidad en GitLab.

La IA del curso será Claude Code; los contratos y metaprompts se redactan para poder adaptarlos a otro agente. Claude **no** necesita escribir el manual: el manual ya forma parte de este repositorio. Claude ejecutará las fases ALM en el taller.

## Cómo encontrar los contenidos

- **[Itinerario de 16 horas](./00_PROGRAMA/ITINERARIO_16H.md)**: tiempos, nivel junior, objetivos y entregables.
- **[Material del alumno](./01_ALUMNOS/README.md)**: índice de los diez laboratorios; **cada laboratorio tiene TEORIA, PRACTICA y METAPROMPT**.
- **[Guía del formador](./02_FORMADOR/GUIA_FORMADOR.md)**: explicaciones, demostraciones, intervenciones y evaluación.
- **[Plantilla para GitLab](./03_GITLAB_PLANTILLA/README.md)**: archivos iniciales que se copiarán al proyecto GitLab cuando esté disponible.

## Qué debe hacer el alumno

1. Leer **TEORIA.md** del laboratorio en curso.
2. Ejecutar **PRACTICA.md** con Claude y GitLab.
3. Usar **METAPROMPT.md** para producir un prompt específico, que Claude después ejecuta.
4. Verificar resultados y evidencias antes de avanzar.
5. Registrar las salidas verificadas en su proyecto GitLab.

Los **metaprompts** están versionados y son reutilizables. Los **prompts operativos** y **artefactos de fase** se crean durante el taller; no se entregan resueltos al alumno.

## Alcance invariable del producto

- Listar salas de reunión.
- Reservar una sala en un intervalo horario.
- Rechazar reservas solapadas.
- Cancelar reservas.
- Evolución final: duración máxima de cuatro horas.

Stack de referencia: Python, FastAPI, SQLite, pytest, GitLab CI/CD. Evitamos autenticación compleja, membresías, facturación, Kubernetes y despliegue productivo. La entrega se verifica mediante ejecución local y pipeline GitLab.

## Alcance de automatización: dos pipelines distintos

- **Pipeline del ALM generativo:** metaprompts → prompts de fase → artefactos → validaciones → siguiente fase. Lo orquesta Claude Code bajo control humano.
- **Pipeline de CI/CD:** tareas automatizadas del proyecto en GitLab, representadas por `.gitlab-ci.yml`.

El pipeline ALM no debe confundirse con CI/CD. Sin integración adicional o credenciales no habrá ejecución desatendida desde GitLab hacia Claude; el agente se ejecuta sobre el clon del repositorio.

## Recursos y costes

Claude Code requiere un plan compatible; Claude Free web no equivale a Claude Code. El curso está dimensionado para una cuenta Pro por alumno, con límites de uso. No se prevén llamadas de API pagadas desde CI. Se prevén puntos de recuperación si un alumno alcanza los límites.

## Fase 2

Quedará pendiente la **integración remota real con GitLab**: crear o vincular el proyecto, configurar acceso, runners, permisos y ejecutar las Merge Requests y pipelines. Hasta entonces la plantilla es material preparado, no infraestructura desplegada.

**No subir las soluciones del formador al repositorio del alumno.**
