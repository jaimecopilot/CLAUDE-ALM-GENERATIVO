# L10 · TEORÍA: GitLab orquesta un ALM generativo automático

**Duración: 180 minutos.** Segunda ejecución del mismo Coworking Manager.

## 1. ¿Quién hace qué?

**Claude Code**, utilizado por el alumno, diseña el archivo `.gitlab-ci.yml` a partir de los seis contratos y metaprompts. **GitLab** ejecuta ese archivo en sus runners: controla el orden, las dependencias, los logs y el paso de artefactos. **Claude Code en cada job** genera primero el prompt operativo y después el artefacto de esa fase. **El alumno** revisa y aprueba antes de lanzar y antes de integrar el resultado.

La primera generación del YAML es guiada porque GitLab no puede lanzar un pipeline que todavía no existe. Una vez versionado y aprobado, se ejecuta desde **GitLab → Build → Pipelines**. No consiste en arrancar un script Python local.

## 2. Seis jobs y una cadena de artefactos

1. `alm_requisitos`: consume `docs/instrucciones/CASO_NEGOCIO.md`; produce especificación, backlog y criterios Gherkin.
2. `alm_diseno`: recibe por **GitLab artifacts** los requisitos generados; produce arquitectura, Mermaid y ADR.
3. `alm_desarrollo`: recibe **requisitos + diseño**; produce código FastAPI y dependencias, sin inventar otra especificación.
4. `alm_testing`: recibe **requisitos + código**; produce tests, los ejecuta y detiene el pipeline si fallan.
5. `alm_devops`: recibe **código + tests**; genera la configuración CI/CD del producto como archivo separado de la orquestación que está ejecutándose.
6. `alm_evolucion`: recibe los anteriores y aplica CAM-01 (máximo de cuatro horas), con pruebas de regresión.

Un job GitLab no conserva por sí solo archivos de otro runner. Se deben transferir mediante **job artifacts**, con `needs: artifacts` o la descarga estándar de etapas anteriores. Los artefactos finales quedan asociados al pipeline y deben revisarse y versionarse mediante una Merge Request separada; no se hace merge automático.

## 3. ALM automático y CI/CD de producto no son lo mismo

El pipeline **ALM** utiliza Claude para generar y transformar especificaciones y código. El pipeline **CI/CD** generado como artefacto en DevOps valida y empaqueta el producto en ejecuciones posteriores. La configuración que está ejecutando el ALM no debe autodestruirse o reescribirse mientras corre.

## 4. Autenticación y coste

La integración oficial Claude Code + GitLab CI/CD requiere una clave **Anthropic API** guardada en GitLab como variable `ANTHROPIC_API_KEY` enmascarada (o un proveedor cloud compatible). **Claude Pro de 20 USD no cubre estos consumos remotos**. También se utilizan minutos de GitLab Runner. Nunca se añade una clave a la documentación, al YAML o a un prompt.

Cada alumno con su propio GitLab solo puede ejecutar remotamente con credenciales autorizadas y presupuesto delimitado. Una clave central del formador **no** debe copiarse a doce repositorios controlados por estudiantes. La alternativa de una demostración del formador se diferencia claramente de doce ejecuciones individuales.

Usar límites de gasto por workspace, máximo de turnos, tiempos de job y una regla que ejecute el pipeline únicamente al lanzarlo manualmente, para evitar bucles que consuman crédito. No declarar «completado» un job que falló por presupuesto, autorización o un criterio funcional.

## 5. Comparación de las dos modalidades

En el modo **guiado** hay decisiones humanas en cada fase. En el modo **automático** GitLab encadena trabajos y verifica gates técnicos, pero una revisión humana final sigue siendo imprescindible. Ambas ejecuciones parten del mismo `base-alm`, de los mismos contratos y del mismo caso. Se comparan resultados, errores, pruebas y trazabilidad.

**Estado:** diseño pedagógico documentado. La ejecución real de GitLab y el consumo API deben verificarse con credenciales y runners disponibles antes de afirmar que un pipeline ha terminado.