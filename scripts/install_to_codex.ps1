# Install all toolkit skills to the Codex global skills directory.

$ToolkitRoot = Split-Path -Parent $PSScriptRoot
$SkillsRoot = Join-Path $ToolkitRoot "skills"
$CodexSkills = Join-Path $env:USERPROFILE ".codex\skills"

if (!(Test-Path $SkillsRoot)) {
    Write-Host "Skills root does not exist: $SkillsRoot"
    exit 1
}

if (!(Test-Path $CodexSkills)) {
    New-Item -ItemType Directory -Path $CodexSkills -Force | Out-Null
}

$installed = @()
$skipped = @()

Get-ChildItem -Path $SkillsRoot -Directory | ForEach-Object {
    $skillName = $_.Name
    $skillSource = $_.FullName
    $skillTarget = Join-Path $CodexSkills $skillName

    if (Test-Path $skillTarget) {
        $skipped += $skillName
        return
    }

    New-Item -ItemType Junction -Path $skillTarget -Target $skillSource | Out-Null
    $installed += $skillName
}

Write-Host "Codex skill install complete."

if ($installed.Count -gt 0) {
    Write-Host "Installed:"
    $installed | ForEach-Object { Write-Host "  - $_" }
}

if ($skipped.Count -gt 0) {
    Write-Host "Skipped existing targets:"
    $skipped | ForEach-Object { Write-Host "  - $_" }
}
