# Fix Code Smells

**Source**: olaf-core/competencies/developer/prompts/fix-code-smells.md

## Overview

Transform code smells into clean, elegant solutions using SOLID principles and clean code practices. Provides incremental refactoring with clear explanations and before/after comparisons.

## Purpose

Code smells indicate deeper design problems that reduce maintainability and increase technical debt. This competency systematically identifies and refactors code smells using established clean code principles, helping teams improve code quality while preserving functionality. It balances theoretical best practices with practical constraints.

## Usage

**Command**: `fix code smells`

**Protocol**: Propose-Act

**When to Use**:
- When code review identifies code smells
- During refactoring initiatives
- To improve code maintainability
- When applying SOLID principles to existing code
- For technical debt reduction efforts

## Parameters

### Required Inputs
- **code_input**: The code to analyze and improve
- **project_name**: Name of the project for report generation

### Optional Inputs
- **context**: Purpose, constraints, or system context of the code
- **refactoring_scope**: Desired level of transformation (minimal|moderate|comprehensive, default: moderate)
- **priority_focus**: Primary improvement area (readability|performance|maintainability|testability|all, default: all)
- **generate_report**: Whether to save actionable report (default: true)

### Context Requirements
- Code to be refactored
- Understanding of system constraints
- Optional: existing tests for validation

## Output

Comprehensive refactoring with clear explanations and actionable improvements.

**Deliverables**:
- Identified code smells with categorization
- Before/after code comparisons
- SOLID principles application examples
- Incremental transformation steps
- Explanation of each improvement
- Optional: actionable report document

**Format**: Inline code transformations with explanations, optional markdown report

## Examples

### Example 1: SOLID Principles Application

**Scenario**: Class with multiple responsibilities violating SRP

**Command**:
```
fix code smells
```

**Input**:
- code_input: [UserManager class handling authentication, validation, and database operations]
- project_name: "user-service"
- priority_focus: "maintainability"

**Result**: Refactored into separate classes (AuthenticationService, UserValidator, UserRepository) following Single Responsibility Principle

### Example 2: Comprehensive Refactoring

**Scenario**: Legacy code with multiple code smells

**Command**:
```
fix code smells
```

**Input**:
- code_input: [complex method with deep nesting, long parameter list, duplicated code]
- project_name: "payment-processor"
- refactoring_scope: "comprehensive"

**Result**: Applied Extract Method, Introduce Parameter Object, and Remove Duplication patterns with detailed explanations

## Related Competencies

- **review-code**: Use first to identify code smells
- **improve-cyclomatic-complexity**: Apply for complexity-specific issues
- **evolve-code-iteratively**: Use for multi-iteration refactoring
- **assess-code-quality-principles**: Validate improvements against principles
- **augment-code-unit-test**: Add tests after refactoring

## Tips & Best Practices

- Start with smallest refactoring scope and increase as needed
- Focus on one code smell category at a time
- Ensure tests exist before refactoring
- Apply incremental transformations
- Document rationale for each change
- Balance perfection with practical constraints
- Consider system-wide impact of changes

## Limitations

- Requires understanding of SOLID principles for best results
- May suggest changes that conflict with existing architecture
- Some refactorings may require broader system changes
- Automated detection may miss context-specific smells
- Refactoring scope affects transformation depth
