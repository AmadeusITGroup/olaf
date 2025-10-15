<<<<<<< HEAD
---
name: convert-initial-design
description: Convert the Initial Design Creation prompt to standardized template, preserving prerequisites and design scope
tags: [prompt, conversion, design]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.
 
You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **spec_path**: path - Path to `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **workspace_context**: string - Target codebase for pattern analysis (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and design creation

## Prerequisites (if applicable)
1. You MUST complete full specification analysis.
2. You MUST analyze existing codebase patterns (entities, services, controllers, repositories) with specific file references.

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `spec_path` exists and read entirely
- Confirm access to codebase for pattern analysis

### 2. Execution Phase
You WILL execute these operations as needed:

**Tool Operations**:
- `grep_search` + `read_file` to document existing patterns to follow/extend

**Core Logic**:
- Produce architecture, data model, security, UI, API, performance, and implementation planning sections
- Align design with existing patterns and constraints

### 3. Validation Phase
You WILL validate results:
- Ensure design addresses all FRs/NFRs
- Ensure pattern alignment and constraints documented

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Design document following `../templates/template-design-document.md`

## User Communication

### Progress Updates
- Confirmation of prereq completion
- Pattern analysis summary

### Completion Summary
- Design overview and key decisions

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-2-2-design-validation.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Cite specific existing patterns with file paths
- Rule 2: Do not drift from established conventions without justification

## Success Criteria
You WILL consider the task complete when:
- [ ] All design sections complete and aligned with patterns
- [ ] Constraints and risks documented
- [ ] Output follows template exactly

## Required Actions
1. Validate inputs
2. Analyze patterns and produce design
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Evidence of Patterns**: Go deeper or flag
- **Template Access Issues**: Provide fallback outline inline

⚠️ **Critical Requirements**
- MANDATORY: Pattern-aligned design
- NEVER skip prerequisites
=======
﻿# Prompt 2.1: Initial Design Creation

## Purpose
Create the initial technical design from the approved specification, **INFORMED BY** existing codebase architecture patterns while proposing optimal solutions for new requirements. Design must align with established patterns while meeting all specification requirements.

## Instructions

Please create a comprehensive technical design document based on the approved specification:

### Input Required
- Approved specification document: `SPECIFICATION_<PROJECT-ID>.md` 
- **Complete specification analysis** (entire document, not just first section)
- **Existing codebase architecture understanding** (analyze patterns before designing)
- Understanding of modern architectural patterns and best practices
- Knowledge of target technology stack (Spring Boot, JPA, Angular, etc.)

### Task

#### 0. Prerequisites (MUST DO FIRST)

⚠️ **YOU MUST COMPLETE THESE STEPS BEFORE DESIGNING** ⚠️

**Step 0.1: Complete Specification Analysis**

1. **Read Entire Specification Document**:
   - Use `read_file` to read ALL sections of the specification (not just first 100-200 lines)
   - Document total line count and confirm you've read the complete document
   - Extract all functional requirements (FR-001 through FR-XXX)
   - Extract all non-functional requirements (NFR-001 through NFR-XXX)
   - Understand data model requirements completely
   - Understand integration requirements completely
   - Note all constraints and assumptions

2. **Create Requirements Summary**:
   - List all functional requirements with key acceptance criteria
   - List all non-functional requirements with specifications
   - Identify critical integration points
   - Note MVP scope and out-of-scope items

**Step 0.2: Existing Codebase Architecture Analysis**

1. **Analyze Entity Patterns**:
   - Use `grep_search` to find existing entity base classes
   - Use `read_file` to examine inheritance strategies (@Inheritance annotations)
   - Document existing entity patterns (e.g., AbstractAuditingEntity, JOINED inheritance)
   - Identify entity patterns you'll extend for new entities

2. **Analyze Service Patterns**:
   - Use `grep_search` to find existing service implementations
   - Use `read_file` to examine service structure (e.g., AbstractCRUDService)
   - Document dependency injection patterns (@Service, @Autowired)
   - Document transaction boundary patterns (@BirdTransaction)

3. **Analyze Controller Patterns**:
   - Use `grep_search` to find existing REST controllers
   - Use `read_file` to examine controller structure (@RestController, mappings)
   - Document security patterns (@BirdAuthorized with roles)
   - Document request/response handling patterns

4. **Analyze Repository Patterns**:
   - Use `grep_search` to find existing repository implementations
   - Use `read_file` to examine repository structure (AbstractRepositoryAdapter)
   - Document data access patterns
   - Document query patterns

5. **Create Architecture Summary**:
   - Document existing patterns you'll follow
   - Document existing components you'll extend
   - Document integration points with existing services
   - Note any architectural constraints

**Quality Gate:** If you cannot provide specific file paths and class names from the codebase for existing patterns, you have NOT completed Step 0.2 properly. Go back and analyze deeper.

#### 1. Architecture Design

Now that you understand both the requirements and existing architecture, design the optimal technical solution:
Design the optimal technical solution focusing on:

- **System Architecture**
  - High-level component architecture and relationships
  - Service layer organization and responsibilities  
  - Data flow and integration patterns
  - API design and endpoint organization

- **Data Model Design**
  - Entity relationship design optimized for requirements
  - Database schema design with proper normalization
  - Data access patterns and repository design
  - Migration strategy for schema changes

- **Security Architecture**
  - Authentication and authorization approach
  - Role-based access control design
  - Security validation and enforcement patterns
  - Data protection and privacy considerations

- **User Interface Design**
  - UI component organization and structure
  - User experience flow and interaction patterns
  - Frontend architecture and state management
  - Responsive design and accessibility considerations

#### 2. Technical Solution Design
Define implementation approach covering:

- **API Design**
  - REST endpoint specification with request/response schemas
  - Service layer interfaces and contracts
  - Error handling and validation patterns
  - API versioning and backward compatibility

- **Business Logic Organization**
  - Service layer design and business rule implementation
  - Transaction boundaries and data consistency
  - Workflow and process management
  - Integration with external systems

- **Performance and Scalability**
  - Caching strategies and performance optimization
  - Database indexing and query optimization
  - Scalability considerations and bottleneck prevention
  - Monitoring and observability design

#### 3. Implementation Planning
Plan the development approach including:

- **Technology Stack Selection**
  - Framework and library choices with justification
  - Development tools and build pipeline requirements
  - Testing framework and quality assurance approach
  - Deployment and infrastructure considerations

- **Development Strategy**
  - Implementation phases and milestone planning
  - Risk mitigation and technical challenges
  - Team organization and skill requirements
  - Quality gates and review processes

### Interactive Elements

During the design process, please:

1. **Clarify Requirements**
   - Ask for clarification on ambiguous functional requirements
   - Confirm non-functional requirement priorities and trade-offs
   - Validate assumptions about user workflows and data volumes

2. **Present Design Options**
   - Offer alternative architectural approaches when applicable
   - Explain trade-offs between different technical solutions
   - Recommend optimal approaches based on requirements

3. **Validate Design Decisions**
   - Confirm that design meets all functional requirements
   - Verify that non-functional requirements are addressed
   - Ensure design is maintainable and extensible

### Output Format

**Structure:** Follow the comprehensive design template defined in ../templates/template-design-document.md including:

### Document Standards
- Complete architecture diagrams and component relationships
- Detailed API specifications with schemas
- Database design with ERD and migration plans
- Security design with authentication/authorization details
- UI/UX design with mockups and user flows
- Implementation planning with technology stack and development strategy

**Template Reference:** ../templates/template-design-document.md provides complete structure for technical design documentation.

### Success Criteria

- Design addresses all functional and non-functional requirements
- Architecture is scalable, maintainable, and follows best practices
- Technical decisions are well-justified and documented
- Implementation plan is realistic and achievable
- Design is ready for codebase validation in next step

### � Pre-Design Completion Checklist

Before declaring Step 2.1 complete, verify:

**Specification Analysis:**
- [ ] Read ENTIRE specification document (verified line count)
- [ ] Documented all functional requirements (FR-001 through FR-XXX)
- [ ] Documented all non-functional requirements (NFR-001 through NFR-XXX)
- [ ] Understood data model requirements
- [ ] Understood integration requirements
- [ ] Noted constraints and assumptions

**Codebase Analysis:**
- [ ] Analyzed entity patterns (file paths and class names documented)
- [ ] Analyzed service patterns (specific service implementations examined)
- [ ] Analyzed controller patterns (specific controllers examined)
- [ ] Analyzed repository patterns (specific repository implementations examined)
- [ ] Documented existing patterns to follow/extend

**Design Completeness:**
- [ ] Entity design aligns with existing entity patterns
- [ ] Service design aligns with existing service patterns
- [ ] API design aligns with existing controller patterns
- [ ] Repository design aligns with existing repository patterns
- [ ] All requirements addressed in design
- [ ] Technology stack matches existing stack
- [ ] Security design uses existing @BirdAuthorized patterns
- [ ] Transaction design uses existing @BirdTransaction patterns

**If ANY checkbox is unchecked, Step 2.1 is INCOMPLETE.**

### �🔒 MANDATORY EXIT DECLARATION

Upon completion of ALL checklist items, you MUST declare:

**"Step 2.1 (Initial Design) is complete. Proceeding to Step 2.2 (Design Validation)."**

⚠️ **YOU MUST NOT:**
- Say "design is ready for finalization"
- Say "ready for implementation phase"
- Skip to Step 2.3 or 2.4
- Ask user if they want to proceed to implementation

**NEXT STEP IS ALWAYS 2.2 - NO EXCEPTIONS**
>>>>>>> 82415e9 (Feat: Add comprehensive prompts for design finalization, test planning, documentation strategy, implementation planning, and execution phases)
