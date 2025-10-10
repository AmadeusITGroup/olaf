---
name: workflow-3-planning-xs
description: Extra small change implementation planning producing implementation-notes.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 3: Planning (XS)

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

**Purpose**: Direct code implementation planning for extra small changes (no heavy artifacts)

**Input**: Context package from router

**Output**: Implementation approach notes

---

## Input Requirements
- **Primary Input**: Context package from router
- **Secondary Inputs**: N/A
- **Input Format**: Markdown/YAML context

## Output Specifications
- **Primary Output**: `implementation-notes.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute prompt - no skipping

### Prompt 3-1: Implementation Planning

**File**: `../../prompts/prompt-3-1-implementation.md`

**Input**: Context package from router

**Output**: `implementation-notes.md`

**Description**: Produce a concise implementation approach suitable for immediate execution in Workflow 4.

**Validation**: Approach defined and feasible

---

## Data Flow Diagram
```text
[Context package] → [Step 3-1: Implementation Planning] → implementation-notes.md
```

## Error Handling
- **Step Failure**: If context is incomplete, request missing inputs and stop
- **Recovery**: Provide missing context and re-run the step
- **Rollback**: Not applicable; notes can be regenerated

## Completion Criteria
- [ ] Prompt executed successfully
- [ ] Implementation approach is clear and actionable
- [ ] Ready to hand off to Workflow 4

## Next Steps
- Proceed to `workflow-4-implementation.md`

## Handoff

**Next workflow**: `workflow-4-implementation.md`

**Provides**: `implementation-notes.md`
