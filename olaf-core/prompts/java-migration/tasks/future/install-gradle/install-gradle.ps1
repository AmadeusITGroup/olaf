param(
    [string]$Version = "8.10.1",
    [string]$InstallDir = "C:\migration-toolkit\gradle",
    [string]$SymlinkBinDir = "C:\migration-toolkit\bin",
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

function Write-Info($msg){ Write-Host "[gradle-install] $msg" -ForegroundColor Cyan }
function Write-Warn($msg){ Write-Host "[gradle-install] $msg" -ForegroundColor Yellow }
function Write-Err($msg){ Write-Host "[gradle-install] $msg" -ForegroundColor Red }

# Resolve latest if requested (simple JSON feed)
if ($Version -eq 'latest') {
    try {
        Write-Info "Resolving latest version"
        $all = Invoke-RestMethod -Uri https://services.gradle.org/versions/all -UseBasicParsing
        $stable = $all | Where-Object { -not $_.snapshot -and $_.nightly -eq $false } | Select-Object -First 1
        if ($stable.version) { $Version = $stable.version } else { throw 'No stable version found' }
    } catch {
        Write-Warn "Failed to resolve latest automatically: $_. Falling back to default 8.10.1"
        $Version = '8.10.1'
    }
}

$distName = "gradle-$Version"
$zipName = "$distName-bin.zip"
$baseUrl = "https://services.gradle.org/distributions"
$downloadUrl = "$baseUrl/$zipName"
$targetDir = Join-Path $InstallDir $distName

if (Test-Path $targetDir -PathType Container -and -not $Force) {
    Write-Info "Gradle $Version already installed at $targetDir (use -Force to reinstall)."
} else {
    if (Test-Path $targetDir -PathType Container -and $Force) {
        Write-Info "Force specified: removing existing directory $targetDir"
        Remove-Item $targetDir -Recurse -Force
    }
    New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
    $tmpZip = Join-Path ([IO.Path]::GetTempPath()) $zipName
    Write-Info "Downloading $downloadUrl"
    Invoke-WebRequest -Uri $downloadUrl -OutFile $tmpZip -UseBasicParsing

    Write-Info "Extracting to $InstallDir"
    Expand-Archive -Path $tmpZip -DestinationPath $InstallDir -Force
    Remove-Item $tmpZip -Force
}

# Create shim / ensure PATH
New-Item -ItemType Directory -Force -Path $SymlinkBinDir | Out-Null
$shimBat = Join-Path $SymlinkBinDir 'gradle.bat'
$gradleBat = Join-Path $targetDir 'bin/gradle.bat'
$shimContent = "@echo off`r`ncall `"$gradleBat`" %*"
Set-Content -Path $shimBat -Encoding ascii -Value $shimContent

# Update PATH (User scope) if missing
$path = [Environment]::GetEnvironmentVariable('Path','User')
if (-not ($path.Split(';') | Where-Object { $_ -eq $SymlinkBinDir })) {
    Write-Info "Adding $SymlinkBinDir to User PATH"
    [Environment]::SetEnvironmentVariable('Path', ($path + ';' + $SymlinkBinDir), 'User')
} else {
    Write-Info "SymlinkBinDir already on PATH"
}

# Validation
$env:PATH = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')
Write-Info "Installed gradle version:"
& $shimBat --version | Select-Object -First 5

Write-Info "Done"
