$competencies = Get-ChildItem -Path "olaf-core/competencies" -Directory
$results = @()

foreach ($comp in $competencies) {
    $promptsCount = (Get-ChildItem -Path "$($comp.FullName)/prompts" -Filter "*.md" -ErrorAction SilentlyContinue).Count
    $docsCount = (Get-ChildItem -Path "$($comp.FullName)/docs" -Directory -ErrorAction SilentlyContinue).Count
    $manifestPath = "$($comp.FullName)/competency-manifest.json"
    
    if (Test-Path $manifestPath) {
        $manifest = Get-Content $manifestPath | ConvertFrom-Json
        $entryPointsCount = $manifest.entry_points.Count
    } else {
        $entryPointsCount = 0
    }
    
    if ($promptsCount -ne $docsCount -or $promptsCount -ne $entryPointsCount) {
        $results += [PSCustomObject]@{
            Pack = $comp.Name
            Prompts = $promptsCount
            DocsFolders = $docsCount
            ManifestEntries = $entryPointsCount
            Mismatch = if ($promptsCount -ne $docsCount) { "Docs" } elseif ($promptsCount -ne $entryPointsCount) { "Manifest" } else { "Both" }
        }
    }
}

if ($results.Count -eq 0) {
    Write-Host "All competency packs are aligned!" -ForegroundColor Green
} else {
    Write-Host "Found $($results.Count) competency packs with mismatches:" -ForegroundColor Yellow
    $results | Format-Table -AutoSize
}
