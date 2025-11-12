---

name: merge-branch-with-safety

description: Perform safe branch merge with dry-run validation, automatic tagging, and rollback capability

tags: [git, merge, safety, tags, dry-run, workflow]

---



## Framework Validation
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.- <olaf-interaction-protocols> - Appropriate execution protocol

You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

You MUST request these parameters if not provided by the user:

- **source_branch**: string - Branch to merge FROM (REQUIRED)

- **target_branch**: string - Branch to merge INTO (REQUIRED)

- **merge_strategy**: string - "merge" or "squash" (OPTIONAL, default: "merge")

- **auto_push**: boolean - Automatically push after successful merge (OPTIONAL, default: false)

- **tag_prefix**: string - Custom prefix for tags (OPTIONAL, default: "merge")



## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Use **Propose-Confirm-Act** protocol for merge execution due to permanent repository impact



## Process



### 1. Validation Phase



#### 1.1 Basic Repository Validation

You WILL verify basic requirements:

- Confirm repository is a valid git repository

- Verify git is available and functional

- Ensure working directory is clean (no uncommitted changes)

- Confirm no merge conflicts exist in working directory

- Validate user has commit and tag permissions

- Check if repository is in detached HEAD state



**Basic Validation Commands**:

```powershell

# Check git availability

git --version



# Check working directory status

git status --porcelain



# Verify no ongoing merge

Test-Path .git/MERGE_HEAD

```



#### 1.2 Branch Existence Validation



**Source Branch Check**:

```powershell

# Check if source branch exists (local or remote)

$sourceBranchExists = git branch --list $source_branch

if (-not $sourceBranchExists) {

    $sourceBranchExists = git branch -r --list "origin/$source_branch"

}

```



**If source branch does NOT exist**:

- STOP execution immediately

- Display error message: "❌ Source branch '{source_branch}' does not exist"

- List available branches: `git branch -a`

- Ask user to verify branch name and try again

- DO NOT proceed with merge



**Target Branch Check**:

```powershell

# Check if target branch exists (local or remote)

$targetBranchExists = git branch --list $target_branch

if (-not $targetBranchExists) {

    $targetBranchExists = git branch -r --list "origin/$target_branch"

}

```



**If target branch does NOT exist**:

- Present creation proposal to user

- Ask user if they want to create the target branch

- If YES: Ask for base branch (default: 'main')

- If NO: STOP execution



**Target Branch Creation Proposal**:

```markdown

⚠️ **Target branch '{target_branch}' does not exist**



Would you like to create it?



**Options:**

1. **Create from 'main'** (default)

2. **Create from another branch** (specify which one)

3. **Cancel merge operation**



If you choose option 1 or 2, I will:

- Create branch: `git checkout -b {target_branch} {base_branch}`

- Then proceed with merge validation



**What would you like to do?** (1/2/3 or specify base branch name)

```



**If user chooses to create target branch**:

```powershell

# Get base branch (default to 'main' if not specified)

$base_branch = if ($user_specified_base) { $user_specified_base } else { "main" }



# Verify base branch exists

$baseBranchExists = git branch --list $base_branch

if (-not $baseBranchExists) {

    $baseBranchExists = git branch -r --list "origin/$base_branch"

}



if (-not $baseBranchExists) {

    Write-Error "Base branch '$base_branch' does not exist. Available branches:"

    git branch -a

    exit 1

}



# Create target branch from base

git checkout -b $target_branch $base_branch



# Confirm creation

git branch --list $target_branch

```



**Branch Validation Summary**:

After validation, you MUST have:

- ✅ Source branch exists (local or remote)

- ✅ Target branch exists (existing or newly created)

- ✅ Both branches are accessible



### 2. Dry-Run Merge Analysis Phase



**Create Test Branch**:

- Create temporary test branch from target: `git checkout -b test-merge-dry-run-{timestamp} {target_branch}`

- Attempt merge without commit: `git merge --no-commit --no-ff {source_branch}`

- Analyze merge results for conflicts

- Check merge statistics (files changed, additions, deletions)



**Conflict Detection**:

```powershell

# Attempt test merge

git merge --no-commit --no-ff $source_branch



# Check for conflicts

git status --porcelain | Select-String "^UU|^AA|^DD"



# Get merge statistics

git diff --cached --stat

```



**Cleanup Test Environment**:

- Abort test merge: `git merge --abort`

- Return to original branch: `git checkout {original_branch}`

- Delete test branch: `git branch -D test-merge-dry-run-{timestamp}`



### 3. Proposal Phase



**Merge Analysis Report**:

Present detailed proposal to user with dry-run results:



```markdown

# 🔀 Merge Safety Analysis - {timestamp}



## Branches

**Source Branch**: {source_branch}

**Target Branch**: {target_branch}

**Merge Strategy**: {merge_strategy}



## Dry-Run Results

✅ **Merge Status**: {clean_merge | has_conflicts}

📊 **Files Changed**: {file_count}

➕ **Additions**: {additions_count} lines

➖ **Deletions**: {deletions_count} lines



{if conflicts exist:}

⚠️ **CONFLICTS DETECTED**:

{list of conflicting files}



**Action Required**: Resolve conflicts before proceeding

{endif}



## Proposed Tag Strategy



### Before Merge

1. **Target Branch Tag**: `{tag_prefix}/before-merge-from-{source_branch}-{timestamp}`

   - Branch: {target_branch}

   - Purpose: Rollback point for target branch

   

2. **Source Branch Tag**: `{tag_prefix}/start-merge-to-{target_branch}-{timestamp}`

   - Branch: {source_branch}

   - Purpose: Mark source state at merge start



### After Successful Merge

3. **Target Branch Tag**: `{tag_prefix}/after-merge-from-{source_branch}-{timestamp}`

   - Branch: {target_branch}

   - Purpose: Mark successful merge completion on target

   

4. **Source Branch Tag**: `{tag_prefix}/merge-to-{target_branch}-completed-{timestamp}`

   - Branch: {source_branch}

   - Purpose: Mark merge completion on source



## Execution Plan



### Step 1: Pre-Merge Tagging

- Create safety tag on {target_branch}

- Create start tag on {source_branch}



### Step 2: Execute Merge

- Switch to {target_branch}

- Merge {source_branch} using {merge_strategy} strategy

- Verify merge success



### Step 3: Post-Merge Tagging

- Create completion tag on {target_branch}

- Switch to {source_branch}

- Create completion tag on {source_branch}



### Step 4: Push (Optional)

{if auto_push:}

- Push {target_branch} to origin

- Push all tags to origin

{else:}

- Manual push required after confirmation

{endif}



## Rollback Instructions

If issues occur after merge:

```powershell

# Rollback target branch to before-merge state

git checkout {target_branch}

git reset --hard {tag_prefix}/before-merge-from-{source_branch}-{timestamp}



# Force push if already pushed (CAUTION)

git push origin {target_branch} --force-with-lease

```



## 🎮 User Decision

**Proceed with merge?** (yes/no)

```



### 4. Confirmation Phase



**Wait for explicit user confirmation** before executing merge.

- If conflicts detected: STOP and require conflict resolution first

- If user declines: ABORT and provide exit message

- If user confirms: Proceed to execution phase



### 5. Execution Phase



**Execute ONLY after user confirmation and zero conflicts:**



#### Step 5.1: Pre-Merge Tagging

```powershell

# Get current timestamp

$timestamp = Get-Date -Format "yyyyMMdd-HHmm"



# Tag target branch (before merge)

git checkout $target_branch

git tag "${tag_prefix}/before-merge-from-${source_branch}-${timestamp}"



# Tag source branch (merge start)

git checkout $source_branch

git tag "${tag_prefix}/start-merge-to-${target_branch}-${timestamp}"



# Return to target branch for merge

git checkout $target_branch

```



#### Step 5.2: Execute Merge

```powershell

# Perform merge based on strategy

if ($merge_strategy -eq "squash") {

    git merge --squash $source_branch

    git commit -m "Merge branch '$source_branch' into $target_branch (squashed)"

} else {

    git merge --no-ff $source_branch -m "Merge branch '$source_branch' into $target_branch"

}



# Verify merge succeeded

if ($LASTEXITCODE -ne 0) {

    Write-Error "Merge failed! Rolling back..."

    git merge --abort

    exit 1

}

```



#### Step 5.3: Post-Merge Tagging

```powershell

# Tag target branch (after merge)

git tag "${tag_prefix}/after-merge-from-${source_branch}-${timestamp}"



# Tag source branch (merge completed)

git checkout $source_branch

git tag "${tag_prefix}/merge-to-${target_branch}-completed-${timestamp}"



# Return to target branch

git checkout $target_branch

```



#### Step 5.4: Optional Push

```powershell

if ($auto_push -eq $true) {

    # Push target branch

    git push origin $target_branch

    

    # Push all tags

    git push origin --tags

}

```



### 6. Validation Phase

You WILL validate execution results:

- Confirm merge commit exists in target branch

- Verify all 4 tags were created successfully

- Check git log shows proper merge commit

- Validate target branch history includes source branch commits

- Confirm working directory is clean after merge



**Validation Commands**:

```powershell

# List created tags

git tag -l "${tag_prefix}/*${timestamp}"



# Verify merge commit

git log -1 --oneline



# Check branch contains merge

git log --oneline --graph -10

```



## Output Format



### Analysis Report

- Dry-run merge results with conflict detection

- File change statistics and impact analysis

- Proposed tag naming with rollback instructions

- Clear proceed/abort recommendation



### Execution Summary

- Tag creation confirmation (4 tags with full names)

- Merge commit SHA and message

- Branch state before and after merge

- Push status if auto_push enabled

- Rollback commands for emergency recovery



## Domain-Specific Rules

You MUST follow these constraints:

- Rule 1: **NEVER execute merge if dry-run detects conflicts** - require resolution first

- Rule 2: **ALWAYS create all 4 tags** in the specified order (2 before, 2 after)

- Rule 3: **Create tags ONLY if previous step succeeds** - maintain atomic operation

- Rule 4: **NEVER force push** without explicit user request and warning

- Rule 5: Tag naming MUST include timestamp for uniqueness and auditability

- Rule 6: Return to target branch after completion for user convenience

- Rule 7: Preserve detailed audit trail through tags and commit messages



## Success Criteria

You WILL consider the task complete when:

- [ ] Repository validated as git repository with clean working directory

- [ ] Source branch existence confirmed (or operation stopped if missing)

- [ ] Target branch existence confirmed (or created with user approval)

- [ ] Dry-run merge executed successfully without conflicts

- [ ] User explicitly confirmed merge execution

- [ ] Target branch tagged before merge: `{tag_prefix}/before-merge-from-{source_branch}-{timestamp}`

- [ ] Source branch tagged at merge start: `{tag_prefix}/start-merge-to-{target_branch}-{timestamp}`

- [ ] Merge executed successfully on target branch

- [ ] Target branch tagged after merge: `{tag_prefix}/after-merge-from-{source_branch}-{timestamp}`

- [ ] Source branch tagged after merge: `{tag_prefix}/merge-to-{target_branch}-completed-{timestamp}`

- [ ] All 4 tags visible in `git tag` output

- [ ] Merge commit exists in git log with proper message

- [ ] Working directory clean after merge

- [ ] User provided with rollback instructions



## Required Actions

1. Validate git repository state and working directory cleanliness

2. Verify source branch exists (STOP if missing)

3. Verify target branch exists (propose creation if missing)

4. Create target branch from base if user approves

5. Execute dry-run merge in isolated test branch

6. Analyze merge results and detect any conflicts

7. Present comprehensive proposal with tag strategy and rollback plan

8. Wait for explicit user confirmation

9. Create pre-merge tags on both branches

10. Execute merge using specified strategy

11. Create post-merge tags on both branches

12. Optionally push changes and tags to origin



## Error Handling

You WILL handle these scenarios:

- **Source Branch Does Not Exist**: STOP immediately, list available branches with `git branch -a`, ask user to verify branch name

- **Target Branch Does Not Exist**: Propose creation with base branch selection (default: main), wait for user decision

- **Base Branch Does Not Exist** (for target creation): Display error, list available branches, request valid base branch

- **Merge Conflicts Detected**: STOP execution, provide conflict list, guide user to resolve manually

- **Working Directory Not Clean**: Require user to commit or stash changes before proceeding

- **Tag Creation Fails**: Abort merge operation, provide rollback to pre-merge state

- **Merge Command Fails**: Execute `git merge --abort`, preserve pre-merge tags for analysis

- **Push Fails** (if auto_push): Merge remains local, provide manual push commands

- **Permission Denied**: Check user has write access to repository and tag creation rights

- **Detached HEAD State**: Guide user to checkout proper branch before merge

- **Target Branch Creation Fails**: STOP execution, display git error, suggest manual branch creation



## Rollback Procedure

If merge needs to be undone after completion:



```powershell

# Reset target branch to before-merge state

git checkout {target_branch}

git reset --hard {tag_prefix}/before-merge-from-{source_branch}-{timestamp}



# If already pushed to remote

git push origin {target_branch} --force-with-lease



# Clean up post-merge tags (optional)

git tag -d {tag_prefix}/after-merge-from-{source_branch}-{timestamp}

git tag -d {tag_prefix}/merge-to-{target_branch}-completed-{timestamp}

git push origin :refs/tags/{tag_prefix}/after-merge-from-{source_branch}-{timestamp}

git push origin :refs/tags/{tag_prefix}/merge-to-{target_branch}-completed-{timestamp}

```



⚠️ **Critical Requirements**

- MANDATORY: Use Propose-Confirm-Act protocol for all merge executions

- MANDATORY: Verify source branch exists - STOP immediately if missing

- MANDATORY: Verify target branch exists - propose creation if missing

- MANDATORY: Execute dry-run merge before proposing actual merge

- MANDATORY: Create all 4 tags in correct order (2 before merge, 2 after)

- NEVER merge if conflicts exist - require manual resolution first

- NEVER skip tag creation - tags are safety net for rollback

- NEVER proceed if source branch does not exist

- ALWAYS provide rollback instructions in proposal and summary

- ALWAYS preserve detailed audit trail through tags with timestamps

