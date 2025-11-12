# Report My Daily

## Overview

Generates a daily work report by analyzing git activity, file changes, PRs, and project artifacts.

## Purpose

Automates the creation of daily status reports by analyzing your actual work output, saving time and ensuring accurate reporting of accomplishments, progress, and blockers.

## Usage

**Command**: `report my daily`

**Protocol**: Propose-Act

**When to Use**: At end of day for status updates, standups, or personal work tracking.

## Parameters

### Required Inputs
None - analyzes today's work by default

### Optional Inputs
- **Date Range**: Specify different date or range (yesterday, this week, etc.)
- **Branch**: Specific branch to analyze
- **Format**: Desired output format (bullets, narrative, etc.)

### Context Requirements
- Git repository with commit history
- Work done during the specified period

## Output

**Deliverables**:
- Summary of accomplishments
- List of commits with descriptions
- Files modified by category
- Features completed or in progress
- Blockers or issues
- Next steps

**Format**: Structured markdown report, customizable

## Examples

### Example 1: End of Day Report

**Scenario**: Need to report on today's work for standup

**Command**:
```
report my daily
```

**Result**: Report showing commits, features worked on, files modified, and progress made

### Example 2: Weekly Summary

**Scenario**: Need weekly status for team meeting

**Command**:
```
report my work this week
```

**Result**: Comprehensive weekly summary with major accomplishments and metrics

### Example 3: Specific Feature Report

**Scenario**: Report on work for specific feature branch

**Command**:
```
report my daily on feature/user-authentication branch
```

**Result**: Focused report on authentication feature work

## Related Competencies

- **create-carry-over**: Create session notes after reviewing daily report
- **carry-on-work**: Resume work based on report's next steps
- **stash-work**: Stash current work before switching based on report insights

## Tips & Best Practices

- Run at end of day for most accurate reporting
- Use for daily standups to save preparation time
- Customize format for different audiences (team vs management)
- Review report before sharing to add context if needed
- Combine with carry-over notes for continuity

## Limitations

- Requires git commits to analyze
- Cannot capture work not committed to git
- Quality depends on commit message quality
- May miss context not evident in code changes
