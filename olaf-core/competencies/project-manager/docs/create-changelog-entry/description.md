# Create Changelog Entry

## Overview

Adds structured entries to the project changelog with proper formatting, timestamps, and categorization to maintain a comprehensive record of all project changes and activities.

## Purpose

Projects need a centralized, chronological record of all changes, features, fixes, and activities. This competency solves the problem of scattered or inconsistent change tracking by providing a standardized way to log project modifications in a single, well-organized changelog that serves as the project's historical record and communication tool.

## Usage

**Command**: `create changelog entry`

**Protocol**: Propose-Act

**When to Use**: Use this competency whenever any significant project activity occurs, including new features, bug fixes, code refactoring, documentation updates, analysis reports, releases, reviews, or any other change that should be tracked in the project's history.

## Parameters

### Required Inputs
- **change_type**: Category of change being logged (Feature, Fix, Chore, Documentation, Report, Analysis, Release, Review, or Refactor)
- **description**: Clear, concise description of what changed or what was accomplished

### Optional Inputs
- **links**: References to related resources such as job IDs, commit hashes, pull request numbers, or issue numbers (format: `job-123, PR#45, abc1234`)

### Context Requirements
- Access to changelog register file (`[id:changelog_register]`)
- Access to changelog template for format reference
- System time access via terminal commands for accurate timestamping

## Output

**Deliverables**:
- New entry added to the changelog register
- Entry includes timestamp, type, description, and any provided links
- Changelog maintains proper chronological order (reverse chronological within each day)

**Format**: Markdown-formatted entry following the pattern: `- Type: Description [Links: references]` with proper date section hierarchy (Year > Month > Day).

## Examples

### Example 1: Feature Addition

**Scenario**: Completed implementation of user authentication feature

**Command**:
```
create changelog entry
```

**Input**:
```
Change Type: Feature
Description: Implemented OAuth2 authentication with Google and GitHub providers
Links: job-042, PR#156, commit-a3f9d21
```

**Result**: Added entry under today's date section: `- Feature: Implemented OAuth2 authentication with Google and GitHub providers [Links: job-042, PR#156, commit-a3f9d21]`

### Example 2: Bug Fix

**Scenario**: Fixed critical production issue

**Command**:
```
create changelog entry
```

**Input**:
```
Change Type: Fix
Description: Resolved memory leak in background job processor causing server crashes
Links: issue-789, PR#158
```

**Result**: Entry logged with current timestamp showing the fix and related references

### Example 3: Documentation Update

**Scenario**: Updated API documentation after endpoint changes

**Command**:
```
create changelog entry
```

**Input**:
```
Change Type: Documentation
Description: Updated REST API documentation to reflect new pagination parameters
```

**Result**: Documentation change recorded in changelog without links (none provided)

## Related Competencies

- **create-decision-record**: Decision records should be logged in the changelog after creation
- **analyze-changelog-and-report**: Analyzes changelog entries to generate progress reports
- **archive-changelog-entries**: Moves completed changelog entries to archive for cleanup
- **generate-professional-release-notes**: Uses changelog entries as source material for release notes
- **create-job**: Job creation and completion should be logged in the changelog

## Tips & Best Practices

- Log changes as they happen rather than batching them - real-time logging ensures nothing is forgotten
- Use consistent, descriptive language in descriptions - future readers should understand what happened without additional context
- Always include relevant links (job IDs, PRs, commits) for traceability
- Choose the most specific change type available - this helps with later analysis and reporting
- Keep descriptions concise but informative - one clear sentence is usually sufficient
- Create date sections as needed - the system will maintain proper hierarchy automatically

## Limitations

- Uses system time from terminal commands - cannot create entries with custom timestamps
- Does not automatically detect changes - requires manual invocation to log activities
- Cannot modify existing entries (except within the current day's section) - changelog is append-only for historical integrity
- Does not validate that linked resources (jobs, PRs, commits) actually exist
- Requires manual categorization - does not automatically determine change type from content

**Source**: `olaf-core/competencies/project-manager/prompts/create-changelog-entry.md`
