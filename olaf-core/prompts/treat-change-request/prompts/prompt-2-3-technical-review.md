---
name: convert-technical-review
description: Convert the Technical Review & Design Modification prompt to standardized template, preserving collaborative technical review and change integration
tags: [prompt, conversion, technical-review, collaboration]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **design_path**: path - Validated design `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **stakeholders**: string[] - Technical roles to engage (architects, senior devs, security, DB, UI/UX) (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion, then facilitate review sessions

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `design_path` exists
- Enumerate stakeholder roles to engage

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Coordinate review: agenda, focus on high-risk/blocked items
- Present design summary and critical decisions
- Collect actionable technical feedback
- Integrate refinements (architecture, data model, API, security, performance)
- Update risks, implementation phases, and testing strategy as needed

### 3. Validation Phase
You WILL validate results:
- Ensure all concerns addressed or acknowledged
- Ensure changes documented with rationale
- Capture explicit approval to proceed

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Updated design
- Change documentation: `../templates/template-change-log.md`

## User Communication

### Progress Updates
- Stakeholder engagement status
- Key changes integrated

### Completion Summary
- Approval status and readiness for finalization

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-2-4-design-finalization.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Document change rationale with source of feedback
- Rule 2: Avoid introducing redesign unrelated to review feedback

## Success Criteria
You WILL consider the task complete when:
- [ ] Technical feedback addressed and documented
- [ ] Risks and mitigation updated
- [ ] Explicit approval recorded

## Required Actions
1. Validate inputs
2. Facilitate review and integrate changes
3. Capture approval and communicate next step

## Error Handling
You WILL handle these scenarios:
- **Conflicting Feedback**: Facilitate consensus, document decision
- **Unresolved High-Risk Items**: Escalate and plan mitigations

⚠️ **Critical Requirements**
- MANDATORY: Explicit technical approval
- NEVER bypass unresolved critical risks
