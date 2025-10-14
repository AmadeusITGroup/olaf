---
name: compose-commits
description: Analyze untracked and staged files to intelligently group them into logical commit clusters with meaningful commit messages.
tags: [git, commits, compose, file-analysis, clustering]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.



## Git Command Requirements
**CRITICAL**: Always use non-interactive git commands to prevent pager prompts:
- Use `git --no-pager` prefix for log, show, diff commands
- Use `--oneline` for concise output
- Use specific commit limits to prevent excessive output

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
# Compose Commits Analysis

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
## Standardized Workflow Process

### Phase 1: Repository Analysis
1. **Scan Repository State**: Analyze all staged, modified, and untracked files
3. **Get File Timestamps**: Retrieve creation and modification times for clustering
4. **Filter Non-Trackable**: Automatically identify files that shouldn't be committed
5. **Clean Malformed Files**: Remove any command artifacts or invalid filenames

### Phase 2: Intelligent Clustering
1. **Timestamp-Based Grouping**: Primary clustering by creation/modification time
2. **Content Analysis**: Secondary clustering by file purpose and relationships
3. **Semantic Grouping**: Group related functionality (features, fixes, docs, etc.)
4. **Generate Detailed Messages**: Create comprehensive commit messages with:
   - Conventional commit format (type(scope): description)
   - Detailed multi-line descriptions
   - Bullet points listing specific changes
   - Rationale for grouping decisions

### Phase 3: Standardized Cluster Presentation
**ALWAYS present clusters in chronological order (A, B, C, D, E, F, G, H, I, J, K, L)**

**Each cluster MUST include:**
- **Cluster ID**: Letter designation (A-L)
- **Commit Type & Scope**: Conventional format
- **File Count**: Exact number of files
- **Complete File List**: All files with their status (new/modified/deleted)
- **Detailed Commit Message**: Full message with description and bullet points
- **Rationale**: Why these files are grouped together

### Phase 4: User Decision Interface
**Present standardized command options:**
```
COMMIT OPTIONS:
- commit A,B,E          # Commit specific clusters
- commit A-E            # Commit range of clusters  
- commit untested H     # Commit with UNTESTED prefix
- wait R                # Skip cluster R for later
- gitignore F           # Add cluster F files to .gitignore
- gitkeep folder xxx    # Add .gitkeep to folder xxx

UTILITY OPTIONS:
- cleanup               # Remove malformed files
- details C             # Show detailed analysis of cluster C
- modify H              # Edit cluster H contents
- list                  # Show cluster list again
```

### Phase 5: Automated Execution
1. **Process .gitignore Updates**: Add specified patterns and create .gitkeep files
2. **Execute Commits in Order**: Process clusters one by one:
   - `git add` files for the cluster
   - `git commit` with detailed message
   - Handle UNTESTED prefix when specified
3. **Progress Reporting**: Show each commit as it's created
4. **Final Status**: Display summary of completed actions

## Standardized Cluster Presentation Format

**MANDATORY FORMAT for each cluster:**

```markdown
### ✅ **Cluster A: `type(scope): description`**
**Files (X):**
```
file1.js                                          (new/modified/deleted)
file2.md                                          (new/modified/deleted)
folder/file3.py                                   (new/modified/deleted)
```
**Detailed Message:**
```
type(scope): description

Comprehensive description of what this cluster accomplishes
- Specific change 1 with technical details
- Specific change 2 with technical details
- Specific change 3 with technical details
- Impact and benefits of these changes
```
**Rationale:** Explanation of why these files belong together based on timestamps, content, and functionality
```

## Standardized Command Interface

**USER COMMANDS (case-insensitive):**
```
COMMIT ACTIONS:
commit A,B,E            # Commit specific clusters by letter
commit A-E              # Commit range of clusters
commit untested H       # Commit cluster H with UNTESTED prefix
commit all              # Commit all clusters

MANAGEMENT ACTIONS:
wait R                  # Skip cluster R for this session
gitignore F             # Add cluster F files to .gitignore
gitkeep folder xxx      # Add .gitkeep to specified folder

UTILITY ACTIONS:
cleanup                 # Remove malformed/invalid files
details C               # Show detailed analysis of cluster C
modify H                # Edit cluster H file contents
list                    # Redisplay all clusters
status                  # Show current repository status
```

## Execution Requirements

### MANDATORY Workflow Steps:
1. **Always analyze file timestamps** for chronological clustering
3. **Always present clusters A-L** in chronological order
4. **Always use standardized format** for each cluster presentation
5. **Always provide detailed commit messages** with bullet points
6. **Always execute git commands** for approved clusters
7. **Always show progress** during execution

### MANDATORY Commit Message Format:
```
type(scope): concise description

Detailed explanation of what this commit accomplishes
- Specific technical change 1
- Specific technical change 2  
- Specific technical change 3
- Business impact or technical benefit
- Any warnings or special considerations (for UNTESTED commits)
```

### MANDATORY User Interface:
```
# 🔍 Compose Commits Analysis
**Timestamp:** YYYYMMDD-HHmm
**Branch:** branch-name
**Repository:** repo-name

## 📊 Repository State Analysis
- Staged files: X
- Untracked files: Y  
- Deleted files: Z
- Total files to analyze: W

## 📦 Intelligent Clusters (Chronological Order)

[Present each cluster using standardized format]

## 🎯 CLUSTER SELECTION
**Choose which clusters to commit:**

**Commands:**
- commit A,B,E          # Commit specific clusters
- commit untested H     # Commit with UNTESTED prefix  
- wait R                # Skip cluster R
- gitignore F           # Add cluster F to .gitignore
- gitkeep folder xxx    # Add .gitkeep to folder

**Which clusters would you like to commit?**
```

### Example Complete Session:
```
User Input: "commit A,B,E commit untested H wait R gitignore F gitkeep folder conversations"

Expected Actions:
1. Commit clusters A, B, E normally
2. Commit cluster H with UNTESTED prefix
3. Skip cluster R for later
4. Add cluster F files to .gitignore
5. Create .gitkeep in conversations folder
6. Execute git commands for each approved cluster
7. Show progress and final summary
```