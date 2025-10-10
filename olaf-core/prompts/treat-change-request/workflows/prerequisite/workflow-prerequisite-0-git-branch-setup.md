---
name: workflow-prerequisite-0-git-branch-setup
description: Validate current branch and create a compliant feature branch before prerequisite workflows
tags: [workflow, sequential, treat-change-request]
---

# Workflow Prerequisite-0: Git Branch Setup

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

## Workflow Overview

**Purpose**: Ensure all work is performed in an appropriate feature branch, not on main/master branches.

**Input**: Current git repository state

**Output**: Branch validation and setup confirmation

---

## Input Requirements
- **Primary Input**: Current git repository state
- **Secondary Inputs**: N/A
- **Input Format**: Local git repository

## Output Specifications
- **Primary Output**: `prerequisite-0-branch-setup.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute this step first - no skipping

### Prompt Prerequisite-0-1: Git Branch Validation and Creation

**File**: `../../prompts/prompt-prerequisite-0-git-branch-setup.md`

**Input**: Current git repository state

**Output**: `prerequisite-0-branch-setup.md`

**Description**: Validate the current branch and create a new feature branch if necessary, following naming conventions.

**Validation**:
- Current branch identified
- If on main/master, new branch created
- Branch name follows convention: `olaf-work-YYMMDD-HHMM` or user-provided name
- Confirmation that work will proceed on appropriate branch

---

## Data Flow Diagram
```text
[Local git repo state] → [Step 0-0-1: Branch Validation & Creation] → prerequisite-0-branch-setup.md
```

## Error Handling
- **Step Failure**: If git repository not found or branch creation fails, document error and stop
- **Recovery**: Initialize repository or fix permissions; retry step
- **Rollback**: If wrong branch created, delete branch and recreate with correct name

## Completion Criteria
- [ ] Current git branch has been checked
- [ ] If on main/master, new branch has been created and checked out
- [ ] Branch name documented in `prerequisite-0-branch-setup.md`
- [ ] Ready to proceed with demand analysis

## Next Steps
- Proceed to `workflow-prerequisite-1-demand-analysis.md`

## Handoff

**Next workflow**: `workflow-prerequisite-1-demand-analysis.md`

**Provides**: `prerequisite-0-branch-setup.md` with confirmed branch name
