# Orchestrator 0: Change Router

**Purpose**: Entry point for all changes - evaluates, sizes, and routes to appropriate orchestrator.

**Version**: 2.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Entry point for all change requests. Executes four workflows in sequence:

1. Git branch validation and setup
2. Gather comprehensive change information
3. Evaluate size objectively using matrices
4. Route to the appropriate orchestrator

---

## Workflows

```
Orchestrator-0-Router
├── Workflow 0-0: Git Branch Setup
├── Workflow 0-1: Information Gathering
├── Workflow 0-2: Size Evaluation
└── Workflow 0-3: Routing & Dispatch
```

---

## Inputs

| Input | Description | Required |
|-------|-------------|----------|
| **Issue IDs** | One or more issue IDs (e.g., SACP-172207) or JIRA export | Yes |
| **Requestor** | Person requesting the change | Yes |
| **Priority** | Business priority (Critical/High/Medium/Low) | Yes |
| **Target Date** | Desired completion date (if any) | No |
| **Initial Context** | Any additional context from the requestor | No |

---

## Outputs

| Output | Description |
|--------|-------------|
| **Size Classification** | XL, L, M, S, or XS |
| **Target Orchestrator** | Which orchestrator to route to |
| **Sizing Rationale** | Documented reasoning for size decision |
| **Context Package** | All gathered information for the target orchestrator |
| **Routing Metadata** | Tracking information, timestamps, approvals |
| **Analysis Directory** | Complete analysis with all artifacts |
| **Tracking File** | `0-tracking.md` - Progress tracking for all workflows |

---

## Workflow Execution

### Workflow 0-0: Git Branch Setup

**File**: `../workflows/router/workflow-0-0-git-branch-setup.md`

**Input**: Current git repository state

**Outputs**: `0-branch-setup.md`

**Validation**: Work is being done in appropriate branch (not main/master)

---

### Workflow 0-1: Information Gathering

**File**: `../workflows/router/workflow-0-1-information-gathering.md`

**Input**: Analysis directory path (to validate prerequisites)

**Outputs**: 
- Prerequisite validation (confirms `prerequisite-3-change-request.md` exists)
- `2-technical-scope-analysis.md` (router-specific technical analysis)
- `3-risk-assessment.md` (router-specific risk analysis)

**Validation**: Prerequisite-3 exists AND 2 router-specific files created before proceeding

**Note**: `1-change-request-summary.md` NO LONGER CREATED (eliminated 90% duplication with prerequisite-3)

---

### Workflow 0-2: Size Evaluation

**File**: `../workflows/router/workflow-0-2-size-evaluation.md`

**Input**: Artifacts from Workflow 0-1

**Outputs**: `4-size-evaluation-matrix.md`, `5-final-size-decision.md`

**Validation**: Both files must exist and size (XL/L/M/S/XS) must be stated before proceeding

---

### Workflow 0-3: Routing & Dispatch

**File**: `../workflows/router/workflow-0-3-routing-dispatch.md`

**Input**: Artifacts from Workflows 0-1 and 0-2

**Outputs**: `6-context-package.yaml`, `7-routing-summary.md`, `README.md`

**Validation**: All 3 files must exist and target orchestrator must be identified

---

### Completion Criteria

✅ **Router execution is complete when**:

1. Work is being done in appropriate branch (not main/master)
2. Prerequisite change request validated (`prerequisite-3-change-request.md` complete)
3. All 7 router-specific output files exist (see Success Criteria below)
4. Final size classification is documented
5. Target orchestrator is clearly identified
6. Context package is ready for handoff

**Note**: Total files reduced from 8 to 7 (eliminated duplicate `1-change-request-summary.md`)

---

## Success Criteria

This orchestrator is successful when:

### Required Outputs (File Validation)

- ✅ **Prerequisite validation**: `prerequisite-3-change-request.md` exists and is complete
- ✅ **Workflow 0-0 outputs**: `0-branch-setup.md`
- ✅ **Workflow 0-1 outputs**: `2-technical-scope-analysis.md`, `3-risk-assessment.md`
  - **ELIMINATED**: ~~`1-change-request-summary.md`~~ (90% duplicate of prerequisite-3)
- ✅ **Workflow 0-2 outputs**: `4-size-evaluation-matrix.md`, `5-final-size-decision.md`
- ✅ **Workflow 0-3 outputs**: `6-context-package.yaml`, `7-routing-summary.md`, `README.md`

**Total Router Files**: 7 (down from 8 - duplication eliminated)

### Required Decisions Documented

- ✅ Prerequisite change request validated (complete with Epic, Features, MVP, Open Questions)
- ✅ Size classification determined (XL/L/M/S/XS) with rationale in `5-final-size-decision.md`
- ✅ Target orchestrator identified in `7-routing-summary.md`
- ✅ Context package contains all necessary information for handoff

---

## Next Steps

After this orchestrator completes:

1. **Invoke target orchestrator** with the context package from `6-context-package.yaml`
2. **Team begins work** following the workflows of the target orchestrator
3. **Optional**: Set up escalation monitoring if re-sizing detection is needed
4. **Optional**: Update router metrics for continuous improvement

---

## Exception Handling

If during workflow execution the change is determined to be:

- **Out of scope**: Not a code change, configuration only, infrastructure only
- **Blocked**: Dependencies not available, requirements incomplete
- **Requires splitting**: Too large, should be broken into multiple changes

**Actions**: Document in workflow outputs, return to requestor with recommendation, do not complete routing until ready

---

## End of Orchestrator

**Version**: 2.1  
**Last Updated**: October 8, 2025
**Execution Model**: Delegate to workflows (0-0 → 0-1 → 0-2 → 0-3)  
**Validation**: Check prerequisite-3 exists + 7 router output files before completion

**Changelog v2.1**:
- ✅ Eliminated duplicate `1-change-request-summary.md` (90% overlap with prerequisite-3)
- ✅ Added prerequisite validation at start of Workflow 0-1
- ✅ Router now stops if prerequisites incomplete
- ✅ Reduced router files from 8 to 7 (efficiency improvement)
