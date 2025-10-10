---
name: convert-routing-logic
description: Convert the Routing Logic prompt to standardized template, preserving orchestrator selection and context package generation
tags: [prompt, conversion, routing, orchestrator]
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
- **orchestrators_dir**: path - Path to orchestrators directory (REQUIRED, default: `../orchestrators/`)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and routing

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `final_size_path` exists and includes size, confidence, effort
- Verify orchestrator file exists for selected size

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Extract size, confidence, effort
- Select target orchestrator per decision table
- Prepare context package with metrics, risk summary, dependencies, artifacts list
- Generate `6-context-package.yaml` with all required fields

### 3. Validation Phase
You WILL validate results:
- Ensure orchestrator exists
- Ensure YAML is complete and valid

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: `6-context-package.yaml` per structure in source prompt

## User Communication

### Progress Updates
- Orchestrator selection result
- YAML generation status

### Completion Summary
- Target orchestrator and key stats

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-0-3-2-routing-documentation.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Orchestrator choice must match size table
- Rule 2: YAML must reference artifacts 1-5

## Success Criteria
You WILL consider the task complete when:
- [ ] Target orchestrator verified
- [ ] YAML generated with all sections populated

## Required Actions
1. Validate inputs and orchestrator availability
2. Generate context package
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Orchestrator**: Report missing file and stop
- **Incomplete Final Size**: Request corrected input

⚠️ **Critical Requirements**
- MANDATORY: Accurate routing based on final size
- NEVER generate incomplete context YAML
