# Analyze Changelog and Report: Step-by-Step Tutorial

**How to Execute the "Analyze Changelog and Report" Competency**

This tutorial shows exactly how to analyze changelog register entries, cross-reference with prompt files, identify discrepancies, and generate a comprehensive summary report.

## Prerequisites

- OLAF framework loaded and active
- Changelog register with entries to analyze
- Access to prompt files directory (optional)
- Understanding of date formats (YYYYMMDD)

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Initiate the changelog analysis process.

**User Action:**
1. Type: `olaf analyze changelog and report`
2. Or use any alias: `olaf analyze changelog`, `olaf changelog report`, `olaf progress analysis`
3. Press Enter to start the process

**AI Response:**
The AI will acknowledge the request and begin gathering required parameters using the Act protocol.

### Step 2: Provide Analysis Parameters
**User Action:** Respond to prompts with analysis criteria

**Required Parameters:**
- **start_date**: "20251001" (YYYYMMDD format - analyze entries from this date forward)

**Optional Parameters:**
- **prompt_dir**: "olaf-core/competencies/" (directory containing prompt files to check against)

**Example Input:**
```
Start Date: 20251001
Prompt Directory: olaf-core/competencies/
```

### Step 3: Input Validation
**What AI Does:**
- Verifies date format is YYYYMMDD
- Validates date is not in the future
- Sets default prompt directory if not provided
- Confirms parameters before proceeding

**You Should See:** 
Confirmation of validated parameters and start of analysis.

### Step 4: Changelog Analysis
**What AI Does:**
1. Reads changelog register from specified start date
2. Parses entries by date, type, and theme
3. Categorizes changes (Features, Fixes, Chores, Documentation, etc.)
4. Identifies incomplete or malformed entries
5. Counts entries by category
6. Extracts referenced jobs, PRs, and commits

**You Should See:** 
Initial analysis summary showing:
- Number of changelog entries found
- Date range covered
- Distribution by change type
- Potential formatting issues

### Step 5: Prompt File Verification (Optional)
**What AI Does:**
- Scans specified prompt directory
- Cross-references prompt files with changelog entries
- Identifies prompts mentioned in changelog
- Flags any discrepancies or missing documentation
- Lists prompt files with their status

**You Should See:** 
Number of prompt files checked and summary of potential issues.

### Step 6: Discrepancy Resolution
**User Action:** Review and resolve identified issues

**AI Presents:**
- Each discrepancy with context
- Options: Skip, Resolve, Flag for review
- Recommendations for resolution

**Interactive Prompts:**
```
Issue: Changelog references job-042 but file not found
Options:
1. Skip (ignore this issue)
2. Resolve (provide correct reference)
3. Flag for manual review
```

**User Action:**
Select appropriate option for each issue.

### Step 7: Report Generation
**What AI Does:**
- Uses changelog template for report structure
- Compiles executive summary with statistics
- Creates detailed change listing by category
- Documents all discrepancies and resolutions
- Includes recommendations for improvements
- Saves report with timestamp

**Report Saved To:**
`olaf-data/findings/ChangelogSummaries/YYYYMMDD-HHMMSS-summary.md`

### Step 8: Final Report Delivery
**AI Provides:**
1. **Executive Summary**: High-level overview of changes
2. **Detailed Change Log**: All entries organized by type
3. **Resolution Documentation**: How discrepancies were handled
4. **Recommendations**: Suggestions for process improvements

**You Should See:** 
Complete report with collapsible sections, summary statistics, and actionable insights.

## Verification Checklist

✅ **All changelog entries analyzed** from start date forward
✅ **Entries categorized correctly** by type and theme
✅ **Prompt files cross-referenced** (if directory provided)
✅ **Discrepancies identified and documented**
✅ **Report generated and saved** with timestamp
✅ **Original changelog preserved** without modifications
✅ **Audit trail maintained** for all actions

## Troubleshooting

**If no entries found:**
```bash
# Verify changelog file exists and has content
cat olaf-data/product/documentations/changelog-register.md
```
Check that start_date is not after all existing entries.

**If prompt directory not found:**
- Verify the path is correct relative to workspace root
- Use absolute path if relative path fails
- Check directory permissions

**If report generation fails:**
- Ensure findings directory exists: `olaf-data/findings/ChangelogSummaries/`
- Check write permissions
- Verify sufficient disk space

**If discrepancies seem incorrect:**
- Review the original changelog entries for accuracy
- Verify prompt file references are correct
- Check for typos in job/PR/commit references

## Key Learning Points

1. **Non-Destructive Analysis**: This competency never modifies the original changelog, only reads and analyzes it.

2. **Cross-Reference Validation**: Linking changelog entries to actual prompt files helps identify documentation gaps and inconsistencies.

3. **Interactive Resolution**: The competency allows manual review of each issue rather than auto-correcting, preserving human judgment.

4. **Comprehensive Reporting**: Generated reports include both summary statistics and detailed listings for different audiences.

## Next Steps to Try

- Generate monthly changelog reports for stakeholder updates
- Use reports to identify patterns in change types
- Cross-reference with decision records for impact analysis
- Archive analyzed entries using archive-changelog-entries
- Create release notes from changelog analysis

## Expected Timeline

- **Total process time:** 5-10 minutes (depends on entry count)
- **User input required:** 1-2 minutes for parameters and discrepancy resolution
- **AI execution time:** 3-8 minutes for analysis, cross-referencing, and report generation
- **Entries processed:** ~50-100 entries per minute
