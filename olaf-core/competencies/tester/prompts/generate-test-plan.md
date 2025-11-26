---
name: generate-test-plan
description: Create a comprehensive test plan based on functional specifications and application requirements.
tags: [testing, quality-assurance, documentation, validation]
---


## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

Use terminal commands, not training data.

Use terminal commands, not training data.

## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **specification**: string - Path to functional specification document
- **application**: string - Name of the application under test
- **test_levels**: array[enum] - (Optional) Test levels to include (unit, integration, system, acceptance)
- **test_types**: array[enum] - (Optional) Test types to include (functional, performance, security, etc.)
- **coverage_target**: number - (Optional) Target test coverage percentage (default: 80)

## Process

1. **Requirement Analysis**:
   - Review functional specification
   - Identify testable requirements
   - Define test objectives
   - Document assumptions

2. **Test Strategy**:
   - Define test levels and types
   - Identify test environment needs
   - Determine entry/exit criteria
   - Plan test data requirements

3. **Test Case Development**:
   - Create test cases in Gherkin format
   - Define test data sets
   - Specify preconditions and postconditions
   - Document expected results

4. **Test Execution Planning**:
   - Schedule test cycles
   - Allocate resources
   - Define risk management approach
   - Plan defect management

## Output/Result Format
Use `[id:templates_dir]tester/test-plan-template.md` to structure the test plan:
- Follow the template's sections for consistency
- Include all required fields from the template
- Replace placeholder content with actual test planning details
- Maintain the structured format for documentation

## Output to USER
1. **Test Plan Overview**:
   - Scope and objectives
   - Test approach
   - Resource requirements
   - Timeline estimates

2. **Detailed Test Cases**:
   - Organized by feature/module
   - Clear pass/fail criteria
   - Traceability to requirements

3. **Supporting Documentation**:
   - Test data guidelines
   - Environment setup instructions
   - Reporting templates

## Domain-Specific Rules
- Rule 1: Align with business requirements
- Rule 2: Ensure test traceability
- Rule 3: Prioritize test cases by risk
- Rule 4: Include both positive and negative tests
- Rule 5: Document test environment needs

## Required Actions
1. Analyze requirements
2. Define test strategy
3. Develop test cases
4. Plan test execution
5. Document test plan

⚠️ **Critical Notes**
- Maintain requirement traceability
- Consider edge cases
- Include regression test planning
- Document known limitations
- Plan for test maintenance