---
name: convert-functional-testing-execution
description: Convert the Functional Testing Execution prompt to standardized template, preserving Gherkin-based scenarios and automation patterns
tags: [prompt, conversion, testing, functional, gherkin]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **test_plan_path**: path - `TEST_PLAN_<PROJECT-ID>.md` (REQUIRED)
- **workspace_context**: string - Implemented system/codebase location (REQUIRED)

## User Interaction Protocol
- Propose-Act for conversion and test generation

## Process

### 1. Validation Phase
- Confirm inputs exist and system under test is accessible

### 2. Execution Phase
**Core Logic**:
- Design Gherkin scenarios (Given-When-Then) for user journeys, API, integrations, performance
- Create executable scenarios with specific data and expected outcomes
- Implement automation: framework setup, step definitions, data management, environment config

### 3. Validation Phase
- Ensure coverage across major workflows, rules, edge cases, and integrations
- Verify scenarios run automatically and consistently; integrate with CI

## Output Format
- Deliverables per templates: `../templates/template-functional-test-scenarios.md` and `../templates/template-functional-test-implementation.md`

## User Communication
- Progress: scenario generation and automation setup
- Completion: suite runs, reports generated, and integration with CI

## Domain-Specific Rules
- Rule 1: Business-readable scenarios; executable without manual tweaks
- Rule 2: Keep data and env setup isolated and repeatable

## Success Criteria
- [ ] Gherkin feature files for key scenarios
- [ ] Automated step definitions and runner config
- [ ] CI integration and reports available

## Error Handling
- **Environment Issues**: Provide fallback mocks or instructions
- **Flaky Tests**: Stabilize or quarantine with clear rationale

⚠️ **Critical Requirements**
- MANDATORY: Executable scenarios with reliable automation
- NEVER rely on manual steps for functional test execution
