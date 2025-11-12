---

name: create-changelog-entry

description: Add a new entry to the main changelog file with proper formatting and structure.

tags: [changelog, documentation, versioning, maintenance]

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

- **change_type**: enum[Feature,Fix,Chore,Documentation,Report,Analysis,Release,Review,Refactor] - Type of change being logged

- **description**: string - Concise description of the change

- **links**: string - (Optional) References to related jobs, commits, or PRs



## Process



1. **Time Retrieval**:

   - Get current timestamp using system command

   - Format: `YYYYMMDD HH:MM` (24-hour format)

   - Use terminal time, not system date for consistency



2. **Template Loading**:

   - Read file: `[id:competencies_dir][competency]/templates/project-manager/changelog-template.md`

   - Parse and understand the required format

   - Validate against expected structure



3. **Changelog Update**:

   - Read current `[id:changelog_register]` content

   - Locate or create appropriate date section

   - Insert new entry at the top of the day's entries

   - Maintain proper section hierarchy

   - Write updated content back to file



## Output/Result Format

- Markdown-formatted changelog entry

- Consistent with existing structure

- Includes all necessary metadata

- Properly linked to related resources



## Output to USER

1. **Confirmation**:

   - Entry successfully added

   - Timestamp used

   - Location in changelog



2. **Preview**:

   - The exact entry that was added

   - Context before and after



3. **Next Steps**:

   - How to edit if needed

   - How to verify the entry



## Domain-Specific Rules

- Rule 1: Always add new entries to the top of their day section

- Rule 2: Maintain reverse chronological order for all entries

- Rule 3: Use consistent timestamp format (YYYYMMDD HH:MM)

- Rule 4: Preserve all existing formatting and structure

- Rule 5: Create missing date/month sections as needed



## Required Actions

1. Get current timestamp

2. Load and parse template

3. Read current changelog

4. Insert new entry

5. Save updated changelog

6. Verify changes



## Entry Format Example

```markdown

- Type: Description of the change [Links: job-123, PR#45, abc1234]

```



⚠️ **Critical Notes**

- Always use terminal time, not system date

- Never modify existing entries (except for the current day's section)

- Preserve all whitespace and formatting

- Validate all links before adding

- Create backups before making changes

