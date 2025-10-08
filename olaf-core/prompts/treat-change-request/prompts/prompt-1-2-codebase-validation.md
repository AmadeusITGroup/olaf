# Prompt 1.2: Codebase Validation & Feasibility Assessment

## Purpose
Validate that the specification requirements are **TECHNICALLY FEASIBLE** within the existing codebase architecture and constraints. Assess implementation reality without designing specific solutions.

## Instructions

Please validate and refine the specification document by conducting a comprehensive analysis of the existing codebase:

### Input Required
- Initial specification document: `SPECIFICATION_<PROJECT-ID>.md`
- Access to the complete codebase
- Existing architectural documentation (if available)

### Task

#### 1. Deep Feasibility Assessment (MANDATORY)
Analyze the existing codebase to validate specification feasibility with **EVIDENCE-BASED VALIDATION**:

**🔍 CRITICAL: You MUST read actual implementation code, not just file names or summaries.**

- **Security Requirements Validation**
  - **MUST DO**: Use `grep_search` to find security configuration classes (e.g., `SecurityConfiguration`, `@BirdAuthorized`)
  - **MUST DO**: Use `read_file` to examine actual authentication/authorization implementation
  - **Evidence Required**: Document specific annotations, security filter chains, role definitions with file paths and line numbers
  - **Example**: "`@BirdAuthorized` annotation found in `SecurityAspect.java:45` supports DESIGNER, APPROVER, RELEASE roles"
  - Verify that required authentication/authorization mechanisms are available
  - Confirm that role-based access control supports required permissions
  - Validate that security annotations can enforce required access patterns
  - Check for any security constraints that would block requirements

- **Data and Transaction Feasibility**
  - **MUST DO**: Use `grep_search` to find entity base classes (e.g., `AbstractAuditingEntity`, inheritance strategies)
  - **MUST DO**: Use `read_file` to examine actual entity implementations, annotations, and relationships
  - **Evidence Required**: Document inheritance strategy (e.g., `@Inheritance(strategy = InheritanceType.JOINED)` at `Entity.java:15`), field annotations, cascade types
  - **Example**: "DeploymentRequestIdentifierEntity uses JOINED inheritance at line 17, supports extending with ConfigurationDeploymentRequestIdentifierEntity"
  - Confirm database schema can support required data models
  - Validate transaction patterns support required consistency levels
  - Check that JPA patterns can handle required entity relationships
  - Verify migration capabilities for required schema changes

- **API and Service Layer Compatibility**
  - **MUST DO**: Use `grep_search` to find controller endpoints and service implementations
  - **MUST DO**: Use `read_file` to examine actual REST mappings, request/response handling, validation logic
  - **Evidence Required**: Document endpoint paths, HTTP methods, security headers with file paths and line numbers
  - **Example**: "Webhook endpoint `POST /webhook` at `DeploymentRepositoryController.java:572` uses HMAC-SHA256 signature validation"
  - Validate that REST patterns support required API endpoints
  - Confirm service layer can implement required business logic
  - Check dependency injection supports required component integration
  - Verify existing patterns align with functional requirements

- **State Management & Workflow Validation**
  - **MUST DO**: Use `grep_search` to find state enums, workflow controllers, lifecycle management
  - **MUST DO**: Use `read_file` to examine actual state transitions, validation logic, rollback mechanisms
  - **Evidence Required**: Document enum values, state transition logic, recovery actions with file paths and line numbers
  - **Example**: "DeploymentRequestState enum at `DeploymentRequestState.java:10` has 6 states (OPEN, SUBMITTED, SUCCESSFUL, FALLBACKED, DECLINED, FAILED) covering full lifecycle"

- **Integration and Performance Constraints**
  - **MUST DO**: Use `grep_search` to find integration clients, async patterns, caching mechanisms
  - **MUST DO**: Use `read_file` to examine actual integration implementations, performance optimizations
  - **Evidence Required**: Document integration patterns, transaction boundaries, async handling with file paths and line numbers
  - Identify any existing integrations that could conflict with requirements
  - Validate performance characteristics meet non-functional requirements
  - Check for architectural constraints that would prevent implementation
  - Assess scalability limitations that could impact requirements

#### 2. Constraint and Risk Identification
Identify potential blockers and implementation risks:

- **Technical Constraints**
  - Database limitations that could prevent required data models
  - Security framework limitations that could block access patterns
  - Performance bottlenecks that could prevent scale requirements
  - Integration conflicts with existing systems

- **Architecture Compatibility**
  - Requirements that don't align with established patterns
  - Functional needs that would require major architectural changes
  - Non-functional requirements that exceed current capabilities
  - Dependencies that could create circular references or conflicts

#### 3. Visual Architecture Documentation (MANDATORY)

Create Mermaid diagrams to clarify specification understanding:

- **🎨 REQUIRED DIAGRAMS**:
  
  **a) Data Model Entity Relationship Diagram**
  - Use `erDiagram` syntax to show all entities and relationships
  - Include cardinality (1..1, 1..*, *..*)
  - Show inheritance with existing base classes
  - Label foreign key relationships
  - **Example**:
    ```mermaid
    erDiagram
        DeploymentRequestIdentifierEntity ||--o{ ConfigurationOnlyDeploymentRequest : extends
        ConfigurationOnlyDeploymentRequest ||--o{ ConfigurationFileChange : contains
        ConfigurationOnlyDeploymentRequest }o--|| DeploymentRequest : "aggregated in"
        ConfigurationOnlyDeploymentRequest }o--|| User : "imported by"
    ```

  **b) Workflow State Machine Diagram**
  - Use `stateDiagram-v2` syntax to show state transitions
  - Include all states and transition triggers
  - Show happy path and error paths
  - Include rollback/fallback states
  - **Example**:
    ```mermaid
    stateDiagram-v2
        [*] --> IMPORTED : PR Imported
        IMPORTED --> SCHEDULED : Added to Deployment
        SCHEDULED --> DEPLOYED : Deployment Success
        SCHEDULED --> FAILED : Deployment Failure
        DEPLOYED --> FALLBACKED : Rollback Triggered
        FAILED --> [*]
        FALLBACKED --> [*]
    ```

  **c) Integration Architecture Diagram**
  - Use `graph TB` (top-bottom) or `graph LR` (left-right) syntax
  - Show all external system integrations
  - Include API endpoints and protocols
  - Show data flow directions
  - **Example**:
    ```mermaid
    graph TB
        UI[Bird UI] --> API[Configuration API]
        API --> Service[Configuration Service]
        Service --> GitOps[GitOps Repository]
        Service --> DM[Deployment Manager]
        Service --> TR[Task Record System]
        Service --> DB[(PostgreSQL)]
    ```

  **d) MVP Workflow Sequence Diagram**
  - Use `sequenceDiagram` syntax for FR-001 manual import
  - Show user interaction, validation steps, persistence
  - Include error handling paths
  - **Example**:
    ```mermaid
    sequenceDiagram
        User->>+UI: Enter PR URL
        UI->>+API: POST /import-pr
        API->>+Service: importPullRequest()
        Service->>+GitOps: Fetch PR Details
        GitOps-->>-Service: PR Metadata
        Service->>Service: Validate Configuration-only
        Service->>+DB: Save ConfigurationOnlyDeploymentRequest
        DB-->>-Service: Entity Saved
        Service-->>-API: Success Response
        API-->>-UI: Display Success
        UI-->>-User: PR Imported
    ```

**📋 Quality Gate**: All 4 diagrams MUST be embedded in the specification document. If any diagram is missing, validation is INCOMPLETE.

#### 4. Validation Summary and Recommendations

Update the specification with validation results:

- **Feasibility Confirmation with Evidence**
  - Mark each requirement as "Feasible", "Requires Modification", or "Blocked"
  - **MUST INCLUDE**: For each "Feasible" requirement, cite specific code evidence (class names, file paths, line numbers, annotations)
  - **Quality Gate**: If you cannot cite specific implementation details, your validation is INCOMPLETE - go deeper
  - Document any constraints that affect requirement implementation
  - Note existing patterns and frameworks that support requirements

- **Implementation Notes (High-Level Only)**
  - Reference existing security roles that could be leveraged (with file paths)
  - Note existing transaction patterns that align with requirements (with annotations)
  - Identify existing services that could be extended (with class names)
  - Flag any requirements needing architectural discussion

- **Risk Mitigation Recommendations**
  - Suggest requirement modifications to address technical constraints
  - Recommend alternative approaches for blocked requirements
  - Flag high-risk requirements for design phase attention

### 📋 Evidence-Based Validation Checklist

Before finalizing validation, ensure you have:

- ✅ Used `grep_search` to find ALL relevant components for each requirement
- ✅ Used `read_file` to examine ACTUAL implementations (not just summaries)
- ✅ Documented specific file paths, line numbers, class names, annotations
- ✅ Verified inheritance patterns (e.g., `@Inheritance(strategy = ...)`)
- ✅ Confirmed security mechanisms (e.g., filter chains, role definitions)
- ✅ Validated state management (e.g., enum values, transitions)
- ✅ Checked audit/transaction frameworks (e.g., `@EntityListeners`, `@BirdTransaction`)
- ✅ Created validation table with code references for each requirement
- ✅ **Entity Relationship Diagram** (erDiagram) embedded in specification
- ✅ **State Machine Diagram** (stateDiagram-v2) embedded in specification
- ✅ **Integration Architecture Diagram** (graph) embedded in specification
- ✅ **MVP Workflow Sequence Diagram** (sequenceDiagram) embedded in specification

**If you cannot check all boxes above, your validation is NOT COMPLETE.**

### Output Format

- **Document Name**: `SPECIFICATION_<PROJECT-ID>.md` (validation-enhanced version)
- **Template Reference**: Use `../templates/template-specification-enhanced.md` for validation sections
- **Content Updates**: Add feasibility assessment and constraint documentation
- **Preservation**: Maintain all original requirements with validation status
- **Focus**: Technical feasibility validation without detailed design decisions

### Success Criteria

- Each requirement validated for technical feasibility **WITH CODE EVIDENCE**
- Validation includes specific file paths, line numbers, class names, annotations
- Constraints and risks clearly documented
- No detailed architectural design decisions included
- Validation focuses on "Can we build this?" not "How will we build this?"
- Document ready for stakeholder review with realistic expectations
- **Quality Gate**: Every "Feasible" requirement must have at least one code reference

### 🔒 MANDATORY EXIT DECLARATION

Upon completion, you MUST declare:

**"Step 1.2 (Codebase Validation) is complete. Proceeding to Step 1.3 (User Review)."**

⚠️ **YOU MUST NOT:**
- Say "specification is ready for finalization"
- Say "ready for design phase"
- Skip to Step 1.4
- Assume user is satisfied without asking

**NEXT STEP IS ALWAYS 1.3 - NO EXCEPTIONS**

