# Workflow 1: Specification (XL)

## Overview

**Purpose**: Define comprehensive requirements specification for extra large changes

**Input**: Context package from router

**Output**: Validated and approved specification document ready for design phase

---

## Prompt Execution

**Execute all prompts in sequence - no skipping**

### Prompt 1-1: Initial Specification

**File**: `../../prompts/prompt-1-1-initial-specification.md`

**Input**: Context package from router, JIRA ticket

**Output**: `SPECIFICATION_<PROJECT-ID>.md` (initial draft)

**Validation**: All functional and non-functional requirements documented

---

### Prompt 1-2: Codebase Validation

**File**: `../../prompts/prompt-1-2-codebase-validation.md`

**Input**: Initial specification, codebase analysis

**Output**: Updated `SPECIFICATION_<PROJECT-ID>.md` with feasibility assessment

**Validation**: Technical feasibility confirmed with code references

---

### Prompt 1-3: User Review

**File**: `../../prompts/prompt-1-3-user-review.md`

**Input**: Validated specification

**Output**: Updated `SPECIFICATION_<PROJECT-ID>.md` with feedback integrated

**Validation**: Stakeholder approval obtained

---

### Prompt 1-4: Specification Finalization

**File**: `../../prompts/prompt-1-4-finalization.md`

**Input**: Reviewed specification

**Output**: Final `SPECIFICATION_<PROJECT-ID>.md`

**Validation**: Professional formatting applied, all sections complete

---

## Completion Criteria

✅ **Workflow complete when**:

1. All 4 prompts executed successfully
2. Final specification document exists
3. Stakeholder approval documented
4. Ready to hand off to Workflow 2

---

## Handoff

**Next workflow**: `workflow-2-design.md`

**Provides**: Final `SPECIFICATION_<PROJECT-ID>.md` with approvals
