---
name: analyze-function-complexity
description: Analyze a specific function's complexity, structure, and provide detailed metrics similar to complexity analyzer output
tags: [function-analysis, complexity, code-quality, metrics]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **function_name**: string - Name of the function to analyze
- **file_path**: string - (Optional) Path to the file containing the function
- **language**: string - (Optional) Programming language (auto-detected if file_path provided)
- **context**: string - (Optional) Additional context about the function's purpose

## Process

1. **Function Location**:
   - If file_path provided, locate the function in the file
   - If only function_name provided, search the current workspace
   - Extract the complete function code including signature and body

2. **Complexity Analysis**:
   - Calculate cyclomatic complexity using standard patterns:
     - Decision points: if, else if, else, switch, case
     - Loops: for, foreach, while, do-while
     - Logical operators: &&, ||, and, or
     - Exception handling: try, catch, except, finally
     - Ternary operators: ? :
   - Count lines of code (excluding comments and blank lines)
   - Calculate complexity density (complexity / line_count)

3. **Structure Analysis**:
   - Function signature analysis (parameters, return type)
   - Nesting depth analysis
   - Variable scope analysis
   - Dependency analysis (functions/methods called)

4. **Quality Assessment**:
   - Code readability score
   - Maintainability indicators
   - Potential refactoring opportunities
   - Best practices adherence

## Output Format

Use template: `[id:competencies_dir]developer/templates/function-complexity-analysis-template.md`

The report should include:
- Function signature and metadata
- Complexity metrics (cyclomatic complexity, lines of code, nesting depth)
- Breakdown by construct type (if/else, loops, switch, logical operators)
- Risk assessment with standard thresholds
- Code quality indicators (readability, maintainability, testability)
- Dependencies and coupling analysis
- Specific recommendations for improvement
- Refactoring opportunities
- Test coverage recommendations based on complexity

## Output to USER
1. **Summary**: Brief overview of complexity and risk level
2. **Key Metrics**: Most important numbers (complexity, lines, density)
3. **Immediate Actions**: Priority recommendations
4. **Detailed Report**: Full analysis as formatted above

## Domain-Specific Rules
- Rule 1: Always provide specific, actionable recommendations
- Rule 2: Include complexity calculation methodology
- Rule 3: Consider language-specific patterns and idioms
- Rule 4: Provide context-appropriate thresholds
- Rule 5: Include both quantitative metrics and qualitative assessment

## Required Actions
1. Locate and extract the target function
2. Calculate all complexity metrics
3. Assess code quality indicators
4. Generate risk assessment
5. Provide specific recommendations
6. Format comprehensive report

⚠️ **Critical Notes**
- Use language-specific complexity patterns
- Consider function context and purpose
- Balance thoroughness with clarity
- Provide actionable, specific guidance
- Include positive aspects when present
