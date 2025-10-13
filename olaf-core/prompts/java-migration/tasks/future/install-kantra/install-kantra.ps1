<#
Install or update Konveyor Kantra CLI (Windows)

Current upstream release artifacts are ZIP files (e.g. kantra.windows.amd64.zip)
containing the executable. The previous implementation attempted to download a
non-existent standalone EXE. This revision:
  * Resolves the desired release (latest or specific tag)
  * Locates the Windows amd64 asset dynamically
  * Downloads + extracts the ZIP to a temp folder
  * Copies the kantra.exe into the target InstallDir
  * Adds InstallDir to the user PATH if missing
Idempotency: Skips install if exact version present unless -Force is supplied.
#>
param(
  [string]$Version = 'latest',
  [string]$InstallDir = 'C:\migration-toolkit\bin',
  [switch]$Force
)
$ErrorActionPreference = 'Stop'
function Info($m){ Write-Host "[INFO] $m" }
function Warn($m){ Write-Warning $m }
function Die($m){ throw $m }
if(-not (Test-Path $InstallDir)){ Info "Creating $InstallDir"; New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null }
$exePath = Join-Path $InstallDir 'kantra.exe'
function Get-InstalledVersion {
  if(Test-Path $exePath){
    try {
      $line = & $exePath version 2>&1 | Select-Object -First 1
      if($line -match '(?:kantra version|version:?)[^v]*(v?\d+\.\d+\.\d+)'){ return $Matches[1] }
    } catch {}
  }
  return $null
}
function Get-Release($tag){
  $headers = @{ 'User-Agent'='kantra-installer' }
  $url = if($tag -eq 'latest'){ 'https://api.github.com/repos/konveyor/kantra/releases/latest' } else { "https://api.github.com/repos/konveyor/kantra/releases/tags/$tag" }
  try { return Invoke-RestMethod -Uri $url -Headers $headers } catch { Die "Failed to fetch release metadata for $tag. $_" }
}
$installed = Get-InstalledVersion
if($installed){ Info "Installed version detected: $installed" }
if($Version -ne 'latest' -and -not $Version.StartsWith('v')){ $Version = 'v' + $Version }
$release = Get-Release $Version
$Version = $release.tag_name
Info "Target version: $Version"
if($installed -and $installed -ieq $Version -and -not $Force){ Info 'Requested version already installed. Use -Force to re-install.'; exit 0 }

# Locate windows amd64 asset (zip)
$asset = $release.assets | Where-Object { $_.name -match 'windows\.amd64\.zip$' } | Select-Object -First 1
if(-not $asset){ Die "Could not find a windows amd64 asset in release $Version" }
Info "Found asset: $($asset.name) size=$([math]::Round($asset.size/1MB,2))MB"
$tmpZip = Join-Path $env:TEMP $asset.name
Info "Downloading $($asset.browser_download_url)"
try { Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $tmpZip -UseBasicParsing } catch { Die "Download failed: $_" }
if(-not (Test-Path $tmpZip) -or ((Get-Item $tmpZip).Length -lt 10MB)){ Warn "Zip seems smaller than expected. Continuing." }
$extractDir = Join-Path $env:TEMP ([System.IO.Path]::GetFileNameWithoutExtension($asset.name) + '-' + [System.Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $extractDir | Out-Null
Info "Extracting to $extractDir"
try { Expand-Archive -LiteralPath $tmpZip -DestinationPath $extractDir -Force } catch { Die "Failed to extract archive: $_" }
# Find kantra executable (allow patterns like kantra.exe or kantra-windows-amd64.exe)
$cand = Get-ChildItem -Path $extractDir -Recurse -File -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -match '^(windows-)?kantra(.*)?\.exe$' -or $_.Name -ieq 'kantra' } |
  Select-Object -First 1
if(-not $cand){ Die "Extracted archive does not contain kantra executable." }
Info "Installing to $exePath"
Copy-Item $cand.FullName $exePath -Force
Remove-Item $tmpZip -Force -ErrorAction SilentlyContinue
Remove-Item $extractDir -Recurse -Force -ErrorAction SilentlyContinue
$userPath = [Environment]::GetEnvironmentVariable('PATH','User')
if(-not $userPath){ $userPath = '' }
if(-not ($userPath -split ';' | Where-Object { $_ -eq $InstallDir })){ Info "Appending $InstallDir to user PATH"; [Environment]::SetEnvironmentVariable('PATH',($InstallDir + ';' + $userPath).Trim(';'),'User') } else { Info 'InstallDir already present on PATH' }
if(-not ($env:PATH -split ';' | Where-Object { $_ -eq $InstallDir })){ $env:PATH = "$InstallDir;" + $env:PATH }
$line = & $exePath version 2>&1 | Select-Object -First 1
Write-Host $line
if($line -match [regex]::Escape($Version)){ Info "SUCCESS: Installed kantra $Version"; exit 0 } else { Warn "Version output did not match expected $Version"; exit 1 }
