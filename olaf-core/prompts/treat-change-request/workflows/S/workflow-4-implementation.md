---
name: workflow-4-implementation-s
description: Small change implementation producing working code, tests (>60% coverage) and documentation
tags: [workflow, sequential, treat-change-request]
---

# Workflow 4: Implementation (S)

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

**Purpose**: Code implementation and validation for small changes

**Input**: Artifacts from Workflow 3 (`IMPLEMENTATION_PLAN_<PROJECT-ID>.md`)

**Output**: Working code with tests (>60% coverage) and basic documentation

---

## Input Requirements
- **Primary Input**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`
- **Secondary Inputs**: Context package and design/spec references as needed
- **Input Format**: Markdown plan and local repository

## Output Specifications
- **Primary Output**: Working code, `test-results.md`
- **Secondary Outputs**: `security-scan-results.md`
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute all prompts in sequence - no skipping

### Prompt 4-1: Code Implementation

**File**: `../../prompts/prompt-4-1-implementation-execution.md`

**Input**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`

**Output**: Source code with tests and documentation

**Validation**: Code compiles, tests pass, coverage >60%

---

### Prompt 4-2: Security & Quality Validation

**File**: `../../prompts/prompt-4-2-validation.md`

**Input**: Implemented code

**Output**: `test-results.md`, automated security checks

**Validation**: All automated checks passing

---

## Data Flow Diagram
```text
[IMPLEMENTATION_PLAN.md] → [Step 4-1: Code Implementation] → code + tests → [Step 4-2: Security & Quality Validation] → test-results.md, security-scan-results.md
```

## Error Handling
- **Step Failure**: If build/tests/security checks fail, document in results and stop
- **Recovery**: Fix issues and re-run the failed step
- **Rollback**: Use VCS to revert partial/incorrect changes if necessary

## Completion Criteria
- [ ] Both prompts executed successfully
- [ ] Code complete and tested (>60% coverage)
- [ ] Peer review approved
- [ ] Optional Tech Lead review (if needed)
- [ ] Ready for deployment

---

## Handoff

**Next step**: Deployment following standard deployment process

**Provides**: Working codebase with tests, `test-results.md`, and documentation
