# L10 · METAPROMPT: Claude diseña un pipeline ALM ejecutado por GitLab

~~~text
Actúa como ingeniero especialista en GitLab CI/CD, Claude Code y Application Lifecycle Management.

Primero redacta en evidencias/prompt-L10.md un único prompt operativo para construir el orquestador. Incluye en él las instrucciones siguientes. Muestra el prompt y detente hasta recibir la aprobación.

Al ejecutar el prompt aprobado debes GENERAR un archivo .gitlab-ci.yml para que sea GITLAB quien EJECUTE automáticamente el ciclo ALM, utilizando Claude Code como motor generativo en cada job. No diseñes un script local que sustituya a GitLab.

Entradas:
- CLAUDE.md y alm/maestro.md.
- Los seis contratos de alm/contratos/.
- Los seis metaprompts de alm/metaprompts/.
- docs/instrucciones/CASO_NEGOCIO.md, evidencias/L01.md y evidencias/L02.md de la etiqueta entrada-l02. El preflight compara estos dos últimos archivos con su versión etiquetada y bloquea si faltan o difieren.

Etapas obligatorias ordenadas:
alm_requisitos → alm_diseno → alm_desarrollo → alm_testing → alm_devops → alm_evolucion.

Cada etapa tiene que:
1. Leer su metaprompt y generar el prompt operativo correspondiente.
2. Ejecutar el prompt operativo con Claude Code CLI en el runner GitLab.
3. Guardar artefactos reales en rutas documentadas.
4. Obtener mediante artifacts los resultados necesarios de todas las etapas anteriores.
5. Ejecutar validaciones técnicas y detenerse si falta un documento o falla pytest.
6. Conservar logs y evidencias para la revisión final.

Seguridad/coste:
- Utilizar ANTHROPIC_API_KEY únicamente desde variable CI/CD enmascarada.
- NO introducir claves en YAML ni en logs.
- Limitar turnos, timeout y concurrencia.
- Lanzar el ALM solo con un trigger manual explícito en la rama practica/automatica.
- No hacer push, merge ni despliegue sin aprobación humana.
- La fase DevOps genera CI de la aplicación como archivo independiente del pipeline ALM actual.

Tras aprobar el prompt, genera el YAML y los scripts auxiliares imprescindibles, explica con un esquema el paso de artefactos y proporciona una checklist de revisión. No ejecutes la API ni comprometas presupuesto sin aprobación expresa del formador. En esta edición solo él ejecuta el pipeline en su proyecto GitLab.
~~~

**Criterio de aprobación:** GitLab controla el pipeline y Claude ejecuta las fases. No se considera automatización GitLab un script que únicamente corre en el ordenador del alumno.
