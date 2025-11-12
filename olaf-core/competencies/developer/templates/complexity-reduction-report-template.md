# Cyclomatic Complexity Reduction Report

**Purpose**: Document systematic reduction of cyclomatic complexity while preserving functionality  
**Used By**: improve-cyclomatic-complexity prompt  
**Version**: 1.0  
**Last Updated**: 2025-10-27

---

## Template Structure

## Target Information
- **Target Code**: {target_identifier}
- **File Location**: {file_path}
- **Programming Language**: {programming_language}
- **Analysis Date**: {analysis_timestamp}

## Current Complexity Assessment

### Complexity Metrics
- **Current Cyclomatic Complexity**: {current_complexity}
- **Target Complexity**: {target_complexity}
- **Reduction Required**: {reduction_needed}
- **Risk Level**: {risk_level}

### Decision Points Identified
| Type | Count | Contribution |
|------|-------|--------------|
| If/Else Statements | {if_count} | {if_contribution} |
| Switch/Case Statements | {switch_count} | {switch_contribution} |
| Loops (for/while/do) | {loop_count} | {loop_contribution} |
| Logical Operators (&&/\|\|) | {logical_count} | {logical_contribution} |
| Try/Catch Blocks | {exception_count} | {exception_contribution} |
| **Total** | **{total_decision_points}** | **{current_complexity}** |

### Control Flow Visualization
```
{control_flow_diagram}
```

### Most Complex Sections
1. **Lines {section_1_lines}**: Complexity {section_1_complexity} - {section_1_description}
2. **Lines {section_2_lines}**: Complexity {section_2_complexity} - {section_2_description}
3. **Lines {section_3_lines}**: Complexity {section_3_complexity} - {section_3_description}

## Test Coverage Evaluation

### Existing Test Analysis
- **Total Tests**: {total_tests}
- **Code Coverage**: {code_coverage}%
- **Branch Coverage**: {branch_coverage}%
- **Untested Paths**: {untested_paths}

### Test Quality Assessment
```{language}
{test_example}
```

**Assessment**: {test_quality_assessment}

### Coverage Gaps
- {coverage_gap_1}
- {coverage_gap_2}
- {coverage_gap_3}

## Root Cause Analysis

### Complexity Patterns Identified

#### Pattern 1: {pattern_1_name}
- **Location**: Lines {pattern_1_lines}
- **Complexity Contribution**: {pattern_1_complexity}
- **Description**: {pattern_1_description}
- **Root Cause**: {pattern_1_root_cause}

#### Pattern 2: {pattern_2_name}
- **Location**: Lines {pattern_2_lines}
- **Complexity Contribution**: {pattern_2_complexity}
- **Description**: {pattern_2_description}
- **Root Cause**: {pattern_2_root_cause}

[Repeat for each pattern]

### Complexity Sources
- **Mixed Abstraction Levels**: {mixed_abstraction_assessment}
- **Multiple Responsibilities**: {multiple_responsibilities_assessment}
- **Deep Nesting**: {deep_nesting_assessment}
- **Complex Boolean Logic**: {complex_boolean_assessment}
- **State-Based Complexity**: {state_complexity_assessment}
- **Error Handling Mixed with Logic**: {error_handling_assessment}

## Refactoring Strategy

### Phased Approach

#### Phase 1: {phase_1_name} (Priority: {phase_1_priority})
- **Target Complexity Reduction**: {phase_1_reduction}
- **Estimated Effort**: {phase_1_effort}
- **Risk Level**: {phase_1_risk}
- **Techniques**: {phase_1_techniques}

#### Phase 2: {phase_2_name} (Priority: {phase_2_priority})
- **Target Complexity Reduction**: {phase_2_reduction}
- **Estimated Effort**: {phase_2_effort}
- **Risk Level**: {phase_2_risk}
- **Techniques**: {phase_2_techniques}

[Repeat for each phase]

### Refactoring Techniques Selected

#### Technique 1: {technique_1_name}
- **Application**: {technique_1_application}
- **Expected Impact**: {technique_1_impact}
- **Implementation Steps**:
  1. {technique_1_step_1}
  2. {technique_1_step_2}
  3. {technique_1_step_3}

#### Technique 2: {technique_2_name}
- **Application**: {technique_2_application}
- **Expected Impact**: {technique_2_impact}
- **Implementation Steps**:
  1. {technique_2_step_1}
  2. {technique_2_step_2}
  3. {technique_2_step_3}

[Repeat for each technique]

## Refactored Implementation

### Original Code
```{language}
{original_code}
```

**Complexity**: {original_complexity}

### Refactored Code
```{language}
{refactored_code}
```

**Complexity**: {refactored_complexity}

### Supporting Classes/Methods Created

#### New Class: {new_class_1_name}
```{language}
{new_class_1_code}
```

**Purpose**: {new_class_1_purpose}  
**Complexity**: {new_class_1_complexity}

#### New Method: {new_method_1_name}
```{language}
{new_method_1_code}
```

**Purpose**: {new_method_1_purpose}  
**Complexity**: {new_method_1_complexity}

[Repeat for each new class/method]

## Verification and Measurement

### Test Execution Results
- **Tests Run**: {tests_run}
- **Tests Passed**: {tests_passed}
- **Tests Failed**: {tests_failed}
- **New Tests Added**: {new_tests_added}

### Failed Tests (if any)
```
{failed_test_output}
```

**Resolution**: {failed_test_resolution}

### Complexity Metrics Comparison

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Cyclomatic Complexity | {before_complexity} | {after_complexity} | {complexity_improvement} |
| Lines of Code | {before_lines} | {after_lines} | {lines_change} |
| Nesting Depth | {before_nesting} | {after_nesting} | {nesting_improvement} |
| Method Count | {before_methods} | {after_methods} | {methods_change} |
| Parameter Count | {before_params} | {after_params} | {params_change} |

### Behavior Preservation Validation
- ✅ **Functional Equivalence**: {functional_equivalence_status}
- ✅ **Performance Impact**: {performance_impact}
- ✅ **Interface Compatibility**: {interface_compatibility}
- ✅ **Error Handling**: {error_handling_status}

### Readability Assessment
- **Before**: {readability_before}/10
- **After**: {readability_after}/10
- **Improvement**: {readability_improvement}

**Justification**: {readability_justification}

### Testability Assessment
- **Before**: {testability_before}/10
- **After**: {testability_after}/10
- **Improvement**: {testability_improvement}

**Justification**: {testability_justification}

## Updated Test Cases

### Modified Tests
```{language}
{modified_test_code}
```

**Changes Made**: {test_changes_description}

### New Tests Added
```{language}
{new_test_code}
```

**Purpose**: {new_test_purpose}

## Summary

### Achievements
- ✅ Complexity reduced from {before_complexity} to {after_complexity} ({complexity_reduction_percentage}% reduction)
- ✅ Target complexity of {target_complexity} {target_achievement_status}
- ✅ All {tests_passed} tests passing
- ✅ Readability improved by {readability_improvement} points
- ✅ Testability improved by {testability_improvement} points

### Constraints Respected
- ✅ Interface compatibility maintained: {interface_status}
- ✅ Performance requirements met: {performance_status}
- ✅ Backward compatibility preserved: {compatibility_status}

### Recommendations for Future Work
1. {future_recommendation_1}
2. {future_recommendation_2}
3. {future_recommendation_3}

### Monitoring Suggestions
- Monitor {monitoring_metric_1} for {monitoring_reason_1}
- Track {monitoring_metric_2} for {monitoring_reason_2}
- Review {monitoring_metric_3} for {monitoring_reason_3}

---

## Placeholder Guide

- `{target_identifier}`: Name of the method/function/class being refactored
- `{file_path}`: Full path to the file containing the target code
- `{programming_language}`: Language of the code (Java, Python, JavaScript, etc.)
- `{analysis_timestamp}`: Timestamp in YYYYMMDD-HHmm format
- `{current_complexity}`: Current cyclomatic complexity score
- `{target_complexity}`: Desired complexity score (typically <10)
- `{reduction_needed}`: Difference between current and target
- `{risk_level}`: Assessment of refactoring risk (Low/Medium/High)
- `{*_count}`: Count of each decision point type
- `{*_contribution}`: Complexity points contributed by each type
- `{control_flow_diagram}`: Visual representation of control flow (text-based or Mermaid)
- `{section_*_lines}`: Line numbers of complex sections
- `{section_*_complexity}`: Complexity score of each section
- `{section_*_description}`: Description of what the section does
- `{total_tests}`, `{code_coverage}`, `{branch_coverage}`: Test metrics
- `{untested_paths}`: Number of code paths without test coverage
- `{test_example}`: Example of existing test code
- `{test_quality_assessment}`: Evaluation of test quality
- `{coverage_gap_*}`: Identified gaps in test coverage
- `{pattern_*_name}`: Name of complexity pattern (e.g., "Deep Nesting", "Complex Boolean Logic")
- `{pattern_*_lines}`: Line numbers where pattern occurs
- `{pattern_*_complexity}`: Complexity contribution of the pattern
- `{pattern_*_description}`: Description of the pattern
- `{pattern_*_root_cause}`: Why this pattern exists
- `{*_assessment}`: Assessment of various complexity sources
- `{phase_*_name}`: Name of refactoring phase
- `{phase_*_priority}`: Priority level (High/Medium/Low)
- `{phase_*_reduction}`: Expected complexity reduction
- `{phase_*_effort}`: Estimated effort (hours/days)
- `{phase_*_risk}`: Risk level of the phase
- `{phase_*_techniques}`: Refactoring techniques to use
- `{technique_*_name}`: Name of refactoring technique (e.g., "Extract Method", "Replace Conditional with Polymorphism")
- `{technique_*_application}`: Where/how to apply the technique
- `{technique_*_impact}`: Expected impact on complexity
- `{technique_*_step_*}`: Implementation steps for the technique
- `{original_code}`, `{refactored_code}`: Before and after code
- `{original_complexity}`, `{refactored_complexity}`: Complexity scores
- `{new_class_*_name}`, `{new_method_*_name}`: Names of new classes/methods created
- `{new_class_*_code}`, `{new_method_*_code}`: Code for new classes/methods
- `{new_class_*_purpose}`, `{new_method_*_purpose}`: Purpose of new classes/methods
- `{new_class_*_complexity}`, `{new_method_*_complexity}`: Complexity of new classes/methods
- `{tests_run}`, `{tests_passed}`, `{tests_failed}`, `{new_tests_added}`: Test execution results
- `{failed_test_output}`: Output from failed tests
- `{failed_test_resolution}`: How failed tests were resolved
- `{before_*}`, `{after_*}`: Metric values before and after refactoring
- `{*_improvement}`, `{*_change}`: Changes in metrics
- `{functional_equivalence_status}`: Confirmation that behavior is preserved
- `{performance_impact}`: Description of performance changes
- `{interface_compatibility}`: Status of interface compatibility
- `{error_handling_status}`: Status of error handling preservation
- `{readability_before}`, `{readability_after}`: Readability scores out of 10
- `{readability_improvement}`: Change in readability
- `{readability_justification}`: Explanation of readability assessment
- `{testability_before}`, `{testability_after}`: Testability scores out of 10
- `{testability_improvement}`: Change in testability
- `{testability_justification}`: Explanation of testability assessment
- `{modified_test_code}`: Code for modified tests
- `{test_changes_description}`: Description of test changes
- `{new_test_code}`: Code for new tests
- `{new_test_purpose}`: Purpose of new tests
- `{complexity_reduction_percentage}`: Percentage reduction in complexity
- `{target_achievement_status}`: Whether target was achieved (Achieved/Exceeded/Not Achieved)
- `{interface_status}`, `{performance_status}`, `{compatibility_status}`: Status of constraints
- `{future_recommendation_*}`: Recommendations for future improvements
- `{monitoring_metric_*}`: Metrics to monitor
- `{monitoring_reason_*}`: Why to monitor each metric

## Example

```markdown
# Cyclomatic Complexity Reduction Report

## Target Information
- **Target Code**: UserService.processOrder()
- **File Location**: src/services/UserService.java
- **Programming Language**: Java
- **Analysis Date**: 20251027-1430

## Current Complexity Assessment

### Complexity Metrics
- **Current Cyclomatic Complexity**: 18
- **Target Complexity**: 8
- **Reduction Required**: 10
- **Risk Level**: Medium

### Decision Points Identified
| Type | Count | Contribution |
|------|-------|--------------|
| If/Else Statements | 8 | 8 |
| Switch/Case Statements | 1 | 3 |
| Loops (for/while/do) | 2 | 2 |
| Logical Operators (&&/\|\|) | 5 | 5 |
| Try/Catch Blocks | 0 | 0 |
| **Total** | **16** | **18** |

### Control Flow Visualization
```
processOrder()
├── if (order == null) → return error
├── if (user == null) → return error
├── if (!validateOrder(order))
│   ├── if (order.items.isEmpty()) → return error
│   └── if (order.total < 0) → return error
├── switch (order.type)
│   ├── case STANDARD → processStandard()
│   ├── case EXPRESS → processExpress()
│   └── case BULK → processBulk()
├── for (item in order.items)
│   ├── if (item.quantity > stock) → return error
│   └── if (item.price != catalog.price) → update price
└── if (payment.process() && inventory.reserve())
    └── return success
```

### Most Complex Sections
1. **Lines 45-65**: Complexity 8 - Order validation with nested conditions
2. **Lines 70-85**: Complexity 5 - Item processing loop with conditionals
3. **Lines 90-100**: Complexity 3 - Payment and inventory coordination

[Rest of report...]
```

## Notes

- Always preserve existing functionality - no behavioral changes
- Make incremental changes with test validation at each step
- Focus on single responsibility principle when extracting methods
- Keep methods/functions short and focused (ideally <20 lines)
- Improve naming to clarify intent and purpose
- Apply consistent coding standards for the target language
- Ensure adequate test coverage before and after refactoring
- Document complex algorithms that cannot be simplified further
- Ensure team familiarity with introduced design patterns
