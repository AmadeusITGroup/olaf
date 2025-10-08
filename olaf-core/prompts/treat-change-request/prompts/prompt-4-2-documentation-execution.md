# Prompt 4-2: Documentation Execution

## Context Loading

Load planning documents and implemented code:

- Review `DOCUMENTATION_PLAN.md` for planned documentation types and stakeholders
- Analyze implemented codebase to understand actual functionality and features
- Review specification and design documents for business context and requirements
- Identify public APIs, user interfaces, and configuration options from actual code

## Documentation Generation Approach

### Code-First Documentation

Generate documentation based on actual implemented features:

1. **Code Analysis**
   - Scan implemented classes, methods, and APIs for functionality
   - Extract business logic and workflow implementations
   - Identify configuration options and deployment requirements
   - Document actual error handling and edge cases

2. **Feature Mapping**
   - Map implemented features to original requirements
   - Identify any deviations or additional functionality
   - Create feature inventory with actual capabilities
   - Document integration points and dependencies

3. **User Journey Documentation**
   - Based on actual UI implementations and API endpoints
   - Create realistic workflows using implemented functionality
   - Generate examples with actual code and responses
   - Document configuration and setup based on real requirements

## Documentation Types and Generation

### User Documentation

**End User Guides**:

- Generate step-by-step guides for actual implemented features
- Create screenshots and examples from working system
- Document actual user workflows and business processes
- Include troubleshooting for real error conditions and edge cases

**API Documentation**:

- Auto-generate API documentation from actual endpoints
- Include real request/response examples from implemented code
- Document authentication, rate limiting, and error responses as implemented
- Create SDKs or client libraries if applicable

**Configuration and Setup**:

- Document actual deployment and configuration procedures
- Include real environment variables and configuration files
- Create installation guides based on actual system requirements
- Document integration with external systems as implemented

### Technical Documentation

**Developer Documentation**:

- Generate architecture diagrams based on implemented structure
- Document design patterns and code organization as built
- Create contributing guidelines based on actual codebase structure
- Include testing and development setup procedures

**Operations Documentation**:

- Document actual monitoring, logging, and alerting capabilities
- Create runbooks for deployed system operations
- Document backup, recovery, and maintenance procedures
- Include performance tuning and scaling guidance

**Integration Documentation**:

- Document actual integration points and protocols
- Create integration guides for external systems
- Document data formats, schemas, and protocols as implemented
- Include security and compliance considerations

## Quality Standards

### Accuracy and Relevance

**Code Alignment**:

- All examples work with actual implemented code
- Screenshots and UI documentation match actual interfaces
- API documentation reflects actual endpoints and responses
- Configuration examples use real settings and parameters

**Completeness**:

- Cover all implemented features and capabilities
- Include edge cases and error conditions as handled in code
- Document all public APIs and user-facing functionality
- Provide examples for all major use cases and workflows

**Usability**:

- Write for identified stakeholder knowledge levels
- Use clear, concise language appropriate for each audience
- Include visual aids, diagrams, and examples where helpful
- Organize content logically for different user types and scenarios

## Output Generation

### Documentation Files

Generate actual documentation files:

- **User Guides**: Step-by-step instructions for end users
- **API Reference**: Complete API documentation with examples
- **Installation Guide**: Setup and deployment instructions
- **Developer Guide**: Technical implementation and contribution documentation
- **Operations Manual**: System administration and maintenance procedures

### Interactive Documentation

Where applicable, create:

- **Interactive API Documentation**: Swagger/OpenAPI specifications with live examples
- **Code Examples**: Working sample code and integration examples
- **Video Tutorials**: Screen recordings for complex workflows (describe, don't create)
- **FAQ and Troubleshooting**: Based on anticipated user questions and implemented error handling

## Validation and Testing

### Content Validation

**Technical Accuracy**:

- Verify all code examples compile and execute correctly
- Test all documented procedures and workflows
- Validate API examples against actual endpoints
- Confirm configuration examples work with deployed system

**User Experience**:

- Review documentation flow and organization
- Test instructions with representative users if possible
- Ensure examples are realistic and useful
- Verify completeness for each identified stakeholder type

### Documentation Maintenance

**Living Documentation**:

- Structure documentation for easy updates as code changes
- Use automated documentation generation where possible
- Create templates for consistent formatting and structure
- Establish procedures for keeping documentation current

## Validation Criteria

Documentation execution is complete when:

- [ ] All stakeholder documentation types are generated and complete
- [ ] Documentation accurately reflects implemented functionality
- [ ] All code examples work with actual implementation
- [ ] API documentation matches actual endpoints and responses
- [ ] User workflows are documented with realistic examples
- [ ] Installation and setup procedures are tested and accurate
- [ ] Technical documentation reflects actual architecture and patterns

## Handoff to Functional Testing Phase

Prepare for functional testing by:

- Documenting all user scenarios and workflows for test scenario creation
- Providing clear acceptance criteria based on implemented functionality
- Identifying business rules and validation logic for Gherkin scenarios
- Creating test data examples and expected outcomes
- Documenting error conditions and edge cases for negative testing

This prompt ensures AI generates comprehensive, accurate documentation that reflects the actual implemented system while serving the needs of all identified stakeholders.