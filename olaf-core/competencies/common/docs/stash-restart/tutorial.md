# Stash Restart: Step-by-Step Tutorial

**How to Execute the "Stash Restart" Workflow**

This tutorial shows how to resume previously stashed work.

## Prerequisites

- Previously stashed work using `stash work`
- Stash files exist in `carry-overs/` directory
- Ready to resume the stashed task

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Initiate stash restart

**User Action:**
1. Type the command: `stash restart`
2. Optionally specify which stash to resume

**OLAF Response:**
OLAF will search for stashed work files

### Step 2: View Available Stashes
**What OLAF Does:**
- Scans `carry-overs/` directory for stashed files
- Lists all `stashed-*.txt` files
- Displays task names and timestamps
- Shows brief description of each stash

**You Should See:** Numbered list of available stashed work

### Step 3: Select Stash
**User Action:** Choose which stash to resume
```
Option 2: feature-authentication (stashed 2 days ago)
```

**Provide Selection:**
- Enter the number or task name
- Confirm the selection

### Step 4: Context Restoration
**What OLAF Does:**
- Reads the selected stash file
- Parses work context and state
- Summarizes what was being worked on
- Identifies progress made before stashing
- Lists files and tasks involved
- Notes any blockers or issues

**You Should See:** Detailed summary of stashed work

### Step 5: Resume Working
**User Action:** Continue the work
- Review the restored context
- Verify understanding of where you left off
- Ask clarifying questions if needed
- Begin working on the task

## Verification Checklist

✅ **Correct stash file was loaded**
✅ **Work context is accurately restored**
✅ **Progress and state are clear**
✅ **Files and tasks are identified**
✅ **You can continue work without confusion**

## Troubleshooting

**If no stashes found:**
```
No stashed work found in carry-overs/ directory
```
Solution: You need to stash work first using `stash work`

**If wrong stash is loaded:**
- Specify the task name: "stash restart authentication"
- List all stashes first: "show me all stashed work"
- Select by number from the list

**If context seems incomplete:**
- Ask for more details: "what files were being modified?"
- Request specific information: "what was the blocker?"
- Provide additional context as needed

## Key Learning Points

1. **Task-Specific**: Stashes are named by task for easy identification
2. **Detailed State**: More detailed than carry-over notes
3. **Multiple Stashes**: Can maintain multiple stashed tasks
4. **Timestamped**: Files include timestamps for tracking

## Next Steps to Try

- Continue working on the resumed task
- Stash again if you need to switch tasks
- Create carry-over when ending the session
- Clean up completed stashes

## Expected Timeline

- **Total restart time:** 1-2 minutes
- **User input required:** Command and selection (30 seconds)
- **OLAF execution time:** File loading and context restoration (1-2 minutes)
