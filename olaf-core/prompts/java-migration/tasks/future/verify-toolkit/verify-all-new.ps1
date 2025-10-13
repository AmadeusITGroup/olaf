# Task 0.2: Verify Toolkit (Windows)
# Verifies all migration tools are installed and configured correctly
# Usage: .\verify-all.ps1

$ErrorActionPreference = "Continue"  # Don't stop on first error

Write-Host "=== Task 0.2: Verify Toolkit ===" -ForegroundColor Cyan
Write-Host ""

$allChecksPassed = $true
$JDK_DIR = "C:\migration-toolkit\jdk"

# Function to check if a command exists
function Test-CommandExists {
    param($command)
    $null = Get-Command $command -ErrorAction SilentlyContinue
    return $?
}

# Function to extract version from Java output
function Get-JavaVersion {
    param($output)
    if ($output -match 'version\s+"?(\d+)\.') {
        return $Matches[1]
    } elseif ($output -match 'version\s+"?1\.(\d+)') {
        return $Matches[1]  # For Java 8 format (1.8.x)
    }
    return "unknown"
}

# Check JDK Installations
Write-Host "Checking JDK Installations..." -ForegroundColor Yellow

$jdkVersions = @("11", "17", "21")
foreach ($version in $jdkVersions) {
    $jdkPath = "$JDK_DIR\$version"
    $javaExe = "$jdkPath\bin\java.exe"
    
    if (-not (Test-Path $jdkPath)) {
        Write-Host "  ✗ JDK $version`: Not found at $jdkPath" -ForegroundColor Red
        $allChecksPassed = $false
    } elseif (-not (Test-Path $javaExe)) {
        Write-Host "  ✗ JDK $version`: Directory exists but java.exe missing" -ForegroundColor Red
        $allChecksPassed = $false
    } else {
        try {
            $javaVersion = & $javaExe -version 2>&1 | Select-Object -First 1
            $versionNum = Get-JavaVersion $javaVersion
            Write-Host "  ✓ JDK $version`: $jdkPath (version $versionNum)" -ForegroundColor Green
        } catch {
            Write-Host "  ✗ JDK $version`: Found but java.exe doesn't work" -ForegroundColor Red
            $allChecksPassed = $false
        }
    }
}

# Check Maven
Write-Host ""
Write-Host "Checking Maven..." -ForegroundColor Yellow

if (-not (Test-CommandExists "mvn")) {
    Write-Host "  ✗ Maven: Not found in PATH" -ForegroundColor Red
    $allChecksPassed = $false
} else {
    try {
        $mavenVersion = mvn --version 2>&1 | Select-Object -First 1
        if ($mavenVersion -match 'Apache Maven (\d+\.\d+\.\d+)') {
            $version = $Matches[1]
            $versionParts = $version.Split('.')
            $major = [int]$versionParts[0]
            $minor = [int]$versionParts[1]
            $patch = [int]$versionParts[2]
            
            # Check if version >= 3.9.5
            if (($major -gt 3) -or ($major -eq 3 -and $minor -gt 9) -or ($major -eq 3 -and $minor -eq 9 -and $patch -ge 5)) {
                Write-Host "  ✓ Maven: $version (in PATH)" -ForegroundColor Green
            } else {
                Write-Host "  ✗ Maven: $version is too old (need 3.9.5+)" -ForegroundColor Red
                $allChecksPassed = $false
            }
        } else {
            Write-Host "  ✗ Maven: Found but couldn't parse version" -ForegroundColor Red
            $allChecksPassed = $false
        }
    } catch {
        Write-Host "  ✗ Maven: Found but 'mvn --version' failed" -ForegroundColor Red
        $allChecksPassed = $false
    }
}

# Check Git
Write-Host ""
Write-Host "Checking Git..." -ForegroundColor Yellow

if (-not (Test-CommandExists "git")) {
    Write-Host "  ✗ Git: Not found in PATH" -ForegroundColor Red
    $allChecksPassed = $false
} else {
    try {
        $gitVersion = git --version 2>&1
        if ($gitVersion -match 'git version (.+)') {
            $version = $Matches[1]
            Write-Host "  ✓ Git: $version (in PATH)" -ForegroundColor Green
        } else {
            Write-Host "  ✓ Git: Found in PATH" -ForegroundColor Green
        }
    } catch {
        Write-Host "  ✗ Git: Found but 'git --version' failed" -ForegroundColor Red
        $allChecksPassed = $false
    }
}

# Check Environment Variables
Write-Host ""
Write-Host "Checking Environment Variables..." -ForegroundColor Yellow

$envVars = @{
    "JDK11_HOME" = "$JDK_DIR\11"
    "JDK17_HOME" = "$JDK_DIR\17"
    "JDK21_HOME" = "$JDK_DIR\21"
    "JAVA_HOME"  = "$JDK_DIR\17"
}

foreach ($varName in $envVars.Keys) {
    $expectedValue = $envVars[$varName]
    $actualValue = [Environment]::GetEnvironmentVariable($varName, "User")
    
    if (-not $actualValue) {
        $actualValue = [Environment]::GetEnvironmentVariable($varName, "Machine")
    }
    
    if (-not $actualValue) {
        $actualValue = [Environment]::GetEnvironmentVariable($varName, "Process")
    }
    
    if (-not $actualValue) {
        Write-Host "  ✗ $varName`: Not set" -ForegroundColor Red
        $allChecksPassed = $false
    } elseif ($actualValue -eq $expectedValue) {
        Write-Host "  ✓ $varName = $actualValue" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ $varName = $actualValue (expected: $expectedValue)" -ForegroundColor Yellow
        # Not failing for this, just warning
    }
}

# Summary
Write-Host ""
if ($allChecksPassed) {
    Write-Host "=== All Checks Passed ===" -ForegroundColor Green
    Write-Host "Toolkit is ready for migration!" -ForegroundColor Green
    Write-Host ""
    exit 0
} else {
    Write-Host "=== Some Checks Failed ===" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    Write-Host "  - Missing JDK: Run Task 0.0.1 (Install JDKs) again" -ForegroundColor White
    Write-Host "  - Missing Maven: Install Maven 3.9.5+ from https://maven.apache.org/" -ForegroundColor White
    Write-Host "  - Missing Git: Install Git from https://git-scm.com/" -ForegroundColor White
    Write-Host "  - Environment variables: Restart terminal or run Task 0.0.1 again" -ForegroundColor White
    Write-Host ""
    exit 1
}
