---
name: create-feature-for-pr
description: Extract features from integration branch to create a feature branch and PR to main
tags: [git, feature, branch, pr, workflow]
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

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **source_branch**: string - Source branch to extract from (REQUIRED - user selects from numbered list, cannot be main or master)
- **target_branch**: string - Target branch for PR (REQUIRED - user selects from numbered list, typically main or master)
- **feature_name**: string - Name of the feature to extract (REQUIRED)
- **feature_description**: string - Brief description of what the feature does (REQUIRED)
- **files_to_extract**: array - List of files from source branch (OPTIONAL - will be discovered)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Confirm-Act for all destructive operations and branch creation
- Act for file discovery and documentation generation
- Propose-Act for final PR creation

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Check git status and ensure clean working directory
- Discover all available branches: `git --no-pager branch -a`
- Present numbered list of available branches for source selection (exclude main/master)
- Present numbered list of available branches for target selection (typically main/master)
- Request user selection for source and target branches
- Validate user has provided feature name and description
- Verify access to both selected source and target branches

### 2. Branch Selection Phase
You WILL execute these operations:

**Branch Discovery**:
- List all branches: `git --no-pager branch -a`
- Filter and present source branch options (exclude main/master) as numbered list
- Request user to select source branch by number
- Filter and present target branch options (typically main/master) as numbered list  
- Request user to select target branch by number
- Confirm selected branches with user

### 3. Feature Discovery Phase
You WILL execute these operations:

**Feature File Identification**:
- Switch to selected source branch: `git checkout [user_selected_source_branch]`
- Pull latest changes: `git pull origin [user_selected_source_branch]`
- Ask user to identify which specific files and folders make up their feature
- List the current directory structure to help user identify feature files
- Do NOT compare branches - focus on identifying the complete feature file set

**Interactive File Selection**:
- Present current files and folders to user for identification
- Ask user to specify which files belong to their feature
- Allow iterative refinement of file list as user identifies more components
- Confirm final file selection with user before proceeding

### 4. Documentation Generation Phase
You WILL create feature documentation:

**Documentation Creation**:
- Generate `docs/olaf-[feature_name].md` with:
  - Feature overview and purpose
  - Bootstrap sequence integration explanation
  - Context switch functionality description
  - Mermaid diagrams showing workflow
  - File structure and dependencies
- Request user guidance for documentation content
- Allow user review and iteration of documentation

### 5. Branch Creation and File Extraction Phase
You WILL execute following protocol requirements:

**Target Branch Preparation**:
- Switch to target branch: `git checkout [target_branch]`
- Pull latest changes: `git pull origin [target_branch]`
- Create feature branch: `git checkout -b feature/[feature_name]`

**File Extraction Process**:
- For each selected file, checkout from source: `git checkout [source_branch] -- [file_path]`
- Identify files that exist on target but need deletion for feature to work
- Stage all changes: `git add .`
- Commit changes: `git commit -m "feat: [feature_description]"`

**Branch Publishing**:
- Push feature branch: `git push origin feature/[feature_name]`
- Generate GitHub compare URL: `https://github.com/[repo]/compare/[target_branch]...feature/[feature_name]`

### 6. PR Preparation Phase
You WILL generate PR materials:
- Create PR title following conventional commits format
- Generate comprehensive PR description including:
  - Feature overview
  - Files changed summary
  - Testing instructions
  - Breaking changes (if any)
- Present PR materials to user for review

### 7. Cleanup Phase
You WILL offer cleanup options:
- Ask user if local feature branch should be deleted
- Update target branch to latest: `git checkout [target_branch] && git pull origin [target_branch]`
- Update source branch with latest target: `git checkout [source_branch] && git pull origin [target_branch] && git push origin [source_branch]`

## Output Format
You WILL generate outputs following this structure:
- Feature documentation: `docs/olaf-[feature_name].md`
- GitHub compare URL for PR creation
- PR title and description text
- Summary of all files extracted and operations performed

## User Communication

### Progress Updates
- Confirmation when all branches are discovered and presented to user
- Confirmation when user has selected source and target branches
- Confirmation when branches are analyzed and file differences found
- Status updates during file selection process
- Confirmation when documentation is generated and ready for review
- Updates during branch creation and file extraction
- Confirmation when feature branch is pushed and PR materials are ready

### Completion Summary
- List of all files extracted from integration to feature branch
- Location of generated documentation
- GitHub compare URL for PR creation
- PR title and description for copy-paste use
- Status of branch cleanup operations

### Next Steps
You WILL clearly define:
- GitHub PR creation using provided URL and materials
- Any manual testing or validation required
- Integration branch maintenance status

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER create files directly on feature branch without user confirmation
- Rule 2: Focus on identifying complete feature file set, not branch comparisons
- Rule 3: Feature branch MUST be created from latest target branch
- Rule 4: Source branch CANNOT be main or master
- Rule 5: Target branch is typically main or master
- Rule 6: Documentation MUST include Mermaid diagrams for workflow visualization
- Rule 7: PR description MUST include comprehensive change summary
- Rule 8: Source branch MUST be updated with latest target after feature extraction
- Rule 9: ALWAYS ask user before deleting local branches
- Rule 10: Use --no-pager option with git commands that support it and may produce paginated output (like diff, log, branch -a)

## Success Criteria
You WILL consider the task complete when:
- [ ] Source and target branches selected by user from numbered lists
- [ ] Feature files successfully identified and confirmed by user
- [ ] Feature documentation generated and approved by user
- [ ] Feature branch created from latest target branch
- [ ] All selected files extracted from source branch
- [ ] Changes committed and pushed to origin
- [ ] GitHub compare URL provided to user
- [ ] PR title and description generated and presented
- [ ] Branch cleanup options offered to user
- [ ] Source branch updated with latest target branch

## Required Actions
1. Validate repository state and branch access
2. Discover and confirm feature files with user interaction
3. Generate comprehensive feature documentation
4. Create feature branch and extract files following git best practices
5. Provide PR creation materials and cleanup options

## Error Handling
You WILL handle these scenarios:
- **Branch Access Issues**: Verify remote branches exist and provide manual checkout instructions
- **Merge Conflicts During File Extraction**: Stop process and request user resolution
- **Documentation Generation Failures**: Request user input for missing information
- **Push Failures**: Provide alternative push strategies and troubleshooting
- **File Not Found in Source Branch**: Verify file paths and offer manual selection
- **Dirty Working Directory**: Request user to commit or stash changes before proceeding
- **Network Issues During Git Operations**: Provide offline alternatives and retry instructions

⚠️ **Critical Requirements**
- MANDATORY: Always create feature branch from target branch, never from source branch
- MANDATORY: Source branch cannot be main or master
- MANDATORY: Confirm all file selections with user before extraction
- NEVER delete files without explicit user confirmation
- ALWAYS verify source branch updates are successful
- ALWAYS provide rollback instructions for each major operation
- NEVER proceed with file extraction if working directory is not clean
- ALWAYS generate comprehensive documentation before code extraction