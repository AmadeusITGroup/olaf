# Create Carry-Over: Step-by-Step Tutorial

**How to Execute the "Create Carry-Over" Workflow**

This tutorial shows how to create session carry-over notes for future work resumption.

## Prerequisites

- Active OLAF session with work in progress
- Meaningful context or progress to capture
- `carry-overs/` directory exists (created automatically if needed)

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Create carry-over notes at the end of your session

**User Action:**
1. When ready to end your session, type: `create carry-over`
2. Optionally provide additional notes or context

**OLAF Response:**
OLAF will analyze the current session and begin creating the carry-over summary

### Step 2: Session Analysis
**What OLAF Does:**
- Reviews the conversation history
- Identifies key accomplishments and progress
- Extracts important decisions made
- Notes any blockers or open questions
- Determines logical next steps

**You Should See:** Confirmation that session is being analyzed

### Step 3: File Creation
**What OLAF Does:**
- Generates structured carry-over content
- Creates timestamp-based filename (YYYYMMDD-HHmm format)
- Writes file to `carry-overs/` directory
- Confirms successful file creation

**You Should See:** Confirmation message with filename
```
Carry-over notes saved to: carry-overs/carry-over-20251027-1730.txt
```

### Step 4: Review Summary
**User Action:** Review the carry-over summary
- OLAF will display the summary content
- Verify it captures the essential context
- Request additions if anything important is missing
- Confirm the summary is complete

## Verification Checklist

✅ **File created in carry-overs/ directory with timestamp**
✅ **Summary captures key accomplishments**
✅ **Important decisions are documented**
✅ **Next steps are clearly identified**
✅ **Sufficient context for future resumption**

## Troubleshooting

**If carry-overs/ directory doesn't exist:**
OLAF will create it automatically - no action needed

**If summary seems incomplete:**
- Provide additional context: "also include the API design decisions"
- Request specific additions: "add notes about the database schema changes"
- OLAF will update the carry-over file

**If you need to edit the file later:**
Files are plain text - you can manually edit them in `carry-overs/` directory

## Key Learning Points

1. **Automatic Analysis**: OLAF analyzes the session automatically
2. **Timestamped Files**: Files use YYYYMMDD-HHmm format for chronological organization
3. **Private Files**: carry-overs/ is gitignored - notes stay local
4. **Structured Format**: Consistent format makes resumption easier

## Next Steps to Try

- End your current session
- Start a new session and use `carry on` to resume
- Create multiple carry-overs throughout the day for different work sessions
- Query your work history: "what did I accomplish this week?"

## Expected Timeline

- **Total creation time:** 1-2 minutes
- **User input required:** Just the command (10 seconds)
- **OLAF execution time:** Analysis and file creation (1-2 minutes)
