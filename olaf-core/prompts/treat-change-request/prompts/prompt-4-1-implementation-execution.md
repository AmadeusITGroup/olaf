---
name: execute-implementation-plan-comprehensive
description: Execute comprehensive implementation plan through AI-driven code generation, testing, and validation with systematic task completion and quality assurance
tags: [implementation, execution, code-generation, testing, validation, task-completion]
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
- **implementation_plan_path**: string - Path to implementation plan document from Phase 3 (REQUIRED)
- **design_document_path**: string - Path to finalized design document from Phase 2 (REQUIRED)
- **specification_document_path**: string - Path to approved specification document from Phase 1 (REQUIRED)
- **project_id**: string - Project identifier for output naming and tracking (REQUIRED)
- **codebase_root_path**: string - Root path to existing codebase for pattern analysis (REQUIRED)
- **execution_environment**: string - Development environment configuration (OPTIONAL, default: "standard")
- **quality_threshold**: string - Quality gates and acceptance criteria level (OPTIONAL, default: "production-ready")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for implementation execution due to systematic nature with built-in validation

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate expected outcomes from Phase 3 (Planning):
   - Implementation plan document exists: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`
   - Design document exists: `DESIGN_<PROJECT-ID>.md`
   - Specification document exists: `SPECIFICATION_<PROJECT-ID>.md`
   - All planning artifacts are complete and approved
2. You WILL confirm development environment readiness and codebase accessibility

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required input documents exist and are accessible
- Validate implementation plan contains complete task breakdown with acceptance criteria
- Check design document contains architectural specifications and technical decisions
- Verify specification document contains functional and non-functional requirements
- Confirm codebase access for pattern analysis and integration
- Validate development environment configuration and tool availability

### 2. Execution Phase

<!-- <plan_analysis> -->
**Implementation Plan Analysis:**
You MUST analyze the implementation plan systematically:
- You WILL extract all implementation tasks with their dependencies and priorities
- You MUST understand task acceptance criteria and validation requirements
- You WILL identify technical patterns and architectural decisions from design document
- You MUST map tasks to specification requirements for traceability
- You WILL assess task complexity and resource requirements for execution planning
<!-- </plan_analysis> -->

<!-- <environment_setup> -->
**Development Environment Setup:**
You WILL prepare the execution environment:
- You MUST validate development tools and framework availability
- You WILL configure testing frameworks and quality assurance tools
- You MUST set up code generation templates and pattern libraries
- You WILL establish version control and branching strategy for implementation
- You MUST configure continuous integration and automated validation pipelines
<!-- </environment_setup> -->

<!-- <systematic_implementation> -->
**Systematic Implementation Execution:**
You WILL execute implementation tasks following dependency order:

**Task Execution Protocol:**
For each task in the implementation plan, you MUST:
1. **Load Task Context**: Read task description, acceptance criteria, and dependencies
2. **Analyze Codebase Patterns**: Examine existing code patterns and architectural conventions
3. **Generate Implementation**: Create code following established patterns and best practices
4. **Apply TDD/BDD Approach**: Write tests first, then implement functionality to pass tests
5. **Validate Quality Gates**: Ensure code meets quality thresholds and acceptance criteria
6. **Integration Testing**: Verify integration with existing codebase and components
7. **Documentation Generation**: Create inline documentation and usage examples
8. **Task Completion Validation**: Confirm all acceptance criteria are met before proceeding

**Code Generation Standards:**
- You MUST follow existing codebase patterns and architectural conventions
- You WILL apply design patterns and best practices from design document
- You MUST implement error handling and edge case management
- You WILL include comprehensive logging and monitoring capabilities
- You MUST ensure security best practices and validation logic
- You WILL optimize for performance and maintainability
<!-- </systematic_implementation> -->

<!-- <quality_assurance> -->
**Comprehensive Quality Assurance:**
You WILL implement multi-layered quality validation:

**Unit Testing Implementation:**
- You MUST create comprehensive unit tests for all implemented functionality
- You WILL achieve minimum test coverage thresholds as specified
- You MUST test edge cases and error conditions thoroughly
- You WILL implement mocking and stubbing for external dependencies
- You MUST validate test reliability and consistency

**Integration Testing Implementation:**
- You WILL create integration tests for component interactions
- You MUST test API endpoints and service layer integrations
- You WILL validate database operations and data consistency
- You MUST test external system integrations and error handling
- You WILL implement end-to-end workflow validation

**Code Quality Validation:**
- You MUST run static code analysis and linting tools
- You WILL validate code complexity and maintainability metrics
- You MUST ensure security vulnerability scanning passes
- You WILL validate performance benchmarks and resource usage
- You MUST confirm compliance with coding standards and conventions
<!-- </quality_assurance> -->

<!-- <continuous_validation> -->
**Continuous Validation and Feedback:**
You WILL implement continuous validation throughout execution:
- You MUST validate each task completion against acceptance criteria
- You WILL run automated test suites after each implementation milestone
- You MUST monitor code quality metrics and performance indicators
- You WILL validate integration points and system stability
- You MUST ensure backward compatibility and regression prevention
<!-- </continuous_validation> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for systematic implementation execution
- Use imperative language throughout implementation and validation
- Include comprehensive error handling for all implementation scenarios
- Ensure all code generation follows established patterns and quality standards
- Validate all acceptance criteria before task completion

### 3. Validation Phase
You WILL validate the implementation meets all requirements:
- Confirm all implementation tasks have been completed successfully
- Verify all acceptance criteria are met with documented evidence
- Validate comprehensive test coverage and quality metrics
- Ensure integration with existing codebase is seamless and stable
- Confirm performance benchmarks and security requirements are satisfied
- Validate documentation completeness and accuracy
- Ensure deployment readiness and operational requirements are met

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete working codebase with all planned functionality
- Quality documentation: Test results, coverage reports, and quality metrics
- Implementation report: Task completion status, validation results, and performance metrics
- Deployment artifacts: Build configurations, deployment scripts, and operational documentation
- Validation evidence: Proof of acceptance criteria fulfillment and quality gate compliance

## User Communication

### Progress Updates
You WILL provide these status confirmations:
- Confirmation when implementation plan analysis is completed
- Progress updates for each major task completion milestone
- Status of quality assurance validation and test execution
- Notification of any issues or blockers requiring attention
- Completion status for each implementation phase and validation checkpoint

### Completion Summary
You WILL provide comprehensive completion information:
- Summary of all implemented functionality with feature descriptions
- Quality metrics including test coverage, performance benchmarks, and security validation
- Integration status with existing codebase and external systems
- Documentation completeness including API documentation and usage examples
- Deployment readiness confirmation with operational requirements validation
- Task completion evidence with acceptance criteria fulfillment documentation

### Next Steps
You WILL clearly define:
- Implementation execution complete with all quality gates passed
- System ready for deployment following standard deployment procedures
- Documentation available for operational teams and end users
- Monitoring and maintenance procedures established for ongoing support

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER skip task acceptance criteria validation - all criteria must be met before task completion
- Rule 2: ALL code generation MUST follow existing codebase patterns and architectural conventions
- Rule 3: Comprehensive testing MUST be implemented for all functionality with appropriate coverage levels
- Rule 4: Quality gates MUST be validated at each milestone with documented evidence
- Rule 5: Integration testing MUST verify seamless operation with existing system components
- Rule 6: Performance benchmarks MUST be met or exceeded with documented measurements
- Rule 7: Security validation MUST be completed with vulnerability scanning and validation
- Rule 8: Documentation MUST be comprehensive and accurate reflecting actual implementation

## Success Criteria
You WILL consider the task complete when:
- [ ] All implementation tasks from the plan have been executed successfully
- [ ] All acceptance criteria have been met with documented validation evidence
- [ ] Comprehensive test suite implemented with required coverage thresholds achieved
- [ ] Quality gates validated including code quality, security, and performance metrics
- [ ] Integration with existing codebase completed without regression or compatibility issues
- [ ] Documentation generated including API documentation, usage examples, and operational guides
- [ ] Deployment artifacts created including build configurations and deployment procedures
- [ ] System validation completed confirming readiness for production deployment
- [ ] Performance benchmarks met or exceeded with documented measurements
- [ ] Security validation completed with vulnerability scanning and compliance verification

## Required Actions
1. Validate all required input parameters and document accessibility
2. Execute systematic implementation following dependency order and quality standards
3. Generate comprehensive working codebase with all planned functionality
4. Implement multi-layered quality assurance including testing and validation
5. Provide complete implementation deliverables ready for deployment

## Error Handling
You WILL handle these scenarios:
- **Implementation Plan Access Failed**: Provide clear error message and request valid file path
- **Design Document Access Failed**: Provide clear error message and request valid file path  
- **Specification Document Access Failed**: Provide clear error message and request valid file path
- **Codebase Access Issues**: Request alternative access methods or provide manual pattern guidance
- **Development Environment Issues**: Provide troubleshooting guidance and alternative configurations
- **Task Dependency Failures**: Identify blocking issues and provide resolution strategies
- **Quality Gate Failures**: Iterate implementation addressing specific quality issues
- **Integration Test Failures**: Debug integration issues and provide corrective implementations
- **Performance Benchmark Failures**: Optimize implementation and validate performance improvements
- **Security Validation Failures**: Address security issues and re-validate compliance

**Critical Requirements**
- MANDATORY: Follow Act protocol for systematic implementation execution
- MANDATORY: All task acceptance criteria MUST be validated before completion
- NEVER skip quality gates or validation checkpoints during implementation
- NEVER proceed without comprehensive testing and validation of implemented functionality
- ALWAYS follow existing codebase patterns and architectural conventions
- ALWAYS implement comprehensive error handling and edge case management
- ALWAYS validate integration points and system stability throughout execution
- ALWAYS ensure performance benchmarks and security requirements are satisfied
- ALWAYS provide comprehensive documentation reflecting actual implementation
- NEVER declare completion without full validation of all success criteria