---
name: create-initial-technical-design
description: Create comprehensive technical design from approved specification, informed by existing codebase architecture patterns while proposing optimal solutions for new requirements
tags: [design, architecture, specification, codebase-analysis, technical-solution]
---

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

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **specification_document**: string - Path to approved specification document (REQUIRED)
- **project_id**: string - Project identifier for file naming and references (REQUIRED)
- **technology_stack**: string - Target technology stack (Spring Boot, JPA, Angular, etc.) (OPTIONAL, default: "Spring Boot, JPA, Angular")
- **design_template**: string - Path to design document template (OPTIONAL, default: "../templates/template-design-document.md")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for design creation due to moderate impact on development workflow

## Prerequisites
This prompt is part of a workflow chain:
1. You MUST verify the specification approval phase was completed
2. You WILL validate expected outcomes from previous step:
   - Approved specification document exists and is accessible
   - Specification contains complete functional requirements (FR-001 through FR-XXX)
   - Specification contains complete non-functional requirements (NFR-001 through NFR-XXX)
   - Project ID is established and consistent

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm specification document path is provided and accessible
- Validate specification document contains complete requirements
- Check access to existing codebase for architecture analysis
- Verify design template is available

### 2. Execution Phase

**Prerequisites Execution (MANDATORY FIRST STEPS):**
<!-- <specification_analysis> -->
You MUST complete comprehensive specification analysis:
- Read ENTIRE specification document using file operations
- Document total line count to confirm complete reading
- Extract all functional requirements (FR-001 through FR-XXX)
- Extract all non-functional requirements (NFR-001 through NFR-XXX)
- Understand data model requirements completely
- Understand integration requirements completely
- Note all constraints and assumptions
- Create complete requirements summary
<!-- </specification_analysis> -->

<!-- <codebase_analysis> -->
You MUST complete existing codebase architecture analysis:
- Analyze entity patterns using search operations to find base classes
- Examine inheritance strategies and @Inheritance annotations
- Document existing entity patterns for extension
- Analyze service patterns and AbstractCRUDService implementations
- Document dependency injection patterns (@Service, @Autowired)
- Document transaction boundary patterns (@BirdTransaction)
- Analyze controller patterns and @RestController implementations
- Document security patterns (@BirdAuthorized with roles)
- Document request/response handling patterns
- Analyze repository patterns and AbstractRepositoryAdapter implementations
- Document data access and query patterns
- Create comprehensive architecture summary with specific file paths and class names
<!-- </codebase_analysis> -->

**Architecture Design:**
<!-- <architecture_design> -->
You WILL design the optimal technical solution:
- Create high-level component architecture and relationships
- Design service layer organization and responsibilities
- Define data flow and integration patterns
- Design API organization and endpoint structure
- Create entity relationship design optimized for requirements
- Design database schema with proper normalization
- Define data access patterns and repository design
- Plan migration strategy for schema changes
- Design authentication and authorization approach
- Create role-based access control design
- Define security validation and enforcement patterns
- Plan data protection and privacy considerations
<!-- </architecture_design> -->

**Technical Solution Design:**
<!-- <technical_solution> -->
You WILL define implementation approach:
- Specify REST endpoint design with request/response schemas
- Define service layer interfaces and contracts
- Create error handling and validation patterns
- Plan API versioning and backward compatibility
- Design business logic organization and business rule implementation
- Define transaction boundaries and data consistency
- Plan workflow and process management
- Design integration with external systems
- Create caching strategies and performance optimization
- Plan database indexing and query optimization
- Define scalability considerations and bottleneck prevention
- Design monitoring and observability approach
<!-- </technical_solution> -->

**Implementation Planning:**
<!-- <implementation_planning> -->
You WILL plan the development approach:
- Select technology stack with justification
- Define development tools and build pipeline requirements
- Plan testing framework and quality assurance approach
- Consider deployment and infrastructure requirements
- Create implementation phases and milestone planning
- Identify risk mitigation and technical challenges
- Plan team organization and skill requirements
- Define quality gates and review processes
<!-- </implementation_planning> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for design approval
- Complete all mandatory prerequisite analyses before design
- Ensure design aligns with existing codebase patterns
- Provide comprehensive technical specifications
- Include complete implementation planning

### 3. Validation Phase
You WILL validate results meet all requirements:
- Confirm design addresses all functional requirements
- Verify design addresses all non-functional requirements
- Ensure architecture follows existing codebase patterns
- Validate technical decisions are well-justified
- Confirm implementation plan is realistic and achievable
- Verify design is ready for codebase validation phase

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete technical design document following template structure
- Requirements analysis summary with all FR and NFR items
- Codebase architecture analysis with specific patterns identified
- Design validation checklist confirming template compliance

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when specification analysis completes with line count verification
- Confirmation when codebase architecture analysis completes with specific patterns documented
- Confirmation when each design phase completes
- Status of design validation against requirements
- Timestamp identifier used: YYYYMMDD-HHmm format

### Completion Summary
- Complete technical design document ready for review
- Summary of design decisions and architectural choices
- Validation results confirming requirement coverage
- Files created with locations and naming conventions

### Next Steps
You WILL clearly define:
- Design document ready for codebase validation (Step 2.2)
- Technical design validated against specification requirements
- Architecture aligned with existing codebase patterns
- Implementation plan ready for development team review

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER proceed with design without completing specification analysis (entire document read and documented)
- Rule 2: NEVER proceed with design without completing codebase architecture analysis (specific patterns documented with file paths)
- Rule 3: Design MUST align with existing entity, service, controller, and repository patterns
- Rule 4: Design MUST address ALL functional and non-functional requirements from specification
- Rule 5: Design MUST use existing security patterns (@BirdAuthorized) and transaction patterns (@BirdTransaction)
- Rule 6: Design MUST be production-ready and follow established architectural best practices
- Rule 7: Implementation plan MUST be realistic and achievable with specified technology stack
- Rule 8: Design MUST include comprehensive error handling and validation strategies

## Success Criteria
You WILL consider the task complete when:
- [ ] Complete specification analysis performed (all FR and NFR items documented)
- [ ] Complete codebase architecture analysis performed (specific patterns and file paths documented)
- [ ] Technical design addresses all functional requirements
- [ ] Technical design addresses all non-functional requirements
- [ ] Architecture aligns with existing codebase patterns
- [ ] API design follows existing controller patterns
- [ ] Security design uses existing @BirdAuthorized patterns
- [ ] Transaction design uses existing @BirdTransaction patterns
- [ ] Database design includes proper migration strategy
- [ ] Implementation plan is comprehensive and realistic
- [ ] Design document follows template structure completely
- [ ] User approval obtained via Propose-Act protocol
- [ ] Design ready for Step 2.2 (Design Validation)

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute mandatory specification and codebase analysis
3. Create comprehensive technical design following existing patterns
4. Generate outputs in specified template format
5. Obtain user approval via Propose-Act protocol
6. Prepare for next phase (Step 2.2 Design Validation)

## Error Handling
You WILL handle these scenarios:
- **Specification Document Access Failed**: Request valid file path and verify document completeness
- **Incomplete Specification Analysis**: Stop and complete full document analysis before proceeding
- **Codebase Access Issues**: Request alternative access methods or manual pattern documentation
- **Missing Architecture Patterns**: Request specific codebase locations or manual pattern specification
- **Requirement Coverage Gaps**: Iterate design to address all missing requirements
- **Template Compliance Issues**: Revise design document to match template structure exactly
- **User Rejection During Propose-Act**: Request specific feedback and iterate design accordingly
- **Technology Stack Misalignment**: Adjust design to match existing technology choices

Critical Requirements
- MANDATORY: Complete specification analysis BEFORE any design work (verify by documenting line count)
- MANDATORY: Complete codebase architecture analysis BEFORE any design work (verify with specific file paths and class names)
- MANDATORY: Follow Propose-Act protocol for design approval
- MANDATORY: Design MUST align with existing codebase patterns (entity, service, controller, repository)
- NEVER skip prerequisite analysis phases
- NEVER proceed to Step 2.3 or beyond without completing Step 2.2 first
- ALWAYS declare "Step 2.1 (Initial Design) is complete. Proceeding to Step 2.2 (Design Validation)." upon completion
- ALWAYS ensure design addresses ALL requirements from specification
- ALWAYS validate design follows existing architectural patterns before approval
