---
name: create-initial-specification-from-requirements
description: Create comprehensive specification document from requirements, focusing on business and user needs without implementation details
tags: [specification, requirements, business-analysis, functional-requirements]
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
- **requirements_source**: string - JIRA ticket ID or requirements document path (REQUIRED)
- **project_id**: string - Project identifier for output naming (REQUIRED)
- **business_context**: string - Business context and objectives (OPTIONAL)
- **target_system**: string - Target system information (OPTIONAL)
- **output_location**: string - Location for specification document (OPTIONAL, default: current directory)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for specification creation due to systematic analytical nature

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm requirements source is accessible and complete
- Validate project identifier format for output naming
- Check access to business context and target system information
- Verify write access to output location

### 2. Execution Phase

<!-- <requirements_analysis> -->
**Requirements Analysis:**
You WILL analyze the source requirements comprehensively:
- Extract all functional requirements with clear acceptance criteria
- Identify non-functional requirements (performance, security, usability)
- Document user stories and use cases with business value
- Capture business rules and validation requirements
- Identify stakeholders and their roles
<!-- </requirements_analysis> -->

<!-- <specification_creation> -->
**Specification Document Creation:**
You WILL create a comprehensive specification following this structure:

**1. Executive Summary**
- You MUST provide project context and business objectives
- You WILL document high-level scope and deliverables
- You MUST identify key stakeholders and success criteria
- You WILL establish project timeline and milestones

**2. Business Requirements**
- You MUST document business problem and opportunity
- You WILL capture business objectives and success metrics
- You MUST identify business rules and constraints
- You WILL define business processes and workflows

**3. Functional Requirements**
- You MUST enumerate all functional requirements with unique identifiers (FR-001, FR-002, etc.)
- You WILL provide detailed descriptions with acceptance criteria
- You MUST specify user interactions and system behaviors
- You WILL document data requirements and validation rules

**4. Non-Functional Requirements**
- You MUST specify performance requirements with measurable criteria
- You WILL document security requirements and compliance needs
- You MUST define usability and accessibility requirements
- You WILL establish scalability and availability requirements

**5. User Stories and Use Cases**
- You MUST document user stories in standard format: "As a [user], I want [capability], so that [benefit]"
- You WILL provide detailed use case scenarios with preconditions and postconditions
- You MUST identify primary and alternative flows
- You WILL specify error conditions and exception handling

**6. System Integration Requirements**
- You MUST identify all external systems and interfaces
- You WILL document data exchange requirements and formats
- You MUST specify authentication and authorization requirements
- You WILL define service level agreements and dependencies

**7. Data Requirements**
- You MUST specify data entities and their relationships
- You WILL document data validation and business rules
- You MUST identify data sources and migration requirements
- You WILL establish data retention and archival policies

**8. Constraints and Assumptions**
- You MUST document technical constraints and limitations
- You WILL identify regulatory and compliance requirements
- You MUST specify budget and resource constraints
- You WILL document key assumptions and dependencies
<!-- </specification_creation> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for systematic specification development
- Use imperative language throughout specification documentation
- Include comprehensive error handling for requirement gaps
- Ensure all requirements are testable and measurable

### 3. Validation Phase
You WILL validate the specification meets all requirements:
- Confirm all functional requirements have clear acceptance criteria
- Verify non-functional requirements are measurable and testable
- Validate user stories follow standard format and include business value
- Ensure all stakeholders and their needs are documented
- Confirm specification is complete and ready for design phase

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete specification document `SPECIFICATION_<PROJECT-ID>.md`
- Requirements traceability matrix linking source to specification requirements
- Stakeholder approval checklist for specification review
- File location: `<output_location>/SPECIFICATION_<PROJECT-ID>.md`

## User Communication

### Progress Updates
- Confirmation when requirements source is successfully analyzed
- Status updates during each specification section completion
- Progress on requirements extraction and documentation
- Validation results for specification completeness

### Completion Summary
- Specification document created with all required sections
- Total functional requirements documented (FR-001 through FR-XXX)
- Total non-functional requirements documented (NFR-001 through NFR-XXX)
- User stories and use cases documented with business value
- File location: `SPECIFICATION_<PROJECT-ID>.md`

### Next Steps
You WILL clearly define:
- Specification ready for stakeholder review and approval
- Next phase: Design phase can begin once specification is approved
- Stakeholder review process and approval requirements
- Dependencies for design phase initiation

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ALL functional requirements MUST have unique identifiers and clear acceptance criteria
- Rule 2: Non-functional requirements MUST be measurable with specific metrics
- Rule 3: User stories MUST follow standard format and include business value
- Rule 4: Business rules MUST be clearly stated and testable
- Rule 5: Stakeholder needs MUST be explicitly documented and validated
- Rule 6: Requirements MUST be traceable to original source
- Rule 7: Specification MUST be complete before proceeding to design
- Rule 8: All assumptions and constraints MUST be explicitly documented

## Success Criteria
You WILL consider the task complete when:
- [ ] Requirements source successfully analyzed and understood
- [ ] All functional requirements documented with unique identifiers (FR-001, FR-002, etc.)
- [ ] All non-functional requirements documented with measurable criteria
- [ ] User stories documented in standard format with business value
- [ ] Business rules and validation requirements clearly specified
- [ ] System integration requirements documented with external interfaces
- [ ] Data requirements specified with entities and relationships
- [ ] Constraints and assumptions explicitly documented
- [ ] Specification document generated following template structure exactly
- [ ] Requirements traceability established to original source

## Required Actions
1. Validate all required input parameters and requirements source accessibility
2. Execute comprehensive requirements analysis following systematic approach
3. Generate complete specification document in specified format
4. Provide user communication and progress updates
5. Define next steps for stakeholder review and design phase transition

## Error Handling
You WILL handle these scenarios:
- **Requirements Source Access Failed**: Provide clear error message and request valid source path or ticket ID
- **Incomplete Requirements**: Request additional information and clarification from stakeholders
- **Ambiguous Business Rules**: Flag ambiguities and request specific clarification
- **Missing Stakeholder Information**: Request stakeholder identification and contact details
- **Conflicting Requirements**: Document conflicts and request prioritization guidance
- **Non-Measurable Requirements**: Request specific metrics and acceptance criteria
- **Template Access Failed**: Use standard markdown structure and continue with specification creation
- **File Save Failures**: Provide alternative save locations and troubleshooting steps

**Critical Requirements**
- MANDATORY: All functional requirements MUST have unique identifiers and testable acceptance criteria
- MANDATORY: Non-functional requirements MUST include specific, measurable metrics
- NEVER proceed to design phase without complete and approved specification
- NEVER make assumptions about business requirements without stakeholder validation
- ALWAYS ensure requirements are traceable to original source
- ALWAYS validate that user stories include clear business value
- ALWAYS document constraints and assumptions explicitly
- ALWAYS ensure specification completeness before declaring task complete