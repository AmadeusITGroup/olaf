# Create Job: Step-by-Step Tutorial

**How to Execute the "Create Job" Competency**

This tutorial shows exactly how to create a new job file in the jobs directory following the job template structure with proper ID generation and system integration.

## Prerequisites

- OLAF framework loaded and active
- Access to jobs directory and job register
- Job template available
- Understanding of job types and priorities

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Initiate the job creation process.

**User Action:**
1. Type: `olaf create job`
2. Or use any alias: `olaf new job`, `olaf job record`, `olaf create work`
3. Press Enter to start the process

**AI Response:**
The AI will acknowledge the request and begin gathering required information using the Propose-Confirm-Act protocol.

### Step 2: Provide Job Details
**User Action:** Respond to prompts with job information

**Required Parameters:**
- **job_title**: "Implement OAuth 2.0 token refresh"
- **job_type**: User Story | Bug Fix | Task | Refactoring | Spike | Feature Enhancement | Other
- **priority**: High | Medium | Low
- **job_description**: "Add automatic token refresh to prevent session expiration"

**Optional Parameters:**
- **initial_tasks**: "1. Design refresh token flow, 2. Implement refresh endpoint, 3. Add client-side refresh logic"
- **reference_links**: "https://oauth.net/2/refresh-tokens/, DR-20251027-01"
- **assignee**: "@DevLead" (defaults to @AssigneeName if not provided)

**Example Input:**
```
Job Title: Implement OAuth 2.0 token refresh
Job Type: Feature Enhancement
Priority: High
Description: Add automatic token refresh to prevent session expiration
Initial Tasks: Design refresh token flow, Implement refresh endpoint, Add client-side refresh logic
Reference Links: https://oauth.net/2/refresh-tokens/
Assignee: @DevLead
```

### Step 3: Template and Register Loading
**What AI Does:**
1. Reads job template: `olaf-core/competencies/project-manager/templates/job-template.md`
2. Reads job register: `olaf-data/projects/jobs-register.md`
3. Extracts current serial number from register
4. Validates template structure

**You Should See:** 
Confirmation that template and register loaded successfully.

### Step 4: Job ID Generation
**What AI Does:**
- Increments serial number from job register
- Creates new job ID format: `JOB-{serial}` (e.g., JOB-042)
- Prepares filename: `JOB-042.md`
- Ensures no duplicate IDs exist

**You Should See:** 
Generated job ID displayed for confirmation.

### Step 5: Template Population
**What AI Does:**
- Uses job template structure as base
- Fills all required sections with provided parameters:
  - Job title and description
  - Job type and priority
  - Assignee information
  - Initial tasks (if provided)
  - Reference links (if provided)
- Sets creation date using terminal timestamp
- Sets initial status to "Open" or "To Do"
- Generates proper job metadata

**Template Sections Populated:**
```markdown
# JOB-042: Implement OAuth 2.0 token refresh

**Type:** Feature Enhancement
**Priority:** High
**Status:** Open
**Assignee:** @DevLead
**Created:** 2025-10-27
**Updated:** 2025-10-27

## Description
Add automatic token refresh to prevent session expiration

## Tasks
- [ ] Design refresh token flow
- [ ] Implement refresh endpoint
- [ ] Add client-side refresh logic

## References
- https://oauth.net/2/refresh-tokens/
```

### Step 6: Review Proposed Job
**AI Presents:** Complete job file for review

**User Action:**
1. Review all sections carefully
2. Type "approved" or "yes" to proceed
3. Or request changes: "update priority to Medium"

**AI Response:**
If approved, creates files and updates register. If changes requested, revises and presents again.

### Step 7: File Creation and Register Update
**What AI Does:**
1. Creates job file: `olaf-data/projects/jobs/JOB-042.md`
2. Updates job register with new entry
3. Increments serial number in register
4. Saves updated register file
5. Creates changelog entry documenting job creation

**Atomic Operation:**
Both job file and register update must succeed together to maintain consistency.

### Step 8: Confirmation
**AI Provides:**
- Job creation confirmation with ID: `JOB-042`
- File location: `olaf-data/projects/jobs/JOB-042.md`
- Updated job register confirmation
- Job details summary for verification
- Next steps: Begin work using `work-on-job` competency

**You Should See:** 
Complete confirmation with all file locations and next action recommendations.

## Verification Checklist

✅ **Unique job ID generated** (JOB-{serial} format)
✅ **Job file created** in correct directory
✅ **All required sections populated** from template
✅ **Job register updated** with new entry
✅ **Serial number incremented** in register
✅ **Changelog entry created** documenting the action
✅ **Template structure preserved** exactly

## Troubleshooting

**If duplicate job ID error:**
```bash
# Check existing jobs
ls olaf-data/projects/jobs/

# Verify job register serial number
cat olaf-data/projects/jobs-register.md | grep "Serial"
```
The AI should automatically handle this, but manual verification may be needed.

**If job register not found:**
- Verify path in memory-map.md: `[id:jobs]`
- Create register file if missing
- Initialize with serial number: 0

**If template not found:**
Verify template exists at: `olaf-core/competencies/project-manager/templates/job-template.md`

**If file creation fails:**
- Check directory permissions
- Verify sufficient disk space
- Ensure no file locks on job directory

## Key Learning Points

1. **Atomic Operations**: Job file and register update happen together to prevent inconsistencies.

2. **Sequential ID Generation**: Job IDs are sequential (JOB-001, JOB-002, etc.) for easy tracking and reference.

3. **Template-Based Consistency**: Using templates ensures all jobs have the same structure and required information.

4. **Propose-Confirm-Act Protocol**: Two-step confirmation prevents accidental job creation with incorrect information.

## Next Steps to Try

- Use work-on-job competency to start executing the created job
- Link job to related decision records or changelog entries
- Create multiple jobs for a project and track in register
- Generate tasklists from job descriptions
- Review progress across all jobs using review-progress

## Expected Timeline

- **Total process time:** 3-5 minutes
- **User input required:** 2-3 minutes to provide job details and review
- **AI execution time:** 1-2 minutes for ID generation, template population, and file operations
