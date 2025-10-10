---
name: workflow-4-implementation-m
description: Medium change implementation producing working code, tests (>70% coverage), and documentation
tags: [workflow, sequential, treat-change-request]
---

# Workflow 4: Implementation (M)

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

**Purpose**: Code implementation and validation for medium changes

**Input**: Artifacts from Workflow 3 (implementation plan)

**Output**: Working code with tests (>70% coverage) and documentation

---

## Input Requirements
- **Primary Input**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`, `DESIGN_<PROJECT-ID>.md`
- **Secondary Inputs**: Context package as needed
- **Input Format**: Markdown plans and local repository

## Output Specifications
- **Primary Output**: Working code, `security-scan-results.md`, `test-results.md`
- **Secondary Outputs**: Documentation updates
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute all prompts in sequence - no skipping

### Prompt 4-1: Code Implementation

**File**: `../../prompts/prompt-4-1-implementation-execution.md`

**Input**: `IMPLEMENTATION_PLAN_<PROJECT-ID>.md`, `DESIGN_<PROJECT-ID>.md`

**Output**: Source code with tests and documentation

**Validation**: Code compiles, tests pass, coverage >70%

---

### Prompt 4-2: Security & Quality Validation

**File**: `../../prompts/prompt-4-2-validation.md`

**Input**: Implemented code

**Output**: `security-scan-results.md`, `test-results.md`

**Validation**: No critical security issues, all tests passing

---

## Data Flow Diagram
```text
[IMPLEMENTATION_PLAN.md + DESIGN.md] → [Step 4-1: Code Implementation] → code + tests → [Step 4-2: Security & Quality Validation] → security-scan-results.md, test-results.md
```

## Error Handling
- **Step Failure**: If build/tests/security checks fail, document in results and stop
- **Recovery**: Fix issues and re-run the failed step
- **Rollback**: Use VCS to revert partial/incorrect changes if necessary

## Completion Criteria
- [ ] Both prompts executed successfully
- [ ] Code complete and tested (>70% coverage)
- [ ] Senior Developer review approved
- [ ] Tech Lead validated
- [ ] Ready for deployment

---

## Handoff

**Next step**: Deployment following standard deployment process

**Provides**: Working codebase with tests, `security-scan-results.md`, `test-results.md`, and documentation
