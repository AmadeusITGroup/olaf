---
name: execute-documentation-generation
description: Generate comprehensive documentation based on implemented code and features following code-first approach
tags: [documentation, code-analysis, user-guides, api-docs]
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

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **documentation_plan_path**: string - Path to DOCUMENTATION_PLAN.md file (REQUIRED)
- **codebase_path**: string - Root path to implemented codebase for analysis (REQUIRED)
- **specification_path**: string - Path to specification and design documents (REQUIRED)
- **output_directory**: string - Directory where documentation files will be generated (REQUIRED)
- **documentation_types**: array - Types of documentation to generate [user_guides, api_docs, technical_docs, operations_docs] (OPTIONAL, default: all types)
- **include_screenshots**: boolean - Whether to include screenshot placeholders in user documentation (OPTIONAL, default: true)
- **api_format**: string - Format for API documentation [swagger, openapi, markdown] (OPTIONAL, default: swagger)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act for documentation generation due to moderate impact

## Prerequisites
You MUST verify the preceding planning phase was completed:
1. You MUST verify DOCUMENTATION_PLAN.md exists and contains stakeholder requirements
2. You WILL validate expected outcomes from previous step:
   - Documentation plan with defined stakeholder types and requirements
   - Identified documentation formats and delivery methods
   - Planned documentation structure and organization
   - Specific deliverables that must be generated

## Process

### 1. Validation Phase
You WILL verify all requirements:
<!-- <validation_phase> -->
- Confirm all required parameters are provided
- Validate documentation plan file exists and is accessible
- Check codebase path contains implemented functionality
- Verify specification documents are available for business context
- Confirm output directory is writable and accessible
- Validate prerequisites from planning phase are met
<!-- </validation_phase> -->

### 2. Execution Phase

**Context Loading Operations**:
<!-- <context_loading> -->
You WILL execute these operations in sequence:
- Read and analyze: `[documentation_plan_path]` for planned documentation types and stakeholders
- Scan codebase: `[codebase_path]` to understand actual functionality and features
- Review specification files: `[specification_path]` for business context and requirements
- Identify public APIs, user interfaces, and configuration options from actual code implementation
<!-- </context_loading> -->

**Code Analysis Operations**:
<!-- <code_analysis> -->
You WILL perform comprehensive code analysis:
- Scan implemented classes, methods, and APIs for actual functionality
- Extract business logic and workflow implementations from source code
- Identify configuration options and deployment requirements from actual setup
- Document actual error handling and edge cases as implemented in code
- Map implemented features to original requirements from specifications
- Identify any deviations or additional functionality beyond original scope
- Create feature inventory with actual capabilities and limitations
- Document integration points and dependencies as implemented
<!-- </code_analysis> -->

**Documentation Generation Operations**:
<!-- <documentation_generation> -->
You WILL generate documentation following code-first approach:

**User Documentation Generation**:
- Generate step-by-step guides for actual implemented features only
- Create screenshot placeholders and examples from working system capabilities
- Document actual user workflows and business processes as supported by implementation
- Include troubleshooting for real error conditions and edge cases found in code

**API Documentation Generation**:
- Auto-generate API documentation from actual endpoints discovered in codebase
- Include real request/response examples from implemented code structure
- Document authentication, rate limiting, and error responses as actually implemented
- Create SDK examples or client library documentation if applicable

**Technical Documentation Generation**:
- Generate architecture diagrams based on actual implemented structure
- Document design patterns and code organization as built in the codebase
- Create contributing guidelines based on actual codebase structure and conventions
- Include testing and development setup procedures from actual project structure

**Operations Documentation Generation**:
- Document actual monitoring, logging, and alerting capabilities found in code
- Create runbooks for deployed system operations based on implemented features
- Document backup, recovery, and maintenance procedures as supported
- Include performance tuning and scaling guidance based on actual architecture
<!-- </documentation_generation> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for user approval of documentation generation approach
- Complete all documentation generation steps following code-first methodology
- Provide required user confirmations for each documentation type generated
- Ensure all examples work with actual implemented code functionality

### 3. Validation Phase
You WILL validate documentation results:
<!-- <validation_phase> -->
- Confirm all outputs accurately reflect implemented functionality
- Verify all code examples compile and execute correctly against actual codebase
- Test all documented procedures and workflows for accuracy
- Validate API examples against actual endpoints discovered in code
- Confirm configuration examples work with actual deployed system requirements
- Ensure documentation completeness for each identified stakeholder type
- Verify technical accuracy of all generated content
<!-- </validation_phase> -->

## Output Format
You WILL generate outputs following this structure:
- **Primary deliverable**: Complete documentation suite in `[output_directory]`
- **User Guides**: Step-by-step instructions for end users (`user-guides/`)
- **API Reference**: Complete API documentation with examples (`api-reference/`)
- **Installation Guide**: Setup and deployment instructions (`installation/`)
- **Developer Guide**: Technical implementation and contribution documentation (`developer/`)
- **Operations Manual**: System administration and maintenance procedures (`operations/`)
- **Interactive Documentation**: Swagger/OpenAPI specifications with live examples (if applicable)
- **Code Examples**: Working sample code and integration examples (`examples/`)

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when documentation plan is successfully loaded and analyzed
- Confirmation when codebase analysis is complete with feature inventory
- Confirmation when each documentation type generation is complete
- Status of validation results for generated documentation accuracy
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- Summary of documentation types generated with file locations
- Code analysis results showing implemented vs planned features
- Validation results confirming technical accuracy and completeness
- Any deviations from original plan due to implementation differences

### Next Steps
You WILL clearly define:
- Documentation suite ready for functional testing phase
- All user scenarios and workflows documented for test scenario creation
- Clear acceptance criteria provided based on implemented functionality
- Business rules and validation logic identified for Gherkin scenarios
- Test data examples and expected outcomes documented
- Error conditions and edge cases documented for negative testing

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: All documentation MUST accurately reflect actual implemented functionality, never planned features
- Rule 2: All code examples MUST work with the actual codebase and compile successfully
- Rule 3: API documentation MUST match actual endpoints and responses, not theoretical specifications
- Rule 4: User workflows MUST be based on actual UI implementations and capabilities
- Rule 5: Configuration examples MUST use real settings and parameters from actual deployment
- Rule 6: Documentation MUST be generated for all stakeholder types identified in the planning phase
- Rule 7: All technical documentation MUST reflect actual architecture and design patterns used
- Rule 8: Operations documentation MUST be based on actual monitoring and deployment capabilities

## Success Criteria
You WILL consider the task complete when:
- [ ] All required parameters validated and prerequisites confirmed
- [ ] Documentation plan successfully loaded and analyzed
- [ ] Codebase analysis completed with comprehensive feature inventory
- [ ] All stakeholder documentation types generated and complete
- [ ] Documentation accurately reflects implemented functionality with no theoretical content
- [ ] All code examples work with actual implementation and have been validated
- [ ] API documentation matches actual endpoints and responses
- [ ] User workflows documented with realistic examples from actual implementation
- [ ] Installation and setup procedures tested and confirmed accurate
- [ ] Technical documentation reflects actual architecture and patterns
- [ ] All generated files saved in specified output directory structure
- [ ] Validation completed confirming 100% technical accuracy
- [ ] User approval obtained via Propose-Act protocol
- [ ] Handoff materials prepared for functional testing phase

## Required Actions
1. Validate all required input parameters and prerequisites from planning phase
2. Execute documentation generation following appropriate interaction protocol
3. Generate outputs in specified format with accurate technical content
4. Provide user communication and confirmations throughout process
5. Define next steps for functional testing phase transition

## Error Handling
You WILL handle these scenarios:
- **Missing Documentation Plan**: Request specific path to DOCUMENTATION_PLAN.md file
- **Codebase Access Issues**: Provide clear error message and request valid codebase path
- **Specification File Access Failed**: Request alternative specification sources or manual input
- **Code Analysis Failures**: Provide detailed error information and request guidance on proceeding
- **API Discovery Issues**: Document manual API endpoint identification process
- **Output Directory Write Failures**: Provide alternative save locations and troubleshooting steps
- **Documentation Validation Failures**: Stop process and request user guidance on accuracy issues
- **Template or Example Generation Failures**: Offer manual creation alternatives with clear instructions

## Critical Requirements
- MANDATORY: Follow Propose-Act protocol for all documentation generation activities
- MANDATORY: All generated documentation MUST reflect actual implemented code, never theoretical features
- NEVER generate documentation for features not actually implemented in the codebase
- NEVER use placeholder or example content that doesn't work with actual implementation
- ALWAYS validate that all code examples compile and execute successfully
- ALWAYS ensure API documentation matches actual endpoints and responses
- ALWAYS base user workflows on actual UI implementations and capabilities
- ALWAYS confirm technical accuracy before considering documentation complete
- ALWAYS provide comprehensive handoff materials for functional testing phase
