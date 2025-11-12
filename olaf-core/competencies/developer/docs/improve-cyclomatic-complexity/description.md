# Improve Cyclomatic Complexity

**Source**: olaf-core/competencies/developer/prompts/improve-cyclomatic-complexity.md

## Overview

Systematically reduce cyclomatic complexity of code sections while preserving functionality and improving maintainability. Provides phased refactoring approach with complexity measurement.

## Purpose

High cyclomatic complexity makes code difficult to understand, test, and maintain. This competency analyzes complex code, identifies root causes, and applies targeted refactoring techniques to reduce complexity while preserving behavior. It ensures changes are validated through testing and measured for improvement.

## Usage

**Command**: `improve complexity`

**Protocol**: Propose-Act

**When to Use**:
- When code complexity metrics exceed thresholds
- During code review identifying complex methods
- To improve code testability
- When reducing technical debt
- For making code more maintainable

## Parameters

### Required Inputs
- **target_code**: The method/function with high cyclomatic complexity (include containing class/module and file location)
- **programming_language**: The programming language of the code

### Optional Inputs
- **test_information**: Available test information and coverage details
- **interface_restrictions**: Restrictions on changing interfaces/signatures
- **performance_requirements**: Performance constraints to consider
- **compatibility_needs**: Backward compatibility requirements
- **target_complexity**: Target cyclomatic complexity score (default: <10)

### Context Requirements
- Code with high cyclomatic complexity
- Existing tests for validation
- Understanding of interface constraints

## Output

Refactored code with reduced complexity and preserved functionality.

**Deliverables**:
- Current complexity assessment with score
- Visual control flow representation
- Root cause analysis of complexity
- Phased refactoring strategy
- Refactored code with reduced complexity
- New complexity measurements
- Test validation results

**Format**: Code transformations with complexity analysis, saved to `[id:findings_dir]code-evolution/`

## Examples

### Example 1: Nested Conditionals Refactoring

**Scenario**: Method with deeply nested if-else statements (complexity: 18)

**Command**:
```
improve complexity
```

**Input**:
- target_code: [processOrder method with nested conditionals]
- programming_language: "Java"
- target_complexity: 8

**Result**: Refactored using Extract Method and Guard Clauses, reduced complexity from 18 to 7

### Example 2: State-Based Complexity Reduction

**Scenario**: Complex state machine logic (complexity: 25)

**Command**:
```
improve complexity
```

**Input**:
- target_code: [handleEvent method with state transitions]
- programming_language: "TypeScript"
- target_complexity: 10

**Result**: Applied State Pattern, extracted state classes, reduced complexity from 25 to 6 per method

## Related Competencies

- **analyze-function-complexity**: Use first to identify complex functions
- **fix-code-smells**: Apply for broader code quality improvements
- **evolve-code-iteratively**: Use for multi-iteration complexity reduction
- **review-code**: Validate complexity improvements
- **augment-code-unit-test**: Improve test coverage after refactoring

## Tips & Best Practices

- Measure complexity before and after refactoring
- Start with highest complexity methods first
- Use Extract Method as primary technique
- Apply design patterns for state-based complexity
- Ensure tests pass after each refactoring step
- Consider Guard Clauses for early returns
- Replace conditionals with polymorphism when appropriate
- Keep target complexity realistic (<10 is good goal)

## Limitations

- Some complexity is inherent to business logic
- Refactoring may increase number of methods/classes
- Interface restrictions may limit refactoring options
- Performance requirements may constrain approaches
- Requires good test coverage for safe refactoring
