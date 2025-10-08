# Workflow 3: Planning (L)

## Overview

**Purpose**: Create comprehensive execution plans for large changes

**Input**: Artifacts from Workflow 2 (approved design)

**Output**: Test Plan, Documentation Plan, and Implementation Plans

---

## Prompt Execution

Execute all prompts in sequence - no skipping

### Prompt 3-1: Test Plan

**File**: `../../prompts/prompt-3-1-test-plan.md`

**Input**: `DESIGN_<PROJECT-ID>.md`, `SPECIFICATION_<PROJECT-ID>.md`

**Output**: `TEST_PLAN_<PROJECT-ID>.md`

**Validation**: All requirements covered, test cases defined, environments planned

---

### Prompt 3-2: Documentation Plan

**File**: `../../prompts/prompt-3-2-documentation-plan.md`

**Input**: `DESIGN_<PROJECT-ID>.md`, `SPECIFICATION_<PROJECT-ID>.md`

**Output**: `DOCUMENTATION_PLAN_<PROJECT-ID>.md`

**Validation**: All stakeholder documentation needs identified and planned

---

### Prompt 3-3: Implementation Plans

**File**: `../../prompts/prompt-3-3-implementation-plans.md`

**Input**: `DESIGN_<PROJECT-ID>.md`

**Output**: Multiple phase plans: `IMPLEMENTATION_PLAN_PHASE_*.md`

**Validation**: All design components covered, tasks breakdown complete, dependencies mapped

---

## Completion Criteria

✅ **Workflow complete when**:

1. All 3 prompts executed successfully
2. Test plan exists with comprehensive coverage
3. Documentation plan addresses all stakeholders
4. Implementation plans provide detailed task breakdown
5. Ready to hand off to Workflow 4

---

## Handoff

**Next workflow**: `workflow-4-implementation.md`

**Provides**: `TEST_PLAN_<PROJECT-ID>.md`, `DOCUMENTATION_PLAN_<PROJECT-ID>.md`, `IMPLEMENTATION_PLAN_PHASE_*.md`
