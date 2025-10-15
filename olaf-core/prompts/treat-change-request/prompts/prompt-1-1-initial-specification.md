<<<<<<< HEAD
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
=======
﻿# Prompt 1.1: Initial Specification

## Purpose
Define **WHAT** needs to be built with complete functional and non-functional requirements, focused on business and user needs without implementation details.

## Instructions

Please create a comprehensive specification document based on the provided requirements:

### Input Required
- JIRA ticket or requirements document
- Business context and objectives
- User stories or use cases
- Target system information

### Task
Create a detailed specification document with the following structure:

1. **Executive Summary**
   - Project context and objectives
   - High-level feature description
   - Business value and impact

2. **Functional Requirements (FR-001 through FR-020)**
   - User stories with acceptance criteria
   - Feature descriptions and behaviors
   - Business rules and constraints
   - Input/output specifications

3. **Non-Functional Requirements (NFR-001 through NFR-015)**
   - Performance requirements
   - Security requirements
   - Reliability requirements
   - Scalability requirements
   - Maintainability requirements
   - Usability requirements

4. **Data Model Specification**
   - Conceptual data entities
   - Entity relationships
   - Data validation rules
   - Data lifecycle requirements

5. **Integration Specification**
   - External system dependencies
   - Integration points and interfaces
   - Data exchange formats
   - Communication protocols

6. **Workflow Specification**
   - Business process flows
   - User interaction flows
   - System behavior scenarios
   - Error handling workflows

7. **Constraints and Assumptions**
   - Technical constraints
   - Business constraints
   - Assumptions about environment
   - Risk factors and mitigation

8. **Requirement Traceability Matrix**
   - Mapping requirements to business objectives
   - Priority levels
   - Dependencies between requirements

### Output Format
- **Document Name**: `SPECIFICATION_<PROJECT-ID>.md`
- **Template Reference**: Use `../templates/template-specification.md` as the structure template
- **Length**: As concise as possible while covering all requirements thoroughly
- **Language Style**: Business-oriented, implementation-agnostic descriptions
- **Focus**: WHAT to build, not HOW to build it

### Success Criteria

- All functional requirements have clear acceptance criteria
- Non-functional requirements are measurable
- Requirements are traceable to business objectives
- Document follows the template structure exactly
- Ready for codebase validation in next step

### 🔒 MANDATORY EXIT DECLARATION

Upon completion, you MUST declare:

**"Step 1.1 (Initial Specification) is complete. Proceeding to Step 1.2 (Codebase Validation)."**

⚠️ **YOU MUST NOT:**
- Say "specification is ready for finalization"
- Say "ready for design phase"
- Skip to Step 1.3 or 1.4
- Ask user if they want to proceed to design

**NEXT STEP IS ALWAYS 1.2 - NO EXCEPTIONS**
>>>>>>> 82415e9 (Feat: Add comprehensive prompts for design finalization, test planning, documentation strategy, implementation planning, and execution phases)
