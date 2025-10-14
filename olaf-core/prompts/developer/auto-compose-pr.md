---
name: auto-compose-pr
description: Analyze commits to intelligently group them into logical Pull Request clusters, create feature branches, and generate GitHub PRs.
tags: [git, pr, pull-request, auto-compose, branch-management, github]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

Use terminal commands, not training data.

## Input Parameters
- **source_branch**: string - (Optional) Source branch to analyze (default: current branch)
- **target_branch**: string - (Optional) Target branch for PRs (default: main)
- **commit_limit**: number - (Optional) Number of recent commits to analyze (default: 20)
- **pr_strategy**: enum[semantic,temporal,mixed] - (Optional) How to group commits (default: mixed)
- **integration_prefix**: string - (Optional) Integration branch prefix (default: integration)

## Standardized Workflow Process

### Phase 1: Repository Analysis & Validation
1. **Get Current Timestamp**: Use terminal command for YYYYMMDD-HHmm format
2. **Validate Repository State**: 
   - Check current branch and status
   - Ensure working directory is clean
   - Verify git remotes are accessible
3. **Sync Target Branch**:
   - `git fetch origin`
   - `git checkout main`
   - `git pull origin main`
   - If conflicts or issues, STOP and report error
4. **Return to Source Branch**: `git checkout <source_branch>`

### Phase 2: Commit Analysis & PR Clustering
1. **Analyze Recent Commits**: Get commit history with messages, dates, and file changes
2. **Apply Clustering Strategy**:
   - **Semantic Clustering**: Group by commit type (feat, fix, chore, docs)
   - **Temporal Clustering**: Group by development sessions (same day/timeframe)
   - **Functional Clustering**: Group by related functionality or file changes
3. **Generate PR Proposals**: Create logical PR groups with:
   - Descriptive PR titles following conventional format
   - Detailed PR descriptions with bullet points
   - Commit lists for each PR
   - Risk assessment (stable, experimental, UNTESTED)

### Phase 3: User PR Selection Interface
**Present standardized PR proposal format:**

```markdown
# 🔍 Auto-Compose PR Analysis
**Timestamp:** YYYYMMDD-HHmm
**Source Branch:** branch-name
**Target Branch:** main
**Commits Analyzed:** X commits

## 📦 Proposed Pull Request Groups

### ✅ **PR A: `feat: implement framework optimization`**
**Commits (3):**
```
bed7fd3 feat(framework): add condensed OLAF reference
db11d84 feat: architecture shift to condensed framework
abc1234 docs: update framework documentation
```
**Files Changed:** 12 files (+245, -67)
**Risk Level:** Medium
**Generated Title:** `feat: implement condensed OLAF framework architecture`
**Generated Description:**
```
Optimize OLAF framework performance with condensed reference system

## Changes
- Add condensed framework reference for improved performance
- Implement architecture shift to use condensed OLAF framework
- Update documentation to reflect new framework structure

## Benefits
- Faster session initialization
- Reduced memory footprint
- Improved framework maintainability

## Testing
- [ ] Verify framework loads correctly
- [ ] Test session initialization performance
- [ ] Validate all existing functionality works
```

[Similar format for PR B, C, D, etc.]

## 🎯 PR SELECTION
**Choose which PRs to create:**

**Commands:**
- accept A,B,E          # Accept specific PRs
- accept A-E            # Accept range of PRs
- reject C              # Reject specific PR
- modify D              # Modify PR D contents
- details B             # Show detailed analysis of PR B
- create                # Proceed with accepted PRs
```

### Phase 4: Integration Branch Creation & Management
1. **Create Integration Branch**:
   ```bash
   git checkout main
   git checkout -b integration-YYYYMMDD-HHmm
   ```
2. **Integration Branch Purpose**:
   - Staging area for all PR branches
   - Allows testing combined changes
   - Provides rollback point if needed
3. **Push Integration Branch**: `git push origin integration-YYYYMMDD-HHmm`

### Phase 5: Feature Branch Creation & Cherry-picking
**For each accepted PR:**
1. **Create Feature Branch**:
   ```bash
   git checkout integration-YYYYMMDD-HHmm
   git checkout -b feature/framework-optimization
   ```
2. **Cherry-pick Commits**:
   ```bash
   git cherry-pick bed7fd3 db11d84 abc1234
   ```
3. **Handle Cherry-pick Conflicts**: If conflicts occur, provide resolution guidance
4. **Push Feature Branch**: `git push origin feature/framework-optimization`

### Phase 6: GitHub PR Creation
**For each feature branch:**
1. **Generate PR via GitHub CLI**:
   ```bash
   gh pr create \
     --title "feat: implement condensed OLAF framework architecture" \
     --body "$(cat pr-description.md)" \
     --base main \
     --head feature/framework-optimization \
     --label "enhancement" \
     --assignee @me
   ```
2. **PR Body Generation**: Create detailed markdown description with:
   - Summary of changes
   - Bullet-pointed change list
   - Benefits and impact
   - Testing checklist
   - Breaking changes (if any)

## Advanced Features

### Smart PR Grouping Strategies
- **Dependency Analysis**: Detect commits that depend on each other
- **File Overlap Detection**: Group commits that modify the same files
- **Risk-based Separation**: Separate UNTESTED/experimental features
- **Size Optimization**: Keep PRs reviewable (max 20 files, 500 lines)

### Conflict Resolution
- **Cherry-pick Conflicts**: Provide step-by-step resolution guidance
- **Branch Conflicts**: Detect and handle branch creation conflicts
- **Remote Conflicts**: Handle push conflicts and suggest solutions

### PR Quality Assurance
- **Conventional Commits**: Ensure PR titles follow conventional format
- **Description Quality**: Generate comprehensive, reviewable descriptions
- **Label Assignment**: Auto-assign appropriate GitHub labels
- **Reviewer Suggestions**: Suggest reviewers based on file changes

## Error Handling & Safety
- **Pre-flight Checks**: Validate git state before starting
- **Rollback Capability**: Provide commands to undo changes if needed
- **Conflict Detection**: Stop process if unresolvable conflicts occur
- **Branch Protection**: Respect branch protection rules

## Required Actions
1. **Validate repository state** and sync target branch
2. **Analyze commits** and generate PR clusters
3. **Present PR proposals** for user selection
4. **Create integration branch** as staging area
5. **Create feature branches** with cherry-picked commits
6. **Push all branches** to origin
7. **Generate GitHub PRs** with detailed descriptions
8. **Provide summary** of created PRs and next steps

## Integration Branch Strategy
**Purpose of integration-YYYYMMDD-HHmm:**
- **Staging Area**: Base for all feature branches
- **Testing Ground**: Allows testing combined changes
- **Rollback Point**: Safe point to return to if issues arise
- **Documentation**: Preserves the PR creation session context

**Should be pushed to origin:** YES
- Provides backup of the integration session
- Allows collaboration on PR review process
- Enables rollback if feature branches have issues

## Example Complete Session
```bash
# User command: "auto compose pr"

# 1. Analysis phase
🔍 Analyzing 15 recent commits on research-straf...
📊 Found 5 potential PR groups

# 2. User selection
User: "accept A,B,E reject C modify D"

# 3. Integration branch
✅ Created integration-20251014-2330
✅ Pushed to origin/integration-20251014-2330

# 4. Feature branches
✅ Created feature/framework-optimization (3 commits)
✅ Created feature/developer-productivity (2 commits)  
✅ Created feature/user-experience (4 commits)

# 5. GitHub PRs
✅ PR #123: feat: implement condensed OLAF framework architecture
✅ PR #124: feat: add developer productivity tools
✅ PR #125: feat: enhance user experience with context management

📋 Summary: 3 PRs created, 9 commits organized, ready for review
```

⚠️ **Critical Requirements**
- GitHub CLI must be installed and authenticated
- User must have push permissions to origin
- Target branch must be up-to-date with origin
- Working directory must be clean before starting
- All commits must be valid and cherry-pickable