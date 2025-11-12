# Check TODOs In Code

**Source**: olaf-core/competencies/developer/prompts/check-todos-in-code.md

## Overview

Search and analyze TODO comments in codebase, assess validity, and generate complete code solutions with user decision tracking. Provides actionable resolution plan with actual replacement code.

## Purpose

TODO comments accumulate in codebases over time, representing technical debt and deferred work. This competency systematically identifies, analyzes, and provides concrete solutions for TODOs, helping teams prioritize and resolve technical debt efficiently. Unlike simple TODO scanners, it provides actual code solutions and implementation guidance.

## Usage

**Command**: `check todos`

**Protocol**: Propose-Act

**When to Use**:
- Before release to identify and resolve pending work
- During technical debt cleanup initiatives
- When onboarding to understand deferred work
- For sprint planning to estimate TODO resolution effort
- To track and prioritize technical debt systematically

## Parameters

### Required Inputs
- **target_path**: Path to folder or repository to scan
- **repository_name**: Name of the repository being analyzed

### Optional Inputs
- **file_extensions**: File extensions to include (defaults to common code files)
- **todo_patterns**: TODO patterns to search for (defaults to TODO, FIXME, HACK, XXX, BUG)
- **save_document**: Save resolution document (default: true)
- **max_todos_threshold**: Maximum TODOs to analyze in one session (default: 50)

### Context Requirements
- Access to codebase source files
- Ability to read and analyze code context around TODOs
- Optional: version control history for author information

## Output

Comprehensive TODO analysis with concrete solutions and implementation guidance.

**Deliverables**:
- TODO inventory organized by repository → folder → file hierarchy
- Priority classification for each TODO (Critical, High, Medium, Low)
- Actual replacement code solutions (not just recommendations)
- Specific line ranges to replace
- Implementation and testing instructions
- Effort estimates and dependency identification

**Format**: Markdown document following todo-resolution-template.md structure

## Examples

### Example 1: Full Repository Scan

**Scenario**: Preparing for release, need to identify all pending TODOs

**Command**:
```
check todos
```

**Input**:
- target_path: "./src"
- repository_name: "payment-service"

**Result**: Found 23 TODOs, analyzed and prioritized with 5 critical items requiring immediate attention, complete with replacement code for each

### Example 2: Focused Scan with Subset

**Scenario**: Large codebase with 150 TODOs, focusing on critical items

**Command**:
```
check todos
```

**Input**:
- target_path: "./src"
- repository_name: "user-service"
- todo_patterns: ["FIXME", "BUG"]

**Result**: Identified 12 critical TODOs (FIXME/BUG patterns), provided solutions for immediate resolution

## Related Competencies

- **review-code**: Use for comprehensive code review after TODO resolution
- **fix-code-smells**: Apply to address code quality issues found in TODOs
- **augment-code-unit-test**: Create tests for TODO resolutions
- **evolve-code-iteratively**: Use for complex TODO resolutions requiring iteration

## Tips & Best Practices

- Start with FIXME and BUG patterns for highest priority items
- Use subset selection for large codebases (>50 TODOs)
- Review TODO context carefully before applying solutions
- Test each TODO resolution independently
- Track resolved TODOs to measure technical debt reduction
- Run periodically to prevent TODO accumulation

## Limitations

- Solutions require manual review and testing before application
- May not capture all context for complex TODOs
- Author information depends on comment format
- Large codebases may require multiple sessions
- Some TODOs may require architectural changes beyond code replacement
