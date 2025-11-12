

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.


## Purpose
Load the latest carry-over note and resume work from the previous session using the captured context and next steps.

## Context
- User wants to resume work from a previous session
- Need to locate and load the most recent carry-over note
- Should continue with the listed next actions from the note

## Instructions

**Important:** Do NOT auto-select or trigger any OLAF competency. Only display the exact "Next Prompt / Workflow" string from the carry-over and let the user decide when to run it.

### 1. Find Latest Carry-Over File (PRIORITY 1)
- **FIRST**: Directly check carry-overs/ directory for latest carry-over file
- Look for pattern: `carry-over-YYYYMMDD-HHmm.txt`  
- Sort by timestamp to find most recent file
- **Framework principle**: Domain expert knows file locations, no workspace wandering

### 2. Load and Parse Carry-Over Content
- Read the latest carry-over file (most recent by timestamp)
- Extract key information:
  - **Immediate Next Action** (Priority 1)
  - Strategic roadmap (Sessions 2-5)
  - Current state and accomplishments
  - Repository state and context dependencies
  - Success metrics for validation
  - Next Prompt / Workflow to Execute (if present)
  - Key Files for Next Session (to open immediately)
- Prepare a concise proposal of the Immediate Next Action and ask the user to agree or disagree before proceeding.

### 3. Present Context to User
**Format:**
``` 
## Resuming from Previous Session

** CRITICAL FIRST STEP - REQUIRED FOR SUCCESS:**
**Close ALL open files/tabs in your VS Code editor NOW**
- Why: Open files create context confusion and prevent proper session restoration
- How: Ctrl+K W (Windows) or Cmd+W (Mac) to close all editors
- Verify: No file tabs should be visible in the editor area
** DO NOT PROCEED until your editor is completely clear**

**Carry-Over File:** [filename]
**Session Date:** [extracted from filename]

### IMMEDIATE NEXT ACTION:
[Priority 1 task from carry-over - highlighted and focused]
- Context: [Why this is the priority]
- Expected Result: [What should happen]

### Previous Session Summary:
[Current state & what was done]

### Repository State:
[Workspace/git state from carry-over]

### Strategic Roadmap (Upcoming Sessions):
[Future sessions roadmap - visible but not primary focus]

### Next Prompt / Workflow
[Slash command or workflow string captured in carry-over]

### Key Files for Next Session
[List of curated files to open first]
- **Prioritize the IMMEDIATE NEXT ACTION** from carry-over
- Present it as the primary focus for this session
- Keep strategic roadmap visible but secondary
- Start executing the immediate action only after file closure confirmation

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
1. **Header:** " Resuming from Previous Session"
2. **Primary Focus:** Highlight the IMMEDIATE NEXT ACTION prominently
3. **Context:** Essential summary and repository state
4. **Roadmap:** Strategic plan visible but secondary
5. **Action (Confirm):** "Proposed immediate next action is above. Do you agree to proceed now? (Yes/No). If No, specify adjustments."

### If No Carry-Over Found:
1. **Message:** "No recent carry-over notes found"
2. **Alternative:** Offer to check for stashed work files
3. **Suggestion:** Propose starting fresh or creating new work plan

### After Loading:
1. **Confirmation:** "Loaded context from: [filename]"
2. **Focus:** Immediately present the priority action as default path
3. **Continuity:** Maintain awareness of strategic roadmap throughout session
4. **Ready State:** "Starting with immediate next action: [action description]"

## Success Criteria
- Latest carry-over file successfully located and loaded
- **Immediate Next Action clearly prioritized and ready to execute**
- Strategic roadmap visible and understood for session planning
- Historical continuity maintained from previous carry-overs
- Context dependencies preserved for seamless work continuation
- User can immediately proceed with priority task or consciously redirect

## Session Management
**Throughout the Session:**
- Keep strategic roadmap in mind when making decisions
- When completing immediate action, reference what comes next in roadmap
- If user requests new carry-over, update roadmap based on progress
- Maintain historical thread by referencing previous sessions when relevant

**Git Hygiene During Session:**
- At logical completion points (immediate action complete, major milestones), check git status
- **If staged files exist**: Propose commit with appropriate message
- **If modified files exist**: Offer to stage them with `git add`
- **Optional**: Offer commit thread competency for organized commits (user choice only)
- Focus on actual project files, not session management artifacts

**Roadmap Awareness:**
- Use strategic roadmap to guide scope and depth of current work
- Suggest transitioning to next roadmap item when immediate action completes
- Adapt roadmap if priorities change, but maintain strategic coherence

## Error Handling
- Handle missing carry-overs directory gracefully
- Skip corrupted or unreadable carry-over files
- If no immediate action found, derive priority from available context
````
