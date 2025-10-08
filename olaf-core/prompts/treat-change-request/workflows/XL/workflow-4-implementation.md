<<<<<<< HEAD
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
=======
# Workflow 4: Implementation (XL)# Workflow 4: Execution Phase



## Overview## Overview



**Purpose**: Execute all planned work through AI automation for extra large changesThe Execution Phase transforms planning documents into actual working software. This workflow executes the implementation, documentation, and testing plans created in Phase 3, with AI doing the heavy lifting of code generation, documentation writing, and test creation.



**Input**: Artifacts from Workflow 3 (planning documents)**Input**: Planning documents from Phase 3 (Implementation Plans, Documentation Plan, Test Plan)
>>>>>>> c5759c0 (feat: Add orchestrator workflows for extra large changes including specification, design, planning, and implementation phases)

**Output**: Working software with documentation and functional tests

**Output**: Working software with documentation and functional tests

<<<<<<< HEAD
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
=======
## 📋 Task Tracking Reminder

---

**IMPORTANT**: Update the Master Task Checklist in `orchestrator/main-orchestrator.md` (or your working document) as you complete each step:

## Prompt Execution

- [ ] **Step 4.1** - Implementation Execution

Execute all prompts in sequence - no skipping- [ ] **Step 4.2** - Documentation Execution

- [ ] **Step 4.3** - Functional Testing Execution

### Prompt 4-1: Implementation Execution- [ ] **Phase 4 Complete** - Feature fully implemented, documented, and tested



**File**: `../../prompts/prompt-4-1-implementation-execution.md`Check ✅ each box as you complete it to track progress.



**Input**: `IMPLEMENTATION_PLAN_PHASE_*.md`, `DESIGN_<PROJECT-ID>.md`---



**Output**: Working codebase with full functionality## Phase Purpose



**Validation**: All components implemented, unit tests pass, code compiles**WHAT**: Execute all planned work through AI automation

**HOW**: Use AI prompts to generate code, documentation, and tests

---**WHY**: Minimize manual work and accelerate delivery through automation



### Prompt 4-2: Documentation Execution## Execution Order



**File**: `../../prompts/prompt-4-2-documentation-execution.md`### Step 4.1: Implementation Execution

**Prompt File**: `../../prompts/prompt-4-1-implementation-execution.md`

**Input**: `DOCUMENTATION_PLAN_<PROJECT-ID>.md`, implemented code

**Purpose**: AI generates actual code based on implementation tasks

**Output**: Complete documentation suite

**Process**:

**Validation**: All stakeholder documentation created, examples work with actual code1. Load Implementation Plan tasks from Phase 3

2. Execute each task through AI code generation

---3. Apply TDD approach (tests first, then implementation)

4. Generate working code with proper structure and patterns

### Prompt 4-3: Functional Testing Execution5. Validate code compiles and unit tests pass



**File**: `../../prompts/prompt-4-3-functional-testing-execution.md`**Expected Output**: Working codebase with full functionality



**Input**: `TEST_PLAN_<PROJECT-ID>.md`, implemented features### Step 4.2: Documentation Execution  

**Prompt File**: `../../prompts/prompt-4-2-documentation-execution.md`

**Output**: Automated functional test suite with Gherkin scenarios

**Purpose**: AI generates actual documentation based on implemented features

**Validation**: Key scenarios covered, tests executable, business rules validated

**Process**:

---1. Load Documentation Plan tasks from Phase 3

2. Analyze implemented code to understand actual functionality

## Completion Criteria3. Generate user documentation, API docs, and technical guides

4. Create examples and code samples based on real implementation

✅ **Workflow complete when**:5. Validate documentation accuracy against actual code behavior



1. All 3 prompts executed successfully**Expected Output**: Complete documentation suite matching implemented features

2. Working software implements all requirements

3. Documentation accurately describes functionality### Step 4.3: Functional Testing Execution

4. Functional tests validate business requirements**Prompt File**: `../../prompts/prompt-4-3-functional-testing-execution.md`

5. System ready for deployment

**Purpose**: AI generates functional tests as Gherkin scenarios that can be automated

---

**Process**:

## Handoff1. Load Test Plan requirements from Phase 3

2. Analyze implemented features to understand actual behavior

**Next step**: Deployment following standard deployment process3. Generate Gherkin scenarios for functional testing

4. Create test automation code for the Gherkin scenarios

**Provides**: Working codebase, documentation, automated tests, deployment procedures5. Focus on functional tests rather than complex integration tests


**Expected Output**: Automated functional test suite with Gherkin scenarios

## Key Principles

### AI-First Execution
- AI generates actual code, not just plans
- AI creates real documentation from implemented features
- AI writes executable test scenarios
- Minimal human intervention required

### Immediate Execution
- AI executes tasks as fast as possible
- Iterative execution with immediate validation
- Continuous feedback and correction

### Practical Testing Approach
- Focus on functional tests that AI can create and run
- Use Gherkin scenarios for business-readable tests
- Avoid complex integration tests that are hard for AI
- Emphasize automated, repeatable test scenarios

### Code-Documentation Alignment
- Documentation generated from actual implemented code
- Examples and samples based on real working features
- API documentation reflects actual endpoints and responses
- User guides match actual UI and workflows

## Quality Validation

### Implementation Execution Complete When:
- [ ] All planned components are implemented and compile successfully
- [ ] Unit tests pass with appropriate coverage
- [ ] Code follows established patterns and standards
- [ ] Integration points work as designed
- [ ] Performance meets basic requirements

### Documentation Execution Complete When:
- [ ] All stakeholder documentation types are created
- [ ] Documentation accurately reflects implemented features
- [ ] Code examples work with actual implementation
- [ ] API documentation matches actual endpoints
- [ ] User workflows are documented and verified

### Functional Testing Execution Complete When:
- [ ] Key user scenarios are covered by Gherkin tests
- [ ] Functional tests can be executed automatically
- [ ] Business rules are validated through test scenarios
- [ ] Critical workflows are tested end-to-end
- [ ] Test results provide clear pass/fail feedback

## Success Criteria

### Phase 4 Complete When:
- [ ] Working software implements all specification requirements
- [ ] Documentation accurately describes implemented functionality
- [ ] Functional tests validate business requirements
- [ ] All deliverables are execution-ready (not just planned)
- [ ] System can be deployed and used by intended users

### Handoff to Deployment:
- Working codebase ready for deployment
- Complete documentation for users and operators
- Automated functional tests for ongoing validation
- Clear deployment and operation procedures
- Minimal manual setup or configuration required

## Execution Benefits

### Speed and Efficiency
- AI execution eliminates manual development time
- Fast AI-driven generation instead of traditional development cycles
- Automated testing reduces QA cycles
- Documentation stays current with implementation

### Quality and Consistency
- AI follows consistent patterns and standards
- Generated tests cover planned scenarios systematically
- Documentation matches actual implementation behavior
- Reduced human error in routine tasks

### Maintainability
- Code generated with modern patterns and practices
- Documentation automatically aligned with code
- Test scenarios provide living specification
- Changes can be regenerated quickly through AI

## Integration with Previous Phases

**From Specification Phase (Phase 1)**:
- Requirements drive implementation priorities
- Business rules become functional test scenarios
- User stories guide documentation content

**From Design Phase (Phase 2)**:
- Architecture guides code structure and patterns
- API specifications become actual endpoints
- Technical decisions drive implementation approach

**From Planning Phase (Phase 3)**:
- Implementation tasks become AI generation prompts
- Documentation plan guides content creation priorities
- Test plan becomes functional scenario coverage

This execution phase ensures that all planning work translates into actual deliverable software through AI automation, minimizing manual effort while maximizing quality and speed.
>>>>>>> c5759c0 (feat: Add orchestrator workflows for extra large changes including specification, design, planning, and implementation phases)
