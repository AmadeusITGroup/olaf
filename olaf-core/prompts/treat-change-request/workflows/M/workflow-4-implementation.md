# Workflow 4: Implementation (M)

## Overview

**Purpose**: Code implementation and validation for medium changes

**Input**: Artifacts from Workflow 3 (implementation plan)

**Output**: Working code with tests (>70% coverage) and documentation

---

## Prompt Execution

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

## Completion Criteria

✅ **Workflow complete when**:

1. Both prompts executed successfully
2. Code complete and tested
3. Senior Developer review approved
4. Tech Lead validated
5. Ready for deployment

---

## Handoff

**Next step**: Deployment following standard deployment process

**Provides**: Working codebase with tests and documentation
