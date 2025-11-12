# Archive Changelog Entries: Step-by-Step Tutorial

**How to Execute the "Archive Changelog Entries" Competency**

This tutorial shows exactly how to archive changelog entries older than a specified number of days to maintain a clean and organized changelog register.

## Prerequisites

- OLAF framework loaded and active
- Python 3.x installed and accessible
- Changelog register with entries to archive
- Archive changelog file location configured
- Write permissions for changelog and archive files

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Initiate the changelog archival process.

**User Action:**
1. Type: `olaf archive changelog entries`
2. Or use any alias: `olaf archive changelog`, `olaf cleanup changelog`, `olaf clean changelog`
3. Press Enter to start the process

**AI Response:**
The AI will acknowledge the request and begin gathering required parameters using the Propose-Act protocol.

### Step 2: Provide Archival Parameters
**User Action:** Respond to prompts with archival criteria

**Optional Parameters (with defaults):**
- **days_to_keep**: 7 (number of days of entries to keep in active changelog)
- **changelog_path**: Uses `[id:changelog_register]` from memory-map
- **archive_path**: Uses `[id:changelog_register_archive]` from memory-map

**Example Input:**
```
Days to Keep: 30
Changelog Path: (use default)
Archive Path: (use default)
```

### Step 3: File Path Validation
**What AI Does:**
- Resolves changelog_register path from memory-map.md
- Resolves archive path from memory-map.md
- Verifies both files exist or can be created
- Checks file permissions for read/write access
- Validates Python script availability

**You Should See:** 
Confirmation of file paths and permissions validated successfully.

### Step 4: Python Script Execution
**What AI Does:**
Executes the archival script with validated parameters:

```python
import subprocess

subprocess.run([
    "python", "olaf-core/tools/archive_changelog_entries.py",
    "olaf-data/product/documentations/changelog-register.md",
    "olaf-data/product/documentations/changelog-register-archive.md",
    "--days-to-keep", "7"
], check=True)
```

**Script Actions:**
1. Reads current changelog register
2. Identifies entries older than specified days
3. Moves old entries to archive file
4. Maintains chronological order in both files
5. Preserves all formatting and metadata
6. Adds maintenance entry to changelog

**You Should See:** 
Script execution progress and status messages.

### Step 5: Archival Process
**What Python Script Does:**
- Parses changelog entries by date
- Calculates cutoff date (today - days_to_keep)
- Separates entries into keep/archive groups
- Writes archived entries to archive file (appends)
- Writes kept entries to changelog file (overwrites)
- Maintains section structure and formatting

**Automatic Actions:**
- Creates backup of original files (optional safety measure)
- Validates entry counts before and after
- Ensures no data loss during transfer

### Step 6: Maintenance Entry Creation
**What AI Does:**
- Adds maintenance entry to changelog documenting the archival
- Includes timestamp, number of entries archived, and date range
- Format: `- Chore: Archived X changelog entries older than YYYY-MM-DD`

**You Should See:** 
Maintenance entry added to changelog for audit trail.

### Step 7: Execution Summary
**AI Provides:**
1. **Archival Statistics**:
   - Number of entries archived
   - Number of entries remaining in active changelog
   - Date range of archived entries
   - Archive file location

2. **Validation Results**:
   - File integrity check passed
   - Entry count verification (before = after)
   - Maintenance entry confirmation

3. **Any Warnings or Errors**:
   - File permission issues
   - Missing entries
   - Format inconsistencies

**You Should See:** 
Complete summary with all statistics and confirmation of successful archival.

## Verification Checklist

✅ **Old entries moved to archive** (older than days_to_keep)
✅ **Recent entries remain** in active changelog
✅ **Chronological order maintained** in both files
✅ **All formatting preserved** (no data corruption)
✅ **Maintenance entry added** to changelog
✅ **Entry counts validated** (no entries lost)
✅ **Archive file updated** with new entries appended

## Troubleshooting

**If Python script not found:**
```bash
# Verify script exists
ls olaf-core/tools/archive_changelog_entries.py

# Check Python installation
python --version
```

**If permission denied:**
```bash
# Check file permissions
ls -l olaf-data/product/documentations/changelog-register.md

# Grant write permissions if needed (Unix/Linux/macOS)
chmod u+w olaf-data/product/documentations/changelog-register.md
```

**If entries not archived:**
- Verify date format in changelog entries (YYYYMMDD)
- Check that entries are actually older than days_to_keep
- Review script output for parsing errors

**If archive file grows too large:**
- Consider creating yearly archive files
- Compress old archive files
- Implement archive rotation policy

## Key Learning Points

1. **Non-Destructive Archival**: Entries are moved, never deleted, ensuring complete project history is preserved.

2. **Automated Maintenance**: The Python script handles all file operations automatically, reducing manual effort and errors.

3. **Audit Trail**: Maintenance entries document when and what was archived, providing transparency.

4. **Configurable Retention**: The days_to_keep parameter allows flexible retention policies based on project needs.

## Next Steps to Try

- Set up automated monthly archival using cron jobs or scheduled tasks
- Create yearly archive files for long-term storage
- Analyze archived entries for historical project insights
- Integrate archival with release cycles
- Generate reports from archived data

## Expected Timeline

- **Total process time:** 1-3 minutes
- **User input required:** 30 seconds to provide parameters
- **AI execution time:** 30-120 seconds for script execution and validation
- **Processing speed:** ~1000 entries per second
- **File operations:** Depends on changelog size (typically < 1 second)
