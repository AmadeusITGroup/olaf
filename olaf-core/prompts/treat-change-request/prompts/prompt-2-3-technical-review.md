# Prompt 2.3: Technical Review & Design Modification

## Purpose
Facilitate collaborative review and modification of the validated design by technical stakeholders to ensure accuracy, completeness, and architectural alignment.

## Instructions

Please conduct a collaborative review session with technical stakeholders to refine and improve the design document:

### Input Required
- Validated design document: `DESIGN_<PROJECT-ID>.md` (from codebase validation)
- Technical stakeholders (architects, senior developers, security specialists)
- Access to existing architectural documentation and standards

### Task

#### 1. Stakeholder Review Coordination
Organize and facilitate the technical review process:

- **Review Preparation**
  - Distribute design document to all technical stakeholders
  - Prepare review agenda focusing on high-risk and complex components
  - Identify specific areas requiring expert input (security, performance, etc.)
  - Schedule review sessions with appropriate technical participants

- **Review Session Management**
  - Present design overview and key architectural decisions
  - Focus discussion on components marked as "Requires Modification" or "Blocked"
  - Facilitate technical discussions on alternative approaches
  - Document all feedback, concerns, and suggested modifications

- **Expertise Integration**
  - Ensure security specialists review authentication/authorization design
  - Have performance experts validate scalability and optimization approaches
  - Include database specialists for data model and migration review
  - Involve UI/UX experts for frontend architecture and user experience

#### 2. Technical Feedback Integration
Systematically address stakeholder feedback:

- **Architecture Refinements**
  - Incorporate feedback on system architecture and component organization
  - Refine integration patterns based on existing system expertise
  - Adjust service layer design based on maintainability concerns
  - Update performance and scalability approaches per expert recommendations

- **Implementation Approach Improvements**
  - Modify technical solutions based on feasibility feedback
  - Refine API design based on integration and usability concerns
  - Adjust data model design based on performance and maintenance feedback
  - Update security implementation based on compliance and risk assessment

- **Risk Mitigation Updates**
  - Address high-risk components with alternative approaches
  - Modify implementation phases based on complexity and resource feedback
  - Update testing strategy based on quality assurance recommendations
  - Refine deployment approach based on infrastructure and operations input

#### 3. Collaborative Design Enhancement
Work with stakeholders to improve the design:

- **Consensus Building**
  - Facilitate discussion on conflicting technical opinions
  - Help stakeholders reach agreement on optimal technical approaches
  - Document rationale for chosen solutions and rejected alternatives
  - Ensure all technical concerns are addressed or acknowledged

- **Design Optimization**
  - Collaborate on optimizing performance-critical components
  - Refine user experience based on usability feedback
  - Improve maintainability based on development team input
  - Enhance security based on compliance and risk management feedback

### Interactive Elements

During the review process, please:

1. **Facilitate Technical Discussions**
   - Ask clarifying questions about technical concerns and suggestions
   - Help stakeholders understand trade-offs between different approaches
   - Encourage specific, actionable feedback rather than general comments

2. **Document Change Rationale**
   - Record the reasoning behind each significant design modification
   - Track which stakeholder input led to specific changes
   - Maintain audit trail of design evolution and decision justification

3. **Validate Modifications**
   - Confirm that proposed changes address the original concerns
   - Verify that modifications don't introduce new technical risks
   - Ensure changes maintain alignment with functional and non-functional requirements

### Output Format

**Structure:** Use ../templates/template-change-log.md to document all modifications and stakeholder feedback:

### Change Documentation
- Complete log of all modifications made during review
- Stakeholder feedback summary with resolution status
- Rationale for design changes and alternative approaches considered
- Updated risk assessment based on modified design

**Template Reference:** ../templates/template-change-log.md provides structure for documenting collaborative review outcomes.

### Success Criteria

- All technical stakeholder feedback has been reviewed and addressed
- Design modifications are documented with clear rationale
- Technical risks have been mitigated or acknowledged
- Stakeholders have approved the refined design approach
- Design is ready for final formatting and approval

### 🔒 MANDATORY USER ENGAGEMENT

⚠️ **YOU MUST ACTIVELY FACILITATE TECHNICAL REVIEW - DO NOT WAIT FOR USER TO VOLUNTEER FEEDBACK** ⚠️

**Required Actions:**

1. **Present Design Summary**:
   - Summarize key architectural decisions
   - Highlight critical components and integrations
   - Present technology stack choices with justifications

2. **Ask Explicit Review Questions**:
   - "Please review the design above. Do you have technical feedback or concerns?"
   - "Are there any architectural decisions that need reconsideration?"
   - "Do any components need more detail or alternative approaches?"

3. **Document User Response**:
   - Record all technical feedback provided
   - Apply requested design modifications
   - Address technical concerns raised

4. **Get Explicit Approval**:
   - Ask: "Are you satisfied with the design approach?"
   - If yes: "May I proceed to Step 2.4 (Design Finalization)?"
   - If no: Address concerns and repeat

### 🔒 MANDATORY EXIT DECLARATION

Upon user approval, you MUST declare:

**"Step 2.3 (Technical Review) is complete. User has approved design. Proceeding to Step 2.4 (Design Finalization)."**

⚠️ **YOU MUST NOT:**
- Skip this step and go directly to finalization
- Assume user is satisfied without asking
- Say "ready for implementation phase" without completing Step 2.4

**NEXT STEP IS ALWAYS 2.4 - NO EXCEPTIONS**