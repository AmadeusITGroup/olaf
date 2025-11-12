# Bootstrap Functional Spec from Code

## Overview

This competency analyzes existing source code to extract and document its functionalities from a business and user perspective, creating a draft functional specification. It reverse-engineers the implementation to produce business-focused documentation that explains what the system does and why, without requiring deep technical knowledge.

## Purpose

Many software projects lack up-to-date functional specifications, especially legacy systems or rapidly developed applications. When documentation is missing or outdated, this competency solves the problem by analyzing the actual implementation to generate a business-readable specification. This is invaluable for modernization projects, knowledge transfer, or creating documentation for undocumented systems.

## Usage

**Command**: `bootstrap functional spec from code`

**Protocol**: Act

**When to Use**: Use this competency when you have working code but missing or outdated functional specifications, when preparing for application modernization or migration, when onboarding new team members to legacy systems, or when stakeholders need business-level documentation of technical implementations.

## Parameters

### Required Inputs
- **source_path**: Path to the application's source code or codebase directory to analyze

### Optional Inputs
- **output_format**: Output format for the specification (markdown, html, or pdf; default: markdown)
- **detail_level**: Level of detail to include (overview, standard, or detailed; default: standard)

### Context Requirements
- Source code must be accessible in the workspace or specified directory
- Functional specification template is automatically loaded from competency templates
- Code should be reasonably structured for effective analysis

## Output

This competency produces a business-focused functional specification document extracted from code analysis.

**Deliverables**:
- Functional specification document saved to `olaf-data/specs/FunctionalSpec-YYYYMMDD-NNN.md`
- Executive summary of identified components and business processes
- User stories derived from code functionality
- Data models and integration points documentation

**Format**: Structured markdown document following the functional-specification-template, written in business-focused language with technical details relegated to appendices. Includes visual diagrams where helpful.

## Examples

### Example 1: Legacy System Documentation

**Scenario**: A 5-year-old customer management system lacks documentation, and the team needs a functional spec before planning a modernization effort.

**Command**:
```
olaf bootstrap functional spec from code
```

**Input**:
```
source_path: ./legacy-crm/src
detail_level: detailed
```

**Result**: Generated comprehensive functional specification documenting customer lifecycle management, reporting capabilities, integration with payment systems, and data models. Identified 12 core business processes and 8 external integrations.

### Example 2: Quick System Overview

**Scenario**: New product manager needs to understand what an existing microservice does from a business perspective.

**Command**:
```
olaf bootstrap functional spec from code
```

**Input**:
```
source_path: ./services/notification-service
detail_level: overview
```

**Result**: High-level functional specification describing notification delivery capabilities, supported channels (email, SMS, push), and business rules for notification routing.

## Related Competencies

- **extend-specification**: Use after bootstrapping to add missing UI/UX details and frontend requirements
- **improve-spec**: Enhance the bootstrapped specification with visual diagrams and detailed data definitions
- **analyze-business-requirements**: Validate the extracted requirements against business needs
- **generate-technical-specification** (architect): Create technical architecture documentation to complement the functional spec

## Tips & Best Practices

- Start with overview detail level for initial assessment, then run detailed analysis for specific components
- Review the generated specification with original developers if available to validate accuracy
- Use this as a starting point—expect to refine and enhance the specification with stakeholder input
- Combine with code comments and commit history analysis for better context
- Focus on well-structured code first; refactor unclear code before bootstrapping if possible
- Maintain traceability between specification sections and source code locations

## Limitations

- Cannot infer business intent or rationale—only documents what the code does, not why
- Quality depends on code structure and clarity—poorly organized code yields less useful specifications
- May miss implicit business rules or undocumented assumptions in the implementation
- Cannot validate if the implementation matches original business requirements
- Does not modify or analyze code quality—purely extracts functional behavior
- Requires human review to ensure business accuracy and completeness

---

**Source**: `olaf-core/competencies/business-analyst/prompts/bootstrap-functional-spec-from-code.md`
