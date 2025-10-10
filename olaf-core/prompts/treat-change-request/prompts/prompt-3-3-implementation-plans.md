---
name: convert-implementation-plans
description: Convert the Implementation Plans Creation prompt to standardized template, preserving adaptive task breakdown and TDD integration
tags: [prompt, conversion, implementation, planning]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **design_path**: path - Final `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **spec_path**: path - Approved `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **test_plan_path**: path - `TEST_PLAN_<PROJECT-ID>.md` (OPTIONAL)

## User Interaction Protocol
- Propose-Act for conversion and plan generation

## Process

### 1. Validation Phase
- Confirm inputs exist
- Load templates: `../templates/template-implementation-plans.md`, `../templates/template-implementation-task.md`

### 2. Execution Phase
**Core Logic**:
- Analyze design to identify natural implementation boundaries (data, service, API, integrations)
- Generate adaptive tasks matching actual complexity, not forced phases
- For each task, define acceptance criteria and integrate unit testing via TDD/BDD
- Organize tasks by implementation order based on dependencies

### 3. Validation Phase
- Ensure all design components are covered
- Ensure tasks are actionable, testable, and ordered with dependencies

## Output Format
- Primary deliverable: Implementation plan per `../templates/template-implementation-plans.md`

## User Communication
- Progress: task generation and ordering complete
- Completion: plan ready for development

## Domain-Specific Rules
- Rule 1: Integrate unit testing in every task (TDD/BDD)
- Rule 2: Do not artificially split or combine tasks

## Success Criteria
- [ ] All components covered by tasks
- [ ] Clear acceptance criteria and TDD prompts per task
- [ ] Realistic dependency-based ordering

## Error Handling
- **Gaps in Components**: Flag and request clarifications
- **Over-fragmented Tasks**: Consolidate and document rationale

⚠️ **Critical Requirements**
- MANDATORY: TDD integrated per task
- NEVER force structure contrary to actual complexity
