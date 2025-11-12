# Prepare Conversation Handover

## Overview

Creates clear, concise handover documents that capture conversation context, key files, decisions, current state, and next steps to ensure smooth transitions between conversation sessions or team members.

## Purpose

Work often spans multiple sessions or involves multiple people, and context can be lost between transitions. This competency solves the problem of context loss by systematically capturing the current state of work, documenting key files and decisions, identifying next steps with clear ownership, and producing structured handover documentation that enables seamless continuation of work.

## Usage

**Command**: `prepare conversation handover`

**Protocol**: Act

**When to Use**: Use this competency when ending a work session that will be continued later, transitioning work to another team member, pausing work due to blockers, or whenever you need to document current context for future reference or continuation.

## Parameters

### Required Inputs
- **author**: Name of the person preparing the handover document

### Optional Inputs
- **next_steps**: Array of specific tasks to be completed next with owners and dependencies
- **context**: Additional context, notes, or important information for the handover
- **timezone**: Timezone for timestamps (defaults to "CEDT")

### Context Requirements
- Current conversation context and history
- Access to handover template
- Understanding of current work state and progress
- Identification of key files and resources involved
- Clarity on blockers, dependencies, and next actions

## Output

**Deliverables**:
- Structured handover document saved to handover directory
- Session metadata (author, timestamp, project context)
- Project state summary (1-2 sentences)
- Key files and resources with descriptions and absolute paths
- Next steps with clear ownership and dependencies
- Important notes, decisions, and context
- References to related documentation

**Format**: Markdown document following the handover template structure with clear sections, absolute file paths, and actionable next steps.

## Examples

### Example 1: End of Day Handover

**Scenario**: Finishing work session on authentication feature, will continue tomorrow

**Command**:
```
prepare conversation handover
```

**Input**:
```
Author: Sarah Chen
Next Steps:
  - Complete OAuth provider integration (Owner: Sarah, Depends on: API keys from DevOps)
  - Write integration tests (Owner: Sarah)
  - Update documentation (Owner: Sarah)
Context: Made good progress on OAuth implementation, waiting for production API keys to complete testing
```

**Result**: Created handover document with current state, files modified (auth-service.py, oauth-handler.py), blocker noted (API keys), clear next steps for tomorrow

### Example 2: Team Member Transition

**Scenario**: Handing off bug fix work to another developer

**Command**:
```
prepare conversation handover
```

**Input**:
```
Author: Alex Thompson
Next Steps:
  - Reproduce memory leak in test environment (Owner: Jamie Lee)
  - Implement fix based on profiling results (Owner: Jamie Lee, Depends on: reproduction)
  - Validate fix in staging (Owner: Jamie Lee)
Context: Profiling identified the leak in background job processor, root cause is unclosed database connections. Detailed findings in /docs/investigation-memory-leak.md
```

**Result**: Comprehensive handover with investigation findings, root cause analysis, clear next steps for Jamie to continue the work

### Example 3: Blocked Work Handover

**Scenario**: Work blocked waiting for external dependency

**Command**:
```
prepare conversation handover
```

**Input**:
```
Author: Michael Rodriguez
Next Steps:
  - Wait for API specification from partner team (Owner: Partner team, ETA: Oct 30)
  - Review and validate API spec when received (Owner: Michael)
  - Begin integration implementation (Owner: Michael, Depends on: spec approval)
Context: Integration design complete, implementation ready to start once we have final API specification. All preparatory work done.
```

**Result**: Handover documenting blocker, what's waiting for, and what happens next when blocker is resolved

## Related Competencies

- **store-conversation-record**: Creates detailed conversation records that complement handover documents
- **work-on-job**: Job work often requires handovers when pausing or transitioning
- **review-progress**: Progress reviews may identify work that needs handover documentation
- **create-changelog-entry**: Significant handover points can be logged in the changelog

## Tips & Best Practices

- Create handovers at natural stopping points - end of day, end of sprint, before context switches
- Use absolute file paths so anyone can locate referenced files without guessing
- Be specific about next steps - vague actions like "continue work" aren't helpful
- Identify blockers explicitly with expected resolution dates when known
- Include enough context for someone unfamiliar with the work to understand the situation
- Document decisions made during the session that affect future work
- Link to related documentation, issues, or resources for additional context
- Update handover documents if circumstances change before work resumes
- Keep handovers concise but complete - aim for clarity over comprehensiveness

## Limitations

- Requires manual identification of key files and next steps - not automatically detected
- Cannot automatically notify the next person - handover distribution is manual
- Does not track whether handover was received or understood
- Cannot automatically update when circumstances change - requires manual revision
- Handover quality depends on author's understanding of what's important to document
- Does not integrate with task management systems - next steps are documentation only

**Source**: `olaf-core/competencies/project-manager/prompts/prepare-conversation-handover.md`
