# Stash Restart - Project Manager Competency

## Purpose
Scan the carry-overs folder for stashed work files and propose resuming from available stashed work sessions.

## Context
- User wants to resume previously stashed work
- Need to identify available stashed work sessions
- Should present options clearly for user selection

## Instructions

### 1. Scan Carry-Overs Directory
- List all files in carry-overs/ folder
- Identify stashed work files (pattern: `stashed-*.txt`)
- Also check for regular carry-over files that might contain resumable work
- Sort by timestamp (newest first)

### 2. Analyze Stash Files
For each stashed/carry-over file found:
- Extract timestamp and subject from filename
- Read file header to get work summary
- Identify the stash reason and current state
- Note key accomplishments and next steps

### 3. Present Options
Create a structured list of available work sessions:

**Format:**
```
## Available Stashed Work Sessions:

### 🔄 [Subject] - [Date/Time]
**File:** [filename]
**Summary:** [Brief description of work]
**Status:** [Current state/progress]
**Next Steps:** [What's expected next]

---
```

### 4. User Interaction
- Present all available options clearly
- Ask user which work session to resume
- Provide option to start fresh if no stash appeals
- Include file references for easy identification

### 5. Resume Preparation
Once user selects a stash:
- Confirm the selection
- Provide context from the stash file
- Summarize where work left off
- Present next steps clearly
- Ask for confirmation to proceed

## File Identification Rules

**Stashed Work Files:**
- Pattern: `stashed-*.txt`
- Contains "STASHED WORK" header
- Has work transition notices

**Carry-Over Files:**
- Pattern: `carry-over-*.txt` or `carry-over-*.txt`
- Contains "CARRY-OVER NOTE" header
- May contain resumable work context

**File Exclusions:**
- Skip files older than 30 days unless specifically requested
- Ignore empty or corrupted files
- Skip files without clear work context

## Output Format

### If Stashed Work Found:
1. **Header:** "🔄 Available Stashed Work Sessions"
2. **List:** Structured list of available sessions
3. **Prompt:** "Which work session would you like to resume?"
4. **Options:** Include "Start fresh" option

### If No Stashed Work Found:
1. **Message:** "No stashed work sessions found"
2. **Alternative:** Offer to check for carry-over files
3. **Suggestion:** Propose starting new work

### After Selection:
1. **Confirmation:** "Resuming work on: [subject]"
2. **Context:** Summary of previous work
3. **Status:** Current state and progress
4. **Next Steps:** Clear action items
5. **Question:** "Ready to continue? What would you like to focus on first?"

## Success Criteria
- All available stashed work identified and presented
- Clear options provided to user
- Selected work context properly loaded
- User understands current state and next steps
- Smooth transition back to productive work

## Error Handling
- Handle missing carry-overs directory gracefully
- Skip corrupted or unreadable files
- Provide helpful message if no resumable work found
- Offer alternatives when stash files are incomplete