# Task 0.1: Git Branch Setup (Windows)
# Creates migration workflow branches and baseline tag
# Usage: .\create-branches.ps1 [-Force]

param(
    [switch]$Force
)

$ErrorActionPreference = "Stop"

Write-Host "=== Task 0.1: Git Branch Setup ===" -ForegroundColor Cyan
if ($Force) {
    Write-Host "Force mode enabled - will delete and recreate existing branches/tags" -ForegroundColor Yellow
}

# Git configuration
$BASELINE_TAG = "baseline-before-migration"
$BACKUP_BRANCH = "backup/pre-migration"
$MIGRATION_BRANCH = "migration/java-upgrade"

# Check if we're in a git repository
Write-Host ""
Write-Host "Checking Git repository..." -ForegroundColor Yellow

$gitCheck = git rev-parse --git-dir 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Not a git repository" -ForegroundColor Red
    Write-Host "Please run 'git init' first or run this script from within a git repository" -ForegroundColor Yellow
    exit 1
}

Write-Host "  ✓ Git repository detected" -ForegroundColor Green

# Check for uncommitted changes
Write-Host ""
Write-Host "Checking for uncommitted changes..." -ForegroundColor Yellow

$status = git status --porcelain 2>&1
if ($status) {
    Write-Host "  ⚠ WARNING: Uncommitted changes detected" -ForegroundColor Yellow
    Write-Host ""
    git status --short
    Write-Host ""
    Write-Host "It's recommended to commit all changes before creating migration branches." -ForegroundColor Yellow
    
    if (-not $Force) {
        $response = Read-Host "Continue anyway? (y/N)"
        if ($response -ne 'y' -and $response -ne 'Y') {
            Write-Host "Aborted. Please commit your changes first." -ForegroundColor Yellow
            exit 1
        }
    } else {
        Write-Host "Force mode enabled - continuing with uncommitted changes" -ForegroundColor Yellow
    }
} else {
    Write-Host "  ✓ Working directory clean" -ForegroundColor Green
}

# Get current branch
$currentBranch = git branch --show-current
Write-Host ""
Write-Host "Current branch: $currentBranch" -ForegroundColor Cyan

# Create baseline tag
Write-Host ""
Write-Host "Creating baseline tag..." -ForegroundColor Yellow

$tagExists = git tag -l $BASELINE_TAG
if ($tagExists) {
    if ($Force) {
        Write-Host "  Deleting existing tag '$BASELINE_TAG'..." -ForegroundColor Yellow
        git tag -d $BASELINE_TAG | Out-Null
    } else {
        Write-Host "  SKIP: Tag '$BASELINE_TAG' already exists (use -Force to recreate)" -ForegroundColor Cyan
    }
}

if (-not $tagExists -or $Force) {
    git tag -a $BASELINE_TAG -m "Starting point before Java/Spring Boot migration" 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Created tag: $BASELINE_TAG" -ForegroundColor Green
    } else {
        Write-Host "  ERROR: Failed to create tag" -ForegroundColor Red
        exit 1
    }
}

# Create backup branch
Write-Host ""
Write-Host "Creating backup branch..." -ForegroundColor Yellow

$backupExists = git branch --list $BACKUP_BRANCH
if ($backupExists) {
    if ($Force) {
        Write-Host "  Deleting existing branch '$BACKUP_BRANCH'..." -ForegroundColor Yellow
        git branch -D $BACKUP_BRANCH | Out-Null
    } else {
        Write-Host "  SKIP: Branch '$BACKUP_BRANCH' already exists (use -Force to recreate)" -ForegroundColor Cyan
    }
}

if (-not $backupExists -or $Force) {
    git branch $BACKUP_BRANCH 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Created branch: $BACKUP_BRANCH" -ForegroundColor Green
    } else {
        Write-Host "  ERROR: Failed to create backup branch" -ForegroundColor Red
        exit 1
    }
}

# Create and checkout migration branch
Write-Host ""
Write-Host "Creating migration branch..." -ForegroundColor Yellow

$migrationExists = git branch --list $MIGRATION_BRANCH
if ($migrationExists) {
    if ($Force) {
        Write-Host "  Deleting existing branch '$MIGRATION_BRANCH'..." -ForegroundColor Yellow
        # Switch to a different branch first if we're on the migration branch
        $currentBranch = git branch --show-current
        if ($currentBranch -eq $MIGRATION_BRANCH) {
            git checkout $BACKUP_BRANCH | Out-Null
        }
        git branch -D $MIGRATION_BRANCH | Out-Null
    } else {
        Write-Host "  SKIP: Branch '$MIGRATION_BRANCH' already exists (use -Force to recreate)" -ForegroundColor Cyan
        # Check it out if it exists
        $currentBranch = git branch --show-current
        if ($currentBranch -ne $MIGRATION_BRANCH) {
            Write-Host "  Checking out existing branch..." -ForegroundColor Yellow
            git checkout $MIGRATION_BRANCH | Out-Null
        }
    }
}

if (-not $migrationExists -or $Force) {
    git checkout -b $MIGRATION_BRANCH 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Created and checked out branch: $MIGRATION_BRANCH" -ForegroundColor Green
    } else {
        Write-Host "  ERROR: Failed to create migration branch" -ForegroundColor Red
        exit 1
    }
}

# Display summary
Write-Host ""
Write-Host "=== Git Workflow Setup Complete ===" -ForegroundColor Green
Write-Host ""
Write-Host "Created Git Structure:" -ForegroundColor Cyan
Write-Host "  Tag:              $BASELINE_TAG" -ForegroundColor White
Write-Host "  Backup branch:    $BACKUP_BRANCH" -ForegroundColor White
Write-Host "  Migration branch: $MIGRATION_BRANCH" -ForegroundColor White
Write-Host ""

$currentBranch = git branch --show-current
Write-Host "Current branch:     $currentBranch" -ForegroundColor Green
Write-Host ""

# Show all branches
Write-Host "All branches:" -ForegroundColor Cyan
git branch -a | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
Write-Host ""

# Show all tags
Write-Host "All tags:" -ForegroundColor Cyan
git tag -l | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
Write-Host ""

Write-Host "Next Steps:" -ForegroundColor Yellow
Write-Host "  1. All migration work will happen on branch: $MIGRATION_BRANCH" -ForegroundColor White
Write-Host "  2. Original state preserved in: $BACKUP_BRANCH" -ForegroundColor White
Write-Host "  3. Rollback point marked as: $BASELINE_TAG" -ForegroundColor White
Write-Host ""
Write-Host "Optional: Push branches and tags to remote:" -ForegroundColor Yellow
Write-Host "  git push origin $MIGRATION_BRANCH" -ForegroundColor Gray
Write-Host "  git push origin $BACKUP_BRANCH" -ForegroundColor Gray
Write-Host "  git push origin $BASELINE_TAG" -ForegroundColor Gray

exit 0
