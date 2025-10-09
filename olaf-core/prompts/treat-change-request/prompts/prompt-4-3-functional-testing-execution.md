---
name: execute-functional-testing-comprehensive
description: Execute comprehensive functional testing through AI-driven test scenario generation, automation implementation, and validation following Gherkin-based approach
tags: [functional-testing, test-automation, gherkin-scenarios, quality-assurance]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **test_plan_path**: string - Path to TEST_PLAN.md for planned testing scenarios and coverage requirements (REQUIRED)
- **codebase_path**: string - Path to implemented codebase to understand actual functionality (REQUIRED)
- **documentation_path**: string - Path to generated documentation for user workflows and expected behaviors (REQUIRED)
- **project_id**: string - Project identifier for test file naming and tracking (REQUIRED)
- **testing_framework**: string - Testing framework to use (cucumber, specflow, pytest-bdd) (OPTIONAL, default: "cucumber")
- **output_directory**: string - Directory for generated test scenarios and automation code (OPTIONAL, default: "functional-tests")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for functional testing execution due to systematic nature with built-in validation

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate expected outcomes from previous phases:
   - Test plan document exists: `TEST_PLAN_<PROJECT-ID>.md`
   - Implementation is complete with working codebase
   - Documentation is available describing user workflows and system behavior
   - All planning artifacts are complete and approved

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm test plan document exists and contains complete testing scenarios and coverage requirements
- Validate codebase path contains implemented functionality and business logic
- Check documentation path contains user workflows and expected system behaviors
- Verify access to all user-facing features, APIs, and integration points from actual implementation
- Confirm testing framework availability and configuration requirements

### 2. Execution Phase

<!-- <context_loading> -->
**Context Loading Operations:**
You WILL execute these operations systematically:
- Read and analyze: `TEST_PLAN.md` for planned testing scenarios and coverage requirements
- Scan codebase: `[codebase_path]` to understand actual functionality and business logic implementation
- Review documentation: `[documentation_path]` to understand user workflows and expected behaviors
- Identify all user-facing features, APIs, and integration points from actual implementation analysis
<!-- </context_loading> -->

<!-- <gherkin_test_design> -->
**Gherkin-Based Test Design Implementation:**
You WILL create functional tests as executable Gherkin scenarios:

**Business-Readable Test Creation:**
- You MUST write scenarios in Given-When-Then format using business language that stakeholders understand
- You WILL focus on user behaviors and expected outcomes from actual implemented functionality
- You MUST create scenarios that validate business requirements as implemented in the codebase
- You WILL ensure scenarios reflect actual system capabilities and constraints

**Executable Scenario Development:**
- You MUST design scenarios that can be automated with specified testing frameworks
- You WILL include specific test data and expected results based on actual system behavior
- You MUST create scenarios for both positive and negative test cases as supported by implementation
- You WILL ensure scenarios can be run independently and repeatedly with consistent results

**Comprehensive Coverage Implementation:**
- You MUST cover all major user workflows and business processes as implemented
- You WILL include edge cases and error conditions as actually handled in the codebase
- You MUST test integration points and external system interactions as implemented
- You WILL validate business rules and data validation logic as coded in the system
<!-- </gherkin_test_design> -->

<!-- <test_scenario_generation> -->
**Test Scenario Generation Operations:**
You WILL generate comprehensive test scenarios following template patterns:

**User Journey Testing Implementation:**
For each user workflow identified in documentation and implemented in codebase:
- You MUST create feature files with complete scenario structure
- You WILL implement Given-When-Then format examples with realistic test data
- You MUST create data-driven scenario outlines with comprehensive examples tables
- You WILL include error handling and edge case patterns as implemented in code

**API and Integration Testing Implementation:**
For each API endpoint and integration point discovered in codebase:
- You MUST create successful API call scenarios with actual request/response structures
- You WILL implement error handling scenarios for all error conditions coded in system
- You MUST include authentication and authorization testing as implemented
- You WILL create integration scenarios covering external system connectivity and data exchange
- You MUST test database operations and data consistency as implemented
- You WILL include file processing and data import/export scenarios if applicable
- You MUST test background job processing and scheduling if implemented

**Performance and Load Testing Implementation:**
For performance-critical components identified in codebase:
- You MUST create response time scenarios under normal load with specific acceptance criteria
- You WILL implement system behavior testing under concurrent load conditions
- You MUST define performance acceptance criteria based on actual system capabilities
<!-- </test_scenario_generation> -->

<!-- <test_automation_implementation> -->
**Test Automation Implementation Operations:**
You WILL generate complete automated test implementation:

**Test Framework Setup:**
- You MUST configure Cucumber, SpecFlow, or similar Gherkin runner for specified framework
- You WILL implement step definitions that interact with actual system endpoints and interfaces
- You MUST create test data management procedures with setup and cleanup automation
- You WILL configure test environments and system dependencies for automated execution

**Step Definition Implementation:**
- You MUST implement API testing steps for health checks, request execution, and response validation
- You WILL create UI testing steps for browser navigation, user interactions, and page verification
- You MUST implement test data management with automated setup and cleanup procedures
- You WILL configure test environment setup and system dependency management
- You MUST implement framework configuration for continuous integration and automated execution
<!-- </test_automation_implementation> -->

<!-- <data_environment_management> -->
**Test Data and Environment Management Operations:**
You WILL implement comprehensive data and environment strategies:

**Test Data Strategy Implementation:**
- You MUST create test data that supports all scenario variations with realistic business examples
- You WILL implement automated data cleanup procedures after test execution
- You MUST use database fixtures or API-based data setup procedures
- You WILL ensure test data isolation preventing interference between test executions

**Environment Configuration Implementation:**
- You MUST set up isolated test environments with proper system configuration
- You WILL configure external system mocks or test instances for integration testing
- You MUST manage test database state and migration procedures
- You WILL handle configuration differences between test, staging, and production environments

**Continuous Testing Integration:**
- You MUST integrate tests with CI/CD pipeline for automated execution
- You WILL configure test execution triggers on code changes and deployments
- You MUST implement test reporting and coverage metrics generation
- You WILL set up automated alerts and notifications for test failures
<!-- </data_environment_management> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for systematic functional testing execution
- Use imperative language throughout test scenario creation and automation
- Include comprehensive error handling for all testing scenarios
- Ensure all test scenarios reflect actual implemented functionality
- Validate all test automation works with real system components

### 3. Validation Phase
You WILL validate the functional testing implementation:
- Confirm all key user scenarios are covered by executable Gherkin tests
- Verify all test scenarios can be run automatically and consistently
- Validate business rules and validation logic are verified through test scenarios
- Ensure critical workflows are tested end-to-end with realistic data
- Confirm test results provide clear pass/fail feedback with useful error information
- Verify test suite integration with continuous integration systems
- Validate test coverage meets requirements specified in the test plan

## Output Format
You WILL generate outputs following this structure:
- **Primary deliverable**: Complete test automation suite with executable Gherkin scenarios
- **Gherkin Feature Files**: Business-readable test scenarios organized by feature area
- **Step Definition Code**: Automated test implementation with framework integration
- **Test Configuration**: Environment setup and test runner configuration files
- **Test Data**: Realistic test data sets and fixtures with management procedures
- **Test Reports**: Execution results templates and coverage metrics configuration
- **Maintenance Guide**: Instructions for updating and extending test scenarios

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when test plan and context loading is completed successfully
- Status updates during Gherkin scenario generation for each feature area
- Progress on test automation implementation and step definition creation
- Completion status for test data and environment management setup
- Validation results for test execution and coverage verification

### Completion Summary
- Summary of functional testing implementation with total scenarios created
- Test automation coverage results across all user workflows and system components
- Integration status with CI/CD pipeline and automated execution capabilities
- Quality validation results confirming comprehensive test coverage
- File locations for all generated test artifacts and documentation

### Next Steps
You WILL clearly define:
- Functional testing suite ready for continuous execution and monitoring
- Test scenarios available for regression testing during ongoing development
- Quality gates established for release validation and acceptance criteria
- Monitoring and maintenance procedures for test suite evolution

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ALL test scenarios MUST be based on actual implemented functionality, never theoretical features
- Rule 2: Gherkin scenarios MUST use business language understandable by stakeholders
- Rule 3: Test automation MUST work with real system endpoints and interfaces
- Rule 4: Test data MUST be realistic and support all scenario variations
- Rule 5: Test coverage MUST include all major user workflows and business processes
- Rule 6: Error handling scenarios MUST reflect actual system error conditions
- Rule 7: Integration tests MUST validate actual external system connections
- Rule 8: Performance tests MUST use realistic load patterns and acceptance criteria

## Success Criteria
You WILL consider the task complete when:
- [ ] All test plan requirements analyzed and converted to executable scenarios
- [ ] Key user scenarios covered by executable Gherkin tests with business language
- [ ] All test scenarios can be run automatically and consistently
- [ ] Business rules and validation logic verified through comprehensive test scenarios
- [ ] Critical workflows tested end-to-end with realistic data and expected outcomes
- [ ] Test results provide clear pass/fail feedback with useful error information
- [ ] Test suite integrated with continuous integration systems
- [ ] Test coverage meets all requirements specified in the test plan
- [ ] Test automation framework configured and operational
- [ ] Test data management and environment setup procedures implemented
- [ ] Documentation and maintenance guides created for ongoing test evolution

## Required Actions
1. Validate all required input parameters and test plan accessibility
2. Execute systematic functional testing implementation following Act protocol
3. Generate comprehensive test automation suite with executable scenarios
4. Implement test data management and environment configuration
5. Provide complete testing deliverables ready for continuous execution

## Error Handling
You WILL handle these scenarios:
- **Test Plan Access Failed**: Provide clear error message and request valid file path
- **Codebase Access Issues**: Request alternative access methods or provide manual analysis guidance
- **Documentation Access Failed**: Request alternative documentation sources or manual workflow specification
- **Testing Framework Configuration Issues**: Provide troubleshooting guidance and alternative framework options
- **Test Data Generation Failures**: Offer manual test data creation alternatives with clear templates
- **Environment Setup Issues**: Provide alternative environment configuration and troubleshooting steps
- **Test Automation Implementation Failures**: Debug automation issues and provide corrective implementations
- **Integration Testing Failures**: Identify integration issues and provide resolution strategies
- **Coverage Validation Failures**: Iterate test creation addressing specific coverage gaps

**Critical Requirements**
- MANDATORY: Follow Act protocol for systematic functional testing execution
- MANDATORY: All test scenarios MUST reflect actual implemented functionality
- NEVER create test scenarios for features not implemented in the codebase
- NEVER use placeholder or theoretical test data that doesn't work with actual system
- ALWAYS ensure test automation works with real system endpoints and interfaces
- ALWAYS validate that Gherkin scenarios use business language understandable by stakeholders
- ALWAYS implement comprehensive error handling for all testing scenarios
- ALWAYS provide realistic test data supporting all scenario variations
- ALWAYS ensure test coverage meets all requirements specified in test plan
- NEVER declare completion without full validation of automated test execution