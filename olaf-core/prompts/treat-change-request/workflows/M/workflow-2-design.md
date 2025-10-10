---
name: workflow-2-design-m
description: Medium-size technical design workflow producing DESIGN_<PROJECT-ID>.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 2: Design (M)

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

**Purpose**: Technical design for medium changes

**Input**: `SPECIFICATION_<PROJECT-ID>.md` (or context package), codebase

**Output**: Technical design document ready for planning phase

---

## Prerequisites

- Approved `SPECIFICATION_<PROJECT-ID>.md` exists or equivalent context package.
- Access to the codebase for validation and references.

---

## Input Requirements
- **Primary Input**: `SPECIFICATION_<PROJECT-ID>.md` (or context package)
- **Secondary Inputs**: Codebase access for validation and references
- **Input Format**: Markdown specification, codebase

## Output Specifications
- **Primary Output**: `DESIGN_<PROJECT-ID>.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute all steps in sequence - no skipping

### Prompt 2-1: Initial Design

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-2-1-initial-design.md`

**Input**: `SPECIFICATION_<PROJECT-ID>.md` (or context package), codebase

**Output**: `DESIGN_<PROJECT-ID>.md` (initial draft)

**Validation**: Architecture, components, and technical decisions documented

---

### Prompt 2-2: Design Validation

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-2-2-design-validation.md`

**Input**: Initial design, codebase analysis

**Output**: Updated `DESIGN_<PROJECT-ID>.md` with feasibility assessment

**Validation**: Implementation feasibility confirmed with code references

---

### Prompt 2-3: Technical Review

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-2-3-technical-review.md`

**Input**: Validated design

**Output**: Updated `DESIGN_<PROJECT-ID>.md` with feedback integrated

**Validation**: Technical stakeholder approval obtained

---

### Prompt 2-4: Design Finalization

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-2-4-design-finalization.md`

**Input**: Reviewed design

**Output**: Final `DESIGN_<PROJECT-ID>.md`

**Validation**: Professional formatting applied, all sections complete

## Data Flow Diagram
```text
[SPECIFICATION.md] → [Step 2-1: initial design] → DESIGN.md → [Step 2-2: design validation] → DESIGN.md
                                            ↓
                              [Step 2-3: technical review] → DESIGN.md → [Step 2-4: finalization] → DESIGN.md (final)
```

## Error Handling
- **Step Failure**: Document issues; if conflicts found, loop back to specification
- **Recovery**: Refresh analysis and update design; re-run failed step
- **Rollback**: Maintain previous design versions before updates

## Completion Criteria
- [ ] All prompts executed successfully
- [ ] Design document complete
- [ ] Technical stakeholder approval documented
- [ ] Ready to hand off to Workflow 3

## Next Steps
- Proceed to `workflow-3-planning.md`

## Handoff

**Next workflow**: `workflow-3-planning.md`

**Provides**: Final `DESIGN_<PROJECT-ID>.md` with approvals
