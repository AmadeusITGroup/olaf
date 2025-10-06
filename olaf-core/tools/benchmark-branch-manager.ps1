# Benchmark Branch Manager
# Utility script to manage Git branches for persona-based benchmarks
# Replaces expensive folder copying with efficient Git branching

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("create", "cleanup", "list", "switch")]
    [string]$Action,
    
    [string]$Agent = "windsurf-cascade",
    [string]$Model = "cascade", 
    [ValidateSet("coder", "business_analyst", "architect_designer", "technical_writer", "tester", "project_manager")]
    [string]$Persona = "coder",
    [string]$Timestamp,
    [string]$BranchName,
    [switch]$Force
)

# Get current timestamp if not provided
if (-not $Timestamp) {
    $Timestamp = Get-Date -Format "yyyyMMdd-HHmm"
}

# Construct branch name if not provided
if (-not $BranchName) {
    $BranchName = "benchmark-otter-$Agent-$Model-$Persona-$Timestamp"
}

# Paths
$WorkspaceRoot = "."
$ResultsPath = "olaf-data/benchmarks/otter-$Timestamp-$Persona-$Agent-$Model"

function Test-GitRepository {
    if (-not (Test-Path ".git")) {
        Write-Error "Current directory is not a Git repository. Please run from the main workspace root."
        exit 1
    }
    
    # Verify otter directory exists as a folder (not a repo)
    if (-not (Test-Path "otter")) {
        Write-Error "Otter directory not found. Please run from the main workspace root containing the otter folder."
        exit 1
    }
}

function Create-BenchmarkBranch {
    Write-Host "Creating benchmark branch: $BranchName" -ForegroundColor Green
    
    try {
        # Switch to research-benchmark first (as per corrected process)
        Write-Host "Switching to research-benchmark base branch..." -ForegroundColor Cyan
        git checkout research-benchmark
        
        # Check if branch already exists
        $branchExists = git branch --list $BranchName
        if ($branchExists -and -not $Force) {
            Write-Error "Branch '$BranchName' already exists. Use -Force to overwrite."
            return
        }
        
        if ($branchExists -and $Force) {
            Write-Host "Force deleting existing branch..." -ForegroundColor Yellow
            git branch -D $BranchName
        }
        
        # Create and switch to new branch from research-benchmark
        git checkout -b $BranchName
        
        # Create results directory
        New-Item -ItemType Directory -Path "../$ResultsPath" -Force | Out-Null
        
        # Create session-info.json
        $sessionInfo = @{
            timestamp = $Timestamp
            agent = $Agent
            model = $Model
            persona = $Persona
            branch_name = $BranchName
            working_directory = $OtterPath
            results_directory = $ResultsPath
            created_at = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssZ")
        } | ConvertTo-Json -Depth 3
        
        $sessionInfo | Out-File -FilePath "../$ResultsPath/session-info.json" -Encoding UTF8
        
        # Create git-branch-info.json
        $gitInfo = @{
            branch_name = $BranchName
            base_branch = "main"
            initial_commit = (git rev-parse HEAD)
            created_timestamp = $Timestamp
            repository_path = $OtterPath
        } | ConvertTo-Json -Depth 3
        
        $gitInfo | Out-File -FilePath "../$ResultsPath/git-branch-info.json" -Encoding UTF8
        
        # Create persona-tasks.json template
        $tasks = @{
            persona = $Persona
            tasks = @()
            status = "initialized"
            created_at = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssZ")
        } | ConvertTo-Json -Depth 3
        
        $tasks | Out-File -FilePath "../$ResultsPath/persona-tasks.json" -Encoding UTF8
        
        # Create interventions.json
        $interventions = @{
            interventions = @()
            count = 0
            created_at = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssZ")
        } | ConvertTo-Json -Depth 3
        
        $interventions | Out-File -FilePath "../$ResultsPath/interventions.json" -Encoding UTF8
        
        Write-Host "✅ Benchmark environment created successfully!" -ForegroundColor Green
        Write-Host "Branch: $BranchName" -ForegroundColor Cyan
        Write-Host "Results: $ResultsPath" -ForegroundColor Cyan
        
    } finally {
        Pop-Location
    }
}

function Cleanup-BenchmarkBranches {
    Write-Host "Cleaning up benchmark branches..." -ForegroundColor Yellow
    
    Push-Location $OtterPath
    
    try {
        # List all benchmark branches
        $benchmarkBranches = git branch --list "benchmark-otter-*"
        
        if (-not $benchmarkBranches) {
            Write-Host "No benchmark branches found." -ForegroundColor Green
            return
        }
        
        Write-Host "Found benchmark branches:" -ForegroundColor Cyan
        $benchmarkBranches | ForEach-Object { Write-Host "  $_" }
        
        if ($Force) {
            # Delete all benchmark branches
            $benchmarkBranches | ForEach-Object {
                $branch = $_.Trim().Replace("* ", "")
                if ($branch -ne (git branch --show-current)) {
                    git branch -D $branch
                    Write-Host "Deleted: $branch" -ForegroundColor Red
                }
            }
        } else {
            Write-Host "Use -Force to delete these branches" -ForegroundColor Yellow
        }
        
    } finally {
        Pop-Location
    }
}

function List-BenchmarkBranches {
    Write-Host "Listing benchmark branches..." -ForegroundColor Cyan
    
    Push-Location $OtterPath
    
    try {
        $benchmarkBranches = git branch --list "benchmark-otter-*"
        $currentBranch = git branch --show-current
        
        if (-not $benchmarkBranches) {
            Write-Host "No benchmark branches found." -ForegroundColor Yellow
            return
        }
        
        Write-Host "Benchmark branches:" -ForegroundColor Green
        $benchmarkBranches | ForEach-Object {
            $branch = $_.Trim().Replace("* ", "")
            $marker = if ($branch -eq $currentBranch) { " (current)" } else { "" }
            Write-Host "  $branch$marker" -ForegroundColor $(if ($branch -eq $currentBranch) { "Green" } else { "White" })
        }
        
    } finally {
        Pop-Location
    }
}

function Switch-ToBenchmarkBranch {
    if (-not $BranchName) {
        Write-Error "Branch name is required for switch action"
        return
    }
    
    Write-Host "Switching to benchmark branch: $BranchName" -ForegroundColor Cyan
    
    Push-Location $OtterPath
    
    try {
        git checkout $BranchName
        Write-Host "✅ Switched to branch: $BranchName" -ForegroundColor Green
        
    } finally {
        Pop-Location
    }
}

# Main execution
Test-GitRepository

switch ($Action) {
    "create" { Create-BenchmarkBranch }
    "cleanup" { Cleanup-BenchmarkBranches }
    "list" { List-BenchmarkBranches }
    "switch" { Switch-ToBenchmarkBranch }
}
