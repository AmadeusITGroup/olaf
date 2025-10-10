---
name: convert-test-plan
description: Convert the Test Plan Creation prompt to standardized template, preserving QA strategy, coverage, and validation gates
tags: [prompt, conversion, test-plan, QA]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **design_path**: path - Finalized `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **spec_path**: path - Approved `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)

## User Interaction Protocol
- Propose-Act for conversion and plan generation

## Process

### 1. Validation Phase
- Confirm both inputs exist
- Load template `../templates/template-test-plan.md`

### 2. Execution Phase
**Core Logic**:
- Analyze specification and design to derive strategy, integration/system/E2E coverage
- Define QA strategy, environments, tools, automation, and quality gates
- Generate integration/system/performance/security plans with tickable tasks

### 3. Validation Phase
- Verify coverage of FRs and NFRs
- Verify environments and data requirements are feasible

## Output Format
- Primary deliverable: Test plan per `../templates/template-test-plan.md`

## User Communication
- Progress: analysis complete, sections generated
- Completion: plan ready for review

## Domain-Specific Rules
- Rule 1: Focus on integration/system tests (unit tests in implementation step)
- Rule 2: Provide measurable acceptance criteria

## Success Criteria
- [ ] Coverage for FRs/NFRs
- [ ] Integration/system/performance/security sections complete
- [ ] Template structure followed

## Error Handling
- **Missing Inputs**: Request paths
- **Gaps in Coverage**: Flag and request clarifications

⚠️ **Critical Requirements**
- MANDATORY: Evidence-backed coverage mapping
- NEVER include unit test implementation guidance here
