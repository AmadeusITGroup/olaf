# Create Carry-Over - Project Manager Competency

## Purpose
Create a concise carry-over note to capture current session state and enable resuming work in the next session.

## Context
- User wants to end current session and preserve context for next session
- Need to capture current state, accomplishments, and next steps
- Should be concise but sufficient for session continuity

## Instructions

### 1. Session Analysis
- Review current conversation and work completed
- Identify key accomplishments and current state
- Note repository/workspace state and any pending tasks
- Capture what's expected next

### 2. Generate Carry-Over Content
Create carry-over file with format: `carry-over-YYYYMMDD-HHmm.txt`

**Content Structure:**
```
CARRY-OVER NOTE - <timestamp>
================================

## Current State & What We Did:
[Concise summary of work completed this session]

## Repository State:
[Current workspace/git state, modified files]

## What's Expected Next:
[Clear next steps and pending tasks]

## Key Files Modified:
[List of changed files]

## Commands for Next Session:
[Specific commands to continue work]
```

### 3. Timestamp Generation
- Use format: YYYYMMDD-HHmm CEDT
- Get current time using appropriate system command
- Ensure timestamp is accurate for file naming

### 4. File Management
- Save to carry-overs/ directory in workspace root
- Use exact filename format: `carry-over-YYYYMMDD-HHmm.txt`
- Ensure file is accessible for future sessions

### 5. Content Guidelines
**Be Concise but Sufficient:**
- Focus on essential information for continuity
- Include enough context to resume work effectively
- Avoid unnecessary details but don't omit critical information

**State Information:**
- Current progress and accomplishments
- Repository state and modified files
- Pending tasks and blockers
- Next logical steps

## Output Format
1. Create carry-over file in carry-overs/
2. Confirm file creation with exact path
3. Provide brief summary of what was captured
4. Instruct user to start new session and use carry-on functionality

## Success Criteria
- Carry-over file created with comprehensive but concise summary
- File properly named with timestamp
- Contains sufficient information for session continuity
- User understands how to resume in next session

## Session Transition Message
After creating carry-over file:
- Confirm carry-over note has been created
- Provide file path for reference
- Instruct: "To resume this work in your next session, use 'carry on' or 'resume from carry over'"
- Suggest verifying the carry-over content before ending session