param(
  [switch]$Pull,
  [switch]$Check,
  [switch]$DryRun,
  [string]$Dest = "$HOME\.codex\skills"
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..")
$SkillsDir = Join-Path $RepoRoot "skills"

function Assert-SkillTree {
  if (-not (Test-Path $SkillsDir)) {
    throw "skills directory not found: $SkillsDir"
  }

  $skillDirs = Get-ChildItem -LiteralPath $SkillsDir -Directory | Where-Object { $_.Name -like "ieee-*" }
  if ($skillDirs.Count -eq 0) {
    throw "no ieee-* skill directories found under $SkillsDir"
  }

  foreach ($dir in $skillDirs) {
    $skillMd = Join-Path $dir.FullName "SKILL.md"
    if (-not (Test-Path $skillMd)) {
      throw "missing SKILL.md in $($dir.FullName)"
    }
  }

  $shared = Join-Path $SkillsDir "_shared"
  if (-not (Test-Path $shared)) {
    throw "missing shared directory: $shared"
  }

  Write-Host "Skill tree check passed."
}

if ($Pull) {
  $git = Get-Command git -ErrorAction SilentlyContinue
  if (-not $git) {
    throw "git is not available. Install git or run without -Pull."
  }
  Push-Location $RepoRoot
  try {
    git pull
  } finally {
    Pop-Location
  }
}

Assert-SkillTree

if ($Check) {
  exit 0
}

if ([System.IO.Path]::IsPathRooted($Dest)) {
  $destFull = [System.IO.Path]::GetFullPath($Dest)
} else {
  $destFull = [System.IO.Path]::GetFullPath((Join-Path (Get-Location).Path $Dest))
}
New-Item -ItemType Directory -Force -Path $destFull | Out-Null

$sourceRoot = (Resolve-Path $SkillsDir).Path
$destRoot = (Resolve-Path $destFull).Path

Write-Host "Installing skills from $sourceRoot"
Write-Host "Installing skills to   $destRoot"

$items = Get-ChildItem -LiteralPath $SkillsDir -Directory | Where-Object {
  $_.Name -eq "_shared" -or $_.Name -like "ieee-*"
}

foreach ($item in $items) {
  $target = Join-Path $destRoot $item.Name
  if ($DryRun) {
    Write-Host "[dry-run] copy $($item.FullName) -> $target"
    continue
  }

  if (Test-Path $target) {
    Remove-Item -LiteralPath $target -Recurse -Force
  }
  Copy-Item -LiteralPath $item.FullName -Destination $target -Recurse
  Write-Host "Installed $($item.Name)"
}

Write-Host "Done. Restart Codex or start a new turn for updated skills to be discovered."
