param (
    [Parameter(Mandatory=$true)]
    [string]$ProjectPath
)

$ToolkitRoot = Split-Path -Parent $PSScriptRoot
$AiDir = Join-Path $ProjectPath ".ai"
$ToolkitLink = Join-Path $AiDir "toolkit"

if (!(Test-Path $ProjectPath)) {
    Write-Host "Project path does not exist: $ProjectPath"
    exit 1
}

if (!(Test-Path $AiDir)) {
    New-Item -ItemType Directory -Path $AiDir -Force | Out-Null
}

if (Test-Path $ToolkitLink) {
    Write-Host "Existing toolkit link found: $ToolkitLink"
    Write-Host "Remove it manually if you want to recreate the link."
    exit 0
}

New-Item -ItemType Junction -Path $ToolkitLink -Target $ToolkitRoot | Out-Null

Write-Host "Linked toolkit to project:"
Write-Host $ToolkitLink
