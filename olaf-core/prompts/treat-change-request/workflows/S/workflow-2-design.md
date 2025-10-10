---
name: workflow-2-design-s
description: Small-size quick design review producing design-review-notes.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 2: Design (S)

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

**Purpose**: Quick design review for small changes (lightweight - no detailed design)

**Input**: Context package from router

**Output**: Design review notes

---

## Input Requirements
- **Primary Input**: Context package from router
- **Secondary Inputs**: Codebase for reference
- **Input Format**: Markdown/YAML context + repository

## Output Specifications
- **Primary Output**: `design-review-notes.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute prompt - no skipping

### Prompt 2-3: Design Review

**File**: `../../prompts/prompt-2-3-design-review.md`

**Input**: Context package from router, codebase

**Output**: `design-review-notes.md`

**Description**: Perform a lightweight technical design review to validate approach without producing a full design document.

**Validation**: Tech Lead or Senior Developer approval obtained; approach is sound

---

## Data Flow Diagram
```text
[Context package + codebase] → [Step 2-3: Design Review] → design-review-notes.md
```

## Error Handling
- **Step Failure**: If context is incomplete, request missing inputs and stop
- **Recovery**: Provide missing context and re-run the step
- **Rollback**: Not applicable; notes can be regenerated

## Completion Criteria
- [ ] Prompt executed successfully
- [ ] Design review notes exist
- [ ] Approach approved by Tech Lead/Senior Developer
- [ ] Ready to hand off to Workflow 3

## Next Steps
- Proceed to `workflow-3-planning.md`

## Handoff

**Next workflow**: `workflow-3-planning.md`

**Provides**: `design-review-notes.md`
