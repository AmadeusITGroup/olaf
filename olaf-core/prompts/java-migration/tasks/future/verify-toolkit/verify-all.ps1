# Task 0.2: Verify Toolkit (Windows)
# Verifies all migration tools are installed and configured correctly
# Usage: .\verify-all.ps1

$ErrorActionPreference = "Continue"  # Don't stop on first error

Write-Host "=== Task 0.2: Verify Toolkit ==="
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
    if ($output -match 'version\s+"?(\d+)\.') { return $Matches[1] }
    elseif ($output -match 'version\s+"?1\.(\d+)') { return $Matches[1] }
    else { return "unknown" }
}

# Check JDK Installations
Write-Host "Checking JDK Installations..."

$jdkVersions = @('11','17','21')
foreach ($version in $jdkVersions) {
    $jdkPath = Join-Path $JDK_DIR $version
    $javaExe = Join-Path $jdkPath 'bin/java.exe'

    if (-not (Test-Path $jdkPath)) {
        Write-Host "  FAIL JDK $version missing at $jdkPath"
        $allChecksPassed = $false
        continue
    }
    if (-not (Test-Path $javaExe)) {
        Write-Host "  FAIL JDK $version java.exe missing"
        $allChecksPassed = $false
        continue
    }
    try {
        $javaVersionLine = & $javaExe -version 2>&1 | Select-Object -First 1
        $versionNum = Get-JavaVersion $javaVersionLine
        Write-Host "  OK   JDK $version present (reported major $versionNum)"
    } catch {
        Write-Host "  FAIL JDK $version java.exe execution failed: $($_.Exception.Message)"
        $allChecksPassed = $false
    }
}

# Check Maven
Write-Host ""
Write-Host "Checking Maven..."
if (-not (Test-CommandExists 'mvn')) {
    Write-Host '  FAIL Maven not in PATH'
    $allChecksPassed = $false
} else {
    try {
        $mvnLine = mvn --version 2>&1 | Select-Object -First 1
        if ($mvnLine -match 'Apache Maven (\d+)\.(\d+)\.(\d+)') {
            $maj = [int]$Matches[1]; $min = [int]$Matches[2]; $pat = [int]$Matches[3]
            if (($maj -gt 3) -or ($maj -eq 3 -and $min -gt 9) -or ($maj -eq 3 -and $min -eq 9 -and $pat -ge 5)) {
                Write-Host "  OK   Maven $maj.$min.$pat"
            } else {
                Write-Host "  FAIL Maven $maj.$min.$pat < 3.9.5"
                $allChecksPassed = $false
            }
        } else {
            Write-Host '  FAIL Maven version parse'
            $allChecksPassed = $false
        }
    } catch {
        Write-Host "  FAIL mvn --version error: $($_.Exception.Message)"
        $allChecksPassed = $false
    }
}

# Check Git
Write-Host ""
Write-Host "Checking Git..."
if (-not (Test-CommandExists 'git')) {
    Write-Host '  FAIL Git not in PATH'
    $allChecksPassed = $false
} else {
    try {
        $gitLine = git --version 2>&1
        if ($gitLine -match 'git version (.+)') { Write-Host "  OK   Git $($Matches[1])" } else { Write-Host '  OK   Git present' }
    } catch {
        Write-Host "  FAIL git --version error: $($_.Exception.Message)"
        $allChecksPassed = $false
    }
}

# Check Environment Variables
Write-Host ""
Write-Host "Checking Environment Variables..."
$envVars = @{
  'JDK11_HOME' = Join-Path $JDK_DIR '11'
  'JDK17_HOME' = Join-Path $JDK_DIR '17'
  'JDK21_HOME' = Join-Path $JDK_DIR '21'
  'JAVA_HOME'  = Join-Path $JDK_DIR '17'
}
foreach ($k in $envVars.Keys) {
  $expected = $envVars[$k]
  $val = [Environment]::GetEnvironmentVariable($k,'User')
  if (-not $val) { $val = [Environment]::GetEnvironmentVariable($k,'Machine') }
  if (-not $val) { $val = [Environment]::GetEnvironmentVariable($k,'Process') }
  if (-not $val) {
    Write-Host "  FAIL $k not set"
    $allChecksPassed = $false
  } elseif ($val -eq $expected) {
    Write-Host "  OK   $k=$val"
  } else {
    Write-Host "  WARN $k=$val (expected $expected)"
  }
}

# Summary
Write-Host ""
if ($allChecksPassed) {
  Write-Host '=== SUCCESS: Toolkit verified ==='
  exit 0
} else {
  Write-Host '=== FAILURE: Some checks failed ==='
  exit 1
}

