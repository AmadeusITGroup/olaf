---
name: workflow-template-orchestrator
description: Template for creating master/orchestrator workflows that coordinate and chain multiple sub-workflows in sequence
tags: [template, workflow, orchestrator, master, coordination, chaining]
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

# Master/Orchestrator Workflow Template

> **Note:** All files referenced below are either prompts located in `[id:competencies_dir][competency]/prompts/` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

# [WORKFLOW_NAME]: [WORKFLOW_DESCRIPTION]

## Template Variables
- `[WORKFLOW_NAME]`: Name of the orchestrator workflow (kebab-case)
- `[WORKFLOW_DESCRIPTION]`: Brief description of orchestrator purpose
- `[SUB_WORKFLOW_NAME]`: Names of each sub-workflow in the chain
- `[sub-workflow-file]`: Names of sub-workflow files without extension
- `[descriptive-orchestrator-log-name]`: Name for orchestrator execution log
- `[descriptive-final-output-name]`: Name for final consolidated output
- `[sub-workflow-output-file]`: Names of individual sub-workflow outputs
- `[orchestrator-state-name]`: Name for orchestrator state tracking file
- `[unique-execution-id]`: Unique identifier for orchestrator execution
- `[transformation-description]`: Description of data transformations between workflows

## Workflow Type
Master/Orchestrator - Chains and coordinates complete sub-workflows and prompts in sequence

## Workflow Overview
[Brief description of what this orchestrator accomplishes by coordinating sub-workflows]

## Prerequisites
- [List any required conditions before starting]
- [Dependencies on external systems or configurations]

## Input Requirements
- **Primary Input:** [Description of main input to the orchestrator]
- **Configuration Input:** [Any orchestrator-level configuration]
- **Input Format:** [File format and structure expected]

## Output Specifications
- **Orchestrator Log:** `[descriptive-orchestrator-log-name].json`
- **Final Consolidated Output:** `[descriptive-final-output-name].json`
- **Sub-workflow Outputs:** [List of outputs from each sub-workflow]
- **Output Location:** [id:findings_dir]

## Sub-Workflow Chain

### Sub-Workflow 1: [SUB_WORKFLOW_NAME]
- **Type:** `Sequential|Iterative|Decision|Orchestrator`
- **Prompt/Workflow:** `[id:competencies_dir][competency]/prompts/[sub-workflow-file].md`
- **Input Requirements:**
  - Primary: [What this sub-workflow needs to start]
  - From Previous: [Any inputs from orchestrator or previous sub-workflows]
- **Output Produced:** `[sub-workflow-output-file].json`
- **Description:** [What this sub-workflow accomplishes]
- **Success Criteria:** [How to validate this sub-workflow completed successfully]
- **Failure Handling:** [What to do if this sub-workflow fails]

### Sub-Workflow 2: [SUB_WORKFLOW_NAME]
- **Type:** `Sequential|Iterative|Decision|Orchestrator`
- **Prompt/Workflow:** `[id:competencies_dir][competency]/prompts/[sub-workflow-file].md`
- **Input Requirements:**
  - Primary: Output from Sub-Workflow 1 (`[previous-output-file].json`)
  - Additional: [Any additional inputs needed]
- **Output Produced:** `[sub-workflow-output-file].json`
- **Description:** [What this sub-workflow accomplishes]
- **Success Criteria:** [How to validate this sub-workflow completed successfully]
- **Failure Handling:** [What to do if this sub-workflow fails]

### Sub-Workflow N: [SUB_WORKFLOW_NAME]
- **Type:** `Sequential|Iterative|Decision|Orchestrator`
- **Prompt/Workflow:** `[id:competencies_dir][competency]/prompts/[sub-workflow-file].md`
- **Input Requirements:**
  - Primary: Outputs from previous sub-workflows
  - Consolidated: [Any consolidated inputs from multiple previous outputs]
- **Output Produced:** `[final-sub-workflow-output].json`
- **Description:** [What this final sub-workflow accomplishes]
- **Success Criteria:** [How to validate final sub-workflow completed successfully]
- **Failure Handling:** [What to do if this sub-workflow fails]

## Data Flow Between Sub-Workflows

### Input/Output Chain
```
[Orchestrator Input] 
    ↓
[Sub-Workflow 1] → [Output 1]
    ↓
[Sub-Workflow 2] → [Output 1] + [Output 2]
    ↓
[Sub-Workflow N] → [All Previous Outputs] + [Final Output]
    ↓
[Consolidated Final Output]
```

### Data Transformation Points
- **Between Sub-Workflow 1 & 2:** [How output 1 is transformed/prepared for input to 2]
- **Between Sub-Workflow 2 & 3:** [How outputs 1+2 are consolidated for input to 3]
- **Final Consolidation:** [How all outputs are combined into final result]

## Orchestrator Control Logic

### Execution Flow
```
1. VALIDATE orchestrator prerequisites
2. PREPARE initial inputs for first sub-workflow
3. FOR each sub-workflow in chain:
   a. VALIDATE sub-workflow prerequisites 
   b. PREPARE sub-workflow inputs from previous outputs
   c. EXECUTE sub-workflow
   d. VALIDATE sub-workflow completion
   e. LOG sub-workflow results
   f. PREPARE outputs for next sub-workflow
4. CONSOLIDATE all sub-workflow outputs
5. GENERATE final orchestrator output
```

## Template Validation
- All `[id:...]` references must exist in memory map
- All sub-workflow files must exist in `[id:competencies_dir][competency]/prompts/`
- Sub-workflow chain must be logically ordered
- Data flow between sub-workflows must be compatible
- State management files must be properly structured
- Error recovery strategies must be defined for each sub-workflow
- Input/output transformations must be clearly specified
- No circular dependencies between sub-workflows

### Error Recovery Strategy
- **Sub-Workflow Failure:** [Strategy for handling individual sub-workflow failures]
- **Chain Interruption:** [How to resume from partial completion]
- **Data Corruption:** [How to recover from corrupted intermediate outputs]
- **Rollback Capability:** [Whether/how to rollback completed sub-workflows]

## Progress Tracking

### Orchestrator State File: `[orchestrator-state-name].json`
```json
{
  "orchestrator_name": "[WORKFLOW_NAME]",
  "execution_id": "[unique-execution-id]",
  "start_time": "2025-07-28T14:00:00Z",
  "current_status": "running|paused|completed|failed",
  "completed_sub_workflows": [
    {
      "name": "[sub-workflow-1]",
      "status": "completed",
      "output_file": "[output-file].json",
      "completion_time": "2025-07-28T14:15:00Z"
    }
  ],
  "current_sub_workflow": {
    "name": "[sub-workflow-2]",
    "status": "running",
    "start_time": "2025-07-28T14:15:00Z"
  },
  "pending_sub_workflows": [
    "[sub-workflow-3]",
    "[sub-workflow-n]"
  ],
  "overall_progress": {
    "completed": 1,
    "total": 4,
    "percentage": 25
  }
}
```

## Sub-Workflow Coordination

### Input Preparation Logic
```json
{
  "input_preparation_rules": {
    "[sub-workflow-1]": {
      "sources": ["orchestrator_input"],
      "transformations": ["[transformation-description]"]
    },
    "[sub-workflow-2]": {
      "sources": ["[sub-workflow-1].output", "orchestrator_input"],
      "transformations": ["[merge-logic]", "[format-conversion]"]
    },
    "[sub-workflow-n]": {
      "sources": ["all_previous_outputs"],
      "transformations": ["[consolidation-logic]"]
    }
  }
}
```

### Output Consolidation Logic
```json
{
  "consolidation_rules": {
    "final_output_structure": {
      "orchestrator_metadata": {
        "execution_summary": "from orchestrator_state.json",
        "sub_workflow_results": "summary of each sub-workflow"
      },
      "consolidated_data": {
        "primary_results": "merged from all sub-workflow outputs",
        "secondary_data": "additional consolidated information"
      },
      "validation_results": {
        "overall_success": "boolean",
        "sub_workflow_successes": "array of individual results"
      }
    }
  }
}
```

## User Interaction Points

### Orchestrator-Level Approvals
- **Start Execution:** "This orchestrator will execute [N] sub-workflows in sequence. Proceed?"
- **Critical Checkpoints:** [List any points where user approval is required]
- **Sub-Workflow Failures:** "Sub-workflow [X] failed. [Continue/Retry/Abort]?"

### Progress Reporting
- **Status Updates:** Regular progress reports after each sub-workflow completion
- **Milestone Notifications:** Key achievement notifications
- **Completion Summary:** Final orchestrator execution summary

## Validation and Completion

### Sub-Workflow Validation
- [ ] Each sub-workflow completed successfully
- [ ] All sub-workflow outputs generated and validated
- [ ] No critical errors in sub-workflow chain

### Orchestrator Validation  
- [ ] All sub-workflows executed in correct sequence
- [ ] Data flow between sub-workflows successful
- [ ] Final consolidated output generated
- [ ] Orchestrator state properly maintained
- [ ] All intermediate files preserved for audit

### Completion Criteria
- [ ] All sub-workflows in chain completed
- [ ] Final consolidated output validated
- [ ] Orchestrator execution log complete
- [ ] No unresolved errors or warnings

## Common Error Patterns
- **Sub-workflow not found:** Verify all sub-workflow files exist in `[id:competencies_dir][competency]/prompts/`
- **Invalid sub-workflow type:** Ensure sub-workflow types are correctly specified
- **Data transformation failures:** Check input/output compatibility between sub-workflows
- **State file corruption:** Implement backup and recovery for orchestrator state
- **Sub-workflow execution timeouts:** Handle long-running sub-workflows appropriately
- **Permission errors:** Check file access rights for all input/output files
- **Invalid memory map ID:** Check all references exist in memory map file
- **Circular dependencies:** Ensure sub-workflow chain has no loops
- **Incomplete consolidation:** Verify all sub-workflow outputs are properly merged
- **Resource exhaustion:** Monitor system resources during orchestrator execution

## Next Steps
- [What happens after this orchestrator completes]
- [Which higher-level orchestrator or process this feeds into]
- [Any cleanup or archival procedures required]

## Example Usage
```
INPUT: [orchestrator-input].json
EXECUTE: Sub-Workflow 1 → Sub-Workflow 2 → ... → Sub-Workflow N
OUTPUT: [consolidated-final-output].json + individual sub-workflow outputs
LOG: [orchestrator-execution-log].json
```
