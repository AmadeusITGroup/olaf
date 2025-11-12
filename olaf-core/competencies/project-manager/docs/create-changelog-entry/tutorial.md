# Create Changelog Entry: Step-by-Step Tutorial

**How to Execute the "Create Changelog Entry" Competency**

This tutorial shows exactly how to add a new entry to the main changelog file with proper formatting and structure.

## Prerequisites

- OLAF framework loaded and active
- Access to changelog register file
- Understanding of change types (Feature, Fix, Chore, Documentation, etc.)
- Changelog template available

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Initiate the changelog entry creation process.

**User Action:**
1. Type: `olaf create changelog entry`
2. Or use any alias: `olaf changelog entry`, `olaf add changelog`, `olaf log change`
3. Press Enter to start the process

**AI Response:**
The AI will acknowledge the request and begin gathering required information using the Propose-Act protocol.

### Step 2: Provide Change Information
**User Action:** Respond to prompts with change details

**Required Parameters:**
- **change_type**: Select from: Feature, Fix, Chore, Documentation, Report, Analysis, Release, Review, Refactor
- **description**: "Added OAuth 2.0 authentication support"

**Optional Parameters:**
- **links**: "job-123, PR#45, abc1234" (references to related jobs, commits, or PRs)

**Example Input:**
```
Change Type: Feature
Description: Added OAuth 2.0 authentication support with PKCE flow
Links: job-042, PR#156, commit-7a8b9c2
```

### Step 3: Automatic Timestamp Retrieval
**What AI Does:**
- Executes terminal command to get current time
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`
- Formats timestamp as: YYYYMMDD HH:MM (24-hour format)
- Uses actual system time, not training data

**You Should See:** 
Confirmation of timestamp retrieved (e.g., "20251027 14:30").

### Step 4: Template Loading and Formatting
**What AI Does:**
- Reads changelog template from competency pack
- Parses required format structure
- Validates against expected template sections
- Prepares formatted entry

**Entry Format:**
```markdown
- Type: Description of the change [Links: job-123, PR#45, abc1234]
```

### Step 5: Changelog Update
**What AI Does:**
1. Reads current changelog register content
2. Locates or creates appropriate date section (YYYYMMDD format)
3. Inserts new entry at the top of the day's entries
4. Maintains reverse chronological order
5. Preserves all existing formatting and structure
6. Writes updated content back to file

**You Should See:** 
Preview of the exact entry that was added with context before and after.

### Step 6: Confirmation and Verification
**AI Response:**
- Entry successfully added confirmation
- Timestamp used in the entry
- Location in changelog file
- Preview of the new entry in context

**User Action:**
Review the confirmation to ensure accuracy.

## Verification Checklist

✅ **Changelog entry added** to correct date section
✅ **Entry at top of day's section** (reverse chronological order)
✅ **Timestamp format correct** (YYYYMMDD HH:MM)
✅ **Change type specified** (Feature, Fix, Chore, etc.)
✅ **Description clear and concise**
✅ **Links properly formatted** (if provided)
✅ **Existing entries preserved** without modification

## Troubleshooting

**If timestamp format is incorrect:**
```bash
# Manually verify system time
# Windows:
Get-Date -Format "yyyyMMdd-HHmm"
# Unix/Linux/macOS:
date +"%Y%m%d-%H%M"
```

**If date section doesn't exist:**
The AI will automatically create the missing date/month sections as needed following the existing structure.

**If entry appears in wrong location:**
- Verify the changelog follows reverse chronological order
- Check that new entries are added to the top of their day section
- Review the changelog structure for consistency

**If links are not formatted correctly:**
Ensure links follow the format: `[Links: job-123, PR#45, abc1234]` with comma separation.

## Key Learning Points

1. **Reverse Chronological Order**: New entries always go to the top of their day section, making recent changes easy to find.

2. **Terminal Time Usage**: The competency always uses actual system time via terminal commands, never training data, ensuring accurate timestamps.

3. **Atomic Updates**: Each changelog entry is a single, focused change description that can be easily tracked and referenced.

4. **Structured Format**: Consistent formatting makes changelog entries machine-readable and easy to parse for reports and analysis.

## Next Steps to Try

- Create multiple changelog entries for different change types
- Use the analyze-changelog-and-report competency to generate summaries
- Archive old changelog entries using archive-changelog-entries
- Link changelog entries to decision records and job files

## Expected Timeline

- **Total process time:** 1-2 minutes
- **User input required:** 30 seconds to provide change details
- **AI execution time:** 30-60 seconds for timestamp retrieval, template loading, and file update
