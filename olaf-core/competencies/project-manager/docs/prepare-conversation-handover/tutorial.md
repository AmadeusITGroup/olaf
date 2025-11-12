# Prepare Conversation Handover: Step-by-Step Tutorial

**How to Execute the "Prepare Conversation Handover" Competency**

This tutorial shows exactly how to create a clear and concise handover document to ensure smooth transition between conversation sessions or team members.

## Prerequisites

- OLAF framework loaded and active
- Active conversation session with work to hand over
- Handover template available
- Understanding of project context and next steps

## Step-by-Step Instructions

### Step 1: Invoke the Competency
**User Action:**
1. Type: `olaf prepare conversation handover`
2. Or use aliases: `olaf conversation handover`, `olaf handover`, `olaf prepare handover`
3. Press Enter

**AI Response:**
Acknowledges request and begins gathering handover information using Act protocol.

### Step 2: Provide Handover Metadata
**User Provides Required Information:**
- **author**: "Jane Smith" (person preparing the handover)
- **next_steps**: Array of tasks to be completed next

**Optional Information:**
- **context**: Additional context or notes
- **timezone**: "CEDT" or "EST" or "PST" (default: CEDT)

**Example:**
```
Author: Jane Smith
Timezone: EST
```

### Step 3: Session Analysis
**What AI Does:**
1. Reviews current conversation context
2. Identifies key files and resources discussed
3. Notes important decisions and discussions
4. Captures current state and progress
5. Extracts action items and blockers

**Analysis Includes:**
- Files created, modified, or referenced
- Commands executed
- Decisions made
- Problems encountered
- Solutions implemented

**You Should See:** Progress update as AI analyzes conversation.

### Step 4: Identify Next Steps
**AI Asks:** "What are the next steps for continuation?"

**User Provides:**
```
Next Steps:
1. Complete OAuth token refresh implementation
   - Owner: @DevLead
   - Dependencies: None
   - Priority: High

2. Update authentication documentation
   - Owner: @TechWriter
   - Dependencies: Step 1 complete
   - Priority: Medium

3. Deploy to staging environment
   - Owner: @DevOps
   - Dependencies: Steps 1 and 2 complete
   - Priority: High
```

### Step 5: Handover Preparation
**What AI Does:**
- Documents file locations and purposes
- Lists pending tasks with priorities
- Notes any blockers or dependencies
- Includes relevant references and links
- Captures important context

**Handover Structure:**
```markdown
# Conversation Handover

**Author:** Jane Smith
**Date:** 2025-10-27 15:30 EST
**Project:** OAuth Authentication Service

## Project State
Currently implementing OAuth 2.0 token refresh functionality. 
Core implementation complete, documentation and deployment pending.

## Key Files and Resources
- `src/auth/token-refresh.js` - Token refresh implementation
- `src/auth/token-validator.js` - Token validation logic
- `tests/auth/token-refresh.test.js` - Test coverage
- `docs/authentication.md` - Documentation (needs update)

## Next Steps
1. **Complete OAuth token refresh implementation**
   - Owner: @DevLead
   - Dependencies: None
   - Priority: High
   - Details: Finalize error handling and edge cases

2. **Update authentication documentation**
   - Owner: @TechWriter
   - Dependencies: Step 1 complete
   - Priority: Medium
   - Details: Document new token refresh flow

3. **Deploy to staging environment**
   - Owner: @DevOps
   - Dependencies: Steps 1 and 2 complete
   - Priority: High
   - Details: Use standard deployment pipeline

## Important Notes
- Token refresh uses PKCE flow for security
- Breaking change: JWT format updated (see DR-20251027-01)
- Staging deployment scheduled for 2025-10-28

## References
- Decision Record: DR-20251027-01
- Job File: JOB-042
- PR: #156
```

### Step 6: Document Generation
**What AI Does:**
- Loads handover template
- Populates all sections with gathered information
- Adds timestamp and metadata
- Includes clear action items
- Ensures all critical information captured

**Template Applied:**
Uses: `olaf-core/competencies/project-manager/templates/handover-template.md`

### Step 7: Save and Confirm
**What AI Does:**
- Saves handover document to configured location
- Creates changelog entry documenting handover creation
- Provides file location and summary

**File Saved To:**
`olaf-data/product/documentations/handovers/handover-20251027-1530.md`

**You Should See:** 
Confirmation with file location and summary of handover contents.

## Verification Checklist

✅ **Session context captured** completely
✅ **Key files documented** with descriptions
✅ **Next steps clearly defined** with owners and dependencies
✅ **Important decisions noted** with references
✅ **Blockers identified** if any
✅ **Timestamp included** in specified timezone
✅ **File paths absolute** for easy reference
✅ **Template structure followed** exactly

## Troubleshooting

**If file paths not absolute:**
- Verify paths start from workspace root
- Convert relative paths to absolute
- Test paths for accessibility

**If next steps unclear:**
- Break down into smaller, specific tasks
- Add more context and details
- Include acceptance criteria

**If template not found:**
Verify template at: `olaf-core/competencies/project-manager/templates/handover-template.md`

**If context seems incomplete:**
- Review conversation history manually
- Add missing information explicitly
- Include references to external documentation

## Key Learning Points

1. **Comprehensive Context**: Handovers capture complete state for seamless continuation
2. **Absolute Paths**: Using absolute paths prevents confusion about file locations
3. **Clear Ownership**: Each next step has designated owner and dependencies
4. **Timestamped**: Timezone-aware timestamps prevent confusion across teams

## Next Steps to Try

- Use handover to resume work in new session
- Share handover with team members for collaboration
- Create handovers at end of each work session
- Link handovers to job files and decision records
- Archive handovers for project history

## Expected Timeline

- **Total time:** 5-8 minutes
- **User input:** 2-3 minutes for metadata and next steps
- **AI execution:** 3-5 minutes for analysis and document generation
