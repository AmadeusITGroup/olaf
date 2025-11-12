# Generate Tasklist: Step-by-Step Tutorial

**How to Execute the "Generate Tasklist" Competency**

This tutorial shows exactly how to generate structured tasklists with iteration-task-subtask hierarchy and status tracking for project planning.

## Prerequisites

- OLAF framework loaded and active
- Clear understanding of project goals and scope
- Tasklist template available
- Knowledge of iteration planning (if using multiple iterations)

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Initiate the tasklist generation process.

**User Action:**
1. Type: `olaf generate tasklist`
2. Or use any alias: `olaf create tasks`, `olaf task list`, `olaf generate todos`
3. Press Enter to start the process

**AI Response:**
The AI will acknowledge the request and begin gathering requirements using the Propose-Act protocol.

### Step 2: Define Project Purpose
**AI Asks:** "What is the purpose of this tasklist?"

**User Action:** Provide clear project description

**Example Response:**
```
Purpose: Implement OAuth 2.0 authentication system for the web application
```

**What This Defines:**
- Overall project goal
- Scope boundaries
- Success criteria context

### Step 3: Choose Iteration Type
**AI Asks:** "Single or multiple iterations?"

**User Action:** Select iteration structure

**Options:**
- **single**: One iteration with all tasks (simple projects)
- **multiple**: Multiple iterations/sprints (complex projects)

**Example Response:**
```
Iteration Type: multiple
```

### Step 4: Define Iterations (if multiple)
**AI Asks:** "Please list iteration names/descriptions"

**User Action:** Provide iteration breakdown

**Example Response:**
```
Iterations:
1. Foundation - Set up authentication infrastructure
2. Implementation - Build OAuth 2.0 flows
3. Integration - Connect with existing systems
4. Testing & Deployment - QA and production release
```

**Constraints:**
- Maximum 7 iterations recommended
- Each iteration should have clear deliverable

### Step 5: Identify Major Tasks
**AI Asks:** "What are the major tasks for each iteration?"

**User Action:** List high-level tasks per iteration

**Example Response:**
```
Iteration 1 - Foundation:
- Set up OAuth 2.0 provider configuration
- Create database schema for tokens
- Implement security middleware

Iteration 2 - Implementation:
- Build authorization endpoint
- Build token endpoint
- Implement PKCE flow
```

**Constraints:**
- Maximum 7 tasks per iteration
- Each task can have up to 7 subtasks

### Step 6: Tasklist Structure Generation
**What AI Does:**
1. Loads tasklist template from competency pack
2. Applies iteration-task-subtask hierarchy
3. Assigns status prefixes (todo, wip, done, dump)
4. Formats with proper markdown structure
5. Adds metadata and tracking fields

**Template Structure Applied:**
```markdown
# Project: [Purpose]

## Iteration 1: [Name]
- [ ] todo Task 1: [Description]
  - [ ] todo Subtask 1.1: [Details]
  - [ ] todo Subtask 1.2: [Details]
- [ ] todo Task 2: [Description]
```

**Status Prefixes:**
- `todo`: Not started
- `wip`: Work in progress
- `done`: Completed
- `dump`: Deprioritized/cancelled

### Step 7: Review and Amend
**AI Presents:** Complete proposed tasklist structure

**User Action:** Review and request modifications

**Review Options:**
1. **Accept as-is**: "Looks good, approved"
2. **Request changes**: "Add subtask for error handling under Task 2"
3. **Restructure**: "Move Task 3 to Iteration 2"

**AI Response:**
Applies requested modifications and presents updated version for re-review.

### Step 8: Finalization
**What AI Does:**
- Saves finalized tasklist to specified location
- Adds metadata (creation date, author, version)
- Creates changelog entry documenting tasklist creation
- Provides file location and summary

**You Should See:** 
Confirmation with tasklist file location and structure summary.

## Verification Checklist

✅ **Project purpose clearly defined** at top of tasklist
✅ **Iteration structure appropriate** for project complexity
✅ **Tasks follow hierarchy** (iteration → task → subtask)
✅ **Status prefixes applied** to all items
✅ **Constraints respected** (max 7 tasks/iteration, max 7 subtasks/task)
✅ **Template structure followed** exactly
✅ **Markdown formatting correct** with proper checkboxes

## Troubleshooting

**If tasklist seems too complex:**
- Break down into smaller iterations
- Reduce number of subtasks per task
- Consider single iteration for simpler projects

**If tasks are too vague:**
- Add more specific subtasks with actionable details
- Include acceptance criteria in task descriptions
- Reference related documentation or requirements

**If hierarchy is confusing:**
```markdown
Correct Structure:
## Iteration (Level 1)
- [ ] Task (Level 2)
  - [ ] Subtask (Level 3)

Incorrect:
- [ ] Task
    - [ ] Subtask (too much indentation)
```

**If template not found:**
Verify template exists at: `olaf-core/competencies/project-manager/templates/tasklist-template.md`

## Key Learning Points

1. **Hierarchical Planning**: The iteration-task-subtask structure provides clear organization from high-level goals to specific actions.

2. **Constraint-Based Design**: Limiting tasks and subtasks (max 7 each) forces prioritization and prevents overwhelming complexity.

3. **Status Tracking**: Using prefixes (todo, wip, done, dump) enables quick visual scanning of progress.

4. **Iterative Refinement**: The review-and-amend process ensures the tasklist meets actual project needs before finalization.

## Next Steps to Try

- Create job records for high-priority tasks using create-job
- Link tasklist items to decision records
- Update task statuses as work progresses
- Generate progress reports from tasklist status
- Use tasklist as input for sprint planning

## Expected Timeline

- **Total process time:** 10-20 minutes
- **User input required:** 8-15 minutes for defining purpose, iterations, and tasks
- **AI execution time:** 2-5 minutes for structure generation and formatting
- **Review cycles:** 1-3 iterations typically needed for finalization
