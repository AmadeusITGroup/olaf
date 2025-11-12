# Conversation Handover Note

**Purpose**: Template for creating clear and concise handover documents to ensure smooth transition between conversation sessions or team members.

**Used By**: prepare-conversation-handover.md

**Version**: 1.0

**Last Updated**: 2025-10-27

---

## Template Structure

```markdown
# Conversation Handover Note

**Author:** {AUTHOR_NAME}  
**Timestamp:** {TIMESTAMP} {TIMEZONE}  
**Project:** {PROJECT_NAME}

## Current State
{BRIEF_1_2_SENTENCE_SUMMARY_OF_CURRENT_STATUS}

## Key Files
- **Current Job:** {PATH} - {DESCRIPTION}
- **Changelog:** {PATH} - {LAST_ENTRY_SUMMARY}
- **Other Files:**
  - {PATH} - {PURPOSE}
  - {PATH} - {PURPOSE}

## Next Steps
1. [ ] {TASK_1} (Owner: {WHO})
   - {DETAILS}
   - {DEPENDENCIES}
2. [ ] {TASK_2} (Owner: {WHO})
   - {DETAILS}
   - {DEPENDENCIES}

## Important Notes
- {CRITICAL_INFORMATION_OR_WARNINGS}
- {DEPENDENCIES_OR_BLOCKERS}
- {DECISIONS_MADE_IN_SESSION}

## References
- {LINK_TO_DOCUMENTATION}
- {RELATED_CONVERSATIONS}
- {ADDITIONAL_RESOURCES}
```

---

## Placeholder Guide

- `{AUTHOR_NAME}`: Name of the person preparing the handover
- `{TIMESTAMP}`: Current timestamp in YYYYMMDD-HHmm format
- `{TIMEZONE}`: Timezone abbreviation (e.g., CEDT, UTC, EST)
- `{PROJECT_NAME}`: Name of the project or work area
- `{BRIEF_1_2_SENTENCE_SUMMARY_OF_CURRENT_STATUS}`: Concise summary of where things stand
- `{PATH}`: Absolute or relative file path
- `{DESCRIPTION}`: Brief description of file purpose or content
- `{LAST_ENTRY_SUMMARY}`: Summary of most recent changelog entry
- `{PURPOSE}`: Purpose or role of the file in the project
- `{TASK_N}`: Description of next action item
- `{WHO}`: Person or role responsible for the task
- `{DETAILS}`: Additional information about the task
- `{DEPENDENCIES}`: Prerequisites or blockers for the task
- `{CRITICAL_INFORMATION_OR_WARNINGS}`: Important context that must be communicated
- `{DEPENDENCIES_OR_BLOCKERS}`: Issues preventing progress
- `{DECISIONS_MADE_IN_SESSION}`: Key decisions or agreements reached
- `{LINK_TO_DOCUMENTATION}`: URL or path to relevant documentation
- `{RELATED_CONVERSATIONS}`: References to previous discussions or handovers
- `{ADDITIONAL_RESOURCES}`: Other helpful materials or references

---

## Example

```markdown
# Conversation Handover Note

**Author:** Alice Developer  
**Timestamp:** 20251027-1430 CEDT  
**Project:** OLAF Documentation Restructure

## Current State
Completed audit of project-manager competency pack. Identified one prompt requiring template extraction (prepare-conversation-handover.md).

## Key Files
- **Current Job:** .kiro/specs/olaf-documentation-restructure/tasks.md - Main task list for documentation restructure
- **Changelog:** olaf-data/product/changelog-register.md - Last entry: Completed business-analyst audit
- **Other Files:**
  - .kiro/specs/olaf-documentation-restructure/project-manager-audit-findings.md - Audit results
  - olaf-core/competencies/project-manager/templates/ - Template directory

## Next Steps
1. [ ] Create handover-template.md (Owner: Next Session)
   - Extract inline template from prepare-conversation-handover.md
   - Add proper metadata and placeholder guide
2. [ ] Update prepare-conversation-handover.md (Owner: Next Session)
   - Replace inline template with template reference
   - Test prompt with new template

## Important Notes
- Project-manager pack has excellent template coverage (11/13 prompts compliant)
- Only one template extraction needed for full compliance
- Template pattern: metadata + structure + placeholder guide + example

## References
- Task 13.8: Audit project-manager competency pack prompts
- Requirements 7.2, 9.3, 10.1-10.7 in requirements.md
- Template audit plan in template-audit-plan.md
```

---

## Notes

- Always use absolute paths for file references to avoid ambiguity
- Keep the Current State section to 1-2 sentences maximum
- Include all necessary context but remain concise
- Update timestamps when reusing or referencing handovers
- Verify all links and file paths before finalizing
- Use checkbox format for Next Steps to enable easy tracking
