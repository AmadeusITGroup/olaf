# Stash Work - Project Manager Competency

## Purpose
Create a stash record to pause current work and prepare for new work session, similar to carry-over but with explicit work transition messaging.

## Context
- User wants to pause current work and start something new
- Need to preserve current session context for future reference
- Should communicate work transition clearly

## Instructions

### 1. Session Analysis
- Review current conversation and work done
- Identify key accomplishments and current state
- Note any pending tasks or next steps
- Capture repository/workspace state

### 2. Generate Stash Content
Create stash file with format: `stashed-<subject>-YYYYMMDD-HHmm.txt`

**Subject Extraction Rules:**
- Use main topic/feature being worked on
- Keep to 2-3 words maximum
- Use kebab-case format
- Examples: "olaf-framework", "api-integration", "ui-components"

**Content Structure:**
```
STASHED WORK - <timestamp>
==============================

## Work Transition Notice:
🔄 **CURRENT WORK PAUSED** - Moving to new work session
📋 **STASH REASON**: [Brief reason for stashing]

## Current State & What We Did:
[Detailed summary of work completed]

## Repository State:
[Current workspace/git state]

## What's Expected Next:
[Pending tasks and next steps]

## Key Files Modified:
[List of changed files]

## Commands for Resuming:
[Specific commands to resume this work]

## Transition Notes:
✅ Work stashed successfully
🚀 Ready for new work session
```

### 3. File Management
- Save to carry-overs/ directory
- Use timestamp format: YYYYMMDD-HHmm CEDT
- Ensure file is accessible for future reference

### 4. Session Transition Message
After creating stash file, provide clear transition message:
- Confirm work has been stashed
- State readiness for new work
- Provide stash file reference

## Output Format
1. Create stash file in carry-overs/
2. Confirm stash creation with file path
3. Provide transition message
4. Ask what new work to begin

## Success Criteria
- Stash file created with comprehensive work summary
- Clear transition messaging provided
- User understands current work is paused
- Ready to begin new work session