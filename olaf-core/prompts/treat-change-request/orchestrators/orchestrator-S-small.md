<<<<<<< HEAD
---
name: orchestrator-s-small-workflow
description: Master/orchestrator workflow that coordinates the Small (S) change sub-workflows 2 → 3 → 4
tags: [workflow, orchestrator, small, governance, coordination]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## orchestrator-s-small-workflow: Small Changes Orchestrator Workflow

> Note: All files referenced below are either prompts located in `[id:prompts_dir]` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

## Template Variables
- `[WORKFLOW_NAME]`: orchestrator-s-small-workflow
- `[WORKFLOW_DESCRIPTION]`: Small (S) changes with lightweight governance
- `[SUB_WORKFLOW_NAME]`: Design | Planning | Implementation
- `[sub-workflow-file]`: treat-change-request/workflows/S/workflow-2-design | treat-change-request/workflows/S/workflow-3-planning | treat-change-request/workflows/S/workflow-4-implementation
- `[descriptive-orchestrator-log-name]`: s-orchestrator-execution-log
- `[descriptive-final-output-name]`: s-final-output
- `[sub-workflow-output-file]`: design artifacts | planning artifacts | implementation artifacts
- `[orchestrator-state-name]`: orchestrator-s-state
- `[unique-execution-id]`: s-[timestamp]
- `[transformation-description]`: Transform and validate artifacts between phases, preserving traceability

## Workflow Type
Master/Orchestrator - Chains and coordinates complete sub-workflows and prompts in sequence

## Workflow Overview
Handles Small (S) changes involving 1-2 services and 2-5 days effort. Executes three sub-workflows (Design → Planning → Implementation) with lightweight validations and approvals at each stage.

## Prerequisites
- Receives context package from Orchestrator-0-Router containing issue IDs, size classification (S), rationale, technical scope, and router artifacts
- Reviewer identified for lightweight design review
- Repository access and team capacity inputs available

## Input Requirements
- Primary Input: Context package from router (`6-context-package.yaml`) and associated artifacts
- Configuration Input: Review gates and checklists for Design, Planning, Implementation (lightweight)
- Input Format: Markdown/YAML for artifacts, JSON for orchestrator state/log

## Output Specifications
- Orchestrator Log: `s-orchestrator-execution-log.json`
- Final Consolidated Output: `s-final-output.json`
- Sub-workflow Outputs:
  - Design Artifacts (quick design review and technical decisions)
  - Planning Artifacts (implementation plan, task breakdown)
  - Implementation Artifacts (code, tests, validation results)
- Tracking File: `s-progress-tracking.md`
- Output Location: `[id:findings_dir]`

## Sub-Workflow Chain

### Sub-Workflow 1: Design
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/S/workflow-2-design.md`
- Input Requirements:
  - Primary: Context package from router and router artifacts
  - From Previous: N/A (first step)
- Output Produced: Design artifacts (quick design review and technical decisions)
- Description: Lightweight design review and decisions
- Success Criteria: Design review approved before proceeding
- Failure Handling: Capture review feedback; iterate quickly until approval; orchestrator pauses if not approved

### Sub-Workflow 2: Planning
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/S/workflow-3-planning.md`
- Input Requirements:
  - Primary: Artifacts from Design
  - Additional: Capacity and scheduling inputs
- Output Produced: Planning artifacts (implementation plan, task breakdown)
- Description: Plans execution with milestones and minimal governance
- Success Criteria: Implementation plan complete before proceeding
- Failure Handling: Re-plan based on constraints; require owner approval

### Sub-Workflow 3: Implementation
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/S/workflow-4-implementation.md`
- Input Requirements:
  - Primary: Artifacts from Planning
  - Additional: Test plan and validation checklist (lightweight)
- Output Produced: Implementation artifacts (code, tests, validation results)
- Description: Build and validate solution ready for merge
- Success Criteria: Code complete, tests passing, reviews approved
- Failure Handling: Block merge; remediate and re-validate

## Data Flow Between Sub-Workflows

### Input/Output Chain
```
[Context Package]
    ↓
[Design] → Design Artifacts
    ↓
[Planning] → Planning Artifacts
    ↓
[Implementation] → Implementation Artifacts
    ↓
[Consolidated Final Output]
```

### Data Transformation Points
- Between Design & Planning: Break down design into executable tasks, estimates, milestones
- Final Consolidation: Aggregate implementation validations; ensure traceability to design and plan

## Orchestrator Control Logic

### Execution Flow
```
1. VALIDATE orchestrator prerequisites and router context package completeness
2. PREPARE inputs for Design
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
- All sub-workflow files exist in `[id:prompts_dir]treat-change-request/workflows/S/`
- Sub-workflow chain is 2 → 3 → 4 with required approvals
- Data flow between sub-workflows is compatible and traceable
- State management/log files are structured in JSON
- Error recovery strategies defined per sub-workflow
- No circular dependencies between sub-workflows

### Error Recovery Strategy
- Sub-Workflow Failure: Pause orchestrator, log context, address review findings, allow resume
- Chain Interruption: Resume from last successful sub-workflow using state file
- Data Corruption: Re-generate affected outputs from prior validated step; keep backups
- Rollback Capability: Preserve intermediate artifacts to support rollback

## Progress Tracking

### Orchestrator State File: `orchestrator-s-state.json`
```json
{
  "orchestrator_name": "orchestrator-s-small-workflow",
  "execution_id": "s-[timestamp]",
  "start_time": "2025-07-28T14:00:00Z",
  "current_status": "running|paused|completed|failed",
  "completed_sub_workflows": [
    {
      "name": "design",
      "status": "completed",
      "output": "design-artifacts",
      "completion_time": "2025-07-28T14:20:00Z"
    }
  ],
  "current_sub_workflow": {
    "name": "planning",
    "status": "running",
    "start_time": "2025-07-28T14:20:00Z"
  },
  "pending_sub_workflows": [
    "implementation"
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
    "design": {
      "sources": ["router_context_package"],
      "transformations": ["validate-context"]
    },
    "planning": {
      "sources": ["design.outputs"],
      "transformations": ["breakdown-to-tasks", "estimate-and-schedule"]
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
        "execution_summary": "from orchestrator-s-state.json",
        "sub_workflow_results": "summary of each sub-workflow"
      },
      "consolidated_data": {
        "primary_results": "implementation validations and readiness",
        "secondary_data": "traceability links to design and plan"
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
- Critical Checkpoints: Design approval; Plan baseline; Ready for merge
- Sub-Workflow Failures: "Sub-workflow [X] failed or not approved. Continue/Retry/Abort?"

### Progress Reporting
- Status Updates: After each sub-workflow completion and approval
- Milestone Notifications: Design approved; Plan baselined; Ready for merge
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
- [ ] All sub-workflows in chain completed and approved
- [ ] Final consolidated output validated
- [ ] Orchestrator execution log complete
- [ ] No unresolved errors or warnings

## Next Steps
- Merge code following the team merge process
- Deploy following the standard deployment process
- Monitor in production
=======
# Orchestrator S: Small Changes

**Purpose**: Handle small changes with lightweight governance.

**Version**: 2.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Handles **Small (S)** changes - 1-2 services, limited files, 2-5 days effort.

Executes three workflows in sequence:

1. Design (lightweight review)
2. Planning
3. Implementation

---

## Workflows

```
Orchestrator-S-Small
├── Workflow 2: Design
├── Workflow 3: Planning
└── Workflow 4: Implementation
```

---

## Inputs

Receives context package from **Orchestrator-0-Router** containing:
- Issue IDs and change request details
- Size classification (S) and rationale
- Technical scope analysis
- All router artifacts

---

## Outputs

| Output | Description |
|--------|-------------|
| **Design Artifacts** | Quick design review and technical decisions |
| **Planning Artifacts** | Implementation plan and task breakdown |
| **Implementation Artifacts** | Code, tests, validation results |
| **Tracking File** | Progress tracking for all workflows |

---

## Workflow Execution

### Workflow 2: Design

**File**: `../workflows/S/workflow-2-design.md`

**Input**: Context package from router

**Validation**: Design review approved before proceeding

---

### Workflow 3: Planning

**File**: `../workflows/S/workflow-3-planning.md`

**Input**: Artifacts from Workflow 2

**Validation**: Implementation plan complete before proceeding

---

### Workflow 4: Implementation

**File**: `../workflows/S/workflow-4-implementation.md`

**Input**: Artifacts from Workflow 3

**Validation**: Code complete, tests passing, reviews approved

---

## Success Criteria

This orchestrator is successful when:

- ✅ All workflow outputs exist and validated
- ✅ Design review completed
- ✅ Peer review completed
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
**Execution Model**: Delegate to workflows (2 → 3 → 4)  
**Validation**: Check workflow outputs before completion
>>>>>>> a756d8e (feat: Add orchestrator and workflows for handling small changes with lightweight governance)
