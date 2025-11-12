# Code Evolution Report

**Purpose**: Document iterative code improvement process with metrics and decision tracking  
**Used By**: evolve-code-iteratively prompt  
**Version**: 1.0  
**Last Updated**: 2025-10-27

---

## Template Structure

## Project Information
- **Code Module**: {module_name}
- **Evolution Start**: {start_timestamp}
- **Evolution Complete**: {end_timestamp}
- **Primary Goals**: {goals_list}
- **Total Iterations**: {iteration_count}

## Initial Assessment

### Baseline Metrics
- **Lines of Code**: {initial_lines}
- **Function Count**: {initial_functions}
- **Cyclomatic Complexity**: {initial_complexity}
- **Maintainability Index**: {initial_maintainability}
- **Test Coverage**: {initial_coverage}%

### Identified Issues
1. {issue_1}
2. {issue_2}
3. {issue_3}

### Optimization Opportunities
- {opportunity_1}
- {opportunity_2}
- {opportunity_3}

## Iteration Reports

### Iteration {N}: {iteration_title}

**Date**: {iteration_timestamp}  
**Focus**: {iteration_focus}  
**Approach**: {iteration_approach}

#### Changes Made
```{language}
// BEFORE
{before_code}

// AFTER
{after_code}
```

#### Impact Analysis
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Lines of Code | {before_lines} | {after_lines} | {lines_delta} |
| Complexity | {before_complexity} | {after_complexity} | {complexity_delta} |
| Maintainability | {before_maintainability} | {after_maintainability} | {maintainability_delta} |

#### Validation Results
- ✅ All tests passed: {test_pass_count}/{test_total_count}
- ✅ Functionality preserved: {functionality_status}
- ✅ Performance impact: {performance_impact}

#### Decision Rationale
{decision_explanation}

---

[Repeat Iteration section for each iteration]

---

## Final Results

### Metrics Comparison
| Metric | Initial | Final | Improvement |
|--------|---------|-------|-------------|
| Lines of Code | {initial_lines} | {final_lines} | {lines_improvement} |
| Function Count | {initial_functions} | {final_functions} | {functions_improvement} |
| Cyclomatic Complexity | {initial_complexity} | {final_complexity} | {complexity_improvement} |
| Maintainability Index | {initial_maintainability} | {final_maintainability} | {maintainability_improvement} |
| Test Coverage | {initial_coverage}% | {final_coverage}% | {coverage_improvement} |
| Readability Score | {initial_readability} | {final_readability} | {readability_improvement} |

### Goals Achievement
- **Performance**: {performance_achievement} - {performance_details}
- **Maintainability**: {maintainability_achievement} - {maintainability_details}
- **Testability**: {testability_achievement} - {testability_details}

### Code Quality Improvements
- {quality_improvement_1}
- {quality_improvement_2}
- {quality_improvement_3}

## Before/After Comparison

### Original Code
```{language}
{original_code_full}
```

### Evolved Code
```{language}
{evolved_code_full}
```

### Key Differences
1. **{difference_1_title}**: {difference_1_description}
2. **{difference_2_title}**: {difference_2_description}
3. **{difference_3_title}**: {difference_3_description}

## Decision Log

### Decision 1: {decision_1_title}
- **Iteration**: {decision_1_iteration}
- **Options Considered**: {decision_1_options}
- **Choice Made**: {decision_1_choice}
- **Rationale**: {decision_1_rationale}
- **Trade-offs**: {decision_1_tradeoffs}

### Decision 2: {decision_2_title}
- **Iteration**: {decision_2_iteration}
- **Options Considered**: {decision_2_options}
- **Choice Made**: {decision_2_choice}
- **Rationale**: {decision_2_rationale}
- **Trade-offs**: {decision_2_tradeoffs}

[Repeat for each major decision]

## Rollback Instructions

### Full Rollback
```bash
{full_rollback_commands}
```

### Iteration-Specific Rollback

#### Rollback to Before Iteration {N}
```bash
{iteration_n_rollback_commands}
```

[Repeat for each iteration]

## Recommendations for Future Work

### Immediate Next Steps
1. {next_step_1}
2. {next_step_2}
3. {next_step_3}

### Long-term Improvements
- {longterm_improvement_1}
- {longterm_improvement_2}
- {longterm_improvement_3}

### Monitoring Suggestions
- {monitoring_suggestion_1}
- {monitoring_suggestion_2}

---

## Placeholder Guide

- `{module_name}`: Name of the code module being evolved
- `{start_timestamp}`, `{end_timestamp}`: Evolution start and end times in YYYYMMDD-HHmm format
- `{goals_list}`: Comma-separated list of primary goals (performance, maintainability, testability)
- `{iteration_count}`: Total number of iterations performed
- `{initial_*}`, `{final_*}`: Metric values at start and end of evolution
- `{*_improvement}`: Calculated improvement (delta or percentage)
- `{iteration_timestamp}`: Timestamp for specific iteration
- `{iteration_focus}`: Main focus area for the iteration
- `{iteration_approach}`: Strategy or technique used in the iteration
- `{before_code}`, `{after_code}`: Code snippets showing changes
- `{*_delta}`: Change in metric value (can be positive or negative)
- `{test_pass_count}`, `{test_total_count}`: Test execution results
- `{functionality_status}`: Confirmation that original functionality is preserved
- `{performance_impact}`: Description of performance changes
- `{decision_explanation}`: Rationale for choices made in iteration
- `{*_achievement}`: Status of goal achievement (Achieved/Partially Achieved/Not Achieved)
- `{*_details}`: Detailed explanation of achievement status
- `{original_code_full}`, `{evolved_code_full}`: Complete before/after code
- `{difference_*_title}`, `{difference_*_description}`: Key differences between versions
- `{decision_*_*}`: Decision log details (title, iteration, options, choice, rationale, tradeoffs)
- `{*_rollback_commands}`: Commands to rollback changes
- `{next_step_*}`: Recommended immediate actions
- `{longterm_improvement_*}`: Suggested future enhancements
- `{monitoring_suggestion_*}`: Metrics or areas to monitor

## Example

```markdown
# Code Evolution Report

## Project Information
- **Code Module**: UserAuthenticationService
- **Evolution Start**: 20251027-0900
- **Evolution Complete**: 20251027-1430
- **Primary Goals**: maintainability, testability
- **Total Iterations**: 3

## Initial Assessment

### Baseline Metrics
- **Lines of Code**: 450
- **Function Count**: 12
- **Cyclomatic Complexity**: 28
- **Maintainability Index**: 45
- **Test Coverage**: 35%

### Identified Issues
1. authenticate() method has complexity of 18
2. Multiple responsibilities mixed in single class
3. Hard-coded dependencies make testing difficult

### Optimization Opportunities
- Extract validation logic into separate validator
- Introduce dependency injection for database access
- Split authentication and authorization concerns

## Iteration Reports

### Iteration 1: Extract Validation Logic

**Date**: 20251027-1000  
**Focus**: Reduce complexity by extracting validation  
**Approach**: Extract Method refactoring

#### Changes Made
```java
// BEFORE
public boolean authenticate(String username, String password) {
    if (username == null || username.isEmpty()) return false;
    if (password == null || password.length() < 8) return false;
    // ... more validation and authentication logic
}

// AFTER
public boolean authenticate(String username, String password) {
    if (!validator.isValid(username, password)) return false;
    // ... authentication logic only
}
```

#### Impact Analysis
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Lines of Code | 450 | 420 | -30 |
| Complexity | 28 | 22 | -6 |
| Maintainability | 45 | 52 | +7 |

#### Validation Results
- ✅ All tests passed: 45/45
- ✅ Functionality preserved: Confirmed
- ✅ Performance impact: Negligible (<1ms)

#### Decision Rationale
Extracted validation into UserValidator class to separate concerns and reduce complexity of main authentication method. This makes the code more testable and maintainable.

[Additional iterations...]

## Final Results

### Metrics Comparison
| Metric | Initial | Final | Improvement |
|--------|---------|-------|-------------|
| Lines of Code | 450 | 380 | -70 (-15.6%) |
| Function Count | 12 | 15 | +3 (better separation) |
| Cyclomatic Complexity | 28 | 12 | -16 (-57.1%) |
| Maintainability Index | 45 | 72 | +27 (+60%) |
| Test Coverage | 35% | 85% | +50% |
| Readability Score | 6/10 | 9/10 | +3 |

### Goals Achievement
- **Performance**: Not Applicable - Not a primary goal
- **Maintainability**: Achieved - Complexity reduced by 57%, maintainability index increased by 60%
- **Testability**: Achieved - Test coverage increased from 35% to 85%, dependencies now injectable

[Rest of report...]
```

## Notes

- Document all iterations even if they don't result in code changes
- Include both quantitative metrics and qualitative assessments
- Provide clear rollback instructions for each iteration
- Explain decision rationale to help future maintainers understand choices
- Balance detail with readability - use code snippets judiciously
