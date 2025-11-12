---
name: improve-cyclomatic-complexity
description: Systematically reduce cyclomatic complexity of code sections while preserving functionality and improving maintainability
tags: [refactoring, complexity, code-quality, testing]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **target_code**: string - The method/function with high cyclomatic complexity (include containing class/module and file location)
- **programming_language**: string - The programming language of the code
- **test_information**: string - Available test information and coverage details
- **interface_restrictions**: string - Optional restrictions on changing interfaces/signatures
- **performance_requirements**: string - Optional performance constraints to consider
- **compatibility_needs**: string - Optional backward compatibility requirements
- **target_complexity**: number - Optional target cyclomatic complexity score (default: <10)

If the user does not provide input, make your best to find the answers by analyzing the code base. then once you have the information, you ask for sign-off to the USER.

ALl reports or notes you wish to create or that are requested by teh USER must be saved in [id:findings_dir]code-evolution/

## Process

1. **Assess Current Complexity**:
   - Estimate current cyclomatic complexity score
   - Identify decision points (conditionals, loops, switch statements)
   - Create visual representation of control flow
   - Pinpoint the most complex code sections

2. **Evaluate Test Coverage**:
   - Analyze existing unit tests for the complex code
   - Identify untested paths and edge cases
   - Document baseline behavior for validation
   - Suggest additional test cases if coverage is insufficient

3. **Analyze Root Causes**:
   - Identify complexity patterns:
     - Mixed levels of abstraction
     - Multiple responsibilities in single method
     - Deep nesting structures
     - Complex boolean logic
     - State-based complexity
     - Error handling mixed with business logic

4. **Design Refactoring Strategy**:
   - Develop phased approach to reduce complexity
   - Prioritize changes for maximum impact
   - Select appropriate refactoring techniques:
     - Extract Methods/Functions
     - Replace conditionals with polymorphism
     - Introduce design patterns (Strategy, State, Command)
     - Simplify boolean expressions
     - Extract specialized classes/objects

5. **Apply Refactoring**:
   - Implement refactoring in small, incremental steps
   - Preserve existing behavior exactly
   - Run tests after each change
   - Ensure all functionality remains intact

6. **Verify and Measure**:
   - Confirm all tests pass
   - Measure new complexity metrics
   - Validate behavior preservation
   - Assess readability and testability improvements

## Output Format

Use template: `[id:competencies_dir]developer/templates/complexity-reduction-report-template.md`

The report should include:
- Current complexity assessment with decision point breakdown
- Control flow visualization
- Test coverage evaluation
- Root cause analysis of complexity patterns
- Phased refactoring strategy
- Refactored implementation with supporting classes/methods
- Verification results and metrics comparison
- Behavior preservation validation
- Updated test cases

## Output to USER
- **Analysis Report**: Current complexity metrics, identified patterns, control flow visualization
- **Refactoring Plan**: Prioritized steps and techniques to apply
- **Refactored Implementation**: Complete refactored code with supporting classes/methods
- **Before/After Comparison**: Complexity metrics, code size, readability assessment
- **Test Updates**: Updated or new test cases if necessary
- Next phase: Code review and integration of refactored implementation

## Domain-Specific Rules
- Rule 1: Preserve existing behavior exactly - no functional changes
- Rule 2: Make small, incremental changes with test validation at each step
- Rule 3: Focus on single responsibility principle
- Rule 4: Keep methods/functions short and focused (ideally <20 lines)
- Rule 5: Improve naming to clarify intent and purpose
- Rule 6: Apply consistent coding standards for the target language
- Rule 7: Ensure adequate test coverage before and after refactoring

## Required Actions
1. Estimate current cyclomatic complexity and identify decision points
2. Analyze existing tests and identify coverage gaps
3. Determine root causes of complexity
4. Create prioritized refactoring plan
5. Implement refactoring with incremental testing
6. Verify behavior preservation and measure improvements

⚠️ **Critical Notes**
- Never change external interfaces without explicit permission
- All existing tests must continue to pass after refactoring
- Complexity reduction must not compromise performance requirements
- Document any complex algorithms that cannot be simplified further
- Ensure team familiarity with introduced design patterns
