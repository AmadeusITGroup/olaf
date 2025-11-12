# Deepen Tech Spec Developer

**Source**: olaf-core/competencies/developer/prompts/deepen-tech-spec-developer.md

## Overview

Deep-dive technical analysis focused on developer concerns including code quality, unit testing, architecture patterns, and design principles assessment with evidence-based evaluation. Creates comprehensive chapter-based documentation.

## Purpose

High-level technical specifications often lack the detailed developer-focused analysis needed for effective implementation and maintenance. This competency transforms existing tech specs into comprehensive, chapter-based deep-dive documentation covering architecture patterns, code quality, testing strategies, and implementation details that developers need.

## Usage

**Command**: `deepen tech spec`

**Protocol**: Propose-Confirm-Act

**When to Use**:
- After initial tech spec creation to add developer-focused details
- When onboarding developers to complex codebases
- For architecture review and assessment
- To document existing systems comprehensively
- When planning major refactoring initiatives

## Parameters

### Required Inputs
- **tech_spec_path**: Path to the existing technical specification file
- **application_name**: Name of the application for file naming (kebab-case)

### Optional Inputs
- **chapter_focus**: Specific chapter to start with (defaults to first chapter)

### Context Requirements
- Existing technical specification document
- Access to complete codebase for analysis
- Ability to create chapter files in findings directory

## Output

Comprehensive chapter-based documentation covering developer-focused technical analysis.

**Deliverables**:
- 6 detailed chapters covering:
  1. Architecture & Design Patterns Assessment
  2. API Implementation Quality Analysis
  3. Data Access & Transaction Management
  4. Error Handling & Exception Strategy
  5. Unit Testing & Code Quality Evaluation
  6. Module Dependencies & Structure Assessment
- Evidence-based assessments with code examples
- Best practices and recommendations for each area
- Session management for long-running analysis

**Format**: Individual markdown chapter files saved to findings directory

## Examples

### Example 1: Complete Deep-Dive Analysis

**Scenario**: Creating comprehensive developer documentation for existing system

**Command**:
```
deepen tech spec
```

**Input**:
- tech_spec_path: "./docs/tech-spec.md"
- application_name: "order-management"

**Result**: Generated 6 comprehensive chapters with detailed analysis of architecture patterns, API quality, data access, error handling, testing, and dependencies

### Example 2: Focused Chapter Analysis

**Scenario**: Need detailed testing strategy documentation

**Command**:
```
deepen tech spec
```

**Input**:
- tech_spec_path: "./docs/tech-spec.md"
- application_name: "inventory-service"
- chapter_focus: "Unit Testing & Code Quality Evaluation"

**Result**: Created detailed chapter on testing strategy with coverage analysis, test quality assessment, and recommendations

## Related Competencies

- **generate-tech-spec-from-code**: Use first to create initial tech spec
- **assess-code-quality-principles**: Complements with quality assessment
- **review-code**: Use for detailed code review of identified issues
- **augment-code-unit-test**: Apply to improve testing based on findings

## Tips & Best Practices

- Start with existing tech spec for context
- Process chapters sequentially for comprehensive coverage
- Use session management for large codebases
- Review each chapter before proceeding to next
- Combine with code quality assessment for complete picture
- Update chapters as codebase evolves

## Limitations

- Requires existing technical specification as starting point
- Analysis depth depends on codebase accessibility
- May require multiple sessions for large systems
- Chapter generation is sequential, not parallel
- Requires developer expertise to interpret findings
