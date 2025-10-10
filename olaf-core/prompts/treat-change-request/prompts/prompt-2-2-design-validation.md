---
name: convert-design-validation
description: Convert the Design Codebase Validation prompt to standardized template, preserving implementation feasibility checks and evidence gates
tags: [prompt, conversion, design, validation]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **design_path**: path - Path to `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **workspace_context**: string - Target codebase to validate against (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and validation

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `design_path` exists
- Confirm codebase access for searches and reads

### 2. Execution Phase
You WILL execute these operations as needed:

**Tool Operations**:
- `grep_search` + `read_file` to confirm architecture, data model, security, API and workflow feasibility with evidence

**Core Logic**:
- Validate compatibility with existing patterns and dependencies
- Identify constraints, risks, and integration notes
- Create required diagrams (Class, Component, Sequence, API)

### 3. Validation Phase
You WILL validate results:
- Ensure every implementable component cites existing code patterns
- Ensure all required diagrams are embedded

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Enhanced design using `../templates/template-design-enhanced.md`

## User Communication

### Progress Updates
- Confirmation of inputs
- Evidence references found

### Completion Summary
- Implementability results and risks

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-2-3-technical-review.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Evidence must reference file paths and line numbers
- Rule 2: Avoid redesign; focus on feasibility

## Success Criteria
You WILL consider the task complete when:
- [ ] Implementability validated with evidence
- [ ] Diagrams included as required
- [ ] Output follows template exactly

## Required Actions
1. Validate inputs and access
2. Perform evidence-based validation
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Design Conflicts with Patterns**: Recommend alternatives
- **Missing Evidence**: Go deeper or flag

⚠️ **Critical Requirements**
- MANDATORY: Evidence-based feasibility
- NEVER redesign within this step
