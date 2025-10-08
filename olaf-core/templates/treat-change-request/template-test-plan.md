# Template: Comprehensive Test Plan

## Context

I have completed the specification and design phases.

**Please provide:**

1. **Specification Document**: Path or content of the specification document
2. **Design Document**: Path or content of the design document
3. **Testing Requirements**:
   - Required code coverage percentage
   - Performance benchmarks
   - Security standards to meet (e.g., OWASP Top 10)
   - Compliance requirements
4. **Test Environment**: Description of available test environments and tools

## Request

Create a **Comprehensive Test Plan** covering all testing activities.

### 1. QA Test Strategy

- **Testing Approach**: V-model, continuous testing, shift-left
- **QA Test Levels**: Integration, System, Acceptance (Unit testing handled in Implementation Plan)
- **Test Types**: Functional, Performance, Security, Usability
- **Entry/Exit Criteria**: When to start/stop testing each level

> **Note**: Unit testing is NOT included in this Test Plan. Unit tests are created during implementation as part of the TDD/BDD development process and are documented in the Implementation Plan (Prompt 3.3).

### 2. Integration Test Plan

For each integration point, specify:

- **Test Scenario ID**: (e.g., IT-001)
- **Integration Point**: What's being integrated
- **Test Steps**: Step-by-step test procedure
- **Expected Result**: What should happen
- **Test Data**: Data setup required
- **Dependencies**: External systems needed

### 3. System Test Plan

For each end-to-end workflow:

- **Test Case ID**: (e.g., ST-001)
- **Workflow**: Complete user workflow
- **Preconditions**: Setup required
- **Test Steps**: Detailed steps
- **Expected Results**: Expected outcomes
- **Acceptance Criteria**: Pass/fail criteria

### 4. Performance Test Plan

- **Load Scenarios**: Expected load patterns
- **Performance Metrics**: Response time, throughput, resource usage
- **Test Tools**: JMeter, Gatling, etc.
- **Success Criteria**: Performance benchmarks
- **Test Data Volume**: Data size for realistic testing

### 5. Security Test Plan

- **Security Test Cases**: Authentication, authorization, injection, etc.
- **Vulnerability Scanning**: Tools to use
- **Penetration Testing**: Scenarios to test
- **Security Checklist**: OWASP Top 10, etc.

### 6. Regression Test Plan

- **Regression Test Suite**: Existing tests to run
- **Impact Analysis**: What existing features might be affected
- **Smoke Tests**: Critical paths to verify

### 7. Acceptance Test Plan

- **UAT Scenarios**: Business user test cases
- **User Roles**: Different user personas
- **Business Workflows**: Real-world scenarios
- **Acceptance Criteria**: Business sign-off requirements

### 8. Test Environment Requirements

- **Environment Setup**: Dev, Test, Stage, Prod
- **Test Data**: How to generate/maintain test data
- **External Dependencies**: Mock services needed

### 9. Defect Management

- **Severity Definitions**: P0, P1, P2, P3
- **Defect Workflow**: Report → Triage → Fix → Verify
- **Exit Criteria**: Maximum allowed defects per severity

## Output Format

Provide test plan as structured document with:

- Test case IDs for traceability
- Clear test steps (Given/When/Then format)
- Expected results
- Requirement coverage matrix (which tests cover which requirements)

Do NOT write actual test code yet - provide the TEST PLAN that developers will follow.

## Expected Output

**Document:** `TEST_PLAN_<PROJECT-ID>.md`

**Structure:**

- QA Test Strategy and Approach (excluding unit testing)
- Integration Test Plan (30+ scenarios)
- System Test Plan (20+ end-to-end flows)
- Performance Test Plan
- Security Test Plan
- Regression Test Plan
- Acceptance Test Plan
- Test Environment Setup
- Defect Management Process

**Note**: Unit testing is documented in the Implementation Plan, not here.