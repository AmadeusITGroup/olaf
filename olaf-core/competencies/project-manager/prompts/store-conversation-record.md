---

name: store-conversation-record

description: Create comprehensive conversation record capturing dialogue, actions taken, files affected, and AI models used

tags: [conversation, record, documentation, archive, history]

---
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.

- **user_request**: string - Explicit user request for record creation

- **conversation_scope**: string - Purpose and scope of the record

- **ai_model_used**: string - AI model name used in conversation (must be provided by user)

- **record_purpose**: string - Optional specific use case for the record



## Process



1. **Verify Record Creation Permission**:

   - Confirm explicit user request for record creation (CRITICAL: never create automatically)

   - Clarify purpose and scope of the record with user

   - **IMPORTANT**: Explicitly ask user to specify which AI model is being used

   - Do not attempt to infer or guess AI model - get this information directly from user



2. **Get Timestamp**:

   - Get current time in YYYYMMDD-HHmm format using terminal commands:

     - Windows: `Get-Date -Format "yyyyMMdd-HHmm"`

     - Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

   - Use MCP server tool: `mcp_get-local-time_get_local_time` as alternative

   - You WILL use terminal commands, not training data for timestamps

   - Ensure unique timestamp for each conversation record



3. **Validate File Location Before Creation**:

   - **CRITICAL**: Read `[id:ack_dir]memory-map.md` to resolve `[id:conversation_records_dir]`

   - **MANDATORY**: Verify the resolved path is `olaf-data/product/documentations/conversations/`

   - **STOP**: If path resolution fails or points elsewhere, HALT and ask user for clarification

   - **ENSURE**: Directory exists or create it if missing using create_directory tool



4. **Create New File**:

   - Write file: `[id:conversation_records_dir]conversation-record-[timestamp].md`

   - **Create new file for each record - never append to existing files**

   - Use unique timestamp to ensure no filename conflicts

   - Initialize file with proper structure



4. **Follow Template Structure**:

   - Read file: `[id:competencies_dir][competency]/templates/project-manager/conversation-record-template.md`

   - Apply template structure to organize content:

     - Complete conversation narrative (never summarize)

     - Accurate dialogue capture (each user request and AI response)

     - All actions documented (tool calls, file operations, searches)

     - File operations listed (created/modified/deleted with relative paths)

     - Clean Markdown formatting with corrected user typos



## Output Format

Follow template structure: `[id:competencies_dir][competency]/templates/project-manager/conversation-record-template.md`



Structure with logical topic sections:

- Clear headings for each distinct request/topic

- Format: **USER said:** / **AI said:** / **AI did:**

- Numbered lists for actions, bullet lists for files

- Relative paths from project root (e.g., `\ack\prompts\file.md`)



## Output to USER

- Conversation record created: [file path with timestamp]

- Topics documented: [number of distinct conversation topics]

- Actions captured: [number of tool calls and operations]

- Files affected: [number of files created/modified/deleted]

- Record location: `[id:conversation_records_dir]conversation-record-[timestamp].md`



## Record Creation Rules

- Rule 1: CRITICAL - Only create records when explicitly requested by user, never automatically

- Rule 2: Always get AI model information directly from user - never infer or guess

- Rule 3: Create new file for each record with unique timestamp - never append to existing

- Rule 4: Capture complete conversation - include full narrative, never summarize content

- Rule 5: **MANDATORY PATH VALIDATION** - Always resolve [id:conversation_records_dir] via memory-map.md before file creation

- Rule 6: **FAIL-SAFE** - If path validation fails, STOP and request user guidance rather than guess location

