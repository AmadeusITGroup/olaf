---
name: convert-implementation-execution
description: Convert the Implementation Execution prompt to standardized template, preserving enforced TDD workflow and evidence reporting
tags: [prompt, conversion, implementation, tdd, evidence]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **implementation_plan_path**: path - `IMPLEMENTATION_PLAN_<PROJECT-ID>.md` (REQUIRED)
- **workspace_context**: string - Codebase location/context (REQUIRED)

## User Interaction Protocol
- Propose-Act for conversion and execution guidance

## Process

### 1. Validation Phase
- Confirm implementation plan exists
- Identify first implementable task (no unmet dependencies)
- Load documented codebase patterns (tests, services, controllers, repositories)

### 2. Execution Phase
**Core Logic (ENFORCED TDD)**:
- Write failing tests first per acceptance criteria and existing patterns
- Run tests and verify they fail; document pre-implementation report
- Implement minimal code to pass tests, iterating until all pass
- Run full build and ensure success; document post-implementation report
- Refactor safely while keeping tests green

### 3. Validation Phase
- Verify acceptance criteria met
- Generate implementation evidence report per `../templates/template-implementation-evidence-report.md`

## Output Format
- Primary deliverables: Evidence reports and updated code per plan
- Final summary: `../templates/template-implementation-summary.md` when all tasks complete

## User Communication
- Progress: failing tests created, tests passing, build status
- Completion: evidence report location and next task selection

## Domain-Specific Rules
- Rule 1: Tests MUST fail before implementation begins
- Rule 2: No task completion without evidence report

## Success Criteria
- [ ] Tests created first and verified failing
- [ ] All tests passing and build success
- [ ] Evidence report completed

## Error Handling
- **Missing Patterns**: Analyze deeper and document before proceeding
- **Failing Build/Tests**: Fix immediately before moving on

⚠️ **Critical Requirements**
- MANDATORY: TDD workflow and evidence reporting
- NEVER proceed without passing tests and build
