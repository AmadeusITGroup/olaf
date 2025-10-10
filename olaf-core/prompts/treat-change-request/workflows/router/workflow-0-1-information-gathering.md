---
name: workflow-0-1-information-gathering
description: Gather comprehensive information to enable accurate sizing and routing
tags: [workflow, sequential, treat-change-request]
---

# Workflow 0-1: Information Gathering

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

**Purpose**: Gather comprehensive information about the change request to enable accurate sizing and routing
**Input**: JIRA ticket, issue ID, or business requirement document
**Output**: Three analysis documents providing complete context

---

## Prerequisites

- `prerequisite-3-change-request.md` exists and is complete in the analysis directory.
- Access to the codebase for technical scope analysis.

---

## Input Requirements
- **Primary Input**: Path to analysis directory containing `prerequisite-3-change-request.md`
- **Secondary Inputs**: Access to codebase for scope analysis
- **Input Format**: Markdown documents under the analysis directory

## Output Specifications
- **Primary Output**: `2-technical-scope-analysis.md`, `3-risk-assessment.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute all steps in sequence (no skipping).

### Prompt 0-1-1: Prerequisite Validation & Change Request Check

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-0-1-1-change-request-analysis.md`

**Input**: Analysis directory path (e.g., `olaf-works/demand/SACP-172207-analysis/`)

**Output**: Validation notes and confirmed `prerequisite-3-change-request.md`

**Description**: Validate presence and completeness of prerequisite change request artifacts and prepare inputs for subsequent steps.

**Validation**: `prerequisite-3-change-request.md` exists and key sections are complete.

---

### Prompt 0-1-2: Technical Scope Analysis

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-0-1-2-technical-scope-analysis.md`

**Input**: `prerequisite-3-change-request.md` + codebase

**Output**: `2-technical-scope-analysis.md`

**Validation**: Modules identified, file/LOC estimates, API/DB changes, integrations mapped

---

### Prompt 0-1-3: Risk Assessment

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-0-1-3-risk-assessment.md`

**Input**: Artifacts from Prompts 0-1-1 and 0-1-2

**Output**: `3-risk-assessment.md`

**Validation**: All 4 risk dimensions assessed (Business, Technical, Security, Operational)

---

## Data Flow Diagram
```text
[prerequisite-3-change-request.md] → [Step 0-1-2: Technical Scope] → 2-technical-scope-analysis.md
                                                ↓
                                   [Step 0-1-3: Risk Assessment] → 3-risk-assessment.md
```

## Error Handling
- **Step Failure**: Document missing inputs and stop; return to prerequisite workflows if needed
- **Recovery**: After fixing inputs, re-run from the failed step
- **Rollback**: Not applicable (read-only analysis); maintain prior outputs separately

## Completion Criteria
- [ ] All steps completed successfully
- [ ] `2-technical-scope-analysis.md` and `3-risk-assessment.md` generated under results folder
- [ ] No critical errors encountered

## Next Steps
- Proceed to `workflow-0-2-size-evaluation.md`

## Handoff

**Next workflow**: `workflow-0-2-size-evaluation.md`

**Provides**:

- `prerequisite-3-change-request.md` (from prerequisites - business requirements)
- `2-technical-scope-analysis.md` (router-specific - technical detail)
- `3-risk-assessment.md` (router-specific - risk analysis)
