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
8. Introduce el nombre `coworking-alm-junior`.
9. Comprueba el **namespace / Project URL**: debe ser **tu propio usuario**, no un grupo compartido del formador. El resultado previsto es `https://gitlab.com/TU_USUARIO/coworking-alm-junior`.
10. Utiliza el slug `coworking-alm-junior`, si está disponible. Si ya tienes un proyecto con ese nombre, añade un sufijo corto, pero conserva el mismo caso didáctico.
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
Utiliza un plan compatible con Claude Code. Si la empresa gestiona la autenticación, sigue sus instrucciones. Una variable `ANTHROPIC_API_KEY` activada podría cambiar la facturación a API: para los laboratorios guiados no se necesita. L10 utiliza una API autorizada dentro de GitLab CI/CD, facturada por separado.

## 4. Importar y verificar la plantilla: procedimiento Windows probado

**Regla:** ejecuta los comandos en **PowerShell** desde una carpeta que contenga los dos clones (por ejemplo, tu carpeta de usuario). No escribas a mano la URL ni presupongas que el proyecto siempre se llama `coworking-alm-junior`.

19. Copia desde **GitLab → Code → Clone with HTTPS** la URL exacta del proyecto privado vacío. Comprueba tu nombre de usuario de GitLab.

20. Abre PowerShell y obtén una sola vez los materiales del curso:

~~~powershell
cd $HOME
git clone https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO.git
~~~

Si ya tienes ese clon, no lo dupliques. Nunca copies su directorio `.git` al proyecto del alumno.

21. Prepara la plantilla **sin publicarla**. Sustituye la URL de ejemplo por la dirección HTTPS copiada desde tu GitLab:

~~~powershell
$repo = "https://gitlab.com/TU_USUARIO/NOMBRE_REAL_DEL_PROYECTO.git"
& ".\CLAUDE-ALM-GENERATIVO\scripts\Preparar-L02.ps1" -GitLabRepoUrl $repo -CarpetaTrabajo $HOME
~~~

[Preparar-L02.ps1](../../scripts/Preparar-L02.ps1) detecta el nombre real del proyecto y clona GitLab; después copia únicamente la plantilla, incluidos archivos ocultos. Comprueba las rutas y crea localmente el commit, `main`, la etiqueta `base-alm` y la rama `practica/manual`. Se detiene si detecta cambios sin confirmar o un estado que no deba sobrescribirse.

Si ves `No se ha hecho push`, el paso 21 ha terminado correctamente. Mantén abierta esa ventana de PowerShell. Sigue con el paso 22 para revisar y con el 23 para publicar. En el PDF de 23 páginas, ambos están en la página 7.

22. Verifica el resultado antes de hacer push:

~~~powershell
$nombre = ($repo.TrimEnd("/") -split "/")[-1] -replace "\.git$", ""
cd (Join-Path $HOME $nombre)
Get-ChildItem -Force
git status
git log -1 --oneline
git branch --list
git tag --list
~~~

Deben existir `CLAUDE.md`, `alm/maestro.md`, `alm/contratos/`, `alm/metaprompts/`, `alm/evidencias/registro.md`, `docs/instrucciones/CASO_NEGOCIO.md`, `.gitlab/`, `app/` y `tests/`. Los seis contratos y los seis metaprompts se comprueban antes del commit.

23. **Tras revisar**, publica el estado inicial:

~~~powershell
cd $HOME
& ".\CLAUDE-ALM-GENERATIVO\scripts\Preparar-L02.ps1" -GitLabRepoUrl $repo -CarpetaTrabajo $HOME -Publicar
~~~

La segunda ejecución no duplica commits. Publica `main`, `base-alm`, `practica/manual` y comprueba `origin/main`. Si GitLab solicita autenticación, utiliza Git Credential Manager o el navegador; no pegues contraseñas ni tokens en Claude.

24. Comprueba en GitLab las dos ramas y la etiqueta. En PowerShell:

~~~powershell
cd (Join-Path $HOME $nombre)
git ls-remote --heads origin
git ls-remote --tags origin
git status
~~~

25. Activa la rama de trabajo para L03 y abre el proyecto en VS Code:

~~~powershell
git switch practica/manual
git status
code .
~~~

Si `code` no está en el PATH, abre la carpeta desde VS Code. Nunca desarrolles las prácticas L03–L09 directamente sobre `main`.

**¿Y si prefieres los comandos manuales?** El formador puede explicar la secuencia `clone → copiar plantilla → status → add → commit → push → tag → branch`, pero no se debe combinar el procedimiento manual con el script en un clon parcialmente configurado. En particular, la instrucción para copiar archivos ocultos en PowerShell incluye un separador `|` entre dos comandos: si al pegar desde un PDF se pierde, el comando falla.

**Alcance de la prueba:** [GitHub Actions en Windows](https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO/actions) ejecuta este script contra un remoto Git vacío simulado con dos nombres de proyecto y lo repite para detectar duplicados. **No sustituye** comprobar la autenticación y los permisos del GitLab real.

## 5. Primer commit, rama y versión base

El primer commit publicado en `main` contiene exclusivamente la plantilla. La etiqueta `base-alm` debe apuntar exactamente a ese commit, y `practica/manual` debe nacer desde ese mismo estado. El script prepara y verifica esas referencias. El alumno debe poder explicarlas y comprobarlas.

Puedes proteger `base-alm` desde las opciones **Protected tags** de GitLab, según permisos de tu proyecto. Nunca uses `git tag -f` ni `git push --force` para ocultar un conflicto.

## 5.1 Alternativa macOS/Linux: importación manual con Bash

Utiliza **solo este procedimiento si no has ejecutado el script PowerShell** en ese clon. Trabaja desde una carpeta padre, con el GitLab privado recién creado, vacío y sin README. Copia siempre la URL HTTPS exacta desde GitLab y sustitúyela en el primer comando.

~~~bash
cd "$HOME"
git clone https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO.git
repo="https://gitlab.com/TU_USUARIO/NOMBRE_REAL_DEL_PROYECTO.git"
git clone "$repo"
nombre="$(basename "$repo" .git)"
cd "$nombre"
git symbolic-ref HEAD refs/heads/main
cd ..
cp -R CLAUDE-ALM-GENERATIVO/03_GITLAB_PLANTILLA/. "$nombre"/
cd "$nombre"
git status
git add -A
git commit -m "chore: incorporar plantilla del curso"
git push -u origin main
git tag base-alm
git push origin base-alm
git switch -c practica/manual
git push -u origin practica/manual
git status
~~~

El sufijo \`/.\` de la carpeta origen incluye los archivos ocultos \`.gitignore\` y \`.gitlab/\`. No copies la carpeta \`.git\` de los materiales. El comando \`git clone\` del curso se omite si ya existe localmente. **No repitas este bloque desde cero sobre un repositorio que ya tiene commits:** verifica el estado de las ramas y detente ante divergencias. El alumnado que trabaje en Windows debe usar el procedimiento PowerShell de los apartados 4 y 5, verificado automáticamente.

## 6. Configuración GitLab recomendada

26. Comprueba que el proyecto sigue siendo **Private**. En el apartado 7 aprenderás a invitar al formador como miembro **Developer**, sin hacerlo público.
27. Comprueba que **Issues** y **Merge Requests** están habilitados. Se utilizarán en L03 y L05.
28. Comprueba la protección de la rama `main` en **Settings → Repository / Branch rules** según la versión. No se hará merge sin revisión humana.
29. En **Settings → CI/CD → Runners** verifica que hay runners disponibles. GitLab.com suele ofrecer runners alojados; si tu cuenta no puede utilizarlos, documenta el bloqueo y avisa al formador.
30. No añadas claves API de Anthropic a tu GitLab para este taller. En L10 se estudiará dónde configurar `ANTHROPIC_API_KEY`, pero la ejecución automática la realizará **únicamente el formador** en su GitLab. Recibirás los resultados mediante Git, sin consumir API.

## 7. Invitar al formador como Developer (obligatorio)

Durante el taller, el formador hará una única ejecución del pipeline ALM generativo en su propio GitLab. Después distribuirá una copia de los artefactos a tu repositorio privado. **Para ello no necesitas hacerlo público, ni compartir contraseñas o claves API**: debes concederle acceso **Developer**.

**Dato previo:** el formador facilitará en clase su **nombre de usuario exacto de GitLab**. En este manual aparece el marcador `USUARIO_GITLAB_FORMADOR`; no lo utilices literalmente.

31. Inicia sesión en GitLab y abre **tu proyecto mediante la URL real que copiaste en el paso 14**, aunque su nombre no sea `coworking-alm-junior`.
32. En el menú lateral izquierdo entra en **Manage → Members** (Gestionar → Miembros).
33. Haz clic en **Invite members** (Invitar miembros).
34. En el campo de búsqueda introduce el nombre de usuario de GitLab del formador y selecciona su cuenta. Si tiene una cuenta GitLab existente, es preferible invitarlo por usuario y no por correo.
35. En **Select a role**, selecciona exactamente **Developer**. Este rol puede escribir en ramas no protegidas y abrir Merge Requests, pero no administra el proyecto. No selecciones Guest, Reporter, Maintainer ni Owner.
36. Si se ofrece **Access expiration date**, puedes establecer una fecha posterior a la revisión y distribución de resultados. No pongas una fecha que venza durante el taller.
37. Pulsa **Invite**. Vuelve a **Manage → Members** y comprueba que aparece el usuario correcto con el rol **Developer**. Una invitación enviada por correo puede quedar pendiente de aceptación.
38. Copia la URL HTTPS de la página principal de **tu proyecto** (por ejemplo, `https://gitlab.com/TU_USUARIO/coworking-alm-junior`). Envía al formador mediante el canal del curso **esa URL y tu usuario de GitLab**. No envíes contraseñas, claves API, tokens de acceso ni códigos de seguridad.
39. Cuando el formador distribuya la salida de su pipeline, verifica en **Code → Branches** que existe `referencia/alm-automatico`. Esa rama contendrá el resultado de **la ejecución del formador**, y no debe sobrescribir `practica/manual` ni `main`.
40. Después de que el formador confirme que la entrega está finalizada, puedes retirar su acceso en **Manage → Members → Remove member**. Los archivos ya recibidos permanecerán en tu repositorio.

**Si el formador no puede escribir:** comprueba el usuario, el rol y que intenta subir una **rama no protegida**. No cambies la visibilidad a Public, no le concedas Maintainer y no desprotejas `main` para solucionar un problema de permisos.

Documentación oficial: https://docs.gitlab.com/user/project/members/ y https://docs.gitlab.com/user/permissions/

## 8. Verificación de finalización

- [ ] Puedo entrar a mi cuenta GitLab.
- [ ] Mi proyecto personal existe y está configurado como **Private**.
- [ ] Tiene la plantilla, no la solución preimplementada.
- [ ] Tengo un commit inicial y el tag `base-alm`.
- [ ] Existe la rama `practica/manual`.
- [ ] Puedo ejecutar `claude auth status` y veo una sesión autorizada.
- [ ] He comprobado los runners o documentado la limitación.
- [ ] He invitado al formador con el rol **Developer**.
- [ ] He confirmado que mi proyecto continúa siendo **Private**.
- [ ] He enviado al formador únicamente mi usuario GitLab y la URL del proyecto.
- [ ] Sé que recibiré los resultados automáticos en `referencia/alm-automatico`.

**Resultado L02:** una plataforma de trabajo personal preparada para crear artefactos ALM con Claude. Ninguna especificación de requisitos se considera todavía generada.
