# Switch JDK - Quickly change JAVA_HOME to a different JDK version
# Usage: .\switch-jdk.ps1 <version>
# Example: .\switch-jdk.ps1 17

param(
    [Parameter(Mandatory=$true, Position=0)]
    [ValidateSet("8", "11", "17", "21")]
    [string]$Version
)

$ErrorActionPreference = "Stop"

$JDK_DIR = "C:\migration-toolkit\jdk"
$TARGET_JDK = "$JDK_DIR\$Version"

# Check if JDK exists
if (-not (Test-Path $TARGET_JDK)) {
    Write-Host "ERROR: JDK $Version not found at $TARGET_JDK" -ForegroundColor Red
    Write-Host "Run install-windows.ps1 first to install JDKs" -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path "$TARGET_JDK\bin\java.exe")) {
    Write-Host "ERROR: JDK $Version installation appears incomplete" -ForegroundColor Red
    Write-Host "Missing: $TARGET_JDK\bin\java.exe" -ForegroundColor Yellow
    exit 1
}

# Set JAVA_HOME (User level - persists across sessions)
Write-Host "Switching to JDK $Version..." -ForegroundColor Cyan
[Environment]::SetEnvironmentVariable("JAVA_HOME", $TARGET_JDK, "User")

# Update current session
$env:JAVA_HOME = $TARGET_JDK

# Verify
Write-Host ""
Write-Host "SUCCESS: JAVA_HOME set to JDK $Version" -ForegroundColor Green
Write-Host "  Path: $TARGET_JDK" -ForegroundColor Gray
Write-Host ""

# Show version
Write-Host "Java version:" -ForegroundColor Cyan
& "$TARGET_JDK\bin\java.exe" -version

Write-Host ""
Write-Host "NOTE: Current session updated. New terminals will use JDK $Version automatically." -ForegroundColor Yellow
Write-Host "      To use in THIS terminal, run: `$env:JAVA_HOME = `"$TARGET_JDK`"" -ForegroundColor Yellow

exit 0
