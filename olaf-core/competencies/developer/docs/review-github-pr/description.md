# Review GitHub PR

## Overview

This competency performs comprehensive pull request reviews with user-guided file selection, integration analysis, and automated action plan generation, focusing on code quality, security, and system integration impact.

## Purpose

Pull requests require thorough review to ensure code quality, prevent bugs, and maintain system integrity. This competency provides structured PR reviews that analyze not just individual changes but also integration impacts, cross-file dependencies, and overall system health, with actionable recommendations for improvement.

## Usage

**Command**: `review github pr` (or aliases: `review pr`, `pull request review`, `check pr`, `github pr`)

**Protocol**: Propose-Act

**When to Use**: Use for reviewing pull requests before merging, assessing integration risks, validating that changes meet requirements, ensuring code quality standards, and identifying potential issues that span multiple files.

## Parameters

### Required Inputs
- **pr_url**: GitHub pull request URL or PR number
- **repository**: Repository name if not in URL

### Optional Inputs
- **focus_areas**: Specific aspects to emphasize (security, performance, integration)
- **review_standards**: Coding standards to apply
- **integration_scope**: How deeply to analyze cross-file impacts
- **file_selection**: Specific files to focus on (user-guided)

### Context Requirements
- Access to GitHub repository
- Understanding of codebase architecture
- Knowledge of coding standards and team conventions
- Context about the feature or fix being implemented

## Output

Generates comprehensive PR review with integration analysis and action plan.

**Deliverables**:
- PR overview with change summary
- File-by-file review findings
- Integration impact analysis
- Cross-file dependency assessment
- Security and quality concerns
- Automated action plan with prioritized fixes
- Merge recommendation (approve, request changes, reject)
- Code review report: `pr-review-{pr-number}-YYYYMMDD-HHmm.md`
- Action plan: `pr-action-plan-{pr-number}-YYYYMMDD-HHmm.md`

**Format**: Structured markdown following code-review-action-plan template

## Examples

### Example 1: Feature PR Review

**Scenario**: New authentication feature needs review before merge

**Command**:
```
review github pr
```

**Input**:
```
pr_url: https://github.com/org/repo/pull/123
focus_areas: ["security", "integration"]
```

**Result**: Reviewed 8 files, identified security issue with token storage, found integration risk with existing session management, generated action plan with 5 prioritized fixes, recommended "Request Changes" with specific improvements.

### Example 2: Bug Fix PR Review

**Scenario**: Critical bug fix needs quick but thorough review

**Command**:
```
review pr
```

**Input**:
```
pr_url: https://github.com/org/repo/pull/456
focus_areas: ["correctness", "testing"]
file_selection: [changed files only]
```

**Result**: Verified fix addresses root cause, identified missing edge case handling, recommended additional test cases, generated action plan with test improvements, approved with minor suggestions.

### Example 3: Refactoring PR Review

**Scenario**: Large refactoring PR needs integration analysis

**Command**:
```
check pr
```

**Input**:
```
pr_url: https://github.com/org/repo/pull/789
focus_areas: ["integration", "breaking-changes"]
integration_scope: deep
```

**Result**: Analyzed 23 files, mapped all integration points, identified 3 breaking changes, found 2 files with incomplete refactoring, generated comprehensive action plan with migration steps, recommended "Request Changes" with detailed integration fixes.

## Related Competencies

- **review-code**: General code review that can be used for individual files in PR
- **analyze-function-complexity**: Deep-dive into complex functions changed in PR
- **fix-code-smells**: Implements improvements identified during PR review
- **create-unit-tests**: Adds tests for PR changes lacking coverage

## Tips & Best Practices

- Review PR description and linked issues first for context
- Use user-guided file selection to focus on critical changes
- Pay special attention to integration points and dependencies
- Check for breaking changes and backward compatibility
- Verify test coverage for new functionality
- Look for security implications of changes
- Consider performance impact of modifications
- Review action plan and prioritize critical fixes
- Provide constructive feedback with specific examples
- Acknowledge good practices and clean code

## Limitations

- Cannot execute code or run tests
- May miss runtime behavior issues
- Cannot validate business logic correctness without domain knowledge
- Integration analysis limited to static code analysis
- Cannot detect all security vulnerabilities
- Effectiveness depends on PR description quality
- May not catch issues requiring system-wide context
- Cannot assess user experience or UI/UX changes
- Limited to code changes, doesn't review documentation or configuration
