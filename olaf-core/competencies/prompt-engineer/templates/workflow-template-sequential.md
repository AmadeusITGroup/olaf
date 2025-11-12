---
name: workflow-template-sequential
description: Template for creating sequential/chained workflows where each step depends on the previous step's output
tags: [template, workflow, sequential, automation, chained]
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

# Sequential/Chained Workflow Template

> **Note:** All files referenced below are either prompts located in `[id:competencies_dir][competency]/prompts/` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

# [WORKFLOW_NAME]: [WORKFLOW_DESCRIPTION]

## Template Variables
- `[WORKFLOW_NAME]`: Name of the workflow (kebab-case)
- `[WORKFLOW_DESCRIPTION]`: Brief description of workflow purpose
- `[STEP_1_NAME]`, `[STEP_2_NAME]`, `[STEP_N_NAME]`: Names of each workflow step
- `[step-1-prompt-name]`, `[step-2-prompt-name]`, `[step-n-prompt-name]`: Names of prompt files for each step (without extension)
- `[step-1-tool-name]`, `[step-2-tool-name]`, `[step-n-tool-name]`: Names of tool/script files for each step (without extension)
- `[ext]`: File extension for tools (ps1, py, sh, etc.)

## Workflow Type
Sequential/Chained - Each step depends on the output of the previous step

## Workflow Overview
[Brief description of what this workflow accomplishes]

## Prerequisites
- [List any required conditions before starting]
- [Dependencies on other workflows or files]

## Input Requirements
- **Primary Input:** [Description of main input]
- **Secondary Inputs:** [Optional additional inputs]
- **Input Format:** [File format, data structure, etc.]

## Output Specifications
- **Primary Output:** [Main output file/result]
- **Secondary Outputs:** [Additional outputs if any]
- **Output Location:** [Where outputs are stored]

## Workflow Steps

### Step 1: [STEP_1_NAME]
- **Prompt/Tool:** `[id:competencies_dir][competency]/prompts/[step-1-prompt-name].md` or `[id:tools_dir][step-1-tool-name].[ext]`
- **Input:** [What this step consumes]
- **Output:** [What this step produces]
- **Description:** [What this step does]
- **Validation:** [How to verify step completion]

### Step 2: [STEP_2_NAME]
- **Prompt/Tool:** `[id:competencies_dir][competency]/prompts/[step-2-prompt-name].md` or `[id:tools_dir][step-2-tool-name].[ext]`
- **Input:** [Output from Step 1 + any additional inputs]
- **Output:** [What this step produces]
- **Description:** [What this step does]
- **Validation:** [How to verify step completion]

### Step N: [STEP_N_NAME]
- **Prompt/Tool:** `[id:competencies_dir][competency]/prompts/[step-n-prompt-name].md` or `[id:tools_dir][step-n-tool-name].[ext]`
- **Input:** [Output from Step N-1 + any additional inputs]
- **Output:** [Final workflow output]
- **Description:** [What this step does]
- **Validation:** [How to verify step completion]

## Template Validation
- All `[id:...]` references must exist in memory map
- Step inputs/outputs must be compatible
- No circular dependencies allowed
- All referenced prompt/tool files must exist
- Step sequence must be logical and executable

## Data Flow Diagram
```
[Input] → [Step 1] → [Output 1] → [Step 2] → [Output 2] → ... → [Step N] → [Final Output]
```

## Error Handling
- **Step Failure:** [What to do if a step fails]
- **Recovery:** [How to restart from a failed step]
- **Rollback:** [How to undo partial completion]

## Common Error Patterns
- **Missing input files:** Check prerequisites and previous step outputs
- **Tool not found:** Verify tool exists in `[id:tools_dir]`
- **Permission errors:** Check file access rights and execution permissions
- **Prompt not found:** Verify prompt exists in `[id:competencies_dir][competency]/prompts/`
- **Invalid memory map ID:** Check reference exists in memory map file
- **Incompatible step inputs:** Verify output format matches next step input requirements

## Completion Criteria
- [ ] All steps completed successfully
- [ ] All outputs validated
- [ ] No critical errors encountered
- [ ] [Additional completion criteria]

## Next Steps
- [What happens after this workflow completes]
- [Which workflow to execute next, if any]
