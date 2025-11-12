# Analyze Function Complexity

## Overview

This competency performs in-depth analysis of individual functions or methods, calculating cyclomatic complexity metrics, evaluating code structure, and providing actionable recommendations for improving maintainability and testability.

## Purpose

Complex functions are harder to understand, test, and maintain, leading to increased bug rates and slower development velocity. This competency identifies complexity hotspots by analyzing decision points, nesting depth, and code structure, then provides specific guidance for reducing complexity while preserving functionality.

## Usage

**Command**: `analyze function complexity` (or aliases: `analyze complexity`, `function complexity`, `complexity analysis`)

**Protocol**: Act

**When to Use**: Use when you need to understand why a specific function is difficult to work with, establish complexity baselines before refactoring, prioritize technical debt reduction, or validate that refactoring efforts have reduced complexity.

## Parameters

### Required Inputs
- **function_name**: Name of the function to analyze
- **file_path**: Path to the file containing the function (optional if workspace search is acceptable)
- **language**: Programming language (auto-detected if file_path provided)

### Optional Inputs
- **context**: Additional information about the function's purpose or constraints
- **target_complexity**: Desired complexity threshold (default: <10)

### Context Requirements
- Access to source code containing the target function
- Syntactically valid code
- Understanding of the function's role in the system helps contextualize findings

## Output

Generates a comprehensive function complexity analysis report with metrics and recommendations.

**Deliverables**:
- Function signature and metadata extraction
- Cyclomatic complexity score calculation
- Decision point breakdown by type (conditionals, loops, switches, logical operators)
- Nesting depth analysis
- Risk assessment using industry-standard thresholds
- Code quality indicators (readability, maintainability, testability scores)
- Dependency and coupling analysis
- Specific, actionable refactoring recommendations
- Test coverage recommendations based on complexity

**Format**: Structured markdown report using the function-complexity-analysis template

## Examples

### Example 1: Pre-Refactoring Assessment

**Scenario**: A function has become difficult to test and maintain over time

**Command**:
```
analyze function complexity
```

**Input**:
```
function_name: calculateShippingCost
file_path: src/shipping/calculator.ts
```

**Result**: Report showed complexity of 16 (high risk), identified 8 nested conditionals, recommended extracting 4 helper functions, and provided specific line ranges for extraction.

### Example 2: Validating Refactoring Success

**Scenario**: After refactoring, verify that complexity has been reduced

**Command**:
```
analyze complexity
```

**Input**:
```
function_name: calculateShippingCost
file_path: src/shipping/calculator.ts
```

**Result**: Confirmed complexity reduced from 16 to 7, nesting depth decreased from 4 to 2, maintainability score improved from 45 to 78.

## Related Competencies

- **improve-cyclomatic-complexity**: Follow-up competency that implements the refactoring recommendations from this analysis
- **review-code**: Broader code review that includes complexity assessment among other quality checks
- **fix-code-smells**: Addresses complexity as one type of code smell
- **evolve-code-iteratively**: Iterative improvement approach that can incorporate complexity reduction

## Tips & Best Practices

- Analyze functions before refactoring to establish measurable success criteria
- Prioritize functions with complexity >15 for immediate attention
- Use the decision point breakdown to identify extraction opportunities
- Consider domain complexity vs. accidental complexity when evaluating results
- Combine with unit test analysis to ensure safe refactoring
- Re-analyze after refactoring to validate improvements
- Track complexity trends across the codebase to identify systemic issues

## Limitations

- Measures syntactic complexity, not semantic or domain complexity
- Cannot determine if complexity is justified by business requirements
- Requires valid, parseable code
- Language-specific idioms may affect accuracy
- Does not validate correctness or functionality
- Cannot assess runtime performance implications
