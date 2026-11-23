#Requires -Version 5.1
<#
.SYNOPSIS
  Prepara L02 desde un repositorio GitLab vacío usando la plantilla del curso.
.DESCRIPTION
  No borra archivos ni fuerza commits o pushes. Puede repetirse sin crear commits
  adicionales. Para una importación nueva requiere un proyecto remoto vacío.
.EXAMPLE
  .\Preparar-L02.ps1 -GitLabRepoUrl 'https://gitlab.com/USUARIO/coworking-alm-junior.git' -CarpetaTrabajo "$HOME" -Publicar
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$GitLabRepoUrl,

    [string]$CarpetaTrabajo = (Get-Location).Path,

    [string]$CursoLocal = "",

    [switch]$Publicar
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-Git {
    param([Parameter(Mandatory = $true)][string[]]$Args)
    & git @Args
    if ($LASTEXITCODE -ne 0) {
        throw "Git terminó con error ($LASTEXITCODE): git $($Args -join ' ')"
    }
}

function Get-GitText {
    param([Parameter(Mandatory = $true)][string[]]$Args)
    # Windows PowerShell 5.1 transforma stderr nativo en error terminante
    # con ErrorActionPreference=Stop, aunque Git devuelva un estado esperado
    # (por ejemplo, cuando HEAD todavía no tiene commits).
    $ErrorActionPreference = 'Continue'
    $output = & git @Args 2>$null
    $codigo = $LASTEXITCODE
    if ($codigo -ne 0) { return $null }
    return (($output | Out-String).Trim())
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw 'Git no está instalado o no está disponible en PATH.'
}

# No se permiten nombres de carpeta arbitrarios que puedan escapar del directorio padre.
$slug = (($GitLabRepoUrl.TrimEnd('/','\') -split '[/\\]')[-1] -replace '\.git$', '')
if ($slug -notmatch '^[A-Za-z0-9][A-Za-z0-9._-]*$' -or $slug -eq '.' -or $slug -eq '..') {
    throw 'La URL de GitLab no termina en un nombre de proyecto válido.'
}

$padre = [System.IO.Path]::GetFullPath($CarpetaTrabajo)
if (-not (Test-Path -LiteralPath $padre -PathType Container)) {
    New-Item -Path $padre -ItemType Directory -Force | Out-Null
}
$destino = Join-Path $padre $slug

if ([string]::IsNullOrWhiteSpace($CursoLocal)) {
    $curso = Join-Path $padre 'CLAUDE-ALM-GENERATIVO'
    if (-not (Test-Path -LiteralPath $curso)) {
        Write-Host 'Clonando materiales del curso desde GitHub...'
        Invoke-Git -Args @('clone','https://github.com/jaimecopilot/CLAUDE-ALM-GENERATIVO.git',$curso)
    }
} else {
    $curso = [System.IO.Path]::GetFullPath($CursoLocal)
}
$plantilla = Join-Path $curso '03_GITLAB_PLANTILLA'
if (-not (Test-Path -LiteralPath (Join-Path $plantilla 'CLAUDE.md') -PathType Leaf)) {
    throw "No se encuentra la plantilla del curso en: $plantilla"
}
if ([System.IO.Path]::GetFullPath($destino) -eq [System.IO.Path]::GetFullPath($curso)) {
    throw 'El repositorio de destino coincide con el repositorio de materiales.'
}

if (-not (Test-Path -LiteralPath $destino)) {
    Write-Host "Clonando el proyecto de práctica: $slug"
    Invoke-Git -Args @('clone',$GitLabRepoUrl,$destino)
}
if (-not (Test-Path -LiteralPath (Join-Path $destino '.git'))) {
    throw "La carpeta $destino ya existe y no es un clon Git. No se sobrescribe."
}
$origenActual = Get-GitText -Args @('-C',$destino,'remote','get-url','origin')
if ($origenActual -ne $GitLabRepoUrl) {
    throw "El origin del destino es '$origenActual', pero se pidió '$GitLabRepoUrl'. No se cambia."
}
$estado = (Invoke-Git -Args @('-C',$destino,'status','--porcelain','--untracked-files=all') | Out-String).Trim()
if ($estado) {
    throw "El destino tiene cambios sin confirmar. Revisa git status en: $destino"
}
$cabecera = Get-GitText -Args @('-C',$destino,'rev-parse','--verify','HEAD')
if (-not $cabecera) {
    $refs = @(Invoke-Git -Args @('-C',$destino,'ls-remote','--refs','origin'))
    if ($refs.Count -gt 0) {
        throw 'El remoto ya contiene referencias. Revisa su rama predeterminada antes de importar.'
    }
    if (@(Get-ChildItem -LiteralPath $destino -Force | Where-Object Name -ne '.git').Count) {
        throw 'El clon inicial contiene archivos locales, posiblemente ignorados. Revisa la carpeta.'
    }
    foreach ($cfg in @('user.name','user.email')) {
        if (-not (Get-GitText -Args @('-C',$destino,'config',$cfg))) {
            throw "Configura la identidad Git ($cfg) antes de copiar la plantilla."
        }
    }
    # La rama local de un clon vacío puede ser master, main u otra.
    Invoke-Git -Args @('-C',$destino,'symbolic-ref','HEAD','refs/heads/main')
    Write-Host 'Copiando archivos de la plantilla (también los ocultos)...'
    Get-ChildItem -LiteralPath $plantilla -Force | Copy-Item -Destination $destino -Recurse -Force
} else {
    if (-not (Get-GitText -Args @('-C',$destino,'rev-parse','--verify','refs/heads/main'))) {
        throw 'Ya existen commits, pero no hay rama local main. Revisión manual necesaria.'
    }
    Write-Host 'El repositorio ya tiene commits; no se sobreescriben archivos.'
}

# Control de integridad ANTES del commit.
$obligatorios = @(
    'CLAUDE.md', 'README.md', '.gitignore', 'requirements.txt',
    'alm/maestro.md', 'alm/contratos/01-requisitos.md',
    'alm/metaprompts/01-requisitos.md',
    'docs/instrucciones/CASO_NEGOCIO.md',
    'alm/evidencias/registro.md', 'app', 'tests', '.gitlab'
)
foreach ($rel in $obligatorios) {
    if (-not (Test-Path -LiteralPath (Join-Path $destino $rel))) {
        throw "Falta el archivo o directorio obligatorio: $rel"
    }
}
foreach ($tipo in @('contratos','metaprompts')) {
    $ruta = Join-Path $destino "alm/$tipo"
    $total = @(Get-ChildItem -LiteralPath $ruta -Filter '*.md' -File).Count
    if ($total -lt 6) {
        throw "Faltan archivos en $tipo. Esperados al menos 6; encontrados $total."
    }
}

if (-not $cabecera) {
    Invoke-Git -Args @('-C',$destino,'add','-A')
    $arbolFuente = Get-GitText -Args @('-C',$curso,'rev-parse','--verify','HEAD:03_GITLAB_PLANTILLA')
    $arbolPreparado = Get-GitText -Args @('-C',$destino,'write-tree')
    if (-not $arbolFuente -or $arbolPreparado -ne $arbolFuente) {
        throw 'El contenido preparado difiere de la plantilla versionada. Revisa git diff --cached.'
    }
    Invoke-Git -Args @('-C',$destino,'commit','-m','chore: incorporar plantilla del curso')
}

$mainSha = Get-GitText -Args @('-C',$destino,'rev-parse','refs/heads/main')
if (-not $mainSha) { throw 'No se pudo verificar main local.' }
$baseSha = Get-GitText -Args @('-C',$destino,'rev-parse','--verify','refs/tags/base-alm^{commit}')
if ($baseSha -and $baseSha -ne $mainSha) {
    throw 'La etiqueta base-alm apunta a otro commit; se requiere revisión humana.'
}
if (-not $baseSha) {
    $baseTree = Get-GitText -Args @('-C',$destino,'rev-parse','--verify','refs/heads/main^{tree}')
    $templateTree = Get-GitText -Args @('-C',$curso,'rev-parse','--verify','HEAD:03_GITLAB_PLANTILLA')
    if (-not $templateTree -or $templateTree -ne $baseTree) {
        throw 'main no coincide con la plantilla del curso. No se crea base-alm.'
    }
    Invoke-Git -Args @('-C',$destino,'tag','base-alm',$mainSha)
}

$ramaManual = Get-GitText -Args @('-C',$destino,'rev-parse','refs/heads/practica/manual')
if (-not $ramaManual) {
    $remoteManual = Get-GitText -Args @('-C',$destino,'rev-parse','--verify','refs/remotes/origin/practica/manual')
    if ($remoteManual) {
        Invoke-Git -Args @('-C',$destino,'branch','--track','practica/manual','origin/practica/manual')
    } else {
        Invoke-Git -Args @('-C',$destino,'branch','practica/manual','main')
    }
}
if ((Get-GitText -Args @('-C',$destino,'status','--porcelain'))) {
    throw 'La preparación terminó con cambios sin confirmar.'
}

if ($Publicar) {
    Write-Host 'Publicando main, etiqueta base-alm y rama practica/manual...'
    $referencias = @('refs/heads/main','refs/tags/base-alm','refs/heads/practica/manual')
    Invoke-Git -Args (@('-C',$destino,'push','--atomic','-u','origin') + $referencias)
    $publicadas = @(Invoke-Git -Args (@('-C',$destino,'ls-remote','--refs','origin') + $referencias))
    foreach ($ref in $referencias) {
        $id = Get-GitText -Args @('-C',$destino,'rev-parse','--verify',$ref)
        if ($publicadas -notcontains "$id`t$ref") { throw "El servidor no confirma la referencia $ref." }
    }
} else {
    Write-Host 'No se ha hecho push. Ejecuta otra vez con -Publicar tras revisar el contenido.'
}
Write-Host "L02 preparada. Proyecto: $destino"
Write-Host "Commit base: $mainSha"
Write-Host 'Siguiente: git switch practica/manual (en la carpeta del proyecto).'
