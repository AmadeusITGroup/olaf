param(
  [switch]$Json
)
$ErrorActionPreference = "Continue"

$Result = [ordered]@{
  timestamp = (Get-Date).ToString('o')
  host_os = (Get-CimInstance Win32_OperatingSystem).Caption
  mandatory = @{}
  recommended = @{}
  summary = @{}
}

function Test-Cmd {
  param([string]$name)
  # Returns $true if command exists, otherwise $false
  return [bool](Get-Command -Name $name -ErrorAction SilentlyContinue)
}
function Add-Res($cat,$tool,$status,$details){ $Result[$cat][$tool] = [ordered]@{ status=$status; details=$details } }

Write-Host '=== Extended Toolkit Verification (Task 0.3) ==='

# --- Mandatory Tools ---
# Git
if(Test-Cmd git){ Add-Res 'mandatory' 'git' 'ok' (git --version 2>&1) } else { Add-Res 'mandatory' 'git' 'missing' 'git not found'}

# Java versions (expect 11,17,21 directories)
$javaOk=$true
$jdkBase='C:\migration-toolkit\jdk'
$expected=@('11','17','21')
$present=@()
foreach($v in $expected){ if(Test-Path (Join-Path $jdkBase $v)){ $present+=$v } }
if($present.Count -lt 2){ $javaOk=$false }
$defaultJavaLine = (& java -version 2>&1 | Select-Object -First 1) 2>$null
# If default java is <11, downgrade status to warn even if multiple versions installed
$defaultIsLegacy = $false
if($defaultJavaLine -match 'version "1\.(\d+)\.'){ # legacy style 1.8 etc
  $legacyMinor = [int]$Matches[1]
  if($legacyMinor -lt 11){ $defaultIsLegacy = $true }
} elseif($defaultJavaLine -match 'version "(\d+)\.'){ # modern style 11,17,21
  $majVer = [int]$Matches[1]
  if($majVer -lt 11){ $defaultIsLegacy = $true }
}
if($defaultIsLegacy){ $javaOk = $false }
$javaStatus = if($javaOk){ 'ok' } else { 'warn' }
Add-Res 'mandatory' 'java' $javaStatus ("present=" + ($present -join ',') + "; defaultLine=$defaultJavaLine" + ($(if($defaultIsLegacy){ '; advisory=set default to >=11' } else { '' })))

# Maven
if(Test-Cmd mvn){
  $line = mvn --version 2>&1 | Select-Object -First 1
  if($line -match 'Apache Maven (\d+)\.(\d+)\.(\d+)'){
    $maj=[int]$Matches[1];$min=[int]$Matches[2];$pat=[int]$Matches[3]
    if(($maj -gt 3) -or ($maj -eq 3 -and $min -gt 9) -or ($maj -eq 3 -and $min -eq 9 -and $pat -ge 5)){
      Add-Res 'mandatory' 'maven' 'ok' $line
    } else { Add-Res 'mandatory' 'maven' 'fail' "$line (<3.9.5)" }
  } else { Add-Res 'mandatory' 'maven' 'fail' 'cannot parse version'}
} else { Add-Res 'mandatory' 'maven' 'missing' 'mvn not found'}

# Python3
if(Test-Cmd python){ $py = python --version 2>&1; Add-Res 'mandatory' 'python' 'ok' $py } elseif(Test-Cmd python3){ $py = python3 --version 2>&1; Add-Res 'mandatory' 'python' 'ok' $py } else { Add-Res 'mandatory' 'python' 'missing' 'python not found'}

# curl
if(Test-Cmd curl){ Add-Res 'mandatory' 'curl' 'ok' (curl --version 2>&1 | Select-Object -First 1) } else { Add-Res 'mandatory' 'curl' 'missing' 'curl not found'}

# Container runtime (prefer podman rootless; docker shim acceptable)
$containerTool=$null
foreach($c in 'podman','docker'){ if(Test-Cmd $c){ $containerTool=$c; break } }
if($containerTool){
  $verLine = (& $containerTool --version 2>&1 | Select-Object -First 1)
  $details = $verLine
  if($containerTool -eq 'podman'){
    # Rootless check
    try {
      $rootlessRaw = podman info --format "{{.Host.Security.Rootless}}" 2>$null
      if($rootlessRaw){ $details += "; rootless=$rootlessRaw" }
      if($rootlessRaw -ne 'true'){ $status='warn' } else { $status='ok' }
    } catch { $status='warn'; $details += '; rootless=?' }
  } else {
    # docker present but prefer podman
    $status='warn'; $details += '; advisory=prefer podman rootless'
  }
  Add-Res 'mandatory' 'container' ($status) $details
  # Docker shim detection (docker command actually invoking podman)
  if(Test-Cmd docker){
    try {
      $shimLine = (Get-Command docker).Source
      if($shimLine -match 'docker.ps1' -or $shimLine -match 'docker.cmd'){
        Add-Res 'mandatory' 'docker_shim' 'ok' $shimLine
      } elseif($containerTool -eq 'podman') {
        Add-Res 'mandatory' 'docker_shim' 'warn' 'docker real binary present; ensure policy allows'
      } else {
        Add-Res 'mandatory' 'docker_shim' 'info' 'docker in use (no shim)'
      }
    } catch { Add-Res 'mandatory' 'docker_shim' 'warn' 'cannot inspect docker command' }
  } else {
    Add-Res 'mandatory' 'docker_shim' 'ok' 'no docker binary (podman only)'
  }
} else { Add-Res 'mandatory' 'container' 'missing' 'podman (preferred) or docker not found'}

# kantra (Konveyor CLI)
# Fallback: look in default install dir if not yet on PATH in current session
$kantraInstallDir = 'C:\migration-toolkit\bin'
if(-not (Test-Cmd kantra) -and (Test-Path (Join-Path $kantraInstallDir 'kantra.exe'))){
  # Temporarily prepend for this process so Test-Cmd (future runs) & child commands work
  if(-not ($env:PATH -split ';' | Where-Object { $_ -eq $kantraInstallDir })){ $env:PATH = ($kantraInstallDir + ';' + $env:PATH) }
}
if(Test-Cmd kantra){
  $kantraVerLine = (kantra version 2>&1 | Select-Object -First 1)
  Add-Res 'mandatory' 'kantra' 'ok' $kantraVerLine
} else {
  Add-Res 'mandatory' 'kantra' 'missing' 'kantra CLI not installed'
}

# --- Recommended Tools ---
$recTools = @(
  @{ name='gradle'; test='gradle'; versionCmd='gradle -v'; regex='Gradle (.+)'; },
  @{ name='jq'; test='jq'; versionCmd='jq --version'; regex='jq-(.+)'; },
  @{ name='yq'; test='yq'; versionCmd='yq --version'; regex='yq (.+)'; },
  @{ name='node'; test='node'; versionCmd='node --version'; regex='v(.+)'; },

  # kubectl & helm intentionally deferred (deployment validation phase)
)
foreach($t in $recTools){
  if(Test-Cmd $t.test){
    try {
      $line = Invoke-Expression $t.versionCmd 2>&1 | Select-Object -First 1
      if($line -match $t.regex){ Add-Res 'recommended' $t.name 'ok' $line } else { Add-Res 'recommended' $t.name 'warn' ($line) }
    } catch { Add-Res 'recommended' $t.name 'warn' 'error running version command' }
  } else { Add-Res 'recommended' $t.name 'missing' 'not found' }
}

# Summaries
$mandatoryMissing = ($Result.mandatory.GetEnumerator() | Where-Object { $_.Value.status -in 'missing','fail' } | Select-Object -ExpandProperty Name)
$Result.summary.mandatory_failed = $mandatoryMissing
$Result.summary.mandatory_ok = ($Result.mandatory.Keys | Where-Object { $Result.mandatory[$_].status -eq 'ok' })
$Result.summary.ok = ($mandatoryMissing.Count -eq 0)

if($Json){
  $Result | ConvertTo-Json -Depth 6
  exit ([int](! $Result.summary.ok))
}

Write-Host "" # blank line
Write-Host "Mandatory:"
$Result.mandatory.GetEnumerator() | ForEach-Object { Write-Host ("  {0,-12} {1,-7} {2}" -f $_.Key, $_.Value.status, $_.Value.details) }
Write-Host "" # blank line
Write-Host "Recommended:"
$Result.recommended.GetEnumerator() | ForEach-Object { Write-Host ("  {0,-12} {1,-7} {2}" -f $_.Key, $_.Value.status, $_.Value.details) }

if($Result.summary.ok){ Write-Host ""; Write-Host "ALL MANDATORY TOOLS OK"; exit 0 } else { Write-Host ""; Write-Host "MISSING / FAIL: $($mandatoryMissing -join ', ')"; exit 1 }
