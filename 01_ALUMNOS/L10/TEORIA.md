# L10 · TEORÍA: automatizar el ALM generativo sin perder trazabilidad

**Duración total:** 180 minutos. Este laboratorio es una segunda forma de ejecutar **el mismo caso práctico**, no un proyecto nuevo.

## 1. Qué cambia respecto al modo guiado

En L03–L09 el alumno dirige cada fase: lanza el metaprompt, revisa el prompt operativo generado, aprueba su ejecución y comprueba sus artefactos. En L10 un **ejecutor local** lee una configuración de pipeline y encadena esas operaciones, haciendo avanzar el proyecto cuando los controles automáticos mínimos se cumplen. El alumno aprueba globalmente el recorrido y revisa el resultado final.

La automatización no sustituye el requisito ni el diseño: utiliza los mismos contratos y la misma descripción de Coworking Norte. Lo único que cambia es quién dispara la siguiente fase. El objetivo didáctico es comparar **control humano fase a fase** frente a **orquestación con gates técnicos automáticos**.

## 2. Tres pipelines, dos propósitos

- **ALM manual:** ejecución guiada de contratos de ingeniería generativa. Existe en la rama `practica/manual`.
- **ALM automático:** ejecutor `scripts/alm_auto.py` y configuración `alm/pipeline_auto.json` creada con Claude. Existe en la rama `practica/automatica`. Se ejecuta en el ordenador del alumno.
- **GitLab CI/CD:** archivo `.gitlab-ci.yml` generado en la fase DevOps; GitLab Runner realiza pruebas y empaquetado cuando recibe el push. No genera los requisitos ni sustituye al pipeline ALM.

Un job remoto de GitLab que invocase Claude necesitaría una integración con API facturada; el taller no la necesita y no presupone ese gasto.

## 3. Diseño del pipeline automático

En lugar de pedir «genera todo el software» mediante una única frase, crearemos un **pipeline declarativo**. Cada una de sus seis etapas identifica el contrato, el metaprompt, la ruta del prompt operativo generado y las salidas exigidas. El ejecutor reconoce exclusivamente esas rutas, para evitar que una configuración invente comandos arbitrarios o añada funciones fuera de alcance.

El ciclo interno de cada etapa es:

1. Comprobar que existe el contrato y su metaprompt.
2. Invocar `claude -p` para generar un prompt operativo específico de la fase.
3. Comprobar que dicho archivo se escribió.
4. Invocar de nuevo `claude -p` para ejecutar ese prompt.
5. Validar los archivos resultantes; en testing y evolución ejecutar `pytest`.
6. Guardar el estado y, si no hay bloqueo, continuar con la siguiente fase.

Es la misma arquitectura de dos generaciones del modo manual, pero el alumno no debe introducir una instrucción en cada etapa. **No equivale a garantizar corrección de negocio**: una verificación automática de rutas y tests no sustituye la revisión final.

## 4. Continuidad de los artefactos

El pipeline jamás empieza de otra especificación entre fases. La fase de diseño consume la especificación generada en requisitos. El desarrollo consume esa especificación, el backlog, el diseño y el ADR. Testing consume los requisitos y el código real. DevOps consume código y tests. Evolución incorpora CAM-01 a los documentos y pruebas existentes.

El ejecutor no contiene una solución de coworking: solamente sabe el orden y los contratos de salida. **Claude debe generar** la especificación, diagramas, implementación, pruebas y CI durante la ejecución.

## 5. Seguridad, cuotas y límites

La ejecución se hace con la CLI Claude Code oficial y la cuenta autenticada del alumno. El script no almacena credenciales ni hace push/merge/despliegue. Permite exclusivamente lectura y edición de archivos, no concede Bash al agente; las pruebas las ejecuta Python desde el propio orquestador.

El modo automático requiere más invocaciones que una demo abreviada, y Claude Pro puede alcanzar sus límites. Si ocurre, el sistema se detiene con estado de fases completadas y permite `--resume` después de revisar el bloqueo; el alumno no debe fingir que completó todas las fases.

El script bloquea `ANTHROPIC_API_KEY`, porque esa variable podría facturar consumo API en lugar de utilizar la suscripción. No uses `--bare`: la documentación oficial indica que ese modo no usa la autenticación por suscripción.

## 6. Gates automáticos y humanos

En el recorrido manual hay dos aprobaciones por fase. En el automático se solicita una aprobación inicial del plan global y del alcance. Los gates automáticos comprueban presencia de archivos, identificadores RF, configuración CI básica y resultados de pytest. Si Claude detecta una pregunta de negocio no resuelta, debe generar un bloqueo y detenerse. Al final debe existir una revisión humana de la rama antes de subirla y abrir una MR.

## 7. Qué se comparará

Calidad de la especificación, coherencia entre diseño y código, pruebas y su cobertura de criterios, número de intervenciones humanas, causas de bloqueo, tiempo observado y cantidad de invocaciones. No se comparará «cuántas líneas escribió Claude» ni se atribuirá fiabilidad a un pipeline solo porque terminó.

**Conclusión:** la automatización convierte una secuencia dirigida manualmente en un sistema reproducible de instrucciones y gates. El desarrollador pasa de conducir cada paso a diseñar y auditar el proceso, sin delegar la responsabilidad del software.