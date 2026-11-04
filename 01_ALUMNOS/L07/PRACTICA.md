# L07 · PRÁCTICA: generar y ejecutar CI/CD en GitLab

**75 min:** teoría 10, diseño 10, generación/revisión 15, ejecución remota 25, reparación/cierre 15.

## Entradas
Aplicación de L05, pruebas de L06, **alm/contratos/05-devops.md**, requirements y comandos locales reales. El proyecto ya debe tener una rama y MR abierta o lista para crearse.

## Paso 1 — define antes de pedir YAML
El alumno escribe las condiciones de aceptación del pipeline: cada actualización de MR debe lanzar validación; pytest debe fallar el job si falla un test; un paquete o artefacto se guarda al finalizar; los secretos no se escriben en YAML. Decide con el formador si el runner puede ejecutar Python sin Docker.

## Paso 2 — generar prompt operativo
Ejecuta **METAPROMPT.md** y exige **alm/prompts-generados/05-devops.md**. Comprueba que el prompt conoce las rutas reales de la aplicación y los comandos que ya funcionan localmente. No permitir que Claude invente un despliegue en AWS o una variable secreta que nadie ha provisionado.

## Paso 3 — crear .gitlab-ci.yml
Tras aprobar el prompt, Claude genera el YAML del pipeline GitLab con las fases necesarias: al menos test y un job de preparación de artefactos; lint si encaja. El alumno debe localizar cada job y explicar qué valida, qué dispara el pipeline y cómo se asegura de que un fallo de pytest no pasa inadvertido.

## Paso 4 — inspección y push
Revisa el YAML y haz commit en la rama de trabajo:
~~~bash
git add .gitlab-ci.yml
git commit -m "ci: comprobar app y tests desde GitLab"
git push
~~~
Abre la pestaña **CI/CD → Pipelines** de GitLab y busca la ejecución asociada a ese commit o MR. **No está aprobado hasta comprobar su estado en la instancia real.**

## Paso 5 — diagnosticar fallos
Si el pipeline falla, abre el job, conserva el extracto de log y pide a Claude:
«Diagnostica el fallo observado. Distingue problema de YAML, dependencia, test o runner. Propón la corrección mínima; no desactives las comprobaciones».
Revisa el diff; vuelve a hacer commit y repite la ejecución. Si el problema es el runner, registra el bloqueo de infraestructura en lugar de modificar código que funciona.

## Paso 6 — artefacto y entrega
Comprueba en GitLab la existencia del archivo o paquete que define el job. Descárgalo si está permitido y demuestra cómo arrancar la aplicación en entorno local conforme al README. No afirmes que el producto se ha desplegado en producción: este taller entrega un **MVP verificable**, no un servicio productivo.

## Evidencia y gate
Registrar:
- URL real de MR y pipeline, commit, jobs ejecutados y estado.
- Comandos y resultados, indicando qué parte se comprobó remotamente.
- Registro del fallo/reparación si ocurrió.
- Artefacto generado y guía breve de uso.
- Aprobación humana; no merge automático.
