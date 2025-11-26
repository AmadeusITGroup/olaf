# Generate Test Plan

## Overview

This competency creates comprehensive test plans based on functional specifications and application requirements. It systematically analyzes requirements to identify testable elements, defines test strategy and approach, generates test cases in Gherkin format, and produces a complete test plan document that guides the testing process from planning through execution.

## Purpose

Effective testing requires thorough planning that aligns with requirements, defines clear objectives, and establishes measurable success criteria. This competency addresses the challenge of creating comprehensive test plans by automating requirement analysis, test case generation, and documentation following industry best practices and standardized templates.

## Usage

**Command**: `generate test plan`

**Protocol**: Propose-Act

**When to Use**: Use this competency when starting a new testing cycle, when functional specifications are ready for test planning, when establishing QA processes for a new project, or when updating test plans for new features or releases.

## Parameters

### Required Inputs
- **specification**: Path to functional specification document
- **application**: Name of the application under test

### Optional Inputs
- **test_levels**: Test levels to include (unit, integration, system, acceptance)
- **test_types**: Test types to include (functional, performance, security, etc.)
- **coverage_target**: Target test coverage percentage (default: 80)

### Context Requirements
- Functional specification document should be accessible in the workspace
- Test plan template automatically referenced from competency templates
- Access to application codebase for test environment planning (optional)

## Output

This competency produces a comprehensive test plan document following industry standards.

**Deliverables**:
- Test plan document saved to `olaf-data/findings/test-plan-<application>-YYYYMMDD-NNN.md`
- Structured test plan following the test-plan-template format
- Test cases in Gherkin format with clear acceptance criteria

**Format**: Structured markdown document following the test-plan-template with sections for scope, approach, test cases, environment requirements, entry/exit criteria, and risk management.

## Examples

### Example 1: Standard Test Plan for New Feature

**Scenario**: A QA engineer needs to create a test plan for a new user authentication feature based on the functional specification.

**Command**:
```
olaf generate test plan
```

**Input**:
```
specification: /path/to/auth-feature-spec.md
application: UserAuthService
```

**Result**: Generated comprehensive test plan including:
- Test objectives aligned with authentication requirements
- Test strategy covering unit, integration, and system testing
- 25 test cases in Gherkin format covering positive and negative scenarios
- Environment setup requirements (test users, database, API endpoints)
- Entry/exit criteria with 80% coverage target
- Risk assessment for authentication security

### Example 2: Comprehensive Test Plan with Multiple Test Types

**Scenario**: A QA lead needs a complete test plan covering functional, performance, and security testing for a payment processing system.

**Command**:
```
olaf generate test plan
```

**Input**:
```
specification: /path/to/payment-spec.md
application: PaymentProcessor
test_levels: ["integration", "system", "acceptance"]
test_types: ["functional", "performance", "security"]
coverage_target: 90
```

**Result**: Comprehensive test plan with:
- Multi-level test strategy (integration, system, UAT)
- Functional test cases for payment flows
- Performance test scenarios for transaction throughput
- Security test cases for PCI compliance
- 90% coverage target with traceability matrix
- Resource allocation for specialized testing

## Related Competencies

- **analyze-business-requirements**: Use before test planning to validate requirements quality
- **review-user-story**: Validate user stories before generating test cases
- **augment-code-unit-test**: Complements test planning with actual unit test implementation
- **review-code**: Use to validate test implementation against test plan
- **generate-detailed-tech-spec**: Provides technical context for test environment planning

## Tips & Best Practices

- Start with clear, testable requirements in the functional specification
- Use Gherkin format (Given-When-Then) for test cases to ensure clarity
- Include both positive and negative test scenarios
- Prioritize test cases based on risk and business impact
- Define clear entry/exit criteria to know when testing is complete
- Plan for test data setup and environment requirements early
- Include regression testing in the test strategy
- Document assumptions and dependencies explicitly
- Consider automation opportunities during test planning

## Limitations

- Test plan quality depends on the clarity and completeness of the functional specification
- Cannot validate the feasibility of test execution without actual environment access
- Does not replace human judgment in risk assessment and test prioritization
- Generated test cases may need refinement based on actual system behavior
- Requires manual review to ensure test coverage aligns with business priorities
- Does not include actual test automation scripts (only test case definitions)

---

**Source**: `olaf-core/competencies/tester/prompts/generate-test-plan.md`
