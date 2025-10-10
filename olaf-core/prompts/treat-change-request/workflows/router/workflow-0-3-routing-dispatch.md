---
name: workflow-0-3-routing-dispatch
description: Route sized change request and generate context package and routing documentation
tags: [workflow, sequential, treat-change-request]
---

# Workflow 0-3: Routing & Dispatch

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

## Workflow Overview

**Purpose**: Route the sized change request to the appropriate Orchestrator and create handoff documentation

**Input**: All artifacts from Workflows 0-1 and 0-2 (files 1-5) plus final size classification

**Output**: Context package YAML, routing summary, and README

---

## Prerequisites

- `5-final-size-decision.md` exists with a clear size classification and confidence.
- `4-size-evaluation-matrix.md` exists with completed scoring.
- Artifacts from 0-1 are available: `prerequisite-3-change-request.md`, `2-technical-scope-analysis.md`, `3-risk-assessment.md`.

---

## Input Requirements
- **Primary Input**: Files 1-5 from previous workflows and final size classification
- **Secondary Inputs**: N/A
- **Input Format**: Markdown and YAML

## Output Specifications
- **Primary Output**: `6-context-package.yaml`, `7-routing-summary.md`, `README.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute all steps in sequence (no skipping).

### Prompt 0-3-1: Routing Logic

  **File**: `[id:prompts_dir]treat-change-request/prompts/prompt-0-3-1-routing-logic.md`

  **Input**: Files 1-5, final size classification

  **Output**: `6-context-package.yaml`

  **Validation**: Correct Orchestrator selected, context package complete, all artifacts referenced

  ---

### Prompt 0-3-2: Routing Documentation

  **File**: `[id:prompts_dir]treat-change-request/prompts/prompt-0-3-2-routing-documentation.md`

  **Input**: `6-context-package.yaml`, all artifacts 1-5

  **Output**: `7-routing-summary.md`, `README.md`

  **Validation**: Routing rationale documented, critical highlights included, next steps clear

  ---

## Data Flow Diagram
```text
[Inputs (files 1-5 + final size)] → [Step 0-3-1: Routing Logic] → 6-context-package.yaml
                                                 ↓
                                  [Step 0-3-2: Routing Documentation] → 7-routing-summary.md + README.md
```

## Error Handling
- **Step Failure**: If final size classification missing/unclear: stop and return to Workflow 0-2
- **Recovery**: Fix inputs and re-run failed step
- **Rollback**: Not applicable; outputs can be regenerated

## Completion Criteria
- [ ] All steps completed successfully
- [ ] All 3 outputs exist (6-context-package.yaml, 7-routing-summary.md, README.md)
- [ ] Target Orchestrator clearly identified
- [ ] Context package ready for handoff

## Next Steps
- Open and execute the size-specific Orchestrator identified in `7-routing-summary.md`

## Handoff

**Next step**: Open and execute the size-specific Orchestrator identified in `7-routing-summary.md`

**Provides**: Complete analysis directory with all 7+ files and routing decision
