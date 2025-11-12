---

name: analyze-changelog-and-report

description: Analyze changelog register entries, cross-reference with prompt files, identify discrepancies, and generate a summary report.

tags: [analysis, changelog, reporting, automation]

---
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.

- **start_date**: string (YYYYMMDD) - The start date for changelog analysis

- **prompt_dir**: string - (Optional) Directory containing prompt files to check against



## Process



1. **Input Validation**:

   - Verify date format is YYYYMMDD

   - Set default prompt directory if not provided



2. **Changelog Analysis**:

   - Read entries from `[id:changelog_register]` since start_date

   - Parse and categorize entries by type/theme

   - Identify any incomplete or malformed entries



3. **Prompt File Verification**:prompt files

   - Cross-reference with changelog entries

   - Flag any discrepancies or missing documentation



4. **Discrepancy Resolution**:

   - Present findings to user

   - Allow for confirmation or correction

   - Document resolutions



5. **Report Generation**:

   - Use template: `[id:competencies_dir][competency]/templates/project-manager/changelog-template.md`

   - Include summary of changes

   - List prompt files with status

   - Document any discrepancies found and resolutions



## Output/Result Format

- Final report saved as: `[id:findings_dir]ChangelogSummaries/YYYYMMDD-HHMMSS-summary.md`

- Interactive markdown with collapsible sections

- Summary statistics

- Detailed change listing

- Discrepancy report



## Output to USER

1. **Initial Analysis**:

   - Number of changelog entries found

   - Number of prompt files checked

   - Summary of potential issues



2. **Discrepancy Resolution**:

   - Interactive prompt for each issue

   - Options to skip, resolve, or flag for review



3. **Final Report**:

   - Executive summary

   - Detailed change log

   - Resolution documentation

   - Recommendations



## Domain-Specific Rules

- Rule 1: Always preserve original changelog data

- Rule 2: Maintain audit trail of all changes

- Rule 3: Flag potential issues but don't auto-correct

- Rule 4: Group related changes by theme/component

- Rule 5: Include timestamps for all actions



## Required Actions

1. Validate input parameters

2. Extract and analyze changelog entries

3. Verify prompt files

4. Resolve discrepancies

5. Generate and save report



⚠️ **Critical Notes**

- Never modify original changelog entries

- Always provide option for manual review

- Include references to original data

- Document all assumptions

- Preserve timestamps and authorship

