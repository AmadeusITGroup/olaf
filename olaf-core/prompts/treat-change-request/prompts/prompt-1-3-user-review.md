---
name: review-specification-user-feedback
description: Facilitate stakeholder review and modification of specification documents after codebase validation
tags: [specification, review, stakeholder, collaboration, change-request]
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
- **specification_document**: string - Path to enhanced specification document from codebase validation (REQUIRED)
- **project_id**: string - Project identifier for file naming and tracking (REQUIRED)
- **stakeholder_roles**: array - List of stakeholder roles participating in review (OPTIONAL, default: ["Product Owner", "Technical Lead", "Domain Expert", "Security Team"])
- **review_checklist**: boolean - Whether to use structured review checklist (OPTIONAL, default: true)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for specification review facilitation due to collaborative nature

## Prerequisites
If this prompt is part of a workflow chain:
1. You MUST verify the preceding phase/action was completed
2. You WILL validate expected outcomes from previous step:
   - Enhanced specification document from codebase validation exists: `SPECIFICATION_<PROJECT-ID>.md`
   - Specification contains validated requirements and technical constraints
   - Document is accessible and properly formatted for review

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm specification document exists and is accessible
- Validate project ID format and consistency
- Check stakeholder role assignments are complete
- Verify review process prerequisites are met

### 2. Execution Phase

<!-- <specification_analysis> -->
**Specification Analysis:**
You WILL read and analyze the specification document to:
- Extract all functional requirements (FR-001 through FR-XXX)
- Identify key non-functional requirements
- Map critical integration points and dependencies
- Document current requirement coverage and completeness
<!-- </specification_analysis> -->

<!-- <stakeholder_review_coordination> -->
**Stakeholder Review Coordination:**
You WILL facilitate structured review process:

**Product Owner Review Focus:**
- Verify business requirements alignment with original objectives
- Validate user stories and acceptance criteria completeness
- Ensure business value and priority are correctly represented
- Check that constraints align with business needs

**Technical Lead Review Focus:**
- Validate architectural feasibility and integration approaches
- Review technical constraints and implementation complexity
- Ensure alignment with existing system architecture
- Verify security and performance requirements

**Domain Expert Review Focus:**
- Validate functional requirements completeness and accuracy
- Check business rules and workflow specifications
- Ensure domain-specific requirements are properly captured
- Verify data model alignment with business concepts

**Security Team Review Focus:**
- Review security requirements and compliance needs
- Validate authentication and authorization specifications
- Check data protection and privacy requirements
- Ensure security controls are properly specified
<!-- </stakeholder_review_coordination> -->

<!-- <collaborative_modification> -->
**Collaborative Modification Process:**
You WILL execute the following review workflow:

**Step 1: Specification Presentation**
- Present comprehensive specification summary to stakeholders
- List all functional requirements with clear identifiers
- Summarize key non-functional requirements and constraints
- Highlight critical integration points and dependencies

**Step 2: Active Review Facilitation**
You MUST actively engage stakeholders by:
- Asking explicit review questions about each major section
- Requesting feedback on requirement completeness and accuracy
- Identifying gaps, conflicts, or areas needing clarification
- Documenting all stakeholder responses and concerns

**Step 3: Modification Documentation**
- Apply agreed-upon changes directly to the specification
- Ensure consistency across the document after modifications
- Update related sections affected by changes
- Document change rationale for significant modifications

**Step 4: Conflict Resolution**
- Identify conflicts between different stakeholder perspectives
- Facilitate discussion to resolve requirement conflicts
- Prioritize changes based on business and technical impact
- Ensure final modifications maintain document coherence
<!-- </collaborative_modification> -->

**Core Logic**: You WILL execute following protocol requirements
- Apply Act protocol for collaborative review facilitation
- Present specification summary with explicit review questions
- Document all stakeholder feedback and requested modifications
- Apply changes while maintaining specification integrity
- Obtain explicit stakeholder approval before proceeding

### 3. Validation Phase
You WILL validate results:
- Confirm all stakeholders have completed their review assignments
- Verify conflicts between requirements have been resolved
- Ensure missing requirements have been identified and added
- Validate changes follow proper documentation standards
- Confirm specification is ready for finalization phase

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Updated specification document `SPECIFICATION_<PROJECT-ID>.md`
- Supporting files: Change log documenting major modifications using `../templates/template-change-log.md`
- Documentation: Stakeholder approval indicators and review completion records

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when specification analysis is complete
- Status updates during stakeholder review coordination
- Documentation of all feedback received and changes applied
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- Summary of specification modifications made
- List of stakeholders who participated and approved changes
- Documentation of any unresolved issues or concerns
- Confirmation that specification is ready for finalization

### Next Steps
You WILL clearly define:
- Immediate next action: Proceed to Step 1.4 (Specification Finalization)
- Objective for next phase: Format and finalize specification for approval
- Files provided to next phase: Updated `SPECIFICATION_<PROJECT-ID>.md` with change log
- Dependencies for next step: Stakeholder approval confirmation completed

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER proceed without explicit stakeholder approval and feedback collection
- Rule 2: All specification modifications MUST be documented with clear rationale
- Rule 3: Conflicts between requirements MUST be resolved before proceeding to finalization
- Rule 4: Original specification structure and requirement numbering MUST be preserved unless explicitly modified
- Rule 5: User engagement MUST be active - never assume satisfaction without explicit confirmation

## Success Criteria
You WILL consider the task complete when:
- [ ] Specification document successfully analyzed and presented
- [ ] All assigned stakeholders have provided review feedback
- [ ] Requested modifications have been applied to specification
- [ ] Conflicts between requirements have been resolved
- [ ] Change log documenting modifications has been created
- [ ] Explicit stakeholder approval obtained for proceeding to finalization
- [ ] Next step (1.4 Finalization) clearly defined and confirmed

## Required Actions
1. Validate specification document access and stakeholder assignments
2. Execute collaborative review process following Act protocol
3. Generate updated specification with documented changes
4. Provide stakeholder communication and obtain explicit approval
5. Define next steps for specification finalization phase

## Error Handling
You WILL handle these scenarios:
- **Specification Document Access Failed**: Request valid file path and verify accessibility
- **Stakeholder Unavailable for Review**: Document partial review and request completion timeline
- **Conflicting Requirements Identified**: Facilitate resolution discussion and document agreed solution
- **Modification Requests Conflict**: Prioritize based on business impact and technical feasibility
- **User Provides No Feedback**: Ask specific targeted questions about each major specification section
- **Approval Not Obtained**: Address specific concerns and iterate review process until approval achieved

## MANDATORY USER ENGAGEMENT

**YOU MUST ACTIVELY FACILITATE REVIEW - DO NOT WAIT FOR USER TO VOLUNTEER FEEDBACK**

**Required Actions:**

1. **Present Specification Summary**:
   You WILL list all functional requirements (FR-001 through FR-XXX)
   You WILL summarize key non-functional requirements
   You WILL highlight critical integration points

2. **Ask Explicit Review Questions**:
   You MUST ask: "Please review the specification above. Do you have any feedback or changes?"
   You MUST ask: "Are there any requirements that need clarification or modification?"
   You MUST ask: "Do any sections need expansion or additional detail?"

3. **Document User Response**:
   You WILL record all feedback provided
   You WILL apply requested modifications
   You WILL clarify any ambiguities

4. **Get Explicit Approval**:
   You MUST ask: "Are you satisfied with the specification as it stands?"
   If yes: You MUST ask: "May I proceed to Step 1.4 (Finalization)?"
   If no: You WILL address concerns and repeat review process

## MANDATORY EXIT DECLARATION

Upon user approval, you MUST declare:

**"Step 1.3 (User Review) is complete. User has approved specification. Proceeding to Step 1.4 (Finalization)."**

## Critical Requirements
- MANDATORY: Follow Act protocol for collaborative review facilitation
- MANDATORY: Actively engage stakeholders with explicit questions - never assume satisfaction
- NEVER skip user engagement and proceed directly to finalization
- NEVER assume user approval without explicit confirmation
- ALWAYS document all stakeholder feedback and modifications
- ALWAYS resolve requirement conflicts before proceeding
- ALWAYS provide clear rationale for significant specification changes
- NEXT STEP IS ALWAYS 1.4 (FINALIZATION) - NO EXCEPTIONS
