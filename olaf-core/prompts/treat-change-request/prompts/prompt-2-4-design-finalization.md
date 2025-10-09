---
name: finalize-design-document-professional
description: Finalize design document with professional formatting, complete metadata, stakeholder approvals, and implementation readiness for development phase handoff
tags: [design-finalization, documentation, stakeholder-approval, implementation-readiness]
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
- **design_document_path**: string - Path to reviewed design document `DESIGN_<PROJECT-ID>.md` from technical review (REQUIRED)
- **project_id**: string - Project identifier for file naming and metadata (REQUIRED)
- **technical_reviewer_info**: string - Technical reviewer information and approval status (REQUIRED)
- **change_log**: string - Change log from collaborative review process (OPTIONAL)
- **template_path**: string - Path to final design template (OPTIONAL, default: ../templates/template-design-final.md)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for design finalization due to moderate impact on project timeline

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate that the design document exists and is accessible
2. You WILL confirm expected outcomes from technical review step:
   - Reviewed design document: `DESIGN_<PROJECT-ID>.md` exists
   - Technical review has been completed
   - Design modifications from stakeholder feedback have been integrated
   - Document contains architecture specifications and implementation details

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm design document path is accessible and readable
- Validate project ID format for metadata updates
- Check technical reviewer information is complete
- Verify access to design finalization template

### 2. Execution Phase

<!-- <review_integration_validation> -->
**Review Integration Validation:**
You WILL analyze and validate modifications made by technical stakeholders:

**Change Analysis:**
- You MUST identify all modifications made since codebase validation
- You WILL assess impact of changes on overall architecture consistency
- You MUST validate that changes maintain alignment with original requirements
- You WILL check for any conflicts or contradictions introduced by modifications

**Technical Consistency Validation:**
- You MUST ensure architecture diagrams reflect all approved changes
- You WILL verify API specifications are complete and consistent
- You MUST confirm database design maintains integrity and performance
- You WILL validate security implementation covers all access patterns
<!-- </review_integration_validation> -->

<!-- <professional_documentation_standards> -->
**Professional Documentation Standards:**
You WILL apply comprehensive formatting and documentation standards:

**Document Structure and Formatting:**
- You MUST apply consistent heading hierarchy throughout document
- You WILL format all diagrams with proper labeling and legends
- You MUST ensure all API specifications include complete request/response schemas
- You WILL standardize code examples and technical references

**Technical Documentation Quality:**
- You MUST verify all architecture diagrams are clear and accurate
- You WILL ensure implementation details are complete and actionable
- You MUST validate that migration scripts and deployment procedures are included
- You WILL confirm testing strategies are comprehensive and realistic
<!-- </professional_documentation_standards> -->

<!-- <metadata_approval_management> -->
**Metadata and Approval Management:**
You WILL update document metadata and administrative information:

**Version Control:**
- You MUST update document version number (increment appropriately)
- You WILL set current date using terminal timestamp command
- You MUST update document status to 'Reviewed' or 'Approved'
- You WILL add version history entry documenting review process changes

**Technical Reviewer Information:**
- You MUST request and record technical lead/architect approval
- You WILL document review completion date
- You MUST note any additional reviewers or technical contributors
- You WILL add approval signatures or status indicators

**Implementation Readiness Documentation:**
- You MUST create implementation checklist with key milestones
- You WILL document development prerequisites and environment setup
- You MUST add deployment and testing procedure references
- You WILL include quality gates and review checkpoints
<!-- </metadata_approval_management> -->

<!-- <implementation_handoff_preparation> -->
**Implementation Handoff Preparation:**
You WILL prepare the design for development phase transition:

**Development Team Briefing Materials:**
- You MUST create executive summary highlighting key architectural decisions
- You WILL prepare implementation priority matrix based on dependencies
- You MUST document critical technical decisions and their rationale
- You WILL identify components requiring specialized expertise or careful attention

**Quality Assurance Integration:**
- You MUST ensure testing strategies are actionable and complete
- You WILL validate that acceptance criteria align with original requirements
- You MUST confirm performance benchmarks and quality metrics are defined
- You WILL document risk mitigation approaches for high-complexity components
<!-- </implementation_handoff_preparation> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for user approval of finalized design
- Preserve all technical accuracy while enhancing professional presentation
- Use imperative language throughout finalized documentation
- Include comprehensive quality checklist validation

### 3. Validation Phase
You WILL validate the finalized design:
- Confirm all template sections are complete and properly formatted
- Verify all metadata is current and technical approvals are documented
- Validate that changes from technical review are properly integrated
- Ensure design maintains technical accuracy and implementation feasibility

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Finalized design document following template `../templates/template-design-final.md`
- Quality checklist: Completed validation checklist as appendix
- Implementation readiness confirmation: Document approval status and handoff preparation

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when design document is successfully loaded and analyzed
- Status updates during professional formatting and metadata updates
- Progress on technical reviewer information integration
- Completion status for implementation readiness preparation

### Completion Summary
- Finalized design document presented for review via Propose-Act protocol
- Summary of professional enhancements and formatting improvements applied
- Technical approval status and implementation readiness confirmation
- Save location confirmation for finalized design document

### Next Steps
You WILL clearly define:
- Document is approved, formatted per template, and ready for Phase 3 (Planning)
- Implementation team can proceed with development phase handoff
- Quality gates and review checkpoints are established
- Development prerequisites and environment setup are documented

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER modify technical accuracy or architectural decisions without explicit approval
- Rule 2: ALL template formatting requirements must be completed - no partial compliance
- Rule 3: Technical reviewer approval MUST be documented before declaring completion
- Rule 4: Implementation readiness checklist MUST be fully validated
- Rule 5: Version history MUST include complete change documentation from review process
- Rule 6: Professional document header MUST include complete technical metadata
- Rule 7: Quality checklist validation MUST be completed and documented in appendix
- Rule 8: Phase completion declaration MUST only occur after ALL checklist items are complete

## Success Criteria
You WILL consider the task complete when:
- [ ] Document follows professional technical documentation standards
- [ ] All metadata is current and technical approvals are documented
- [ ] Changes from technical review are properly integrated and validated
- [ ] Design maintains technical accuracy and implementation feasibility
- [ ] Document is approved and ready for development phase handoff
- [ ] Template compliance checklist is 100% complete
- [ ] Implementation readiness is confirmed and documented
- [ ] Quality gates and review processes are defined

## Required Actions
1. Validate all required input parameters and design document accessibility
2. Execute design finalization following appropriate interaction protocol
3. Generate finalized design document in specified template format
4. Provide user communication and obtain approval via Propose-Act
5. Define next steps for Phase 3 (Planning) transition

## Error Handling
You WILL handle these scenarios:
- **Design Document Access Failed**: Provide clear error message and request valid file path
- **Template Access Issues**: Provide manual template structure and continue with standard format
- **Technical Reviewer Information Incomplete**: Request complete approval details before proceeding
- **Formatting Validation Failures**: Iterate formatting addressing specific missing sections
- **User Rejection During Propose-Act**: Request specific feedback and iterate finalization
- **Implementation Readiness Gaps**: Document gaps and request guidance on acceptable modifications
- **Quality Checklist Incomplete**: Stop process and complete all required checklist items
- **Version Control Conflicts**: Resolve conflicts and ensure clean version history

## MANDATORY TEMPLATE COMPLIANCE CHECKLIST

You MUST apply ../templates/template-design-final.md COMPLETELY

**Quality Gate - ALL MUST BE CHECKED:**

- [ ] **Heading Hierarchy**: H1=title only, H2=major sections, H3=components, H4=details
- [ ] **Diagram Standards**: All architecture/sequence/ERD diagrams properly formatted and labeled
- [ ] **API Specifications**: All endpoints documented with request/response schemas
- [ ] **Code Examples**: All code blocks have language tags and proper formatting
- [ ] **Version History**: Complete table with columns: Version | Date | Author | Changes
- [ ] **Section Order**: Matches template structure (Architecture, Data Model, API, Security, etc.)
- [ ] **Cross-References**: All internal links and references working correctly
- [ ] **Quality Checklist**: Completed and documented in appendix
- [ ] **Metadata Complete**: Document Type, Version, Date, Status, Reviewed By, Technical Approvals

**If ANY checkbox is unchecked, Step 2.4 is INCOMPLETE - go back and fix it.**

## MANDATORY EXIT DECLARATION

Upon completion of ALL formatting requirements, you MUST declare:

**"Phase 2 (Design) is COMPLETE. Document is approved, formatted per template, and ready for Phase 3 (Planning)."**

**Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for design finalization approval
- MANDATORY: Complete ALL template formatting requirements - no exceptions
- NEVER skip template formatting or only add metadata without reformatting
- NEVER say "ready for implementation" without completing ALL checklist items
- ALWAYS validate that document maintains technical accuracy while enhancing presentation
- ALWAYS ensure implementation readiness is confirmed through comprehensive checklist
- ALWAYS declare Phase 2 complete and ready for Phase 3 upon successful completion
- NEVER proceed to implementation without completing ALL quality gate requirements