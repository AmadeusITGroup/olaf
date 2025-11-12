# Project Manager Competency Package - Tool Inventory

**Document Date**: October 21, 2025  
**Status**: Active - Tools Included  

---

## Tool Inventory Summary

The Project Manager competency package includes **1 specialized Python tool** for changelog management and access to shared commons utilities.

### Packaged Tools

| Tool | Version | Purpose | Location | Used By | Status |
|------|---------|---------|----------|---------|--------|
| `archive_changelog_entries.py` | 1.0 | Automated changelog archiving and management | `tools/archive_changelog_entries.py` | archive-changelog-entries | ✅ Included |

### Shared Commons Utilities (Included)

| Utility | Location | Purpose | Status |
|---------|----------|---------|--------|
| `project-onboarding/` | `tools/commons/project-onboarding/` | Shared analysis tools for project metrics | ✅ Included |

### Tool Dependencies (External)

| Tool | Version | Purpose | Platforms | Status |
|------|---------|---------|-----------|--------|
| `python` | ≥3.10 | Runtime for changelog processing | Windows, Linux, macOS | **Required** |
| `git` | ≥2.30 | Version control for changelog tracking | Windows, Linux, macOS | **Optional** |

---

## Competency-Specific Tool Usage

### Competency: Archive Changelog Entries

**Tools Used**: `archive_changelog_entries.py`  
**Platforms**: Cross-platform  

**Workflow**:
```bash
python tools/archive_changelog_entries.py [changelog-file] [archive-folder] [options]
```

**Requirements**:
- Changelog markdown file as input
- Python 3.10+ installed
- Changelog follows standard format
- Write access to archive folder

**Features**:
- Automated entry extraction based on date ranges
- Archive file generation with proper formatting
- Changelog cleanup and reorganization
- Backup creation before modifications

### Other Competencies

Other competencies (create-changelog-entry, analyze-changelog-and-report, generate-commits-from-changelog, create-decision-record, create-job, create-person-record, generate-tasklist, generate-professional-release-notes, prepare-conversation-handover, review-progress, stash-work-session, carry-over-session, carry-on-session, stash-restart-session, store-conversation-record, work-on-job) use pure LLM-based task management and documentation generation without requiring packaged tools.

---

## Installation Instructions

### Install Python Dependencies

```bash
# Verify Python installation
python --version  # Should be 3.10+

# No additional pip packages required for archive_changelog_entries.py
# (Uses only standard library)
```

### Verify Tool Access

```bash
# Check archive_changelog_entries.py exists
ls -la tools/archive_changelog_entries.py

# Check python version
python --version  # Should be 3.10+
```

---

## Shared Tool References

**See**: `olaf-core/competencies/TOOLS-USED-BY-COMPETENCIES.md` for cross-competency tool usage patterns.

The Project Manager package includes:
- **Exclusive Tool**: `archive_changelog_entries.py` (not shared with other personas)
- **Shared Utilities**: Commons project-onboarding tools (shared reference, not actively used)

---

## Notes

- The `archive_changelog_entries.py` tool is Python-based and cross-platform compatible
- Requires Python 3.10 or higher for execution
- No external dependencies beyond Python standard library
- The commons utilities are included for reference but not directly used by project-manager competencies
- Git integration is optional for advanced changelog tracking
- Recommended LLM: Claude Sonnet 4.5 or higher for task orchestration and documentation
