<<<<<<< HEAD
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
=======
# Prompt 4-1: Implementation Execution

## Step 0: Prerequisites (MUST DO FIRST)

### 0.1: Analyze Existing Codebase Patterns

**🔍 MANDATORY**: Before implementing anything, analyze how the existing codebase works.

**Required Analysis** (use whatever tools available - file search, code search, file reading):

**Test Patterns:**
- Locate existing test files (e.g., `*Test.java`, `*.test.ts`, `test_*.py`)
- Read test files to understand: test structure, naming conventions, assertion patterns, mocking approaches
- Document findings: "Tests use [framework], located in [directory], follow [pattern]"

**Service/Business Logic Patterns:**
- Locate existing service implementations
- Read service files to understand: dependency injection, transaction management, error handling
- Document findings: "Services use [pattern], transactions via [annotation/pattern], errors handled with [approach]"

**API/Controller Patterns:**
- Locate existing API controllers or handlers
- Read controller files to understand: routing, request/response handling, validation, security
- Document findings: "Controllers use [pattern], security via [mechanism], validation with [approach]"

**Data Access Patterns:**
- Locate existing repository or DAO implementations
- Read data access files to understand: ORM usage, query patterns, transaction boundaries
- Document findings: "Data access uses [ORM/pattern], queries via [method], transactions at [layer]"

**📋 Quality Gate**: If you cannot describe existing patterns with specific examples, you have NOT completed prerequisites.

### 0.2: Load Implementation Context

**Required Preparation:**
- Read the complete implementation plan document
- Identify the first implementable task (no unmet dependencies)
- Extract acceptance criteria for this specific task
- Review related design components
- Note any codebase patterns that should be followed

## Step 1: Test-Driven Development (ENFORCED)

### 1.1: Write Failing Tests FIRST (MANDATORY)

**⚠️ CRITICAL**: Tests must exist and fail BEFORE implementation begins.

**Actions Required:**
1. **Create test file** following existing test patterns you documented
   - Use same directory structure as existing tests
   - Follow naming conventions (e.g., `ServiceImplTest.java`)
   - Use same test framework and imports

2. **Write test cases** covering acceptance criteria
   - One test method per acceptance criterion minimum
   - Include happy path and error cases
   - Use same assertion and mocking patterns as existing tests

3. **Run tests** - verify they ALL FAIL
   - Execute test suite (use build tool, test runner, or IDE)
   - Document results: "Created [X] tests, all failing as expected"

4. **Commit failing tests** (if using version control)
   - Makes TDD process visible and auditable

**📋 Quality Gate**: If tests don't exist, or don't fail initially, STOP. Cannot proceed to implementation.

**Evidence Required:**
```
## Pre-Implementation Test Report

Test File Created: [path/to/TestFile]
Test Count: [number]
Test Status: ALL FAILING ✅ (expected before implementation)
Test Names:
- test_[scenario_1] - FAIL
- test_[scenario_2] - FAIL
- test_[scenario_3] - FAIL
```

### 1.2: Implement Code to Pass Tests (MANDATORY)

**Actions Required:**
1. **Create implementation file** following existing codebase patterns
   - Use same package/module structure
   - Follow naming conventions
   - Use same dependency injection/import patterns

2. **Implement minimal code** to make ONE test pass
   - Focus on simplest test first
   - Run tests after each change
   - Document: "Test [name] now passing"

3. **Iterate** until ALL tests pass
   - Implement remaining functionality
   - Run full test suite frequently
   - Fix failing tests immediately

4. **Verify build success**
   - Run build tool (compile, package, etc.)
   - Ensure no compilation errors
   - Document: "Build: SUCCESS ✅"

**📋 Quality Gate**: If ANY test fails OR build breaks, fix before proceeding.

**Evidence Required:**
```
## Post-Implementation Test Report

Implementation File: [path/to/ImplementationFile]
Test Status: ALL PASSING ✅
Build Status: SUCCESS ✅
Test Results:
- test_[scenario_1] - PASS ✅
- test_[scenario_2] - PASS ✅
- test_[scenario_3] - PASS ✅
```

### 1.3: Refactor and Validate (MANDATORY)

**Actions Required:**
1. **Refactor for quality** (while keeping tests green)
   - Improve code structure and readability
   - Apply design patterns where appropriate
   - Remove duplication
   - Run tests after each refactor

2. **Validate against acceptance criteria**
   - Check each criterion from implementation plan
   - Verify all are met
   - Document any deviations with justification

3. **Generate implementation evidence report**

**📋 Quality Gate**: Cannot mark task complete without evidence report showing all tests passing and build successful.

## Step 2: Implementation Evidence Report (MANDATORY)

### 2.1: Document What Was Implemented

**Generate comprehensive evidence report for the completed task using ../templates/template-implementation-evidence-report.md**

### 2.2: Validation Checklist

Before marking task complete, verify:

- [ ] All tests exist and pass (100% pass rate)
- [ ] Build succeeds without errors
- [ ] All acceptance criteria from plan are met
- [ ] Code follows existing codebase patterns (documented in Step 0)
- [ ] Implementation evidence report is complete
- [ ] Any deviations are documented with justification
- [ ] Known issues are documented with mitigation plans

**📋 Quality Gate**: If ANY checkbox is unchecked, task is NOT complete. Address gaps before proceeding.

## Step 3: Iteration (Continue or Complete)

### Option A: Continue to Next Task
If there are more tasks in the implementation plan:
- Mark current task as complete in plan
- Update task dependencies (tasks dependent on this are now unblocked)
- Select next implementable task (all dependencies met)
- Return to **Step 0** for the next task

### Option B: Complete Implementation Phase
If all tasks are complete:
- Compile final implementation summary
- Run full test suite across all implemented components
- Generate deployment package (if applicable)
- Prepare for Phase 4 Step 2 (Documentation Execution)

## Final Implementation Summary (When All Tasks Complete)

Use **../templates/template-implementation-summary.md** for the final implementation summary report.

---

## Success Criteria for Step 4.1

Implementation execution is complete when:
- [ ] All planned tasks are implemented
- [ ] Each task has implementation evidence report
- [ ] 100% test pass rate across all components
- [ ] Build succeeds without errors
- [ ] All acceptance criteria met
- [ ] Final implementation summary generated
- [ ] Ready for documentation phase

**This approach ensures rigorous, evidence-based implementation with continuous validation and quality enforcement.**
>>>>>>> 82415e9 (Feat: Add comprehensive prompts for design finalization, test planning, documentation strategy, implementation planning, and execution phases)
