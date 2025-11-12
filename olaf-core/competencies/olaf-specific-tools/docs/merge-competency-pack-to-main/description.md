# Merge Competency Pack to Main - Description

## Overview
The **Merge Competency Pack to Main** competency automates the safe migration of competency packs from the `feature/olaf-feature-system` branch to the `main` branch through a controlled Pull Request workflow.

## Purpose
OLAF maintains an extensive feature branch (`feature/olaf-feature-system`) with many competency packs that need selective integration into `main`. This competency orchestrates the entire process:
- Branch management
- Selective cherry-picking of competency folders
- Collection updates
- Index regeneration
- PR creation

## Key Capabilities

### 1. Branch Orchestration
- Creates clean integration branches from `main`
- Ensures proper git hygiene
- Manages branch naming conventions

### 2. Selective Integration
- Cherry-picks specific competency pack folders
- Avoids bringing unrelated changes
- Maintains clean git history

### 3. Framework Integration
- Updates `competency-collections.json` with new competency
- Regenerates `query-competency-index.md`
- Syncs command files to `.github/prompts/` and `.windsurf/workflows/`

### 4. Validation
- Verifies pack structure after cherry-pick
- Validates JSON syntax in collections
- Confirms index regeneration success

### 5. PR Automation
- Generates proper commit messages
- Pushes integration branch
- Provides ready-to-use PR URL

## When to Use

Use this competency when you need to:
- ✅ Move a completed competency pack from feature branch to main
- ✅ Make a feature-branch competency available in production
- ✅ Selectively integrate specific capabilities from the feature system
- ✅ Create a clean, reviewable PR for competency additions

Do NOT use when:
- ❌ Creating a new competency from scratch (use `create-competency-pack` instead)
- ❌ Making changes to existing competencies on main
- ❌ Merging the entire feature branch to main

## Workflow Summary

```
main branch → Create integration branch → Cherry-pick competency pack
    ↓
Update collections.json → Regenerate index → Commit & Push
    ↓
Generate PR URL → Review → Merge → Cleanup
```

## Benefits

1. **Safety**: Uses dedicated integration branches for PR review
2. **Selectivity**: Only brings the specific competency needed
3. **Automation**: Handles all integration steps automatically
4. **Traceability**: Generates proper commit messages and PR links
5. **Validation**: Ensures framework consistency after integration

## Prerequisites

- Access to both `main` and `feature/olaf-feature-system` branches
- Python environment configured (for index regeneration)
- Git credentials set up
- Understanding of which competency pack to merge

## Output

The competency provides:
- Integration branch with all changes
- Updated collections and index files
- Synced command files
- PR creation URL
- Summary report of all changes

## Related Competencies

- `create-competency-pack`: For creating new competencies
- `validate-olaf-artifacts`: For validating the merged pack
- `verify-competency-compliance`: For checking standards compliance
- Git-assistant competencies: For general git operations

## Example Scenario

**Scenario**: You want to add the `pdf-analysis` competency pack to main.

**Process**:
1. Invoke: `/olaf-merge-competency-pack-to-main`
2. Specify: Pack = "pdf-analysis", Collection = "all"
3. Agent creates branch `feat/add-pdf-analysis-pack`
4. Cherry-picks `olaf-core/competencies/pdf-analysis/`
5. Updates collections to include "pdf-analysis"
6. Regenerates index with new entry points
7. Commits and pushes
8. Provides PR URL for review

**Result**: Clean PR ready for review and merge.
