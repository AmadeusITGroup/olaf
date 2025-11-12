---
name: work-on-job
description: Guide the process of working on an existing job by identifying the job, executing tasks, tracking progress, updating documentation, and maintaining the job status.
tags: [job-management, workflow, task-tracking, documentation]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **job_id**: string - (Optional) ID of the job to work on
- **subtask**: string - (Optional) Specific subtask to execute
- **action**: enum[continue,pause,complete] - (Optional) Action to take (default: continue)
- **priority**: enum[low,medium,high,critical] - (Optional) Priority level for the job

## Process

1. **Job Initialization**:
   - Load job details
   - Verify job status
   - Check dependencies
   - Review task list

2. **Task Execution**:
   - Identify next action
   - Execute subtasks
   - Track time and resources
   - Document progress

3. **Status Updates**:
   - Record completion
   - Update documentation
   - Notify stakeholders
   - Adjust priorities if needed

4. **Quality Assurance**:
   - Verify task completion
   - Validate outputs
   - Run tests if applicable
   - Get sign-off if required

## Output/Result Format
- Job status update in markdown
- Updated task list
- Time tracking summary
- Next steps

## Output to USER
1. **Current Status**:
   - Job overview
   - Completed tasks
   - Pending items
   - Blockers if any

2. **Next Actions**:
   - Recommended next steps
   - Priority tasks
   - Dependencies

3. **Documentation**:
   - Updated job file
   - Changelog entries
   - Reference links

## Domain-Specific Rules
- Rule 1: Maintain job state consistency
- Rule 2: Document all changes
- Rule 3: Follow defined workflows
- Rule 4: Update all stakeholders
- Rule 5: Preserve job history

## Required Actions
1. Load job details
2. Execute current task
3. Update documentation
4. Verify completion
5. Plan next steps

⚠️ **Critical Notes**
- Never delete job history
- Always verify before marking complete
- Include relevant context in updates
- Follow security protocols
- Backup work regularly
