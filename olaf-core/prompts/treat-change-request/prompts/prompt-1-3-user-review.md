---
name: convert-user-review
description: Convert the User Review & Modification prompt to standardized template, preserving collaborative review flow and mandatory approvals
tags: [prompt, conversion, review, collaboration]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **spec_path**: path - Enhanced specification `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **stakeholders**: string[] - Stakeholder roles to engage (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion, then actively engage users per step

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `spec_path` exists
- Verify stakeholder roles to engage (PO, Tech Lead, Domain Expert, Security)

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Present specification summary (FR list, key NFRs, integrations)
- Ask explicit review questions per role
- Collect feedback and apply modifications
- Track change log entries
- Request explicit approval to proceed to finalization

### 3. Validation Phase
You WILL validate results:
- Ensure all assigned roles reviewed
- Ensure conflicts resolved and changes documented
- Ensure explicit approval captured

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Updated `SPECIFICATION_<PROJECT-ID>.md`
- Change documentation: `../templates/template-change-log.md`

## User Communication

### Progress Updates
- Summary presented
- Roles engaged and feedback status

### Completion Summary
- Approval status and next step

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-1-4-finalization.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Active facilitation; do not wait for unsolicited feedback
- Rule 2: Require explicit approval before moving on

## Success Criteria
You WILL consider the task complete when:
- [ ] All roles reviewed and provided feedback
- [ ] Changes applied and logged
- [ ] Explicit approval recorded

## Required Actions
1. Validate inputs
2. Facilitate review and apply changes
3. Capture approval and communicate next step

## Error Handling
You WILL handle these scenarios:
- **Missing Stakeholder Feedback**: Escalate and reschedule
- **Conflicting Feedback**: Facilitate resolution and document decisions

⚠️ **Critical Requirements**
- MANDATORY: Obtain explicit user approval
- NEVER skip this step or assume approval
