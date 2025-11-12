---
name: Merge Competency Pack to Main
description: Orchestrates the process of merging a competency pack from feature/olaf-feature-system to main branch through a proper PR workflow
tags: ["git-workflow", "competency-pack", "merge", "pr-creation", "olaf-internal"]
role: orchestrator
version: 1.0.0
created: 2025-11-12
updated: 2025-11-12
author: OLAF Framework
category: olaf-internal
llm: Claude Sonnet 4.5+
---

# Merge Competency Pack to Main

## Purpose
Automate the safe migration of a competency pack from the `feature/olaf-feature-system` branch to `main` through a controlled PR workflow, ensuring proper integration with collections, reindexing, and validation.

## Context
The OLAF framework maintains competency packs on the `feature/olaf-feature-system` branch that need to be selectively merged to `main`. This requires:
1. Creating a clean integration branch from main
2. Cherry-picking specific competency pack from feature branch
3. Updating competency collections
4. Regenerating the competency index
5. Creating a PR for review

## Prerequisites
- Repository is `genai.olaf` (Amadeus-xDLC)
- You have both `main` and `feature/olaf-feature-system` branches available
- Python environment is configured (for reindexing)
- Git credentials are configured

## Process

### STEP 1: Gather Requirements
Ask the user to specify:
- **Competency pack name** to merge (e.g., "pdf-analysis", "onboard", "straf")
- **Target collection(s)** to add it to (e.g., "all", "developer", etc.)
- **Branch name** for the PR (suggest: `feat/add-{competency-name}-pack`)

### STEP 2: Create Integration Branch
```bash
# Ensure we're on main and up to date
git checkout main
git pull origin main

# Create new integration branch
git checkout -b feat/add-{competency-name}-pack
```

### STEP 3: Cherry-Pick Competency Pack
```bash
# Get the competency pack folder from feature branch
git checkout feature/olaf-feature-system -- olaf-core/competencies/{competency-name}
```

Verify the pack was copied:
```bash
ls olaf-core/competencies/{competency-name}
```

### STEP 4: Update Competency Collections
Edit `olaf-core/reference/competency-collections.json`:

1. Read current collections
2. Add the competency ID to the specified collection(s)
3. Ensure alphabetical ordering within each collection
4. Validate JSON syntax

Example:
```json
{
  "all": [
    "business-analyst",
    "common",
    "developer",
    "git-assistant",
    "{new-competency-name}",  // <-- Add here
    "prompt-engineer",
    "project-manager"
  ]
}
```

### STEP 5: Regenerate Competency Index
Run the collection selection script to regenerate the index:

```bash
python .\olaf-core\competencies\prompt-engineer\scripts\select_collection.py --collection all
```

This will:
- Update `olaf-core/reference/query-competency-index.md`
- Sync `/olaf-*` command files to `.github/prompts/` and `.windsurf/workflows/`

### STEP 6: Validate Changes
Check what was modified:
```bash
git status
git diff olaf-core/reference/competency-collections.json
git diff olaf-core/reference/query-competency-index.md
```

Verify:
- ✅ Competency pack folder copied
- ✅ Collections JSON updated
- ✅ Index regenerated
- ✅ Command files synced

### STEP 7: Commit and Push
```bash
# Stage all changes
git add olaf-core/competencies/{competency-name}
git add olaf-core/reference/competency-collections.json
git add olaf-core/reference/query-competency-index.md
git add .github/prompts/
git add .windsurf/workflows/

# Commit with descriptive message
git commit -m "feat: add {competency-name} competency pack

- Copy {competency-name} competency from feature/olaf-feature-system
- Add to collections: {collection-names}
- Regenerate competency index
- Sync /olaf-* command files"

# Push to remote
git push -u origin feat/add-{competency-name}-pack
```

### STEP 8: Generate PR URL
Provide the user with the PR creation URL:

```
https://github.com/Amadeus-xDLC/genai.olaf/compare/main...feat/add-{competency-name}-pack?expand=1
```

## Output Format

Provide a summary report:

```markdown
## Competency Pack Merge Summary

**Pack**: {competency-name}
**Branch**: feat/add-{competency-name}-pack
**Collections Updated**: {collection-list}

### Files Modified:
- ✅ olaf-core/competencies/{competency-name}/ (copied)
- ✅ olaf-core/reference/competency-collections.json
- ✅ olaf-core/reference/query-competency-index.md
- ✅ .github/prompts/ ({n} files synced)
- ✅ .windsurf/workflows/ ({n} files synced)

### Competency Index:
- Entry Points: {count}
- Total Competencies: {count}

### Next Steps:
1. Open PR: https://github.com/Amadeus-xDLC/genai.olaf/compare/main...feat/add-{competency-name}-pack?expand=1
2. Review changes in GitHub
3. Merge PR after approval
4. Delete integration branch after merge
```

## Error Handling

### Competency Pack Not Found
If the pack doesn't exist on feature branch:
```bash
git ls-tree -r --name-only feature/olaf-feature-system | grep "olaf-core/competencies/{name}"
```

List available packs:
```bash
git ls-tree -d --name-only feature/olaf-feature-system:olaf-core/competencies/
```

### Merge Conflicts
If conflicts occur during cherry-pick:
1. Review conflicting files
2. Manually resolve conflicts
3. Continue with `git add` and commit

### Reindex Failures
If Python script fails:
1. Check Python environment is activated
2. Verify script path exists
3. Check for JSON syntax errors in collections.json
4. Re-run with error output for debugging

## Best Practices

1. **One Pack Per PR**: Merge one competency pack at a time for clean review
2. **Descriptive Naming**: Use `feat/add-{pack-name}-pack` convention
3. **Validate Before Push**: Always check `git status` and `git diff` before pushing
4. **Test Locally**: If possible, test the competency pack locally before creating PR
5. **Update Documentation**: If the pack is significant, update root README.md

## Related Commands
- `/olaf-validate-olaf-artifacts` - Validate pack structure before merge
- `/olaf-verify-competency-compliance` - Check compliance with OLAF standards
- `/olaf-git-create-branch` - Alternative branch creation
- `/olaf-git-commit-changes` - Alternative commit workflow

## Automation Command
To invoke this workflow:
```
/olaf-merge-competency-pack-to-main
```

---
**Note**: This is an orchestrator prompt that coordinates multiple git operations, file modifications, and validation steps. Always review changes before pushing to remote.
