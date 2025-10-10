---
name: workflow-4-implementation-xl
description: Extra large change implementation executing implementation, documentation, and testing plans
tags: [workflow, sequential, treat-change-request]
---

# Workflow 4: Implementation (XL)



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

## Overview



**Purpose**: Execute all planned work through AI automation for extra large changes



**Input**: Planning documents from Phase 3 (Implementation Plans, Documentation Plan, Test Plan)

**Output**: Working software with documentation and functional tests

**Output**: Working software with documentation and functional tests

## Input Requirements
- **Primary Inputs**: `IMPLEMENTATION_PLAN_PHASE_*.md`, `DOCUMENTATION_PLAN_<PROJECT-ID>.md`, `TEST_PLAN_<PROJECT-ID>.md`, `DESIGN_<PROJECT-ID>.md`
- **Secondary Inputs**: None
- **Input Format**: Markdown plans and local repository

## Output Specifications
- **Primary Outputs**: Working codebase, complete documentation suite, automated functional test suite
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

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

## Data Flow Diagram
```text
[IMPLEMENTATION_PLAN_PHASE_*.md + DESIGN.md] → [4-1 Implementation Execution] → codebase
                                       ↓
                           [4-2 Documentation Execution] → documentation suite
                                       ↓
                           [4-3 Functional Testing Execution] → functional test suite
```

## Error Handling
- **Step Failure**: If build/tests/documentation generation fail, document and stop
- **Recovery**: Fix issues and re-run failed step
- **Rollback**: Use VCS to revert partial/incorrect changes if necessary

## Completion Criteria
- [ ] All 3 prompts executed successfully
- [ ] Working software implements all requirements
- [ ] Documentation accurately describes functionality
- [ ] Functional tests validate business requirements
- [ ] System ready for deployment

## Handoff

**Next step**: Deployment following standard deployment process

**Provides**: Working codebase, documentation, automated tests, deployment procedures
