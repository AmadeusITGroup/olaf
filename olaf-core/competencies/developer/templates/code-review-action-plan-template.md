# Curative Action Plan

**Purpose**: Provide actionable steps to address code review findings with specific instructions for humans and LLMs  
**Used By**: review-code, review-github-pr prompts  
**Version**: 1.0  
**Last Updated**: 2025-10-27

---

## Template Structure

# Curative Action Plan: {filename}

**Generated:** {timestamp}  
**Review Source:** {review_source_file}

## Priority Matrix

| Issue | Severity | Difficulty | Effort | Order |
|-------|----------|------------|--------|-------|
| {issue_1} | {severity_1} | {difficulty_1} | {effort_1} | {order_1} |
| {issue_2} | {severity_2} | {difficulty_2} | {effort_2} | {order_2} |
| {issue_3} | {severity_3} | {difficulty_3} | {effort_3} | {order_3} |

## Actionable Steps

### Step {N}: {issue_name} - {priority_level}

**File:** `{file_path}`  
**Lines:** {line_range}  
**Type:** {action_type}

#### Human Instructions:
1. {human_instruction_1}
2. {human_instruction_2}
3. {human_instruction_3}

#### LLM Prompt:
```
{llm_prompt_text}
```

#### Code Example:

**Before:**
```{language}
{before_code}
```

**After:**
```{language}
{after_code}
```

#### Validation:
{validation_criteria}

---

[Repeat Step section for each issue]

---

## Implementation Order

### Phase 1: Critical Issues (Immediate)
1. Step {step_number}: {issue_name} - {reason_for_priority}
2. Step {step_number}: {issue_name} - {reason_for_priority}

### Phase 2: High Priority (This Sprint)
1. Step {step_number}: {issue_name} - {reason_for_priority}
2. Step {step_number}: {issue_name} - {reason_for_priority}

### Phase 3: Medium Priority (Next Sprint)
1. Step {step_number}: {issue_name} - {reason_for_priority}
2. Step {step_number}: {issue_name} - {reason_for_priority}

### Phase 4: Low Priority (Future)
1. Step {step_number}: {issue_name} - {reason_for_priority}
2. Step {step_number}: {issue_name} - {reason_for_priority}

## Dependencies

### Step Dependencies
- Step {N} depends on Step {M}: {dependency_reason}
- Step {X} depends on Step {Y}: {dependency_reason}

### External Dependencies
- {external_dependency_1}: {description}
- {external_dependency_2}: {description}

## Effort Summary

| Priority | Total Steps | Estimated Effort | Expected Completion |
|----------|-------------|------------------|---------------------|
| Critical | {critical_count} | {critical_effort} | {critical_timeline} |
| High | {high_count} | {high_effort} | {high_timeline} |
| Medium | {medium_count} | {medium_effort} | {medium_timeline} |
| Low | {low_count} | {low_effort} | {low_timeline} |
| **Total** | **{total_count}** | **{total_effort}** | **{total_timeline}** |

## Success Criteria

- [ ] All critical issues resolved
- [ ] All high priority issues addressed
- [ ] Code review findings implemented
- [ ] All tests passing
- [ ] Code quality metrics improved
- [ ] Documentation updated

## Notes

{additional_notes}

---

## Placeholder Guide

- `{filename}`: Name of the file being addressed
- `{timestamp}`: Generation timestamp in YYYYMMDD-HHmm format
- `{review_source_file}`: Path to the original code review document
- `{issue_*}`: Brief description of the issue
- `{severity_*}`: Severity level (Critical/High/Medium/Low)
- `{difficulty_*}`: Implementation difficulty (Easy/Medium/Hard)
- `{effort_*}`: Estimated effort (e.g., "2h", "1d", "3d")
- `{order_*}`: Implementation order number
- `{issue_name}`: Descriptive name of the issue
- `{priority_level}`: Priority classification (P0/P1/P2/P3)
- `{file_path}`: Path to the file requiring changes
- `{line_range}`: Line numbers affected (e.g., "350-420")
- `{action_type}`: Type of action (Refactoring/Bug Fix/Enhancement/Security Fix)
- `{human_instruction_*}`: Step-by-step instructions for human developers
- `{llm_prompt_text}`: Complete prompt text for LLM execution
- `{language}`: Programming language for code blocks
- `{before_code}`: Current problematic code
- `{after_code}`: Corrected/improved code
- `{validation_criteria}`: How to verify the fix is successful
- `{step_number}`: Reference to step number
- `{reason_for_priority}`: Explanation of why this priority level
- `{dependency_reason}`: Explanation of dependency relationship
- `{external_dependency_*}`: External factors affecting implementation
- `{*_count}`: Count of steps at each priority level
- `{*_effort}`: Total effort estimate for priority level
- `{*_timeline}`: Expected completion timeline
- `{additional_notes}`: Any additional context or considerations

## Example

```markdown
# Curative Action Plan: UserService.java

**Generated:** 20251027-1430  
**Review Source:** code-review-20251027-1400.md

## Priority Matrix

| Issue | Severity | Difficulty | Effort | Order |
|-------|----------|------------|--------|-------|
| Method too long | High | Medium | 2h | 1 |
| Missing null checks | Critical | Easy | 30m | 2 |
| Hardcoded credentials | Critical | Easy | 15m | 3 |
| Complex boolean logic | Medium | Medium | 1h | 4 |

## Actionable Steps

### Step 1: Extract Long Method - P1

**File:** `src/services/UserService.java`  
**Lines:** 45-120  
**Type:** Refactoring

#### Human Instructions:
1. Extract lines 50-70 into `validateUserInput()` method
2. Extract lines 75-95 into `processUserData()` method
3. Extract lines 100-115 into `saveUserRecord()` method
4. Update main method to call extracted methods in sequence

#### LLM Prompt:
```
Refactor the createUser method in src/services/UserService.java by extracting three helper methods:
1. validateUserInput (lines 50-70) - handles input validation
2. processUserData (lines 75-95) - transforms and enriches user data
3. saveUserRecord (lines 100-115) - persists to database

Maintain all existing functionality and error handling. Ensure proper exception propagation.
```

#### Code Example:

**Before:**
```java
public User createUser(UserRequest request) {
    // 75 lines of mixed validation, processing, and persistence
    if (request == null) throw new IllegalArgumentException();
    if (request.getEmail() == null) throw new IllegalArgumentException();
    // ... 70 more lines
}
```

**After:**
```java
public User createUser(UserRequest request) {
    validateUserInput(request);
    UserData data = processUserData(request);
    return saveUserRecord(data);
}

private void validateUserInput(UserRequest request) {
    // Validation logic extracted
}

private UserData processUserData(UserRequest request) {
    // Processing logic extracted
}

private User saveUserRecord(UserData data) {
    // Persistence logic extracted
}
```

#### Validation:
- Method length reduced to <15 lines
- All existing tests pass
- Functionality preserved
- Code readability improved

---

### Step 2: Add Null Checks - P0

**File:** `src/services/UserService.java`  
**Lines:** 45, 67, 89  
**Type:** Bug Fix

#### Human Instructions:
1. Add null check for request parameter at line 45
2. Add null check for email field at line 67
3. Add null check for database connection at line 89

#### LLM Prompt:
```
Add defensive null checks to the createUser method in src/services/UserService.java:
- Line 45: Check if request parameter is null before processing
- Line 67: Check if email field is null before validation
- Line 89: Check if database connection is null before save operation

Throw IllegalArgumentException with descriptive messages for null parameters.
```

#### Code Example:

**Before:**
```java
public User createUser(UserRequest request) {
    String email = request.getEmail(); // NPE risk
    // ...
}
```

**After:**
```java
public User createUser(UserRequest request) {
    if (request == null) {
        throw new IllegalArgumentException("User request cannot be null");
    }
    String email = request.getEmail();
    if (email == null) {
        throw new IllegalArgumentException("Email cannot be null");
    }
    // ...
}
```

#### Validation:
- No NullPointerExceptions thrown
- Appropriate error messages provided
- All tests pass including new null-case tests

[Additional steps...]

## Implementation Order

### Phase 1: Critical Issues (Immediate)
1. Step 3: Remove hardcoded credentials - Security vulnerability must be fixed immediately
2. Step 2: Add null checks - Prevents runtime crashes

### Phase 2: High Priority (This Sprint)
1. Step 1: Extract long method - Improves maintainability significantly

### Phase 3: Medium Priority (Next Sprint)
1. Step 4: Simplify boolean logic - Enhances readability

## Dependencies

### Step Dependencies
- Step 1 should be completed before Step 4: Extracted methods make boolean logic refactoring easier

### External Dependencies
- Step 3 requires configuration management system setup

## Effort Summary

| Priority | Total Steps | Estimated Effort | Expected Completion |
|----------|-------------|------------------|---------------------|
| Critical | 2 | 45m | Today |
| High | 1 | 2h | This week |
| Medium | 1 | 1h | Next week |
| **Total** | **4** | **3h 45m** | **1 week** |

## Success Criteria

- [ ] All critical issues resolved
- [ ] All high priority issues addressed
- [ ] Code review findings implemented
- [ ] All tests passing
- [ ] Code quality metrics improved
- [ ] Documentation updated

## Notes

Consider adding integration tests after Step 1 refactoring to ensure extracted methods work correctly together.
```

## Notes

- Provide specific line numbers and file paths for all changes
- Include both human-readable instructions and LLM-executable prompts
- Show concrete before/after code examples for clarity
- Define clear validation criteria for each fix
- Consider dependencies between fixes when ordering
- Estimate effort realistically based on complexity
- Prioritize by impact and urgency, not just severity
