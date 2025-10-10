#!/bin/bash
# Task 0.1: Git Branch Setup (Linux/Mac/WSL)
# Creates migration workflow branches and baseline tag
# Usage: ./create-branches.sh [-f|--force]

set -e

# Parse arguments
FORCE=false
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--force)
            FORCE=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [-f|--force]"
            exit 1
            ;;
    esac
done

echo "=== Task 0.1: Git Branch Setup ==="
if [ "$FORCE" = true ]; then
    echo "Force mode enabled - will delete and recreate existing branches/tags"
fi

# Git configuration
BASELINE_TAG="baseline-before-migration"
BACKUP_BRANCH="backup/pre-migration"
MIGRATION_BRANCH="migration/java-upgrade"

# Check if we're in a git repository
echo ""
echo "Checking Git repository..."

if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "ERROR: Not a git repository"
    echo "Please run 'git init' first or run this script from within a git repository"
    exit 1
fi

echo "  ✓ Git repository detected"

# Check for uncommitted changes
echo ""
echo "Checking for uncommitted changes..."

if ! git diff-index --quiet HEAD -- 2>/dev/null; then
    echo "  ⚠ WARNING: Uncommitted changes detected"
    echo ""
    git status --short
    echo ""
    echo "It's recommended to commit all changes before creating migration branches."
    
    if [ "$FORCE" = false ]; then
        read -p "Continue anyway? (y/N): " response
        if [[ ! "$response" =~ ^[Yy]$ ]]; then
            echo "Aborted. Please commit your changes first."
            exit 1
        fi
    else
        echo "Force mode enabled - continuing with uncommitted changes"
    fi
else
    echo "  ✓ Working directory clean"
fi

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
echo ""
echo "Current branch: $CURRENT_BRANCH"

# Create baseline tag
echo ""
echo "Creating baseline tag..."

if git tag -l | grep -q "^${BASELINE_TAG}$"; then
    if [ "$FORCE" = true ]; then
        echo "  Deleting existing tag '$BASELINE_TAG'..."
        git tag -d "$BASELINE_TAG" > /dev/null
    else
        echo "  SKIP: Tag '$BASELINE_TAG' already exists (use -f to recreate)"
    fi
fi

if [ "$FORCE" = true ] || ! git tag -l | grep -q "^${BASELINE_TAG}$"; then
    if git tag -a "$BASELINE_TAG" -m "Starting point before Java/Spring Boot migration" 2>/dev/null; then
        echo "  ✓ Created tag: $BASELINE_TAG"
    else
        echo "  ERROR: Failed to create tag"
        exit 1
    fi
fi

# Create backup branch
echo ""
echo "Creating backup branch..."

if git branch --list | grep -q "^[* ]*${BACKUP_BRANCH}$"; then
    if [ "$FORCE" = true ]; then
        echo "  Deleting existing branch '$BACKUP_BRANCH'..."
        git branch -D "$BACKUP_BRANCH" > /dev/null
    else
        echo "  SKIP: Branch '$BACKUP_BRANCH' already exists (use -f to recreate)"
    fi
fi

if [ "$FORCE" = true ] || ! git branch --list | grep -q "^[* ]*${BACKUP_BRANCH}$"; then
    if git branch "$BACKUP_BRANCH" > /dev/null 2>&1; then
        echo "  ✓ Created branch: $BACKUP_BRANCH"
    else
        echo "  ERROR: Failed to create backup branch"
        exit 1
    fi
fi

# Create and checkout migration branch
echo ""
echo "Creating migration branch..."

MIGRATION_EXISTS=false
if git branch --list | grep -q "^[* ]*${MIGRATION_BRANCH}$"; then
    MIGRATION_EXISTS=true
fi

if [ "$MIGRATION_EXISTS" = true ]; then
    if [ "$FORCE" = true ]; then
        echo "  Deleting existing branch '$MIGRATION_BRANCH'..."
        # Switch to a different branch first if we're on the migration branch
        CURRENT_BRANCH=$(git branch --show-current)
        if [ "$CURRENT_BRANCH" = "$MIGRATION_BRANCH" ]; then
            git checkout "$BACKUP_BRANCH" > /dev/null
        fi
        git branch -D "$MIGRATION_BRANCH" > /dev/null
        MIGRATION_EXISTS=false
    else
        echo "  SKIP: Branch '$MIGRATION_BRANCH' already exists (use -f to recreate)"
        # Check it out if it exists
        CURRENT_BRANCH=$(git branch --show-current)
        if [ "$CURRENT_BRANCH" != "$MIGRATION_BRANCH" ]; then
            echo "  Checking out existing branch..."
            git checkout "$MIGRATION_BRANCH" > /dev/null
        fi
    fi
fi

if [ "$MIGRATION_EXISTS" = false ] || [ "$FORCE" = true ]; then
    if git checkout -b "$MIGRATION_BRANCH" > /dev/null 2>&1; then
        echo "  ✓ Created and checked out branch: $MIGRATION_BRANCH"
    else
        echo "  ERROR: Failed to create migration branch"
        exit 1
    fi
fi

# Display summary
echo ""
echo "=== Git Workflow Setup Complete ==="
echo ""
echo "Created Git Structure:"
echo "  Tag:              $BASELINE_TAG"
echo "  Backup branch:    $BACKUP_BRANCH"
echo "  Migration branch: $MIGRATION_BRANCH"
echo ""

CURRENT_BRANCH=$(git branch --show-current)
echo "Current branch:     $CURRENT_BRANCH"
echo ""

# Show all branches
echo "All branches:"
git branch -a | sed 's/^/  /'
echo ""

# Show all tags
echo "All tags:"
git tag -l | sed 's/^/  /'
echo ""

echo "Next Steps:"
echo "  1. All migration work will happen on branch: $MIGRATION_BRANCH"
echo "  2. Original state preserved in: $BACKUP_BRANCH"
echo "  3. Rollback point marked as: $BASELINE_TAG"
echo ""
echo "Optional: Push branches and tags to remote:"
echo "  git push origin $MIGRATION_BRANCH"
echo "  git push origin $BACKUP_BRANCH"
echo "  git push origin $BASELINE_TAG"

exit 0
