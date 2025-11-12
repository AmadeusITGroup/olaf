# Step-by-Step Tutorial

**Improve Cyclomatic Complexity: Step-by-Step Tutorial**

**How to Execute the "Systematic Cyclomatic Complexity Reduction" Workflow**

This tutorial shows exactly how to systematically reduce cyclomatic complexity of code sections while preserving functionality and improving maintainability using the OLAF developer competency's improve-cyclomatic-complexity functionality.

## Prerequisites

- OLAF framework properly installed and configured
- Code with high cyclomatic complexity to refactor
- Existing test suite for the complex code (recommended)
- Basic understanding of refactoring principles and complexity metrics
- Access to project files and testing capabilities

## Step-by-Step Instructions

### Step 1: Initiate Complexity Improvement Analysis

[Brief description: Start the complexity reduction process by invoking the OLAF improve-cyclomatic-complexity competency]

**User Action:**

1. Open your terminal or OLAF interface
2. Navigate to your project directory containing the complex code
3. Execute the OLAF improve-cyclomatic-complexity competency using one of these methods:
   - Direct invocation: `olaf improve-cyclomatic-complexity`
   - Via aliases: `olaf improve complexity`, `olaf reduce complexity`, `olaf cyclomatic`

**OLAF Response:**
The system will prompt you to provide the required parameters for complexity analysis and reduction.

### Step 2: Provide Target Code and Requirements

**User Action:** Specify the complex code and constraints for refactoring

```text
Required Parameters:
- target_code: The method/function with high cyclomatic complexity (include location)
- programming_language: The programming language of the code
- test_information: Available test information and coverage details
- interface_restrictions: Restrictions on changing interfaces/signatures (optional)
- performance_requirements: Performance constraints to consider (optional)
- compatibility_needs: Backward compatibility requirements (optional)
- target_complexity: Target cyclomatic complexity score (default: <10)
```

**Provide Requirements/Parameters:**

- **target_code**: [Example - we used "OrderProcessingService.calculateTotalCost() in src/services/OrderService.java"]
- **programming_language**: [Example - we used "Java"]
- **test_information**: [Example - we used "Unit tests exist with 85% coverage, missing edge cases"]
- **interface_restrictions**: [Example - we used "Cannot change public method signature"]
- **performance_requirements**: [Example - we used "Must maintain sub-100ms execution time"]
- **target_complexity**: [Example - we used "8"] (optional)

### Step 3: Current Complexity Assessment

**What OLAF Does:**

- Estimates current cyclomatic complexity score
- Identifies all decision points (conditionals, loops, switch statements)
- Creates visual representation of control flow
- Pinpoints the most complex code sections
- Gets current timestamp for analysis reports

**You Should See:** Detailed complexity breakdown with decision point analysis and control flow visualization

### Step 4: Test Coverage Evaluation and Root Cause Analysis

**What OLAF Does:**

- **Analyzes existing unit tests** for the complex code
- **Identifies untested paths** and edge cases
- **Documents baseline behavior** for validation
- **Analyzes root causes** of complexity:
  - Mixed levels of abstraction
  - Multiple responsibilities in single method
  - Deep nesting structures
  - Complex boolean logic
  - State-based complexity
  - Error handling mixed with business logic

**You Should See:** Test coverage report and detailed root cause analysis of complexity patterns

### Step 5: Refactoring Strategy Design and Implementation

**User Action:** Review and approve the proposed refactoring strategy

**What OLAF Does:**

- **Develops phased approach** to reduce complexity
- **Prioritizes changes** for maximum impact
- **Selects appropriate refactoring techniques:**
  - Extract Methods/Functions
  - Replace conditionals with polymorphism
  - Introduce design patterns (Strategy, State, Command)
  - Simplify boolean expressions
  - Extract specialized classes/objects
- **Implements refactoring** in small, incremental steps
- **Preserves existing behavior** exactly

**You Should See:** Detailed refactoring plan and step-by-step implementation with preserved functionality

### Step 6: Verification and Measurement

**What OLAF Does:**

- Confirms all tests pass after refactoring
- Measures new complexity metrics
- Validates behavior preservation
- Assesses readability and testability improvements
- Generates comprehensive complexity-reduction report
- Saves all reports to `olaf-data/findings/code-evolution/`

**You Should See:** Before/after comparison with improved complexity metrics and verification results

## Verification Checklist

✅ **Current complexity assessed with decision point breakdown**
✅ **Test coverage evaluated and gaps identified**
✅ **Root causes of complexity analyzed and documented**
✅ **Phased refactoring strategy developed and approved**
✅ **Refactoring implemented with behavior preservation**
✅ **All existing tests pass after refactoring**
✅ **New complexity metrics measured and improved**

## Troubleshooting

**If tests fail after refactoring:**

```bash
# Run specific test suite
mvn test -Dtest=OrderServiceTest
npm test -- OrderService.test.js
pytest tests/test_order_service.py
```

**If complexity doesn't improve as expected:**

- Review if all decision points were addressed
- Check for hidden complexity in extracted methods
- Verify that design patterns were applied correctly
- Consider additional refactoring techniques

**If refactoring breaks external interfaces:**

- Revert changes and review interface restrictions
- Apply adapter pattern to maintain compatibility
- Consider internal refactoring only without interface changes

## Key Learning Points

1. **Incremental Approach:** Complexity reduction works best with small, testable changes rather than large refactoring efforts
2. **Behavior Preservation:** All existing functionality must be preserved exactly; refactoring changes structure, not behavior
3. **Test-Driven Safety:** Comprehensive test coverage is essential before attempting complexity reduction

## Next Steps to Try

- Apply the refactoring strategy in phases as recommended
- Add additional test cases for uncovered paths identified during analysis
- Monitor complexity metrics in future development to prevent regression
- Use extracted methods and patterns as templates for similar complexity issues

## Expected Timeline

- **Total complexity improvement time:** 30-90 minutes (depending on complexity and code size)
- **User input required:** Code identification and constraints specification (5-10 minutes)
- **OLAF analysis time:** Complexity assessment, root cause analysis, and strategy design (15-30 minutes)
- **Implementation verification:** Refactoring execution and testing validation (10-50 minutes)