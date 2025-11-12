# Store Conversation Record: Step-by-Step Tutorial

**How to Execute the "Store Conversation Record" Competency**

This tutorial shows exactly how to create comprehensive conversation records capturing dialogue, actions taken, files affected, and AI models used for future reference and continuity.

## Prerequisites

- OLAF framework loaded and active
- Completed conversation session to record
- Conversation record template available
- Knowledge of AI model being used
- Understanding of record purpose and scope

## Step-by-Step Instructions

### Step 1: Explicit User Request (CRITICAL)
**User Action:**
1. Explicitly request record creation: `olaf store conversation record`
2. Or use aliases: `olaf conversation record`, `olaf save conversation`, `olaf record conversation`
3. Press Enter

**IMPORTANT:** 
- Records are NEVER created automatically
- User must explicitly request record creation
- AI will confirm permission before proceeding

**AI Response:**
Acknowledges request and confirms permission to create record using Act protocol.

### Step 2: Clarify Record Purpose
**AI Asks:** "What is the purpose and scope of this conversation record?"

**User Provides:**
- **conversation_scope**: "OAuth 2.0 token refresh implementation session"
- **record_purpose**: "Document implementation decisions and code changes for team reference"
- **ai_model_used**: "Claude Sonnet 4.5" (MUST be provided by user)

**CRITICAL:** 
- AI model information MUST come from user
- AI will NOT infer or guess the model name
- User must explicitly specify which AI model is being used

**Example:**
```
Scope: OAuth 2.0 token refresh implementation session
Purpose: Document implementation decisions and code changes for team reference
AI Model: Claude Sonnet 4.5
```

### Step 3: Get Timestamp
**What AI Does:**
Retrieves current time using terminal commands:

**Windows:**
```powershell
Get-Date -Format "yyyyMMdd-HHmm"
```

**Unix/Linux/macOS:**
```bash
date +"%Y%m%d-%H%M"
```

**Alternative:** Uses MCP server tool: `mcp_get-local-time_get_local_time`

**Result:** Unique timestamp like "20251027-1530"

**You Should See:** Confirmation of timestamp retrieved.

### Step 4: Validate File Location (CRITICAL)
**What AI Does:**
1. Reads `olaf-data/product/documentations/memory-map.md`
2. Resolves `[id:conversation_records_dir]` reference
3. Verifies resolved path is `olaf-data/product/documentations/conversations/`
4. STOPS if path resolution fails or points elsewhere
5. Ensures directory exists or creates it if missing

**MANDATORY PATH VALIDATION:**
- Path MUST resolve correctly before proceeding
- If validation fails, AI HALTS and asks user for clarification
- No guessing or assuming paths

**You Should See:** Confirmation of validated path.

### Step 5: Create New File
**What AI Does:**
- Creates NEW file: `olaf-data/product/documentations/conversations/conversation-record-20251027-1530.md`
- Uses unique timestamp to prevent filename conflicts
- NEVER appends to existing files
- Initializes file with proper structure

**File Naming:** `conversation-record-[timestamp].md`

### Step 6: Follow Template Structure
**What AI Does:**
Loads and applies conversation record template:

**Template Location:** `olaf-core/competencies/project-manager/templates/conversation-record-template.md`

**Template Sections:**
1. Metadata (date, time, AI model, participants)
2. Conversation Purpose
3. Complete Conversation Narrative
4. Actions Taken
5. Files Affected
6. Key Decisions
7. Next Steps

### Step 7: Capture Complete Conversation
**What AI Does:**
Documents conversation with:

**Format:**
```markdown
# Conversation Record - OAuth 2.0 Token Refresh Implementation

**Date:** 2025-10-27
**Time:** 15:30 EST
**AI Model:** Claude Sonnet 4.5
**Participants:** Jane Smith (Developer)

## Purpose
Document OAuth 2.0 token refresh implementation decisions and code changes

## Conversation Narrative

### Topic 1: Initial Requirements Discussion

**USER said:** "We need to implement automatic token refresh for OAuth 2.0"

**AI said:** "I'll help you implement OAuth 2.0 token refresh with PKCE flow. 
Let's start by reviewing the current authentication implementation."

**AI did:**
1. Read current authentication files
2. Analyzed token validation logic
3. Identified integration points

### Topic 2: Implementation Planning

**USER said:** "What's the best approach for implementing this?"

**AI said:** "I recommend implementing the refresh token endpoint first, 
then adding client-side refresh logic. Here's the plan..."

**AI did:**
1. Created implementation plan
2. Generated task breakdown
3. Identified dependencies

### Topic 3: Code Implementation

**USER said:** "Let's implement the token refresh endpoint"

**AI said:** "I'll create the refresh endpoint with proper error handling..."

**AI did:**
1. Created `src/auth/token-refresh.js`
2. Implemented refresh endpoint logic
3. Added error handling
4. Created test file `tests/auth/token-refresh.test.js`
5. Updated token validator

## Files Affected

**Created:**
- `src/auth/token-refresh.js` - Token refresh endpoint implementation
- `tests/auth/token-refresh.test.js` - Test coverage for refresh logic

**Modified:**
- `src/auth/token-validator.js` - Updated validation for refresh tokens
- `docs/authentication.md` - Added refresh token documentation

**Deleted:**
- None

## Key Decisions
1. Use PKCE flow for enhanced security (DR-20251027-01)
2. Implement automatic refresh 5 minutes before expiry
3. Store refresh tokens in secure HTTP-only cookies

## Next Steps
1. Complete error handling edge cases
2. Deploy to staging environment
3. Update client libraries
```

**Formatting Rules:**
- Clear headings for each distinct topic
- Format: **USER said:** / **AI said:** / **AI did:**
- Numbered lists for actions
- Bullet lists for files
- Relative paths from project root
- Complete narrative, NEVER summarize
- Correct user typos in record

### Step 8: Confirmation
**AI Provides:**
- Conversation record created with file path
- Number of distinct topics documented
- Number of actions captured
- Number of files affected
- Record location confirmation

**You Should See:** 
Complete confirmation with file location and statistics.

## Verification Checklist

✅ **Explicit user request confirmed** (never automatic)
✅ **AI model specified by user** (not inferred)
✅ **New file created** with unique timestamp
✅ **Path validated** via memory-map.md
✅ **Complete conversation captured** (not summarized)
✅ **All actions documented** with tool calls
✅ **Files listed** with relative paths
✅ **Template structure followed** exactly
✅ **Clean markdown formatting** applied

## Troubleshooting

**If path validation fails:**
- Check memory-map.md exists and is readable
- Verify [id:conversation_records_dir] is defined
- Manually specify path if needed

**If file creation fails:**
- Check directory permissions
- Verify sufficient disk space
- Ensure no file locks

**If timestamp conflicts:**
- Wait one minute and retry
- Manually specify different timestamp

**If conversation seems incomplete:**
- Review conversation history manually
- Add missing context explicitly
- Include references to external files

## Key Learning Points

1. **Explicit Permission**: Records only created when explicitly requested by user
2. **AI Model Transparency**: User must specify AI model, never inferred
3. **Complete Narrative**: Full conversation captured, never summarized
4. **Path Validation**: Mandatory validation prevents incorrect file locations
5. **Unique Files**: Each record is separate file, never appended

## Next Steps to Try

- Use stored records for project continuity
- Reference records in handover documents
- Create records at end of significant sessions
- Link records to job files and decision records
- Archive records for project history

## Expected Timeline

- **Total time:** 5-10 minutes
- **User input:** 1-2 minutes for purpose and AI model
- **AI execution:** 4-8 minutes for conversation analysis and documentation
