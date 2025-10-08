<<<<<<< HEAD
---
name: convert-user-review
description: Convert the User Review & Modification prompt to standardized template, preserving collaborative review flow and mandatory approvals
tags: [prompt, conversion, review, collaboration]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **spec_path**: path - Enhanced specification `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **stakeholders**: string[] - Stakeholder roles to engage (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion, then actively engage users per step

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `spec_path` exists
- Verify stakeholder roles to engage (PO, Tech Lead, Domain Expert, Security)

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Present specification summary (FR list, key NFRs, integrations)
- Ask explicit review questions per role
- Collect feedback and apply modifications
- Track change log entries
- Request explicit approval to proceed to finalization

### 3. Validation Phase
You WILL validate results:
- Ensure all assigned roles reviewed
- Ensure conflicts resolved and changes documented
- Ensure explicit approval captured

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Updated `SPECIFICATION_<PROJECT-ID>.md`
- Change documentation: `../templates/template-change-log.md`

## User Communication

### Progress Updates
- Summary presented
- Roles engaged and feedback status

### Completion Summary
- Approval status and next step

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-1-4-finalization.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Active facilitation; do not wait for unsolicited feedback
- Rule 2: Require explicit approval before moving on

## Success Criteria
You WILL consider the task complete when:
- [ ] All roles reviewed and provided feedback
- [ ] Changes applied and logged
- [ ] Explicit approval recorded

## Required Actions
1. Validate inputs
2. Facilitate review and apply changes
3. Capture approval and communicate next step

## Error Handling
You WILL handle these scenarios:
- **Missing Stakeholder Feedback**: Escalate and reschedule
- **Conflicting Feedback**: Facilitate resolution and document decisions

⚠️ **Critical Requirements**
- MANDATORY: Obtain explicit user approval
- NEVER skip this step or assume approval
=======
﻿# Prompt 1.3: User Review & Modification

## Purpose
Allow stakeholders to **REVIEW** and **MODIFY** the specification after codebase validation to ensure it meets all business and technical requirements.

## Instructions

This is a collaborative review phase where stakeholders examine and modify the specification document:

### Input Required
- Enhanced specification document from codebase validation: `SPECIFICATION_<PROJECT-ID>.md`
- Stakeholder access and review assignments
- Review checklist and guidelines

### Review Process

#### 1. Stakeholder Review Assignments

**Product Owner Review:**
- Verify business requirements alignment with original objectives
- Validate user stories and acceptance criteria completeness
- Ensure business value and priority are correctly represented
- Check that constraints align with business needs

**Technical Lead Review:**
- Validate architectural feasibility and integration approaches
- Review technical constraints and implementation complexity
- Ensure alignment with existing system architecture
- Verify security and performance requirements

**Domain Expert Review:**
- Validate functional requirements completeness and accuracy
- Check business rules and workflow specifications
- Ensure domain-specific requirements are properly captured
- Verify data model alignment with business concepts

**Security Team Review:**
- Review security requirements and compliance needs
- Validate authentication and authorization specifications
- Check data protection and privacy requirements
- Ensure security controls are properly specified

#### 2. Review Guidelines

**What to Look For:**
- Missing or unclear requirements
- Conflicts between requirements
- Unrealistic expectations or constraints
- Missing integration points or dependencies
- Inadequate non-functional requirements
- Incomplete user scenarios or edge cases

**How to Document Changes:**
- Make direct edits to the specification document
- Add comments explaining the rationale for changes
- Mark significant modifications clearly
- Ensure changes don't create conflicts with other requirements
- Update requirement numbers if adding new requirements

#### 3. Collaborative Modification Process

**Step 1: Individual Review**
- Each stakeholder reviews their assigned sections
- Documents questions, concerns, and proposed changes
- Identifies missing requirements or gaps

**Step 2: Collaborative Discussion**
- Review team discusses findings and proposed changes
- Resolve conflicts between different stakeholder perspectives
- Prioritize changes based on business and technical impact
- Agree on modifications to be made

**Step 3: Document Updates**
- Apply agreed-upon changes to the specification
- Ensure consistency across the document
- Update related sections affected by changes
- Document change rationale for significant modifications

### Expected Actions

#### Manual Review Activities
- Stakeholders read and analyze the specification thoroughly
- Compare requirements against business objectives and technical constraints
- Identify gaps, conflicts, or areas needing clarification
- Prepare feedback and proposed modifications

#### Direct Editing Activities
- Make necessary changes directly in the specification document
- Add missing requirements or clarify existing ones
- Update acceptance criteria or business rules
- Refine non-functional requirements based on stakeholder input

#### Change Documentation Activities
- Document reasons for significant changes or additions
- Note any requirements that were removed and why
- Update requirement traceability if new requirements are added
- Prepare summary of changes for final review phase

### Output Format
- **Document Name**: `SPECIFICATION_<PROJECT-ID>.md` (user-modified version)
- **Template Reference**: Use `../templates/template-change-log.md` for documenting modifications
- **Change Documentation**: Create change log documenting major modifications
- **Sign-off**: Stakeholder approval indicators and review completion records

### Success Criteria

- All stakeholders have completed their review assignments
- Conflicts between requirements have been resolved
- Missing requirements have been identified and added
- Changes follow the change log template structure
- Ready for final formatting and approval in next step

### 🔒 MANDATORY USER ENGAGEMENT

⚠️ **YOU MUST ACTIVELY FACILITATE REVIEW - DO NOT WAIT FOR USER TO VOLUNTEER FEEDBACK** ⚠️

**Required Actions:**

1. **Present Specification Summary**:
   - List all functional requirements (FR-001 through FR-XXX)
   - Summarize key non-functional requirements
   - Highlight critical integration points

2. **Ask Explicit Review Questions**:
   - "Please review the specification above. Do you have any feedback or changes?"
   - "Are there any requirements that need clarification or modification?"
   - "Do any sections need expansion or additional detail?"

3. **Document User Response**:
   - Record all feedback provided
   - Apply requested modifications
   - Clarify any ambiguities

4. **Get Explicit Approval**:
   - Ask: "Are you satisfied with the specification as it stands?"
   - If yes: "May I proceed to Step 1.4 (Finalization)?"
   - If no: Address concerns and repeat

### 🔒 MANDATORY EXIT DECLARATION

Upon user approval, you MUST declare:

**"Step 1.3 (User Review) is complete. User has approved specification. Proceeding to Step 1.4 (Finalization)."**

⚠️ **YOU MUST NOT:**
- Skip this step and go directly to finalization
- Assume user is satisfied without asking
- Say "ready for design phase" without completing Step 1.4

**NEXT STEP IS ALWAYS 1.4 - NO EXCEPTIONS**
>>>>>>> 82415e9 (Feat: Add comprehensive prompts for design finalization, test planning, documentation strategy, implementation planning, and execution phases)
