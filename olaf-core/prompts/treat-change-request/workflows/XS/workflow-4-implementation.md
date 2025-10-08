# Workflow 4: Implementation (XS)

## Overview

**Purpose**: Direct code implementation and automated validation for extra small changes

**Input**: Artifacts from Workflow 3 (implementation approach)

**Output**: Working code with basic tests and minimal documentation

---

## Prompt Execution

Execute all prompts in sequence - no skipping

### Prompt 4-1: Code Implementation

**File**: `../../prompts/prompt-4-1-implementation-execution.md`

**Input**: Implementation approach, context package

**Output**: Source code with basic tests

**Validation**: Code works, basic tests pass

---

### Prompt 4-2: Automated Validation

**File**: `../../prompts/prompt-4-2-validation.md`

**Input**: Implemented code

**Output**: Automated test results, security scan

**Validation**: Automated checks passing

---

## Completion Criteria

✅ **Workflow complete when**:

1. Both prompts executed successfully
2. Code complete and tested
3. Peer review approved (or post-merge acceptable)
4. Automated checks passing
5. Ready for immediate deployment

---

## Handoff

**Next step**: Can be deployed immediately if checks pass

**Provides**: Working code with automated validation
