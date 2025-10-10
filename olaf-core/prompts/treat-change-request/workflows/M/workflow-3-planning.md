---
name: workflow-3-planning-m
description: Medium-size change planning producing IMPLEMENTATION_PLAN_<PROJECT-ID>.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 3: Planning (M)

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

**Purpose**: Create implementation plan for medium changes

**Input**: Artifacts from Workflow 2 (design documents)

**Output**: Implementation plan

---

## Input Requirements
- **Primary Input**: `DESIGN_<PROJECT-ID>.md`
- **Secondary Inputs**: None
- **Input Format**: Markdown design document

## Output Specifications
- **Primary Output**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute prompt - no skipping

### Prompt 3-1: Implementation Planning

**File**: `../../prompts/prompt-3-1-implementation.md`

**Input**: `DESIGN_<PROJECT-ID>.md`

**Output**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`

**Validation**: Task breakdown complete, dependencies mapped

---

## Data Flow Diagram
```text
[DESIGN_<PROJECT-ID>.md] → [Step 3-1: Implementation Planning] → IMPLEMENTATION_PLAN_<PROJECT-ID>.md
```

## Error Handling
- **Step Failure**: If design is missing/unclear, request clarification and stop
- **Recovery**: Update design/context and re-run the step
- **Rollback**: Not applicable; plan can be regenerated

---

## Completion Criteria

✅ **Workflow complete when**:

1. Prompt executed successfully
2. Implementation plan exists with task breakdown
3. Ready to hand off to Workflow 4

---

## Handoff

**Next workflow**: `workflow-4-implementation.md`

**Provides**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`
