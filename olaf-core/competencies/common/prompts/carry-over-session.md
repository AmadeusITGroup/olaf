## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.

## Purpose
Produce a single actionable prompt to continue the work in the next session, plus a minimal context and a file list with full absolute paths so the next session avoids searching.

## Context
- User wants to end current session and preserve context for next session
- Need only the next-session prompt and essential file paths to continue work
- Should be concise but sufficient for immediate continuation

## Instructions


### 1. Session Analysis (Secondary)
- Skip recapping accomplishments. Do not document what was done.
- Only capture what is strictly needed to run the next-session prompt successfully.

### 2. File Context Analysis (NEW)
**BEFORE creating carry-over content:**
- Identify ALL files that will be needed for next session continuation
- List files with **full absolute paths** (e.g., `c:\Users\<user>\coderepos\<repo>\...`) to avoid any search friction
- Group files by category (Architecture/Design, Development Plans, Implementation, etc.)
- Include directories where new work will be created
- **Framework principle**: Next session should not waste time searching for files

### 3. Generate Carry-Over Content
Create carry-over file with format: `carry-over-YYYYMMDD-HHmm.txt`

**Content Structure:**
```
CARRY-OVER NOTE - <timestamp>
================================

## Next-Session Prompt (run this first):
[Exact slash-command or natural-language prompt to paste and run]
- Example: /olaf-carry-on-session

## Brief Context (1–3 lines):
[What was just done and what this next step will achieve]

## Key Files for Next Session (absolute paths):
[One full absolute path per line, ordered by importance. Include directories where new work will be created.]

## Repo State (optional, 1–2 bullets):
[Branch / notable modified files if relevant]

## Success Check (1 line):
[How we’ll know the next step worked]
```
**⚠️ CRITICAL**: Next session MUST start with closing all open editor files
- Users often ignore this instruction causing context confusion
- Explicitly confirm file closure before proceeding with immediate action
- This prevents carry-over context from mixing with current editor state

## Success Metrics:
[How to validate progress and completion]

### 4. Timestamp Generation
- Use format: YYYYMMDD-HHmm CEDT
- Get current time using appropriate system command
- Ensure timestamp is accurate for file naming

### 5. File Management
- Save to carry-overs/ directory in workspace root
- Use exact filename format: `carry-over-YYYYMMDD-HHmm.txt`
- Ensure file is accessible for future sessions

### 6. Content Guidelines
- Focus on producing a single actionable next-session prompt.
- Include a minimal 1–3 line context only if required to run the prompt.
- Provide a list of key files with full absolute paths; order by importance.
- Do not document past accomplishments or strategic roadmaps here.
- Do not auto-trigger competencies; only output the exact prompt to run next.

## Output Format
1. Create carry-over file in carry-overs/
2. Confirm file creation with exact path
3. Show the Next-Session Prompt and the Key Files list (absolute paths)
4. Instruct user to start the next session and run the prompt

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
````
