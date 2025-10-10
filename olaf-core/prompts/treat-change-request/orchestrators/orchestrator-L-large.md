---
name: orchestrator-l-large-workflow
description: Master/orchestrator workflow that coordinates the Large (L) change sub-workflows 1 → 2 → 3 → 4
tags: [workflow, orchestrator, large, governance, coordination]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## orchestrator-l-large-workflow: Large Changes Orchestrator Workflow

> Note: All files referenced below are either prompts located in `[id:prompts_dir]` or tools located in `[id:tools_dir]`, as specified in the memory map file.
> The solution to analyze is in `[id:core_dir]` and all new non-temporary created files are to be created in `[id:findings_dir]` folder.

## Template Variables
- `[WORKFLOW_NAME]`: orchestrator-l-large-workflow
- `[WORKFLOW_DESCRIPTION]`: Large (L) changes with comprehensive governance
- `[SUB_WORKFLOW_NAME]`: Specification | Design | Planning | Implementation
- `[sub-workflow-file]`: treat-change-request/workflows/L/workflow-1-specification | treat-change-request/workflows/L/workflow-2-design | treat-change-request/workflows/L/workflow-3-planning | treat-change-request/workflows/L/workflow-4-implementation
- `[descriptive-orchestrator-log-name]`: l-orchestrator-execution-log
- `[descriptive-final-output-name]`: l-final-output
- `[sub-workflow-output-file]`: specification artifacts | design artifacts | planning artifacts | implementation artifacts
- `[orchestrator-state-name]`: orchestrator-l-state
- `[unique-execution-id]`: l-[timestamp]
- `[transformation-description]`: Transform and validate artifacts between phases, preserving traceability

## Workflow Type
Master/Orchestrator - Chains and coordinates complete sub-workflows and prompts in sequence

## Workflow Overview
Handles Large (L) changes involving multiple services (3-5) and 10-20 days effort. Executes four sub-workflows in sequence with required reviews and validations at each stage.

## Prerequisites
- Receives context package from Orchestrator-0-Router containing issue IDs, size classification (L), rationale, technical scope, risk assessment, and router artifacts
- Stakeholders and reviewers identified for specification/design approvals
- Repository access and governance checklists available

## Input Requirements
- Primary Input: Context package from router (`6-context-package.yaml`) and associated artifacts
- Configuration Input: Review gates and checklists for Specification, Design, Planning, Implementation
- Input Format: Markdown/YAML for artifacts, JSON for orchestrator state/log

## Output Specifications
- Orchestrator Log: `l-orchestrator-execution-log.json`
- Final Consolidated Output: `l-final-output.json`
- Sub-workflow Outputs:
  - Specification Artifacts (specification and architecture documentation)
  - Design Artifacts (technical design and review documentation)
  - Planning Artifacts (implementation plan, task breakdown)
  - Implementation Artifacts (code, tests, validation results)
- Tracking File: `l-progress-tracking.md`
- Output Location: `[id:findings_dir]`

## Sub-Workflow Chain

### Sub-Workflow 1: Specification
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/L/workflow-1-specification.md`
- Input Requirements:
  - Primary: Context package from router and router artifacts
  - From Previous: N/A (first step)
- Output Produced: Specification artifacts (spec and architecture docs)
- Description: Establishes specification and architecture (lighter than XL)
- Success Criteria: Specification complete and approved before proceeding
- Failure Handling: Capture review feedback, iterate until approval; orchestrator pauses if not approved

### Sub-Workflow 2: Design
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/L/workflow-2-design.md`
- Input Requirements:
  - Primary: Artifacts from Specification
  - Additional: Specification approval record
- Output Produced: Design artifacts (technical design and reviews)
- Description: Produces detailed design aligned with approved specification
- Success Criteria: Design complete and approved before proceeding
- Failure Handling: Address review findings; do not proceed until approved

### Sub-Workflow 3: Planning
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/L/workflow-3-planning.md`
- Input Requirements:
  - Primary: Artifacts from Design
  - Additional: Capacity and scheduling inputs
- Output Produced: Planning artifacts (implementation plan, task breakdown)
- Description: Plans execution with milestones, risks, mitigation
- Success Criteria: Implementation plan complete
- Failure Handling: Re-plan based on constraints; require owner approval

### Sub-Workflow 4: Implementation
- Type: Sequential
- Prompt/Workflow: `[id:prompts_dir]treat-change-request/workflows/L/workflow-4-implementation.md`
- Input Requirements:
  - Primary: Artifacts from Planning
  - Additional: Governance checklists (tests, validation)
- Output Produced: Implementation artifacts (code, tests, validation results)
- Description: Build and validate solution ready for deployment
- Success Criteria: Code complete, tests passing, reviews approved
- Failure Handling: Block release; remediate and re-validate

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
- Between Specification & Design: Map specification to detailed design components
- Between Design & Planning: Break down design into executable tasks, estimates, milestones
- Final Consolidation: Aggregate implementation validations and ensure traceability to spec/design

## Orchestrator Control Logic

### Execution Flow
```
1. VALIDATE orchestrator prerequisites and router context package completeness
2. PREPARE inputs for Specification
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
- All sub-workflow files exist in `[id:prompts_dir]treat-change-request/workflows/L/`
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

### Orchestrator State File: `orchestrator-l-state.json`
```json
{
  "orchestrator_name": "orchestrator-l-large-workflow",
  "execution_id": "l-[timestamp]",
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
      "transformations": ["validate-context"]
    },
    "design": {
      "sources": ["specification.outputs"],
      "transformations": ["map-spec-to-design"]
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
        "execution_summary": "from orchestrator-l-state.json",
        "sub_workflow_results": "summary of each sub-workflow"
      },
      "consolidated_data": {
        "primary_results": "implementation validations and readiness",
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
- Critical Checkpoints: Specification approval; Design approval; Plan baseline; Go-live readiness
- Sub-Workflow Failures: "Sub-workflow [X] failed or not approved. Continue/Retry/Abort?"

### Progress Reporting
- Status Updates: After each sub-workflow completion and approval
- Milestone Notifications: Specification approved; Design approved; Plan baselined; Ready for deployment
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
- Deploy following the deployment process
- Monitor in production
- Document lessons learned
