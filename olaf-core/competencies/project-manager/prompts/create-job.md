---
name: create-job-pml
description: Create a new job file in the jobs directory following the job template structure with proper ID generation and system integration
tags: [job, creation, template, project-management]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **job_title**: string - Concise description of the job (brief, clear title that describes the job's main purpose)
- **job_type**: enum - Category of job being created (User Story | Bug Fix | Task | Refactoring | Spike | Feature Enhancement | Other)
- **priority**: enum - Priority level for the job (High | Medium | Low)
- **job_description**: string - Brief description of the job's goal/objective (clear explanation of what the job aims to accomplish)
- **initial_tasks**: string - Optional list of specific tasks or steps that are already identified
- **reference_links**: string - Optional URLs or references to relevant documentation or resources
- **assignee**: string - Optional person assigned to the job (defaults to @AssigneeName if not provided)

## Process

1. **Read Template and Register**: 
   - Read file: `[id:competencies_dir][competency]/templates/project-manager/job-template.md`
   - Read file: `[id:jobs]` (jobs register at `[id:projects]jobs-register.md`)
   - Extract current serial number from register

2. **Generate Job ID**:
   - Increment serial number from job register
   - Create new job ID format: JOB-{serial}
   - Prepare filename: `JOB-{serial}.md`

3. **Populate Job Template**:
   - Use job template structure as base
   - Fill in all required sections with provided parameters:
     - Job title and description
     - Job type and priority
     - Assignee (or default to @AssigneeName)
     - Initial tasks if provided
     - Reference links if provided
   - Set creation date and status
   - Generate proper job metadata

4. **Create Job File**:
   - Write file: `[id:jobs_dir]JOB-{serial}.md`
   - Ensure proper markdown formatting and template compliance

5. **Update Job Register**:
   - Add new job entry to register at `[id:jobs]`
   - Update serial number counter
   - Save updated register file

## Output Format
Follow template structure: `[id:competencies_dir][competency]/templates/project-manager/job-template.md`

## Output to USER
- Confirmation of job creation with ID: `JOB-{serial}`
- File location: `[id:jobs_dir]JOB-{serial}.md`
- Updated job register with new entry
- Job details summary for verification
- Next phase: Begin work on the created job using `[id:competencies_dir][competency]/prompts/work-on-job-new.md` (converted prompt)

## Domain-Specific Rules
- Rule 1: Always increment serial number in job register at `[id:jobs]`
- Rule 2: Job ID must follow JOB-{serial} format exactly
- Rule 3: All required template sections must be populated
- Rule 4: Job register must be updated atomically with job creation
- Rule 5: Assignee defaults to @AssigneeName if not specified

## Required Actions
1. Read job template and current register from `[id:jobs]`
2. Generate next available job ID
3. Populate template with provided parameters
4. Create new job file in `[id:jobs_dir]`
5. Update job register at `[id:jobs]` with new entry

⚠️ **Critical Notes**
- Never create duplicate job IDs - always check register at `[id:jobs]` first
- Job register and job file creation must succeed together
- Template structure must be preserved exactly
- All metadata fields are required for proper tracking
