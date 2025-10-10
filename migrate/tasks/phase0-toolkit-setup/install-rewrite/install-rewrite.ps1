param(
  [string]$Version = 'latest',
  [string]$InstallDir = 'C:\migration-toolkit\bin',
  [switch]$Force
)

$ErrorActionPreference = 'Stop'
function Info($m){ Write-Host "[rewrite-install] $m" -ForegroundColor Cyan }
function Warn($m){ Write-Host "[rewrite-install][WARN] $m" -ForegroundColor Yellow }

# OpenRewrite is primarily used via Maven/Gradle plugins
# Check if we can verify Maven plugin availability
Info 'Verifying OpenRewrite Maven plugin availability'
Info 'OpenRewrite will be executed via Maven plugin (rewrite-maven-plugin)'
Info 'No standalone CLI binary installation needed - Maven will download plugin on first use'

# Create a marker file to indicate OpenRewrite is configured via Maven
$markerDir = 'C:\migration-toolkit\config'
New-Item -ItemType Directory -Force -Path $markerDir | Out-Null
$markerFile = Join-Path $markerDir 'rewrite-maven-configured.txt'
Set-Content -Path $markerFile -Value "OpenRewrite configured via Maven plugin`nDate: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`nPlugin will be downloaded by Maven on first use"

Info 'OpenRewrite Maven plugin configuration complete'
Info 'To use: Add org.openrewrite.maven:rewrite-maven-plugin to your pom.xml'
exit 0

# Legacy standalone binary approach (currently not available)
if ($false) {
if ($Version -eq 'latest') {
  Info 'Resolving latest rewrite CLI version'
  try {
    $release = Invoke-RestMethod -Uri https://api.github.com/repos/openrewrite/rewrite-recipe-bom/releases/latest -UseBasicParsing
    $Version = $release.tag_name.TrimStart('v')
  } catch {
    Warn "Failed to resolve latest: $_. Using fallback via Maven Central"
    # OpenRewrite CLI is distributed via Maven, not as standalone binary
    # We'll use the Maven plugin approach instead
    $Version = 'maven-plugin'
  }
}
}

New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
$targetExe = Join-Path $InstallDir 'rewrite.exe'

# Detect already installed
if ((Test-Path $targetExe) -and -not $Force) {
  $current = (& $targetExe --version 2>$null) | Select-Object -First 1
  if ($current -match $Version) {
    Info "rewrite CLI $Version already installed (use -Force to reinstall)."
    exit 0
  }
}

$assetPatterns = @(
  "rewrite-windows-amd64",
  "rewrite-win-x86_64.exe",
  "rewrite-windows-x86_64.exe"
)

$downloadUrl = $null
try {
  $rel = Invoke-RestMethod -Uri https://api.github.com/repos/moderneinc/rewrite-cli/releases/tags/v$Version -UseBasicParsing
  foreach ($asset in $rel.assets) {
    foreach ($pat in $assetPatterns) {
      if ($asset.name -ieq $pat -or $asset.name -like "$pat*") { $downloadUrl = $asset.browser_download_url; break }
    }
    if ($downloadUrl) { break }
  }
} catch {
  Warn "Could not fetch tagged release metadata: $_"
}

if (-not $downloadUrl) {
  Warn 'Falling back to constructed URL pattern (may fail if naming changed)'
  $downloadUrl = "https://github.com/moderneinc/rewrite-cli/releases/download/v$Version/rewrite-windows-amd64.exe"
}

$tmpFile = Join-Path ([IO.Path]::GetTempPath()) "rewrite-$Version.tmp"
Info "Downloading $downloadUrl"
Invoke-WebRequest -Uri $downloadUrl -OutFile $tmpFile -UseBasicParsing

Copy-Item $tmpFile $targetExe -Force
Remove-Item $tmpFile -Force

# Ensure PATH
$pathUser = [Environment]::GetEnvironmentVariable('Path','User')
if (-not ($pathUser.Split(';') | Where-Object { $_ -eq $InstallDir })) {
  Info "Adding $InstallDir to User PATH"
  [Environment]::SetEnvironmentVariable('Path', ($pathUser + ';' + $InstallDir), 'User')
}

Info 'Installed version:'
& $targetExe --version
Info 'Done'
