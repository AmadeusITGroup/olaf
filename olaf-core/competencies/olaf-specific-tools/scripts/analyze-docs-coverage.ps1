$competencies = Get-ChildItem -Path "olaf-core/competencies" -Directory
$allResults = @()
$packStats = @()

foreach ($comp in $competencies) {
    $docsPath = "$($comp.FullName)/docs"
    $promptsPath = "$($comp.FullName)/prompts"
    
    # Count prompts
    $promptsCount = 0
    if (Test-Path $promptsPath) {
        $promptsCount = (Get-ChildItem -Path $promptsPath -Filter "*.md" -ErrorAction SilentlyContinue).Count
    }
    
    # Count docs folders
    $docsFoldersCount = 0
    if (Test-Path $docsPath) {
        $docsFoldersCount = (Get-ChildItem -Path $docsPath -Directory -ErrorAction SilentlyContinue).Count
    }
    
    if (-not (Test-Path $docsPath)) {
        continue
    }
    
    $docsFolders = Get-ChildItem -Path $docsPath -Directory -ErrorAction SilentlyContinue
    
    foreach ($folder in $docsFolders) {
        $descExists = Test-Path "$($folder.FullName)/description.md"
        $tutExists = Test-Path "$($folder.FullName)/tutorial.md"
        
        $status = if ($descExists -and $tutExists) { "Both" }
                  elseif ($descExists) { "Description Only" }
                  elseif ($tutExists) { "Tutorial Only" }
                  else { "Neither" }
        
        $allResults += [PSCustomObject]@{
            Pack = $comp.Name
            EntryPoint = $folder.Name
            Description = $descExists
            Tutorial = $tutExists
            Status = $status
        }
    }
    
    # Store pack statistics
    $matchStatus = if ($promptsCount -eq $docsFoldersCount) { "Yes" } else { "No" }
    $packStats += [PSCustomObject]@{
        Pack = $comp.Name
        Prompts = $promptsCount
        DocsFolders = $docsFoldersCount
        Match = $matchStatus
    }
}

# Summary statistics
$total = $allResults.Count
$both = ($allResults | Where-Object { $_.Status -eq "Both" }).Count
$descOnly = ($allResults | Where-Object { $_.Status -eq "Description Only" }).Count
$tutOnly = ($allResults | Where-Object { $_.Status -eq "Tutorial Only" }).Count
$neither = ($allResults | Where-Object { $_.Status -eq "Neither" }).Count

Write-Host "=== Documentation Coverage Analysis ===" -ForegroundColor Cyan
Write-Host ""

# Show prompts vs docs folders vs manifest alignment
Write-Host "=== Prompts vs Docs Folders vs Manifest Entries ===" -ForegroundColor Cyan

# Add manifest entries to pack stats
$enhancedStats = @()
foreach ($stat in $packStats) {
    $manifestPath = "olaf-core/competencies/$($stat.Pack)/competency-manifest.json"
    $manifestEntries = 0
    if (Test-Path $manifestPath) {
        $manifest = Get-Content $manifestPath | ConvertFrom-Json
        $manifestEntries = $manifest.entry_points.Count
    }
    
    $allMatch = ($stat.Prompts -eq $stat.DocsFolders) -and ($stat.Prompts -eq $manifestEntries)
    $matchStatus = if ($allMatch) { "Yes" } else { "No" }
    
    $enhancedStats += [PSCustomObject]@{
        Pack = $stat.Pack
        Prompts = $stat.Prompts
        DocsFolders = $stat.DocsFolders
        ManifestEntries = $manifestEntries
        AllMatch = $matchStatus
    }
}

$enhancedStats | Format-Table -AutoSize
$fullyAligned = ($enhancedStats | Where-Object { $_.AllMatch -eq "Yes" }).Count
$total_packs = $enhancedStats.Count
Write-Host "Fully aligned packs (Prompts = Docs = Manifest): $fullyAligned/$total_packs"
Write-Host ""

Write-Host "=== Documentation Files Coverage ===" -ForegroundColor Cyan
Write-Host "Total entry point folders: $total"
Write-Host ""
Write-Host "Coverage breakdown:" -ForegroundColor Yellow
$bothPct = [math]::Round($both/$total*100, 1)
$descOnlyPct = [math]::Round($descOnly/$total*100, 1)
$tutOnlyPct = [math]::Round($tutOnly/$total*100, 1)
$neitherPct = [math]::Round($neither/$total*100, 1)
Write-Host "  Both files:        $both ($bothPct%)"
Write-Host "  Description only:  $descOnly ($descOnlyPct%)"
Write-Host "  Tutorial only:     $tutOnly ($tutOnlyPct%)"
Write-Host "  Neither:           $neither ($neitherPct%)"
Write-Host ""

# Group by pack with manifest entries
Write-Host "=== By Competency Pack ===" -ForegroundColor Cyan
$competenciesForManifest = Get-ChildItem -Path "olaf-core/competencies" -Directory
$byPack = $allResults | Group-Object Pack | ForEach-Object {
    $packResults = $_.Group
    $packName = $_.Name
    
    # Get manifest entry count
    $compFolder = $competenciesForManifest | Where-Object { $_.Name -eq $packName }
    $manifestPath = "$($compFolder.FullName)/competency-manifest.json"
    $manifestEntries = 0
    if (Test-Path $manifestPath) {
        $manifest = Get-Content $manifestPath | ConvertFrom-Json
        $manifestEntries = $manifest.entry_points.Count
    }
    
    [PSCustomObject]@{
        Pack = $packName
        ManifestEntries = $manifestEntries
        DocsFolders = $packResults.Count
        Both = ($packResults | Where-Object { $_.Status -eq "Both" }).Count
        DescOnly = ($packResults | Where-Object { $_.Status -eq "Description Only" }).Count
        TutOnly = ($packResults | Where-Object { $_.Status -eq "Tutorial Only" }).Count
        Neither = ($packResults | Where-Object { $_.Status -eq "Neither" }).Count
    }
} | Sort-Object Pack

$byPack | Format-Table -AutoSize

# Show problematic entries (not both)
Write-Host "=== Entries Missing Files ===" -ForegroundColor Yellow
$problematic = $allResults | Where-Object { $_.Status -ne "Both" } | Sort-Object Pack, EntryPoint
Write-Host "Found $($problematic.Count) entries with incomplete documentation:"
Write-Host ""
$problematic | Format-Table Pack, EntryPoint, Status -GroupBy Pack

# Export detailed results
$allResults | Export-Csv -Path "docs-coverage-analysis.csv" -NoTypeInformation
Write-Host "Detailed results exported to: docs-coverage-analysis.csv" -ForegroundColor Green
