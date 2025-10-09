---
name: create-comprehensive-test-plan
description: Transform approved technical design into comprehensive testing strategy covering all aspects of system validation and quality assurance
tags: [test-plan, qa-strategy, integration-testing, system-testing, test-automation]
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
- **design_document_path**: string - Path to finalized design document from Phase 2 (REQUIRED)
- **specification_document_path**: string - Path to approved specification document from Phase 1 (REQUIRED)
- **project_id**: string - Project identifier for file naming (REQUIRED)
- **testing_environment_info**: string - Information about available testing environments (OPTIONAL)
- **qa_team_capabilities**: string - Information about QA team tools and expertise (OPTIONAL)
- **test_plan_template_path**: string - Path to test plan template (OPTIONAL, default: "../templates/template-test-plan.md")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for test plan creation due to moderate impact on project timeline

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate expected outcomes from previous phases:
   - Design document: `DESIGN_<PROJECT-ID>.md` exists and is finalized
   - Specification document: `SPECIFICATION_<PROJECT-ID>.md` exists and is approved
   - Both documents contain complete requirements and technical specifications

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm design document exists and contains complete technical specifications
- Validate specification document exists and contains all functional/non-functional requirements
- Check access to test plan template
- Verify project ID format for output naming

### 2. Execution Phase

<!-- <document_analysis> -->
**Comprehensive Document Analysis:**
You MUST analyze both specification and design documents systematically:

**Specification Document Analysis:**
- You WILL extract all functional requirements (FR-xxx) to ensure test coverage
- You MUST extract all non-functional requirements (NFR-xxx) for performance/security testing
- You WILL identify user stories and acceptance criteria for E2E testing
- You MUST determine business rules and validation requirements
- You WILL note critical user workflows and business processes

**Design Document Analysis:**
- You WILL review architectural components and their interactions for integration testing
- You MUST identify testable interfaces and API contracts
- You WILL understand data flows and technical implementation details
- You MUST note security mechanisms and performance considerations
- You WILL map design components to specification requirements

**Cross-Reference Analysis:**
- You MUST ensure every functional requirement has corresponding design components to test
- You WILL validate that design components support all specification requirements
- You MUST identify gaps where requirements lack implementation details
- You WILL determine test priorities based on business criticality and technical risk
<!-- </document_analysis> -->

<!-- <test_strategy_development> -->
**Test Strategy Development:**
You WILL create comprehensive testing approach:

**Overall Testing Strategy:**
- You MUST define overall testing approach (shift-left, risk-based, etc.)
- You WILL specify testing phases and entry/exit criteria
- You MUST identify testing tools and automation strategy
- You WILL define test data management approach

**QA Strategy Section:**
You MUST define the overall QA approach focusing on integration, system, and acceptance testing:

- **Task: Define QA testing strategy**
  - Subtask: Establish testing phases and entry/exit criteria
  - Subtask: Define test data management and environment requirements
  - Subtask: Set up test automation framework for integration/E2E tests
  - Subtask: Define defect management and reporting processes
  - Subtask: Establish quality gates and acceptance criteria

**Note**: Unit testing is handled as part of the Implementation Plan (Prompt 3.3) where developers create unit tests during development using TDD/BDD practices.
<!-- </test_strategy_development> -->

<!-- <integration_test_planning> -->
**Integration Test Plan Development:**
You WILL analyze both specification and design documents for integration requirements and implementation:

**For each integration point identified in the design document, you MUST create:**
- **Task: Test integration between [System A] and [System B from Design]**
  - Subtask: Test data exchange requirements (from specification) via design implementation
  - Subtask: Test business workflows (from specification) that span multiple systems
  - Subtask: Test error scenarios and business rule violations (from specification + design)
  - Subtask: Validate data transformation meets business requirements (specification requirements)
  - Subtask: Test non-functional requirements (performance, security from specification)

**Adaptation Guidelines:**
- **External API integrations**: Include timeout, rate limiting, and error response testing
- **Database integrations**: Focus on transaction integrity and connection handling
- **Internal service integrations**: Emphasize contract testing and service discovery
- **Simple integrations**: May need only 2-3 subtasks focusing on main scenarios
<!-- </integration_test_planning> -->

<!-- <system_test_planning> -->
**System Test Plan Development:**
You WILL analyze the specification for user stories and create E2E workflow tasks:

**For each user story/workflow identified in the specification, you MUST create:**
- **Task: Test [User Story Name from Specification] end-to-end workflow**
  - Subtask: Set up test data (adapt based on workflow data requirements)
  - Subtask: Execute main user journey (based on specification acceptance criteria)
  - Subtask: Test alternative paths (based on specification alternate flows)
  - Subtask: Verify business rules (based on specification business logic)
  - Subtask: Test UI/UX requirements (if applicable to this workflow)

**Adaptation Guidelines:**
- **Critical user workflows** (registration, payment, core business): Extensive testing with multiple paths
- **Standard workflows** (CRUD operations, reports): Focus on main path and error handling
- **Admin workflows** (configuration, maintenance): Basic functionality and permissions testing
- **Complex workflows**: Break into multiple tasks if workflow spans multiple sessions
<!-- </system_test_planning> -->

<!-- <performance_test_planning> -->
**Performance Test Plan Development:**
You WILL create specific, actionable performance tasks:

- **Task: Execute load testing for [Feature/API]**
  - Subtask: Define performance benchmarks (response time, throughput)
  - Subtask: Create load testing scripts and scenarios
  - Subtask: Execute baseline performance tests
  - Subtask: Execute peak load tests (2x normal load)
  - Subtask: Analyze results and identify bottlenecks
<!-- </performance_test_planning> -->

<!-- <security_test_planning> -->
**Security Test Plan Development:**
You WILL create specific, actionable security tasks:

- **Task: Security testing for [Component/API]**
  - Subtask: Test authentication mechanisms
  - Subtask: Test authorization and access controls
  - Subtask: Test input validation (SQL injection, XSS)
  - Subtask: Test data encryption in transit and at rest
  - Subtask: Run vulnerability scanning tools
<!-- </security_test_planning> -->

<!-- <environment_setup_planning> -->
**Test Environment Setup Planning:**
You WILL create specific, actionable environment tasks:

- **Task: Set up test environment infrastructure**
  - Subtask: Provision test databases with sample data
  - Subtask: Configure test application servers
  - Subtask: Set up monitoring and logging
  - Subtask: Create test data refresh procedures
  - Subtask: Document environment access and credentials
<!-- </environment_setup_planning> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for user approval of test plan
- Complete comprehensive analysis of both specification and design documents
- Create actionable test tasks with clear subtasks
- Ensure all requirements have corresponding test coverage
- Include comprehensive quality validation

### 3. Validation Phase
You WILL validate the test plan meets all requirements:
- Confirm all functional requirements have corresponding integration/system test cases
- Verify non-functional requirements are adequately covered by performance/security tests
- Validate integration test scenarios cover all system boundaries
- Ensure E2E test workflows cover all major user journeys
- Confirm test data requirements are realistic and achievable
- Verify environment requirements are clearly defined
- Validate acceptance criteria are measurable and objective

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Comprehensive test plan document `TEST_PLAN_<PROJECT-ID>.md` following template structure
- Test coverage matrix: Mapping requirements to test scenarios
- Test strategy summary: High-level approach and methodology
- Quality validation checklist: Confirmation of coverage completeness

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when specification and design documents are successfully analyzed
- Status updates during test strategy development
- Progress on integration, system, performance, and security test planning
- Completion status for environment setup planning
- Validation results for test coverage completeness

### Completion Summary
- Test plan document presented for review via Propose-Act protocol
- Summary of testing approach and coverage strategy
- Total test scenarios created across all testing categories
- Quality validation results confirming comprehensive coverage
- Save location confirmation: `TEST_PLAN_<PROJECT-ID>.md`

### Next Steps
You WILL clearly define:
- Test plan ready for QA team execution (pending user approval)
- Integration with development process for test-driven development
- Handoff to development team for implementation planning
- Quality gates established for testing phases

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ALL functional requirements MUST have corresponding test cases in integration or system testing
- Rule 2: Non-functional requirements MUST be covered by performance, security, or operational testing
- Rule 3: Test tasks MUST be specific and actionable with clear subtasks
- Rule 4: Integration tests MUST cover all system boundaries identified in design
- Rule 5: System tests MUST cover all major user journeys from specification
- Rule 6: Performance tests MUST include measurable benchmarks and acceptance criteria
- Rule 7: Security tests MUST address all security mechanisms from design
- Rule 8: Test environment requirements MUST be realistic and achievable

## Success Criteria
You WILL consider the task complete when:
- [ ] Both specification and design documents successfully analyzed
- [ ] All functional requirements mapped to test scenarios
- [ ] All non-functional requirements covered by appropriate test types
- [ ] Integration test plan covers all system boundaries
- [ ] System test plan covers all major user workflows
- [ ] Performance test plan includes measurable benchmarks
- [ ] Security test plan addresses all security requirements
- [ ] Test environment setup plan is comprehensive and realistic
- [ ] Quality validation confirms complete coverage
- [ ] Test plan document follows template structure exactly
- [ ] User approval obtained via Propose-Act protocol

## Required Actions
1. Validate all required input parameters and document accessibility
2. Execute comprehensive document analysis following systematic approach
3. Generate complete test plan document in specified template format
4. Provide user communication and obtain approval via Propose-Act
5. Define next steps for QA team execution and development integration

## Error Handling
You WILL handle these scenarios:
- **Design Document Access Failed**: Provide clear error message and request valid file path
- **Specification Document Access Failed**: Provide clear error message and request valid file path
- **Incomplete Requirements Analysis**: Stop process and request complete document analysis
- **Test Coverage Gaps Identified**: Iterate test planning to address all missing coverage areas
- **Template Access Failed**: Use standard markdown structure and continue with test plan creation
- **User Rejection During Propose-Act**: Request specific feedback and iterate test plan accordingly
- **Environment Requirements Unrealistic**: Adjust requirements and provide alternative approaches
- **Performance Benchmarks Unclear**: Request specific metrics and acceptance criteria

**Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for test plan approval
- MANDATORY: Analyze BOTH specification and design documents completely before creating test plan
- NEVER create test plan without comprehensive requirements analysis
- NEVER omit test coverage for any functional or non-functional requirement
- ALWAYS ensure test tasks are specific and actionable with clear subtasks
- ALWAYS validate that integration tests cover all system boundaries
- ALWAYS confirm that system tests cover all major user workflows
- ALWAYS include measurable acceptance criteria for all test categories
- ALWAYS preserve traceability from requirements to test scenarios
- NEVER proceed without user approval of comprehensive test plan