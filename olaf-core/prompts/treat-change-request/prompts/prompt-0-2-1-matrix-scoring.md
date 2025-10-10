---
name: convert-matrix-scoring
description: Convert the Matrix Scoring prompt to standardized template, preserving scoring logic and evidence linkage
tags: [prompt, conversion, scoring, matrix]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.
- **project_context_path**: path - Path to `../olaf-templates/project-complexity-rating.md` (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and scoring

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all input artifacts exist
- Load scoring criteria from `matrix_spec_path`
- Load project context

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Score 5 dimensions (Scope & Scale, Technical Complexity, Risk Profile, Dependencies & Integration, Project Context)
- For each dimension:
  - Assign score 0-5 using criteria
  - Provide justification with explicit references to evidence
- Calculate Total Score = sum of five dimensions
- Map to size classification

### 3. Validation Phase
You WILL validate results:
- Ensure every score has justification
- Ensure total is in 0-25 range and classification derived

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Matrix scoring following `../templates/template-size-evaluation-matrix.md`

## User Communication

### Progress Updates
- Confirmation of inputs and criteria loaded
- Interim scores per dimension

### Completion Summary
- Final total score and size classification
- Evidence references used

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-0-2-2-size-calculation.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Use only defined criteria from the matrix
- Rule 2: Tie justifications to prior artifacts

## Success Criteria
You WILL consider the task complete when:
- [ ] All 5 dimensions scored with justifications
- [ ] Total score and classification computed
- [ ] Output follows template exactly

## Required Actions
1. Validate inputs and load criteria
2. Perform scoring with evidence
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Artifacts**: Request missing paths
- **Ambiguous Evidence**: Ask for clarifications

⚠️ **Critical Requirements**
- MANDATORY: Evidence-based justifications
- NEVER guess scores without citations
