---
name: convert-prerequisite-git-branch-setup
description: Convert the Git Branch Setup prerequisite to standardized template, preserving safety checks and timestamp-based branch naming
tags: [prompt, conversion, git, prerequisite]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
- **repo_path**: path - Target repository (OPTIONAL)

## User Interaction Protocol
- Propose-Act for conversion and branch safety flow

## Process

### 1. Validation Phase
- Verify current workspace is a git repo
- Get current branch and working tree status

### 2. Execution Phase
**Core Logic**:
- If on main/master, propose new branch `olaf-work-<YYMMDD-HHMMSS>` using system timestamp
- Offer user override for custom name, or cancel
- Create and checkout new branch; handle uncommitted changes (proceed, stash, or abort)

### 3. Validation Phase
- Confirm current branch and readiness to proceed
- Document initial state, action taken, final state

## Output Format
- Primary deliverable: `prerequisite-0-branch-setup.md` per `../../templates/template-branch-setup.md`

## Domain-Specific Rules
- Rule 1: Never work on main/master
- Rule 2: Always inform and offer choices for uncommitted changes

## Success Criteria
- [ ] Branch validated or created
- [ ] Uncommitted changes addressed
- [ ] Output document created per template

## Error Handling
- **Not a Git Repo**: Inform and skip with note
- **Branch Creation Failure**: Report and stop

⚠️ **Critical Requirements**
- MANDATORY: Use real system timestamp for proposed branch name
- NEVER proceed on main/master
