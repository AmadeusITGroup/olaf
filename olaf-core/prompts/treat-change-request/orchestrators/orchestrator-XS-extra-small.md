<<<<<<< HEAD
---
name: orchestrator-xs-extra-small-workflow
description: Master/orchestrator workflow that coordinates the Extra Small (XS) change sub-workflows 3 → 4
tags: [workflow, orchestrator, extra-small, xs, governance, coordination]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## orchestrator-xs-extra-small-workflow: XS Changes Orchestrator Workflow

> Note: All files referenced below are either prompts located in `[id:prompts_dir]` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

## Template Variables
- `[WORKFLOW_NAME]`: orchestrator-xs-extra-small-workflow
- `[WORKFLOW_DESCRIPTION]`: Extra Small (XS) changes with minimal governance
- `[SUB_WORKFLOW_NAME]`: Planning | Implementation
- `[sub-workflow-file]`: treat-change-request/workflows/XS/workflow-3-planning | treat-change-request/workflows/XS/workflow-4-implementation
- `[descriptive-orchestrator-log-name]`: xs-orchestrator-execution-log
- `[descriptive-final-output-name]`: xs-final-output
- `[sub-workflow-output-file]`: planning artifacts | implementation artifacts
- `[orchestrator-state-name]`: orchestrator-xs-state
- `[unique-execution-id]`: xs-[timestamp]
- `[transformation-description]`: Minimal transformations with clear traceability

## Workflow Type
Master/Orchestrator - Chains and coordinates complete sub-workflows and prompts in sequence

## Workflow Overview
Handles Extra Small (XS) changes involving a single service and <2 days effort. Executes two sub-workflows (Planning → Implementation) with minimal governance and fast iteration.

## Prerequisites
- Receives context package from Orchestrator-0-Router containing issue IDs, size classification (XS), rationale, technical scope, and router artifacts
- Reviewer identified for peer review
- Repository access and team availability confirmed

## Input Requirements
- Primary Input: Context package from router (`6-context-package.yaml`) and associated artifacts
- Configuration Input: Lightweight checklists for Planning and Implementation
- Input Format: Markdown/YAML for artifacts, JSON for orchestrator state/log

## Output Specifications
- Orchestrator Log: `xs-orchestrator-execution-log.json`
- Final Consolidated Output: `xs-final-output.json`
- Sub-workflow Outputs:
  - Planning Artifacts (implementation plan, task breakdown)
  - Implementation Artifacts (code, tests, validation results)
- Tracking File: `xs-progress-tracking.md`
- Output Location: `[id:findings_dir]`

## Sub-Workflow Chain

### Sub-Workflow 1: Planning
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/XS/workflow-3-planning.md`
- Input Requirements:
  - Primary: Context package from router and router artifacts
  - From Previous: N/A (first step)
- Output Produced: Planning artifacts (implementation plan, task breakdown)
- Description: Plan a minimal, fast execution with clear tasks and estimates
- Success Criteria: Required planning outputs exist before proceeding
- Failure Handling: Adjust plan based on constraints; quick iterate; orchestrator pauses if incomplete

### Sub-Workflow 2: Implementation
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/XS/workflow-4-implementation.md`
- Input Requirements:
  - Primary: Artifacts from Planning
  - Additional: Lightweight validation checklist
- Output Produced: Implementation artifacts (code, tests, validation results)
- Description: Build and validate solution ready for merge
- Success Criteria: Code complete, tests passing, peer review approved
- Failure Handling: Block merge; remediate and re-validate

## Data Flow Between Sub-Workflows

### Input/Output Chain
```
[Context Package]
    ↓
[Planning] → Planning Artifacts
    ↓
[Implementation] → Implementation Artifacts
    ↓
[Consolidated Final Output]
```

### Data Transformation Points
- Between Planning & Implementation: Convert plan into concrete development tasks and validation steps
- Final Consolidation: Aggregate implementation validations and peer review results

## Orchestrator Control Logic

### Execution Flow
```
1. VALIDATE orchestrator prerequisites and router context package completeness
2. PREPARE inputs for Planning
3. FOR each sub-workflow in chain:
   a. VALIDATE sub-workflow prerequisites and approvals
   b. PREPARE sub-workflow inputs from previous outputs
   c. EXECUTE sub-workflow
   d. VALIDATE sub-workflow completion and approvals
   e. LOG sub-workflow results
   f. PREPARE outputs for next sub-workflow
4. CONSOLIDATE all sub-workflow outputs
5. GENERATE final orchestrator output
```

## Template Validation
- All `[id:...]` references must exist in memory map
- All sub-workflow files exist in `[id:prompts_dir]treat-change-request/workflows/XS/`
- Sub-workflow chain is 3 → 4 with required validations
- Data flow between sub-workflows is compatible and traceable
- State management/log files are structured in JSON
- Error recovery strategies defined per sub-workflow
- No circular dependencies between sub-workflows

### Error Recovery Strategy
- Sub-Workflow Failure: Pause orchestrator, log context, address issues, allow resume
- Chain Interruption: Resume from last successful sub-workflow using state file
- Data Corruption: Re-generate affected outputs from prior validated step; keep backups
- Rollback Capability: Preserve intermediate artifacts to support rollback

## Progress Tracking

### Orchestrator State File: `orchestrator-xs-state.json`
```json
{
  "orchestrator_name": "orchestrator-xs-extra-small-workflow",
  "execution_id": "xs-[timestamp]",
  "start_time": "2025-07-28T14:00:00Z",
  "current_status": "running|paused|completed|failed",
  "completed_sub_workflows": [
    {
      "name": "planning",
      "status": "completed",
      "output": "planning-artifacts",
      "completion_time": "2025-07-28T14:10:00Z"
    }
  ],
  "current_sub_workflow": {
    "name": "implementation",
    "status": "running",
    "start_time": "2025-07-28T14:10:00Z"
  },
  "pending_sub_workflows": [],
  "overall_progress": {
    "completed": 1,
    "total": 2,
    "percentage": 50
  }
}
```

## Sub-Workflow Coordination

### Input Preparation Logic
```json
{
  "input_preparation_rules": {
    "planning": {
      "sources": ["router_context_package"],
      "transformations": ["validate-context"]
    },
    "implementation": {
      "sources": ["planning.outputs"],
      "transformations": ["validate-test-plan", "prepare-deployment"]
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
        "execution_summary": "from orchestrator-xs-state.json",
        "sub_workflow_results": "summary of each sub-workflow"
      },
      "consolidated_data": {
        "primary_results": "implementation validations and readiness",
        "secondary_data": "traceability links to plan"
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
- Start Execution: "This orchestrator will execute 2 sub-workflows in sequence. Proceed?"
- Critical Checkpoints: Plan completeness; Ready for merge
- Sub-Workflow Failures: "Sub-workflow [X] failed or not approved. Continue/Retry/Abort?"

### Progress Reporting
- Status Updates: After each sub-workflow completion and approval
- Milestone Notifications: Plan completed; Ready for merge
- Completion Summary: Final execution summary with links to all produced artifacts

## Validation and Completion

### Sub-Workflow Validation
- [ ] Each sub-workflow completed successfully and approved at its gate
- [ ] All sub-workflow outputs generated and validated
- [ ] No critical errors in sub-workflow chain

### Orchestrator Validation
- [ ] All sub-workflows executed in correct sequence with approvals
- [ ] Data flow between sub-workflows successful and traceable
- [ ] Final consolidated output generated
- [ ] Orchestrator state properly maintained
- [ ] All intermediate files preserved for audit

### Completion Criteria
- [ ] Both sub-workflows in chain completed and approved
- [ ] Final consolidated output validated
- [ ] Orchestrator execution log complete
- [ ] No unresolved errors or warnings

## Next Steps
- Merge code following the team merge process
- Deploy following the standard deployment process
- Monitor in production
=======
# Orchestrator XS: Extra Small Changes

**Purpose**: Handle extra small changes with minimal governance.

**Version**: 2.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Handles **Extra Small (XS)** changes - single service, minimal files, <2 days effort.

Executes two workflows in sequence:
1. Planning
2. Implementation

---

## Workflows

```
Orchestrator-XS-Extra-Small
├── Workflow 3: Planning
└── Workflow 4: Implementation
```

---

## Inputs

Receives context package from **Orchestrator-0-Router** containing:
- Issue IDs and change request details
- Size classification (XS) and rationale
- Technical scope analysis
- All router artifacts

---

## Outputs

| Output | Description |
|--------|-------------|
| **Planning Artifacts** | Implementation plan and task breakdown |
| **Implementation Artifacts** | Code, tests, validation results |
| **Tracking File** | Progress tracking for all workflows |

---

## Workflow Execution

### Workflow 3: Planning

**File**: `../workflows/XS/workflow-3-planning.md`

**Input**: Context package from router

**Validation**: Required outputs exist before proceeding to implementation

---

### Workflow 4: Implementation

**File**: `../workflows/XS/workflow-4-implementation.md`

**Input**: Artifacts from Workflow 3

**Validation**: Code complete, tests passing, peer review approved

---

## Success Criteria

This orchestrator is successful when:

- ✅ All workflow outputs exist and validated
- ✅ Peer review completed
- ✅ Automated checks passing
- ✅ Code ready for merge

---

## Next Steps

After this orchestrator completes:
1. **Merge code** following team merge process
2. **Deploy** following standard deployment process
3. **Monitor** in production

---

## End of Orchestrator

**Version**: 2.0  
**Execution Model**: Delegate to workflows (3 → 4)  
**Validation**: Check workflow outputs before completion
>>>>>>> da09d7f (feat: Add orchestrator workflows for extra small changes including planning and implementation phases)
