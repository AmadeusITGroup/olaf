# Prompt Prerequisite-0: Git Branch Setup

## Purpose

Validate the current git branch and ensure work is performed on an appropriate feature branch, not on main or master branches.

---

## Input

- **Current Git Repository**: The git repository where work will be performed
- **Current Branch**: The branch currently checked out

---

## Task Instructions

### Step 1: Check Current Git Branch

1. **Verify Git Repository**
   - Check if the current workspace is a git repository
   - If not a git repository, note this and skip branch validation

2. **Get Current Branch Name**
   - Execute git command to get current branch
   - Document the current branch name

3. **Check Branch Status**
   - Verify if there are uncommitted changes
   - Document the status

### Step 2: Evaluate Branch Appropriateness

Check if the current branch is:

1. **Main Branch**: `main` or `master`
   - If YES: Work should NOT be done on this branch
   - Action required: Create new feature branch

2. **Feature Branch**: Any other branch name
   - If YES: Work can proceed on this branch
   - Action: Document and proceed

### Step 3: Handle Main/Master Branch (if applicable)

If currently on `main` or `master` branch:

1. **Get Current System Timestamp**
   - **IMPORTANT**: Always get the actual current timestamp from the system
   - **For PowerShell (Windows)**: Run `Get-Date -Format "yyMMdd-HHmmss"`
   - **For Bash (Linux/Mac)**: Run `date +%y%m%d-%H%M%S`
   - Capture the output to use in branch name
   - Format: `YYMMDD-HHMMSS`
     - YY = Year (2 digits)
     - MM = Month (2 digits)
     - DD = Day (2 digits)
     - HH = Hour (24-hour format, 2 digits)
     - MM = Minute (2 digits)
     - SS = Second (2 digits)
   - Example: `251008-143045` for October 8, 2025 at 14:30:45

2. **Propose Branch Name**
   - Generate default branch name: `olaf-work-{timestamp}`
   - Use the actual timestamp obtained from the system in step 1
   - Example: `olaf-work-251008-143045`

3. **Ask User for Branch Name**
   - Present the generated branch name to the user
   - Ask: "We are currently on [main/master] branch. To proceed safely, we should create a new feature branch. Proposed name: `olaf-work-{timestamp}`. Would you like to use this name or provide your own?"
   - Wait for user response

4. **User Options**
   - **Accept proposed name**: Use `olaf-work-{timestamp}` with actual system timestamp
   - **Provide custom name**: Use the name provided by user
   - **Cancel**: Do not proceed with orchestrator

5. **Create and Checkout New Branch**
   - Create the new branch from current position
   - Checkout the new branch
   - Verify branch creation was successful
   - Confirm to user: "Now working on branch: [branch-name]"

### Step 4: Handle Uncommitted Changes (if any)

If there are uncommitted changes on main/master:

1. **Warn User**
   - "There are uncommitted changes on [main/master]. These changes will move to the new branch when we create it."

2. **Options**
   - Proceed: Changes will be carried to new branch
   - Stash: Stash changes first, then create branch
   - Abort: User wants to commit or discard changes manually first

### Step 5: Document Branch Setup

Record:

1. **Initial State**
   - Branch before any action
   - Uncommitted changes status

2. **Action Taken**
   - Branch created (if applicable)
   - Branch name used
   - How branch name was determined (generated vs user-provided)

3. **Final State**
   - Current branch after setup
   - Ready to proceed: Yes/No

---

## Output Format

Generate file: `prerequisite-0-branch-setup.md`

Use **../../templates/template-branch-setup.md** to structure the output.

---

## Success Criteria

- [ ] Current git branch identified
- [ ] If on main/master, user was prompted for branch name
- [ ] If on main/master, new branch created and checked out
- [ ] Branch name follows convention or user preference
- [ ] Uncommitted changes handled appropriately (if any)
- [ ] Final branch state documented
- [ ] Safe to proceed with work
- [ ] Output follows template exactly

---

## Tools to Use

- **run_in_terminal**: Execute git and system commands
  - `git branch --show-current` or `git rev-parse --abbrev-ref HEAD` - Get current branch
  - `git status --porcelain` - Check for uncommitted changes
  - **PowerShell**: `Get-Date -Format "yyMMdd-HHmmss"` - Get current timestamp (Windows)
  - **Bash**: `date +%y%m%d-%H%M%S` - Get current timestamp (Linux/Mac)
  - `git checkout -b [branch-name]` - Create and checkout new branch
  - `git stash` - Stash changes (if needed)

---

## Principles

- **Safety First**: Never work directly on main/master branches
- **User Choice**: Always offer user the option to name their branch
- **Clear Communication**: Explain why branch creation is necessary
- **Handle Edge Cases**: Account for uncommitted changes, no git repo, etc.
- **Document Everything**: Record all actions taken

---

## Exit Criteria

Declare: **"Prerequisite Step 0 complete. Working on branch: [branch-name]. Proceeding to demand document gathering."**

---

## Version History

- **v1.0** (2025-10-08): Initial prompt creation for git branch validation

---

**Next Prompt**: `prompt-prerequisite-1-demand-gathering.md`
