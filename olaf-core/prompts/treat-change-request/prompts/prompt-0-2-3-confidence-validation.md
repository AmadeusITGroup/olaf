---
name: convert-confidence-validation
description: Convert the Confidence Validation prompt to standardized template, preserving validation thresholds and investigation recommendations
tags: [prompt, conversion, confidence, validation]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **final_size_path**: path - Path to `5-final-size-decision.md` (REQUIRED)
- **artifacts_root**: path - Folder containing artifacts 1-5 (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and validation

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `final_size_path` and all referenced artifacts are accessible

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Review size, confidence score, and level against thresholds
- Assess evidence quality across artifacts 1-5
- Identify critical unknowns and high-risk assumptions
- Recommend investigations if confidence <80%
- Make final routing decision (APPROVE / CAUTION / INVESTIGATE)

### 3. Validation Phase
You WILL validate results:
- Ensure decision rationale references artifacts and thresholds

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Confidence validation appended to `5-final-size-decision.md` using `../templates/template-confidence-validation.md`

## User Communication

### Progress Updates
- Confirmation of artifact review
- Preliminary evidence quality rating

### Completion Summary
- Final decision and required follow-ups

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Apply thresholds exactly (≥80%, 60-79%, <60%)
- Rule 2: Document unknowns that could shift size category

## Success Criteria
You WILL consider the task complete when:
- [ ] Confidence validated with thresholds
- [ ] Evidence quality assessed
- [ ] Unknowns and assumptions reviewed
- [ ] Final decision made with rationale

## Required Actions
1. Validate inputs
2. Perform validation and recommendations
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Artifacts**: Request paths and retry

⚠️ **Critical Requirements**
- MANDATORY: Threshold-based decision
- NEVER approve without rationale
