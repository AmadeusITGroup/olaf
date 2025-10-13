# Carry-On Work - Project Manager Competency

## Purpose
Load the latest carry-over note and resume work from the previous session using the captured context and next steps.

## Context
- User wants to resume work from a previous session
- Need to locate and load the most recent carry-over note
- Should continue with the listed next actions from the note

## Instructions

### 1. Locate Repository Root
- Determine the current workspace root directory
- Ensure carry-overs/ directory exists

### 2. Find Latest Carry-Over File
- Scan carry-overs/ directory for carry-over files
- Look for pattern: `carry-over-YYYYMMDD-HHmm.txt`
- Sort by timestamp to find the most recent file
- Handle variations in naming (carry-over vs carry-over)

### 3. Load and Parse Carry-Over Content
- Read the latest carry-over file
- Extract key information:
  - Current state and accomplishments
  - Repository state
  - Expected next steps
  - Modified files
  - Specific commands

### 4. Present Context to User
**Format:**
```
## 🔄 Resuming from Previous Session

**Carry-Over File:** [filename]
**Session Date:** [extracted from filename]

### Previous Session Summary:
[Current state & what was done]

### Repository State:
[Workspace/git state from carry-over]

### Next Steps:
[What's expected next from carry-over]

### Modified Files:
[List of files that were changed]
```

### 5. Continue with Next Actions
- Present the next steps clearly
- Ask user which action to start with
- Provide context for decision making
- Be ready to execute the planned next steps

## File Identification Rules

**Carry-Over File Patterns:**
- Primary: `carry-over-YYYYMMDD-HHmm.txt`
- Alternative: `carry-over-YYYYMMDD-HHmm.txt`
- Contains "CARRY-OVER NOTE" header
- Has timestamp in filename

**Selection Logic:**
- Use most recent file by timestamp
- Prefer files from last 7 days
- Skip corrupted or unreadable files

## Output Format

### If Carry-Over Found:
1. **Header:** "🔄 Resuming from Previous Session"
2. **Context:** Full summary from carry-over note
3. **Next Steps:** Clear presentation of planned actions
4. **Question:** "Which of these next steps would you like to start with?"

### If No Carry-Over Found:
1. **Message:** "No recent carry-over notes found"
2. **Alternative:** Offer to check for stashed work files
3. **Suggestion:** Propose starting fresh or creating new work plan

### After Loading:
1. **Confirmation:** "Loaded context from: [filename]"
2. **Summary:** Brief recap of where work left off
3. **Options:** Present next steps as actionable choices
4. **Ready State:** "Ready to continue - what would you like to focus on first?"

## Success Criteria
- Latest carry-over file successfully located and loaded
- Context properly presented to user
- Next steps clearly identified and actionable
- User understands current state and can make informed decisions
- Smooth transition back to productive work

## Error Handling
- Handle missing carry-overs directory gracefully
- Skip corrupted or unreadable carry-over files
- Provide helpful message if no recent carry-overs found
- Offer alternatives when carry-over content is incomplete
- Fall back to stash-restart functionality if appropriate