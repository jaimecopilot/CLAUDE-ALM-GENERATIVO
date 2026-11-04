# L05 · PRÁCTICA: generar Coworking Manager con Claude Code

**Tiempo: 210 min.** Preparación y explicación 25; prompt/plan 25; incremento de salas 35; reservas y conflictos 65; cancelación 25; validación, registro y revisión 35.

## Entradas aprobadas y alcance
- **docs/requisitos/especificacion.md** con RF-01..RF-04 y CA etiquetados.
- **docs/arquitectura/diseno.md** y ADR de L04.
- **alm/contratos/03-desarrollo.md**.
- Directorio de código inicialmente vacío o mínimo, sin solución de referencia.

**Prohibido**: pedirle a Claude que implemente login, cobros, notificaciones, Kubernetes o conectores externos; tampoco copiar la solución del profesor.

## Paso 1 — localizar el trabajo de GitLab
Selecciona issues ordenadas del backlog. Crea una rama de feature o utiliza la rama entregada por el formador:
~~~bash
git status
git switch -c feature/gestion-reservas
~~~
Si la rama existe, no repitas el comando; mantén el historial. Anota el identificador real de issue y cómo se relaciona con RF-01..RF-04.

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
Realiza commit descriptivo y push cuando los cambios estén razonablemente revisados:
~~~bash
git add app tests docs alm
git commit -m "feat: implementar reservas y control de disponibilidad"
git push -u origin feature/gestion-reservas
~~~
Las rutas y nombres pueden variar según el proyecto real. Abre una **Merge Request** a la rama protegida que corresponda, enlaza las issues y resume las pruebas locales. **No la fusiones sin revisión.**

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