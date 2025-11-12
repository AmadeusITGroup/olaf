# Step-by-Step Tutorial

**Analyze Function Complexity: Step-by-Step Tutorial**

**How to Execute the "Function Complexity Analysis" Workflow**

This tutorial shows exactly how to execute a detailed function complexity analysis using the OLAF developer competency's analyze-function-complexity functionality. This workflow analyzes a specific function's complexity, structure, and provides detailed metrics similar to complexity analyzer tools.

## Prerequisites

- OLAF framework properly installed and configured
- Function code to analyze (either file path or function name in workspace)
- Basic understanding of code complexity concepts
- Access to project files or codebase

## Step-by-Step Instructions

### Step 1: Initiate Function Complexity Analysis

[Brief description: Start the function complexity analysis process by invoking the OLAF analyze-function-complexity competency]

**User Action:**

1. Open your terminal or OLAF interface
2. Navigate to your project directory (if analyzing functions in workspace)
3. Execute the OLAF analyze-function-complexity competency using one of these methods:
   - Direct invocation: `olaf analyze-function-complexity`
   - Via aliases: `olaf analyze complexity`, `olaf function complexity`, `olaf complexity analysis`

**OLAF Response:**
The system will prompt you to provide the required parameters for function analysis.

### Step 2: Provide Function Parameters

**User Action:** Specify the function to analyze and optional context

```text
Required Parameters:
- function_name: Name of the function to analyze
- file_path: Path to the file containing the function (optional)
- language: Programming language (optional, auto-detected if file provided)
- context: Additional context about the function's purpose (optional)
```

**Provide Requirements/Parameters:**

- **function_name**: [Example - we used "calculateTotalPrice"]
- **file_path**: [Example - we used "src/services/orderService.js"] (optional)
- **language**: [Example - we used "JavaScript"] (optional)
- **context**: [Example - we used "E-commerce order processing function"] (optional)

### Step 3: Function Location and Extraction

**What OLAF Does:**

- If file_path provided: Locates the function in the specified file
- If only function_name provided: Searches the current workspace for the function
- Extracts the complete function code including signature and body
- Validates that the function exists and is accessible
- Gets current timestamp for analysis report

**You Should See:** Confirmation that the function was located and extracted successfully

### Step 4: Comprehensive Complexity Analysis

**What OLAF Does:**

- **Calculates cyclomatic complexity** using standard patterns:
  - Decision points: if, else if, else, switch, case
  - Loops: for, foreach, while, do-while
  - Logical operators: &&, ||, and, or
  - Exception handling: try, catch, except, finally
  - Ternary operators: ? :
- **Counts lines of code** (excluding comments and blank lines)
- **Calculates complexity density** (complexity / line_count)
- **Analyzes function structure** (parameters, return type, nesting depth)
- **Performs dependency analysis** (functions/methods called)

**You Should See:** Progress updates for complexity calculations and structural analysis

### Step 5: Quality Assessment and Report Generation

**User Action:** Review the complexity analysis results when presented

**What OLAF Does:**

- Generates code readability score and maintainability indicators
- Identifies potential refactoring opportunities
- Assesses best practices adherence
- Creates risk assessment with standard thresholds
- Generates comprehensive analysis report using the function-complexity-analysis template
- Provides specific, actionable recommendations for improvement

**You Should See:** Complete complexity analysis report with metrics, risk assessment, and recommendations

## Verification Checklist

✅ **Function successfully located and extracted**
✅ **Cyclomatic complexity calculated with breakdown by construct type**
✅ **Lines of code counted (excluding comments and blank lines)**
✅ **Complexity density calculated and assessed**
✅ **Function structure analyzed (signature, nesting, dependencies)**
✅ **Quality assessment completed with specific recommendations**

## Troubleshooting

**If function cannot be located:**

```bash
grep -r "function functionName" . --include="*.js" --include="*.ts" --include="*.py" --include="*.java"
find . -name "*.js" -exec grep -l "functionName" {} \;
```

**If complexity calculations seem incorrect:**

- Verify the programming language is correctly identified
- Check that all decision points and loops are counted
- Ensure nested complexity is properly calculated
- Review language-specific complexity patterns

**If no refactoring opportunities identified:**

- Consider that the function may already be well-structured
- Review the complexity thresholds for the specific language
- Check if the function follows single responsibility principle

## Key Learning Points

1. **Cyclomatic Complexity:** Measures the number of linearly independent paths through a program's source code, helping identify testing requirements
2. **Quality Indicators:** Analysis includes readability, maintainability, and testability assessments beyond just complexity numbers
3. **Actionable Recommendations:** All suggestions are specific, prioritized, and include refactoring opportunities

## Next Steps to Try

- Use the complexity analysis to prioritize functions for refactoring
- Apply the recommended improvements and re-analyze to measure progress
- Set up complexity thresholds for your team's coding standards
- Use complexity density metrics to identify overly complex functions

## Expected Timeline

- **Total analysis time:** 2-5 minutes (depending on function size and complexity)
- **User input required:** Function identification and parameters (30 seconds - 1 minute)
- **OLAF execution time:** Function extraction, complexity calculation, and analysis (1-3 minutes)
- **Report generation:** Detailed analysis report with recommendations (30 seconds - 1 minute)