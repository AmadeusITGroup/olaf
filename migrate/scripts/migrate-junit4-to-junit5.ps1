#!/usr/bin/env pwsh#!/usr/bin/env pwsh

# migrate-junit4-to-junit5.ps1# migrate-junit4-to-junit5.ps1

# Automatically migrates JUnit 4 test files to JUnit 5 (Jupiter)# Automatically migrates JUnit 4 test files to JUnit 5 (Jupiter)



param(param(

    [Parameter(Mandatory=$false)]    [Parameter(Mandatory=$false)]

    [string]$ProjectPath = ".",    [string]$ProjectPath = ".",

    [switch]$DryRun    [switch]$DryRun

))



$ErrorActionPreference = "Stop"$ErrorActionPreference = "Stop"



Write-Host "=== JUnit 4 to JUnit 5 Migration Script ===" -ForegroundColor CyanWrite-Host "=== JUnit 4 to JUnit 5 Migration Script ===" -ForegroundColor Cyan

Write-Host ""Write-Host ""



# Resolve absolute path# Resolve absolute path

$ProjectPath = Resolve-Path $ProjectPath$ProjectPath = Resolve-Path $ProjectPath

Write-Host "Project path: $ProjectPath" -ForegroundColor YellowWrite-Host "Project path: $ProjectPath" -ForegroundColor Yellow



# Find all Java test files# Find all Java test files

$testPath = Join-Path $ProjectPath "src\test\java"$testPath = Join-Path $ProjectPath "src\test\java"

if (-not (Test-Path $testPath)) {if (-not (Test-Path $testPath)) {

    Write-Host "ERROR: Test directory not found: $testPath" -ForegroundColor Red    Write-Host "ERROR: Test directory not found: $testPath" -ForegroundColor Red

    exit 1    exit 1

}}



$javaFiles = Get-ChildItem -Path $testPath -Filter "*.java" -Recurse$javaFiles = Get-ChildItem -Path $testPath -Filter "*.java" -Recurse

Write-Host "Found $($javaFiles.Count) Java test files" -ForegroundColor GreenWrite-Host "Found $($javaFiles.Count) Java test files" -ForegroundColor Green

Write-Host ""Write-Host ""



$filesModified = 0$filesModified = 0

$totalChanges = 0$totalChanges = 0



foreach ($file in $javaFiles) {foreach ($file in $javaFiles) {

    $content = Get-Content $file.FullName -Raw -Encoding UTF8    $content = Get-Content $file.FullName -Raw -Encoding UTF8

    $fileChanges = 0    $originalContent = $content

    $changes = @()    $fileChanges = 0

        

    # 1. Import replacements    # Track changes for this file

    if ($content -match 'import org\.junit\.Test;') {    $changes = @()

        $content = $content -replace 'import org\.junit\.Test;', 'import org.junit.jupiter.api.Test;'    

        $changes += "  - Import: org.junit.Test → org.junit.jupiter.api.Test"    # 1. Import replacements

        $fileChanges++    $importReplacements = @{

    }        'import org.junit.Test;' = 'import org.junit.jupiter.api.Test;'

            'import org.junit.Before;' = 'import org.junit.jupiter.api.BeforeEach;'

    if ($content -match 'import org\.junit\.Before;') {        'import org.junit.After;' = 'import org.junit.jupiter.api.AfterEach;'

        $content = $content -replace 'import org\.junit\.Before;', 'import org.junit.jupiter.api.BeforeEach;'        'import org.junit.BeforeClass;' = 'import org.junit.jupiter.api.BeforeAll;'

        $changes += "  - Import: org.junit.Before → org.junit.jupiter.api.BeforeEach"        'import org.junit.AfterClass;' = 'import org.junit.jupiter.api.AfterAll;'

        $fileChanges++        'import org.junit.Ignore;' = 'import org.junit.jupiter.api.Disabled;'

    }        'import org.junit.Assert;' = 'import org.junit.jupiter.api.Assertions;'

            'import org.junit.Rule;' = '// import org.junit.Rule; // JUnit 5: Use @RegisterExtension or assertThrows() instead'

    if ($content -match 'import org\.junit\.After;') {        'import org.junit.rules.ExpectedException;' = '// import org.junit.rules.ExpectedException; // JUnit 5: Use assertThrows() instead'

        $content = $content -replace 'import org\.junit\.After;', 'import org.junit.jupiter.api.AfterEach;'        'import org.junit.runner.RunWith;' = '// import org.junit.runner.RunWith; // Not needed in Spring Boot 2.4+'

        $changes += "  - Import: org.junit.After → org.junit.jupiter.api.AfterEach"        'import org.junit.Assume;' = 'import org.junit.jupiter.api.Assumptions;'

        $fileChanges++        'import static org.junit.Assert\.' = 'import static org.junit.jupiter.api.Assertions.'

    }        'import static org.junit.Assume\.' = 'import static org.junit.jupiter.api.Assumptions.'

        }

    if ($content -match 'import org\.junit\.Ignore;') {    

        $content = $content -replace 'import org\.junit\.Ignore;', 'import org.junit.jupiter.api.Disabled;'    foreach ($old in $importReplacements.Keys) {

        $changes += "  - Import: org.junit.Ignore → org.junit.jupiter.api.Disabled"        $new = $importReplacements[$old]

        $fileChanges++        if ($content -match [regex]::Escape($old)) {

    }            $content = $content -replace [regex]::Escape($old), $new

                $changes += "  - Import: $old → $new"

    if ($content -match 'import org\.junit\.Rule;') {            $fileChanges++

        $content = $content -replace 'import org\.junit\.Rule;', '// import org.junit.Rule; // JUnit 5: Use @RegisterExtension instead'        }

        $changes += "  - Import: Commented org.junit.Rule (use @RegisterExtension in JUnit 5)"    }

        $fileChanges++    

    }    # 2. Annotation replacements

        if ($content -match '@Before\s') {

    if ($content -match 'import org\.junit\.rules\.ExpectedException;') {        $content = $content -replace '@Before\b', '@BeforeEach'

        $content = $content -replace 'import org\.junit\.rules\.ExpectedException;', '// import org.junit.rules.ExpectedException; // JUnit 5: Use assertThrows() instead'        $changes += "  - Annotation: @Before → @BeforeEach"

        $changes += "  - Import: Commented ExpectedException (use assertThrows in JUnit 5)"        $fileChanges++

        $fileChanges++    }

    }    

        if ($content -match '@After\s') {

    if ($content -match 'import org\.junit\.runner\.RunWith;') {        $content = $content -replace '@After\b', '@AfterEach'

        $content = $content -replace 'import org\.junit\.runner\.RunWith;', '// import org.junit.runner.RunWith; // Not needed in Spring Boot 2.4+'        $changes += "  - Annotation: @After → @AfterEach"

        $changes += "  - Import: Commented RunWith (not needed in Spring Boot 2.4+)"        $fileChanges++

        $fileChanges++    }

    }    

        if ($content -match '@BeforeClass\s') {

    if ($content -match 'import static org\.junit\.Assume\.assumeTrue;') {        $content = $content -replace '@BeforeClass\b', '@BeforeAll'

        $content = $content -replace 'import static org\.junit\.Assume\.assumeTrue;', 'import static org.junit.jupiter.api.Assumptions.assumeTrue;'        $changes += "  - Annotation: @BeforeClass → @BeforeAll"

        $changes += "  - Import: org.junit.Assume.assumeTrue → org.junit.jupiter.api.Assumptions.assumeTrue"        $fileChanges++

        $fileChanges++    }

    }    

        if ($content -match '@AfterClass\s') {

    if ($content -match 'import static org\.junit\.Assert\.fail;') {        $content = $content -replace '@AfterClass\b', '@AfterAll'

        $content = $content -replace 'import static org\.junit\.Assert\.fail;', 'import static org.junit.jupiter.api.Assertions.fail;'        $changes += "  - Annotation: @AfterClass → @AfterAll"

        $changes += "  - Import: org.junit.Assert.fail → org.junit.jupiter.api.Assertions.fail"        $fileChanges++

        $fileChanges++    }

    }    

        if ($content -match '@Ignore\b') {

    # 2. Annotation replacements        $content = $content -replace '@Ignore\b', '@Disabled'

    if ($content -match '@Before\s') {        $changes += "  - Annotation: @Ignore → @Disabled"

        $content = $content -replace '@Before\b', '@BeforeEach'        $fileChanges++

        $changes += "  - Annotation: @Before → @BeforeEach"    }

        $fileChanges++    

    }    # 3. Remove @RunWith(SpringRunner.class) - not needed in Spring Boot 2.4+

        if ($content -match '@RunWith\(SpringRunner\.class\)') {

    if ($content -match '@After\s') {        $content = $content -replace '@RunWith\(SpringRunner\.class\)\s*\r?\n', ''

        $content = $content -replace '@After\b', '@AfterEach'        $changes += "  - Removed: @RunWith(SpringRunner.class) [not needed in Spring Boot 2.4+]"

        $changes += "  - Annotation: @After → @AfterEach"        $fileChanges++

        $fileChanges++    }

    }    

        # 4. Convert @RunWith(MockitoJUnitRunner.class) to @ExtendWith(MockitoExtension.class)

    if ($content -match '@Ignore\b') {    if ($content -match '@RunWith\(MockitoJUnitRunner\.class\)') {

        $content = $content -replace '@Ignore\b', '@Disabled'        $content = $content -replace '@RunWith\(MockitoJUnitRunner\.class\)', '@ExtendWith(MockitoExtension.class)'

        $changes += "  - Annotation: @Ignore → @Disabled"        # Add import if not present

        $fileChanges++        if ($content -notmatch 'import org\.junit\.jupiter\.api\.extension\.ExtendWith;') {

    }            $content = $content -replace '(package .*?;)', "`$1`r`nimport org.junit.jupiter.api.extension.ExtendWith;`r`nimport org.mockito.junit.jupiter.MockitoExtension;"

            }

    # 3. Remove @RunWith(SpringRunner.class)        $changes += "  - Annotation: @RunWith(MockitoJUnitRunner.class) → @ExtendWith(MockitoExtension.class)"

    if ($content -match '@RunWith\(SpringRunner\.class\)') {        $fileChanges++

        $content = $content -replace '@RunWith\(SpringRunner\.class\)\s*\r?\n', ''    }

        $changes += "  - Removed: @RunWith(SpringRunner.class) [not needed in Spring Boot 2.4+]"    

        $fileChanges++    # 5. Comment out @Rule ExpectedException (needs manual migration to assertThrows)

    }    if ($content -match '@Rule\s+public\s+final\s+ExpectedException') {

            $content = $content -replace '(@Rule\s+public\s+final\s+ExpectedException[^;]+;)', '// $1 // TODO: Migrate to assertThrows() in JUnit 5'

    # 4. Convert @RunWith(MockitoJUnitRunner.class)        $changes += "  - Commented @Rule ExpectedException [TODO: Manual migration to assertThrows() needed]"

    if ($content -match '@RunWith\(MockitoJUnitRunner\.class\)') {        $fileChanges++

        $content = $content -replace '@RunWith\(MockitoJUnitRunner\.class\)', '@ExtendWith(MockitoExtension.class)'    }

        if ($content -notmatch 'import org\.junit\.jupiter\.api\.extension\.ExtendWith;') {    

            $content = $content -replace '(package .*?;)', "`$1`r`nimport org.junit.jupiter.api.extension.ExtendWith;`r`nimport org.mockito.junit.jupiter.MockitoExtension;"    # 6. Update assumeTrue import usage

        }    if ($content -match 'assumeTrue\(') {

        $changes += "  - Annotation: @RunWith(MockitoJUnitRunner.class) → @ExtendWith(MockitoExtension.class)"        if ($content -match 'import static org\.junit\.Assume\.assumeTrue;') {

        $fileChanges++            $content = $content -replace 'import static org\.junit\.Assume\.assumeTrue;', 'import static org.junit.jupiter.api.Assumptions.assumeTrue;'

    }            $changes += "  - Static import: assumeTrue from Assume → Assumptions"

                $fileChanges++

    # Report and save        }

    if ($fileChanges -gt 0) {    }

        $filesModified++    

        $totalChanges += $fileChanges    # 7. Update Assert.fail to Assertions.fail

        $relativePath = $file.FullName.Replace($ProjectPath + "\", "")    if ($content -match '\bAssert\.fail\b') {

        Write-Host "✓ $relativePath" -ForegroundColor Green        $content = $content -replace '\bAssert\.fail\b', 'Assertions.fail'

        foreach ($change in $changes) {        if ($content -notmatch 'import org\.junit\.jupiter\.api\.Assertions;') {

            Write-Host $change -ForegroundColor Gray            $content = $content -replace '(package .*?;)', "`$1`r`nimport org.junit.jupiter.api.Assertions;"

        }        }

        Write-Host ""        $changes += "  - Static method: Assert.fail → Assertions.fail"

                $fileChanges++

        if (-not $DryRun) {    }

            Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline    

        }    # Report changes for this file

    }    if ($fileChanges -gt 0) {

}        $filesModified++

        $totalChanges += $fileChanges

Write-Host "========================================" -ForegroundColor Cyan        $relativePath = $file.FullName.Replace($ProjectPath + "\", "")

Write-Host "Migration Summary:" -ForegroundColor Cyan        Write-Host "✓ $relativePath" -ForegroundColor Green

Write-Host "  Files processed: $($javaFiles.Count)" -ForegroundColor Yellow        foreach ($change in $changes) {

Write-Host "  Files modified:  $filesModified" -ForegroundColor Green            Write-Host $change -ForegroundColor Gray

Write-Host "  Total changes:   $totalChanges" -ForegroundColor Green        }

        Write-Host ""

if ($DryRun) {        

    Write-Host ""        # Write changes unless dry run

    Write-Host "DRY RUN - No files were actually modified" -ForegroundColor Yellow        if (-not $DryRun) {

} else {            Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline

    Write-Host ""        }

    Write-Host "✓ Migration complete!" -ForegroundColor Green    }

    Write-Host "Next: mvn clean test-compile" -ForegroundColor White} # End foreach

}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Migration Summary:" -ForegroundColor Cyan
Write-Host "  Files processed: $($javaFiles.Count)" -ForegroundColor Yellow
Write-Host "  Files modified:  $filesModified" -ForegroundColor Green
Write-Host "  Total changes:   $totalChanges" -ForegroundColor Green

if ($DryRun) {
    Write-Host ""
    Write-Host "DRY RUN - No files were actually modified" -ForegroundColor Yellow
    Write-Host "Run without -DryRun to apply changes" -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "✓ Migration complete!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "  1. Review changes: git diff" -ForegroundColor White
    Write-Host "  2. Compile tests: mvn clean test-compile" -ForegroundColor White
    Write-Host "  3. Run tests: mvn test" -ForegroundColor White
}

exit 0
