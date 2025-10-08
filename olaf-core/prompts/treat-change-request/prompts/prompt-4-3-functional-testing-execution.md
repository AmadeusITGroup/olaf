# Prompt 4-3: Functional Testing Execution

## Context Loading

Load planning documents and implemented system:

- Review `TEST_PLAN.md` for planned testing scenarios and coverage requirements
- Analyze implemented codebase to understand actual functionality and business logic
- Review documentation to understand user workflows and expected behaviors
- Identify all user-facing features, APIs, and integration points from actual implementation

## Functional Testing Approach

### Gherkin-Based Test Design

Create functional tests as Gherkin scenarios that can be automated:

1. **Business-Readable Tests**
   - Write scenarios in Given-When-Then format
   - Use business language that stakeholders understand
   - Focus on user behaviors and expected outcomes
   - Create scenarios that validate business requirements

2. **Executable Scenarios**
   - Design scenarios that can be automated with testing frameworks
   - Include specific test data and expected results
   - Create scenarios for both positive and negative test cases
   - Ensure scenarios can be run independently and repeatedly

3. **Comprehensive Coverage**
   - Cover all major user workflows and business processes
   - Include edge cases and error conditions as implemented
   - Test integration points and external system interactions
   - Validate business rules and data validation logic

## Test Scenario Generation

### User Journey Testing

**Use Template**: `../templates/template-functional-test-scenarios.md`

**Primary User Workflows**: Refer to the template for complete Gherkin scenario patterns including:
- Feature and scenario structure
- Given-When-Then format examples
- Data-driven scenario outlines with examples
- Error handling and edge case patterns

### API and Integration Testing

**Use Template**: `../templates/template-functional-test-scenarios.md`

**REST API Testing**: Refer to the template for API testing patterns including:
- Successful API call scenarios
- Error handling scenarios
- Authentication and authorization testing

**Integration Scenarios**: See template for patterns covering:
- External system connectivity and data exchange
- Database operations and data consistency
- File processing and data import/export
- Background job processing and scheduling

### Performance and Load Testing

**Use Template**: `../templates/template-functional-test-scenarios.md`

**Performance Scenarios**: Refer to the template for performance testing patterns including:
- Response time under normal load
- System behavior under concurrent load
- Performance acceptance criteria

## Test Automation Implementation

### Test Framework Setup

Generate automated test implementation:

- **Test Runner Configuration**: Set up Cucumber, SpecFlow, or similar Gherkin runner
- **Step Definitions**: Implement step definitions that interact with actual system
- **Test Data Management**: Create test data sets and cleanup procedures
- **Environment Configuration**: Set up test environments and system dependencies

### Test Implementation Patterns

**Use Template**: `../templates/template-functional-test-implementation.md`

Refer to the template for complete implementation patterns including:
- **API Testing Steps**: Step definitions for API health checks, requests, and response validation
- **UI Testing Steps**: Step definitions for browser navigation, user interactions, and page verification
- **Test Data Management**: Setup and cleanup patterns for test data
- **Environment Configuration**: Test environment setup and configuration examples
- **Framework Setup**: Cucumber, SpecFlow, and other framework configuration patterns

## Test Data and Environment Management

### Test Data Strategy

**Data Setup and Cleanup**:

- Create test data that supports all scenario variations
- Implement data cleanup after test execution
- Use database fixtures or API-based data setup
- Ensure test data doesn't interfere with other tests

**Environment Configuration**:

- Set up isolated test environments
- Configure external system mocks or test instances
- Manage test database state and migrations
- Handle configuration differences between environments

### Continuous Testing Integration

**Automated Test Execution**:

- Integrate tests with CI/CD pipeline
- Run tests on code changes and deployments
- Generate test reports and coverage metrics
- Set up alerts for test failures

## Quality Validation

### Test Coverage Assessment

**Functional Coverage**:

- All major user workflows tested
- Business rules and validation logic verified
- Error conditions and edge cases covered
- Integration points validated

**Technical Coverage**:

- API endpoints tested with various inputs
- Database operations verified
- External system interactions validated
- Performance characteristics measured

### Test Maintenance

**Living Test Suite**:

- Tests stay current with implementation changes
- Scenarios reflect actual user behaviors
- Test data remains relevant and realistic
- Test automation stays maintainable and reliable

## Validation Criteria

Functional testing execution is complete when:

- [ ] Key user scenarios are covered by executable Gherkin tests
- [ ] All test scenarios can be run automatically and consistently
- [ ] Business rules and validation logic are verified through test scenarios
- [ ] Critical workflows are tested end-to-end with realistic data
- [ ] Test results provide clear pass/fail feedback with useful error information
- [ ] Test suite can be integrated with continuous integration systems
- [ ] Test coverage meets requirements specified in the test plan

## Output Generation

### Test Suite Deliverables

Generate complete test automation:

- **Gherkin Feature Files**: Business-readable test scenarios
- **Step Definition Code**: Automated test implementation
- **Test Configuration**: Environment setup and test runner configuration
- **Test Data**: Realistic test data sets and fixtures
- **Test Reports**: Execution results and coverage metrics
- **Maintenance Guide**: Instructions for updating and extending tests

### Test Documentation

Create supporting documentation:

- **Test Execution Guide**: How to run tests locally and in CI/CD
- **Test Data Guide**: How to manage and update test data
- **Scenario Mapping**: Traceability from requirements to test scenarios
- **Troubleshooting Guide**: Common test failures and solutions

This prompt ensures AI generates comprehensive, executable functional tests that validate the implemented system against business requirements while providing maintainable automation for ongoing validation.