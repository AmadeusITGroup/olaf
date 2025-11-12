# Evolve Code Iteratively

**Source**: olaf-core/competencies/developer/prompts/evolve-code-iteratively.md

## Overview

Incrementally improve code based on specific goals (performance, maintainability, testability) using a structured, iterative approach with user-guided decision making at each step.

## Purpose

Code improvement often requires multiple iterations to achieve optimal results. This competency provides a structured approach to code evolution, presenting options at each iteration and allowing developers to guide the improvement process. It ensures changes are validated, documented, and reversible while maintaining focus on specific improvement goals.

## Usage

**Command**: `evolve code`

**Protocol**: Act

**When to Use**:
- When refactoring complex code requiring multiple iterations
- To improve code performance systematically
- For enhancing code maintainability and readability
- When increasing testability of existing code
- To explore different refactoring approaches with guidance

## Parameters

### Required Inputs
- **code**: The code to be analyzed and evolved
- **goals**: Primary goals from: performance, maintainability, testability (select one or more)

### Optional Inputs
- **iterations**: Maximum number of iterations (default: 3, max: 5)
- **test_cases**: Test cases to validate changes

### Context Requirements
- Code to be improved (file or snippet)
- Clear improvement goals
- Optional: existing tests for validation

## Output

Comprehensive improvement report documenting the iterative evolution process.

**Deliverables**:
- Initial assessment with baseline metrics
- Iteration reports for each improvement cycle
- Before/after code comparisons with annotations
- Metrics comparison showing improvements
- Decision log with rationale for each change
- Rollback instructions for each iteration
- Final recommendations for future work

**Format**: Markdown report following code-evolution-report-template.md, saved to `[id:ads_dir]/code-evolution/YYYYMMDD-HHmm/`

## Examples

### Example 1: Performance Optimization

**Scenario**: Improving slow data processing function

**Command**:
```
evolve code
```

**Input**:
- code: [data processing function]
- goals: ["performance"]
- iterations: 3

**Result**: Three iterations of improvements: 1) Algorithm optimization, 2) Caching implementation, 3) Parallel processing, with 60% performance improvement

### Example 2: Maintainability Enhancement

**Scenario**: Refactoring complex legacy code

**Command**:
```
evolve code
```

**Input**:
- code: [legacy function]
- goals: ["maintainability", "testability"]
- iterations: 4

**Result**: Four iterations: 1) Extract methods, 2) Simplify conditionals, 3) Add dependency injection, 4) Improve naming, reducing complexity by 40%

## Related Competencies

- **review-code**: Use before evolution to identify improvement areas
- **fix-code-smells**: Apply to address specific code smells
- **improve-cyclomatic-complexity**: Use for complexity-focused improvements
- **augment-code-unit-test**: Add tests after evolution
- **assess-code-quality-principles**: Validate improvements against principles

## Tips & Best Practices

- Start with clear, measurable goals
- Review each iteration before proceeding
- Keep iterations small and focused
- Validate changes with tests after each iteration
- Document decision rationale for future reference
- Use rollback instructions if iteration doesn't meet goals
- Consider stopping early if goals are achieved

## Limitations

- Requires clear improvement goals to be effective
- Metrics may be approximate for some goals
- Complex refactoring may require more iterations than maximum
- User must evaluate and approve each iteration
- May not address architectural issues requiring broader changes
