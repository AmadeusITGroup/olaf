# Angular Migration CI Pipeline Scanner (PowerShell)
# Scans repository for CI/CD configurations and Node.js/Angular settings

param(
    [string]$OutputDir = "olaf-data/findings/migrations"
)

$ErrorActionPreference = "Stop"

$Timestamp = Get-Date -Format "yyyyMMdd-HHmm"
$FindingsDir = Join-Path $OutputDir "migration_$Timestamp/ci"
$ReportFile = Join-Path $FindingsDir "ci_inventory.md"
$JsonFile = Join-Path $FindingsDir "ci_inventory.json"

# Create findings directory
New-Item -ItemType Directory -Path $FindingsDir -Force | Out-Null

Write-Host "=== Angular Migration CI Pipeline Inventory ===" -ForegroundColor Green
Write-Host "Timestamp: $Timestamp"
Write-Host "Findings Directory: $FindingsDir"

# Initialize report
$ReportHeader = @"
# CI Pipeline Inventory - Angular Migration

**Generated:** $(Get-Date)
**Repository:** $(Get-Location)
**Scan Type:** Automated (PowerShell)

## CI Configuration Files Found

"@

Set-Content -Path $ReportFile -Value $ReportHeader

# Initialize JSON report
$JsonData = @{
    timestamp = $Timestamp
    repository = (Get-Location).Path
    ci_files = @()
    node_configs = @()
    angular_configs = @()
    issues = @()
} | ConvertTo-Json -Depth 3

Set-Content -Path $JsonFile -Value $JsonData

# Find CI configuration files
Write-Host "Scanning for CI configuration files..."
$CiFiles = Get-ChildItem -Recurse -Include "*.yml", "*.yaml", "Jenkinsfile" | 
    Where-Object { $_.FullName -match "(\.github|\.gitlab|jenkins|ci)" } |
    Select-Object -First 20

if ($CiFiles) {
    Add-Content -Path $ReportFile -Value "### Found CI Files`n"
    
    foreach ($file in $CiFiles) {
        $relativePath = Resolve-Path -Relative $file.FullName
        Add-Content -Path $ReportFile -Value "- ``$relativePath``"
        
        # Update JSON
        $json = Get-Content $JsonFile | ConvertFrom-Json
        $json.ci_files += $relativePath
        $json | ConvertTo-Json -Depth 3 | Set-Content $JsonFile
        
        Write-Host "  Analyzing: $relativePath"
        
        # Check for Node.js configurations
        $nodeContent = Select-String -Path $file.FullName -Pattern "node|NODE" -Quiet
        if ($nodeContent) {
            Add-Content -Path $ReportFile -Value "  - Contains Node.js configuration"
            
            # Extract Node.js versions
            $nodeVersions = Select-String -Path $file.FullName -Pattern "node.*version|NODE_VERSION" | 
                Select-Object -First 5 -ExpandProperty Line
            
            if ($nodeVersions) {
                Add-Content -Path $ReportFile -Value "  - Node.js versions found:"
                foreach ($version in $nodeVersions) {
                    Add-Content -Path $ReportFile -Value "    $version"
                }
            }
        }
        
        # Check for Angular configurations
        $angularContent = Select-String -Path $file.FullName -Pattern "angular|@angular|ng " -Quiet
        if ($angularContent) {
            Add-Content -Path $ReportFile -Value "  - Contains Angular configuration"
            
            # Extract Angular CLI usage
            $angularUsage = Select-String -Path $file.FullName -Pattern "ng |@angular|angular" | 
                Select-Object -First 5 -ExpandProperty Line
            
            if ($angularUsage) {
                Add-Content -Path $ReportFile -Value "  - Angular usage found:"
                foreach ($usage in $angularUsage) {
                    Add-Content -Path $ReportFile -Value "    $usage"
                }
            }
        }
        
        Add-Content -Path $ReportFile -Value ""
    }
} else {
    Add-Content -Path $ReportFile -Value "### No CI Files Found`n"
    Add-Content -Path $ReportFile -Value "No CI configuration files detected in standard locations."
}

# Issue Detection
Add-Content -Path $ReportFile -Value "`n## Issue Detection`n"

# Scan for hardcoded Node.js versions
Write-Host "Scanning for hardcoded Node.js versions..."
$HardcodedNodeFiles = Get-ChildItem -Recurse -Include "*.yml", "*.yaml", "Jenkinsfile" | 
    Where-Object { (Select-String -Path $_ -Pattern "NODE_VERSION.*=" -Quiet) }

if ($HardcodedNodeFiles) {
    Add-Content -Path $ReportFile -Value "### ❌ Hardcoded Node.js Versions (High Severity)`n"
    
    foreach ($file in $HardcodedNodeFiles) {
        $relativePath = Resolve-Path -Relative $file.FullName
        Add-Content -Path $ReportFile -Value "**File:** ``$relativePath```n"
        Add-Content -Path $ReportFile -Value "````"
        
        $matches = Select-String -Path $file.FullName -Pattern "NODE_VERSION.*=" | 
            Select-Object -First 3 -ExpandProperty Line
        foreach ($match in $matches) {
            Add-Content -Path $ReportFile -Value $match
        }
        
        Add-Content -Path $ReportFile -Value "````n"
        
        # Add to JSON issues
        $json = Get-Content $JsonFile | ConvertFrom-Json
        $json.issues += @{
            file = $relativePath
            type = "hardcoded-node-version"
            severity = "high"
        }
        $json | ConvertTo-Json -Depth 3 | Set-Content $JsonFile
    }
} else {
    Add-Content -Path $ReportFile -Value "### ✅ No Hardcoded Node.js Versions Found`n"
}

# Scan for outdated Angular CLI references
Write-Host "Scanning for outdated Angular CLI references..."
$OutdatedCliFiles = Get-ChildItem -Recurse -Include "*.yml", "*.yaml", "Jenkinsfile" | 
    Where-Object { (Select-String -Path $_ -Pattern "@angular/cli@[0-9]" -Quiet) }

if ($OutdatedCliFiles) {
    Add-Content -Path $ReportFile -Value "### ⚠️ Outdated Angular CLI References (Medium Severity)`n"
    
    foreach ($file in $OutdatedCliFiles) {
        $relativePath = Resolve-Path -Relative $file.FullName
        Add-Content -Path $ReportFile -Value "**File:** ``$relativePath```n"
        Add-Content -Path $ReportFile -Value "````"
        
        $matches = Select-String -Path $file.FullName -Pattern "@angular/cli@" | 
            Select-Object -First 3 -ExpandProperty Line
        foreach ($match in $matches) {
            Add-Content -Path $ReportFile -Value $match
        }
        
        Add-Content -Path $ReportFile -Value "````n"
        
        # Add to JSON issues
        $json = Get-Content $JsonFile | ConvertFrom-Json
        $json.issues += @{
            file = $relativePath
            type = "outdated-angular-cli"
            severity = "medium"
        }
        $json | ConvertTo-Json -Depth 3 | Set-Content $JsonFile
    }
} else {
    Add-Content -Path $ReportFile -Value "### ✅ No Outdated Angular CLI References Found`n"
}

# Scan for container image issues
Write-Host "Scanning for container Node.js versions..."
$ContainerFiles = Get-ChildItem -Recurse -Include "Dockerfile*", "*.yml", "*.yaml" | 
    Where-Object { (Select-String -Path $_ -Pattern "FROM.*node:[0-9]" -Quiet) }

if ($ContainerFiles) {
    Add-Content -Path $ReportFile -Value "### ⚠️ Container Node.js Versions (Medium Severity)`n"
    
    foreach ($file in $ContainerFiles) {
        $relativePath = Resolve-Path -Relative $file.FullName
        Add-Content -Path $ReportFile -Value "**File:** ``$relativePath```n"
        Add-Content -Path $ReportFile -Value "````"
        
        $matches = Select-String -Path $file.FullName -Pattern "FROM.*node:" | 
            Select-Object -First 3 -ExpandProperty Line
        foreach ($match in $matches) {
            Add-Content -Path $ReportFile -Value $match
        }
        
        Add-Content -Path $ReportFile -Value "````n"
        
        # Add to JSON issues
        $json = Get-Content $JsonFile | ConvertFrom-Json
        $json.issues += @{
            file = $relativePath
            type = "container-node-version"
            severity = "medium"
        }
        $json | ConvertTo-Json -Depth 3 | Set-Content $JsonFile
    }
} else {
    Add-Content -Path $ReportFile -Value "### ✅ No Container Node.js Version Issues Found`n"
}

# Generate summary
$json = Get-Content $JsonFile | ConvertFrom-Json
$TotalFiles = $CiFiles.Count
$TotalIssues = $json.issues.Count

Add-Content -Path $ReportFile -Value "`n## Summary`n"
Add-Content -Path $ReportFile -Value "- **CI Files Scanned:** $TotalFiles"
Add-Content -Path $ReportFile -Value "- **Issues Found:** $TotalIssues"
Add-Content -Path $ReportFile -Value "- **Report Generated:** $(Get-Date)"

# Add summary to JSON
$json.summary = @{
    total_files = $TotalFiles
    total_issues = $TotalIssues
}
$json | ConvertTo-Json -Depth 3 | Set-Content $JsonFile

Write-Host ""
Write-Host "=== Scan Complete ===" -ForegroundColor Green
Write-Host "Report: $ReportFile"
Write-Host "JSON: $JsonFile"
Write-Host "Issues found: $TotalIssues"

# Exit with error code if high severity issues found
$HighSeverityCount = ($json.issues | Where-Object { $_.severity -eq "high" }).Count
if ($HighSeverityCount -gt 0) {
    Write-Host "⚠️ High severity issues found. Review required." -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ CI pipeline inventory complete" -ForegroundColor Green