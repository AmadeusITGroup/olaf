---
name: prompt-3-2-documentation-plan
description: Transform approved technical design into comprehensive documentation strategy addressing all stakeholder needs with detailed implementation plans
tags: [documentation-planning, technical-writing, stakeholder-analysis, training-materials, api-documentation]
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
- **design_document_path**: string - Path to finalized design document from Phase 2 (REQUIRED)
- **specification_document_path**: string - Path to approved specification from Phase 1 (REQUIRED)
- **project_id**: string - Project identifier for file naming (REQUIRED)
- **stakeholder_types**: array[string] - List of stakeholder types and roles (OPTIONAL, default: extracted from documents)
- **documentation_standards**: string - Path to existing documentation standards (OPTIONAL)
- **training_requirements**: string - Training delivery methods and requirements (OPTIONAL)
- **output_location**: string - Location for documentation plan output (OPTIONAL, default: same directory as design document)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for documentation planning due to moderate impact on content creation workflow

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate both required documents exist and are accessible
2. You WILL confirm the following expected outcomes from previous phases:
   - Finalized design document: `DESIGN_<PROJECT-ID>.md` exists and contains complete technical specifications
   - Approved specification document: `SPECIFICATION_<PROJECT-ID>.md` exists with user stories and requirements
   - Design document contains architecture specifications and API definitions
   - Specification document includes user types, workflows, and functional requirements
   - Access to template files for documentation plan structure

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm design document path is accessible and contains technical specifications
- Validate specification document path exists and includes user requirements
- Check project ID format for consistent output file naming
- Verify access to documentation template files if standards path provided
- Validate output location is writable and appropriate for documentation artifacts

### 2. Execution Phase

<!-- <document_analysis> -->
**Source Document Analysis:**
You MUST read and analyze both required documents:

**Specification Document Analysis:**
- You WILL extract all user types and their specific roles (end users, administrators, power users, developers)
- You WILL identify user stories and primary workflows requiring documentation
- You WILL understand business processes and user goals from functional requirements
- You WILL note training needs based on user complexity and technical expertise levels
- You WILL map user types to their information consumption preferences

**Design Document Analysis:**
- You WILL extract API specifications and technical integration points with complete endpoint definitions
- You WILL identify system architecture components requiring developer documentation
- You WILL understand operational procedures and maintenance tasks from technical specifications
- You WILL note configuration options and technical customization capabilities
- You WILL map technical implementation details to user-facing features
<!-- </document_analysis> -->

<!-- <stakeholder_mapping> -->
**Comprehensive Stakeholder Analysis:**
You WILL create detailed stakeholder personas with specific documentation needs:

**For Each Identified Stakeholder Type:**
- You WILL define technical expertise level (beginner, intermediate, advanced)
- You WILL map primary tasks and responsibilities from specification analysis
- You WILL identify preferred information formats (visual, text, interactive, video)
- You WILL determine critical workflows requiring step-by-step documentation
- You WILL assess information consumption patterns and accessibility requirements
<!-- </stakeholder_mapping> -->

<!-- <documentation_planning> -->
**Detailed Documentation Plan Creation:**
You MUST generate comprehensive, actionable documentation tasks following this structure:

**User Documentation Plan Section:**
You WILL analyze specification to create specific, tickable tasks for each user type:

**For Each User Type (extracted from specification):**
- [ ] **Task: Create comprehensive documentation for [Specific User Type Name]**
  - [ ] Subtask: Write getting started guide (complexity adapted to user's technical level)
  - [ ] Subtask: Document primary workflows (based on user's main tasks from specification)
  - [ ] Subtask: Create reference materials (format adapted to user preferences)
  - [ ] Subtask: Add troubleshooting content (based on anticipated user challenges)
  - [ ] Subtask: Test documentation with representative users from this user type
  - [ ] Subtask: Create user-specific FAQ addressing common questions

**For Each Major Feature (extracted from specification):**
- [ ] **Task: Document [Specific Feature Name from Specification]**
  - [ ] Subtask: Write feature overview highlighting business benefits
  - [ ] Subtask: Create step-by-step usage instructions with screenshots
  - [ ] Subtask: Document feature settings and customization options
  - [ ] Subtask: Add practical examples and real-world use cases
  - [ ] Subtask: Create feature-specific troubleshooting guide
  - [ ] Subtask: Develop quick reference card for feature

**API Documentation Plan Section:**
You WILL create comprehensive API documentation tasks based on design analysis:
- [ ] **Task: Document API authentication and security**
  - [ ] Subtask: Write API key generation and management procedures
  - [ ] Subtask: Document all authentication methods with code examples
  - [ ] Subtask: Create "first successful API call" tutorial
  - [ ] Subtask: Document rate limiting policies and error response handling
  - [ ] Subtask: Create security best practices guide for API consumers

- [ ] **Task: Document each API endpoint group (from design analysis)**
  - [ ] Subtask: Document [Specific Endpoint Group A] with complete code examples
  - [ ] Subtask: Document [Specific Endpoint Group B] with request/response schemas
  - [ ] Subtask: Create comprehensive Postman/Insomnia collection with examples
  - [ ] Subtask: Write SDK integration examples for major programming languages
  - [ ] Subtask: Document error codes and troubleshooting for each endpoint group

**Operational Documentation Plan Section:**
You WILL create specific operational tasks based on design specifications:
- [ ] **Task: Create comprehensive deployment documentation**
  - [ ] Subtask: Write detailed deployment checklist with verification steps
  - [ ] Subtask: Document environment configuration and variable management
  - [ ] Subtask: Create rollback procedures with decision criteria
  - [ ] Subtask: Document monitoring setup, alerts, and dashboard configuration
  - [ ] Subtask: Create disaster recovery and backup verification procedures

- [ ] **Task: Create maintenance and operations documentation**
  - [ ] Subtask: Write backup and restore procedures with testing protocols
  - [ ] Subtask: Document log management, retention policies, and analysis procedures
  - [ ] Subtask: Create incident response playbook with escalation procedures
  - [ ] Subtask: Document security patching procedures and maintenance windows
  - [ ] Subtask: Create performance monitoring and optimization guidelines

**Developer Documentation Plan Section:**
You WILL create comprehensive developer onboarding and reference tasks:
- [ ] **Task: Create development environment setup guide**
  - [ ] Subtask: Write step-by-step local environment setup with troubleshooting
  - [ ] Subtask: Document required tools, versions, and compatibility matrices
  - [ ] Subtask: Create "first contribution" guide with workflow examples
  - [ ] Subtask: Document code review process and quality standards
  - [ ] Subtask: Create development best practices and coding standards guide

- [ ] **Task: Document system architecture and development patterns**
  - [ ] Subtask: Create system architecture diagrams with detailed explanations
  - [ ] Subtask: Document coding standards, patterns, and architectural decisions
  - [ ] Subtask: Write component interaction guides with sequence diagrams
  - [ ] Subtask: Document testing guidelines with examples and best practices
  - [ ] Subtask: Create debugging and troubleshooting guide for developers

**Training Materials Plan Section:**
You WILL create comprehensive training content tasks:
- [ ] **Task: Create role-based training modules**
  - [ ] Subtask: Design end-user training agenda with learning objectives
  - [ ] Subtask: Create administrator training materials with hands-on labs
  - [ ] Subtask: Develop progressive hands-on exercises and real-world scenarios
  - [ ] Subtask: Create training assessment questions and competency evaluations
  - [ ] Subtask: Design certification criteria and validation processes

- [ ] **Task: Create multimedia and interactive training content**
  - [ ] Subtask: Record system overview demo video (5-10 minutes with narration)
  - [ ] Subtask: Create feature-specific tutorial videos with step-by-step guidance
  - [ ] Subtask: Design interactive training scenarios and simulations
  - [ ] Subtask: Create downloadable quick reference guides and cheat sheets
  - [ ] Subtask: Develop virtual training environment setup and access procedures

**Documentation Maintenance Strategy Section:**
You WILL create sustainable maintenance processes:
- [ ] **Task: Establish documentation lifecycle processes**
  - [ ] Subtask: Define content review, approval, and publication workflow
  - [ ] Subtask: Set up documentation version control and change management
  - [ ] Subtask: Create content update schedule with role responsibilities
  - [ ] Subtask: Design user feedback collection and response system
  - [ ] Subtask: Establish documentation quality assurance and audit procedures

- [ ] **Task: Implement documentation metrics and improvement processes**
  - [ ] Subtask: Implement usage analytics tracking and reporting dashboard
  - [ ] Subtask: Create monthly content freshness and accuracy reports
  - [ ] Subtask: Set up user satisfaction surveys and feedback analysis
  - [ ] Subtask: Define success metrics, KPIs, and improvement targets
  - [ ] Subtask: Create continuous improvement process for documentation effectiveness
<!-- </documentation_planning> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for comprehensive documentation planning
- Preserve original design and specification intent while creating actionable plans
- Use imperative language throughout documentation planning
- Include comprehensive error handling for planning and execution scenarios
- Ensure all documentation tasks are specific, measurable, and time-bound

### 3. Validation Phase
You WILL validate the documentation plan meets all requirements:
- Confirm all stakeholder types from specification have appropriate documentation coverage
- Verify documentation scope aligns completely with project deliverables from design
- Validate content creation timeline is realistic and properly resourced
- Ensure maintenance processes guarantee documentation stays current and accurate
- Confirm training materials address comprehensive knowledge transfer requirements
- Verify documentation standards ensure consistency and professional quality
- Validate all tasks are actionable with clear acceptance criteria

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Comprehensive documentation plan `DOCUMENTATION_PLAN_<PROJECT-ID>.md`
- Stakeholder analysis summary: Detailed personas with information needs mapping
- Task breakdown structure: Complete work breakdown with effort estimates
- Implementation timeline: Phased approach with dependencies and milestones
- Success metrics definition: Measurable outcomes and quality indicators

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when design and specification documents are successfully analyzed
- Status updates during stakeholder analysis and persona development
- Progress on documentation task creation and validation
- Completion status for each major documentation category
- Validation results summary with completeness assessment

### Completion Summary
- Comprehensive documentation plan ready for content team execution
- Stakeholder analysis completed with detailed persona mapping
- Task breakdown structure with realistic timeline and resource requirements
- Training strategy aligned with system implementation schedule
- Save location confirmation: `<output_location>/DOCUMENTATION_PLAN_<PROJECT-ID>.md`

### Next Steps
You WILL clearly define:
- Documentation plan ready for content team assignment and execution
- Original design and specification documents preserved unchanged
- Stakeholder communication strategy for documentation requirements validation
- Preparation for parallel content creation during system development phase

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER modify original design or specification content during analysis
- Rule 2: ALL documentation tasks MUST be specific, measurable, and actionable
- Rule 3: Documentation scope MUST cover all stakeholder types identified in specification
- Rule 4: Training materials MUST address all user complexity levels appropriately
- Rule 5: API documentation MUST cover all endpoints and integration points from design
- Rule 6: Maintenance strategy MUST ensure long-term documentation quality and currency
- Rule 7: All tasks MUST include clear acceptance criteria and success metrics
- Rule 8: Documentation plan MUST align with development timeline and milestones

## Success Criteria
You WILL consider the task complete when:
- [ ] Design and specification documents successfully analyzed for documentation requirements
- [ ] Comprehensive stakeholder analysis completed with detailed personas
- [ ] Complete documentation task breakdown created with specific, actionable items
- [ ] API documentation plan covers all technical integration points from design
- [ ] Training materials plan addresses all user types and complexity levels
- [ ] Maintenance strategy ensures sustainable documentation quality over time
- [ ] Documentation plan document generated with professional formatting and structure
- [ ] User approval obtained via Propose-Act protocol for plan execution

## Required Actions
1. Validate all required input parameters and document accessibility
2. Execute comprehensive document analysis following systematic approach
3. Generate detailed documentation plan with actionable task breakdown
4. Create stakeholder analysis with specific information needs mapping
5. Provide comprehensive planning documentation with timeline and resources

## Error Handling
You WILL handle these scenarios:
- **Document Access Failed**: Provide clear error message and request valid file paths
- **Incomplete Specification Analysis**: Request additional stakeholder information or manual input
- **Design Document Missing Technical Details**: Request design completion before documentation planning
- **Stakeholder Identification Failures**: Provide manual stakeholder definition templates
- **Template Access Issues**: Use standard markdown structure with comprehensive sections
- **Timeline Estimation Challenges**: Request project timeline constraints and resource availability
- **Validation Failures**: Iterate planning process addressing specific coverage gaps
- **File Save Failures**: Provide alternative save methods and troubleshooting steps

Critical Requirements:
- MANDATORY: Follow Propose-Act protocol for all documentation planning decisions
- MANDATORY: Documentation plan MUST cover ALL stakeholder types without exception
- NEVER proceed without analyzing both design and specification documents completely
- NEVER create generic tasks - all documentation tasks MUST be project-specific
- ALWAYS ensure documentation scope aligns with actual system capabilities
- ALWAYS validate that training materials match user complexity and technical levels
- ALWAYS include comprehensive maintenance strategy for long-term documentation quality
- NEVER skip stakeholder analysis - all documentation MUST be audience-appropriate
- ALWAYS ensure API documentation covers complete technical integration requirements