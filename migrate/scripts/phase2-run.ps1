<#
.SYNOPSIS
  Orchestrate Phase 2 (Spring Boot 3.x modernization) tasks 2.0–2.10.

.DESCRIPTION
  This script provides a resumable, idempotent driver for the Phase 2 tasks that were
  scaffolded under tasks/phase2-boot3-migration. Each task has lightweight verification
  logic that checks for expected artifacts or code patterns. Where full automation
  requires domain decisions (e.g., refactoring security config), the script surfaces
  TODO guidance instead of attempting risky changes.

  It maintains a JSON state file (phase2-state.json) tracking task status:
    - not-started | in-progress | completed | failed

  The script DOES NOT mutate code beyond creating logs; it verifies deliverables.
  You still perform the actual refactors guided by each task's prompt; then run this
  script to validate & record progress, optionally committing. This avoids accidental
  destructive automation.

.PARAMETER StartFrom
  Task id to start/resume from (default: earliest not completed). Examples: 2.0, 2.3

.PARAMETER Only
  Comma-separated list of task ids to run exclusively (overrides StartFrom/Until).

.PARAMETER Until
  Last task id to run (inclusive). Useful for partial execution.

.PARAMETER DryRun
  Perform detection & print would-be actions without writing state or git commits.

.PARAMETER Commit
  If set, creates a git commit after each successful task with a conventional message.

.PARAMETER Skip
  Comma-separated list of task ids to skip (recorded as skipped in state).

.PARAMETER Force
  Re-run verification even if a task is already marked completed.

.EXAMPLES
  ./phase2-run.ps1                 # Resume from first incomplete task
  ./phase2-run.ps1 -StartFrom 2.3  # Begin at Security 6 adjustments
  ./phase2-run.ps1 -Only 2.0,2.1   # Run readiness + core upgrade only
  ./phase2-run.ps1 -Until 2.5      # Run through Problem Details adoption
  ./phase2-run.ps1 -Commit         # Auto-commit after each task
  ./phase2-run.ps1 -DryRun         # Show what would be done

.NOTES
  Cross-platform companion: scripts/phase2-run.sh
  Adjust detection patterns to project structure if using multi-module layout.
#>
[CmdletBinding()]
param(
  [string]$StartFrom,
  [string]$Until,
  [string]$Only,
  [switch]$DryRun,
  [switch]$Commit,
  [string]$Skip,
  [switch]$Force
)

$ErrorActionPreference = 'Stop'
$StateFile = Join-Path $PSScriptRoot 'phase2-state.json'
$LogDir = Join-Path $PSScriptRoot 'logs'
if(-not (Test-Path $LogDir)){ New-Item -ItemType Directory -Path $LogDir | Out-Null }

function Write-Info($m){ Write-Host "[Phase2] $m" -ForegroundColor Cyan }
function Write-Warn($m){ Write-Host "[Phase2] WARN $m" -ForegroundColor Yellow }
function Write-Err($m){ Write-Host "[Phase2] ERROR $m" -ForegroundColor Red }

# --- Task Definitions (id, name, verify scriptblock) ---
$Tasks = @(
  @{ Id='2.0'; Name='Readiness Assessment'; Verify={
        $report = Get-ChildItem -Recurse -Include boot3-readiness-report.md | Select-Object -First 1
        if($null -eq $report){ throw 'Missing boot3-readiness-report.md' }
        return @{ note='Readiness report found'; path=$report.FullName }
      }},
  @{ Id='2.1'; Name='Upgrade 2.7→3.0'; Verify={
        $version = & $PSScriptRoot/detect-spring-boot-version.ps1 2>$null
        if(-not $version){ throw 'Cannot detect Spring Boot version' }
        if($version -notmatch '^3\.0\.') { throw "Expected 3.0.x but got $version" }
        return @{ version=$version }
      }},
  @{ Id='2.2'; Name='Jakarta Namespace Migration'; Verify={
        $javaFiles = Get-ChildItem -Recurse -Include *.java -ErrorAction SilentlyContinue
        $javax = 0
        foreach($f in $javaFiles){ if(Select-String -Path $f.FullName -Pattern '\bjavax\.' -Quiet){ $javax++ } }
        if($javax -gt 0){ throw "Found $javax files still containing javax.*" }
        return @{ remaining=$javax }
      }},
  @{ Id='2.3'; Name='Security 6 Adjustments'; Verify={
        $legacy = Get-ChildItem -Recurse -Include *.java | Where-Object { Select-String -Path $_.FullName -Pattern 'WebSecurityConfigurerAdapter' -Quiet }
        if($legacy){ throw 'Legacy WebSecurityConfigurerAdapter still present' }
        $filterChain = Select-String -Path (Get-ChildItem -Recurse -Include *.java) -Pattern 'SecurityFilterChain' -Quiet
        if(-not $filterChain){ Write-Warn 'No SecurityFilterChain bean detected (may be custom config)' }
        return @{ legacy='none' }
      }},
  @{ Id='2.4'; Name='Validation/Actuator/Micrometer Alignment'; Verify={
        $legacyValidation = Select-String -Path (Get-ChildItem -Recurse -Include *.java) -Pattern '\bjavax.validation' -Quiet
        if($legacyValidation){ throw 'javax.validation references remain' }
        return @{ ok='true' }
      }},
  @{ Id='2.5'; Name='Problem Details Adoption'; Verify={
        $pdUsage = Select-String -Path (Get-ChildItem -Recurse -Include *.java) -Pattern '\bProblemDetail' -Quiet
        if(-not $pdUsage){ Write-Warn 'No ProblemDetail usage detected; ensure adoption doc exists' }
        $doc = Get-ChildItem -Recurse -Include problem-details-adoption.md | Select-Object -First 1
        if(-not $doc){ Write-Warn 'problem-details-adoption.md not found' }
        return @{ doc = if($doc){$doc.FullName}else{'missing'} }
      }},
  @{ Id='2.6'; Name='Observability & Logging Modernization'; Verify={
        $concat = Select-String -Path (Get-ChildItem -Recurse -Include *.java) -Pattern 'logger\.(info|error|warn)\(".*" \+' -SimpleMatch:$false -Quiet
        if($concat){ Write-Warn 'Some logger concat patterns remain (consider parameterized logging)' }
        return @{ suggestion='review logging concatenation' }
      }},
  @{ Id='2.7'; Name='Upgrade 3.0→3.1'; Verify={
        $version = & $PSScriptRoot/detect-spring-boot-version.ps1 2>$null
        if($version -notmatch '^3\.1\.') { throw "Expected 3.1.x but got $version" }
        return @{ version=$version }
      }},
  @{ Id='2.8'; Name='Upgrade 3.1→3.2'; Verify={
        $version = & $PSScriptRoot/detect-spring-boot-version.ps1 2>$null
        if($version -notmatch '^3\.2\.') { throw "Expected 3.2.x but got $version" }
        return @{ version=$version }
      }},
  @{ Id='2.9'; Name='Performance & Config Cleanup'; Verify={
        $deprecated = Get-ChildItem -Recurse -Include deprecated-properties.txt | Select-Object -First 1
        if(-not $deprecated){ Write-Warn 'deprecated-properties.txt not found' }
        elseif((Get-Content $deprecated.FullName | Where-Object { $_ -match '\S' }).Count -gt 0){ Write-Warn 'Deprecated properties remaining; review required' }
        return @{ file = if($deprecated){$deprecated.FullName}else{'missing'} }
      }},
  @{ Id='2.10'; Name='Final Phase 2 Report'; Verify={
        $report = Get-ChildItem -Recurse -Include phase2-migration-report.md | Select-Object -First 1
        if(-not $report){ throw 'Missing phase2-migration-report.md' }
        return @{ path=$report.FullName }
      }}
)

# --- Load / Init State ---
if(Test-Path $StateFile){ $State = Get-Content $StateFile -Raw | ConvertFrom-Json } else { $State = [ordered]@{ tasks=@{} version='1'; updated=(Get-Date) } }
if(-not $State.tasks){ $State.tasks = @{} }

# Initialize missing tasks in state
foreach($t in $Tasks){ if(-not $State.tasks.$($t.Id)){ $State.tasks.$($t.Id) = @{ status='not-started'; notes=@() } } }

function Save-State(){ if($DryRun){ return } $State.updated = (Get-Date); $State | ConvertTo-Json -Depth 8 | Set-Content $StateFile }

# --- Selection Logic ---
$onlySet = @()
if($Only){ $onlySet = $Only.Split(',') | ForEach-Object { $_.Trim() } }
$skipSet = @()
if($Skip){ $skipSet = $Skip.Split(',') | ForEach-Object { $_.Trim() } }

function Should-Run($task){
  if($onlySet.Count -gt 0){ return $onlySet -contains $task.Id }
  if($skipSet -contains $task.Id){ return $false }
  if($StartFrom -and ($task.Id -lt $StartFrom)){ return $false }
  if($Until -and ($task.Id -gt $Until)){ return $false }
  return $true
}

# Determine default StartFrom if not specified & no Only
if(-not $Only -and -not $StartFrom){
  $pending = $Tasks | Where-Object { $State.tasks.$($_.Id).status -ne 'completed' }
  if($pending){ $StartFrom = ($pending | Select-Object -First 1).Id } else { $StartFrom = ($Tasks[-1]).Id }
}

Write-Info "Execution plan:"
foreach($t in $Tasks){ if(Should-Run $t){ Write-Host "  - ${($t.Id)} $($t.Name)" } }
if($DryRun){ Write-Warn 'Dry run mode: state & git unchanged' }

# --- Execution Loop ---
foreach($t in $Tasks){
  if(-not (Should-Run $t)){ continue }
  $id = $t.Id
  $st = $State.tasks.$id
  if($st.status -eq 'completed' -and -not $Force){ Write-Info "Skip $id (already completed)"; continue }
  if($skipSet -contains $id){ $st.status = 'skipped'; continue }
  Write-Info "Running verification for $id $($t.Name)"
  $st.status = 'in-progress'; Save-State
  $logPath = Join-Path $LogDir "task-$id.log"
  try {
    $result = & { & $t.Verify } 2>&1 | Tee-Object $logPath
    $st.status = 'completed'
    if($result -is [System.Collections.IDictionary]){ $st.notes += ("result=" + ($result | ConvertTo-Json -Compress)) }
    else { $st.notes += 'verification-complete' }
    Write-Info "Task $id completed"
    if($Commit -and -not $DryRun){
      if(Test-Path .git){
        git add . 2>$null | Out-Null
        git commit -m "chore(phase2): mark task $id complete" 2>$null | Out-Null
        Write-Info "Git commit created for $id"
      } else { Write-Warn 'No git repository detected; skipping commit' }
    }
  }
  catch {
    $st.status = 'failed'
    $errMsg = $_.Exception.Message
    $st.notes += "error=$errMsg"
    Write-Err "Task $id FAILED: $errMsg"
    if(-not $DryRun){ Save-State }
    break
  }
  Save-State
}

Write-Info 'Phase 2 automation run finished.'
if(Test-Path $StateFile){ Write-Info "State file: $StateFile" }
