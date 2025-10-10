---
name: convert-initial-specification
description: Convert the Initial Specification prompt to standardized template focusing on WHAT to build, preserving the structure and success gates
tags: [prompt, conversion, specification]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **requirements_ref**: string - JIRA/requirements document reference (REQUIRED)
- **context**: string - Business context and objectives (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `requirements_ref` provided
- Check access to template `../templates/template-specification.md`

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Produce a specification document focusing on WHAT (not HOW)
- Structure sections: Executive Summary, Functional Requirements, Non-Functional Requirements, Data Model, Integration, Workflow, Constraints & Assumptions, Traceability Matrix

### 3. Validation Phase
You WILL validate results:
- Ensure acceptance criteria for each user story
- Ensure NFRs are measurable
- Ensure requirements trace back to business objectives

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Specification following `../templates/template-specification.md`

## User Communication

### Progress Updates
- Confirmation of inputs
- Section completion updates

### Completion Summary
- Confirmation of readiness for codebase validation

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-1-2-codebase-validation.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Focus on WHAT, not HOW
- Rule 2: Use business-oriented language

## Success Criteria
You WILL consider the task complete when:
- [ ] FRs have acceptance criteria
- [ ] NFRs are measurable
- [ ] Traceability matrix complete

## Required Actions
1. Validate required parameters
2. Produce specification using template
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Requirements Reference**: Request `requirements_ref`
- **Template Access Issues**: Provide fallback structure inline

⚠️ **Critical Requirements**
- MANDATORY: Do not include design or implementation details
- ALWAYS follow template structure
