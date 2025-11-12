# Stash Work: Step-by-Step Tutorial

**How to Execute the "Stash Work" Workflow**

This tutorial shows how to temporarily stash current work to switch to a different task.

## Prerequisites

- Active work session with meaningful progress
- Need to switch to a different task
- `carry-overs/` directory exists (created automatically if needed)

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Stash your current work

**User Action:**
1. When you need to switch tasks, type: `stash work`
2. Optionally provide a task name or description

**OLAF Response:**
OLAF will begin analyzing current work to stash

### Step 2: Provide Task Context
**User Action:** Describe the work being stashed
```
Stashing work on user authentication feature - implementing JWT token validation
```

**Provide Details (Optional):**
- **Task Name**: authentication-feature
- **Current State**: JWT validation partially complete
- **Blocker**: Waiting for security team review

### Step 3: Work Analysis
**What OLAF Does:**
- Reviews current conversation and context
- Identifies files being worked on
- Notes progress and current state
- Captures any blockers or issues
- Records next steps planned
- Identifies dependencies

**You Should See:** Confirmation that work is being analyzed

### Step 4: Stash File Creation
**What OLAF Does:**
- Generates detailed stash content
- Creates filename: `stashed-[task-name]-YYYYMMDD-HHmm.txt`
- Writes file to `carry-overs/` directory
- Confirms successful stash creation

**You Should See:** Confirmation message with filename
```
Work stashed to: carry-overs/stashed-authentication-feature-20251027-1530.txt
```

### Step 5: Switch Tasks
**User Action:** Begin new task
- Current work is safely stashed
- Start working on the new task
- Return to stashed work later using `stash restart`

## Verification Checklist

✅ **Stash file created with descriptive name**
✅ **Current work state is captured**
✅ **Files and progress are documented**
✅ **Blockers or issues are noted**
✅ **You can switch tasks confidently**

## Troubleshooting

**If carry-overs/ directory doesn't exist:**
OLAF will create it automatically - no action needed

**If stash seems incomplete:**
- Provide more context: "also include the API endpoint changes"
- Request specific additions: "add notes about the database migration"
- OLAF will update the stash file

**If you need to edit the stash later:**
Files are plain text - you can manually edit them in `carry-overs/` directory

## Key Learning Points

1. **Task-Specific Naming**: Stashes are named by task for easy identification
2. **Detailed Capture**: More detailed than carry-over notes
3. **Multiple Stashes**: Can maintain multiple stashed tasks simultaneously
4. **Timestamped Files**: Files use YYYYMMDD-HHmm format for tracking

## Next Steps to Try

- Switch to your new task
- Resume stashed work later using `stash restart`
- List all stashed work: "show me all stashed work"
- Clean up completed stashes periodically

## Expected Timeline

- **Total stash time:** 1-2 minutes
- **User input required:** Command and task description (30 seconds)
- **OLAF execution time:** Analysis and file creation (1-2 minutes)
