# Generate Commits from Changelog: Step-by-Step Tutorial

**How to Execute the "Generate Commits from Changelog" Competency**

This tutorial shows exactly how to generate meaningful Git commits from changelog entries and repository changes, ensuring consistency between documentation and version control.

## Prerequisites

- OLAF framework loaded and active
- Git repository initialized
- Changelog with recent entries
- Staged or unstaged changes in repository
- Understanding of conventional commit messages

## Step-by-Step Instructions

### Step 1: Invoke the Competency
**User Action:**
1. Type: `olaf generate commits from changelog`
2. Or use aliases: `olaf generate commits`, `olaf commits from changelog`, `olaf commit generation`
3. Press Enter

**AI Response:**
Acknowledges request and begins analysis using Propose-Act protocol.

### Step 2: Provide Parameters
**User Provides Optional Information:**
- **changelog_path**: (default: uses memory-map reference)
- **repository_root**: (default: current directory)
- **commit_strategy**: "auto" or "interactive" (default: interactive)
- **sign_commits**: true or false (default: false)

**Example:**
```
Commit Strategy: interactive
Sign Commits: false
```

### Step 3: Initial Analysis
**What AI Does:**
1. Checks for staged changes: `git status`
2. Scans for modified, added, and deleted files
3. Identifies untracked files that should be versioned
4. Lists all changes requiring commits

**You Should See:** Summary of repository state with file counts.

### Step 4: Changelog Processing
**What AI Does:**
- Parses recent changelog entries
- Groups related changes logically
- Maps changelog entries to affected files
- Generates commit messages following conventions

**Conventional Commit Format:**
```
type(scope): concise description

Detailed explanation if needed

- List of changes
- Related to #issue
- BREAKING CHANGE: if applicable
```

**Supported Types:**
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes
- refactor: Code refactoring
- perf: Performance improvements
- test: Test additions/modifications
- chore: Maintenance tasks

### Step 5: Change Analysis
**What AI Does:**
- Analyzes file modifications using `git diff`
- Groups related files by feature/fix
- Identifies changes not in changelog
- Creates additional commit proposals for unassociated changes

**Grouping Logic:**
- Files in same directory often related
- Similar file types grouped together
- Changelog references guide grouping

### Step 6: Commit Planning
**What AI Does:**
Creates commit plan with:
- Proposed commit messages
- Files to include in each commit
- Changelog entry references
- Validation against branch policies

**Example Commit Plan:**
```markdown
## Proposed Commits

### Commit 1: feat(auth): implement OAuth 2.0 token refresh
**Files:**
- src/auth/token-refresh.js
- src/auth/token-validator.js
- tests/auth/token-refresh.test.js

**Changelog Reference:** Feature: Added OAuth 2.0 token refresh [20251027]

**Message:**
feat(auth): implement OAuth 2.0 token refresh

Add automatic token refresh to prevent session expiration.
Implements PKCE flow for enhanced security.

- Add token refresh endpoint
- Implement client-side refresh logic
- Add comprehensive test coverage

Related to: job-042

### Commit 2: docs: update authentication documentation
**Files:**
- docs/authentication.md
- README.md

**Changelog Reference:** Documentation: Updated auth docs [20251027]
```

### Step 7: Review and Modify
**User Action:** Review proposed commits

**Options:**
1. **Accept all**: "approved" - create all commits as proposed
2. **Modify individual**: "update commit 1 message to include breaking change note"
3. **Regenerate**: "regenerate with different grouping"
4. **Abort**: "cancel" - exit without creating commits

**AI Response:**
Applies modifications and presents updated plan for re-review.

### Step 8: Commit Execution
**What AI Does:**
For each approved commit:
1. Stages specified files: `git add [files]`
2. Creates commit with generated message: `git commit -m "[message]"`
3. Optionally signs commit if requested: `git commit -S`
4. Validates commit created successfully
5. Updates changelog with commit hash

**You Should See:** Progress for each commit created with hash.

### Step 9: Execution Summary
**AI Provides:**
- Number of commits created
- Files included in each commit
- Commit hashes for reference
- Any warnings or errors encountered
- Next steps (push, create PR, etc.)

## Verification Checklist

✅ **All changes committed** (no unstaged changes remain)
✅ **Commit messages follow conventions** (type, scope, description)
✅ **Related files grouped** logically in commits
✅ **Changelog references included** in commit messages
✅ **Atomic commits** (each commit is self-contained)
✅ **Branch policies respected** (no violations)
✅ **Commit history clean** (no unnecessary commits)

## Troubleshooting

**If no changes detected:**
```bash
# Check repository status
git status

# Verify changes exist
git diff
```

**If commit fails:**
```bash
# Check for conflicts
git status

# Verify branch is not protected
git branch -vv
```

**If message format rejected:**
- Review conventional commit format
- Check for required scope or type
- Verify no special characters causing issues

**If files not staged:**
- Ensure files are tracked by git
- Check .gitignore rules
- Verify file permissions

## Key Learning Points

1. **Consistency**: Changelog and git history stay synchronized
2. **Conventional Commits**: Following standards improves readability and automation
3. **Atomic Commits**: Each commit represents one logical change
4. **Interactive Review**: Human oversight prevents incorrect grouping

## Expected Timeline

- **Total time:** 5-10 minutes
- **User input:** 2-3 minutes for review and approval
- **AI execution:** 3-7 minutes for analysis and commit creation
- **Files processed:** ~50-100 files per minute
