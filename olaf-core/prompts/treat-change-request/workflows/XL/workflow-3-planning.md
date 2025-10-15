<<<<<<< HEAD
---
name: workflow-3-planning-xl
description: Extra large change planning producing TEST_PLAN, DOCUMENTATION_PLAN and IMPLEMENTATION_PLAN_PHASE_*.md
tags: [workflow, sequential, treat-change-request]
---

# Workflow 3: Planning (XL)



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



**Purpose**: Create comprehensive execution plans for extra large changes



## Prompt Execution

Execute all prompts in sequence - no skipping

### Prompt 3-1: Test Plan

**File**: `../../prompts/prompt-3-1-test-plan.md`

**Input**: `DESIGN_<PROJECT-ID>.md`, `SPECIFICATION_<PROJECT-ID>.md`

**Output**: `TEST_PLAN_<PROJECT-ID>.md`

**Validation**: All requirements covered, test cases defined, environments planned

### Prompt 3-2: Documentation Plan

**File**: `../../prompts/prompt-3-2-documentation-plan.md`

**Input**: `DESIGN_<PROJECT-ID>.md`, `SPECIFICATION_<PROJECT-ID>.md`

**Output**: `DOCUMENTATION_PLAN_<PROJECT-ID>.md`

**Validation**: All stakeholder documentation needs identified and planned

### Prompt 3-3: Implementation Plans

**File**: `../../prompts/prompt-3-3-implementation-plans.md`


**Output**: Multiple phase plans: `IMPLEMENTATION_PLAN_PHASE_*.md`

**Validation**: All design components covered, tasks breakdown complete, dependencies mapped

## Data Flow Diagram
```text
[DESIGN.md + SPEC.md] → [3-1 Test Plan] → TEST_PLAN.md
                              ↓
                       [3-2 Documentation Plan] → DOCUMENTATION_PLAN.md
                              ↓
                       [3-3 Implementation Plans] → IMPLEMENTATION_PLAN_PHASE_*.md
```

## Error Handling
- **Step Failure**: If inputs are incomplete, request missing items and stop
- **Recovery**: Provide missing context and re-run failed step
- **Rollback**: Not applicable; plans can be regenerated

## Completion Criteria

✅ **Workflow complete when**:

1. All 3 prompts executed successfully
2. Test plan exists with comprehensive coverage
3. Documentation plan addresses all stakeholders
4. Implementation plans provide detailed task breakdown
5. Ready to hand off to Workflow 4

## Handoff

**Next workflow**: `workflow-4-implementation.md`

**Provides**: `TEST_PLAN_<PROJECT-ID>.md`, `DOCUMENTATION_PLAN_<PROJECT-ID>.md`, `IMPLEMENTATION_PLAN_PHASE_*.md`
=======
# Workflow 3: Planning (XL)# Workflow 3: Planning Phase



## Overview## Overview



**Purpose**: Create comprehensive execution plans for extra large changesThe Planning Phase transforms the approved technical design into comprehensive execution plans. This workflow creates three essential planning documents that guide the implementation phase.



**Input**: Artifacts from Workflow 2 (approved design)**Input**: Finalized design document from Phase 2

**Output**: Test Plan, Documentation Plan, and Implementation Plans

**Output**: Test Plan, Documentation Plan, and Implementation Plans

## 📋 Task Tracking Reminder

---

**IMPORTANT**: Update the Master Task Checklist in `orchestrator/main-orchestrator.md` (or your working document) as you complete each step:

## Prompt Execution

- [ ] **Step 3.1** - Test Plan Creation

Execute all prompts in sequence - no skipping- [ ] **Step 3.2** - Documentation Plan Creation

- [ ] **Step 3.3** - Implementation Plans Creation

### Prompt 3-1: Test Plan- [ ] **Phase 3 Complete** - All plans approved



**File**: `../../prompts/prompt-3-1-test-plan.md`Check ✅ each box as you complete it to track progress.



**Input**: `DESIGN_<PROJECT-ID>.md`, `SPECIFICATION_<PROJECT-ID>.md`---



**Output**: `TEST_PLAN_<PROJECT-ID>.md`## Phase Purpose



**Validation**: All requirements covered, test cases defined, environments planned**WHAT**: Create comprehensive execution plans

**HOW**: Generate detailed strategies for testing, documentation, and development

---**WHY**: Ensure structured, efficient implementation with clear quality gates



### Prompt 3-2: Documentation Plan## Workflow Steps



**File**: `../../prompts/prompt-3-2-documentation-plan.md`### Step 3.1: Test Plan Creation

**Prompt File**: `../../prompts/prompt-3-1-test-plan.md`

**Input**: `DESIGN_<PROJECT-ID>.md`, `SPECIFICATION_<PROJECT-ID>.md`**Template**: `../../templates/template-test-plan.md`



**Output**: `DOCUMENTATION_PLAN_<PROJECT-ID>.md`**Purpose**: Transform the technical design into a comprehensive testing strategy



**Validation**: All stakeholder documentation needs identified and planned**Process**:

1. Analyze design document for testable components

---2. Create test strategy covering all requirement types

3. Generate detailed test cases (unit, integration, system, performance)

### Prompt 3-3: Implementation Plans4. Define test data requirements and environment setup

5. Establish acceptance criteria and quality gates

**File**: `../../prompts/prompt-3-3-implementation-plans.md`

**Expected Output**: `TEST_PLAN_<PROJECT-ID>.md`

**Input**: `DESIGN_<PROJECT-ID>.md`

**Key Sections**:

**Output**: Multiple phase plans: `IMPLEMENTATION_PLAN_PHASE_*.md`- Test Strategy and Approach

- Unit Test Plan (100+ test cases)

**Validation**: All design components covered, tasks breakdown complete, dependencies mapped- Integration Test Plan (30+ scenarios)  

- System Test Plan (20+ end-to-end flows)

---- Performance Test Plan

- Security Test Plan

## Completion Criteria- Test Environment Setup

- Quality Gates and Acceptance Criteria

✅ **Workflow complete when**:

### Step 3.2: Documentation Plan Creation

1. All 3 prompts executed successfully**Prompt File**: `../../prompts/prompt-3-2-documentation-plan.md`

2. Test plan exists with comprehensive coverage**Template**: `../../templates/template-documentation-plan.md`

3. Documentation plan addresses all stakeholders

4. Implementation plans provide detailed task breakdown**Purpose**: Define comprehensive documentation strategy for all stakeholders

5. Ready to hand off to Workflow 4

**Process**:

---1. Identify all stakeholder types and their documentation needs

2. Map documentation requirements to project deliverables

## Handoff3. Define content creation and maintenance processes

4. Establish documentation standards and templates

**Next workflow**: `workflow-4-implementation.md`5. Plan training materials and knowledge transfer



**Provides**: `TEST_PLAN_<PROJECT-ID>.md`, `DOCUMENTATION_PLAN_<PROJECT-ID>.md`, `IMPLEMENTATION_PLAN_PHASE_*.md`**Expected Output**: `DOCUMENTATION_PLAN_<PROJECT-ID>.md`


**Key Sections**:
- Stakeholder Analysis and Documentation Needs
- User Documentation Plan (end users)
- API Documentation Plan (developers)
- Operational Documentation Plan (admins/support)
- Developer Documentation Plan (maintainers)
- Training Materials Plan
- Documentation Maintenance Strategy

### Step 3.3: Implementation Plans Creation
**Prompt File**: `../../prompts/prompt-3-3-implementation-plans.md`
**Template**: `../../templates/template-implementation-plans.md`

**Purpose**: Break down technical design into executable development phases

**Process**:
1. Analyze design complexity and identify logical development phases
2. Create detailed task breakdown for each phase
3. Define task dependencies and critical path
4. Generate implementation prompts for development guidance
5. Establish progress tracking and milestone criteria

**Expected Output**: Multiple implementation plan documents
- `IMPLEMENTATION_PLAN_PHASE_1.md` - Backend Foundation
- `IMPLEMENTATION_PLAN_PHASE_2.md` - Integration & Error Handling  
- `IMPLEMENTATION_PLAN_PHASE_3.md` - Frontend & UX
- `IMPLEMENTATION_PLAN_PHASE_4.md` - Testing & Documentation

**Key Sections per Phase**:
- Phase Overview and Objectives
- Work Breakdown Structure (20-30 tasks per phase)
- Task Dependencies and Sequencing
- Implementation Prompts (specific guidance for each task)
- Testing Prompts (validation for each task)
- Progress Tracking and Milestone Criteria

## Quality Validation

### Test Plan Quality Checklist
- [ ] All functional requirements have corresponding test cases
- [ ] Non-functional requirements (performance, security) are covered
- [ ] Test environment requirements are realistic and achievable
- [ ] Test data requirements are clearly defined
- [ ] Acceptance criteria are measurable and objective

### Documentation Plan Quality Checklist
- [ ] All stakeholder types are identified with specific needs
- [ ] Documentation scope covers entire project lifecycle
- [ ] Content creation processes are realistic and resourced
- [ ] Maintenance strategy ensures documentation stays current
- [ ] Training materials address knowledge transfer needs

### Implementation Plans Quality Checklist
- [ ] All design components are covered by implementation tasks
- [ ] Task breakdown is detailed enough for development (no task > 1 day)
- [ ] Dependencies are clearly identified and realistic
- [ ] Each task has specific implementation guidance
- [ ] Progress tracking mechanisms are defined

## Success Criteria

### Phase 3 Complete When:
- [ ] Test plan covers all requirements with detailed test cases
- [ ] Documentation plan addresses all stakeholder needs
- [ ] Implementation plans provide clear development roadmap
- [ ] All planning documents are reviewed and approved
- [ ] Development team confirms implementation plans are actionable

### Handoff to Implementation
- Development team has clear task breakdown and guidance
- QA team has comprehensive test plan and environments
- Documentation team has content strategy and templates
- Project management has progress tracking mechanisms
- All stakeholders understand their roles in execution

## File Organization

```
📁 Planning Phase Outputs
├── 📄 TEST_PLAN_<PROJECT-ID>.md
├── 📄 DOCUMENTATION_PLAN_<PROJECT-ID>.md  
└── 📁 Implementation Plans
    ├── 📄 IMPLEMENTATION_PLAN_PHASE_1.md
    ├── 📄 IMPLEMENTATION_PLAN_PHASE_2.md
    ├── 📄 IMPLEMENTATION_PLAN_PHASE_3.md
    └── 📄 IMPLEMENTATION_PLAN_PHASE_4.md
```

## Integration with Previous Phases

**From Specification Phase (Phase 1)**:
- Functional requirements → Test cases
- Non-functional requirements → Performance/security tests
- User stories → Acceptance criteria

**From Design Phase (Phase 2)**:
- Architecture components → Integration test scenarios
- API specifications → API documentation requirements
- Technical decisions → Implementation task breakdown

**To Implementation Phase**:
- Test plan → Quality gates during development
- Documentation plan → Content creation alongside development
- Implementation plans → Development team task execution

This planning phase ensures that implementation is structured, measurable, and aligned with both business requirements and technical design decisions.
>>>>>>> c5759c0 (feat: Add orchestrator workflows for extra large changes including specification, design, planning, and implementation phases)
