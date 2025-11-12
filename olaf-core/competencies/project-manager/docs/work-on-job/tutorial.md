# Work on Job: Step-by-Step Tutorial

**How to Execute the "Work on Job" Competency**

This tutorial shows exactly how to guide the process of working on an existing job by identifying the job, executing tasks, tracking progress, updating documentation, and maintaining the job status.

## Prerequisites

- OLAF framework loaded and active
- Existing job file created (use create-job if needed)
- Access to job directory and files
- Understanding of job workflow and status transitions

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Initiate the work-on-job process.

**User Action:**
1. Type: `olaf work on job`
2. Or use any alias: `olaf execute job`, `olaf job work`, `olaf continue job`
3. Press Enter to start the process

**AI Response:**
The AI will acknowledge the request and begin gathering job information using the Act protocol.

### Step 2: Identify Target Job
**AI Asks:** "Which job would you like to work on?"

**User Action:** Provide job identifier

**Options:**
- **job_id**: "JOB-042" (specific job ID)
- **Browse**: "show me open jobs" (list available jobs)
- **Latest**: "continue last job" (resume most recent)

**Example Response:**
```
Job ID: JOB-042
```

### Step 3: Job Initialization
**What AI Does:**
1. Loads job file from jobs directory
2. Parses job details (title, description, status, tasks)
3. Verifies job status (Open, In Progress, Blocked, etc.)
4. Checks for dependencies or blockers
5. Reviews task list and completion status

**You Should See:** 
Job overview with current status, completed tasks, and pending items.

**Job Overview Display:**
```markdown
Job: JOB-042 - Implement OAuth 2.0 token refresh
Status: Open
Priority: High
Assignee: @DevLead

Completed Tasks: 0/3
Pending Tasks:
- [ ] Design refresh token flow
- [ ] Implement refresh endpoint
- [ ] Add client-side refresh logic
```

### Step 4: Specify Action (Optional)
**AI Asks:** "What would you like to do?"

**User Action:** Choose action or let AI recommend

**Options:**
- **continue**: Work on next pending task (default)
- **subtask**: "work on specific subtask: Design refresh token flow"
- **pause**: Pause work and document current state
- **complete**: Mark job as complete
- **priority**: Adjust priority level

**Example Response:**
```
Action: continue
```

### Step 5: Task Execution
**What AI Does:**
1. Identifies next action based on task list
2. Provides context and requirements for the task
3. Executes or guides execution of subtasks
4. Tracks time and resources used
5. Documents progress in real-time

**For Each Subtask:**
- Explains what needs to be done
- Provides relevant context and references
- Executes code changes or file operations
- Validates completion criteria
- Updates task status

**You Should See:** 
Step-by-step execution with progress updates for each subtask.

### Step 6: Progress Documentation
**What AI Does:**
- Updates job file with completed tasks
- Records completion timestamps
- Documents any issues or blockers encountered
- Updates job status (Open → In Progress → Review → Complete)
- Creates changelog entries for significant progress

**Automatic Updates:**
```markdown
## Progress Log
- 2025-10-27 14:30: Started work on job
- 2025-10-27 14:45: Completed "Design refresh token flow"
- 2025-10-27 15:20: Completed "Implement refresh endpoint"
```

### Step 7: Quality Assurance
**What AI Does:**
- Verifies task completion against acceptance criteria
- Validates outputs (code, documentation, etc.)
- Runs tests if applicable
- Checks for integration issues
- Requests sign-off if required

**You Should See:** 
Validation results and confirmation of task completion.

### Step 8: Status Update and Next Steps
**AI Provides:**
1. **Current Status**:
   - Job overview with updated progress
   - Completed tasks marked
   - Remaining pending items
   - Any blockers identified

2. **Next Actions**:
   - Recommended next steps
   - Priority tasks to focus on
   - Dependencies to resolve

3. **Documentation**:
   - Updated job file location
   - Changelog entries created
   - Reference links to related work

**User Action:**
- Continue with next task
- Pause and save progress
- Mark job complete if all tasks done

## Verification Checklist

✅ **Job loaded successfully** with all details
✅ **Current status accurate** and up-to-date
✅ **Tasks executed** according to plan
✅ **Progress documented** in job file
✅ **Changelog entries created** for significant updates
✅ **Quality checks passed** for completed work
✅ **Next steps identified** clearly

## Troubleshooting

**If job file not found:**
```bash
# List available jobs
ls olaf-data/projects/jobs/

# Verify job ID format
cat olaf-data/projects/jobs-register.md
```

**If job status inconsistent:**
- Review job file manually for corruption
- Check changelog for recent updates
- Verify no concurrent modifications

**If task execution fails:**
- Document the blocker in job file
- Update status to "Blocked"
- Create decision record if needed
- Notify stakeholders

**If dependencies missing:**
- Identify required resources or information
- Update job file with dependency notes
- Adjust priority or timeline as needed

## Key Learning Points

1. **Continuous Documentation**: Progress is documented in real-time, not after the fact, ensuring accurate records.

2. **State Management**: Job status transitions (Open → In Progress → Review → Complete) provide clear workflow visibility.

3. **Atomic Task Execution**: Each subtask is completed and verified before moving to the next, ensuring quality.

4. **Flexible Workflow**: The competency supports pausing, resuming, and adjusting priorities as project needs change.

## Next Steps to Try

- Work on multiple jobs in parallel
- Link job progress to decision records
- Generate progress reports using review-progress
- Create follow-up jobs for additional work
- Archive completed jobs for historical reference

## Expected Timeline

- **Total process time:** Varies by job complexity (30 minutes to several hours)
- **User input required:** Minimal after initial job selection
- **AI execution time:** Depends on task complexity and automation level
- **Documentation updates:** Real-time throughout execution
