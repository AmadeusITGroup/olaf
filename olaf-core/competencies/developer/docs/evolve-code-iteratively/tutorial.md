# Step-by-Step Tutorial

**Evolve Code Iteratively: Step-by-Step Tutorial**

**How to Execute the "Iterative Code Improvement" Workflow**

This tutorial shows exactly how to incrementally improve code based on specific goals (performance, maintainability, testability) using the OLAF developer competency's evolve-code-iteratively functionality with a structured, iterative approach.

## Prerequisites

- OLAF framework properly installed and configured
- Code that needs improvement (performance, maintainability, or testability)
- Clear improvement goals and success criteria
- Basic understanding of iterative development principles
- Test cases to validate changes (recommended)

## Step-by-Step Instructions

### Step 1: Initiate Iterative Code Evolution

[Brief description: Start the iterative code improvement process by invoking the OLAF evolve-code-iteratively competency]

**User Action:**

1. Open your terminal or OLAF interface
2. Prepare the code you want to improve (copy or identify file location)
3. Execute the OLAF evolve-code-iteratively competency using one of these methods:
   - Direct invocation: `olaf evolve-code-iteratively`
   - Via aliases: `olaf evolve code`, `olaf iterative development`, `olaf improve iteratively`

**OLAF Response:**
The system will prompt you to provide the required code and improvement parameters.

### Step 2: Provide Code and Improvement Goals

**User Action:** Specify the code to improve and your goals

```text
Required Parameters:
- code: The code to be analyzed and evolved (REQUIRED)
- goals: Primary goals - performance, maintainability, testability (REQUIRED)
- iterations: Maximum number of iterations (optional, default: 3, max: 5)
- test_cases: Test cases to validate changes (optional)
```

**Provide Requirements/Parameters:**

- **code**: [Example - we used complete function/class code or file path]
- **goals**: [Example - we used ["maintainability", "testability"]]
- **iterations**: [Example - we used "4"] (optional)
- **test_cases**: [Example - we used "Jest unit tests covering main functionality"] (optional)

### Step 3: Initial Assessment and Baseline

**What OLAF Does:**

- Analyzes code structure and patterns thoroughly
- Establishes baseline metrics (lines, functions, complexity indicators)
- Identifies optimization opportunities with estimated impact
- Documents current state and technical debt
- Gets current timestamp for iteration tracking
- Creates directory structure: `olaf-data/findings/code-evolution/YYYYMMDD-HHmm/`

**You Should See:** Comprehensive initial assessment with baseline metrics and identified improvement opportunities

### Step 4: Iterative Improvement Cycles

**What OLAF Does for Each Iteration:**

- **Critiques current code** against specified goals
- **Proposes two distinct solutions** with specific implementation details
- **Presents options comparison** with pros/cons table
- **Makes a recommendation** and asks for your feedback

**User Action:** Choose your preferred option:

```text
Decision Options:
- "Option 1": Implement the first proposed solution
- "Option 2": Implement the second proposed solution  
- "Stop here": End iterations and generate final report
```

**What OLAF Does After Your Choice:**

- Implements the selected changes
- Validates with unit tests (if available) or proposes basic validation
- Documents changes and measures impact where possible
- Continues to next iteration or stops based on your feedback

**You Should See:** Step-by-step iteration progress with clear before/after comparisons for each improvement

### Step 5: Finalization and Comprehensive Report

**What OLAF Does:**

- Generates comprehensive improvement report with available metrics
- Documents all changes made with rationale for each decision
- Provides annotated before/after code comparison
- Includes recommendations for future improvements
- Creates rollback instructions for each iteration
- Saves complete evolution report using the code-evolution-report template

**You Should See:** Complete evolution report with measurable improvements and detailed change documentation

## Verification Checklist

✅ **Initial code assessment completed with baseline metrics**
✅ **Improvement goals clearly defined and tracked**
✅ **Each iteration implemented with two-option decision process**
✅ **Functionality preserved throughout all iterations**
✅ **Changes validated with existing tests or proposed validation**
✅ **Comprehensive evolution report generated with rollback instructions**
✅ **All iterations documented in olaf-data/findings/code-evolution/**

## Troubleshooting

**If iterations don't show meaningful improvements:**

- Review if the improvement goals are realistic for the given code
- Check if the baseline code was already well-optimized
- Consider focusing on a single goal rather than multiple goals
- Stop iterations early if no further improvements are possible

**If functionality breaks during iterations:**

- Use the rollback instructions provided for the problematic iteration
- Review the validation process and ensure tests are comprehensive
- Consider smaller, more focused changes in future iterations

**If goals seem conflicting:**

- Prioritize goals (e.g., maintainability over performance)
- Consider separate iteration runs focusing on one goal at a time
- Discuss trade-offs explicitly in each iteration decision

## Key Learning Points

1. **Iterative Approach:** Small, focused changes with validation are more effective than large refactoring efforts
2. **Decision-Driven Process:** Each iteration requires explicit user choice between options, ensuring alignment with priorities
3. **Preservation Focus:** Functionality is preserved while improving non-functional aspects like maintainability and testability

## Next Steps to Try

- Implement the final improved code in your project
- Use the rollback instructions if any iteration needs to be reversed
- Apply the documented improvement patterns to similar code sections
- Set up automated metrics tracking to maintain code quality improvements

## Expected Timeline

- **Total evolution time:** 20-60 minutes (depending on code complexity and iteration count)
- **User input required:** Code submission, goal selection, and iteration decisions (5-15 minutes total)
- **OLAF analysis time:** Initial assessment and iterative improvement cycles (10-35 minutes)
- **Finalization:** Report generation with rollback instructions (5-10 minutes)