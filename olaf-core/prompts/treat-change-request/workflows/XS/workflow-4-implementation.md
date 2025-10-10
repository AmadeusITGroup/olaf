---
name: workflow-4-implementation-xs
description: Extra small change implementation producing working code and automated validation
tags: [workflow, sequential, treat-change-request]
---

# Workflow 4: Implementation (XS)

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

**Purpose**: Direct code implementation and automated validation for extra small changes

**Input**: Artifacts from Workflow 3 (`implementation-notes.md`)

**Output**: Working code with basic tests and minimal documentation

---

## Input Requirements
- **Primary Input**: `implementation-notes.md`
- **Secondary Inputs**: Context package from router
- **Input Format**: Markdown plan and local repository

## Output Specifications
- **Primary Output**: Working code and `test-results.md`
- **Secondary Outputs**: Minimal update notes `implementation-changes.md`
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute all prompts in sequence - no skipping

### Prompt 4-1: Code Implementation

**File**: `../../prompts/prompt-4-1-implementation-execution.md`

**Input**: `implementation-notes.md`, context package

**Output**: Source code with basic tests

**Validation**: Code works, basic tests pass

---

### Prompt 4-2: Automated Validation

**File**: `../../prompts/prompt-4-2-validation.md`

**Input**: Implemented code

**Output**: Automated test results, security scan

**Validation**: Automated checks passing

---

## Data Flow Diagram
```text
[implementation-notes.md] → [Step 4-1: Code Implementation] → code + tests → [Step 4-2: Automated Validation] → test-results.md
```

## Error Handling
- **Step Failure**: If build or tests fail, capture logs in `test-results.md` and stop
- **Recovery**: Fix issues, re-run failed step
- **Rollback**: Use VCS to revert partial changes if needed

## Completion Criteria
- [ ] Both prompts executed successfully
- [ ] Code complete and tested
- [ ] Peer review approved (or post-merge acceptable)
- [ ] Automated checks passing
- [ ] Ready for immediate deployment

---

## Handoff

**Next step**: Can be deployed immediately if checks pass

**Provides**: Working code with automated validation and `test-results.md`
