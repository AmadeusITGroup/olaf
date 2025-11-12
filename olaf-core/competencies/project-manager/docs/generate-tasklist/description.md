# Generate Tasklist

## Overview

Generates structured, hierarchical tasklists with iteration-task-subtask organization and status tracking to break down project work into manageable, trackable units.

## Purpose

Projects need clear, organized task breakdowns to coordinate work and track progress. This competency solves the problem of ad-hoc task management by creating standardized tasklists with proper hierarchy (iterations > tasks > subtasks), status tracking, and constraints that prevent overwhelming complexity while maintaining clarity.

## Usage

**Command**: `generate tasklist`

**Protocol**: Propose-Act

**When to Use**: Use this competency when starting a new project or feature, planning sprints or iterations, breaking down large work items into manageable tasks, or whenever you need a structured approach to organizing and tracking project work.

## Parameters

### Required Inputs
- **project_purpose**: Brief description of the overall goal or project objective
- **iteration_type**: Whether the project has a single iteration or multiple iterations (single | multiple)

### Optional Inputs
- **iterations_list**: Array of iteration names or descriptions (required if iteration_type is "multiple")
- **major_tasks**: Array of high-level tasks for each iteration (helps seed the tasklist generation)

### Context Requirements
- Access to tasklist template for structure and formatting
- Understanding of project scope and requirements
- Clarity on iteration boundaries and deliverables

## Output

**Deliverables**:
- Structured tasklist file with iteration-task-subtask hierarchy
- Status prefixes for tracking (todo, wip, done, dump)
- Properly formatted markdown with checkboxes and indentation
- Constraints enforced: maximum 7 tasks per iteration, maximum 7 subtasks per task

**Format**: Markdown file following the tasklist template structure with clear hierarchy, status indicators, and organized sections for each iteration.

## Examples

### Example 1: Single Iteration Feature

**Scenario**: Building a user profile feature in a single sprint

**Command**:
```
generate tasklist
```

**Input**:
```
Project Purpose: Implement user profile management feature
Iteration Type: single
Major Tasks: Database schema, API endpoints, UI components, Testing
```

**Result**: Generated tasklist with one iteration containing 4 major tasks, each broken down into 3-5 subtasks with todo status

### Example 2: Multi-Iteration Project

**Scenario**: Planning a 3-sprint project to build a reporting system

**Command**:
```
generate tasklist
```

**Input**:
```
Project Purpose: Build comprehensive analytics and reporting system
Iteration Type: multiple
Iterations List: 
  - Sprint 1: Data collection and storage
  - Sprint 2: Report generation engine
  - Sprint 3: UI and visualization
Major Tasks: [Provided for each sprint]
```

**Result**: Generated tasklist with 3 iterations, each containing up to 7 tasks with subtasks, all marked as todo

### Example 3: Refactoring Project

**Scenario**: Planning technical debt reduction work

**Command**:
```
generate tasklist
```

**Input**:
```
Project Purpose: Refactor authentication system to improve security and maintainability
Iteration Type: single
Major Tasks: Audit current implementation, Design new architecture, Implement changes, Migration strategy, Testing and validation
```

**Result**: Structured tasklist with 5 major tasks, each with detailed subtasks for the refactoring work

## Related Competencies

- **create-job**: Individual tasks from the tasklist can be converted into job records for detailed tracking
- **work-on-job**: Execute work on tasks that have been formalized as jobs
- **review-progress**: Use tasklist completion status to assess project progress
- **create-changelog-entry**: Log tasklist creation and major task completions in the changelog
- **generate-commits-from-changelog**: Task completions logged in changelog can be converted to commit messages

## Tips & Best Practices

- Start with high-level tasks and let the competency help break them down into subtasks
- Keep task descriptions clear and action-oriented (start with verbs: "Implement", "Design", "Test")
- Use the 7-task and 7-subtask limits as forcing functions to maintain appropriate granularity
- Review and refine the generated tasklist before finalizing - it's a starting point for discussion
- Update task status regularly (todo → wip → done) to maintain accurate progress visibility
- Use "dump" status for tasks that become irrelevant rather than deleting them (maintains history)
- Consider iteration boundaries carefully - they should align with natural project milestones

## Limitations

- Enforces maximum 7 tasks per iteration and 7 subtasks per task - cannot exceed these limits
- Requires clear project understanding upfront - cannot generate meaningful tasks from vague requirements
- Does not automatically estimate effort or assign resources to tasks
- Generated tasklist is a starting point - requires human review and refinement
- Does not integrate with external project management tools - tasklist is markdown-based only
- Cannot automatically update task status based on actual work completion

**Source**: `olaf-core/competencies/project-manager/prompts/generate-tasklist.md`
