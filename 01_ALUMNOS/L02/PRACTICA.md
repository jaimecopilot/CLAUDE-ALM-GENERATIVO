# L02 · PRÁCTICA: crear el espacio que ejecutará el ALM

**Duración: 60 min.** 15 explicación, 30 preparación guiada, 10 primer metaprompt, 5 comprobación.

## Antes de comenzar
El formador entrega URL de GitLab de cada equipo y plantilla del proyecto. No se crea un repositorio separado por cada alumno dentro del mismo equipo. Cada estudiante utiliza su cuenta de Claude Code; no se comparten contraseñas ni sesiones.

## Paso 1 — distinguir repositorios (5 min)
Abre este GitHub del curso y el GitLab del equipo. Explica en voz alta qué cambia en cada uno. En GitHub **estudiamos materiales**; en GitLab **producimos la aplicación**. La solución del formador no se publica en el repositorio del alumno.

## Paso 2 — clonar y preparar (10 min)
Comprueba que Git, Python, VS Code y Claude Code están disponibles. En una terminal usa:
~~~bash
git clone URL_REAL_DE_GITLAB
cd NOMBRE_DEL_PROYECTO
git switch -c laboratorio/inicio-alm
git status
~~~
No copies literalmente los marcadores de URL; reemplázalos por el enlace proporcionado. Si GitLab ya tiene una rama de laboratorio creada, utilízala en lugar de crear otra.

## Paso 3 — reconocer el contrato (10 min)
Abre **CLAUDE.md**, **alm/maestro.md** y **alm/contratos/01-requisitos.md**. Identifica en el contrato entradas, salidas y criterios de aceptación. Pregunta: ¿cuál es la diferencia entre el contrato y un requisito funcional? **Respuesta:** el contrato define cómo operar una fase; la especificación funcional será uno de sus resultados.

## Paso 4 — invocar Claude Code (10 min)
Abre Claude Code dentro del directorio de trabajo conforme a la instalación autorizada de la empresa. Pide que lea únicamente las instrucciones y el contrato; comprueba que NO ha creado aún la aplicación. No introduzcas tokens de GitLab en el prompt.

## Paso 5 — generar el primer prompt operativo (10 min)
Ejecuta el texto de **METAPROMPT.md**. Claude debe generar un archivo **alm/prompts-generados/01-requisitos.md**. Revísalo antes de autorizar la ejecución: entradas reales, artefactos esperados, restricciones, validación y condiciones de parada.

## Paso 6 — registrar evidencia (5 min)
Guarda **alm/evidencias/L02.md** con ruta del prompt generado y un breve informe de revisión; crea commit si la configuración y el acceso están correctos. No hacer merge directo a main.

**Fin de laboratorio:** el alumno demuestra la distinción entre GitHub docente, GitLab de trabajo y Claude motor; localiza contrato, metaprompt y prompt operativo; la aplicación todavía NO está generada.

**Si no hay GitLab remoto:** la práctica puede preparar un clon local, pero se etiqueta como preparación local y NO se declara la integración completada.
