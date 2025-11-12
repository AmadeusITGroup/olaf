---
name: generate-tasklist-new
description: Generate structured tasklists with iteration-task-subtask hierarchy and status tracking
tags: [tasklist, planning, project, iteration, tasks]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **project_purpose**: string - Brief description of the overall goal or project
- **iteration_type**: single|multiple - Whether project has single or multiple iterations
- **iterations_list**: array - List of iteration names/descriptions (if multiple)
- **major_tasks**: array - High-level tasks for each iteration

## Process

1. **Gather Requirements**:
   - Ask: "What is the purpose of this tasklist?"
   - Ask: "Single or multiple iterations?"
   - If multiple: "Please list iteration names/descriptions"
   - Ask: "What are the major tasks for each iteration?"

2. **Generate Tasklist Structure**:
   - Use template: `[id:competencies_dir][competency]/templates/project-manager/tasklist-template.md`
   - Apply status prefixes: todo, wip, done, dump
   - Follow iteration-task-subtask hierarchy
   - Enforce constraints: max 7 tasks per iteration, max 7 subtasks per task

3. **Present for Review**:
   - Display proposed tasklist structure
   - Request user amendments
   - Apply modifications as requested

## Output Format
Follow template structure: `[id:competencies_dir][competency]/templates/project-manager/tasklist-template.md`

## Output to USER
- Present proposed tasklist for review
- Request amendments and modifications
- Confirm final structure
