# Workflow Prerequisite-0: Git Branch Setup

## Overview

**Purpose**: Ensure all work is performed in an appropriate feature branch, not on main/master branches.

**Input**: Current git repository state

**Output**: Branch validation and setup confirmation

---

## Prompt Execution

**Execute this prompt first - no skipping**

### Prompt Prerequisite-0-1: Git Branch Validation and Creation

**File**: `../../prompts/prompt-prerequisite-0-git-branch-setup.md`

**Input**: Current git repository state

**Output**: `prerequisite-0-branch-setup.md`

**Validation**: 
- Current branch identified
- If on main/master, new branch created
- Branch name follows convention: `olaf-work-YYMMDD-HHMM` or user-provided name
- Confirmation that work will proceed on appropriate branch

---

## Completion Criteria

✅ **Workflow complete when**:

1. Current git branch has been checked
2. If on main/master, new branch has been created and checked out
3. Branch name documented
4. Ready to proceed with demand analysis

---

## Handoff

**Next workflow**: `workflow-prerequisite-1-demand-analysis.md`

**Provides**: `prerequisite-0-branch-setup.md` with confirmed branch name
