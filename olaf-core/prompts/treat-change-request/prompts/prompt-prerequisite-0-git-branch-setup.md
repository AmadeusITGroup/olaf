---
name: validate-git-branch-setup
description: Validate current git branch and ensure work is performed on appropriate feature branch, not on main or master branches, with automated branch creation
tags: [git, branch-management, safety, workflow-setup, prerequisite]
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
- **workspace_path**: string - Path to git repository workspace (OPTIONAL, default: current directory)
- **branch_prefix**: string - Prefix for generated branch names (OPTIONAL, default: "olaf-work")
- **force_branch_creation**: boolean - Force creation of new branch even if on feature branch (OPTIONAL, default: false)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for git branch validation due to safety-critical nature

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm workspace path exists and is accessible
- Validate git repository presence in workspace
- Check git command availability and permissions
- Verify ability to create and checkout branches

### 2. Execution Phase

<!-- <git_repository_validation> -->
**Git Repository Validation:**
You MUST verify git repository status:
- You WILL check if current workspace is a git repository using `git rev-parse --git-dir`
- You MUST handle case where workspace is not a git repository
- You WILL document repository status and proceed accordingly
- If not a git repository, you MUST note this and skip branch validation with clear documentation
<!-- </git_repository_validation> -->

<!-- <current_branch_analysis> -->
**Current Branch Analysis:**
You WILL analyze current git branch status:
- You MUST get current branch name using `git branch --show-current` or `git rev-parse --abbrev-ref HEAD`
- You WILL check for uncommitted changes using `git status --porcelain`
- You MUST document current branch name and working directory status
- You WILL assess whether current branch is appropriate for work
<!-- </current_branch_analysis> -->

<!-- <branch_appropriateness_evaluation> -->
**Branch Appropriateness Evaluation:**
You MUST evaluate current branch safety:
- You WILL identify if current branch is `main` or `master` (protected branches)
- You MUST determine if work should proceed on current branch
- You WILL assess risk level of working on current branch
- For protected branches (main/master): Work should NOT proceed without new branch creation
- For feature branches: Work can proceed safely on current branch
- You MUST document evaluation decision with clear rationale
<!-- </branch_appropriateness_evaluation> -->

<!-- <timestamp_generation> -->
**System Timestamp Generation:**
You MUST obtain current system timestamp for branch naming:
- You WILL execute appropriate command based on operating system:
  - **PowerShell (Windows)**: `Get-Date -Format "yyMMdd-HHmmss"`
  - **Bash (Linux/Mac)**: `date +%y%m%d-%H%M%S`
- You MUST capture actual system output for timestamp
- Format specification: YYMMDD-HHMMSS (6 digits date + 6 digits time)
- Example: `251008-143045` for October 8, 2025 at 14:30:45
- You WILL use this timestamp for branch name generation
<!-- </timestamp_generation> -->

<!-- <branch_creation_workflow> -->
**Branch Creation Workflow (if required):**
You WILL execute branch creation when on protected branches:

**Step 1: Generate Branch Name**
- You MUST create default branch name: `{branch_prefix}-{timestamp}`
- You WILL use actual system timestamp obtained in previous step
- Example result: `olaf-work-251008-143045`

**Step 2: User Interaction for Branch Name**
- You MUST present generated branch name to user
- You WILL ask: "Currently on [{current_branch}] branch. To proceed safely, creating new feature branch. Proposed name: `{generated_name}`. Accept this name or provide your own?"
- You MUST wait for user response and handle all options:
  - **Accept proposed**: Use generated name with system timestamp
  - **Provide custom**: Use user-specified branch name
  - **Cancel**: Abort branch creation and document decision

**Step 3: Handle Uncommitted Changes**
If uncommitted changes exist on protected branch:
- You MUST warn user: "Uncommitted changes detected on [{protected_branch}]. These will move to new branch."
- You WILL provide options:
  - **Proceed**: Changes carry to new branch (default)
  - **Stash**: Stash changes first using `git stash`
  - **Abort**: User handles changes manually first

**Step 4: Create and Checkout New Branch**
- You MUST create new branch using `git checkout -b {branch_name}`
- You WILL verify branch creation success
- You MUST confirm to user: "Now working on branch: [{branch_name}]"
- You WILL document successful branch creation with timestamp
<!-- </branch_creation_workflow> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for systematic git branch validation
- Use imperative language throughout branch management operations
- Include comprehensive error handling for all git operations
- Ensure branch safety before allowing work to proceed
- Document all branch operations with clear rationale

### 3. Validation Phase
You WILL validate branch setup results:
- Confirm current branch is appropriate for work (not main/master)
- Verify no uncommitted changes remain on protected branches
- Validate branch creation was successful if new branch was created
- Ensure git repository is in stable state for continued work
- Document final branch state and readiness to proceed

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Branch setup documentation using template structure
- Branch status report: Initial and final branch states with change log
- Safety confirmation: Verification that work can proceed safely
- File location: `prerequisite-0-branch-setup.md` in current working directory

## User Communication

### Progress Updates
You WILL provide these status confirmations:
- Confirmation when git repository status is validated
- Status of current branch analysis and appropriateness evaluation
- Progress updates during branch creation workflow (if applicable)
- Confirmation when timestamp generation and branch naming is complete
- Final validation results for branch setup completion

### Completion Summary
You WILL provide comprehensive completion information:
- Initial branch state: Original branch name and status
- Action taken: Branch created, no action needed, or user cancelled
- Final branch state: Current working branch after setup
- Safety status: Confirmed safe to proceed with work
- Branch naming: How branch name was determined (generated vs user-provided)

### Next Steps
You WILL clearly define:
- Branch setup complete and ready for demand document gathering
- Working branch confirmed: [{final_branch_name}]
- Git repository in stable state for continued workflow
- Proceeding to prerequisite step 1: Demand document gathering

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER allow work to proceed directly on main or master branches
- Rule 2: ALWAYS obtain actual system timestamp for branch naming, never use placeholder values
- Rule 3: Branch creation MUST be user-confirmed before execution
- Rule 4: Uncommitted changes MUST be handled appropriately before branch operations
- Rule 5: Git operations MUST be validated for success before proceeding
- Rule 6: Branch naming MUST follow convention: {prefix}-{timestamp} or user preference
- Rule 7: All git operations MUST include error handling and recovery procedures
- Rule 8: Documentation MUST record all actions taken with clear rationale

## Success Criteria
You WILL consider the task complete when:
- [ ] Git repository status validated (present or absent documented)
- [ ] Current branch identified and appropriateness evaluated
- [ ] Protected branch handling completed if required (main/master)
- [ ] System timestamp obtained using actual terminal commands
- [ ] Branch creation completed successfully if required
- [ ] User confirmation obtained for branch name if applicable
- [ ] Uncommitted changes handled appropriately if present
- [ ] Final branch state documented and validated as safe for work
- [ ] Branch setup documentation generated following template structure
- [ ] Ready to proceed status confirmed with next step defined

## Required Actions
1. Validate git repository presence and accessibility
2. Execute systematic branch analysis and safety evaluation
3. Generate system timestamp for branch naming if required
4. Create new branch following user confirmation if on protected branch
5. Document complete branch setup process with final status confirmation

## Error Handling
You WILL handle these scenarios:
- **No Git Repository**: Document absence and skip branch validation with clear explanation
- **Git Command Failures**: Provide specific error messages and troubleshooting guidance
- **Branch Creation Failures**: Diagnose issues and provide alternative approaches
- **Uncommitted Changes Conflicts**: Guide user through change management options
- **Permission Issues**: Identify permission problems and provide resolution steps
- **User Cancellation**: Document cancellation and provide guidance for manual branch setup
- **Timestamp Generation Failures**: Provide fallback timestamp methods and manual alternatives
- **Branch Name Conflicts**: Handle existing branch names and suggest alternatives

**Critical Requirements**
- MANDATORY: Follow Act protocol for all git branch operations
- MANDATORY: Obtain actual system timestamp using terminal commands, never use training data
- NEVER proceed with work on main or master branches without creating feature branch
- NEVER create branches without user confirmation and appropriate naming
- ALWAYS validate git operations for success before declaring completion
- ALWAYS handle uncommitted changes appropriately before branch operations
- ALWAYS document all actions taken with clear rationale and timestamps
- ALWAYS ensure git repository is in stable state before proceeding to next workflow step
- EXIT DECLARATION: "Prerequisite Step 0 complete. Working on branch: [{branch_name}]. Proceeding to demand document gathering."