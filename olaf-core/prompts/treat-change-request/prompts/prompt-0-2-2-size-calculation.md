---
name: convert-size-calculation
description: Convert the Size Calculation prompt to standardized template with confidence and effort estimation, preserving original mapping rules
tags: [prompt, conversion, sizing, effort, confidence]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and calculation steps

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm both input files exist
- Validate matrix result contains total score and preliminary size

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Extract total score and preliminary size from matrix results
- Confirm size against matrix bands and determine final size
- Calculate confidence score and level (High/Medium/Low) using stated factors
- Compute adjusted effort estimate with risk/unknowns/coordination adjustments
- Identify positive/negative confidence factors

### 3. Validation Phase
You WILL validate results:
- Ensure size classification matches matrix bands
- Ensure confidence and effort have clear justifications

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Final size decision following `../templates/template-final-size-decision.md`

## User Communication

### Progress Updates
- Confirmation of total score extraction
- Status of confidence calculation and effort adjustments

### Completion Summary
- Final size classification, confidence, and effort range

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-0-2-3-confidence-validation.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Use only matrix-defined size bands
- Rule 2: Document factors affecting confidence and effort

## Success Criteria
You WILL consider the task complete when:
- [ ] Final size classification confirmed
- [ ] Confidence score and level justified
- [ ] Effort estimate adjusted and justified
- [ ] Output follows template exactly

## Required Actions
1. Validate inputs
2. Perform calculation and adjustments
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Matrix Result**: Request `matrix_result_path`
- **Invalid Score**: Flag and request corrected matrix file

⚠️ **Critical Requirements**
- MANDATORY: Evidence-based confidence assessment
- NEVER override matrix bands arbitrarily
