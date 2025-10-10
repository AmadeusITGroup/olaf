---
name: orchestrator-0-router-workflow
description: Master/orchestrator workflow that coordinates the Change Router (Orchestrator 0) sub-workflows 0-0 → 0-1 → 0-2 → 0-3
tags: [workflow, orchestrator, change-router, coordination, chaining]
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

# orchestrator-0-router-workflow: Change Router Orchestrator Workflow

> Note: All files referenced below are either prompts located in `[id:prompts_dir]` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

## Template Variables
- `[WORKFLOW_NAME]`: orchestrator-0-router-workflow
- `[WORKFLOW_DESCRIPTION]`: Change Router Orchestrator (entry point for all change requests)
- `[SUB_WORKFLOW_NAME]`: Git Branch Setup | Information Gathering | Size Evaluation | Routing & Dispatch
- `[sub-workflow-file]`: treat-change-request/workflows/router/workflow-0-0-git-branch-setup | treat-change-request/workflows/router/workflow-0-1-information-gathering | treat-change-request/workflows/router/workflow-0-2-size-evaluation | treat-change-request/workflows/router/workflow-0-3-routing-dispatch
- `[descriptive-orchestrator-log-name]`: router-execution-log
- `[descriptive-final-output-name]`: router-final-output
- `[sub-workflow-output-file]`: 0-branch-setup.md | 2-technical-scope-analysis.md | 3-risk-assessment.md | 4-size-evaluation-matrix.md | 5-final-size-decision.md | 6-context-package.yaml | 7-routing-summary.md | README.md
- `[orchestrator-state-name]`: orchestrator-0-router-state
- `[unique-execution-id]`: router-[timestamp]
- `[transformation-description]`: Prepare previous outputs as inputs to subsequent steps (validation, mapping, consolidation)

## Workflow Type
Master/Orchestrator - Chains and coordinates complete sub-workflows and prompts in sequence

## Workflow Overview
Entry point for all change requests. Executes four sub-workflows in sequence to:
1) Validate and set up Git branch.
2) Gather comprehensive change information and validate prerequisites.
3) Evaluate change size using defined matrices.
4) Route to an appropriate target orchestrator and prepare a handoff context package.

## Prerequisites
- `prerequisite-3-change-request.md` exists and is complete (Epic, Features, MVP, Open Questions)
- Access to the repository with a non-main working branch
- Availability of request metadata: Issue IDs, Requestor, Priority, Target Date (optional), Initial Context (optional)

## Input Requirements
- Primary Input: Change request metadata and analysis directory path
- Configuration Input: Orchestrator-level settings (e.g., output directory under `[id:findings_dir]`)
- Input Format: Markdown/YAML artifacts as specified per sub-workflow, JSON for orchestrator state/log

## Output Specifications
- Orchestrator Log: `router-execution-log.json`
- Final Consolidated Output: `router-final-output.json`
- Sub-workflow Outputs:
  - `0-branch-setup.md`
  - `2-technical-scope-analysis.md`
  - `3-risk-assessment.md`
  - `4-size-evaluation-matrix.md`
  - `5-final-size-decision.md`
  - `6-context-package.yaml`
  - `7-routing-summary.md`
  - `README.md`
- Output Location: `[id:findings_dir]`

## Sub-Workflow Chain

### Sub-Workflow 1: Git Branch Setup
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/router/workflow-0-0-git-branch-setup.md`
- Input Requirements:
  - Primary: Current git repository state
  - From Previous: Orchestrator inputs (change request metadata)
- Output Produced: `0-branch-setup.md`
- Description: Validate git state and ensure work proceeds on a non-main branch
- Success Criteria: `0-branch-setup.md` exists and branch validation succeeds
- Failure Handling: Report and stop orchestrator; request corrective action to establish proper branch

### Sub-Workflow 2: Information Gathering
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/router/workflow-0-1-information-gathering.md`
- Input Requirements:
  - Primary: Analysis directory path
  - From Previous: Confirmation that git branch is valid; prerequisite file presence check
- Output Produced: `2-technical-scope-analysis.md`, `3-risk-assessment.md`
- Description: Validate `prerequisite-3-change-request.md` and create router-specific analyses
- Success Criteria: Prerequisite validated AND both router-specific files created
- Failure Handling: Stop orchestrator and notify requestor if prerequisites are incomplete

### Sub-Workflow 3: Size Evaluation
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/router/workflow-0-2-size-evaluation.md`
- Input Requirements:
  - Primary: Outputs from Information Gathering
  - Additional: Any sizing matrices or criteria configured
- Output Produced: `4-size-evaluation-matrix.md`, `5-final-size-decision.md`
- Description: Determine XL/L/M/S/XS classification with documented rationale
- Success Criteria: Both files exist and size is explicitly stated
- Failure Handling: Request additional data or re-assessment; do not proceed to routing until complete

### Sub-Workflow 4: Routing & Dispatch
- Type: Decision/Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/router/workflow-0-3-routing-dispatch.md`
- Input Requirements:
  - Primary: Artifacts from Sub-Workflows 2 and 3
  - Additional: Routing criteria and target orchestrator mapping
- Output Produced: `6-context-package.yaml`, `7-routing-summary.md`, `README.md`
- Description: Identify target orchestrator and prepare context package for handoff
- Success Criteria: All 3 files exist and target orchestrator is clearly identified
- Failure Handling: If no clear route, document rationale and return to requestor; pause orchestrator

## Data Flow Between Sub-Workflows

### Input/Output Chain
```
[Orchestrator Input]
    ↓
[Git Branch Setup] → 0-branch-setup.md
    ↓
[Information Gathering] → 2-technical-scope-analysis.md + 3-risk-assessment.md
    ↓
[Size Evaluation] → 4-size-evaluation-matrix.md + 5-final-size-decision.md
    ↓
[Routing & Dispatch] → 6-context-package.yaml + 7-routing-summary.md + README.md
    ↓
[Consolidated Final Output]
```

### Data Transformation Points
- Between Git Branch Setup & Information Gathering: Validate branch; ensure analysis directory is prepared
- Between Information Gathering & Size Evaluation: Use router-specific analyses as inputs to sizing
- Final Consolidation: Combine size decision and routing summary into final orchestrator log and output

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
- All sub-workflow files exist in `[id:prompts_dir]treat-change-request/workflows/router/`
- Sub-workflow chain is logically ordered (0-0 → 0-1 → 0-2 → 0-3)
- Data flow between sub-workflows is compatible
- State management/log files are structured in JSON
- Error recovery strategies defined per sub-workflow
- No circular dependencies between sub-workflows

### Error Recovery Strategy
- Sub-Workflow Failure: Pause orchestrator, capture error context in log, request correction, allow resume
- Chain Interruption: Resume from last successful sub-workflow using state file
- Data Corruption: Re-generate affected outputs from prior valid step; maintain backups
- Rollback Capability: Keep intermediate artifacts; rollback by reverting to prior validated state

## Progress Tracking

### Orchestrator State File: `orchestrator-0-router-state.json`
```json
{
  "orchestrator_name": "orchestrator-0-router-workflow",
  "execution_id": "router-[timestamp]",
  "start_time": "2025-07-28T14:00:00Z",
  "current_status": "running|paused|completed|failed",
  "completed_sub_workflows": [
    {
      "name": "git-branch-setup",
      "status": "completed",
      "output_file": "0-branch-setup.md",
      "completion_time": "2025-07-28T14:15:00Z"
    }
  ],
  "current_sub_workflow": {
    "name": "information-gathering",
    "status": "running",
    "start_time": "2025-07-28T14:15:00Z"
  },
  "pending_sub_workflows": [
    "size-evaluation",
    "routing-dispatch"
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
    "git-branch-setup": {
      "sources": ["orchestrator_input"],
      "transformations": ["validate-git-state"]
    },
    "information-gathering": {
      "sources": ["git-branch-setup.output", "orchestrator_input"],
      "transformations": ["prepare-analysis-dir", "validate-prerequisite-3"]
    },
    "size-evaluation": {
      "sources": ["information-gathering.outputs"],
      "transformations": ["map-analysis-to-sizing-matrix"]
    },
    "routing-dispatch": {
      "sources": ["size-evaluation.outputs", "information-gathering.outputs"],
      "transformations": ["compose-context-package", "determine-target-orchestrator"]
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
        "execution_summary": "from orchestrator-0-router-state.json",
        "sub_workflow_results": "summary of each sub-workflow"
      },
      "consolidated_data": {
        "primary_results": "size decision + routing summary",
        "secondary_data": "technical scope and risk analysis references"
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
- Start Execution: "This orchestrator will execute 4 sub-workflows in sequence. Proceed?"
- Critical Checkpoints: After each sub-workflow completion if validation fails or requires human approval
- Sub-Workflow Failures: "Sub-workflow [X] failed. Continue/Retry/Abort?"

### Progress Reporting
- Status Updates: Report after each sub-workflow completion
- Milestone Notifications: Branch validated; prerequisites validated; size determined; route selected
- Completion Summary: Final execution summary with links to all produced artifacts

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

## Next Steps
- Invoke the target orchestrator identified in `7-routing-summary.md` with `6-context-package.yaml`
- Team begins work following the target orchestrator workflows
- Optional: Set up escalation monitoring for re-sizing detection
- Optional: Update router metrics for continuous improvement
