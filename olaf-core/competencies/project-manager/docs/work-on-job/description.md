# Work on Job

## Overview

Guides the execution of work on existing job records by loading job details, executing tasks, tracking progress, updating documentation, and maintaining accurate job status throughout the work lifecycle.

## Purpose

Once jobs are created, teams need a structured way to execute and track work. This competency solves the problem of ad-hoc work execution by providing a systematic workflow for working on jobs that ensures progress is documented, status is maintained, dependencies are checked, and all stakeholders stay informed throughout the work process.

## Usage

**Command**: `work on job`

**Protocol**: Act

**When to Use**: Use this competency when starting work on an existing job, continuing work on a job in progress, completing a job, or pausing work to document current state and next steps.

## Parameters

### Required Inputs
- None (competency will guide you through job selection)

### Optional Inputs
- **job_id**: Specific job ID to work on (e.g., JOB-042) - if not provided, competency will help you select
- **subtask**: Specific subtask within the job to execute
- **action**: What to do with the job (continue, pause, complete) - defaults to "continue"
- **priority**: Adjust priority level if needed (low, medium, high, critical)

### Context Requirements
- Access to job file in jobs directory
- Access to jobs register for status tracking
- Understanding of job dependencies and blockers
- Relevant project context and resources

## Output

**Deliverables**:
- Updated job file with current progress and status
- Task completion tracking and time estimates
- Documentation of work performed and decisions made
- Changelog entries for significant progress milestones
- Next steps and recommendations for continuing work

**Format**: Updated markdown job file with progress notes, completed task checkboxes, status changes, and timestamped updates.

## Examples

### Example 1: Starting Work on a Job

**Scenario**: Beginning work on a user authentication feature

**Command**:
```
work on job
```

**Input**:
```
Job ID: JOB-042
Action: continue
```

**Result**: Loaded job details, identified first task (research OAuth2 libraries), executed research, documented findings in job file, marked task complete, identified next task

### Example 2: Completing a Subtask

**Scenario**: Finished implementing OAuth provider integration

**Command**:
```
work on job
```

**Input**:
```
Job ID: JOB-042
Subtask: Implement provider integration
Action: continue
```

**Result**: Marked subtask complete, updated progress percentage, documented implementation details, identified next subtask (user session management)

### Example 3: Pausing Work

**Scenario**: Need to pause work due to blocker

**Command**:
```
work on job
```

**Input**:
```
Job ID: JOB-042
Action: pause
```

**Result**: Documented current state, noted blocker (waiting for API keys), updated status to "blocked", created handover notes for when work resumes

### Example 4: Completing a Job

**Scenario**: All tasks finished, ready to close job

**Command**:
```
work on job
```

**Input**:
```
Job ID: JOB-042
Action: complete
```

**Result**: Verified all tasks complete, ran final validation, updated status to "done", created changelog entry, generated completion summary

## Related Competencies

- **create-job**: Creates the job records that this competency executes
- **generate-tasklist**: Generates task structures that inform job execution
- **create-changelog-entry**: Log significant job progress and completion in changelog
- **review-progress**: Review job status across multiple jobs during progress assessments
- **prepare-conversation-handover**: Create handover documentation when pausing work on jobs

## Tips & Best Practices

- Load job details at the start of each work session to refresh context and review dependencies
- Update job files frequently as work progresses - don't wait until completion to document
- Mark tasks complete as you finish them to maintain accurate progress visibility
- Document blockers immediately when encountered so they can be addressed quickly
- Include enough detail in progress notes for someone else to continue the work if needed
- Use the pause action when switching contexts to capture current state
- Verify all acceptance criteria before marking a job complete
- Create changelog entries for major milestones, not just final completion

## Limitations

- Requires manual execution - does not automatically track work or update status
- Cannot automatically detect task completion - relies on user marking tasks done
- Does not integrate with time tracking systems - time estimates are manual
- Cannot automatically resolve dependencies or blockers - requires human intervention
- Does not enforce workflow rules - users can mark tasks complete in any order
- Job file updates are local - does not sync with external project management tools

**Source**: `olaf-core/competencies/project-manager/prompts/work-on-job.md`
