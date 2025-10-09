---
name: create-implementation-plans-from-design
description: Transform approved technical design into flexible, executable implementation plan with clear tasks, dependencies, and acceptance criteria
tags: [implementation, planning, technical-design, task-breakdown, development]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: Get-Date -Format "yyyyMMdd-HHmm"
- Unix/Linux/macOS: date +"%Y%m%d-%H%M"

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **design_document_path**: string - Path to finalized design document DESIGN_<PROJECT-ID>.md (REQUIRED)
- **specification_document_path**: string - Path to approved specification document SPECIFICATION_<PROJECT-ID>.md (REQUIRED)
- **test_plan_document_path**: string - Path to test plan document TEST_PLAN_<PROJECT-ID>.md (REQUIRED)
- **project_id**: string - Project identifier for output file naming (REQUIRED)
- **codebase_analysis_path**: string - Path to existing codebase patterns and conventions analysis (OPTIONAL)
- **team_constraints**: object - Team capabilities and project constraints information (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for implementation plan creation due to moderate impact

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate expected outcomes from previous step:
   - DESIGN_<PROJECT-ID>.md (finalized design from Phase 2) exists and is accessible
   - SPECIFICATION_<PROJECT-ID>.md (approved specification from Phase 1) exists and is accessible
   - TEST_PLAN_<PROJECT-ID>.md (from Step 3.1) exists and is accessible
2. You MUST confirm design document contains complete architectural components
3. You WILL verify specification contains all functional requirements (FR-xxx format)

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required document paths are provided and accessible
- Validate prerequisites are met (design, specification, test plan documents exist)
- Check access to template files: ../templates/template-implementation-plans.md, ../templates/template-implementation-task.md, ../templates/template-implementation-task-examples.md
- Verify project_id format matches existing naming conventions

### 2. Execution Phase

**Document Analysis Operations:**
<!-- <specification_analysis> -->
You WILL analyze specification requirements:
- Extract all functional requirements (FR-xxx) that need implementation
- Identify business rules and validation logic requirements  
- Understand user workflows and acceptance criteria
- Note non-functional requirements (performance, security, scalability)
- Assess business criticality and implementation priorities
<!-- </specification_analysis> -->

<!-- <design_analysis> -->
You WILL analyze design architecture:
- Review all architectural components and their relationships
- Understand technical implementation approach for each requirement
- Identify integration points and external dependencies
- Assess implementation complexity and technical risk areas
- Map design components to specification requirements
<!-- </design_analysis> -->

<!-- <cross_reference_analysis> -->
You WILL cross-reference and plan implementation:
- Ensure every specification requirement has corresponding design component
- Break down components into implementable tasks based on business value
- Identify shared dependencies and common technical foundations
- Determine optimal sequencing balancing business priorities and technical dependencies
- Consider testing requirements and quality gates from both documents
<!-- </cross_reference_analysis> -->

**Core Logic**: Execute following protocol requirements
<!-- <task_generation> -->
You WILL generate tasks based on ACTUAL COMPLEXITY using adaptive approach:

**Step 1: Analyze Design Components**
- For Data Layer Components: Analyze entity relationships and complexity (simple CRUD vs complex validation/lifecycle)
- For Service Layer Components: Identify business logic complexity (thin wrappers vs complex workflows)
- For API Layer Components: Group related endpoints logically (simple CRUD vs complex multi-resource APIs)
- For Integration Components: One task per external system integration including error handling

**Step 2: Generate Task Structure**
- Use ../templates/template-implementation-task.md for each task structure
- Include unit testing strategy using TDD/BDD practices for each task
- Provide specific implementation guidance and code patterns
- Define clear acceptance criteria and validation checkpoints

**Step 3: Organize Tasks by Implementation Order**
- Foundation First: Core data models, base services, shared utilities
- Build Up from Dependencies: Services depending on data layer, APIs depending on services
- Complete with Quality: Integration testing, performance optimization, documentation
<!-- </task_generation> -->

### 3. Validation Phase
You WILL validate results:
- Confirm all design components are covered by implementation tasks
- Verify task breakdown matches actual complexity (no artificial splitting or combining)
- Validate dependencies create clear implementation order
- Ensure each task has specific, testable acceptance criteria
- Confirm unit testing is integrated into each task (TDD/BDD approach)
- Verify tasks reference existing codebase patterns for consistency

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Follow template ../templates/template-implementation-plans.md
- Document Name: IMPLEMENTATION_PLAN_<PROJECT-ID>.md (single comprehensive document)
- Format: Professional markdown following template structure
- Content Structure:
  - Executive Summary (project scope, key risks)
  - Task List organized by implementation order (not forced phases)
  - Unit Testing Guidance for each task (TDD/BDD - tests written first)
  - Dependency Graph or visual representation
  - Quality gates and validation checkpoints
  - Reference to existing codebase patterns

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when specification analysis completes successfully
- Confirmation when design analysis completes successfully  
- Confirmation when cross-reference analysis identifies all mappings
- Status of task generation process and complexity assessment
- Validation results for task coverage and dependency structure
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- Implementation plan presented for review via Propose-Act protocol
- Summary of task breakdown approach and complexity-based decisions
- Total number of tasks generated and organization rationale
- Key dependencies and critical path identification
- Unit testing integration approach confirmation

### Next Steps
You WILL clearly define:
- Implementation plan ready for development team handoff (pending user approval)
- Tasks can be imported into project management tools (Jira, Azure DevOps)
- Development team review required before execution begins
- Daily work assignments and sprint planning enabled by task breakdown

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Generate tasks based on ACTUAL COMPLEXITY, not forced templates or artificial structures
- Rule 2: Unit testing MUST be integrated into each implementation task using TDD/BDD practices (tests written first)
- Rule 3: Task breakdown MUST match how developers actually work (natural, logical boundaries)
- Rule 4: Every specification requirement MUST have corresponding implementation coverage
- Rule 5: Dependencies MUST be realistic and create clear implementation sequencing
- Rule 6: Each task MUST be independently implementable and testable
- Rule 7: Implementation plan MUST reference existing codebase patterns for consistency
- Rule 8: Quality gates and validation checkpoints MUST be included throughout

## Success Criteria
You WILL consider the task complete when:
- [ ] All required documents successfully analyzed (specification, design, test plan)
- [ ] All design components covered by implementation tasks
- [ ] Task breakdown appropriately matches actual complexity
- [ ] Dependencies clearly identified and create logical implementation order
- [ ] Each task includes specific implementation guidance and acceptance criteria
- [ ] Unit testing requirements integrated into each task (TDD approach)
- [ ] Implementation plan generated in specified format
- [ ] User approval obtained via Propose-Act protocol
- [ ] Output saved as IMPLEMENTATION_PLAN_<PROJECT-ID>.md

## Required Actions
1. Validate all required input parameters and document accessibility
2. Execute document analysis following appropriate interaction protocol
3. Generate adaptive task breakdown based on actual complexity
4. Create comprehensive implementation plan in specified format
5. Provide user communication and obtain approval via Propose-Act

## Error Handling
You WILL handle these scenarios:
- **Missing Required Documents**: Request specific missing document paths from user and validate accessibility
- **Invalid Project ID Format**: Provide clear error message and request correction following established naming conventions
- **Design-Specification Mismatch**: Stop process and request user guidance on requirement gaps or conflicts
- **Template File Access Issues**: Provide clear error message and alternative manual template guidance
- **Complexity Assessment Conflicts**: Request user input on task granularity preferences and team capabilities
- **Task Dependency Circular References**: Identify circular dependencies and request architectural guidance for resolution
- **Codebase Pattern Access Issues**: Continue with generic patterns but note limitation in final output

CRITICAL Requirements
- MANDATORY: Follow Propose-Act protocol for implementation plan approval
- MANDATORY: Unit testing MUST be integrated into each task using TDD/BDD practices
- NEVER create artificial task breakdowns that don't match actual development complexity
- NEVER sacrifice requirement coverage for structural simplicity
- ALWAYS preserve original design intent and architectural decisions
- ALWAYS validate that every specification requirement has implementation coverage
- ALWAYS ensure task dependencies enable realistic development sequencing
- ALWAYS include comprehensive error handling and quality validation checkpoints
