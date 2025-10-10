---
name: workflow-3-planning-l
description: Large change planning producing TEST_PLAN, DOCUMENTATION_PLAN and IMPLEMENTATION_PLAN_PHASE_*.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 3: Planning (L)

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

## Overview

**Purpose**: Create comprehensive execution plans for large changes

**Input**: Artifacts from Workflow 2 (approved design)

**Output**: Test Plan, Documentation Plan, and Implementation Plans

---

## Input Requirements
- **Primary Input**: `DESIGN_<PROJECT-ID>.md`, `SPECIFICATION_<PROJECT-ID>.md`
- **Secondary Inputs**: None
- **Input Format**: Markdown design/spec documents

## Output Specifications
- **Primary Outputs**: `TEST_PLAN_<PROJECT-ID>.md`, `DOCUMENTATION_PLAN_<PROJECT-ID>.md`, `IMPLEMENTATION_PLAN_PHASE_*.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

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

## Data Flow Diagram
```text
[DESIGN.md + SPEC.md] → [3-1 Test Plan] → TEST_PLAN.md
                              ↓
                       [3-2 Documentation Plan] → DOCUMENTATION_PLAN.md
                              ↓
                       [3-3 Implementation Plans] → IMPLEMENTATION_PLAN_PHASE_*.md
```

## Error Handling
- **Step Failure**: If inputs are incomplete, request missing items and stop
- **Recovery**: Provide missing context and re-run failed step
- **Rollback**: Not applicable; plans can be regenerated

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
