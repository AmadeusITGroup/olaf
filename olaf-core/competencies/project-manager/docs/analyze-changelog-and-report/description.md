# Analyze Changelog and Report

## Overview

Analyzes changelog entries over a specified time period, cross-references with project artifacts, identifies discrepancies, and generates comprehensive summary reports with statistics and insights.

## Purpose

Project managers need to understand what happened during a time period, identify patterns, and ensure documentation consistency. This competency solves the problem of manual changelog review by automatically analyzing entries, categorizing changes, detecting inconsistencies between changelog and actual project files, and producing actionable reports that provide visibility into project progress and documentation quality.

## Usage

**Command**: `analyze changelog and report`

**Protocol**: Act

**When to Use**: Use this competency for sprint retrospectives, monthly progress reviews, release preparation, audit requirements, or whenever you need to understand project activity patterns, verify documentation completeness, or generate executive summaries of work completed during a specific timeframe.

## Parameters

### Required Inputs
- **start_date**: Beginning date for analysis in YYYYMMDD format (e.g., 20251001 for October 1, 2025)

### Optional Inputs
- **prompt_dir**: Directory path containing prompt files to cross-reference against changelog entries (defaults to standard prompts directory if not provided)

### Context Requirements
- Access to changelog register file (`[id:changelog_register]`)
- Access to prompt files directory for cross-referencing
- Access to findings directory for saving generated reports
- Changelog template for report formatting

## Output

**Deliverables**:
- Comprehensive analysis report saved to `[id:findings_dir]ChangelogSummaries/YYYYMMDD-HHMMSS-summary.md`
- Summary statistics (total entries, breakdown by type, activity patterns)
- Detailed listing of all changes with categorization
- Discrepancy report identifying mismatches between changelog and project files
- Resolution documentation for any issues found
- Recommendations for improving documentation practices

**Format**: Interactive markdown document with collapsible sections, summary tables, detailed change listings, and actionable insights.

## Examples

### Example 1: Sprint Retrospective Analysis

**Scenario**: Analyzing the past two weeks of work for sprint retrospective meeting

**Command**:
```
analyze changelog and report
```

**Input**:
```
Start Date: 20251013
```

**Result**: Generated report showing 47 changelog entries: 12 features, 8 fixes, 15 chores, 7 documentation updates, 5 reviews. Identified 3 prompt files mentioned in changelog but not found in repository. Report saved for retrospective discussion.

### Example 2: Monthly Progress Report

**Scenario**: Creating monthly status report for stakeholders

**Command**:
```
analyze changelog and report
```

**Input**:
```
Start Date: 20251001
Prompt Dir: olaf-core/competencies/*/prompts
```

**Result**: Comprehensive report covering entire October with categorized changes, contributor statistics, and verification that all documented prompt changes exist in the codebase.

### Example 3: Release Preparation Audit

**Scenario**: Verifying all changes are documented before release

**Command**:
```
analyze changelog and report
```

**Input**:
```
Start Date: 20250915
```

**Result**: Analysis revealed 2 prompt files modified in git but not mentioned in changelog, flagged for review before release.

## Related Competencies

- **create-changelog-entry**: Creates the entries that this competency analyzes
- **archive-changelog-entries**: Use after analysis to clean up old entries
- **generate-professional-release-notes**: Uses similar analysis but focuses on user-facing release documentation
- **review-progress**: Broader progress review that may incorporate changelog analysis findings
- **prepare-conversation-handover**: Analysis reports can be included in handover documentation

## Tips & Best Practices

- Run analysis regularly (weekly or bi-weekly) to catch discrepancies early while context is fresh
- Use consistent start dates aligned with sprint or iteration boundaries for comparable reports
- Review discrepancies interactively during analysis rather than deferring - immediate resolution is more accurate
- Save generated reports with descriptive names for easy reference in future retrospectives
- Compare reports across time periods to identify trends in activity types and documentation quality
- Use findings to improve team practices around changelog discipline and documentation standards

## Limitations

- Only analyzes entries from the specified start date forward - cannot analyze specific date ranges with end dates
- Cross-referencing is limited to prompt files - does not verify other artifact types mentioned in changelog
- Cannot automatically resolve discrepancies - requires human judgment for each issue
- Analysis quality depends on changelog entry quality - vague or incomplete entries produce less useful insights
- Does not integrate with version control systems to automatically detect undocumented changes

**Source**: `olaf-core/competencies/project-manager/prompts/analyze-changelog-and-report.md`
