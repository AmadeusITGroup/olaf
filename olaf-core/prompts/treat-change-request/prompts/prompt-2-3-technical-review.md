---
name: facilitate-technical-design-review
description: Facilitate collaborative review and modification of validated design by technical stakeholders to ensure accuracy, completeness, and architectural alignment
tags: [technical-review, design-review, stakeholder-collaboration, architecture-validation]
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
- **design_document_path**: string - Path to validated design document from codebase validation (REQUIRED)
- **project_id**: string - Project identifier for file naming (REQUIRED)
- **technical_stakeholders**: array - List of technical stakeholders participating in review (OPTIONAL, default: ["architects", "senior developers", "security specialists"])
- **review_scope**: string - Specific areas requiring expert input (OPTIONAL, default: "all components")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for technical review facilitation due to collaborative nature

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate expected outcomes from previous step:
   - Validated design document: `DESIGN_<PROJECT-ID>.md` exists (from codebase validation)
   - Design contains architecture specifications and feasibility assessment
   - Technical constraints and implementation details documented

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm validated design document exists and is accessible
- Validate project identifier format for output naming
- Check availability of technical stakeholders for review
- Verify review scope parameters are appropriate

### 2. Execution Phase

<!-- <stakeholder_review_coordination> -->
**Stakeholder Review Coordination:**
You WILL organize and facilitate the technical review process:

**Review Preparation**
- You MUST distribute design document to all technical stakeholders
- You WILL prepare review agenda focusing on high-risk and complex components
- You MUST identify specific areas requiring expert input (security, performance, etc.)
- You WILL schedule review sessions with appropriate technical participants

**Review Session Management**
- You MUST present design overview and key architectural decisions
- You WILL focus discussion on components marked as "Requires Modification" or "Blocked"
- You MUST facilitate technical discussions on alternative approaches
- You WILL document all feedback, concerns, and suggested modifications

**Expertise Integration**
- You MUST ensure security specialists review authentication/authorization design
- You WILL have performance experts validate scalability and optimization approaches
- You MUST include database specialists for data model and migration review
- You WILL involve UI/UX experts for frontend architecture and user experience
<!-- </stakeholder_review_coordination> -->

<!-- <technical_feedback_integration> -->
**Technical Feedback Integration:**
You WILL systematically address stakeholder feedback:

**Architecture Refinements**
- You MUST incorporate feedback on system architecture and component organization
- You WILL refine integration patterns based on existing system expertise
- You MUST adjust service layer design based on maintainability concerns
- You WILL update performance and scalability approaches per expert recommendations

**Implementation Approach Improvements**
- You MUST modify technical solutions based on feasibility feedback
- You WILL refine API design based on integration and usability concerns
- You MUST adjust data model design based on performance and maintenance feedback
- You WILL update security implementation based on compliance and risk assessment

**Risk Mitigation Updates**
- You MUST address high-risk components with alternative approaches
- You WILL modify implementation phases based on complexity and resource feedback
- You MUST update testing strategy based on quality assurance recommendations
- You WILL refine deployment approach based on infrastructure and operations input
<!-- </technical_feedback_integration> -->

<!-- <collaborative_design_enhancement> -->
**Collaborative Design Enhancement:**
You WILL work with stakeholders to improve the design:

**Consensus Building**
- You MUST facilitate discussion on conflicting technical opinions
- You WILL help stakeholders reach agreement on optimal technical approaches
- You MUST document rationale for chosen solutions and rejected alternatives
- You WILL ensure all technical concerns are addressed or acknowledged

**Design Optimization**
- You MUST collaborate on optimizing performance-critical components
- You WILL refine user experience based on usability feedback
- You MUST improve maintainability based on development team input
- You WILL enhance security based on compliance and risk management feedback
<!-- </collaborative_design_enhancement> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for collaborative review facilitation
- Present design summary with explicit review questions
- Document all stakeholder feedback and requested modifications
- Apply changes while maintaining design integrity
- Obtain explicit stakeholder approval before proceeding

### 3. Validation Phase
You WILL validate the review results:
- Confirm all technical stakeholder feedback has been reviewed and addressed
- Verify design modifications are documented with clear rationale
- Validate technical risks have been mitigated or acknowledged
- Ensure stakeholders have approved the refined design approach
- Confirm design is ready for final formatting and approval

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Updated design document with integrated feedback
- Change documentation: Complete log of modifications using `../templates/template-change-log.md`
- Stakeholder approval records: Documentation of review participation and approvals
- Risk assessment update: Modified risk profile based on design changes

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when design document is successfully loaded and analyzed
- Status updates during stakeholder review coordination
- Progress on feedback integration and design modifications
- Completion status for consensus building and design optimization

### Completion Summary
- Summary of technical review outcomes and design modifications
- List of stakeholders who participated and provided feedback
- Documentation of resolved technical concerns and remaining risks
- Confirmation that refined design approach has stakeholder approval

### Next Steps
You WILL clearly define:
- Immediate next action: Proceed to Step 2.4 (Design Finalization)
- Objective for next phase: Format and finalize design for implementation
- Files provided to next phase: Updated design with integrated feedback
- Dependencies for next step: Stakeholder approval confirmation completed

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER proceed without explicit stakeholder approval and feedback collection
- Rule 2: ALL design modifications MUST be documented with clear technical rationale
- Rule 3: Conflicting technical opinions MUST be resolved through facilitated discussion
- Rule 4: Original design structure and component organization MUST be preserved unless explicitly modified
- Rule 5: User engagement MUST be active - never assume satisfaction without explicit confirmation
- Rule 6: Risk mitigation approaches MUST be updated based on modified design
- Rule 7: Performance and scalability concerns MUST be addressed by appropriate experts
- Rule 8: Security and compliance feedback MUST be integrated before finalization

## Success Criteria
You WILL consider the task complete when:
- [ ] Design document successfully analyzed and presented to stakeholders
- [ ] All assigned technical stakeholders have provided review feedback
- [ ] Requested design modifications have been applied and documented
- [ ] Conflicting technical opinions have been resolved through consensus building
- [ ] Change log documenting all modifications has been created
- [ ] Technical risks have been mitigated or acknowledged with stakeholder approval
- [ ] Explicit stakeholder approval obtained for proceeding to design finalization
- [ ] Next step (2.4 Design Finalization) clearly defined and confirmed

## Required Actions
1. Validate design document access and technical stakeholder assignments
2. Execute collaborative technical review process following Act protocol
3. Generate updated design document with documented changes
4. Provide stakeholder communication and obtain explicit approval
5. Define next steps for design finalization phase

## Error Handling
You WILL handle these scenarios:
- **Design Document Access Failed**: Request valid file path and verify accessibility
- **Technical Stakeholder Unavailable**: Document partial review and request completion timeline
- **Conflicting Technical Feedback**: Facilitate resolution discussion and document agreed solution
- **Modification Requests Conflict**: Prioritize based on technical feasibility and architectural impact
- **User Provides No Feedback**: Ask specific targeted questions about each major design component
- **Approval Not Obtained**: Address specific technical concerns and iterate review process until approval achieved
- **Risk Mitigation Inadequate**: Request additional expert input and alternative approaches
- **Performance Concerns Unresolved**: Escalate to architecture team and request performance validation

## MANDATORY USER ENGAGEMENT

**YOU MUST ACTIVELY FACILITATE TECHNICAL REVIEW - DO NOT WAIT FOR USER TO VOLUNTEER FEEDBACK**

**Required Actions:**

1. **Present Design Summary**:
   - You WILL summarize key architectural decisions
   - You WILL highlight critical components and integrations
   - You WILL present technology stack choices with justifications

2. **Ask Explicit Review Questions**:
   - You MUST ask: "Please review the design above. Do you have technical feedback or concerns?"
   - You MUST ask: "Are there any architectural decisions that need reconsideration?"
   - You MUST ask: "Do any components need more detail or alternative approaches?"

3. **Document User Response**:
   - You WILL record all technical feedback provided
   - You WILL apply requested design modifications
   - You WILL address technical concerns raised

4. **Get Explicit Approval**:
   - You MUST ask: "Are you satisfied with the design approach?"
   - If yes: You MUST ask: "May I proceed to Step 2.4 (Design Finalization)?"
   - If no: You WILL address concerns and repeat review process

## MANDATORY EXIT DECLARATION

Upon user approval, you MUST declare:

**"Step 2.3 (Technical Review) is complete. User has approved design. Proceeding to Step 2.4 (Design Finalization)."**

**Critical Requirements**
- MANDATORY: Follow Act protocol for collaborative technical review facilitation
- MANDATORY: Actively engage stakeholders with explicit questions - never assume satisfaction
- NEVER skip user engagement and proceed directly to finalization
- NEVER assume user approval without explicit confirmation
- ALWAYS document all stakeholder feedback and design modifications
- ALWAYS resolve conflicting technical opinions before proceeding
- ALWAYS provide clear technical rationale for significant design changes
- ALWAYS ensure technical risks are mitigated or acknowledged with stakeholder approval
- NEXT STEP IS ALWAYS 2.4 (DESIGN FINALIZATION) - NO EXCEPTIONS