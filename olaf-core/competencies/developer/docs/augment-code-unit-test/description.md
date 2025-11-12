# Create Unit Tests

## Overview

This competency generates comprehensive unit tests for code modules by analyzing existing test patterns, identifying coverage gaps, and creating meaningful tests that validate core functionality while avoiding trivial test anti-patterns.

## Purpose

Adequate unit test coverage is essential for maintaining code quality, enabling safe refactoring, and catching bugs early. This competency systematically improves test coverage by analyzing code complexity, identifying untested paths, and generating tests that focus on meaningful validation rather than trivial assertions like getter/setter tests.

## Usage

**Command**: `create unit tests` (or aliases: `augment tests`, `augment unit test`, `improve test coverage`, `unit test augmentation`)

**Protocol**: Propose-Act

**When to Use**: Use when you need to improve test coverage for complex modules, establish testing patterns for new code, validate critical business logic, or prepare code for refactoring by ensuring adequate test protection.

## Parameters

### Required Inputs
- **code_path**: Directory path containing the codebase to test
- **target_coverage**: Desired test coverage percentage (default: 55%)

### Optional Inputs
- **file_filter**: Specific file types or patterns to focus on
- **batch_size**: Number of files to process per iteration (default: 10)
- **max_iterations**: Maximum number of improvement cycles (default: 10)

### Context Requirements
- Existing codebase with some test infrastructure
- Testing framework installed and configured
- Write access to test directories
- Understanding of existing test patterns helps maintain consistency

## Output

Generates unit tests and produces comprehensive coverage reports.

**Deliverables**:
- New unit test files following existing patterns
- Updated test coverage metrics
- Iteration results documenting progress
- Final report with coverage statistics
- Recommendations for future testing improvements

**Format**: Test files in appropriate testing framework format, JSON reports for metrics tracking

## Examples

### Example 1: Improving Coverage for Complex Business Logic

**Scenario**: Core business logic has only 30% test coverage

**Command**:
```
create unit tests
```

**Input**:
```
code_path: src/business-logic
target_coverage: 55%
```

**Result**: Generated 34 new unit tests across 7 modules, increased coverage from 30% to 58%, focused on complex validation and calculation functions, avoided trivial getter/setter tests.

### Example 2: Preparing for Refactoring

**Scenario**: Need test protection before refactoring a legacy module

**Command**:
```
augment unit test
```

**Input**:
```
code_path: src/legacy/payment-processor
target_coverage: 70%
max_iterations: 5
```

**Result**: Created comprehensive test suite with 45 tests covering edge cases, error handling, and business rules, enabling safe refactoring with confidence.

## Related Competencies

- **analyze-function-complexity**: Identify complex functions that need thorough testing
- **review-code**: Includes test coverage assessment as part of code review
- **evolve-code-iteratively**: Iterative improvement that includes test enhancement
- **fix-code-smells**: Often requires adding tests to enable safe refactoring

## Tips & Best Practices

- Start with the most complex modules first for maximum impact
- Focus on meaningful tests that validate business logic, not trivial assertions
- Follow existing test patterns and naming conventions in the codebase
- Run tests after each iteration to ensure they pass
- Aim for 55-80% coverage as a practical target (100% is often impractical)
- Test edge cases, error conditions, and boundary values
- Avoid testing framework code or simple getters/setters
- Use the iterative approach to manage large codebases effectively

## Limitations

- Cannot generate tests for code that requires complex external dependencies without mocking
- Test quality depends on understanding of business requirements
- May require manual adjustment for framework-specific testing patterns
- Cannot validate that tests actually test the right behavior
- Limited to unit tests - does not create integration or end-to-end tests
- Requires existing test infrastructure and framework
- May hit session limits on very large codebases (use batch processing)
