# Workflow 2: Design (M)

## Overview

**Purpose**: Technical design for medium changes

**Input**: Context package from router

**Output**: Technical design document ready for planning phase

---

## Prompt Execution

Execute all prompts in sequence - no skipping

### Prompt 2-1: Technical Design

**File**: `../../prompts/prompt-2-1-technical-design.md`

**Input**: Context package from router, codebase

**Output**: `DESIGN_<PROJECT-ID>.md`

**Validation**: Architecture and technical approach documented

---

### Prompt 2-3: Design Review

**File**: `../../prompts/prompt-2-3-design-review.md`

**Input**: `DESIGN_<PROJECT-ID>.md`

**Output**: `design-review-report.md`

**Validation**: Tech Lead approval obtained

---

## Completion Criteria

✅ **Workflow complete when**:

1. Both prompts executed successfully
2. Design document complete
3. Design review approved
4. Ready to hand off to Workflow 3

---

## Handoff

**Next workflow**: `workflow-3-planning.md`

**Provides**: `DESIGN_<PROJECT-ID>.md`, `design-review-report.md`
