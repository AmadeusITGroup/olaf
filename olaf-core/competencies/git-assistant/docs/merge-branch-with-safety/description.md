# Merge Branch with Safety

## Overview

Performs safe branch merging with comprehensive validation, automatic tagging for rollback capability, and dry-run conflict detection. This competency ensures merge operations are safe, auditable, and reversible through a 4-tag safety system.

## Purpose

Branch merging is a critical and potentially destructive git operation. Mistakes can corrupt branch history or lose work. This competency solves the problem by:
- Validating branches exist before attempting merge
- Running dry-run merge to detect conflicts before execution
- Creating automatic safety tags for rollback capability
- Providing detailed merge analysis and impact assessment
- Maintaining complete audit trail through timestamped tags
- Offering clear rollback instructions if issues occur

## Usage

**Command**: `merge branch safely` (or aliases: `merge branch`, `safe merge`, `merge with tags`, `dry run merge`, `merge safely`, `merge branches`, `branch merge`, `git merge`)

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this whenever you need to merge branches, especially for important merges like feature branches to main, release branches, or integration branch updates. Essential for teams that need merge auditability and rollback capability.

## Parameters

### Required Inputs
- **source_branch**: Branch to merge FROM (the branch containing changes)
- **target_branch**: Branch to merge INTO (the branch receiving changes)

### Optional Inputs
- **merge_strategy**: "merge" or "squash" (default: "merge")
- **auto_push**: Automatically push after successful merge (default: false)
- **tag_prefix**: Custom prefix for tags (default: "merge")

### Context Requirements
- Valid git repository
- Clean working directory (no uncommitted changes)
- Both source and target branches must exist (or target can be created)
- No ongoing merge operations
- Commit and tag permissions on repository
- Not in detached HEAD state

## Output

**Deliverables**:
- Dry-run merge analysis report with conflict detection
- Four timestamped safety tags (2 before merge, 2 after)
- Successful merge commit on target branch
- Detailed rollback instructions
- Optional push to remote repository

**Format**: 
- Markdown analysis report with merge statistics
- Git tags: `{prefix}/before-merge-from-{source}-{timestamp}` and 3 others
- Git merge commit with detailed message
- PowerShell rollback commands

## Examples

### Example 1: Merge Feature Branch to Main

**Scenario**: You've completed a feature branch and want to safely merge it to main with full rollback capability.

**Command**:
```
olaf merge branch safely
```

**Interactive Flow**:
```
Source branch: feature/user-authentication
Target branch: main
Merge strategy: merge

[Dry-run analysis runs...]

Merge Safety Analysis:
✅ Merge Status: clean_merge
📊 Files Changed: 8
➕ Additions: 245 lines
➖ Deletions: 12 lines

Proposed Tags:
1. merge/before-merge-from-feature-user-authentication-20251027-1430
2. merge/start-merge-to-main-20251027-1430
3. merge/after-merge-from-feature-user-authentication-20251027-1430
4. merge/merge-to-main-completed-20251027-1430

Proceed with merge? yes
```

**Result**: 
- Feature branch successfully merged to main
- 4 safety tags created for audit trail
- Rollback instructions provided
- Clean merge commit in git history

### Example 2: Merge with Conflict Detection

**Scenario**: Attempting to merge a branch that has conflicts with target.

**Command**:
```
olaf merge branch safely
```

**Analysis Result**:
```
⚠️ CONFLICTS DETECTED:
- src/config/settings.js
- src/utils/helpers.js

Action Required: Resolve conflicts before proceeding

[Merge operation STOPPED]
```

**Result**: 
- Merge prevented before any changes made
- Conflict list provided for manual resolution
- No tags created (merge not executed)
- Working directory remains clean

### Example 3: Create Target Branch and Merge

**Scenario**: You want to merge to a branch that doesn't exist yet.

**Command**:
```
olaf merge branch safely
```

**Interactive Flow**:
```
Source branch: feature/new-api
Target branch: release/v2.0

⚠️ Target branch 'release/v2.0' does not exist

Would you like to create it?
1. Create from 'main' (default)
2. Create from another branch
3. Cancel merge operation

User: 1

[Target branch created from main]
[Dry-run analysis proceeds...]
[Merge executed with safety tags]
```

**Result**: 
- New release branch created from main
- Feature merged into new branch
- Full safety tag system applied

## Related Competencies

- **create-feature-for-pr**: Use this to create feature branches before merging
- **propose-commit-thread**: Use this to organize commits before merging
- **developer/review-code**: Use this to review changes before merge

## Tips & Best Practices

- Always review the dry-run analysis before confirming merge
- Keep the default "merge" strategy for preserving commit history
- Use "squash" strategy for cleaning up messy feature branch history
- Don't use auto_push until you've verified the merge locally
- Save the rollback instructions in case you need them later
- Use descriptive tag prefixes for different types of merges (e.g., "release", "hotfix")
- Verify the 4 tags were created successfully after merge
- Test merged code before pushing to remote
- Keep safety tags for at least a few days before cleanup

## Limitations

- Cannot automatically resolve merge conflicts (requires manual resolution)
- Source branch must exist (operation stops if missing)
- Requires clean working directory before starting
- Force push for rollback requires --force-with-lease (use with caution)
- Tag creation requires repository write permissions
- Dry-run creates temporary branch (requires branch creation permissions)
- Cannot merge if repository is in detached HEAD state
- GitHub-specific features assume standard GitHub repository structure
