# Install scientific-figure-making skill to Codex global skills directory

$ToolkitRoot = Split-Path -Parent $PSScriptRoot
$SkillSource = Join-Path $ToolkitRoot "skills\scientific-figure-making"
$CodexSkills = Join-Path $env:USERPROFILE ".codex\skills"
$SkillTarget = Join-Path $CodexSkills "scientific-figure-making"

if (!(Test-Path $SkillSource)) {
    Write-Host "Skill source does not exist: $SkillSource"
    exit 1
}

if (!(Test-Path $CodexSkills)) {
    New-Item -ItemType Directory -Path $CodexSkills -Force | Out-Null
}

if (Test-Path $SkillTarget) {
    Write-Host "Existing skill target found: $SkillTarget"
    Write-Host "Remove it manually if you want to recreate the link."
    exit 0
}

New-Item -ItemType Junction -Path $SkillTarget -Target $SkillSource | Out-Null

Write-Host "Installed scientific-figure-making skill to Codex:"
Write-Host $SkillTarget
