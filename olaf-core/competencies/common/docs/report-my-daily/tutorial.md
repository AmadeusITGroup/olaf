# Report My Daily: Step-by-Step Tutorial

**How to Execute the "Report My Daily" Workflow**

This tutorial shows how to generate a daily work report by analyzing your git activity and project artifacts.

## Prerequisites

- Git repository with commit history
- Work done during the day (commits, file changes, etc.)
- Access to project files and git history

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Generate your daily report

**User Action:**
1. At end of day, type: `report my daily`
2. Optionally specify date range

**OLAF Response:**
OLAF will begin analyzing your git activity and project files

### Step 2: Git Activity Analysis
**What OLAF Does:**
- Runs `git log` to get today's commits
- Analyzes commit messages and changes
- Identifies files modified
- Calculates lines added/removed
- Groups changes by feature or area

**You Should See:** Progress indication of git analysis

### Step 3: File and Artifact Analysis
**What OLAF Does:**
- Reviews modified files for context
- Checks for PR descriptions or comments
- Analyzes code changes for patterns
- Identifies completed features or fixes
- Notes any TODO items or blockers

**You Should See:** Analysis of work artifacts

### Step 4: Report Generation
**What OLAF Provides:**
- Summary of accomplishments
- List of commits with descriptions
- Files modified by category
- Features completed or in progress
- Blockers or issues encountered
- Next steps planned

**You Should See:** Structured daily report

### Step 5: Review and Share
**User Action:** Use the report
- Review for accuracy
- Request additions or clarifications
- Copy for standup or status update
- Save for personal records

## Verification Checklist

✅ **All commits from today are included**
✅ **Work is accurately summarized**
✅ **Features and accomplishments are highlighted**
✅ **Blockers or issues are noted**
✅ **Report is ready to share**

## Troubleshooting

**If no commits found:**
```
No commits found for today
```
Solution: Verify you have commits in the current repository, or specify a different date range

**If report seems incomplete:**
- Specify date range: "report my daily for yesterday"
- Include specific branches: "report my daily including feature branches"
- Add context: "also include work on the API redesign"

**If you want different format:**
- Request specific format: "format as bullet points for standup"
- Ask for different grouping: "group by feature instead of by file"

## Key Learning Points

1. **Automated Analysis**: Analyzes git history automatically
2. **Context-Aware**: Understands code changes and their purpose
3. **Flexible Reporting**: Can customize format and content
4. **Time-Saving**: Eliminates manual report writing

## Next Steps to Try

- Use for daily standups or status updates
- Generate weekly summaries: "report my work this week"
- Compare with previous days: "how does today compare to yesterday?"
- Create carry-over notes: `create carry-over` after reviewing report

## Expected Timeline

- **Total report time:** 2-3 minutes
- **User input required:** Just the command (10 seconds)
- **OLAF execution time:** Git analysis and report generation (2-3 minutes)
