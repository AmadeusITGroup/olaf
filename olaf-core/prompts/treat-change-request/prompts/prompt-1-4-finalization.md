---
name: convert-specification-finalization
description: Convert the Specification Finalization & Formatting prompt to standardized template, preserving formatting, metadata, and approval gates
tags: [prompt, conversion, specification, finalization]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **spec_path**: path - User-modified `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **primary_reviewer**: string - Reviewer name (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and finalization

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `spec_path` exists
- Load change log/notes from review process if available

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Analyze and validate user changes for consistency and feasibility
- Apply formatting standards (headings, lists, tables, code blocks)
- Update metadata: version, date, status, reviewers, history
- Ensure change log updated with rationale

### 3. Validation Phase
You WILL validate results:
- Ensure all required sections present and complete
- Ensure FRs have acceptance criteria and NFRs are measurable
- Ensure cross-references and links valid

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Finalized specification per `../templates/template-specification-final.md`

## User Communication

### Progress Updates
- Formatting applied
- Metadata updated

### Completion Summary
- Finalization status and readiness for design

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to Phase 2 (Design)

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Apply template formatting completely
- Rule 2: Maintain technical feasibility and consistency

## Success Criteria
You WILL consider the task complete when:
- [ ] Template compliance checklist fully met
- [ ] Metadata complete and accurate
- [ ] Document approved and ready for design

## Required Actions
1. Validate inputs
2. Apply formatting and update metadata
3. Validate completeness and feasibility

## Error Handling
You WILL handle these scenarios:
- **Broken Links/Refs**: Fix or flag with TODO
- **Incomplete Sections**: Request missing content

⚠️ **Critical Requirements**
- MANDATORY: Full template compliance
- NEVER mark ready for design without checklist completion
