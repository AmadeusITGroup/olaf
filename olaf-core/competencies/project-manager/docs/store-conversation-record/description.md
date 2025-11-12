# Store Conversation Record

## Overview

Creates comprehensive conversation records that capture complete dialogue, actions taken, files affected, AI models used, and full context to preserve project history and enable future reference.

## Purpose

Important conversations and work sessions contain valuable context, decisions, and rationale that can be lost over time. This competency solves the problem of lost institutional knowledge by creating detailed, structured records of conversations that capture the complete narrative, all actions performed, files modified, and context needed to understand what happened and why.

## Usage

**Command**: `store conversation record`

**Protocol**: Act

**When to Use**: Use this competency only when explicitly requested by the user to preserve important conversations, document significant work sessions, capture decision-making processes, or create historical records for future reference, audits, or knowledge transfer.

## Parameters

### Required Inputs
- **user_request**: Explicit user request for record creation (CRITICAL: never create automatically)
- **conversation_scope**: Purpose and scope of the record being created
- **ai_model_used**: Name of the AI model used in the conversation (must be provided by user - never infer)

### Optional Inputs
- **record_purpose**: Specific use case or reason for creating this record

### Context Requirements
- Explicit user permission to create the record
- Access to conversation history and context
- Access to conversation records directory (`[id:conversation_records_dir]`)
- Access to conversation record template
- System time for unique timestamp generation

## Output

**Deliverables**:
- Comprehensive conversation record file with unique timestamp
- Complete conversation narrative (never summarized)
- Accurate dialogue capture (each user request and AI response)
- All actions documented (tool calls, file operations, searches)
- File operations listed (created/modified/deleted with relative paths)
- Clean markdown formatting with corrected user typos
- Organized by logical topic sections

**Format**: Markdown file following conversation record template with structured sections, clear headings for each topic, and formatted dialogue using **USER said:** / **AI said:** / **AI did:** patterns.

## Examples

### Example 1: Feature Development Session

**Scenario**: User wants to preserve a complex feature implementation conversation

**Command**:
```
store conversation record
```

**Input**:
```
User Request: Please create a conversation record for this OAuth implementation session
Conversation Scope: OAuth2 authentication feature implementation
AI Model Used: Claude Sonnet 4.5
Record Purpose: Document implementation decisions and approach for team reference
```

**Result**: Created `conversation-record-20251027-1430.md` with complete dialogue, all code changes, design decisions, and implementation steps documented

### Example 2: Problem-Solving Session

**Scenario**: Debugging session that identified root cause of production issue

**Command**:
```
store conversation record
```

**Input**:
```
User Request: Store this debugging conversation for the incident report
Conversation Scope: Memory leak investigation and root cause analysis
AI Model Used: Claude Sonnet 4.5
Record Purpose: Incident documentation and future reference
```

**Result**: Created record capturing investigation process, profiling results, root cause identification, and fix implementation

### Example 3: Architecture Decision Session

**Scenario**: Important architectural discussion that needs to be preserved

**Command**:
```
store conversation record
```

**Input**:
```
User Request: Create a record of this architecture discussion
Conversation Scope: Microservices vs monolithic architecture decision
AI Model Used: Claude Sonnet 4.5
Record Purpose: Preserve decision rationale for future team members
```

**Result**: Created record with complete discussion, options considered, trade-offs analyzed, and final decision with rationale

## Related Competencies

- **prepare-conversation-handover**: Handovers capture next steps, records capture complete history
- **create-decision-record**: Formal decisions discussed in conversations can be extracted to decision records
- **create-changelog-entry**: Significant conversations can be logged in the changelog
- **review-progress**: Conversation records provide detailed context for progress reviews

## Tips & Best Practices

- Only create records when explicitly requested - never automatically
- Always ask user to specify the AI model being used - never infer or guess
- Create new file for each record with unique timestamp - never append to existing files
- Capture complete conversation - include full narrative, never summarize content
- Validate file path resolution via memory-map.md before creating files
- Organize content by logical topics with clear headings for easy navigation
- Correct obvious user typos in the record for readability
- Use relative paths from project root for all file references
- Include all tool calls and actions performed, not just the results
- Format dialogue consistently using **USER said:** / **AI said:** / **AI did:** patterns

## Limitations

- Requires explicit user request - cannot be triggered automatically
- Cannot infer AI model information - must be provided by user
- Creates new files only - cannot append to or update existing records
- Does not automatically categorize or tag conversations for searchability
- File path must be validated via memory-map.md - cannot guess locations
- Does not integrate with external documentation systems
- Cannot automatically extract decisions or action items - manual extraction needed
- Record quality depends on conversation clarity and completeness

**Source**: `olaf-core/competencies/project-manager/prompts/store-conversation-record.md`
