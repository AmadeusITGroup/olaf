---
name: convert-codebase-validation
description: Convert the Codebase Validation & Feasibility Assessment prompt to standardized template, preserving evidence-first validation approach
tags: [prompt, conversion, validation, feasibility]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **spec_path**: path - Path to `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **workspace_context**: string - Target codebase to analyze (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and validation steps

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `spec_path` exists
- Confirm access to codebase for search and reads

### 2. Execution Phase
You WILL execute these operations as needed:

**Tool Operations**:
- `grep_search` to locate relevant components (security, entities, controllers, services, repositories)
- `read_file` to examine actual implementations and cite evidence (file paths, line numbers)

**Core Logic**:
- Validate Security, Data/Transactions, API/Service, State/Workflow, Integration/Performance
- Produce mandatory Mermaid diagrams (ER, State Machine, Integration, Sequence)
- Summarize feasibility with explicit evidence

### 3. Validation Phase
You WILL validate results:
- Ensure every feasible requirement cites at least one code reference
- Ensure all 4 diagrams are present

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Enhanced specification using `../templates/template-specification-enhanced.md`

## User Communication

### Progress Updates
- Confirmation of search progress
- Evidence table count

### Completion Summary
- Feasibility results and key risks

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-1-3-user-review.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Evidence must include file paths and line numbers
- Rule 2: No design decisions in this step

## Success Criteria
You WILL consider the task complete when:
- [ ] Every feasible requirement cites code evidence
- [ ] All mandatory diagrams embedded
- [ ] Validation focuses on feasibility, not design

## Required Actions
1. Validate inputs and access
2. Perform evidence-based analysis
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Insufficient Evidence**: Go deeper or flag requirement
- **Tool Failures**: Provide alternative manual steps

⚠️ **Critical Requirements**
- MANDATORY: Evidence-first validation
- NEVER invent patterns without confirming in codebase
