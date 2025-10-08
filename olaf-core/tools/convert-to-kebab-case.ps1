# PowerShell Script: Convert olaf-works filenames to kebab-case
# This script renames all files to lowercase kebab-case and updates all internal references

param(
    [string]$BasePath = "c:\Users\ppaccaud\coderepos\genai-1a-projects\bird-java-api\olaf-works",
    [switch]$DryRun = $false
)

Write-Host "=== OLAF-WORKS KEBAB-CASE CONVERSION SCRIPT ===" -ForegroundColor Green
Write-Host "Base Path: $BasePath" -ForegroundColor Yellow
Write-Host "Dry Run Mode: $DryRun" -ForegroundColor Yellow
Write-Host ""

# Function to convert filename to kebab-case
function Convert-ToKebabCase {
    param([string]$FileName)
    
    # Remove file extension temporarily
    $nameWithoutExt = [System.IO.Path]::GetFileNameWithoutExtension($FileName)
    $extension = [System.IO.Path]::GetExtension($FileName)
    
    # Convert to kebab-case
    $kebabName = $nameWithoutExt.ToLower() -replace '_', '-'
    
    return "$kebabName$extension"
}

# Define file mapping for all files that need renaming
$FileMapping = @{
    # Orchestrator files
    "orchestrator\MAIN_ORCHESTRATOR.md" = "orchestrator\main-orchestrator.md"
    "orchestrator\METHODOLOGY_OVERVIEW.md" = "orchestrator\methodology-overview.md"
    
    # Workflow files
    "workflows\WORKFLOW_1_SPECIFICATION.md" = "workflows\workflow-1-specification.md"
    "workflows\WORKFLOW_2_DESIGN.md" = "workflows\workflow-2-design.md"
    "workflows\WORKFLOW_3_PLANNING.md" = "workflows\workflow-3-planning.md"
    "workflows\WORKFLOW_4_EXECUTION.md" = "workflows\workflow-4-execution.md"
    
    # Prompt files - Phase 1
    "prompts\PROMPT_1-1_INITIAL_SPECIFICATION.md" = "prompts\prompt-1-1-initial-specification.md"
    "prompts\PROMPT_1-2_CODEBASE_VALIDATION.md" = "prompts\prompt-1-2-codebase-validation.md"
    "prompts\PROMPT_1-3_USER_REVIEW.md" = "prompts\prompt-1-3-user-review.md"
    "prompts\PROMPT_1-4_FINALIZATION.md" = "prompts\prompt-1-4-finalization.md"
    
    # Prompt files - Phase 2
    "prompts\PROMPT_2-1_INITIAL_DESIGN.md" = "prompts\prompt-2-1-initial-design.md"
    "prompts\PROMPT_2-2_DESIGN_VALIDATION.md" = "prompts\prompt-2-2-design-validation.md"
    "prompts\PROMPT_2-3_TECHNICAL_REVIEW.md" = "prompts\prompt-2-3-technical-review.md"
    "prompts\PROMPT_2-4_DESIGN_FINALIZATION.md" = "prompts\prompt-2-4-design-finalization.md"
    
    # Prompt files - Phase 3
    "prompts\PROMPT_3-1_TEST_PLAN.md" = "prompts\prompt-3-1-test-plan.md"
    "prompts\PROMPT_3-2_DOCUMENTATION_PLAN.md" = "prompts\prompt-3-2-documentation-plan.md"
    "prompts\PROMPT_3-3_IMPLEMENTATION_PLANS.md" = "prompts\prompt-3-3-implementation-plans.md"
    
    # Prompt files - Phase 4
    "prompts\PROMPT_4-1_IMPLEMENTATION_EXECUTION.md" = "prompts\prompt-4-1-implementation-execution.md"
    "prompts\PROMPT_4-2_DOCUMENTATION_EXECUTION.md" = "prompts\prompt-4-2-documentation-execution.md"
    "prompts\PROMPT_4-3_FUNCTIONAL_TESTING_EXECUTION.md" = "prompts\prompt-4-3-functional-testing-execution.md"
    
    # Template files
    "templates\TEMPLATE_CHANGE_LOG.md" = "templates\template-change-log.md"
    "templates\TEMPLATE_DESIGN_DOCUMENT.md" = "templates\template-design-document.md"
    "templates\TEMPLATE_DESIGN_ENHANCED.md" = "templates\template-design-enhanced.md"
    "templates\TEMPLATE_DESIGN_FINAL.md" = "templates\template-design-final.md"
    "templates\TEMPLATE_DOCUMENTATION_PLAN.md" = "templates\template-documentation-plan.md"
    "templates\TEMPLATE_IMPLEMENTATION_PLANS.md" = "templates\template-implementation-plans.md"
    "templates\TEMPLATE_SPECIFICATION.md" = "templates\template-specification.md"
    "templates\TEMPLATE_SPECIFICATION_ENHANCED.md" = "templates\template-specification-enhanced.md"
    "templates\TEMPLATE_SPECIFICATION_FINAL.md" = "templates\template-specification-final.md"
    "templates\TEMPLATE_TEST_PLAN.md" = "templates\template-test-plan.md"
    
    # Root files
    "README_METHODOLOGY.md" = "readme-methodology.md"
}

Write-Host "=== PHASE 1: FILE ANALYSIS ===" -ForegroundColor Cyan
Write-Host "Files to rename: $($FileMapping.Count)" -ForegroundColor White

# Verify all source files exist
$MissingFiles = @()
foreach ($oldPath in $FileMapping.Keys) {
    $fullOldPath = Join-Path $BasePath $oldPath
    if (-not (Test-Path $fullOldPath)) {
        $MissingFiles += $oldPath
        Write-Host "WARNING: File not found: $oldPath" -ForegroundColor Red
    }
}

if ($MissingFiles.Count -gt 0) {
    Write-Host "ERROR: $($MissingFiles.Count) files are missing. Aborting." -ForegroundColor Red
    exit 1
}

Write-Host "All source files verified." -ForegroundColor Green
Write-Host ""

# Build reference mapping for content updates
Write-Host "=== PHASE 2: BUILDING REFERENCE MAPPING ===" -ForegroundColor Cyan

$ReferenceMapping = @{}

# Add filename-only references (without path)
foreach ($entry in $FileMapping.GetEnumerator()) {
    $oldFileName = Split-Path $entry.Key -Leaf
    $newFileName = Split-Path $entry.Value -Leaf
    $ReferenceMapping[$oldFileName] = $newFileName
}

# Add path-based references
foreach ($entry in $FileMapping.GetEnumerator()) {
    $oldPath = $entry.Key -replace '\\', '/'  # Convert to forward slashes for cross-platform
    $newPath = $entry.Value -replace '\\', '/'
    $ReferenceMapping[$oldPath] = $newPath
    
    # Add relative path variations
    $ReferenceMapping["../$oldPath"] = "../$newPath"
    $ReferenceMapping["./$oldPath"] = "./$newPath"
}

Write-Host "Reference mappings created: $($ReferenceMapping.Count)" -ForegroundColor White
Write-Host ""

if ($DryRun) {
    Write-Host "=== DRY RUN MODE - SHOWING PLANNED CHANGES ===" -ForegroundColor Yellow
    Write-Host ""
    
    Write-Host "File Renames:" -ForegroundColor Cyan
    foreach ($entry in $FileMapping.GetEnumerator()) {
        Write-Host "  $($entry.Key) -> $($entry.Value)" -ForegroundColor White
    }
    
    Write-Host ""
    Write-Host "Reference Updates (sample):" -ForegroundColor Cyan
    $sampleRefs = $ReferenceMapping.GetEnumerator() | Select-Object -First 10
    foreach ($ref in $sampleRefs) {
        Write-Host "  '$($ref.Key)' -> '$($ref.Value)'" -ForegroundColor White
    }
    Write-Host "  ... and $($ReferenceMapping.Count - 10) more reference mappings" -ForegroundColor Gray
    
    Write-Host ""
    Write-Host "To execute the changes, run the script without -DryRun flag" -ForegroundColor Yellow
    exit 0
}

Write-Host "=== PHASE 3: RENAMING FILES ===" -ForegroundColor Cyan

$RenamedFiles = @()
foreach ($entry in $FileMapping.GetEnumerator()) {
    $oldFullPath = Join-Path $BasePath $entry.Key
    $newFullPath = Join-Path $BasePath $entry.Value
    
    try {
        Write-Host "Renaming: $($entry.Key) -> $($entry.Value)" -ForegroundColor White
        Move-Item -Path $oldFullPath -Destination $newFullPath -Force
        $RenamedFiles += @{Old = $entry.Key; New = $entry.Value}
    }
    catch {
        Write-Host "ERROR renaming $($entry.Key): $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host "Files renamed: $($RenamedFiles.Count)" -ForegroundColor Green
Write-Host ""

Write-Host "=== PHASE 4: UPDATING FILE CONTENT REFERENCES ===" -ForegroundColor Cyan

# Get all markdown files for content updates (now with new names)
$AllMarkdownFiles = Get-ChildItem -Path $BasePath -Recurse -Filter "*.md" | Where-Object { $_.FullName -notlike "*\old\*" -and $_.FullName -notlike "*\demand\*" }

$UpdatedFiles = @()
foreach ($file in $AllMarkdownFiles) {
    Write-Host "Processing: $($file.Name)" -ForegroundColor White
    
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    $changesMade = $false
    
    # Apply all reference mappings
    foreach ($mapping in $ReferenceMapping.GetEnumerator()) {
        if ($content -match [regex]::Escape($mapping.Key)) {
            $content = $content -replace [regex]::Escape($mapping.Key), $mapping.Value
            $changesMade = $true
        }
    }
    
    # Save if changes were made
    if ($changesMade) {
        try {
            Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
            $UpdatedFiles += $file.Name
            Write-Host "  Updated references in: $($file.Name)" -ForegroundColor Green
        }
        catch {
            Write-Host "  ERROR updating $($file.Name): $($_.Exception.Message)" -ForegroundColor Red
        }
    }
}

Write-Host "Content updated in $($UpdatedFiles.Count) files" -ForegroundColor Green
Write-Host ""

Write-Host "=== PHASE 5: VERIFICATION ===" -ForegroundColor Cyan

# Check for any remaining uppercase references
$RemainingIssues = @()
foreach ($file in $AllMarkdownFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Look for patterns that might be missed uppercase references
    $upperCaseMatches = [regex]::Matches($content, '\b(WORKFLOW_|PROMPT_|TEMPLATE_|MAIN_ORCHESTRATOR|METHODOLOGY_OVERVIEW|README_METHODOLOGY)\w*\.md\b')
    
    if ($upperCaseMatches.Count -gt 0) {
        $RemainingIssues += @{
            File = $file.Name
            Issues = $upperCaseMatches | ForEach-Object { $_.Value }
        }
    }
}

if ($RemainingIssues.Count -gt 0) {
    Write-Host "WARNING: Found potential remaining uppercase references:" -ForegroundColor Yellow
    foreach ($issue in $RemainingIssues) {
        Write-Host "  $($issue.File): $($issue.Issues -join ', ')" -ForegroundColor Yellow
    }
} else {
    Write-Host "No remaining uppercase references found." -ForegroundColor Green
}

Write-Host ""
Write-Host "=== CONVERSION COMPLETE ===" -ForegroundColor Green
Write-Host "Files renamed: $($RenamedFiles.Count)" -ForegroundColor White
Write-Host "Content updated: $($UpdatedFiles.Count) files" -ForegroundColor White
Write-Host "Remaining issues: $($RemainingIssues.Count)" -ForegroundColor White

if ($RemainingIssues.Count -eq 0) {
    Write-Host "SUCCESS: All files converted to kebab-case!" -ForegroundColor Green
} else {
    Write-Host "PARTIAL SUCCESS: Manual review needed for remaining issues." -ForegroundColor Yellow
}