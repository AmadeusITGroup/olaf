# Function Analysis Report

**Purpose**: Standardized template for analyzing function complexity, structure, and quality metrics  
**Used By**: analyze-function-complexity prompt  
**Version**: 1.0  
**Last Updated**: 2025-10-27

---

## Template Structure

**Function**: `{function_name}`  
**File**: `{file_path}`  
**Language**: `{language}`  
**Analysis Date**: {timestamp}

## Function Signature
```{language}
{function_signature}
```

## Complexity Metrics
- **Cyclomatic Complexity**: {complexity_score}
- **Lines of Code**: {line_count}
- **Complexity Density**: {complexity_density}
- **Nesting Depth**: {max_nesting_depth}
- **Parameter Count**: {parameter_count}

## Complexity Breakdown
| Construct Type | Count | Complexity Points |
|---------------|-------|------------------|
| If/Else | {if_count} | {if_complexity} |
| Loops | {loop_count} | {loop_complexity} |
| Switch/Case | {switch_count} | {switch_complexity} |
| Logical Operators | {logical_count} | {logical_complexity} |
| Exception Handling | {exception_count} | {exception_complexity} |

## Risk Assessment
**Risk Level**: {risk_level} (Low/Moderate/High/Very High/Critical)

| Complexity Range | Risk | Status |
|-----------------|------|--------|
| 1-5 | Low | ✅ Simple, maintainable |
| 6-10 | Moderate | ⚠️ Acceptable, monitor |
| 11-20 | High | 🔶 Consider refactoring |
| 21-50 | Very High | 🔴 Refactor recommended |
| 50+ | Critical | 🚨 Immediate attention required |

## Code Quality Indicators
- **Readability**: {readability_score}/10
- **Maintainability**: {maintainability_score}/10
- **Testability**: {testability_score}/10

## Dependencies
- **Functions Called**: {called_functions}
- **External Dependencies**: {external_deps}
- **Coupling Level**: {coupling_level}

## Recommendations
{recommendations_list}

## Refactoring Opportunities
{refactoring_suggestions}

## Test Coverage Recommendations
Based on complexity score of {complexity_score}, this function requires:
- **Minimum Test Cases**: {min_test_cases}
- **Branch Coverage Tests**: {branch_tests}
- **Edge Case Tests**: {edge_case_tests}

---

## Placeholder Guide

- `{function_name}`: Name of the analyzed function
- `{file_path}`: Full path to the file containing the function
- `{language}`: Programming language (e.g., Java, Python, JavaScript)
- `{timestamp}`: Analysis timestamp in YYYYMMDD-HHmm format
- `{function_signature}`: Complete function signature including parameters and return type
- `{complexity_score}`: Calculated cyclomatic complexity value
- `{line_count}`: Number of lines of code (excluding comments and blank lines)
- `{complexity_density}`: Ratio of complexity to line count
- `{max_nesting_depth}`: Maximum depth of nested control structures
- `{parameter_count}`: Number of function parameters
- `{if_count}`, `{loop_count}`, etc.: Count of each construct type
- `{if_complexity}`, `{loop_complexity}`, etc.: Complexity points contributed by each construct type
- `{risk_level}`: Overall risk assessment (Low/Moderate/High/Very High/Critical)
- `{readability_score}`, `{maintainability_score}`, `{testability_score}`: Quality scores out of 10
- `{called_functions}`: List of functions called within this function
- `{external_deps}`: External dependencies used
- `{coupling_level}`: Assessment of coupling (Low/Medium/High)
- `{recommendations_list}`: Specific, actionable recommendations for improvement
- `{refactoring_suggestions}`: Concrete refactoring opportunities identified
- `{min_test_cases}`, `{branch_tests}`, `{edge_case_tests}`: Recommended test coverage based on complexity

## Example

```markdown
# Function Analysis Report

**Function**: `processUserData`  
**File**: `src/services/UserService.java`  
**Language**: Java  
**Analysis Date**: 20251027-1430

## Function Signature
```java
public UserResponse processUserData(UserRequest request, boolean validateOnly) throws ValidationException
```

## Complexity Metrics
- **Cyclomatic Complexity**: 15
- **Lines of Code**: 85
- **Complexity Density**: 0.18
- **Nesting Depth**: 4
- **Parameter Count**: 2

## Complexity Breakdown
| Construct Type | Count | Complexity Points |
|---------------|-------|------------------|
| If/Else | 8 | 8 |
| Loops | 2 | 2 |
| Switch/Case | 1 | 3 |
| Logical Operators | 4 | 2 |
| Exception Handling | 2 | 0 |

## Risk Assessment
**Risk Level**: High (🔶 Consider refactoring)

## Code Quality Indicators
- **Readability**: 6/10
- **Maintainability**: 5/10
- **Testability**: 4/10

## Dependencies
- **Functions Called**: validateUser, transformData, saveToDatabase, sendNotification
- **External Dependencies**: UserValidator, DataTransformer, DatabaseService
- **Coupling Level**: High

## Recommendations
1. Extract validation logic into separate method (lines 10-25)
2. Extract data transformation into separate method (lines 30-50)
3. Reduce nesting depth by using early returns
4. Consider splitting into multiple smaller functions

## Refactoring Opportunities
- Apply Extract Method pattern for validation and transformation
- Introduce Strategy pattern for different validation types
- Use Guard Clauses to reduce nesting

## Test Coverage Recommendations
Based on complexity score of 15, this function requires:
- **Minimum Test Cases**: 8
- **Branch Coverage Tests**: 15
- **Edge Case Tests**: 5
```

## Notes

- Always calculate complexity using language-specific patterns
- Consider function context and purpose when assessing risk
- Provide specific, actionable recommendations with line numbers
- Include both quantitative metrics and qualitative assessment
- Balance thoroughness with clarity in reporting
