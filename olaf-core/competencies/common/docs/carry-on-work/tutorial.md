# Carry-On Work: Step-by-Step Tutorial

**How to Execute the "Carry-On Work" Workflow**

This tutorial shows how to resume work from a previous session using carry-over notes.

## Prerequisites

- Previously created carry-over notes using `create carry-over`
- Carry-over files exist in `carry-overs/` directory
- Starting a new OLAF session

## Step-by-Step Instructions

### Step 1: Start New Session
Begin a fresh conversation with OLAF

**User Action:**
1. Open a new conversation/session with OLAF
2. Type the command: `carry on`

**OLAF Response:**
OLAF will search for the most recent carry-over file in the `carry-overs/` directory

### Step 2: Automatic File Loading
**What OLAF Does:**
- Scans `carry-overs/` directory for files
- Identifies the most recent carry-over file by timestamp
- Reads the carry-over file content
- Parses the session summary and context

**You Should See:** Confirmation that carry-over file was found and loaded

### Step 3: Context Restoration
**What OLAF Does:**
- Summarizes what was accomplished in the previous session
- Identifies key decisions and progress made
- Lists next steps that were planned
- Restores relevant file and project context

**You Should See:** Summary of previous session with clear next steps

### Step 4: Continue Working
**User Action:** Proceed with the work
- Review the restored context
- Confirm understanding or ask clarifying questions
- Begin working on the identified next steps
- Continue the conversation naturally

## Verification Checklist

✅ **Most recent carry-over file was loaded**
✅ **Previous session context is accurately summarized**
✅ **Next steps are clearly identified**
✅ **You can continue work without re-explaining context**

## Troubleshooting

**If no carry-over file is found:**
```
Error: No carry-over files found in carry-overs/ directory
```
Solution: You need to create carry-over notes first using `create carry-over`

**If wrong carry-over is loaded:**
Specify the date/time: "carry on from October 25th afternoon session"

**If context seems incomplete:**
- Ask OLAF to elaborate on specific aspects
- Provide additional context as needed
- Consider creating more detailed carry-over notes in future sessions

## Key Learning Points

1. **Automatic Discovery**: OLAF finds the most recent carry-over automatically
2. **Seamless Resumption**: No need to re-explain context from scratch
3. **Timestamped Files**: Carry-over files use timestamps for chronological organization
4. **Session Continuity**: Maintains work continuity across multiple sessions

## Next Steps to Try

- Continue working on the identified next steps
- Create new carry-over notes when ending this session
- Use `stash work` if you need to pause and switch to a different task
- Query work history: "what have I done this week?"

## Expected Timeline

- **Total resumption time:** 1-2 minutes
- **User input required:** Just the command (10 seconds)
- **OLAF execution time:** File loading and context restoration (1-2 minutes)
