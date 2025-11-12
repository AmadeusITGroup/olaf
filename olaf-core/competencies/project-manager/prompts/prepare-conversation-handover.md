---
name: prepare-conversation-handover
description: Create a clear and concise handover document to ensure smooth transition between conversation sessions or team members.
tags: [handover, documentation, workflow, collaboration]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **author**: string - Name of the person preparing the handover
- **next_steps**: array[object] - List of tasks to be completed next
- **context**: string - (Optional) Additional context or notes
- **timezone**: string - (Optional) Timezone for timestamps (default: "CEDT")

## Process

1. **Session Analysis**:
   - Review current conversation context
   - Identify key files and resources
   - Note important decisions and discussions
   - Capture current state and progress

2. **Handover Preparation**:
   - Document file locations and purposes
   - List pending tasks with priorities
   - Note any blockers or dependencies
   - Include relevant references and links

3. **Document Generation**:
   - Create structured handover document
   - Add timestamp and metadata
   - Include clear action items
   - Ensure all critical information is captured

## Output/Result Format

Use template: `[id:competencies_dir][competency]/templates/handover-template.md`

The handover document should include:
- Session metadata (author, timestamp, project)
- Project state summary (1-2 sentences)
- Key files and resources with descriptions
- Next steps with owners and dependencies
- Important notes and decisions
- References to related documentation

## Output to USER
1. **Handover Document**:
   - Complete markdown file
   - Saved to `[id:handover]`
   - Ready for sharing or continuation

2. **Confirmation**:
   - Summary of created handover
   - Location of saved file
   - Next steps for the user

## Domain-Specific Rules
- Rule 1: Always include timestamps in specified timezone
- Rule 2: Use absolute paths for all file references
- Rule 3: Keep language clear and concise
- Rule 4: Structure information for easy scanning
- Rule 5: Include all necessary context for handover

## Required Actions
1. Gather session information
2. Identify key files and resources
3. Document current state
4. Define next steps
5. Generate handover document using template

⚠️ **Critical Notes**
- Always use absolute paths
- Include all necessary context
- Keep it concise but complete
- Update timestamps when reusing
- Verify all links and references
