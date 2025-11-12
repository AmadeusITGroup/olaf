# Create Job

## Overview

Creates structured job records following a standardized template with unique ID generation, proper metadata, and integration with the project's job tracking system for comprehensive work management.

## Purpose

Projects need a formal system for tracking work items beyond simple task lists. This competency solves the problem of informal work tracking by creating detailed job records that capture requirements, tasks, status, and metadata in a consistent format that enables systematic work management, progress tracking, and team coordination.

## Usage

**Command**: `create job`

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this competency when defining new work items such as user stories, bug fixes, features, refactoring efforts, or any significant work that requires formal tracking, assignment, and status management throughout its lifecycle.

## Parameters

### Required Inputs
- **job_title**: Concise, clear title describing the job's main purpose
- **job_type**: Category of work (User Story, Bug Fix, Task, Refactoring, Spike, Feature Enhancement, or Other)
- **priority**: Urgency level (High, Medium, or Low)
- **job_description**: Brief explanation of what the job aims to accomplish

### Optional Inputs
- **initial_tasks**: List of specific tasks or steps already identified for this job
- **reference_links**: URLs or references to relevant documentation, requirements, or resources
- **assignee**: Person assigned to the job (defaults to @AssigneeName if not provided)

### Context Requirements
- Access to job template for structure
- Access to jobs register (`[id:jobs]`) for ID generation and tracking
- Access to jobs directory (`[id:jobs_dir]`) for storing job files
- Current serial number from jobs register for unique ID generation

## Output

**Deliverables**:
- New job file with unique ID (format: `JOB-{serial}.md`)
- Updated jobs register with new entry and incremented serial number
- Job metadata including creation date, status, type, priority, and assignee
- Structured sections for description, tasks, progress tracking, and references

**Format**: Markdown file following the job template structure with frontmatter metadata and organized content sections.

## Examples

### Example 1: User Story

**Scenario**: Creating a job for implementing user authentication feature

**Command**:
```
create job
```

**Input**:
```
Job Title: Implement OAuth2 User Authentication
Job Type: User Story
Priority: High
Job Description: Enable users to authenticate using OAuth2 providers (Google, GitHub)
Initial Tasks:
  - Research OAuth2 libraries
  - Design authentication flow
  - Implement provider integration
  - Add user session management
  - Write integration tests
Reference Links: https://oauth.net/2/, design-doc-auth.md
Assignee: @john-developer
```

**Result**: Created `JOB-042.md` with full job details, updated register to serial 42, ready for work to begin

### Example 2: Bug Fix

**Scenario**: Tracking a critical production bug

**Command**:
```
create job
```

**Input**:
```
Job Title: Fix Memory Leak in Background Processor
Job Type: Bug Fix
Priority: High
Job Description: Resolve memory leak causing server crashes every 6 hours in production
Reference Links: issue-789, monitoring-dashboard-url
Assignee: @sarah-engineer
```

**Result**: Created `JOB-043.md` for immediate attention, high priority bug tracking

### Example 3: Technical Spike

**Scenario**: Research task for evaluating new technology

**Command**:
```
create job
```

**Input**:
```
Job Title: Evaluate GraphQL vs REST for New API
Job Type: Spike
Priority: Medium
Job Description: Research and compare GraphQL and REST approaches for the new customer API, provide recommendation
Initial Tasks:
  - Review GraphQL capabilities and ecosystem
  - Assess REST API best practices
  - Compare performance characteristics
  - Evaluate team learning curve
  - Document recommendation with rationale
Assignee: @alex-architect
```

**Result**: Created `JOB-044.md` for research and evaluation work

## Related Competencies

- **work-on-job**: Execute and track progress on the created job
- **generate-tasklist**: Generate detailed task breakdowns that can inform job creation
- **create-changelog-entry**: Log job creation and completion in the project changelog
- **review-progress**: Review job status and progress during project assessments
- **create-decision-record**: Jobs may require decisions that should be formally documented

## Tips & Best Practices

- Write clear, specific job titles that immediately convey the work's purpose
- Include enough description detail for someone unfamiliar with the context to understand the goal
- Add initial tasks if known, but don't feel obligated to have a complete task list upfront
- Set priority realistically - not everything can be high priority
- Include reference links to requirements, designs, or related documentation for context
- Use appropriate job types to enable filtering and reporting by work category
- Update the job file as work progresses rather than creating a new job for related work

## Limitations

- Requires manual input of job details - does not automatically extract from requirements or conversations
- Job IDs are sequential and cannot be customized - follows JOB-{serial} format strictly
- Does not automatically notify assignees - notification must be handled separately
- Cannot create jobs with past creation dates - always uses current timestamp
- Job register and job file must both succeed - no partial creation (atomic operation)
- Does not validate that assignee exists or has capacity for the work

**Source**: `olaf-core/competencies/project-manager/prompts/create-job.md`
