<<<<<<< HEAD
---
name: orchestrator-xl-extra-large-workflow
description: Master/orchestrator workflow that coordinates the XL (Extra Large) change sub-workflows 1 → 2 → 3 → 4
tags: [workflow, orchestrator, xl, extra-large, governance, coordination]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

Use terminal commands, not training data.

## orchestrator-xl-extra-large-workflow: XL Changes Orchestrator Workflow

> Note: All files referenced below are either prompts located in `[id:prompts_dir]` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

## Template Variables
- `[WORKFLOW_NAME]`: orchestrator-xl-extra-large-workflow
- `[WORKFLOW_DESCRIPTION]`: Extra Large (XL) changes with full governance
- `[SUB_WORKFLOW_NAME]`: Specification | Design | Planning | Implementation
- `[sub-workflow-file]`: treat-change-request/workflows/XL/workflow-1-specification | treat-change-request/workflows/XL/workflow-2-design | treat-change-request/workflows/XL/workflow-3-planning | treat-change-request/workflows/XL/workflow-4-implementation
- `[descriptive-orchestrator-log-name]`: xl-orchestrator-execution-log
- `[descriptive-final-output-name]`: xl-final-output
- `[sub-workflow-output-file]`: specification artifacts | design artifacts | planning artifacts | implementation artifacts
- `[orchestrator-state-name]`: orchestrator-xl-state
- `[unique-execution-id]`: xl-[timestamp]
- `[transformation-description]`: Transform and validate artifacts between phases, preserving traceability

## Workflow Type
Master/Orchestrator - Chains and coordinates complete sub-workflows and prompts in sequence

## Workflow Overview
Handles Extra Large (XL) changes involving multiple modules/services, architectural changes, and high effort. Executes four sub-workflows in sequence with required reviews and validations at each stage.

## Prerequisites
- Receives context package from Orchestrator-0-Router containing issue IDs, size classification (XL), rationale, technical scope, risk assessment, estimates, and router artifacts
- Stakeholders and reviewers identified for architecture and design reviews
- Repository access and governance checklists available

## Input Requirements
- Primary Input: Context package from router (`6-context-package.yaml`) and associated artifacts
- Configuration Input: Review gates and checklists for Architecture, Design, Planning, Implementation
- Input Format: Markdown/YAML for artifacts, JSON for orchestrator state/log

## Output Specifications
- Orchestrator Log: `xl-orchestrator-execution-log.json`
- Final Consolidated Output: `xl-final-output.json`
- Sub-workflow Outputs:
  - Specification Artifacts (complete specification and architecture documentation)
  - Design Artifacts (comprehensive technical design)
  - Planning Artifacts (implementation plan, task breakdown)
  - Implementation Artifacts (code, tests, validation, deployment artifacts)
- Tracking File: `xl-progress-tracking.md`
- Output Location: `[id:findings_dir]`

## Sub-Workflow Chain

### Sub-Workflow 1: Specification
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/XL/workflow-1-specification.md`
- Input Requirements:
  - Primary: Context package from router and all router artifacts
  - From Previous: N/A (first step)
- Output Produced: Specification artifacts (complete spec and architecture docs)
- Description: Establishes comprehensive specification and architecture
- Success Criteria: Architecture review approved before proceeding
- Failure Handling: Capture review feedback, iterate until approval; orchestrator pauses if not approved

### Sub-Workflow 2: Design
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/XL/workflow-2-design.md`
- Input Requirements:
  - Primary: Artifacts from Specification
  - Additional: Architecture review approval record
- Output Produced: Design artifacts (comprehensive technical design)
- Description: Produces detailed design aligned with approved architecture
- Success Criteria: Design review approved before proceeding
- Failure Handling: Address review findings; do not proceed until approved

### Sub-Workflow 3: Planning
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/XL/workflow-3-planning.md`
- Input Requirements:
  - Primary: Artifacts from Design
  - Additional: Capacity and scheduling inputs
- Output Produced: Planning artifacts (implementation plan, task breakdown)
- Description: Plans execution with milestones, risks, mitigation
- Success Criteria: Implementation plan complete and baselined
- Failure Handling: Re-plan based on constraints; require owner approval

### Sub-Workflow 4: Implementation
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/XL/workflow-4-implementation.md`
- Input Requirements:
  - Primary: Artifacts from Planning
  - Additional: Governance checklists (security, performance, testing, deployment)
- Output Produced: Implementation artifacts (code, tests, validation results, deployment artifacts)
- Description: Build, validate, and prepare for production
- Success Criteria: All validations passed, all reviews approved, production-ready
- Failure Handling: Block release; raise escalation as per governance; remediate and re-validate

## Data Flow Between Sub-Workflows

### Input/Output Chain
```
[Context Package]
    ↓
[Specification] → Specification Artifacts
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
- Between Specification & Design: Map approved architecture to detailed design components
- Between Design & Planning: Break down design into executable tasks, estimates, milestones
- Final Consolidation: Aggregate implementation validations, ensure traceability to spec/design

## Orchestrator Control Logic

### Execution Flow
```
1. VALIDATE orchestrator prerequisites and router context package completeness
2. PREPARE inputs for Specification
3. FOR each sub-workflow in chain:
   a. VALIDATE sub-workflow prerequisites and approvals
   b. PREPARE sub-workflow inputs from previous outputs
   c. EXECUTE sub-workflow
   d. VALIDATE sub-workflow completion and review approvals
   e. LOG sub-workflow results
   f. PREPARE outputs for next sub-workflow
4. CONSOLIDATE all sub-workflow outputs
5. GENERATE final orchestrator output
```

## Template Validation
- All `[id:...]` references must exist in memory map
- All sub-workflow files exist in `[id:prompts_dir]treat-change-request/workflows/XL/`
- Sub-workflow chain is 1 → 2 → 3 → 4 with required approvals
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

### Orchestrator State File: `orchestrator-xl-state.json`
```json
{
  "orchestrator_name": "orchestrator-xl-extra-large-workflow",
  "execution_id": "xl-[timestamp]",
  "start_time": "2025-07-28T14:00:00Z",
  "current_status": "running|paused|completed|failed",
  "completed_sub_workflows": [
    {
      "name": "specification",
      "status": "completed",
      "output": "specification-artifacts",
      "completion_time": "2025-07-28T14:30:00Z"
    }
  ],
  "current_sub_workflow": {
    "name": "design",
    "status": "running",
    "start_time": "2025-07-28T14:30:00Z"
  },
  "pending_sub_workflows": [
    "planning",
    "implementation"
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
    "specification": {
      "sources": ["router_context_package"],
      "transformations": ["validate-context", "identify-architecture-reviewers"]
    },
    "design": {
      "sources": ["specification.outputs"],
      "transformations": ["map-architecture-to-design", "collect-design-reviewers"]
    },
    "planning": {
      "sources": ["design.outputs"],
      "transformations": ["breakdown-to-tasks", "estimate-and-schedule"]
    },
    "implementation": {
      "sources": ["planning.outputs"],
      "transformations": ["validate-governance-checklists", "prepare-deployment"]
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
        "execution_summary": "from orchestrator-xl-state.json",
        "sub_workflow_results": "summary of each sub-workflow"
      },
      "consolidated_data": {
        "primary_results": "implementation validations and deployment readiness",
        "secondary_data": "traceability links to spec and design"
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
- Critical Checkpoints: Architecture review approval; Design review approval; Plan baseline approval; Go-live readiness
- Sub-Workflow Failures: "Sub-workflow [X] failed or not approved. Continue/Retry/Abort?"

### Progress Reporting
- Status Updates: After each sub-workflow completion and approval
- Milestone Notifications: Architecture approved; Design approved; Plan baselined; Production-ready
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

## Escalation & De-escalation
- Escalation triggers monitored at each workflow completion; raise governance board if thresholds exceeded
- De-escalation possible if complexity lower than expected; route to lower-tier orchestrator as per policy
- See individual workflow files for specific escalation criteria and actions

## Next Steps
- Deploy following the deployment process
- Monitor new functionality in production
- Document lessons learned, retrospective with team
- Update metrics for continuous improvement
=======
# Orchestrator XL: Extra Large Changes

**Purpose**: Handle extra large, high-complexity, high-risk changes with full governance.

**Version**: 2.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Handles **Extra Large (XL)** changes - multiple services/modules (>5), architectural changes, >20 days effort.

Executes four workflows in sequence:

1. Specification (complete)
2. Design (comprehensive)
3. Planning
4. Implementation

---

## Workflows

```
Orchestrator-XL-Extra-Large
├── Workflow 1: Specification
├── Workflow 2: Design
├── Workflow 3: Planning
└── Workflow 4: Implementation
```

---

## Inputs

Receives context package from **Orchestrator-0-Router** containing:
- Issue IDs and change request details
- Size classification (XL) and rationale
- Technical scope analysis
- Risk assessment
- Effort estimates
- All router artifacts

---

## Outputs

| Output | Description |
|--------|-------------|
| **Specification Artifacts** | Complete specification and architecture documentation |
| **Design Artifacts** | Comprehensive technical design documentation |
| **Planning Artifacts** | Implementation plan and task breakdown |
| **Implementation Artifacts** | Code, tests, validation results, deployment artifacts |
| **Tracking File** | Progress tracking for all workflows |

---

## Workflow Execution

### Workflow 1: Specification

**File**: `../workflows/XL/workflow-1-specification.md`

**Input**: Context package from router

**Validation**: Architecture review approved before proceeding

---

### Workflow 2: Design

**File**: `../workflows/XL/workflow-2-design.md`

**Input**: Artifacts from Workflow 1

**Validation**: Design review approved before proceeding

---

### Workflow 3: Planning

**File**: `../workflows/XL/workflow-3-planning.md`

**Input**: Artifacts from Workflow 2

**Validation**: Implementation plan complete before proceeding

---

### Workflow 4: Implementation

**File**: `../workflows/XL/workflow-4-implementation.md`

**Input**: Artifacts from Workflow 3

**Validation**: All validations passed, all reviews approved, production-ready

---

## Success Criteria

This orchestrator is successful when:

- ✅ All workflow outputs exist and validated
- ✅ Architecture review approved
- ✅ Design review approved
- ✅ Code reviews completed
- ✅ Security validation passed
- ✅ All test suites passing
- ✅ Performance validated
- ✅ Deployment plan verified
- ✅ Stakeholder sign-off obtained
- ✅ Code ready for deployment

---

## Escalation & De-escalation

**Escalation triggers** are monitored at each workflow completion.

**De-escalation** is possible if complexity lower than expected.

**Details**: See individual workflow files for specific escalation criteria and actions.

---

## Next Steps

After this orchestrator completes:

1. **Deploy** following deployment process
2. **Monitor** new functionality in production
3. **Document** lessons learned
4. **Retrospective** with team
5. **Update metrics** for future improvements

---

## End of Orchestrator

**Version**: 2.0  
**Execution Model**: Delegate to workflows (1 → 2 → 3 → 4)  
**Validation**: Check workflow outputs and approvals before completion
>>>>>>> c5759c0 (feat: Add orchestrator workflows for extra large changes including specification, design, planning, and implementation phases)
