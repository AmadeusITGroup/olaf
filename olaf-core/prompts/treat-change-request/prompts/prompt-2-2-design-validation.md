---
name: validate-design-implementation-feasibility
description: Validate design implementability against existing codebase architecture and constraints with evidence-based assessment
tags: [design-validation, codebase-analysis, feasibility-assessment, implementation-validation]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **design_document_path**: string - Path to initial design document (REQUIRED)
- **project_id**: string - Project identifier for file naming (REQUIRED)
- **codebase_root_path**: string - Root path to existing codebase for analysis (REQUIRED)
- **validation_depth**: shallow|deep|comprehensive - Level of codebase analysis (OPTIONAL, default: deep)
- **output_location**: string - Location for enhanced design document (OPTIONAL, default: same directory as input)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act for design validation due to moderate impact on project timeline

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate the design document exists and is accessible
2. You WILL confirm the following expected outcomes from previous step:
   - Initial design document: `DESIGN_<PROJECT-ID>.md` exists
   - Design document contains architecture specifications
   - Access to complete codebase is available
   - Understanding of existing architectural patterns documented

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm design document path is accessible and readable
- Validate codebase root path exists and contains source code
- Check access to grep_search and file reading capabilities
- Verify project ID format for output file naming

### 2. Execution Phase

<!-- <source_analysis> -->
**Source Analysis:**
You WILL read and analyze the initial design document:
- Extract core architectural components and patterns
- Identify proposed entities, services, and controllers
- Document security and data model requirements
- Note API endpoints and integration points
<!-- </source_analysis> -->

<!-- <codebase_validation> -->
**Deep Implementation Feasibility Assessment:**
You MUST conduct evidence-based validation with MANDATORY code examination:

**Architecture Compatibility Analysis:**
- You WILL use `grep_search` to find existing service implementations, controller patterns, dependency injection configurations
- You WILL use `read_file` to examine actual class structures, method signatures, component relationships
- You MUST document specific patterns with file paths and line numbers (e.g., "Service layer uses constructor injection at `ServiceImpl.java:25`")
- You WILL verify proposed architecture aligns with existing patterns
- You WILL check for conflicts with established service layer organization
- You WILL validate integration points with existing components
- You WILL assess impact on existing system performance and stability

**Data Model Feasibility Validation:**
- You WILL use `grep_search` to find existing entity implementations, repositories, migration scripts
- You WILL use `read_file` to examine actual entity annotations, relationships, cascade types, fetch strategies
- You MUST document JPA patterns with evidence (e.g., "`@ManyToOne(fetch = FetchType.LAZY)` pattern at `Entity.java:45` aligns with proposed design")
- You WILL confirm database schema changes are compatible with existing structure
- You WILL validate JPA entity relationships work with current patterns
- You WILL check migration complexity and data consistency requirements
- You WILL assess impact on existing queries and database performance

**Security Implementation Feasibility:**
- You WILL use `grep_search` to find security interceptors, authorization checks, role mappings
- You WILL use `read_file` to examine actual security filter implementations, permission validation logic
- You MUST document security enforcement points with evidence (e.g., "`@BirdAuthorized(roles = {DESIGNER, APPROVER})` at `Controller.java:120`")
- You WILL verify proposed security patterns work with existing framework
- You WILL check role and permission compatibility with current authorization
- You WILL validate authentication integration with existing systems
- You WILL assess security enforcement patterns against current architecture

**API and Service Layer Compatibility:**
- You WILL use `grep_search` to find REST controllers, service interfaces, DTO mappers
- You WILL use `read_file` to examine actual endpoint implementations, exception handling, validation logic
- You MUST document patterns with evidence (e.g., "`@PostMapping` with `@Valid` at `Controller.java:200` matches proposed design")
- You WILL confirm REST endpoint design works with existing controller patterns
- You WILL validate service layer interfaces align with current dependency injection
- You WILL check transaction boundary design against existing patterns
- You WILL assess error handling compatibility with current exception framework

**State Machine & Workflow Implementation:**
- You WILL use `grep_search` to find state transition logic, workflow orchestration, event handlers
- You WILL use `read_file` to examine actual state management implementations, validation rules
- You MUST document state handling patterns with evidence (e.g., "State transitions at `ServiceImpl.java:400` use switch-case with validation")
- You WILL validate proposed state management aligns with existing patterns
<!-- </codebase_validation> -->

<!-- <risk_assessment> -->
**Technical Constraint and Risk Identification:**
You WILL identify potential implementation blockers:
- Architecture constraints that could prevent proposed solutions
- Existing dependencies that conflict with design decisions
- Performance bottlenecks that could impact scalability goals
- Integration conflicts with current system boundaries
- Components requiring significant architectural changes
- Migration challenges for data model changes
- Integration complexity with existing workflows
- Testing challenges for proposed changes
<!-- </risk_assessment> -->

<!-- <diagram_generation> -->
**Visual Design Documentation:**
You MUST create Mermaid diagrams to clarify design architecture:

**Required Diagrams (ALL MANDATORY):**
1. **Detailed Class Diagram** - Use `classDiagram` syntax showing entity/service/controller classes
2. **Component Architecture Diagram** - Use `graph TB` syntax showing layers and dependencies
3. **Deployment Flow Sequence Diagram** - Use `sequenceDiagram` syntax showing end-to-end flow
4. **API Contract Diagram** - Use `graph LR` syntax showing REST endpoints and authorization

You WILL embed all four diagrams in the enhanced design document.
<!-- </diagram_generation> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for user approval of validation results
- Preserve original design decisions while adding validation status
- Use imperative language throughout validation documentation
- Include comprehensive error handling for validation failures
- Ensure all validation includes specific code references

### 3. Validation Phase
You WILL validate the assessment results:
- Confirm all design components have been evaluated for feasibility
- Verify evidence-based validation includes specific file paths and line numbers
- Validate that all four required Mermaid diagrams are present
- Ensure implementation risks are clearly documented with mitigation strategies
- Confirm validation preserves original functionality and intent

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Enhanced design document `DESIGN_<PROJECT-ID>.md` with validation sections
- Validation summary: Before/after comparison highlighting feasibility assessment
- Implementation evidence table: Mapping design components to existing code patterns
- Risk assessment matrix: Categorized implementation challenges and recommendations

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when design document is successfully read and analyzed
- Status updates during codebase pattern analysis
- Progress on evidence collection and validation assessment
- Completion status for each required Mermaid diagram
- Validation results summary with feasibility ratings

### Completion Summary
- Enhanced design document presented for review via Propose-Act protocol
- Validation improvements summary showing evidence-based assessment
- Implementation feasibility ratings for all design components
- Risk assessment results with specific mitigation recommendations
- Save location confirmation: `<output_location>/DESIGN_<PROJECT-ID>.md`

### Next Steps
You WILL clearly define:
- Enhanced design document ready for technical review (pending user approval)
- Original design document preserved unchanged
- Validation evidence available for stakeholder review
- Preparation for Step 2.3 (Technical Review) phase

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER modify original design decisions without explicit user approval
- Rule 2: ALL feasibility assessments MUST include specific code evidence (file paths, line numbers)
- Rule 3: Validation focuses on "Can we implement this?" not "How should we redesign this?"
- Rule 4: MANDATORY creation of all four Mermaid diagrams without exception
- Rule 5: Evidence-based validation requires actual code examination, not assumptions
- Rule 6: Preserve original functionality and intent while adding validation status
- Rule 7: Risk assessment must include specific mitigation strategies
- Rule 8: Quality gate requires code pattern references for all "Implementable" components

## Success Criteria
You WILL consider the task complete when:
- [ ] Design document successfully read and core components extracted
- [ ] Codebase analysis completed with grep_search and read_file operations
- [ ] Evidence-based validation completed with specific file paths and line numbers
- [ ] All four required Mermaid diagrams created and embedded
- [ ] Technical constraints and risks documented with mitigation strategies
- [ ] Feasibility assessment completed for all design components
- [ ] Enhanced design document generated with validation sections
- [ ] User approval obtained via Propose-Act protocol
- [ ] Validation summary provided with implementation recommendations

## Required Actions
1. Validate all required input parameters and design document accessibility
2. Execute codebase analysis following evidence-based validation protocol
3. Generate enhanced design document with feasibility assessment
4. Create all four mandatory Mermaid diagrams
5. Provide user communication and obtain approval via Propose-Act

## Error Handling
You WILL handle these scenarios:
- **Design Document Access Failed**: Provide clear error message and request valid file path
- **Codebase Access Issues**: Request alternative access methods or manual code references
- **Insufficient Code Evidence**: Iterate analysis to find specific implementation patterns
- **Diagram Generation Failures**: Provide manual diagram creation guidance
- **Validation Complexity Exceeded**: Request user guidance on acceptable validation depth
- **Pattern Matching Failures**: Document gaps and request architectural guidance
- **User Rejection During Propose-Act**: Request specific feedback and iterate validation
- **File Save Failures**: Provide alternative save methods and troubleshooting steps

## MANDATORY EXIT DECLARATION

Upon completion, you MUST declare:

**"Step 2.2 (Design Validation) is complete. Proceeding to Step 2.3 (Technical Review)."**

CRITICAL REQUIREMENTS:
- MANDATORY: Follow Propose-Act protocol for validation approval
- MANDATORY: Include ALL four Mermaid diagrams without exception
- NEVER skip evidence-based validation with actual code examination
- NEVER modify original design intent without explicit approval
- ALWAYS provide specific file paths, line numbers, and code pattern references
- ALWAYS validate that proposed patterns match existing conventions
- ALWAYS ensure feasibility assessment includes implementation risk mitigation
- NEVER proceed to Step 2.4 or assume design finalization
- ALWAYS declare next step as 2.3 (Technical Review) upon completion
