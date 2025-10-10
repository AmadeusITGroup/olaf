---
name: workflow-1-specification-l
description: Large change specification producing SPECIFICATION_<PROJECT-ID>.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 1: Specification (L)

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

**Purpose**: Define comprehensive requirements specification for large changes

**Input**: Context package from router

**Output**: Validated and approved specification document ready for design phase

---

## Input Requirements
- **Primary Input**: Context package from router
- **Secondary Inputs**: JIRA ticket, codebase for validation
- **Input Format**: Markdown/YAML context

## Output Specifications
- **Primary Output**: `SPECIFICATION_<PROJECT-ID>.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Prompt Execution

Execute all prompts in sequence - no skipping

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

## Data Flow Diagram
```text
[Context package + JIRA] → [1-1 Initial Spec] → SPEC.md → [1-2 Codebase Validation] → SPEC.md → [1-3 User Review] → SPEC.md → [1-4 Finalization] → SPEC.md (final)
```

## Error Handling
- **Step Failure**: If inputs missing or feasibility fails, document and stop
- **Recovery**: Gather missing inputs, refine scope, or adjust requirements; re-run failed step
- **Rollback**: Maintain previous SPEC version before updates

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
