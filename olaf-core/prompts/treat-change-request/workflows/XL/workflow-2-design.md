<<<<<<< HEAD
---
name: workflow-2-design-xl
description: Extra large change technical design producing DESIGN_<PROJECT-ID>.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 2: Design (XL)

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

=======
# Workflow 2: Design (XL)

>>>>>>> c5759c0 (feat: Add orchestrator workflows for extra large changes including specification, design, planning, and implementation phases)
## Overview

**Purpose**: Define comprehensive technical design for extra large changes

**Input**: Artifacts from Workflow 1 (approved specification)

**Output**: Complete technical design document ready for planning phase

---

<<<<<<< HEAD
## Input Requirements
- **Primary Input**: `SPECIFICATION_<PROJECT-ID>.md`
- **Secondary Inputs**: Codebase access for validation and references
- **Input Format**: Markdown specification, codebase

## Output Specifications
- **Primary Output**: `DESIGN_<PROJECT-ID>.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

=======
>>>>>>> c5759c0 (feat: Add orchestrator workflows for extra large changes including specification, design, planning, and implementation phases)
## Prompt Execution

Execute all prompts in sequence - no skipping

### Prompt 2-1: Initial Design

**File**: `../../prompts/prompt-2-1-initial-design.md`

**Input**: `SPECIFICATION_<PROJECT-ID>.md`, codebase

**Output**: `DESIGN_<PROJECT-ID>.md` (initial draft)

**Validation**: Architecture, components, and technical decisions documented

---

### Prompt 2-2: Design Validation

**File**: `../../prompts/prompt-2-2-design-validation.md`

**Input**: Initial design, codebase analysis

**Output**: Updated `DESIGN_<PROJECT-ID>.md` with feasibility assessment

**Validation**: Implementation feasibility confirmed with code references

---

### Prompt 2-3: Technical Review

**File**: `../../prompts/prompt-2-3-technical-review.md`

**Input**: Validated design

**Output**: Updated `DESIGN_<PROJECT-ID>.md` with feedback integrated

**Validation**: Technical stakeholder approval obtained

---

### Prompt 2-4: Design Finalization

**File**: `../../prompts/prompt-2-4-design-finalization.md`

**Input**: Reviewed design

**Output**: Final `DESIGN_<PROJECT-ID>.md`

**Validation**: Professional formatting applied, all sections complete

---

<<<<<<< HEAD
## Data Flow Diagram
```text
[SPECIFICATION.md] → [2-1 Initial Design] → DESIGN.md → [2-2 Design Validation] → DESIGN.md → [2-3 Technical Review] → DESIGN.md → [2-4 Finalization] → DESIGN.md (final)
```

## Error Handling
- **Step Failure**: Document issues; if conflicts found, loop back to specification
- **Recovery**: Refresh analysis and update design; re-run failed step
- **Rollback**: Maintain previous design versions before updates

=======
>>>>>>> c5759c0 (feat: Add orchestrator workflows for extra large changes including specification, design, planning, and implementation phases)
## Completion Criteria

✅ **Workflow complete when**:

1. All 4 prompts executed successfully
2. Final design document exists
3. Technical stakeholder approval documented
4. Ready to hand off to Workflow 3

---

## Handoff

**Next workflow**: `workflow-3-planning.md`

**Provides**: Final `DESIGN_<PROJECT-ID>.md` with approvals
