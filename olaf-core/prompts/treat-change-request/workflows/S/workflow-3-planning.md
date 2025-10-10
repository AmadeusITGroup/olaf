---
name: workflow-3-planning-s
description: Small-size planning workflow producing IMPLEMENTATION_PLAN_<PROJECT-ID>.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 3: Planning (S)

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

**Purpose**: Create implementation plan for small changes

**Input**: Artifacts from Workflow 2 (design review notes)

**Output**: Implementation plan

---

## Input Requirements
- **Primary Input**: `design-review-notes.md`
- **Secondary Inputs**: Context package
- **Input Format**: Markdown notes + project context

## Output Specifications
- **Primary Output**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute prompt - no skipping

### Prompt 3-1: Implementation Planning

**File**: `../../prompts/prompt-3-1-implementation.md`

**Input**: `design-review-notes.md`, context package

**Output**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`

**Description**: Produce a concise, actionable implementation plan with task breakdown for a small change.

**Validation**: Task breakdown complete

---

## Data Flow Diagram
```text
[design-review-notes.md + context] → [Step 3-1: Implementation Planning] → IMPLEMENTATION_PLAN_<PROJECT-ID>.md
```

## Error Handling
- **Step Failure**: If inputs missing, request them and stop
- **Recovery**: Provide missing inputs and re-run the step
- **Rollback**: Not applicable; plan can be regenerated

## Completion Criteria
- [ ] Prompt executed successfully
- [ ] Implementation plan exists
- [ ] Ready to hand off to Workflow 4

## Next Steps
- Proceed to `workflow-4-implementation.md`

## Handoff

**Next workflow**: `workflow-4-implementation.md`

**Provides**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`
