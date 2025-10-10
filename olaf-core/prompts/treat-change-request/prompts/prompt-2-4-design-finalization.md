---
name: convert-design-finalization
description: Convert the Design Finalization prompt to standardized template, preserving professional formatting, approvals, and implementation readiness
tags: [prompt, conversion, design, finalization]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
- **design_path**: path - Reviewed design `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **tech_approver**: string - Technical lead/architect approver (OPTIONAL)

## User Interaction Protocol
- Propose-Act for conversion and finalization

## Process

### 1. Validation Phase
- Confirm `design_path` exists and loads
- Load change log from technical review if present

### 2. Execution Phase
**Core Logic**:
- Ensure integration validation changes are reflected (diagrams, APIs, DB, security)
- Apply professional formatting standards and complete metadata
- Prepare implementation readiness sections (checklists, env setup, deployment/testing refs)
- Prepare dev team briefing materials summary

### 3. Validation Phase
- Verify template compliance per `../templates/template-design-final.md`
- Confirm approvals and readiness

## Output Format
- Primary deliverable: Finalized design per `../templates/template-design-final.md`

## User Communication
- Progress: formatting applied, metadata updated
- Completion: approvals captured, ready for development handoff

## Domain-Specific Rules
- Rule 1: Update all diagrams and specs to match approved changes
- Rule 2: Record technical approvals and dates

## Success Criteria
- [ ] Template compliance checklist complete
- [ ] Metadata and approvals documented
- [ ] Implementation readiness confirmed

## Error Handling
- **Missing Approvals**: Flag and request approver info
- **Out-of-date Diagrams**: Update or flag with TODOs

⚠️ **Critical Requirements**
- MANDATORY: Full template compliance before handoff
- NEVER mark ready without approvals and complete metadata
