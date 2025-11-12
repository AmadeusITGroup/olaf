# Archive Changelog Entries

## Overview

Archives completed changelog entries by moving them from the active changelog to archive storage, maintaining a clean and manageable active log while preserving historical records.

## Purpose

As projects progress, changelogs grow large and unwieldy, making it difficult to focus on recent activity. This competency solves the problem of changelog bloat by systematically moving older, completed entries to archive storage while maintaining full historical traceability and keeping the active changelog focused on current and recent work.

## Usage

**Command**: `archive changelog entries`

**Protocol**: Propose-Act

**When to Use**: Use this competency at the end of sprints, releases, or quarters to clean up the active changelog, when the changelog becomes too large to navigate efficiently, or as part of regular project maintenance to keep documentation organized and focused on current activities.

## Parameters

### Required Inputs
- **archive_date**: Cutoff date for archiving - entries before this date will be moved to archive (format: YYYYMMDD)

### Optional Inputs
- **archive_reason**: Brief description of why archiving is being performed (e.g., "End of Q4 2025", "Release v2.0 cleanup")

### Context Requirements
- Access to active changelog register (`[id:changelog_register]`)
- Access to changelog archive directory for storing archived entries
- Backup capability to preserve original changelog before modifications

## Output

**Deliverables**:
- Archived changelog file containing entries before the cutoff date
- Updated active changelog with only recent entries
- Archive index updated with new archive file reference
- Backup of original changelog before archiving

**Format**: Archived entries maintain their original markdown format and structure in dated archive files (e.g., `changelog-archive-2025Q4.md`).

## Examples

### Example 1: End of Sprint Cleanup

**Scenario**: Completed 2-week sprint and want to archive entries older than 30 days

**Command**:
```
archive changelog entries
```

**Input**:
```
Archive Date: 20250927
Archive Reason: End of Sprint 12 - archiving entries older than 30 days
```

**Result**: Moved 45 entries from September and earlier to `changelog-archive-2025Q3.md`, active changelog now contains only October entries

### Example 2: Release Milestone Archive

**Scenario**: Just released v2.0 and want to archive all pre-release entries

**Command**:
```
archive changelog entries
```

**Input**:
```
Archive Date: 20251015
Archive Reason: v2.0 Release - archiving all development entries
```

**Result**: Created archive file with all entries through October 15, clean changelog ready for v2.1 development cycle

### Example 3: Quarterly Maintenance

**Scenario**: End of quarter routine maintenance to keep changelog manageable

**Command**:
```
archive changelog entries
```

**Input**:
```
Archive Date: 20250930
Archive Reason: Q3 2025 quarterly archive
```

**Result**: Q3 entries archived, Q4 entries remain active, archive index updated with Q3 reference

## Related Competencies

- **create-changelog-entry**: Creates the entries that eventually get archived
- **analyze-changelog-and-report**: Run analysis before archiving to capture insights from entries being archived
- **generate-professional-release-notes**: Generate release notes before archiving release-related entries
- **review-progress**: Progress reviews may inform appropriate archive timing and scope

## Tips & Best Practices

- Archive at regular intervals (monthly, quarterly, or per release) to maintain consistency
- Run analysis reports before archiving to capture insights from entries being moved
- Keep at least 30-60 days of entries in the active changelog for easy reference
- Use meaningful archive file names that indicate the time period or milestone
- Always create backups before archiving - archiving modifies the active changelog
- Document archive reason to provide context for future reference
- Verify archive file was created successfully before confirming active changelog cleanup

## Limitations

- Cannot selectively archive specific entries - all entries before cutoff date are archived together
- Does not automatically determine optimal archive timing - requires manual decision
- Archived entries are moved, not copied - they no longer appear in active changelog
- Cannot easily merge archived entries back into active changelog if needed
- Does not compress or optimize archived files - large archives may need manual management

**Source**: `olaf-core/competencies/project-manager/prompts/archive-changelog-entries.md`
