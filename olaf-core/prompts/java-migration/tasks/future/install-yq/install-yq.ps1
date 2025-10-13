param(
  [string]$Version='latest',
  [string]$InstallDir='C:\migration-toolkit\bin',
  [switch]$Force
)
$ErrorActionPreference='Stop'
function Info($m){Write-Host "[INFO] $m"}
function Warn($m){Write-Warning $m}
function Die($m){throw $m}
if(-not (Test-Path $InstallDir)){ Info "Creating $InstallDir"; New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null }
$exe = Join-Path $InstallDir 'yq.exe'

function Get-InstalledVersion {
  if(Test-Path $exe){
    try { (& $exe --version 2>&1 | Select-Object -First 1) } catch { return $null }
  } else { return $null }
}
if($Version -ne 'latest' -and -not $Version.StartsWith('v')){ $Version = 'v' + $Version }
$installed = Get-InstalledVersion
if($installed){ Info "Installed: $installed" }
$apiBase='https://api.github.com/repos/mikefarah/yq/releases'
$rel = if($Version -eq 'latest'){ Invoke-RestMethod -Uri "$apiBase/latest" -Headers @{ 'User-Agent'='yq-installer' } } else { Invoke-RestMethod -Uri "$apiBase/tags/$Version" -Headers @{ 'User-Agent'='yq-installer' } }
$targetTag = $rel.tag_name
if($installed -and $installed -match $targetTag -and -not $Force){ Info 'Requested version already installed.'; exit 0 }
$asset = $rel.assets | Where-Object { $_.name -match 'yq_windows_amd64.exe$' } | Select-Object -First 1
if(-not $asset){ Die "Could not find yq_windows_amd64.exe in $targetTag" }
$tmp = Join-Path $env:TEMP $asset.name
Info "Downloading $($asset.browser_download_url)"
Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $tmp -UseBasicParsing
Copy-Item $tmp $exe -Force
Remove-Item $tmp -Force
$userPath = [Environment]::GetEnvironmentVariable('PATH','User'); if(-not $userPath){$userPath=''}
if(-not (($userPath -split ';') -contains $InstallDir)){ [Environment]::SetEnvironmentVariable('PATH', ($InstallDir + ';' + $userPath).Trim(';'), 'User'); Info "Added $InstallDir to user PATH" }
if(-not (($env:PATH -split ';') -contains $InstallDir)){ $env:PATH = "$InstallDir;" + $env:PATH }
$line = & $exe --version 2>&1 | Select-Object -First 1
Write-Host $line
if($line -match $targetTag){ Info "SUCCESS: Installed $line"; exit 0 } else { Warn "Version mismatch expected $targetTag"; exit 1 }
