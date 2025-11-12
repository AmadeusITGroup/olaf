# Propose Commit Thread: Step-by-Step Tutorial

## How to Execute the "Analyze Git Changes and Create Smart Commit Sequences"

This tutorial shows exactly how to reproduce the intelligent commit clustering workflow for organizing changes into logical, coherent commits with GitHub issue integration.

## Prerequisites

- Git installed and configured on your system
- Repository with uncommitted changes ready for analysis
- GitHub CLI installed (optional, for issue integration)
- Write permissions to the repository
- Understanding of your project's feature/component structure

## Step-by-Step Instructions

### Step 1: Initiate Commit Analysis

[This step starts the OLAF commit analysis workflow]

**User Action:**

1. Invoke the propose-commit-thread competency in OLAF
2. Navigate to your repository with pending changes
3. Ensure git status shows files ready for commit organization

**OLAF Response:**

You should see OLAF validate the repository state and begin analyzing all uncommitted changes for intelligent clustering.

### Step 2: Provide Analysis Parameters

**User Action:** Specify analysis preferences when prompted

```bash
Repository path: [current directory or specify path]
Include GitHub issues integration? (y/n): [your choice]
Commit strategy (granular/feature-based): [your preference]
Auto-execute after approval? (y/n): [recommended: no]
```

**Provide Analysis Configuration:**

- **Repository Path**: Path to git repository (defaults to current directory)
- **GitHub Issues**: Enable to link commits with related open issues
- **Commit Strategy**: Choose between granular (file-by-file) or feature-based clustering
- **Auto Execute**: Keep false for safety - allows review before execution

### Step 3: Change Analysis and Categorization

**What OLAF Does:**

- Executes `git status --porcelain` for machine-readable status
- Categorizes files by git status (Modified, Added, Deleted, Renamed, etc.)
- Analyzes `git diff` for each file to understand change scope
- Groups related files by functionality, dependencies, and components
- Scans for GitHub issues if integration enabled

**You Should See:** Comprehensive analysis of all changes with file categorization and initial clustering proposals

### Step 4: GitHub Issues Integration

**What OLAF Does (if enabled):**

- Retrieves open GitHub issues using `gh issue list`
- Extracts keywords from your changes (file names, functions, classes)
- Matches potential issues by title keywords and labels
- Correlates changes with bug reports, enhancements, or features

**You Should See:** List of potentially related GitHub issues with relevance scores and suggested associations

### Step 5: Interactive Commit Proposal

**User Action:** Review the structured commit thread proposal

```markdown
# 📋 Proposed Commit Thread - YYYYMMDD-HHmm

## Repository Analysis
**Repository**: your-repo-name
**Branch**: current-branch
**Files Changed**: X (Y untracked, Z modified, W staged)

## 🎯 Proposed Commit Sequence

### Commit 1: Feature Implementation
**Files** (3):
- src/feature/main.js (Modified)
- src/feature/helper.js (Added)

**Commit Message**:
feat: implement user authentication feature

- Add main authentication logic
- Create helper utilities for token validation

**Related GitHub Issues**: #42 - User Login System

**👤 User Actions Available:**
- ✅ APPROVE: Accept this commit as proposed
- 🔄 MODIFY: Change commit message or file grouping
- ➕ SPLIT: Break into smaller commits
- ➖ MERGE: Combine with another commit
- ❌ SKIP: Don't commit these changes now
```

**Available Interactive Commands:**

- `1a` = Approve commit 1
- `1m` = Modify commit 1  
- `1s` = Split commit 1
- `merge 1,2` = Merge commits 1 and 2
- `skip 1` = Skip commit 1
- `execute` = Execute all approved commits

### Step 6: Interactive Modification Phase

**User Action:** Use commands to refine commit organization

**Modification Operations:**

- **Message Edit**: Update commit title and description
- **File Regrouping**: Move files between commit clusters
- **Commit Splitting**: Break large commits into focused smaller ones
- **Commit Merging**: Combine related commits for cleaner history
- **Issue Association**: Link/unlink GitHub issues

**Real-time Updates:**

OLAF provides immediate feedback as you modify the commit structure, ensuring consistency and preventing conflicts.

### Step 7: Final Approval and Execution

**User Action:** Execute the final commit sequence

```bash
execute
```

**What OLAF Does:**

1. **For each approved commit (in logical order):**
   - Stage specified files: `git add [file_list]`
   - Create commit with detailed message: `git commit -m "[commit_message]"`
   - Update related GitHub issues with commit reference
   - Verify commit success before proceeding

2. **GitHub Integration:**
   - Add commit references to related issues
   - Update issue labels based on commit types
   - Close issues if commit messages include closing keywords

**You Should See:** Step-by-step execution with confirmation of each successful commit and issue integration results

## Verification Checklist

✅ **All intended files committed** (git log shows proper commit sequence)

✅ **Logical commit organization** (each commit has coherent purpose and scope)

✅ **Detailed commit messages** (follows conventional commits with bullet points)

✅ **GitHub issues updated** (commits referenced in related issues)

✅ **Clean working directory** (git status shows no remaining uncommitted changes)

✅ **Git history integrity** (no conflicts or broken dependencies between commits)

## Troubleshooting

**If not a git repository:**

```bash
Error: Not a valid git repository
```

- Navigate to correct directory containing .git folder
- Initialize repository with `git init` if needed

**If merge conflicts present:**

- OLAF will stop and require resolution before proceeding
- Resolve conflicts manually using `git mergetool` or editor
- Re-run the competency after conflicts are resolved

**If GitHub CLI not available:**

- OLAF will skip GitHub integration and proceed with git-only workflow
- Install GitHub CLI with `gh auth login` for issue integration
- Alternative: manually reference issues in commit messages

**If commit permission denied:**

- Verify you have write access to the repository
- Check if branch is protected and requires specific permissions
- Ensure proper Git configuration with valid author information

## Key Learning Points

1. **Intelligent Clustering:** Changes are grouped by logical relationships rather than arbitrary file selection
2. **Interactive Refinement:** Full control over commit organization with real-time modification capabilities  
3. **GitHub Integration:** Automatic linking between commits and project issues for better project tracking
4. **Safety First:** Propose-Confirm-Act protocol prevents accidental commits and allows thorough review

## Next Steps to Try

- Review git log to see clean, logical commit sequence
- Check GitHub issues for automatic commit references and updates
- Push commits to remote repository for team collaboration
- Use similar approach for future change sets to maintain clean history

## Expected Timeline

- **Total analysis and execution time:** 5-15 minutes
- **User input required:** Analysis parameters, commit review and modification, final execution approval
- **OLAF execution time:** Git analysis, GitHub integration, automated commit execution with issue updates