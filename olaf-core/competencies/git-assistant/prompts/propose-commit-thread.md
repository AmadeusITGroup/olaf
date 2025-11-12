---
name: propose-commit-thread
description: View git repository changes (new, modified, tracked, untracked files) and propose meaningful, logical commit sets for user approval

## Time Retrieval
Use the common helper: `olaf-core/competencies/common/prompts/time-retrieval.md`.

core_purpose: Analyze what files have changed and group them into sensible commits with clear purposes


---


## Core Purpose


**PRIMARY GOAL**: Help users understand what files have changed in their git repository and organize them into meaningful commit groups.





**UNIVERSAL COMPATIBILITY**: This competency works with any AI agent, any terminal (PowerShell, Bash, etc.), and any git environment. It does not depend on specific tool behaviors or complex shell scripting.





**What this competency does**:


1. **View file changes**: Show what's new, modified, tracked, untracked


2. **Categorize changes**: Group files by type and purpose  


3. **Propose commits**: Suggest logical commit sets with clear messages


4. **Get approval**: Let user review and modify before executing





**What makes a good commit**:


- Clear, single purpose (e.g., "Add documentation", "Fix bug in X", "Remove deprecated files")


- Related files grouped together


- Reasonable size (not too many unrelated files)


- Descriptive commit message explaining the "why"





## Framework Validation


You MUST apply the <olaf-work-instructions> framework.


You MUST pay special attention to:


- <olaf-general-role-and-behavior> - Expert domain approach


- <olaf-interaction-protocols> - Appropriate execution protocol


You MUST strictly apply <olaf-framework-validation>.





## Universal Command Approach


You MUST use simple, robust commands that work across all AI agents and environments:





**Core Principle**: Use the simplest possible commands that work universally


- **Primary**: `git status --porcelain` (works everywhere)


- **Counting**: Use basic pipe commands or manual counting from output


- **Time**: Use simple date commands without complex formatting


- **Parsing**: Analyze git output directly, avoid complex shell scripting





**Windows PowerShell**:


```powershell


# Simple, universal commands


git status --porcelain


git status --porcelain | Measure-Object -Line


Get-Date -Format yyyyMMdd-HHmm


```





**Unix/Linux/macOS Bash**:


```bash


# Simple, universal commands  


git status --porcelain


git status --porcelain | wc -l


date +"%Y%m%d-%H%M"


```





**Fallback Strategy**: If any command fails, proceed with manual analysis of available git output.





## Input Parameters


You MUST request these parameters if not provided by the user:


- **repository_path**: string - Path to git repository (REQUIRED, defaults to current working directory)


- **include_github_issues**: boolean - Check for related GitHub issues (OPTIONAL, default: false for large changesets)


- **commit_strategy**: string - "granular", "feature-based", or "structural" clustering (OPTIONAL, default: auto-detect)


- **auto_execute**: boolean - Execute commits automatically after approval (OPTIONAL, default: false)


- **max_files_per_commit**: integer - Maximum files per commit (OPTIONAL, default: 50)


- **changeset_threshold**: integer - Threshold for large changeset handling (OPTIONAL, default: 100)





## User Interaction Protocol


You MUST follow the established interaction protocol strictly:


- Act / Propose-Act / Propose-Confirm-Act (defined externally)


- Use **Propose-Confirm-Act** protocol for commit execution due to permanent git history impact





## Process





### 1. Enhanced Repository State Assessment


You WILL perform comprehensive repository analysis:





**Basic Validation**:


- Confirm repository_path exists and is a valid git repository


- Verify git is available and functional


- Check GitHub CLI availability if include_github_issues is true


- Ensure working directory is clean of merge conflicts


- Validate user has commit permissions





**Changeset Scale Detection**:


Use simple, universal approaches:





**Method 1 - Command-based counting**:


```bash


# Universal commands (work in both PowerShell and Bash)


git status --porcelain | wc -l                    # Total files (Unix)


git status --porcelain | Measure-Object -Line     # Total files (PowerShell)


```





**Method 2 - Manual analysis** (if commands fail):


- Run `git status --porcelain` and analyze output directly


- Count lines manually by examining the output


- Look for patterns: `??` (untracked), ` D` (deleted), ` M` (modified)





**Scale Classification**:


- **Small** (< 20 files): Standard analysis


- **Medium** (20-100 files): Enhanced clustering


- **Large** (100+ files): Structural analysis with user confirmation


- **Massive** (500+ files): Require explicit strategy confirmation





### 2. Enhanced Git Status Analysis





**Robust Status Parsing**:


You MUST handle git status codes correctly:


- `??` - Untracked files (new files)


- ` M` - Modified in working tree


- `M ` - Modified in index (staged)


- `MM` - Modified in both index and working tree


- ` D` - Deleted in working tree


- `D ` - Deleted in index


- ` A` - Added to index


- `R ` - Renamed in index


- `C ` - Copied in index





**Large Changeset Handling**:


For repositories with 100+ changes:


1. **Categorize by change type first**


2. **Group by directory structure**


3. **Identify bulk operations** (mass file moves, deletions, additions)


4. **Detect structural changes** (new directories, reorganizations)


5. **Present summary before detailed analysis**





**Change Analysis**:


- For each modified file, analyze `git diff` to understand change scope


- Group related files by:


  - **Feature clusters**: Files changed together for same functionality


  - **File type clusters**: Documentation, tests, configuration, source code


  - **Dependency clusters**: Files that depend on each other


  - **Component clusters**: Files in same module/package/directory





**GitHub Issues Analysis** (if enabled):


- Execute: `gh issue list --state open --limit 50 --json number,title,labels`


- Extract keywords from commit changes (file names, functions, classes)


- Match potential issues by:


  - Title keyword matching


  - Label relevance (bug, enhancement, feature)


  - Recent activity correlation





### 3. Intelligent Clustering Strategies





**Auto-Detection Logic**:


```


IF (untracked_files > 50 AND new_directories > 5):


    strategy = "structural"


ELIF (total_changes > 100):


    strategy = "feature-based" 


ELSE:


    strategy = "granular"


```





**Structural Clustering** (for major reorganizations):


- **Infrastructure commits**: New directory structures, build files


- **Documentation commits**: Bulk documentation additions/moves


- **Code migration commits**: Moving existing code to new locations


- **Configuration commits**: Config files, manifests, settings


- **Cleanup commits**: Deletions, deprecated file removal





**Enhanced Feature-Based Clustering:**


- **Core functionality**: Business logic changes


- **Documentation**: README, docs, comments


- **Tests**: Test files and test data


- **Configuration**: Config files, environment settings


- **Dependencies**: Package files, requirements


- **Tooling**: Scripts, build tools, CI/CD





**Granular Clustering:**


- One commit per logical file change


- Separate commits for each component modification


- Individual commits for each fix/enhancement





**Cluster Validation**:


- Ensure each cluster compiles/builds independently


- Verify no circular dependencies between clusters


- Check that each cluster has coherent purpose





### 4. Proposal Phase





**Commit Thread Proposal**:


Present structured proposal to user with interactive modification capabilities:





```markdown


# 📋 Proposed Commit Thread - {timestamp}





## Repository Analysis


**Repository**: {repository_name}


**Branch**: {current_branch}


**Files Changed**: {total_files} ({untracked_count} untracked, {modified_count} modified, {staged_count} staged)





## 🎯 Proposed Commit Sequence





### Commit 1: {cluster_1_title}


**Files** ({file_count}):


- {file_1} ({change_type})


- {file_2} ({change_type})





**Commit Message**:


```


{proposed_commit_message_1}





- {bullet_point_1}


- {bullet_point_2}


```





**Related GitHub Issues**: #{issue_number} - {issue_title}





**👤 User Actions Available:**


- ✅ APPROVE: Accept this commit as proposed


- 🔄 MODIFY: Change commit message or file grouping


- ➕ SPLIT: Break this commit into smaller commits


- ➖ MERGE: Combine with another commit


- ❌ SKIP: Don't commit these changes now





### Commit 2: {cluster_2_title}


[Same structure repeated for each proposed commit]





## 📊 Summary


- **Total Commits**: {commit_count}


- **Potential GitHub Issues**: {issue_count} matches found


- **Execution Order**: {execution_strategy}





## 🎮 Interactive Commands


Type your choice for each commit:


- `1a` = Approve commit 1


- `1m` = Modify commit 1  


- `1s` = Split commit 1


- `merge 1,2` = Merge commits 1 and 2


- `skip 1` = Skip commit 1


- `execute` = Execute all approved commits


```





### 5. Interactive Modification Phase





**User Interaction Handling**:


- Parse user commands and apply modifications


- Allow real-time commit message editing


- Support file regrouping between commits


- Enable commit merging/splitting operations


- Validate modifications maintain git consistency





**Modification Operations**:


- **Message Edit**: Update commit title and description


- **File Regrouping**: Move files between commit clusters


- **Commit Splitting**: Break large commits into focused smaller ones


- **Commit Merging**: Combine related commits for cleaner history


- **Issue Association**: Link/unlink GitHub issues





### 6. Execution Phase





**Commit Execution** (after final user approval):


- Execute commits in proposed logical order


- For each commit:


  1. Stage specified files: `git add {file_list}`


  2. Create commit with detailed message: `git commit -m "{commit_message}"`


  3. If GitHub issue linked: Update issue with commit reference


- Verify each commit succeeds before proceeding to next


- Provide rollback instructions if any commit fails





**GitHub Issue Integration**:


- Add commit references to related issues


- Update issue labels if commits address specific types (bug fixes, features)


- Close issues if commit messages include closing keywords





### 7. Validation Phase


You WILL validate execution results:


- Confirm all intended files are committed


- Verify git log shows proper commit sequence


- Check GitHub issue updates if applicable


- Validate working directory is clean after execution





## Output Format


You WILL generate outputs following this structure:


- **Analysis Report**: Git status breakdown with change categorization


- **Commit Proposal**: Interactive structured proposal with modification options


- **Execution Summary**: Results of commit operations with git log confirmation





## User Communication





### Progress Updates


- Confirmation when git analysis completes


- GitHub issues analysis results (if enabled)


- Commit clustering completion with cluster count


- Real-time feedback during interactive modification phase





### Interactive Proposal


- Clear presentation of proposed commit sequence


- Available user commands and modification options


- Real-time updates as user modifies proposals


- Confirmation requests before each major operation





### Execution Summary


- Detailed log of each commit operation


- GitHub issue integration results


- Final repository state confirmation


- Instructions for any manual follow-up needed





## Domain-Specific Rules


You MUST follow these constraints:


- Rule 1: **NEVER execute commits without explicit user approval** via Propose-Confirm-Act


- Rule 2: Present commits in logical dependency order (dependencies first)


- Rule 3: Separate infrastructure changes from business logic changes


- Rule 4: Include detailed commit messages with bullet points explaining changes


- Rule 5: Always validate git repository state before and after operations


- Rule 6: Preserve git history integrity - never force push or rewrite committed history





## Success Criteria


You WILL consider the task complete when:


- [ ] Git repository status analyzed and categorized completely


- [ ] Changes clustered into logical, coherent commit groups


- [ ] GitHub issues identified and associated with relevant commits (if enabled)


- [ ] User has interactively reviewed and approved commit proposal


- [ ] All approved commits executed successfully in logical order


- [ ] GitHub issues updated with commit references (if applicable)


- [ ] Repository working directory is clean after execution


- [ ] Git log shows proper commit sequence with detailed messages





## Required Actions (Universal Workflow)


1. **Show file status**: Run `git status --porcelain` (works on all platforms)


2. **Count and summarize**: Use simple counting methods or manual analysis from git output


3. **Group logically**: Organize files into meaningful commit groups by purpose  


4. **Propose commits**: Present clear commit messages and file lists for each group


5. **Get approval**: Let user approve, modify, or reject each proposed commit


6. **Execute safely**: Use standard `git add` and `git commit` commands (universal)





**Universal Git Commands** (work everywhere):


- `git status --porcelain` - Get machine-readable status


- `git add <files>` - Stage files for commit


- `git commit -m "message"` - Create commit with message


- `git log --oneline -n 5` - Verify recent commits





## Enhanced Error Handling


You WILL handle these scenarios:


- **Not a Git Repository**: Provide instructions to initialize or navigate to correct directory


- **Merge Conflicts Present**: Require resolution before proceeding with commit analysis


- **GitHub CLI Not Available**: Skip GitHub integration and proceed with git-only workflow


- **Commit Permission Denied**: Check repository permissions and provide resolution steps


- **GitHub Issue API Failures**: Continue with git operations, log issue integration failures


- **Git Command Failures**: Stop execution, provide specific error details and recovery steps


- **Circular Dependencies in Clusters**: Reorganize clusters to respect dependency order


- **Command Execution Failures**: Fall back to manual analysis of git output


- **Platform Differences**: Use universal git commands, avoid platform-specific syntax


- **AI Agent Limitations**: Work with any AI system, don't depend on specific tool behaviors


- **Large Output Handling**: Process git status output in manageable chunks





**Large Changeset User Confirmation**:


For 100+ files, present summary first:


```markdown


# 🚨 Large Changeset Detected - {total_files} files





## Quick Summary


- **Untracked**: {untracked_count} files


- **Modified**: {modified_count} files  


- **Deleted**: {deleted_count} files


- **Estimated Commits**: {estimated_commits}





## Detected Patterns


- Documentation: {doc_count} files


- Configuration: {config_count} files


- Code: {code_count} files





**⚠️ This is a large changeset. Proceed with detailed analysis?**


- `yes` - Continue with full analysis


- `summary` - Show high-level grouping only


- `abort` - Cancel operation


```





⚠️ **Critical Requirements**


- MANDATORY: Use Propose-Confirm-Act protocol for all commit executions


- MANDATORY: Validate git repository state before any write operations  


- NEVER commit without explicit user approval of final commit sequence


- NEVER force push or rewrite existing git history


- ALWAYS provide rollback instructions for commit operations


- ALWAYS preserve detailed audit trail of all git operations performed