# L05 · PRÁCTICA: generar Coworking Manager con Claude Code

**Herramienta principal:** Claude Code en VS Code sobre el clon GitLab. **Git** sincroniza el código; MCP o `glab` (opcionales) sirven para issues, MR y pipelines. No hace falta VM. Ver [guía y flujo completo issue → pruebas → MR → CI](../GUIA_INTEGRACION_CLAUDE_CODE_GITLAB.md).

**Tiempo: 210 min.** Preparación y explicación 25; prompt/plan 25; incremento de salas 35; reservas y conflictos 65; cancelación 25; validación, registro y revisión 35.

## Entradas aprobadas y alcance
- **docs/requisitos/especificacion.md** con RF-01..RF-04 y CA etiquetados.
- **docs/arquitectura/diseno.md** y ADR de L04.
- **alm/contratos/03-desarrollo.md**.
- Directorio de código inicialmente vacío o mínimo, sin solución de referencia.

**Prohibido**: pedirle a Claude que implemente login, cobros, notificaciones, Kubernetes o conectores externos; tampoco copiar la solución del profesor.

## Paso 1 — localizar el trabajo de GitLab
Selecciona issues ordenadas del backlog y trabaja **por defecto en `practica/manual`**, creada en L02. Esta misma rama reunirá los artefactos de L03 a L09 para poder compararlos con el resultado automático del formador en L11:
~~~bash
git status
git switch practica/manual
git pull --ff-only origin practica/manual
~~~
Haz `pull` únicamente con el árbol de trabajo limpio. **Rama opcional:** si deseas aislar una funcionalidad, crea `feature/gestion-reservas` desde `practica/manual`, presenta una MR **hacia `practica/manual`** y no continúes L06 hasta que el cambio aprobado se haya integrado en ella. No dejes el MVP únicamente en la rama feature. Anota la issue real y su relación con RF-01..RF-04.

## Paso 2 — metaprompt, prompt operativo y aprobación
Pide a Claude ejecutar **METAPROMPT.md** en modo «solo generar prompt»; debe guardar **alm/prompts-generados/03-desarrollo.md**. Examina el plan: ¿separa sala, reserva y validaciones?, ¿respeta arquitectura?, ¿incluye comandos para instalar, ejecutar y probar?, ¿enumera restricciones? No autorices cambios hasta comprobarlo.

## Paso 3 — primer incremento: salas
Autoriza generar un endpoint **GET /salas** con datos de ejemplo o persistidos según diseño. Comprueba que FastAPI se inicia. El resultado es una respuesta JSON legible y comprobable desde navegador o herramienta HTTP. No añadas una interfaz compleja antes de que la API responda.

Prueba manual: realiza la petición, observa HTTP 200 y la estructura de salas. Registra si los datos son persistentes o de arranque.

## Paso 4 — segundo incremento: alta de reservas
Autoriza implementar el modelo y **POST /reservas** con validación de sala y fechas. Prueba al menos un caso válido y una fecha inicial posterior a la final. La respuesta debe permitir reconocer qué reserva se creó; una entrada inválida no puede dejar cambios parciales.

### Caso mínimo de éxito
Sala S1 sin reservas. Solicitar S1 de 10:00 a 11:00 (misma fecha y zona explícita). Debe guardarse y ser recuperable o verificable con los datos de la API.

## Paso 5 — tercer incremento: evitar conflictos
Ahora pide únicamente la regla RF-03. Explica por qué es una regla de negocio y no un detalle de interfaz. Pide a Claude que no modifique tests para silenciar un fallo. Ejecuta manualmente tres casos:
- Reserva 10:00–11:00 activa; solicitar 10:30–11:30 → rechazo 409.
- Reserva 10:00–11:00 activa; solicitar 11:00–12:00 → aceptada si no hay otra reserva.
- Reserva activa de S1; misma hora para S2 → aceptada.

Si se produce un resultado diferente, captura entrada, salida y causa probable; pide corrección focalizada y repite.

## Paso 6 — cuarto incremento: cancelación
Pide implementar **DELETE /reservas/{id}** o ruta acordada para cancelar una reserva existente. Prueba la misma franja de tiempo antes y después de cancelar: después debe poder reservarse de nuevo. Comprueba que cancelar una reserva inexistente tiene una respuesta consistente con los requisitos.

## Paso 7 — prueba de la aplicación y diff
Lee los cambios:
~~~bash
git diff
git status
~~~
Inspecciona imports, validaciones, tratamiento de timezone, existencia de sala y control de conflictos. La revisión del alumno es parte de la práctica, aunque Claude haya realizado las modificaciones. Ejecuta los comandos que existan en README; si no existen, pide a Claude que los documente y después ejecútalos.

## Paso 8 — versionar y solicitar revisión
En el recorrido principal, confirma con `git branch --show-current` que estás en `practica/manual`. Revisa también cualquier ruta adicional que hayas creado y añádela de forma explícita. Tras Gate B:
~~~bash
git add app tests docs alm README.md requirements.txt
git diff --cached --stat
git commit -m "feat: implementar reservas y control de disponibilidad"
git push -u origin practica/manual
~~~
Las rutas y nombres pueden variar según el proyecto real. Si trabajaste directamente en `practica/manual`, abre una **Merge Request en borrador** desde `practica/manual` hacia `main`, enlaza las issues y **no la fusiones durante L05–L09**: las siguientes prácticas completarán el mismo recorrido. Si elegiste la rama feature, sustituye la línea de push del bloque por `git push -u origin HEAD` desde la feature. La MR debe apuntar a `practica/manual`; tras las comprobaciones y aprobación humana, integra el cambio allí y vuelve a `practica/manual`.

## Evidencia obligatoria
1. Rutas reales del código generado y del prompt operativo.
2. Solicitud HTTP de éxito y rechazo solapado (captura de salida o log textual).
3. Diff revisado y lista de problemas detectados.
4. Enlace real de MR, o estado «pendiente» si no hubo acceso.
5. Registro de gate en **alm/evidencias/registro.md**.

## Errores típicos del taller
**Claude afirma que funciona:** exigir ejecución. **Reserva contigua rechazada:** revisar comparación de intervalos. **Prueba en otra sala falla:** el filtro no considera el identificador de sala. **Dependencias sobredimensionadas:** reducirlas al stack. **Código sin persistencia pese al diseño:** corregir la discrepancia. **MR sin referencias:** añadir enlaces a RF e issues.

## Fin del L05
La aplicación debe ejecutar las operaciones del MVP. En L06 se convertirán los criterios en pruebas más completas y se introducirán revisiones de seguridad. En L07 se integrarán dichas comprobaciones en GitLab CI/CD.


## Cómo publica Claude Code los resultados de L05

1. Consulta la **issue real** en GitLab web, con MCP o con `glab issue view N` (opcional).
2. Confirma `git status` y sincroniza con `git fetch origin` y `git pull --ff-only` en la rama correcta. Si hay cambios locales, revísalos antes de hacer pull.
3. Claude genera primero `alm/prompts-generados/03-desarrollo.md`. **Gate A:** revisa y autoriza ese archivo; el modo Plan no sustituye su aprobación.
4. Tras la ejecución, comprueba salida real de tests y `git diff`. **Gate B:** no autorices commit/push sin revisar.
5. Autoriza commit y `git push` en `practica/manual`; abre o actualiza la MR en borrador hacia `main`. No la fusiones automáticamente; la CI se verificará en L07.

**Git no equivale a MCP:** en el clon se publica normalmente mediante Git; en Claude web + MCP los cambios pueden escribirse directamente en GitLab, pero requieren los mismos gates.
