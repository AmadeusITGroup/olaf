param(
  [string]$Version = 'distro',
  [string]$InstallDir = 'C:\migration-toolkit\bin',
  [switch]$Create_Docker_Shim,
  [switch]$Force
)
$ErrorActionPreference = 'Stop'
function Info($m){ Write-Host "[podman-install] $m" -ForegroundColor Cyan }
function Warn($m){ Write-Host "[podman-install][WARN] $m" -ForegroundColor Yellow }

# Check if podman already installed
if (Get-Command podman -ErrorAction SilentlyContinue) {
  $existingVersion = (podman --version) 2>$null
  Info "Podman already present: $existingVersion"
  if ($Version -ne 'distro' -and $Version -ne 'latest' -and ($existingVersion -notmatch $Version)) {
    Warn "Requested version $Version differs; upgrade/downgrade not automated yet."
  }
} else {
  if ($Version -eq 'distro') {
    if (Get-Command winget -ErrorAction SilentlyContinue) {
      Info 'Installing Podman via winget'
      $winget = Start-Process winget -ArgumentList 'install','-e','--id','RedHat.Podman','-h' -Wait -PassThru
      if ($winget.ExitCode -ne 0) { throw "winget install failed with code $($winget.ExitCode)" }
    } else {
      Warn 'winget not available. Please install Podman manually or add custom installer logic.'
    }
  } else {
    Warn 'Specific version install not implemented; attempting winget latest.'
    if (Get-Command winget -ErrorAction SilentlyContinue) {
      $winget = Start-Process winget -ArgumentList 'install','-e','--id','RedHat.Podman','-h' -Wait -PassThru
      if ($winget.ExitCode -ne 0) { throw "winget install failed with code $($winget.ExitCode)" }
    } else { throw 'Cannot install Podman automatically without winget.' }
  }
}

# Verify
Get-Command podman -ErrorAction Stop | Out-Null
Info (podman --version)

# Docker shim
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
if ($Create_Docker_Shim.IsPresent) {
  $ps1 = Join-Path $InstallDir 'docker.ps1'
  $cmd = Join-Path $InstallDir 'docker.cmd'
  if (-not (Test-Path $ps1) -or $Force) {
    Info 'Creating docker.ps1 shim'
    @("param([Parameter(ValueFromRemainingArguments=$true)][string[]]$Args)",
      "if (-not (Get-Command podman -ErrorAction SilentlyContinue)) { Write-Error 'podman not found'; exit 1 }",
      "& podman @Args") | Set-Content -Path $ps1 -Encoding UTF8
  }
  if (-not (Test-Path $cmd) -or $Force) {
    Info 'Creating docker.cmd shim'
    $cmdContent = "@echo off`r`npowershell -ExecutionPolicy Bypass -File `"%~dp0docker.ps1`" %*"
    Set-Content -Path $cmd -Encoding ASCII -Value $cmdContent
  }
}

# Smoke test
try {
  Info 'Running smoke test podman run --rm quay.io/podman/hello'
  podman run --rm quay.io/podman/hello | Select-Object -First 5
} catch { Warn "Smoke test failed: $_" }

Info 'Done.'
