---
name: orchestrator-prerequisite-workflow
description: Master/orchestrator workflow that coordinates prerequisite demand analysis and change request generation (Prerequisite-0 → Prerequisite-1 → Prerequisite-2)
tags: [workflow, orchestrator, prerequisite, demand-analysis, change-request, coordination]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## orchestrator-prerequisite-workflow: Demand Document Analysis Orchestrator Workflow

> Note: All files referenced below are either prompts located in `[id:prompts_dir]` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

## Template Variables
- `[WORKFLOW_NAME]`: orchestrator-prerequisite-workflow
- `[WORKFLOW_DESCRIPTION]`: Analyze demand folder and generate structured change request
- `[SUB_WORKFLOW_NAME]`: Git Branch Setup | Demand Analysis | Change Request Generation
- `[sub-workflow-file]`: treat-change-request/workflows/prerequisite/workflow-prerequisite-0-git-branch-setup | treat-change-request/workflows/prerequisite/workflow-prerequisite-1-demand-analysis | treat-change-request/workflows/prerequisite/workflow-prerequisite-2-change-request-generation
- `[descriptive-orchestrator-log-name]`: prerequisite-orchestrator-execution-log
- `[descriptive-final-output-name]`: prerequisite-final-output
- `[sub-workflow-output-file]`: prerequisite-0-branch-setup.md | prerequisite-1-demand-inventory.md | prerequisite-2-extracted-information.md | prerequisite-3-change-request.md
- `[orchestrator-state-name]`: orchestrator-prerequisite-state
- `[unique-execution-id]`: prerequisite-[timestamp]
- `[transformation-description]`: Extract and transform document contents into structured change request while preserving literal fidelity

## Workflow Type
Master/Orchestrator - Chains and coordinates complete sub-workflows and prompts in sequence

## Workflow Overview
Executes three sub-workflows to prepare prerequisites:
1) Validate and set up Git branch.
2) Gather and analyze demand documents from a folder (inventory + literal extraction).
3) Generate a structured change request with Epic, Features, and User Stories when available.

## Prerequisites
- Demand Folder Path provided and accessible
- Optional MCP server access (JIRA/Confluence/GitHub) available if needed
- Repository access for branch operations

## Input Requirements
- Primary Input: Demand Folder Path; optional MCP server access; optional Requestor
- Configuration Input: Output directory under `[id:findings_dir]`
- Input Format: Markdown/YAML artifacts for outputs; JSON for orchestrator state/log

## Output Specifications
- Orchestrator Log: `prerequisite-orchestrator-execution-log.json`
- Final Consolidated Output: `prerequisite-final-output.json`
- Sub-workflow Outputs:
  - `prerequisite-0-branch-setup.md`
  - `prerequisite-1-demand-inventory.md`
  - `prerequisite-2-extracted-information.md`
  - `prerequisite-3-change-request.md`
- Tracking File: `prerequisite-tracking.md`
- Output Location: `[id:findings_dir]`

## Sub-Workflow Chain

### Sub-Workflow 1: Git Branch Setup (Prerequisite-0)
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/prerequisite/workflow-prerequisite-0-git-branch-setup.md`
- Input Requirements:
  - Primary: Current git repository state
- Output Produced: `prerequisite-0-branch-setup.md`
- Description: Validate git state and ensure work proceeds on a non-main branch
- Success Criteria: `prerequisite-0-branch-setup.md` exists and branch validation succeeds
- Failure Handling: Report and pause; request corrective action to establish proper branch

### Sub-Workflow 2: Demand Analysis (Prerequisite-1)
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/prerequisite/workflow-prerequisite-1-demand-analysis.md`
- Input Requirements:
  - Primary: Demand folder path; optional MCP server access
  - From Previous: Confirmation that git branch is valid
- Output Produced: `prerequisite-1-demand-inventory.md`, `prerequisite-2-extracted-information.md`
- Description: Inventory all documents and extract all literal information with no omissions or inventions
- Success Criteria: All documents scanned; all extractable information captured
- Failure Handling: If folder not found or empty, stop and report; if unreadable docs, list and proceed with readable

### Sub-Workflow 3: Change Request Generation (Prerequisite-2)
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/prerequisite/workflow-prerequisite-2-change-request-generation.md`
- Input Requirements:
  - Primary: Artifacts from Demand Analysis
- Output Produced: `prerequisite-3-change-request.md`
- Description: Structure a change request (Epic, Features, User Stories) when information is available
- Success Criteria: Change request generated per available information; no invention or interpretation
- Failure Handling: If information incomplete, mark sections as [Not Provided]; do not invent; proceed with what is available

## Data Flow Between Sub-Workflows

### Input/Output Chain
```
[Demand Folder Path]
    ↓
[Git Branch Setup] → prerequisite-0-branch-setup.md
    ↓
[Demand Analysis] → prerequisite-1-demand-inventory.md + prerequisite-2-extracted-information.md
    ↓
[Change Request Generation] → prerequisite-3-change-request.md
    ↓
[Consolidated Final Output]
```

### Data Transformation Points
- Between Demand Analysis & Change Request Generation: Map extracted information to structured sections (Epic/Features/User Stories) when present; otherwise retain flat extraction
- Final Consolidation: Combine inventory, extracted info, and structured change request into final outputs and log

## Orchestrator Control Logic

### Execution Flow
```
1. VALIDATE orchestrator prerequisites (folder path exists; repo state ok)
2. PREPARE inputs for Git Branch Setup
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
- All sub-workflow files exist in `[id:prompts_dir]treat-change-request/workflows/prerequisite/`
- Sub-workflow chain is Prerequisite-0 → Prerequisite-1 → Prerequisite-2
- Data flow between sub-workflows is compatible and traceable
- State management/log files are structured in JSON
- Error recovery strategies defined per sub-workflow
- No circular dependencies between sub-workflows

### Error Recovery Strategy
- Sub-Workflow Failure: Pause orchestrator, capture error context in log, request correction, allow resume
- Chain Interruption: Resume from last successful sub-workflow using state file
- Data Corruption: Re-generate affected outputs from prior validated step; maintain backups
- Rollback Capability: Keep intermediate artifacts; rollback by reverting to prior validated state

## Progress Tracking

### Orchestrator State File: `orchestrator-prerequisite-state.json`
```json
{
  "orchestrator_name": "orchestrator-prerequisite-workflow",
  "execution_id": "prerequisite-[timestamp]",
  "start_time": "2025-07-28T14:00:00Z",
  "current_status": "running|paused|completed|failed",
  "completed_sub_workflows": [
    {
      "name": "git-branch-setup",
      "status": "completed",
      "output": "prerequisite-0-branch-setup.md",
      "completion_time": "2025-07-28T14:10:00Z"
    }
  ],
  "current_sub_workflow": {
    "name": "demand-analysis",
    "status": "running",
    "start_time": "2025-07-28T14:10:00Z"
  },
  "pending_sub_workflows": [
    "change-request-generation"
  ],
  "overall_progress": {
    "completed": 1,
    "total": 3,
    "percentage": 33
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
    "demand-analysis": {
      "sources": ["demand_folder_path"],
      "transformations": ["inventory-documents", "extract-literal-information"]
    },
    "change-request-generation": {
      "sources": ["demand-analysis.outputs"],
      "transformations": ["map-extraction-to-structure"]
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
        "execution_summary": "from orchestrator-prerequisite-state.json",
        "sub_workflow_results": "summary of each sub-workflow"
      },
      "consolidated_data": {
        "primary_results": "structured change request + inventory + extraction",
        "secondary_data": "notes on MCP usage and exceptions"
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
- Start Execution: "This orchestrator will execute 3 sub-workflows in sequence. Proceed?"
- Critical Checkpoints: Folder/path validation; Extraction completeness confirmation; Change request structure confirmation
- Sub-Workflow Failures: "Sub-workflow [X] failed. Continue/Retry/Abort?"

### Progress Reporting
- Status Updates: After each sub-workflow completion
- Milestone Notifications: Branch validated; Demand analyzed; Change request generated
- Completion Summary: Final orchestrator execution summary

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
- [ ] All three sub-workflows in chain completed
- [ ] Final consolidated output validated
- [ ] Orchestrator execution log complete
- [ ] No unresolved errors or warnings

## Principles
- No Omission | No Invention | No Interpretation | No Assumptions | Structure When Possible

## Next Steps
- Review the generated change request document for completeness
- Supplement missing information if needed
- Route to `Orchestrator-0-Router` for sizing and workflow assignment
- Optional: Update demand folder with generated artifacts for traceability
