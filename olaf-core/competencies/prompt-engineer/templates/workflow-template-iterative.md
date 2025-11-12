---
name: workflow-template-iterative
description: Template for creating iterative workflows that repeat until completion criteria are met with user authorization
tags: [template, workflow, iterative, automation, state-management]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

Use terminal commands, not training data.

# Iterative Workflow Template

> **Note:** All files referenced below are either prompts located in `[id:competencies_dir][competency]/prompts/` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

# [WORKFLOW_NAME]: [WORKFLOW_DESCRIPTION]

## Template Variables
- `[WORKFLOW_NAME]`: Name of the workflow (kebab-case)
- `[WORKFLOW_DESCRIPTION]`: Brief description of workflow purpose
- `[STEP_NAME]`: Name of the iteration step
- `[prompt-file-name]`: Name of prompt file without extension
- `[tool-name]`: Name of tool/script file without extension
- `[ext]`: File extension for tools (ps1, py, sh, etc.)
- `[descriptive-iteration-state-name]`: Name for iteration state file
- `[descriptive-iteration-output-name]`: Name for iteration output file
- `[descriptive-final-output-name]`: Name for final output file
- `[descriptive-progress-tracking-name]`: Name for progress tracking file

## Workflow Type
Iterative - Repeats the same process until completion criteria are met with user authorization

## Workflow Overview
[Brief description of what this workflow accomplishes through iteration]

## Prerequisites
- [List any required conditions before starting]
- [Dependencies on other workflows or files]

## Input Requirements
- **Primary Input:** [Description of main input for first iteration]
- **Iteration State File:** `[descriptive-iteration-state-name].json`
- **Input Format:** JSON file containing iteration state and progress data

## Output Specifications
- **Iteration Output:** `[descriptive-iteration-output-name].json` (updated each iteration)
- **Final Output:** `[descriptive-final-output-name].json`
- **Progress Tracking:** `[descriptive-progress-tracking-name].json`
- **Output Location:** [id:findings_dir]

## Iteration Logic

### Iteration Step: [STEP_NAME]
- **Prompt/Tool:** `[id:competencies_dir][competency]/prompts/[prompt-file-name].md` or `[id:tools_dir][tool-name].[ext]`
- **Input:**
  - First iteration: [Initial input]
  - Subsequent iterations: Output from previous iteration + `[iteration-state-file].json`
- **Output:** `[iteration-output-file].json`
- **Description:** [What each iteration does]
- **Validation:** [How to verify iteration completion]

## Completion Criteria
```json
{
  "completion_criteria": {
    "primary_condition": "[Main condition to check]",
    "secondary_conditions": [
      "[Additional condition 1]",
      "[Additional condition 2]"
    ],
    "max_iterations": [number],
    "success_threshold": "[Measurable threshold]"
  }
}
```

## Template Validation
- All `[id:...]` references must exist in memory map
- Iteration logic must be clearly defined
- State management files must be properly structured
- Completion criteria must be measurable
- User authorization points must be clearly identified
- No infinite iteration loops allowed

## User Authorization Process

### After Each Iteration:
1. **Present Results:** Display iteration output and current progress
2. **Provide Recommendation:** 
   - **Continue:** "[Reason to continue with next iteration]"
   - **Stop:** "[Reason to stop - completion achieved]"
   - **Modify:** "[Reason to adjust approach]"
3. **Request Authorization:** "Based on the analysis, I recommend [RECOMMENDATION]. Shall I proceed?"

### Recommendation Logic:
- **Continue if:** [Conditions that suggest more iterations needed]
- **Stop if:** [Conditions that suggest completion achieved]
- **Modify if:** [Conditions that suggest approach adjustment needed]

## Data Flow Diagram
```
[Initial Input] → [Iteration 1] → [Output 1] → [User Auth] → [Iteration 2] → [Output 2] → [User Auth] → ... → [Final Output]
                     ↑                            ↑                            ↑
               [State File]              [Updated State]              [Updated State]
```

## State Management
- **State File Format:** `[iteration-state-name].json`
```json
{
  "iteration_number": 1,
  "start_time": "2025-07-28T14:00:00Z",
  "current_status": "[status]",
  "previous_outputs": [
    {
      "iteration": 1,
      "output_file": "[file-name].json",
      "timestamp": "2025-07-28T14:00:00Z"
    }
  ],
  "completion_progress": {
    "criteria_met": ["[criterion1]"],
    "criteria_pending": ["[criterion2]"],
    "progress_percentage": 65
  }
}
```

## Error Handling
- **Iteration Failure:** [What to do if an iteration fails]
- **State Recovery:** [How to recover from corrupted state]
- **Rollback:** [How to return to previous iteration]

## Common Error Patterns
- **State file corruption:** Backup and restore mechanisms needed
- **Infinite iteration loops:** Max iteration limits must be enforced
- **Tool not found:** Verify tool exists in `[id:tools_dir]`
- **Permission errors:** Check file access rights and execution permissions
- **Prompt not found:** Verify prompt exists in `[id:competencies_dir][competency]/prompts/`
- **Invalid memory map ID:** Check reference exists in memory map file
- **User authorization timeout:** Handle cases where user doesn't respond
- **Completion criteria never met:** Implement fallback mechanisms

## Completion Actions
- [ ] All completion criteria met
- [ ] Final output validated
- [ ] State file archived
- [ ] [Additional completion actions]

## Next Steps
- [What happens after this workflow completes]
- [Which workflow to execute next, if any]
