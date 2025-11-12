# Generate Code from Spec

## Overview

This competency transforms technical specifications into working code implementations, following best practices and design patterns while ensuring the generated code meets specified requirements and quality standards.

## Purpose

Converting specifications into code is time-consuming and error-prone. This competency accelerates development by generating initial implementations from technical specifications, ensuring consistency with documented requirements, and applying appropriate design patterns and coding standards from the start.

## Usage

**Command**: `generate code from spec` (or aliases: `implement spec`, `code from specification`, `build from spec`)

**Protocol**: Propose-Act

**When to Use**: Use when you have detailed technical specifications and need to generate initial implementations, bootstrap new features, create proof-of-concepts, or ensure code matches documented requirements.

## Parameters

### Required Inputs
- **specification**: Technical specification document or detailed requirements
- **target_language**: Programming language for implementation
- **framework**: Framework or technology stack to use

### Optional Inputs
- **coding_standards**: Specific coding standards or style guides to follow
- **design_patterns**: Preferred design patterns to apply
- **test_requirements**: Testing approach and coverage expectations
- **output_structure**: Desired file and directory organization

### Context Requirements
- Clear, detailed technical specification
- Understanding of target technology stack
- Access to relevant coding standards and patterns
- Knowledge of project structure and conventions

## Output

Generates working code implementation based on specifications.

**Deliverables**:
- Source code files implementing specified functionality
- Supporting classes, interfaces, and utilities
- Configuration files if needed
- Basic unit tests (if specified)
- Implementation notes documenting design decisions
- README or documentation for generated code

**Format**: Source code files in specified language and framework

## Examples

### Example 1: API Endpoint Implementation

**Scenario**: Technical spec defines REST API endpoints, need implementation

**Command**:
```
generate code from spec
```

**Input**:
```
specification: API spec for user management endpoints
target_language: TypeScript
framework: Express.js
coding_standards: Airbnb style guide
```

**Result**: Generated Express routes, controller classes, service layer, data models, input validation, error handling, and basic unit tests following specified patterns.

### Example 2: Data Processing Module

**Scenario**: Specification describes data transformation pipeline

**Command**:
```
implement spec
```

**Input**:
```
specification: Data processing pipeline spec
target_language: Python
framework: pandas
design_patterns: Strategy pattern for transformations
```

**Result**: Created pipeline classes, transformation strategies, error handling, logging, configuration management, and sample usage examples.

## Related Competencies

- **generate-technical-specification**: Architect competency that creates the specs this competency implements
- **review-code**: Should be used to review generated code before integration
- **create-unit-tests**: Can enhance generated code with comprehensive tests
- **fix-code-smells**: Can improve generated code quality after initial implementation

## Tips & Best Practices

- Ensure specifications are detailed and unambiguous before generating code
- Review and test generated code thoroughly before integration
- Specify coding standards and patterns upfront for consistency
- Use generated code as starting point, expect to refine and enhance
- Include test requirements in specification for better test coverage
- Provide examples in specification for more accurate implementation
- Iterate on generated code with feedback and refinements
- Document any deviations from specification in implementation notes

## Limitations

- Quality depends heavily on specification clarity and completeness
- Cannot make design decisions not specified in requirements
- May not capture all edge cases or error scenarios
- Generated code requires review and testing before production use
- Cannot infer business logic not explicitly documented
- May need adjustment for project-specific conventions
- Does not replace developer judgment and domain expertise
- Cannot optimize for performance without specific requirements
