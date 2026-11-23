# Conexión operativa: Claude, Claude Code, GitLab y VS Code

**Material transversal para L02–L11.** Se aplica al mismo caso Coworking Norte, los mismos contratos y los mismos artefactos. Los alumnos tienen Claude Pro y GitLab.com Free. **No se necesita una máquina virtual** para ejecutar Claude Code en el ordenador personal.

## 1. Arquitectura del recorrido práctico y alternativas

~~~mermaid
flowchart TD
    GL["GitLab personal y privado: repositorio, issues y CI/CD"]
    LOCAL["VS Code + Claude Code: carpeta clonada y terminal"]
    WEB["Claude web + Proyecto + MCP GitLab"]
    CI["GitLab Runner: CI del producto"]
    AUTO["GitLab del profesor: ALM automático central"]
    LOCAL <-->|"Git clone / pull / push"| GL
    WEB <-->|"Herramientas MCP y OAuth"| GL
    GL --> CI
    AUTO -->|"Resultado versionado, rama de referencia"| GL
~~~

**Recorrido práctico de desarrollo (L02–L09):** Claude Code en VS Code, con **Git** como mecanismo de sincronización hacia GitLab. Requisitos y diseño pueden realizarse opcionalmente con Claude web + MCP. El Web IDE es una alternativa para editar en navegador y examinar commits, pero no proporciona una terminal de proyecto.

**Alternativa remota completa:** Claude web + MCP modifica los archivos directamente en GitLab y espera al CI para comprobar el software. Esto no equivale a ejecutar Claude Code localmente. Un workspace remoto con terminal es una opción, **no un requisito**.

**Automático (L10):** GitLab Runner invoca Claude Code/Agent SDK de forma no interactiva **con API facturada por separado**. Solo el formador lanza el pipeline central y distribuye una rama de referencia a cada alumno, nunca su clave API.

## 2. Tres conexiones distintas de Claude Code con GitLab

| Vía | Función | Autenticación |
|---|---|---|
| **Git (obligatoria con clon)** | `git clone`, `fetch`, `pull`, `commit`, `push`, ramas y tags | Credenciales Git de cada alumno (Git Credential Manager o SSH) |
| **MCP GitLab (opcional)** | Consultar issues, abrir MR, revisar pipelines, trabajar con recursos remotos | OAuth individual en Claude Code mediante `/mcp` |
| **`glab` (opcional)** | Realizar desde terminal las operaciones de GitLab: issues, MR, CI, logs | `glab auth login`, con cuenta individual |

**Distinción:** cuando Claude Code edita el clon, los cambios se publican normalmente mediante `git push`. Claude web con MCP puede escribir directamente en GitLab sin un clon. MCP y `glab` **no reemplazan automáticamente** Git, y tampoco proporcionan una terminal remota.

## 3. Preparar GitLab y Claude Code

1. Abre [L02: alta paso a paso](./L02/GUIA_GITLAB_PASO_A_PASO.md). Crea un proyecto **privado** en tu espacio personal de GitLab; inicialmente, sin README.
2. Clona el curso y copia **solo** `03_GITLAB_PLANTILLA` al proyecto GitLab. Publica el primer commit.
3. Crea el tag `base-alm` y publica la rama `practica/manual`.
4. Inicia sesión en Claude Code con tu cuenta Claude Pro; **no configures ANTHROPIC_API_KEY para L02–L09**.
5. Abre el clon del proyecto en VS Code; Claude Code lee `CLAUDE.md` como instrucciones del proyecto. Comprueba con `claude auth status`.
6. Si quieres usar GitLab MCP desde Claude Code, sigue el apartado 4. Si no puedes autorizar MCP, **puedes seguir los laboratorios mediante Git, GitLab web y Claude Code**.

Comandos habituales en una terminal **dentro del clon GitLab**:

~~~powershell
git status
git fetch origin
git switch practica/manual
git pull --ff-only origin practica/manual
claude
~~~

No ejecutes `git pull` si tienes cambios locales sin guardar o sin revisar. Revisa `git status` antes de sincronizar; ante conflictos, **no uses `reset --hard` ni `push --force`**.

## 4. GitLab MCP desde Claude Code (opcional)

En la terminal:

~~~powershell
claude mcp add -s user --transport http GitLab https://gitlab.com/api/v4/mcp
claude mcp list
claude
~~~

Dentro de Claude Code, usa `/mcp`, selecciona GitLab y autoriza por OAuth. Cada alumno se identifica con su propia cuenta; **no se comparten contraseñas ni tokens**. GitLab.com requiere que el usuario disponga de acceso MCP habilitado en un **grupo de nivel superior** al que pertenezca. Si falta ese requisito, registra el bloqueo; **no traslades proyectos o cambies permisos por tu cuenta**.

**Ámbitos de Claude Code:** `local` (solo proyecto y usuario), `user` (para ese usuario en varios proyectos) y `project` (crea `.mcp.json` compartible). Por ejemplo:

~~~powershell
claude mcp add -s project --transport http GitLab https://gitlab.com/api/v4/mcp
~~~

La configuración compartida sería:

~~~json
{
  "mcpServers": {
    "GitLab": {
      "type": "http",
      "url": "https://gitlab.com/api/v4/mcp"
    }
  }
}
~~~

**Esta configuración es optativa, no viene activada en la plantilla.** Claude Code normalmente solicita aprobación de un servidor definido en `.mcp.json` al abrir una sesión interactiva, pero una ejecución **no interactiva** puede cargarlo sin ese diálogo. El formador debe revisar la configuración y el código del runner antes de incluirla. `.mcp.json` no debe almacenar credenciales.

Referencias: [GitLab MCP](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) y [Ámbitos MCP de Claude Code](https://code.claude.com/docs/en/mcp).

## 5. Alternativa de terminal: GitLab CLI (`glab`)

`glab` es la CLI oficial de GitLab; **no es obligatoria**. Puede realizar operaciones similares a MCP sin salir de la terminal.

~~~powershell
glab auth login
glab auth status
glab issue list
glab mr list
glab ci status
glab ci view
glab ci trace
~~~

`glab` detecta el proyecto a partir de los remotos Git cuando se ejecuta dentro del clon. Si falla, comprueba `git remote -v` y la autorización de `glab`. Para instalarla, consulta [GitLab CLI](https://docs.gitlab.com/cli/), que ofrece instrucciones por sistema operativo.

En la interfaz web siempre puedes consultar issues, MRs y pipelines **sin instalar MCP ni glab**.

## 6. Flujo completo: issue → Claude Code → MR → CI

1. **Entrada real.** Abre una issue de GitLab. Consulta su texto por navegador, MCP o `glab issue view N`. Relaciónala con un RF y su criterio de aceptación.
2. **Sincronización.** Confirma `git status`, `git switch practica/manual` y `git pull --ff-only origin practica/manual`; si utilizas una rama `feature`, créala desde `practica/manual`, abre la MR hacia esa rama y, tras aprobación, integra el cambio antes de avanzar de laboratorio. El resultado guiado final de L03–L09 debe quedar en `practica/manual`.
3. **Gate A.** Lee el contrato y el metaprompt de la fase; Claude genera primero `alm/prompts-generados/NN-fase.md`. **El alumno revisa y aprueba este archivo**. El modo Plan es una ayuda, no sustituye este gate.
4. **Implementación y pruebas.** Tras la aprobación, Claude Code edita archivos y ejecuta `pytest` (o `mvn test` / `dotnet test` en una adaptación del taller). Conserva salida real, no afirmaciones.
5. **Gate B.** Revisa `git diff`, los criterios y los tests. **Hasta esta aprobación, no autorices commit, push ni MR**.
6. **Publicar.** `git add`, `git commit` y `git push` en la rama autorizada. Abre MR mediante GitLab web, MCP o `glab mr create`; **no hagas merge automáticamente**.
7. **Validación remota.** Consulta Build → Pipelines o `glab ci status`/`glab ci view`. Si falla, inspecciona el job y `glab ci trace`; diagnostica la causa, repara lo mínimo y repite las pruebas. No declares «CI verde» sin pipeline real.
8. **Evidencias.** Registra enlaces verdaderos al commit, MR, pipeline y al archivo de requisitos/test que corresponde.

### Prompt de ejemplo para Claude Code

~~~text
Trabajas en la rama practica/manual del proyecto Coworking Norte.
Lee CLAUDE.md, alm/maestro.md, el contrato y el metaprompt de la fase.
Comprueba que existen los requisitos y el diseño previamente aprobados.
Primero genera alm/prompts-generados/03-desarrollo.md y DETENTE.
Esperaré a revisar ese archivo y aprobarlo (gate A).
Solo después: implementa los cambios autorizados y ejecuta pruebas.
Muestra la salida real y el git diff. DETENTE para el gate B.
No hagas commit, push, MR ni merge sin mi aprobación.
~~~

## 7. Alternar Claude web + MCP y Claude Code sin pisar cambios

Los dos mecanismos **no comparten automáticamente el estado de sus conversaciones**. Comparten los **archivos publicados** en GitLab.

- **De Claude web a Claude Code:** confirma que Claude web ha escrito y confirmado el commit en GitLab. En el clon, revisa `git status` y sincroniza con `git fetch` y `git pull --ff-only`, con la rama correcta.
- **De Claude Code a Claude web:** termina el gate B, haz commit y push. En Claude web, vuelve a solicitar la lectura de los archivos y del commit recientes por MCP; no des por vigente una lectura anterior.
- Si ambos agentes proponen editar el mismo archivo simultáneamente, detén uno de los trabajos. No uses `git push --force` para tapar el conflicto.
- Evita copiar al chat claves privadas, tokens, datos reales de clientes o archivos de otras personas.

## 8. Diferencia entre CI del producto y ALM automático

**L07 (CI del producto):** un `.gitlab-ci.yml` ejecuta instalación, lint, `pytest` y comprobación de artefactos. **No llama a Claude API**. Los alumnos lo generan, comprueban y revisan en su propio GitLab.

**L10 (ALM generativo central):** otro pipeline, preparado y revisado por el formador, encadena `alm_requisitos → alm_diseno → alm_desarrollo → alm_testing → alm_devops → alm_evolucion`. Los trabajos consumen archivos anteriores mediante artifacts, invocan Claude Code en modo no interactivo y necesitan una clave `ANTHROPIC_API_KEY` y presupuesto **solo en GitLab del formador**. Al acabar, el formador versiona los resultados y publica la rama `referencia/alm-automatico` en cada repositorio privado al que tenga acceso Developer. **Los alumnos no ejecutan doce pipelines AI**, ni reciben la clave API del profesor.

El YAML de L10 y los resultados del runner **deben validarse realmente** antes de considerarlos completos: un metaprompt o una demostración conceptual no demuestra ejecución.

## 9. Problemas frecuentes

| Síntoma | Comprobación |
|---|---|
| Claude Code no ve GitLab | Sin MCP, usa la web y Git. Si hay MCP, revisa `claude mcp list`, `/mcp`, OAuth y acceso del grupo |
| `git push` falla | Revisa `git remote -v`, credenciales Git y que la rama no esté protegida |
| `glab` no reconoce el proyecto | Abre la terminal dentro del clon, revisa `glab auth status` y `git remote -v` |
| GitLab pipeline no arranca | Verifica `.gitlab-ci.yml`, runners, reglas, permisos y cuota de CI |
| Claude modifica algo que no estaba aprobado | Detén la fase, revisa `git diff` y recupera la versión correcta sin destruir cambios ajenos |
| Claude afirma que ha probado algo pero no hay log | Estado **NO VERIFICADO** hasta que exista salida de terminal o CI |
| El profesor no puede subir la rama de referencia | Comprueba invitación Developer y rama no protegida; no hagas público el proyecto |

## 10. Comprobación de la conexión

- [ ] Proyecto GitLab privado y plantilla importada
- [ ] Tag `base-alm` y rama `practica/manual` creados
- [ ] Git sincroniza el clon con GitLab
- [ ] Claude Code inicia sesión con Pro y lee `CLAUDE.md`
- [ ] Sé distinguir Git, MCP y `glab`
- [ ] El primer metaprompt genera el prompt operativo y se detiene para Gate A
- [ ] Gate B revisa archivos, diff y pruebas antes del push
- [ ] La CI normal se comprueba con logs reales
- [ ] Sé qué parte del L10 es una ejecución central del formador y qué parte es aprendizaje del alumno
- [ ] Si uso Claude web + MCP, sé sincronizar su trabajo con Claude Code

Documentación técnica: [Claude Code + MCP](https://code.claude.com/docs/en/mcp), [permisos de Claude Code](https://code.claude.com/docs/en/permissions), [GitLab CLI](https://docs.gitlab.com/cli/), [GitLab MCP](https://docs.gitlab.com/user/model_context_protocol/mcp_server/).

## Verificación de L02 y entrada en L03

En Windows, prepara primero el clon con el [script L02](../scripts/Preparar-L02.ps1). Tras revisar el árbol, ejecuta la opción `-Publicar`. Git publica juntas las tres referencias y vuelve a leerlas del servidor. En un segundo clon, la rama local de prácticas debe conservar el SHA remoto del trabajo previo. En Bash, emplea el [bloque de la guía L02](./L02/GUIA_GITLAB_PASO_A_PASO.md), que se detiene ante un destino existente.

Desde `practica/manual`, usa el [texto de L03](./L03/METAPROMPT.md). Claude debe leer las cinco entradas y escribir solo el prompt. Revisa su contenido para el Gate A. La publicación de los requisitos necesita un segundo control humano, el Gate B. La auditoría de comandos y su alcance se encuentran en la [matriz L01–L11](../00_PROGRAMA/AUDITORIA_OPERATIVA_L01_L11_2026-11-23.md).
