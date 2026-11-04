# Guía L02 — Cuenta GitLab y proyecto personal, paso a paso

Esta guía se realiza **individualmente**. No hay un GitLab facilitado por el profesor. Cada alumno conserva su proyecto al finalizar. Si tu organización ya proporciona una cuenta en una instancia GitLab, usa esa cuenta e instancia según sus políticas.

## 1. Cuenta GitLab

1. Abre https://gitlab.com (o la instancia GitLab autorizada de tu empresa).
2. **Si tienes cuenta**, selecciona iniciar sesión y comprueba que puedes acceder a tus proyectos. No crees una segunda cuenta innecesaria.
3. **Si no tienes cuenta**, selecciona registrarte y completa el formulario. Verifica tu dirección de correo si GitLab lo solicita.
4. Configura cualquier comprobación de seguridad que solicite GitLab (por ejemplo, autenticación de dos factores). No compartas contraseñas, códigos de recuperación ni tokens.
5. En tu perfil identifica tu **nombre de usuario GitLab**. Lo necesitarás para crear un proyecto en tu espacio personal.
6. Vuelve al panel principal. No hace falta instalar un servidor GitLab: trabajaremos en GitLab.com.

## 2. Crear el proyecto

7. Selecciona **Create new → New project/repository → Create blank project** (los textos exactos pueden variar según idioma/versión).
8. Introduce el nombre \`coworking-alm-junior\`.
9. Comprueba el **namespace / Project URL**: debe ser **tu propio usuario**, no un grupo compartido del formador. El resultado previsto es \`https://gitlab.com/TU_USUARIO/coworking-alm-junior\`.
10. Utiliza el slug \`coworking-alm-junior\`, si está disponible. Si ya tienes un proyecto con ese nombre, añade un sufijo corto, pero conserva el mismo caso didáctico.
11. **Visibility: Private.** El alumno puede conceder acceso de revisión al formador más adelante, sin publicar el proyecto.
12. **Initialize repository with a README: desmarcado**, porque importaremos una plantilla de archivos ya preparada como primer commit.
13. No actives un despliegue cloud, Auto DevOps ni un proyecto de demostración diferente. Selecciona **Create project**.
14. Copia el enlace **Clone with HTTPS** que ofrece GitLab; guárdalo en tus apuntes, no dentro de un prompt con credenciales.

## 3. Herramientas locales

15. Comprueba que tu equipo tiene **Git**, **Python**, **VS Code** y **Claude Code**. Abre PowerShell si utilizas Windows.
16. Comprueba herramientas:
~~~powershell
git --version
python --version
claude --version
~~~
17. Configura tu identidad Git si aún no existe:
~~~powershell
git config --global user.name "Tu nombre"
git config --global user.email "tu-correo@ejemplo.com"
~~~
Sustituye esos ejemplos por tu identidad real. No copies claves de acceso ni contraseñas en los comandos del curso.

18. Inicia sesión en Claude Code mediante su interfaz de autenticación oficial:
~~~powershell
claude auth login
claude auth status
~~~
Utiliza un plan compatible con Claude Code. Si la empresa gestiona la autenticación, sigue sus instrucciones. Una variable \`ANTHROPIC_API_KEY\` activada podría cambiar la facturación a API: para este taller no se necesita.

## 4. Importar la plantilla GitLab

19. Clona el repositorio de **material docente** (necesitarás permiso de acceso porque es privado):
~~~powershell
git clone https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO.git
~~~
Si ya lo tienes, utiliza su carpeta local y omite esta operación.

20. Clona tu nuevo proyecto GitLab, aún vacío, utilizando **la URL exacta obtenida en el paso 14**:
~~~powershell
git clone https://gitlab.com/TU_USUARIO/coworking-alm-junior.git
~~~
Sustituye \`TU_USUARIO\` por el tuyo. Es normal que Git avise que el repositorio está vacío. Si la autenticación Git solicita credenciales, utiliza el procedimiento autorizado por GitLab, Git Credential Manager o SSH; no pegues tokens en Claude.

21. Desde la carpeta **padre de ambos clones** en PowerShell, copia exclusivamente los archivos de \`03_GITLAB_PLANTILLA\` al repositorio GitLab. Esto incluye archivos ocultos como \`.gitignore\` y \`.gitlab/\`:
~~~powershell
Get-ChildItem -LiteralPath ".\CLAUDE-ALM-GENERATIVO\03_GITLAB_PLANTILLA" -Force |
  Copy-Item -Destination ".\coworking-alm-junior" -Recurse -Force
~~~
Si tu clon GitLab tiene otro nombre de carpeta, adapta la ruta de destino. **No copies el manual del curso, la carpeta completa del GitHub ni las soluciones del formador**.

22. Abre la carpeta GitLab y comprueba las rutas:
~~~powershell
cd .\coworking-alm-junior
Get-ChildItem -Force
git status
~~~
Deben existir \`CLAUDE.md\`, \`alm/maestro.md\`, \`alm/contratos/\`, \`alm/metaprompts/\`, \`scripts/alm_auto.py\` y la plantilla de casos de negocio.

## 5. Primer commit, rama y versión base

23. Publica la plantilla:
~~~powershell
git add .
git commit -m "chore: incorporar plantilla del taller ALM"
git push -u origin HEAD:main
~~~
Si GitLab no te permite hacer push a main por una regla corporativa, utiliza el procedimiento de ramas y MR autorizado por tu instancia. No fuerces el push.

24. **Etiqueta el estado inicial** antes de generar ningún artefacto:
~~~powershell
git tag base-alm
git push origin base-alm
~~~
Este tag permitirá que L10 cree una segunda rama desde exactamente el mismo punto de partida. Sin él no podemos comparar limpiamente el modo guiado y el automático.

25. Crea la rama de trabajo manual:
~~~powershell
git switch -c practica/manual
git push -u origin practica/manual
~~~
Verifica que \`git status\` está limpio antes de comenzar L03. No realices todo el curso directamente sobre main.

## 6. Configuración GitLab recomendada

26. Abre el proyecto en GitLab y confirma **Project information → Members** (la ruta puede variar). El alumno es propietario de su proyecto personal; podrá invitar al formador con permiso mínimo de revisión si la actividad lo exige. No conceder permisos de administración ni compartir credenciales personales.
27. Comprueba que **Issues** y **Merge Requests** están habilitados. Se utilizarán en L03 y L05.
28. Comprueba la protección de la rama \`main\` en **Settings → Repository / Branch rules** según la versión. No se hará merge sin revisión humana.
29. En **Settings → CI/CD → Runners** verifica que hay runners disponibles. GitLab.com suele ofrecer runners alojados; si tu cuenta no puede utilizarlos, documenta el bloqueo y avisa al formador.
30. No es necesario añadir variables de CI con claves de Claude o tokens de Anthropic. El pipeline GitLab del L07 ejecutará pruebas Python, no invocaciones de IA.

## 7. Verificación de finalización

- [ ] Puedo entrar a mi cuenta GitLab.
- [ ] Mi proyecto personal existe y está configurado como **Private**.
- [ ] Tiene la plantilla, no la solución preimplementada.
- [ ] Tengo un commit inicial y el tag \`base-alm\`.
- [ ] Existe la rama \`practica/manual\`.
- [ ] Puedo ejecutar \`claude auth status\` y veo una sesión autorizada.
- [ ] He comprobado los runners o documentado la limitación.

**Resultado L02:** una plataforma de trabajo personal preparada para crear artefactos ALM con Claude. Ninguna especificación de requisitos se considera todavía generada.
