# Merge Branch with Safety: Step-by-Step Tutorial

## How to Execute the "Safe Branch Merge with Automatic Tagging and Rollback Capability"

This tutorial shows exactly how to reproduce the safe branch merge workflow with dry-run validation, comprehensive tagging strategy, and built-in rollback mechanisms.

## Prerequisites

- Git installed and configured on your system
- Repository with source and target branches ready for merge
- Write permissions for commits and tag creation
- Clean working directory (no uncommitted changes)
- Understanding of merge strategy preferences (merge vs squash)

## Step-by-Step Instructions

### Step 1: Initiate Safe Merge Process

[This step starts the OLAF safe merge workflow with comprehensive validation]

**User Action:**

1. Invoke the merge-branch-with-safety competency in OLAF
2. Navigate to your repository with branches ready for merge
3. Ensure working directory is clean with no pending changes

**OLAF Response:**

You should see OLAF validate the repository state, check git availability, and verify working directory cleanliness before proceeding.

### Step 2: Provide Merge Configuration

**User Action:** Specify merge parameters when prompted

```bash
Source branch (merge FROM): [branch-name]
Target branch (merge INTO): [branch-name] 
Merge strategy (merge/squash): [your preference]
Auto-push after merge? (y/n): [recommended: no]
Tag prefix (optional): [custom-prefix or default: "merge"]
```

**Provide Merge Configuration:**

- **Source Branch**: Branch containing changes to merge (must exist)
- **Target Branch**: Branch receiving the merge (will be created if doesn't exist)
- **Merge Strategy**: "merge" for full history preservation, "squash" for single commit
- **Auto Push**: Enable to automatically push after successful merge
- **Tag Prefix**: Custom prefix for safety tags (default: "merge")

### Step 3: Branch Existence Validation

**What OLAF Does:**

- Verifies source branch exists (local or remote)
- Checks if target branch exists
- **If source branch missing**: STOPS execution, lists available branches
- **If target branch missing**: Proposes creation with base branch selection

**Branch Creation Proposal (if needed):**

```markdown
⚠️ **Target branch 'feature-target' does not exist**

Would you like to create it?

**Options:**
1. **Create from 'main'** (default)
2. **Create from another branch** (specify which one)
3. **Cancel merge operation**

What would you like to do? (1/2/3 or specify base branch name)
```

**You Should See:** Either confirmation that both branches exist, or a creation proposal for missing target branch

### Step 4: Dry-Run Merge Analysis

**What OLAF Does:**

- Creates temporary test branch: `test-merge-dry-run-[timestamp]`
- Attempts merge without commit: `git merge --no-commit --no-ff [source_branch]`
- Analyzes merge results for conflicts and statistics
- Cleans up test environment (aborts merge, deletes test branch)

**Conflict Detection Process:**

```powershell
# Test merge execution
git checkout -b test-merge-dry-run-20241027-1045 target-branch
git merge --no-commit --no-ff source-branch

# Analyze results
git status --porcelain | Select-String "^UU|^AA|^DD"  # Check conflicts
git diff --cached --stat                              # Get statistics

# Cleanup
git merge --abort
git checkout original-branch  
git branch -D test-merge-dry-run-20241027-1045
```

**You Should See:** Comprehensive analysis showing merge feasibility, file changes, and conflict detection

### Step 5: Safety Analysis Proposal

**User Action:** Review detailed merge proposal with safety mechanisms

```markdown
# 🔀 Merge Safety Analysis - 20241027-1045

## Branches
**Source Branch**: feature-authentication
**Target Branch**: main
**Merge Strategy**: merge

## Dry-Run Results  
✅ **Merge Status**: clean_merge
📊 **Files Changed**: 8
➕ **Additions**: 245 lines
➖ **Deletions**: 12 lines

## Proposed Tag Strategy

### Before Merge
1. **Target Branch Tag**: `merge/before-merge-from-feature-authentication-20241027-1045`
   - Branch: main
   - Purpose: Rollback point for target branch
   
2. **Source Branch Tag**: `merge/start-merge-to-main-20241027-1045`  
   - Branch: feature-authentication
   - Purpose: Mark source state at merge start

### After Successful Merge
3. **Target Branch Tag**: `merge/after-merge-from-feature-authentication-20241027-1045`
   - Branch: main  
   - Purpose: Mark successful merge completion on target
   
4. **Source Branch Tag**: `merge/merge-to-main-completed-20241027-1045`
   - Branch: feature-authentication
   - Purpose: Mark merge completion on source

## Execution Plan
- Step 1: Create pre-merge safety tags
- Step 2: Execute merge using specified strategy
- Step 3: Create post-merge completion tags
- Step 4: Optional push to origin

## Rollback Instructions
If issues occur after merge:
```powershell
git checkout main
git reset --hard merge/before-merge-from-feature-authentication-20241027-1045
git push origin main --force-with-lease  # If already pushed
```

## 🎮 User Decision
**Proceed with merge?** (yes/no)
```

**Critical Review Points:**

- Verify merge status is "clean_merge" (no conflicts)
- Review file change statistics for expected scope
- Understand the 4-tag safety strategy for complete rollback capability
- Note the specific rollback commands for emergency recovery

### Step 6: User Confirmation and Execution

**User Action:** Provide explicit confirmation to proceed

```bash
yes
```

**What OLAF Does (ONLY after confirmation and zero conflicts):**

1. **Pre-Merge Tagging:**
   - Tag target branch: `[prefix]/before-merge-from-[source]-[timestamp]`
   - Tag source branch: `[prefix]/start-merge-to-[target]-[timestamp]`

2. **Execute Merge:**
   - Switch to target branch
   - Execute merge based on strategy (merge/squash)
   - Verify merge success

3. **Post-Merge Tagging:**
   - Tag target branch: `[prefix]/after-merge-from-[source]-[timestamp]`  
   - Tag source branch: `[prefix]/merge-to-[target]-completed-[timestamp]`

4. **Optional Push:**
   - Push target branch if auto_push enabled
   - Push all tags to origin

**You Should See:** Step-by-step execution with confirmation of each tag creation and successful merge completion

### Step 7: Validation and Completion

**What OLAF Does:**

- Lists all 4 created tags with `git tag -l "[prefix]/*[timestamp]"`
- Verifies merge commit exists with `git log -1 --oneline`
- Checks branch history includes source branch commits
- Confirms working directory is clean after merge

**Completion Summary:**

```markdown
## Execution Summary

### Tags Created Successfully
✅ merge/before-merge-from-feature-auth-20241027-1045 (main)
✅ merge/start-merge-to-main-20241027-1045 (feature-auth)  
✅ merge/after-merge-from-feature-auth-20241027-1045 (main)
✅ merge/merge-to-main-completed-20241027-1045 (feature-auth)

### Merge Details
- **Merge Commit SHA**: abc123def456
- **Message**: "Merge branch 'feature-auth' into main"
- **Files Changed**: 8 files, 245 insertions, 12 deletions
- **Push Status**: Completed (if auto_push enabled)

### Emergency Rollback
git checkout main
git reset --hard merge/before-merge-from-feature-auth-20241027-1045
```

## Verification Checklist

✅ **Source branch existed** (validation passed before merge)

✅ **Target branch ready** (existing or created from appropriate base)

✅ **Dry-run completed** (no conflicts detected in test merge)

✅ **All 4 tags created** (2 before merge, 2 after merge with timestamp)

✅ **Merge executed successfully** (commit exists in git log)

✅ **Working directory clean** (no remaining uncommitted changes)

✅ **Rollback instructions available** (specific commands for emergency recovery)

## Troubleshooting

**If source branch does not exist:**

```bash
❌ Source branch 'feature-xyz' does not exist
```

- OLAF stops execution immediately
- Review available branches with `git branch -a`
- Verify branch name spelling and try again

**If merge conflicts detected in dry-run:**

```bash
⚠️ **CONFLICTS DETECTED**:
- src/main.js
- config/settings.json
```

- OLAF stops execution and requires manual resolution
- Resolve conflicts using `git mergetool` or editor
- Re-run competency after conflicts are resolved

**If tag creation fails:**

- Check repository permissions for tag creation
- Verify no existing tags with same names
- Ensure adequate disk space and git repository health

**If merge command fails:**

- OLAF executes `git merge --abort` automatically
- Pre-merge tags are preserved for analysis
- Check git error messages for specific issues

## Key Learning Points

1. **Comprehensive Safety Net:** 4-tag strategy provides complete rollback capability for any merge scenario
2. **Dry-Run Validation:** Test merge prevents conflicts and validates feasibility before execution
3. **Atomic Operations:** Each step must succeed before proceeding, preventing partial merge states
4. **Audit Trail:** Timestamped tags provide detailed history of merge operations for troubleshooting

## Next Steps to Try

- Verify merge results by testing functionality in target branch
- Push changes to remote repository if not auto-pushed
- Clean up source branch after confirming merge success
- Use rollback commands if issues discovered after merge

## Expected Timeline

- **Total merge time:** 2-5 minutes
- **User input required:** Merge configuration, branch creation decisions, final execution approval
- **OLAF execution time:** Branch validation, dry-run analysis, tag creation, merge execution with safety checks