# Task 0.0.1: Install JDKs (Windows)
# Installs JDK 11, 17, 21 to C:\migration-toolkit\jdk\
# Usage: .\install-windows.ps1 [-Force]

param(
    [switch]$Force
)

$ErrorActionPreference = "Stop"

Write-Host "=== Task 0.0.1: Install JDKs ===" -ForegroundColor Cyan
if ($Force) {
    Write-Host "Force reinstall enabled" -ForegroundColor Yellow
}

$TOOLKIT_DIR = "C:\migration-toolkit"
$JDK_DIR = "$TOOLKIT_DIR\jdk"

# JDK download URLs (Eclipse Temurin - using latest stable versions)
# Note: JDK 8 is excluded as it's EOL and most migrations start from JDK 11+
$JDK_URLS = @{
    "11" = "https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.25%2B9/OpenJDK11U-jdk_x64_windows_hotspot_11.0.25_9.zip"
    "17" = "https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.13%2B11/OpenJDK17U-jdk_x64_windows_hotspot_17.0.13_11.zip"
    "21" = "https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.5%2B11/OpenJDK21U-jdk_x64_windows_hotspot_21.0.5_11.zip"
}

# Create directories
Write-Host "Creating directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path $JDK_DIR | Out-Null

# Install each JDK
foreach ($version in $JDK_URLS.Keys) {
    Write-Host ""
    Write-Host "Installing JDK $version..." -ForegroundColor Yellow
    
    $url = $JDK_URLS[$version]
    $zipFile = "$env:TEMP\jdk-$version.zip"
    $extractDir = "$JDK_DIR\$version"
    
    # Check if already installed
    if ((Test-Path $extractDir) -and (Test-Path "$extractDir\bin\java.exe") -and (-not $Force)) {
        Write-Host "  SKIP: JDK $version already installed (use -Force to reinstall)" -ForegroundColor Cyan
        continue
    }
    
    # Remove existing if force reinstall
    if ($Force -and (Test-Path $extractDir)) {
        Write-Host "  Removing existing installation..." -ForegroundColor Yellow
        Remove-Item -Path $extractDir -Recurse -Force
    }
    
    # Download
    Write-Host "  Downloading..." -ForegroundColor Gray
    try {
        Invoke-WebRequest -Uri $url -OutFile $zipFile -UseBasicParsing
    } catch {
        Write-Host "  ERROR: Failed to download JDK $version" -ForegroundColor Red
        Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
        exit 1
    }
    
    # Extract
    Write-Host "  Extracting to $extractDir" -ForegroundColor Gray
    New-Item -ItemType Directory -Force -Path $extractDir | Out-Null
    
    try {
        Expand-Archive -Path $zipFile -DestinationPath "$env:TEMP\jdk-$version-temp" -Force
        
        # Find the actual JDK directory (it's nested)
        $jdkFolder = Get-ChildItem -Path "$env:TEMP\jdk-$version-temp" -Directory | Select-Object -First 1
        
        # Move contents
        Move-Item -Path "$($jdkFolder.FullName)\*" -Destination $extractDir -Force
        
        # Cleanup
        Remove-Item -Path "$env:TEMP\jdk-$version-temp" -Recurse -Force
        Remove-Item -Path $zipFile -Force
        
    } catch {
        Write-Host "  ERROR: Failed to extract JDK $version" -ForegroundColor Red
        Write-Host "  $($_.Exception.Message)" -ForegroundColor Red
        exit 1
    }
    
    Write-Host "  SUCCESS: JDK $version installed" -ForegroundColor Green
}

# Set environment variables (User level)
Write-Host ""
Write-Host "Setting environment variables..." -ForegroundColor Yellow

[Environment]::SetEnvironmentVariable("JDK11_HOME", "$JDK_DIR\11", "User")
[Environment]::SetEnvironmentVariable("JDK17_HOME", "$JDK_DIR\17", "User")
[Environment]::SetEnvironmentVariable("JDK21_HOME", "$JDK_DIR\21", "User")
[Environment]::SetEnvironmentVariable("JAVA_HOME", "$JDK_DIR\17", "User")

# Update current session
$env:JDK11_HOME = "$JDK_DIR\11"
$env:JDK17_HOME = "$JDK_DIR\17"
$env:JDK21_HOME = "$JDK_DIR\21"
$env:JAVA_HOME = "$JDK_DIR\17"

Write-Host "  JDK11_HOME = $JDK_DIR\11" -ForegroundColor Green
Write-Host "  JDK17_HOME = $JDK_DIR\17" -ForegroundColor Green
Write-Host "  JDK21_HOME = $JDK_DIR\21" -ForegroundColor Green
Write-Host "  JAVA_HOME  = $JDK_DIR\17 (default)" -ForegroundColor Green

Write-Host ""
Write-Host "=== Installation Complete ===" -ForegroundColor Green
Write-Host "JDKs installed to: $JDK_DIR" -ForegroundColor Cyan
Write-Host "Run verify.py to confirm" -ForegroundColor Cyan

exit 0
