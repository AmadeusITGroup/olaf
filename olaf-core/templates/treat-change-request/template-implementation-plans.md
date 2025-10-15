# Template: Phase-by-Phase Implementation Plans

## Context

I have completed all planning phases: specification, design, test plan, and documentation plan.

**Please provide:**

1. **All Previous Documents**: Paths or content of:
   - Specification document
   - Design document
   - Test plan document
   - Documentation plan document
2. **Team Structure**: Team size, roles, and skill levels
3. **Timeline**: Overall project timeline and any hard deadlines
4. **Development Environment**: Tools, IDEs, CI/CD setup
5. **Code Standards**: Coding conventions, review process, quality gates

## Request

Create **Phase-by-Phase Implementation Plans** that break down the work into manageable chunks.

> **IMPORTANT**: This Implementation Plan includes **unit testing strategy and prompts**. Unit tests are created during development using TDD/BDD practices as part of each implementation task. The Test Plan document covers integration, system, performance, and security testing only.

For each implementation phase, provide:

### 1. Phase Overview

- **Phase Name**: (e.g., "Phase 1: Backend Foundation")
- **Duration**: Time estimate
- **Objectives**: What this phase achieves
- **Success Criteria**: How to know phase is done
- **Team**: Roles and people needed

### 2. Work Breakdown Structure

For each work item:

- **Task ID**: (e.g., TASK-001)
- **Task Name**: Brief description
- **File Path**: File to create/modify
- **Change Type**: ADD | MODIFY | DELETE
- **Purpose**: What this achieves
- **Requirements Covered**: Link to requirements (FR-001, NFR-003, etc.)
- **Design Reference**: Link to design section
- **Prompt to Achieve Goal**: A specific prompt a developer could use to implement this task

Example:

```
TASK-001: Create Service Interface for Feature Detection
File: .../service/FeatureDetectionService.java
Change: ADD
Purpose: Service to detect specific feature characteristics
Requirements: FR-003, NFR-005
Design Reference: Section 5.2 of DESIGN_<PROJECT-ID>.md

Prompt to implement:
"Create a service interface based on the design in section 5.2 of the design document. 
The interface should implement the detection logic as specified. Include proper JavaDoc 
comments explaining the contract, parameters, return values, and exceptions."
```

### 3. Dependencies

- **Task Dependencies**: Which tasks must be done before this one
- **External Dependencies**: Waiting on other teams, external systems
- **Blockers**: Known blockers and mitigation plans

### 4. Code Generation Prompts

For each significant implementation task, provide a prompt that a developer (or AI) could use:

Example:

```
Task: Implement REST Endpoint

Prompt:
"Based on the API design in section 4.3 of the design document, implement the 
REST endpoint as specified in the controller class. 

Requirements:
- Accept the form/DTO as specified in the design
- Validate using @Valid annotation
- Call the appropriate service method
- Return the correct DTO with appropriate HTTP status
- Handle exceptions with proper error responses
- Add proper OpenAPI/Swagger annotations
- Follow existing code patterns in the controller

Include proper error handling and logging as per section 8 of the design document."
```

### 5. Unit Testing Prompts (TDD/BDD Approach)

**CRITICAL**: Unit tests are created DURING implementation as part of this plan, NOT in the Test Plan document.

For each implementation task, provide unit testing prompts following TDD/BDD practices:

Example:

```
Task: Unit Test Validation Logic (TDD - Write Tests First)

Prompt:
"Using TDD approach, FIRST create unit tests for the validation method before implementing it.

Test-First Requirements:
- Write failing tests for all acceptance criteria from the specification
- Create test cases for:
  * All positive test scenarios (valid inputs)
  * All negative test scenarios (invalid inputs, edge cases)
  * Error conditions and exception handling
  * Boundary conditions
- Use appropriate mocking frameworks to mock dependencies
- Follow existing test patterns in the test suite
- Verify tests FAIL before implementation

Then implement the validation method to make tests pass.
Then refactor while keeping tests green."
```

> **Note**: Integration, system, performance, and security testing are covered in the Test Plan. Unit testing belongs here in the Implementation Plan.

### 6. Progress Tracking

- **Checkpoint Schedule**: Daily/weekly checkpoints
- **Metrics to Track**: Tasks completed, tests passing, code coverage
- **Reporting**: Status update template

## Output Format

Create separate implementation plans for each phase:

- IMPLEMENTATION_PLAN_PHASE_1.md (Backend Foundation)
- IMPLEMENTATION_PLAN_PHASE_2.md (Integration & Error Handling)
- IMPLEMENTATION_PLAN_PHASE_3.md (Frontend & UX)
- IMPLEMENTATION_PLAN_PHASE_4.md (Testing & Documentation)

Each plan should be:

- Action-oriented (not just descriptive)
- Include specific prompts developers can use
- Reference back to Specification, Design, and Test Plan
- Provide enough context to implement without re-reading all previous docs

Focus on WHAT to do and HOW to achieve each goal, with prompts that can be used to generate the actual code.

## Expected Output

**Documents:**

- `IMPLEMENTATION_PLAN_PHASE_1.md`
- `IMPLEMENTATION_PLAN_PHASE_2.md`
- `IMPLEMENTATION_PLAN_PHASE_3.md`
- `IMPLEMENTATION_PLAN_PHASE_4.md`

**Structure for Each:**

- Phase Overview
- Work Breakdown (20-30 tasks per phase)
- Task Dependencies
- Implementation Prompts (specific prompts for each task)
- Unit Testing Prompts (TDD/BDD test prompts for each task - tests written FIRST)
- Progress Tracking

**Note**: Each task should include both implementation and unit testing guidance, following TDD principles.