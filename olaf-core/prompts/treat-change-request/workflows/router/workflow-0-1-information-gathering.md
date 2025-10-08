# Workflow 0-1: Information Gathering

## Overview

**Purpose**: Gather comprehensive information about the change request to enable accurate sizing and routing

**Input**: JIRA ticket, issue ID, or business requirement document

**Output**: Three analysis documents providing complete context

---

## Prompt Execution

**Execute all prompts in sequence - no skipping**

### Prompt 0-1-1: Prerequisite Validation & Change Request Check

**File**: `../prompts/prompt-0-1-1-change-request-analysis.md`

**Input**: Analysis directory path (e.g., `olaf-works/demand/SACP-172207-analysis/`)

**Output**: 
- **If prerequisite-3-change-request.md exists**: No output (validation only)
- **If prerequisite-3 missing**: STOP execution, return error to user

**Validation**: 
- ✅ Prerequisite change request exists and is complete (Epic, Features, MVP, Open Questions)
- ❌ If missing: Stop router, request prerequisite phase completion

---

### Prompt 0-1-2: Technical Scope Analysis

**File**: `../prompts/prompt-0-1-2-technical-scope-analysis.md`

**Input**: `1-change-request-summary.md` + codebase

**Output**: `2-technical-scope-analysis.md`

**Validation**: Modules identified, file/LOC estimates, API/DB changes, integrations mapped

---

### Prompt 0-1-3: Risk Assessment

**File**: `../prompts/prompt-0-1-3-risk-assessment.md`

**Input**: Artifacts from Prompts 0-1-1 and 0-1-2

**Output**: `3-risk-assessment.md`

**Validation**: All 4 risk dimensions assessed (Business, Technical, Security, Operational)

---

## Completion Criteria

✅ **Workflow complete when**:

1. **Prerequisite change request validated** (`prerequisite-3-change-request.md` exists and is complete)
2. **2 router-specific output files created**: `2-technical-scope-analysis.md`, `3-risk-assessment.md`
3. Each file contains required analysis with evidence-based estimates
4. Ready to hand off to Workflow 0-2

**Note**: `1-change-request-summary.md` is NO LONGER CREATED (eliminated duplication - use prerequisite-3 directly)

---

## Handoff

**Next workflow**: `workflow-0-2-size-evaluation.md`

**Provides**: 
- `prerequisite-3-change-request.md` (from prerequisites - business requirements)
- `2-technical-scope-analysis.md` (router-specific - technical detail)
- `3-risk-assessment.md` (router-specific - risk analysis)
