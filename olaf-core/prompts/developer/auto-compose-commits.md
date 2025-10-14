---
name: auto-compose-commits
description: Analyze untracked and staged files to intelligently group them into logical commit clusters with meaningful commit messages.
tags: [git, commits, auto-compose, file-analysis, clustering]
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
- **repository_root**: string - (Optional) Path to the Git repository root (default: current directory)
- **include_untracked**: boolean - (Optional) Whether to analyze untracked files (default: true)
- **commit_strategy**: enum[auto,interactive,dry-run] - (Optional) How to handle commit creation (default: interactive)
- **max_commits**: number - (Optional) Maximum number of commits to create (default: 5)
- **clustering_strategy**: enum[semantic,directory,file-type,mixed] - (Optional) How to group files (default: mixed)
- **auto_gitignore**: boolean - (Optional) Automatically suggest .gitignore additions for non-trackable files (default: true)

## Process

1. **Repository State Analysis**:
   - Get current git status
   - List staged files with their status (modified, added, deleted)
   - List untracked files (if include_untracked=true)
   - Identify file types and directory structure
   - Check for existing commit history patterns
   - Analyze .gitignore patterns and suggest improvements

2. **File Content Analysis**:
   - Analyze file changes using git diff for staged files
   - Examine untracked files for content type and purpose
   - Identify relationships between files (imports, references, etc.)
   - Detect code patterns, documentation updates, configuration changes
   - **Filter Non-Trackable Files**: Identify files that shouldn't be tracked:
     - Build artifacts (dist/, build/, target/)
     - Dependencies (node_modules/, vendor/, .venv/)
     - IDE files (.vscode/, .idea/, *.swp)
     - OS files (.DS_Store, Thumbs.db)
     - Logs and temporary files (*.log, *.tmp, *.cache)
     - Environment and secret files (.env, *.key, *.pem)
     - Large binary files and media assets

3. **Intelligent Clustering**:
   - **Semantic Clustering**: Group files by logical functionality
     - Feature additions/modifications
     - Bug fixes
     - Documentation updates
     - Configuration changes
     - Test additions/updates
   - **Directory-based Clustering**: Group by file location
   - **File-type Clustering**: Group similar file types
   - **Dependency Clustering**: Group interdependent files

4. **Commit Message Generation**:
   - Analyze changes to determine commit type (feat, fix, docs, etc.)
   - Generate concise, descriptive commit messages
   - Follow conventional commit format
   - Include scope when applicable
   - Add detailed descriptions for complex changes

5. **Validation and Optimization**:
   - Ensure each commit is atomic and focused
   - Validate against project conventions
   - Check for potential conflicts or issues
   - Optimize commit order for logical progression

## Clustering Strategies

### Semantic Clustering (Recommended)
- **Feature Development**: New functionality, related tests, documentation
- **Bug Fixes**: Fix implementation, related tests, documentation updates
- **Refactoring**: Code improvements without functional changes
- **Documentation**: README updates, code comments, API docs
- **Configuration**: Build files, environment configs, dependencies
- **Testing**: Test files, test configurations, test data

### Directory-based Clustering
- Group files by their directory structure
- Useful for component-based or module-based projects

### File-type Clustering
- Group by file extensions (.js, .css, .md, etc.)
- Useful for projects with clear separation of concerns

### Mixed Strategy (Default)
- Combine semantic and directory-based approaches
- Prioritize semantic relationships over directory structure

## Output Format

### Commit Plan Report
```markdown
# Auto-Compose Commits Analysis

## Repository Status
- Staged files: X
- Untracked files: Y
- Files filtered out (non-trackable): Z
- Total commitable files: W

## 🚫 Non-Trackable Files Detected
**These files should probably not be committed:**
- build/dist/app.js (build artifact)
- node_modules/ (dependencies)
- .env (environment secrets)
- *.log (log files)

**Suggested .gitignore additions:**
```
# Build artifacts
build/
dist/

# Environment files
.env
.env.local

# Logs
*.log
```

**Action Required:** 
- [ ] Add to .gitignore
- [ ] Remove from staging (if staged)
- [ ] Ignore for this session

## 📦 Commitable Clusters (Choose which to commit)

### ✅ Cluster 1: [type](scope): description
**Status:** Ready to commit
**Files:**
- path/to/file1.js (modified)
- path/to/file2.js (added)
- path/to/test.spec.js (added)

**Rationale:** Brief explanation of why these files are grouped together

**Generated Message:**
```
feat(auth): implement user authentication system

Add login/logout functionality with JWT tokens
- Add authentication service
- Add login component
- Add corresponding unit tests
```

**User Decision:** 
- [ ] ✅ Commit this cluster
- [ ] ❌ Skip this cluster
- [ ] ✏️ Modify this cluster

### ⚠️ Cluster 2: [type](scope): description  
**Status:** Needs review (mixed concerns detected)
**Files:**
- path/to/feature.js (modified)
- path/to/unrelated.css (modified)

**User Decision:**
- [ ] ✅ Commit as-is
- [ ] ❌ Skip entirely  
- [ ] 🔄 Split into separate commits
- [ ] ✏️ Modify grouping

## 🎯 Execution Options
1. **Commit Selected Clusters**: Only commit clusters marked with ✅
2. **Interactive Review**: Review each cluster individually
3. **Batch Commit**: Commit multiple selected clusters at once
4. **Save Selections**: Save cluster decisions for later
5. **Dry Run**: Show what would be committed without executing
```

## Advanced Features

### Smart Detection Patterns
- **Related Files**: Detect files that should be committed together
  - Source file + corresponding test file
  - Component + its styles/templates
  - Configuration + documentation
  - Migration + rollback scripts

- **Change Types**: Automatically detect change categories
  - New features (new files + modifications)
  - Bug fixes (modifications to existing functionality)
  - Refactoring (structural changes without new features)
  - Documentation (README, comments, docs)
  - Dependencies (package.json, requirements.txt, etc.)

### Non-Trackable File Detection
- **Build Artifacts**: dist/, build/, target/, out/, .next/
- **Dependencies**: node_modules/, vendor/, .venv/, __pycache__/
- **IDE/Editor Files**: .vscode/, .idea/, *.swp, *.swo, .sublime-*
- **OS Files**: .DS_Store, Thumbs.db, desktop.ini
- **Logs & Temp**: *.log, *.tmp, *.cache, .sass-cache/
- **Environment**: .env*, *.key, *.pem, *.p12, config.local.*
- **Large Binaries**: *.zip, *.tar.gz, *.exe, *.dmg (>10MB)
- **Generated Files**: Auto-generated code, compiled assets

### Conflict Detection
- Identify files that might belong to multiple commits
- Suggest splitting large files with multiple concerns
- Warn about potentially incomplete features
- Flag files that should be in .gitignore but aren't

### Project-Specific Adaptations
- Learn from existing commit history patterns
- Adapt to project's commit message conventions
- Respect project's file organization structure
- Analyze existing .gitignore patterns

## Domain-Specific Rules
- Rule 1: Each commit should represent a single logical change
- Rule 2: Related files should be committed together
- Rule 3: Follow conventional commit message format
- Rule 4: Prioritize semantic relationships over file proximity
- Rule 5: Ensure commits can be safely reverted independently
- Rule 6: Group tests with their corresponding implementation
- Rule 7: Keep documentation updates with related code changes

## Required Actions
1. Analyze current repository state
2. **Filter non-trackable files** and suggest .gitignore updates
3. Examine file contents and relationships for commitable files
4. Apply clustering strategy to group files into logical commits
5. **Present clusters for user selection** - let user choose which to commit
6. Generate meaningful commit messages for selected clusters
7. Execute only the approved clusters
8. Optionally update .gitignore with suggested patterns

## Error Handling
- Handle empty repositories gracefully
- Warn about large commits (>20 files)
- Detect and report potential merge conflicts
- Validate commit message format
- Check for sensitive information in files

## Integration Points
- Can be integrated with IDE git interfaces
- Compatible with git hooks and pre-commit checks
- Supports custom commit message templates
- Works with branch protection rules

⚠️ **Critical Notes**
- Always review generated commits before execution
- Respect .gitignore and .gitattributes files
- Never commit sensitive information (passwords, keys, etc.)
- Ensure atomic commits that can be safely reverted
- Validate against project's contribution guidelines
#
# User Interaction Flow

### Phase 1: File Analysis & Filtering
1. **Scan Repository**: Analyze all staged and untracked files
2. **Filter Non-Trackable**: Automatically identify files that shouldn't be committed
3. **Present Filtered Files**: Show user what was filtered out and why
4. **Suggest .gitignore Updates**: Propose additions to .gitignore
5. **User Decision**: User approves .gitignore updates or skips

### Phase 2: Cluster Presentation & Selection
1. **Present Clusters**: Show all proposed commit clusters
2. **Cluster Status Indicators**:
   - ✅ **Ready**: Clean, focused cluster
   - ⚠️ **Needs Review**: Mixed concerns or large cluster
   - 🔍 **Uncertain**: Files that might not belong together
3. **User Selection**: User chooses which clusters to commit:
   - Select individual clusters with checkboxes
   - Modify cluster contents
   - Split clusters into smaller commits
   - Skip clusters entirely

### Phase 3: Execution
1. **Commit Selected Clusters**: Only process user-approved clusters
2. **Show Progress**: Display each commit as it's created
3. **Handle Errors**: Gracefully handle any commit failures
4. **Summary Report**: Show what was committed and what was skipped

## Interactive Commands During Execution

```
Available commands during cluster selection:
- 'commit 1,3,5' - Commit specific clusters by number
- 'skip 2,4' - Skip specific clusters  
- 'modify 3' - Edit files in cluster 3
- 'split 2' - Split cluster 2 into smaller commits
- 'all' - Commit all ready clusters (✅ status only)
- 'none' - Skip all clusters
- 'review' - Show detailed view of all clusters
- 'gitignore' - Update .gitignore with suggestions
```

## Example User Session

```
🔍 Analyzing repository...

📊 Found 15 files:
- 8 commitable files
- 4 build artifacts (filtered out)
- 2 log files (filtered out) 
- 1 .env file (filtered out)

🚫 Non-trackable files detected:
- dist/bundle.js (build artifact)
- debug.log (log file)
- .env (secrets)

💡 Suggested .gitignore additions:
+ dist/
+ *.log
+ .env

❓ Add these to .gitignore? (y/n): y

📦 Proposed commit clusters:

✅ Cluster 1: feat(auth): add login system
   - src/auth/login.js
   - src/auth/login.test.js
   - docs/auth.md

⚠️ Cluster 2: mixed changes (needs review)
   - src/utils/helper.js (refactor)
   - README.md (docs update)

🎯 Which clusters to commit?
Enter cluster numbers (e.g., '1,2') or commands: 1

✅ Committing cluster 1...
✅ Created commit: feat(auth): add login system

📋 Summary:
- 1 cluster committed
- 1 cluster skipped  
- 3 files added to .gitignore
```