# Plantilla del proyecto GitLab que usarán los alumnos

**Objetivo:** subir los archivos de esta carpeta como raíz de un proyecto nuevo de GitLab. **No** subir el resto del curso (manuales, teoría o solución del formador) al repositorio de ejecución.

En [CLAUDE.md](./CLAUDE.md) están los límites operativos del agente y en [alm/maestro.md](./alm/maestro.md) el protocolo de fase. Las rutas **alm/contratos/** contienen **qué debe entregar** cada fase; las rutas **alm/metaprompts/** contienen **cómo generar un prompt operativo** que después, con aprobación, ejecutará Claude.

## Preparación por parte del formador

1. Cada alumno crea un proyecto GitLab **personal y privado**, con su propio usuario (ver L02).
2. Importar esta plantilla y comprobar que el repositorio es clonable.
3. Confirmar Python, Git, Claude Code y runner de GitLab para el L07.
4. Crear proyecto de prueba pequeño; no se usan credenciales reales del negocio.
5. El alumno comunica al formador la URL de su proyecto y registra cualquier limitación de CI.

## Pasos del alumno

- Leer el material L01–L11 en [GitHub del curso](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/tree/main/01_ALUMNOS).
- Clonar su proyecto GitLab personal y abrirlo en VS Code.
- Ejecutar por orden las seis fases. Cada fase produce primero **alm/prompts-generados/NN-fase.md**, luego sus artefactos.
- Confirmar gates humanos; no fingir resultados ni cerrar una fase solo porque Claude generó texto.
- L09 termina la documentación manual; L10 estudia el pipeline ALM automatizado y sus evidencias, pero **solo el formador lo ejecuta una vez** en su propio GitLab. Después distribuye la referencia en `referencia/alm-automatico`; L11 evalúa ambas modalidades.

**Nota:** no hay .gitlab-ci.yml inicial. En L07 Claude lo genera para CI de la aplicación en la rama guiada; en L10 lo genera para **orquestación ALM** en una rama limpia desde base-alm. Son configuraciones distintas. Hasta ese momento la ausencia de CI es intencionada.

## Rutas iniciales

| Carpeta | Propósito |
|---|---|
| alm/contratos | Entradas, salidas y criterios de fase |
| alm/metaprompts | Generación controlada de prompts operativos |
| alm/prompts-generados | Salida de Claude, inicialmente vacía |
| alm/evidencias | Registro de comprobaciones y aprobaciones |
| docs/requisitos | Especificaciones producidas en L03 |
| docs/arquitectura | Diseño y ADR producidos en L04 |
| docs/calidad | Matriz y resultados de L06 |
| docs/entrega | Pipeline y evolución documentada en L07-L08 |
| docs/trazabilidad | Matriz final de L09 |
| app/ y tests/ | Implementación y pruebas generadas |
