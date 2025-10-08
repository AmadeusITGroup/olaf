# Workflow 2: Design (XL)

## Overview

**Purpose**: Define comprehensive technical design for extra large changes

**Input**: Artifacts from Workflow 1 (approved specification)

**Output**: Complete technical design document ready for planning phase

---

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
