# Workflow 4: Implementation (S)

## Overview

**Purpose**: Code implementation and validation for small changes

**Input**: Artifacts from Workflow 3 (implementation plan)

**Output**: Working code with tests (>60% coverage) and basic documentation

---

## Prompt Execution

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

## Completion Criteria

✅ **Workflow complete when**:

1. Both prompts executed successfully
2. Code complete and tested
3. Peer review approved
4. Optional Tech Lead review (if needed)
5. Ready for deployment

---

## Handoff

**Next step**: Deployment following standard deployment process

**Provides**: Working codebase with tests and documentation
