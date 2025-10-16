---
name: compose-pr
description: Analyze commits to intelligently group them into logical Pull Request clusters, create feature branches, and generate GitHub PRs.
tags: [git, pr, pull-request, compose, branch-management, github]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.



## Git Command Requirements
**CRITICAL**: Always use non-interactive git commands to prevent pager prompts:
- **MANDATORY**: Use `git --no-pager` prefix for ALL git commands that support it (log, show, diff, branch, status, etc.)
- Use `--oneline` for concise output in log commands
- Use specific commit limits (e.g., `-20`) to prevent excessive output
- **Examples**: `git --no-pager log --oneline -10`, `git --no-pager show HEAD`, `git --no-pager diff HEAD~1`

## Input Parameters
- **source_branch**: string - (Optional) Source branch to analyze (default: current branch)
- **target_branch**: string - (Optional) Target branch for PRs (default: main)
- **commit_limit**: number - (Optional) Number of recent commits to analyze (default: 20)
- **pr_strategy**: enum[semantic,temporal,mixed] - (Optional) How to group commits (default: mixed)
- **integration_prefix**: string - (Optional) Integration branch prefix (default: integration)

## Standardized Workflow Process

### Phase 1: Repository Analysis & Validation
1. **CRITICAL SAFETY CHECK - Uncommitted Changes**:
   - Check for uncommitted changes: `git status --porcelain`
   - If changes detected, **STOP IMMEDIATELY** and present options:
     - **Alert**: "⚠️ SAFETY STOP: Uncommitted changes detected. Choose resolution:"
     - **Option 1**: Stash changes: `git stash push -m "work in progress"`
     - **Option 2**: Commit changes: `git add . && git commit -m "WIP: save changes"`
     - **Option 3**: Stop workflow (user handles manually)
   - **Workflow cannot proceed** until working directory is clean
2. **CRITICAL SAFETY CHECK - Branch Validation**:
   - **STOP IMMEDIATELY** if current branch is `main`, `master`, `develop`, or `dev`
   - **Alert user**: "❌ SAFETY STOP: Compose PR cannot run on protected branch '{branch_name}'. Please switch to a work-in-progress branch first."
   - **Required action**: User must checkout a feature/work branch before proceeding
   - **Protected branches**: main, master, develop, dev, production, prod, release
3. **Validate Repository State**: 
   - Check current branch and status
   - Ensure working directory is clean
   - Verify git remotes are accessible
3. **Sync Target Branch**:
   - `git fetch origin`
   - `git checkout main`
   - `git pull origin main`
   - If conflicts or issues, STOP and report error
4. **Return to Source Branch**: `git checkout <source_branch>`

### Phase 2: Integration Branch Creation & Commit Identification
1. **Create Integration Branch FIRST**:
   ```bash
   git checkout main
   git pull origin main  # Ensure up-to-date
   git checkout -b integration-YYYYMMDD-HHmm
   git push origin integration-YYYYMMDD-HHmm
   ```
   - Integration branch serves as the baseline for all feature branches
   - Provides staging area and ensures complete commit coverage
2. **Return to Source Branch**: `git checkout <source_branch>`
3. **Identify ALL Commits to Process**: 
   ```bash
   git --no-pager log --oneline integration-YYYYMMDD-HHmm..HEAD
   ```
   - Get all commits in current branch that are NOT in integration branch
   - **MANDATORY**: Use `--no-pager` to prevent interactive pager prompts
   - This ensures we capture EVERY commit that needs to be in PRs
4. **Filter Out UNTESTED Commits**:
   - **CRITICAL**: Exclude any commits with "UNTESTED" in their title/message
   - UNTESTED commits are experimental and must NOT be included in PRs
   - Log excluded commits for user awareness but do not process them
   - Only process commits that are production-ready
5. **Verify Complete Coverage**:
   - Ensure all production-ready commits are assigned to PRs
   - No commits should be left unassigned

### Phase 3: Commit Analysis & PR Clustering
1. **Analyze Filtered Commits**: Get commit history with messages, dates, and file changes for production-ready commits only
   - **Use**: `git --no-pager show --stat <commit>` for file changes
   - **Use**: `git --no-pager log --oneline --stat` for overview
2. **Extract Ticket References**: Parse commit messages for ticket/issue references:
   - **JIRA**: Match patterns like `PROJ-123`, `ABC-456`
   - **GitHub Issues**: Match patterns like `#123`, `fixes #456`, `closes #789`
   - **Linear**: Match patterns like `LIN-123`, `LINEAR-456`
   - **Azure DevOps**: Match patterns like `AB#123`, `WorkItem#456`
   - **Custom**: Match any `TICKET-123` or `[TICKET-123]` patterns
   - Group commits by shared ticket references for better PR organization
3. **Apply Clustering Strategy**:
   - **Chronological Constraint**: NEVER group commits out of chronological order
   - **Dependency Analysis**: Ensure later commits don't depend on earlier commits in different PRs
   - **Semantic Clustering**: Group by commit type (feat, fix, chore, docs) WITHIN chronological bounds
   - **Temporal Clustering**: Group by development sessions (same day/timeframe)
   - **Functional Clustering**: Group by related functionality or file changes
3. **Generate PR Proposals**: Create logical PR groups with:
   - Descriptive PR titles following conventional format
   - Detailed PR descriptions with bullet points
   - Commit lists for each PR
   - Risk assessment (stable, experimental, UNTESTED)

### Phase 4: User PR Selection Interface
**Present standardized PR proposal format:**

```markdown
# 🔍 Compose PR Analysis
**Timestamp:** YYYYMMDD-HHmm
**Source Branch:** branch-name
**Target Branch:** main
**Total Commits Ahead:** X commits
**UNTESTED Commits Excluded:** Y commits
**Production-Ready Commits:** Z commits

## 🚫 Excluded UNTESTED Commits
**These commits are excluded from PR creation (experimental/untested):**
```
cafc3dd UNTESTED: feat(migration): add comprehensive Angular migration framework
abc1234 UNTESTED: fix(auth): experimental authentication changes
```
**Note:** UNTESTED commits must be thoroughly tested before being eligible for PRs.

## 📦 Proposed Pull Request Groups

### ✅ **PR A: `feat: implement framework optimization`**
**Commits (3):**
```
bed7fd3 feat(framework): add condensed OLAF reference [OLAF-123]
db11d84 feat: architecture shift to condensed framework fixes #456
abc1234 docs: update framework documentation
```
**Files Changed:** 12 files (+245, -67)
**Risk Level:** Medium
**Tickets Referenced:** OLAF-123, #456
**Generated Title:** `feat: implement condensed OLAF framework architecture`
**Generated Description:**
```
Optimize OLAF framework performance with condensed reference system

## Related Issues
- OLAF-123: Framework performance optimization
- #456: Memory usage improvements

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

## Commits
- bed7fd3 feat(framework): add condensed OLAF reference [OLAF-123]
- db11d84 feat: architecture shift to condensed framework fixes #456
- abc1234 docs: update framework documentation
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

### Phase 5: Feature Branch Creation & Cherry-picking Management
**Note**: Integration branch already created in Phase 2

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

### Phase 7: GitHub PR Creation
**For each feature branch:**
1. **Generate PR via GitHub CLI with Dependency Management**:
   ```bash
   # For dependent PRs (create as draft)
   gh pr create \
     --title "[2/3] feat: implement condensed OLAF framework architecture" \
     --body "$(cat pr-description.md)" \
     --base main \
     --head feature/framework-optimization \
     --label "enhancement,depends-on-pr,merge-order-2" \
     --assignee @me \
     --draft
   
   # For independent PRs (ready for review)
   gh pr create \
     --title "feat: implement independent feature" \
     --body "$(cat pr-description.md)" \
     --base main \
     --head feature/independent \
     --label "enhancement" \
     --assignee @me
   ```
2. **PR Body Generation**: Create appropriately detailed markdown description based on:
   
   **Detail Level Determination:**
   - **Minimal**: 1-3 commits, <5 files, docs/chore/fix types
   - **Standard**: 4-8 commits, 5-15 files, feat/refactor types
   - **Comprehensive**: 9+ commits, 15+ files, major features/architecture
   
   **Generated Content:**
   - **Dependencies**: Clear dependency information for GitHub users
   - **Related Issues**: All extracted ticket references with proper links
   - **Summary**: Context-appropriate explanation (brief to detailed)
   - **Changes**: Bullet-pointed list (simple to categorized)
   - **Benefits**: Impact description (optional for minimal)
   - **Testing**: Checklist appropriate to change complexity
   - **Commits**: Full commit list with ticket references
   - **Breaking Changes**: If any detected from commit messages
   - **Deployment Notes**: For comprehensive PRs only

### GitHub Dependency Management
**Since GitHub lacks built-in PR dependencies, use these practices:**

#### **PR Title Prefixes:**
- `[1/3] feat: first part of feature` - Indicates sequence
- `[DEPENDS: #123] feat: follow-up feature` - Shows dependency
- `[BLOCKED] feat: waiting for dependencies` - Indicates blocked status

#### **PR Description Sections:**
```markdown
## 🔗 Dependencies
- **Depends on:** #123 (must be merged first)
- **Blocks:** #125, #126 (these PRs depend on this one)
- **Merge Order:** This is PR 2 of 3 in the sequence

## ⚠️ Merge Instructions
**CRITICAL:** This PR can only be merged after PR #123 is merged.
Merging out of order will cause conflicts.
```

#### **GitHub Labels:**
- `depends-on-pr` - Has dependencies
- `blocks-other-prs` - Other PRs depend on this
- `merge-order-1`, `merge-order-2`, etc. - Sequence indicators

#### **Draft PR Strategy:**
- Create all PRs as **Draft** initially
- Mark as "Ready for Review" only when dependencies are merged
- Use PR comments to track dependency status

## Advanced Features

### Smart PR Grouping Strategies
- **Chronological Ordering**: CRITICAL - PRs must be mergeable in chronological order
- **Dependency Analysis**: Detect commits that depend on each other and keep them together
- **File Overlap Detection**: Group commits that modify the same files to avoid conflicts
- **Ticket-based Clustering**: Group commits that reference the same tickets/issues
- **Risk-based Separation**: Separate UNTESTED/experimental features
- **Size Optimization**: Keep PRs reviewable (max 20 files, 500 lines)

### Merge Order Safety
- **Sequential PRs**: Each PR must be based on the previous PR's target state
- **No Cherry-pick Conflicts**: Later commits cannot be merged before earlier dependencies
- **File Dependency Tracking**: Detect when files are modified across multiple PRs
- **Merge Order Documentation**: Clearly specify the required merge order for reviewers

### Ticket Reference Extraction
- **JIRA Patterns**: `PROJ-123`, `ABC-456`, `[TICKET-789]`
- **GitHub Issues**: `#123`, `fixes #456`, `closes #789`, `resolves #012`
- **Linear**: `LIN-123`, `LINEAR-456`
- **Azure DevOps**: `AB#123`, `WorkItem#456`
- **Custom Formats**: Any `[IDENTIFIER-NUMBER]` or `IDENTIFIER-NUMBER` patterns
- **Automatic Linking**: Include ticket links in PR descriptions for traceability

### Automatic Detail Level Detection
**Minimal Detail Triggers:**
- ≤3 commits AND ≤5 files changed
- Commit types: `docs`, `chore`, `style`, `fix` (simple)
- File types: README, documentation, config files only

**Standard Detail Triggers:**
- 4-8 commits OR 6-15 files changed
- Commit types: `feat`, `fix` (complex), `refactor`
- Mixed file types: code + tests + docs

**Comprehensive Detail Triggers:**
- ≥9 commits OR ≥16 files changed
- Commit types: `feat!` (breaking), `BREAKING CHANGE`
- Architecture files: core modules, APIs, database schemas
- Multiple domains: frontend + backend + infrastructure

### Conflict Resolution
- **Cherry-pick Conflicts**: Provide step-by-step resolution guidance
- **Branch Conflicts**: Detect and handle branch creation conflicts
- **Remote Conflicts**: Handle push conflicts and suggest solutions

### PR Body Generation Strategy
**Detail Level Based on PR Type and Size:**

#### **Minimal Detail** (Small fixes, docs, chores):
```markdown
## Summary
Brief one-line description of the change

## Related Issues
- Fixes #123

## Changes
- Single bullet point describing the change
```

#### **Standard Detail** (Features, refactoring):
```markdown
## Summary
Clear description of what this PR accomplishes and why

## Related Issues
- PROJ-123: Original feature request
- Fixes #456: Bug that this addresses

## Changes
- Bullet point for each major change
- Include technical details for complex changes
- Mention any new dependencies or breaking changes

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Commits
- abc1234 feat: add new feature
- def5678 test: add unit tests
```

#### **Comprehensive Detail** (Major features, architecture changes):
```markdown
## 🔗 Dependencies
- **Depends on:** #123 - Foundation framework changes (must merge first)
- **Blocks:** #125 - UI components that use this API
- **Merge Order:** This is PR 2 of 3 in the compose feature sequence
- **Status:** ⏳ Waiting for #123 to merge before this can be reviewed

## Summary
Detailed explanation of the feature/change including business context

## Related Issues
- PROJ-123: Original epic/feature request
- PROJ-124: Related technical debt item
- Fixes #456: Bug discovered during development

## Changes
### Core Changes
- Detailed explanation of main functionality
- Architecture decisions and rationale
- Performance implications

### Supporting Changes
- Documentation updates
- Test additions
- Configuration changes

## Benefits
- Business value delivered
- Technical improvements
- Performance gains (with metrics if available)

## Breaking Changes
- List any breaking changes
- Migration steps if needed

## ⚠️ Merge Instructions
**CRITICAL:** 
1. Wait for PR #123 to be merged first
2. Rebase this PR after #123 is merged
3. Only then mark as ready for review
4. Do NOT merge out of order - will cause conflicts

## Testing
- [ ] Unit tests (coverage: X%)
- [ ] Integration tests
- [ ] End-to-end tests
- [ ] Performance testing
- [ ] Security review (if applicable)
- [ ] ✅ Dependency PR #123 merged

## Deployment Notes
- Any special deployment considerations
- Feature flags or rollout strategy
- Monitoring requirements

## Screenshots/Demos
- Include for UI changes
- Before/after comparisons

## Commits
- abc1234 feat(core): implement main feature logic
- def5678 feat(api): add new endpoints
- ghi9012 test: comprehensive test coverage
- jkl3456 docs: update API documentation
```

### PR Quality Assurance
- **Conventional Commits**: Ensure PR titles follow conventional format
- **Description Quality**: Generate appropriate detail level based on PR complexity
- **Label Assignment**: Auto-assign appropriate GitHub labels based on changes
- **Reviewer Suggestions**: Suggest reviewers based on file changes and expertise areas

## Error Handling & Safety
- **CRITICAL BRANCH SAFETY**: NEVER run on main/master/develop/dev/production/prod/release branches
- **Pre-flight Checks**: Validate git state before starting
- **UNTESTED Filter**: MANDATORY exclusion of commits with "UNTESTED" in title
- **Rollback Capability**: Provide commands to undo changes if needed
- **Conflict Detection**: Stop process if unresolvable conflicts occur
- **Branch Protection**: Respect branch protection rules

## Required Actions
1. **MANDATORY SAFETY CHECK**: Check for uncommitted changes and STOP if any exist (no continue option)
2. **MANDATORY SAFETY CHECK**: Verify current branch is NOT main/master/develop/dev/production/prod/release
3. **Validate repository state** and sync target branch
4. **Create integration branch FIRST** as baseline and push to origin
3. **Identify ALL commits to process** using `git log integration-branch..HEAD`
4. **Filter UNTESTED commits** and verify complete coverage
5. **Analyze production-ready commits** and generate PR clusters
6. **Present PR proposals** for user selection
7. **Create feature branches** with cherry-picked commits from integration branch
8. **Push all feature branches** to origin
9. **Generate GitHub PRs** with detailed descriptions targeting main (not integration)
10. **Verify no commits left unassigned** to PRs

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

## Sequential PR Strategy (RECOMMENDED)
**To avoid merge conflicts and dependency issues:**

### Option 1: Sequential PRs (Safest)
1. **PR A**: Contains commits 1-5 (oldest commits)
2. **PR B**: Based on PR A, contains commits 6-10  
3. **PR C**: Based on PR B, contains commits 11-15
4. **Merge Order**: A → B → C (strict chronological order)

### Option 2: Independent PRs (Riskier)
1. **PR A**: Contains commits 1,3,7 (cherry-picked)
2. **PR B**: Contains commits 2,4,8 (cherry-picked)  
3. **Risk**: Potential conflicts if commits have dependencies
4. **Mitigation**: Extensive dependency analysis required

**Default Strategy**: Use Sequential PRs unless commits are proven independent

## Example Complete Session
```bash
# User command: "compose pr"

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
- **UNCOMMITTED CHANGES**: STOP workflow if any uncommitted changes exist - no exceptions
- **BRANCH SAFETY**: NEVER run on main/master/develop/dev/production/prod/release branches
- **UNTESTED commits MUST be excluded** - Never include experimental commits in PRs
- GitHub CLI must be installed and authenticated
- User must have push permissions to origin
- Target branch must be up-to-date with origin
- Working directory must be clean before starting
- All commits must be valid and cherry-pickable