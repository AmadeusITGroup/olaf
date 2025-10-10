---
name: convert-risk-assessment
description: Convert the Risk Assessment prompt to standardized template with structured ratings and mitigation, preserving original intent
tags: [prompt, conversion, risk, assessment]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and execution

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm both input artifacts exist and are accessible
- Validate that each contains the expected sections

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Assess 4 dimensions: Business, Technical, Security, Operational
- For each dimension:
  - Apply rating guides (High/Medium/Low)
  - Provide justification based on evidence from inputs
  - Propose mitigations
- Aggregate dimension ratings into overall risk levels

### 3. Validation Phase
You WILL validate results:
- Ensure all 4 dimensions have ratings and justifications
- Ensure top risks and mitigations are listed

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Risk assessment following `../templates/template-risk-assessment.md`

## User Communication

### Progress Updates
- Confirmation inputs validated
- Summary of risk levels per dimension

### Completion Summary
- Overall risk profile and top risks
- Mitigation strategies

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to size evaluation (`workflow-0-2`)

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Use explicit rating guides
- Rule 2: Tie justifications to evidence in inputs

## Success Criteria
You WILL consider the task complete when:
- [ ] All 4 dimensions assessed with ratings and justifications
- [ ] Top 5 risks prioritized with mitigations
- [ ] Output follows template exactly

## Required Actions
1. Validate required inputs
2. Execute assessments per dimension
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Input Artifact**: Request missing path(s)
- **Insufficient Evidence**: Flag and request additional details

⚠️ **Critical Requirements**
- MANDATORY: Use the rating guides
- NEVER omit mitigations for high risks
