# Workflow 4: Implementation (L)

## Overview

**Purpose**: Execute all planned work through AI automation for large changes

**Input**: Artifacts from Workflow 3 (planning documents)

**Output**: Working software with documentation and functional tests

---

## Prompt Execution

Execute all prompts in sequence - no skipping

### Prompt 4-1: Implementation Execution

**File**: `../../prompts/prompt-4-1-implementation-execution.md`

**Input**: `IMPLEMENTATION_PLAN_PHASE_*.md`, `DESIGN_<PROJECT-ID>.md`

**Output**: Working codebase with full functionality

**Validation**: All components implemented, unit tests pass, code compiles

---

### Prompt 4-2: Documentation Execution

**File**: `../../prompts/prompt-4-2-documentation-execution.md`

**Input**: `DOCUMENTATION_PLAN_<PROJECT-ID>.md`, implemented code

**Output**: Complete documentation suite

**Validation**: All stakeholder documentation created, examples work with actual code

---

### Prompt 4-3: Functional Testing Execution

**File**: `../../prompts/prompt-4-3-functional-testing-execution.md`

**Input**: `TEST_PLAN_<PROJECT-ID>.md`, implemented features

**Output**: Automated functional test suite with Gherkin scenarios

**Validation**: Key scenarios covered, tests executable, business rules validated

---

## Completion Criteria

✅ **Workflow complete when**:

1. All 3 prompts executed successfully
2. Working software implements all requirements
3. Documentation accurately describes functionality
4. Functional tests validate business requirements
5. System ready for deployment

---

## Handoff

**Next step**: Deployment following standard deployment process

**Provides**: Working codebase, documentation, automated tests, deployment procedures
