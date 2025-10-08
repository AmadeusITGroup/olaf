# Prompt 2.2: Design Codebase Validation & Feasibility Assessment

## Purpose
Validate that the design is **TECHNICALLY IMPLEMENTABLE** within the existing codebase architecture and constraints. Assess implementation feasibility without redesigning specific solutions.

## Instructions

Please validate and assess the design document by conducting a comprehensive analysis of implementation feasibility against the existing codebase:

### Input Required
- Initial design document: `DESIGN_<PROJECT-ID>.md`
- Access to the complete codebase
- Understanding of existing architectural patterns and constraints

### Task

#### 1. Deep Implementation Feasibility Assessment (MANDATORY)

Analyze the existing codebase to validate design implementability with **EVIDENCE-BASED VALIDATION**:

**🔍 CRITICAL: You MUST read actual implementation code, not just design proposals or summaries.**

- **Architecture Compatibility**
  - **MUST DO**: Use `grep_search` to find existing service implementations, controller patterns, dependency injection configurations
  - **MUST DO**: Use `read_file` to examine actual class structures, method signatures, component relationships
  - **Evidence Required**: Document specific patterns used (e.g., "Service layer uses constructor injection at `ServiceImpl.java:25`")
  - **Example**: "Proposed ConfigurationDeploymentService follows existing pattern in DeploymentRepositoryServiceImpl.java (constructor injection, @Service annotation, transactional boundaries)"
  - Verify that proposed architecture aligns with existing patterns
  - Check for conflicts with established service layer organization
  - Validate integration points with existing components
  - Assess impact on existing system performance and stability

- **Data Model Feasibility**
  - **MUST DO**: Use `grep_search` to find existing entity implementations, repositories, migration scripts
  - **MUST DO**: Use `read_file` to examine actual entity annotations, relationships, cascade types, fetch strategies
  - **Evidence Required**: Document JPA patterns (e.g., "`@ManyToOne(fetch = FetchType.LAZY)` pattern at `Entity.java:45` aligns with proposed design")
  - **Example**: "Proposed ConfigurationDeploymentRequestIdentifierEntity extends DeploymentRequestIdentifierEntity (JOINED inheritance at line 17) - compatible with existing pattern"
  - Confirm database schema changes are compatible with existing structure
  - Validate JPA entity relationships work with current patterns
  - Check migration complexity and data consistency requirements
  - Assess impact on existing queries and database performance

- **Security Implementation Feasibility**
  - **MUST DO**: Use `grep_search` to find security interceptors, authorization checks, role mappings
  - **MUST DO**: Use `read_file` to examine actual security filter implementations, permission validation logic
  - **Evidence Required**: Document security enforcement points (e.g., "`@BirdAuthorized(roles = {DESIGNER, APPROVER})` at `Controller.java:120`")
  - **Example**: "Proposed endpoint security uses existing `@BirdAuthorized` pattern from DeploymentRepositoryController.java:150 with DESIGNER/APPROVER roles"
  - Verify proposed security patterns work with existing framework
  - Check role and permission compatibility with current authorization
  - Validate authentication integration with existing systems
  - Assess security enforcement patterns against current architecture

- **API and Service Layer Compatibility**
  - **MUST DO**: Use `grep_search` to find REST controllers, service interfaces, DTO mappers
  - **MUST DO**: Use `read_file` to examine actual endpoint implementations, exception handling, validation logic
  - **Evidence Required**: Document patterns (e.g., "`@PostMapping` with `@Valid` at `Controller.java:200` matches proposed design")
  - **Example**: "Proposed GET /configuration-deployments endpoint follows existing pattern in DeploymentRepositoryController.java:300 (pagination, sorting, filtering)"
  - Confirm REST endpoint design works with existing controller patterns
  - Validate service layer interfaces align with current dependency injection
  - Check transaction boundary design against existing patterns
  - Assess error handling compatibility with current exception framework

- **State Machine & Workflow Implementation**
  - **MUST DO**: Use `grep_search` to find state transition logic, workflow orchestration, event handlers
  - **MUST DO**: Use `read_file` to examine actual state management implementations, validation rules
  - **Evidence Required**: Document state handling patterns (e.g., "State transitions at `ServiceImpl.java:400` use switch-case with validation")
  - **Example**: "Proposed configuration deployment state machine reuses DeploymentRequestState enum with OPEN → SUBMITTED → SUCCESSFUL flow"

#### 2. Technical Constraint and Risk Identification
Identify potential implementation blockers and challenges:

- **Architecture Constraints**
  - Framework limitations that could prevent proposed solutions
  - Existing dependencies that conflict with design decisions
  - Performance bottlenecks that could impact scalability goals
  - Integration conflicts with current system boundaries

- **Implementation Complexity Assessment**
  - Components requiring significant architectural changes
  - Migration challenges for data model changes
  - Integration complexity with existing workflows
  - Testing challenges for proposed changes

- **Resource and Timeline Impact**
  - Development effort required for proposed architecture
  - Team skill requirements for implementation
  - Infrastructure changes needed for deployment
  - Quality assurance and testing complexity

#### 3. Validation Summary and Recommendations

Document feasibility assessment results:

- **Feasibility Validation with Evidence**
  - Mark each design component as "Implementable", "Requires Modification", or "Blocked"
  - **MUST INCLUDE**: For each "Implementable" component, cite specific code patterns from existing implementation
  - **Quality Gate**: If you cannot cite specific file paths, class names, method signatures, your validation is INCOMPLETE - go deeper
  - Document any constraints that affect implementation approach
  - Note existing patterns and frameworks that support the design

- **Implementation Risk Assessment**
  - Identify high-risk components requiring careful implementation (with code references showing complexity)
  - Flag design decisions that may need architectural discussion
  - Recommend alternative approaches for blocked components (reference existing alternatives)
  - Suggest implementation phase priorities based on risk and complexity

- **Integration Notes with Code References**
  - Reference existing security patterns that align with design (file paths, line numbers)
  - Note existing transaction and service patterns for implementation (annotations, boundaries)
  - Identify existing UI components that can be leveraged (component names, props)
  - Flag any design elements requiring new architectural patterns

#### 4. Visual Design Documentation (MANDATORY)

Create Mermaid diagrams to clarify design architecture and implementation:

- **🎨 REQUIRED DIAGRAMS**:
  
  **a) Detailed Class Diagram**
  - Use `classDiagram` syntax to show entity/service/controller classes
  - Include key attributes and methods (no need for all, just significant ones)
  - Show inheritance relationships with existing base classes
  - Show composition/aggregation relationships
  - **Example**:
    ```mermaid
    classDiagram
        DeploymentRequestIdentifierEntity <|-- ConfigurationOnlyDeploymentRequestEntity
        AbstractAuditingEntity <|-- ConfigurationFileChangeEntity
        ConfigurationOnlyDeploymentRequestEntity "1" *-- "*" ConfigurationFileChangeEntity
        
        class ConfigurationOnlyDeploymentRequestEntity {
            +Long id
            +String pullRequestUrl
            +String targetPhase
            +DeploymentRequestState status
            +List~ConfigurationFileChangeEntity~ configChanges
        }
        
        class ConfigurationFileChangeEntity {
            +Long id
            +String filePath
            +ChangeType changeType
            +String diffSummary
        }
    ```

  **b) Component Architecture Diagram**
  - Use `graph TB` or `C4Context` syntax to show layers (Controller → Service → Repository → Database)
  - Show component boundaries and dependencies
  - Include security interceptors and transaction boundaries
  - **Example**:
    ```mermaid
    graph TB
        subgraph "Presentation Layer"
            UI[Bird UI]
            Controller[ConfigurationDeploymentController<br/>@RestController]
        end
        
        subgraph "Service Layer"
            Service[ConfigurationDeploymentService<br/>@Service @BirdTransaction]
            GitOps[GitOpsRepositoryService]
        end
        
        subgraph "Data Layer"
            Repo[ConfigurationDeploymentRepositoryAdapter]
            DB[(PostgreSQL)]
        end
        
        UI --> Controller
        Controller --> Service
        Service --> Repo
        Service --> GitOps
        Repo --> DB
        
        Security[BirdSecurityAspect<br/>@BirdAuthorized] -.-> Controller
        Transaction[BirdTransactionAspect<br/>@BirdTransaction] -.-> Service
    ```

  **c) Deployment Flow Sequence Diagram**
  - Use `sequenceDiagram` syntax to show end-to-end deployment flow
  - Include all major components (UI, API, Service, GitOps, Deployment Manager)
  - Show transaction boundaries and error handling
  - **Example**:
    ```mermaid
    sequenceDiagram
        participant User
        participant Controller
        participant Service
        participant GitOps
        participant DeploymentMgr
        participant DB
        
        User->>+Controller: POST /import-pr
        Controller->>Controller: @BirdAuthorized(DESIGNER)
        Controller->>+Service: importPullRequest()
        Service->>Service: @BirdTransaction BEGIN
        Service->>+GitOps: fetchPRDetails()
        GitOps-->>-Service: PR Metadata
        Service->>Service: validateConfigurationOnly()
        Service->>+DB: save(entity)
        DB-->>-Service: Saved
        Service->>+DeploymentMgr: scheduleWithNextDeployment()
        DeploymentMgr-->>-Service: Scheduled
        Service->>Service: @BirdTransaction COMMIT
        Service-->>-Controller: Success
        Controller-->>-User: 200 OK
    ```

  **d) API Contract Diagram**
  - Use simple `graph LR` or table format showing all REST endpoints
  - Include HTTP methods, paths, request/response DTOs
  - Show authorization requirements per endpoint
  - **Example**:
    ```mermaid
    graph LR
        subgraph "Configuration Deployment API"
            A[POST /config-deployments/import<br/>@BirdAuthorized DESIGNER<br/>Request: ImportPRRequest<br/>Response: ConfigDeploymentDTO]
            B[GET /config-deployments<br/>@BirdAuthorized DESIGNER,APPROVER<br/>Response: Page~ConfigDeploymentDTO~]
            C[GET /config-deployments/:id<br/>@BirdAuthorized DESIGNER,APPROVER<br/>Response: ConfigDeploymentDTO]
            D[POST /config-deployments/:id/cancel<br/>@BirdAuthorized DESIGNER<br/>Response: ConfigDeploymentDTO]
        end
    ```

**📋 Quality Gate**: All 4 diagrams MUST be embedded in the design document. If any diagram is missing, validation is INCOMPLETE.

### 📋 Evidence-Based Design Validation Checklist

Before finalizing design validation, ensure you have:

- ✅ Used `grep_search` to find ALL existing implementations of similar features
- ✅ Used `read_file` to examine ACTUAL patterns (controllers, services, entities, DTOs)
- ✅ Documented specific file paths, line numbers, class/method names
- ✅ Verified proposed patterns match existing conventions (naming, structure, annotations)
- ✅ Confirmed proposed security aligns with existing enforcement (filters, roles)
- ✅ Validated proposed transactions match existing boundaries (`@Transactional` patterns)
- ✅ Checked proposed API matches existing REST conventions (paths, methods, responses)
- ✅ Created implementation mapping table linking design components to existing code patterns
- ✅ **Detailed Class Diagram** (classDiagram) embedded in design document
- ✅ **Component Architecture Diagram** (graph TB) embedded in design document
- ✅ **Deployment Flow Sequence Diagram** (sequenceDiagram) embedded in design document
- ✅ **API Contract Diagram** (graph LR) embedded in design document

**If you cannot check all boxes above, your design validation is NOT COMPLETE.**

### Output Format

- **Document Name**: `DESIGN_<PROJECT-ID>.md` (validation-enhanced version)
- **Template Reference**: Use `../templates/template-design-enhanced.md` for validation sections
- **Content Updates**: Add feasibility assessment and constraint documentation
- **Preservation**: Maintain all original design decisions with validation status
- **Focus**: Implementation feasibility validation without redesigning solutions

### Success Criteria

- Each design component validated for implementation feasibility **WITH CODE PATTERN EVIDENCE**
- Validation includes specific file paths, line numbers, class names, method signatures
- Technical constraints and risks clearly documented
- No detailed redesign work included (save for design review phase)
- Validation focuses on "Can we implement this?" not "How should we redesign this?"
- Document ready for technical stakeholder review with realistic expectations
- **Quality Gate**: Every "Implementable" component must reference at least one existing code pattern

### 🔒 MANDATORY EXIT DECLARATION

Upon completion, you MUST declare:

**"Step 2.2 (Design Validation) is complete. Proceeding to Step 2.3 (Technical Review)."**

⚠️ **YOU MUST NOT:**
- Say "design is ready for finalization"
- Say "ready for implementation phase"
- Skip to Step 2.4
- Assume user is satisfied without asking

**NEXT STEP IS ALWAYS 2.3 - NO EXCEPTIONS**

