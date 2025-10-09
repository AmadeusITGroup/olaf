---
name: finalize-specification-document-professional
description: Finalize specification document with professional formatting, complete metadata, stakeholder approvals, and design phase readiness
tags: [specification-finalization, documentation, stakeholder-approval, design-readiness]
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
- **specification_document**: string - Path to user-modified specification document `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **project_id**: string - Project identifier for file naming and metadata (REQUIRED)
- **reviewer_info**: string - Primary reviewer information and approval status (REQUIRED)
- **change_log**: string - Change log or notes from stakeholder review process (OPTIONAL)
- **template_path**: string - Path to final specification template (OPTIONAL, default: ../templates/template-specification-final.md)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for specification finalization due to moderate impact on project timeline

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate that the specification document exists and is accessible
2. You WILL confirm expected outcomes from user review step:
   - User-modified specification document: `SPECIFICATION_<PROJECT-ID>.md` exists
   - Stakeholder review has been completed
   - User modifications have been integrated
   - Document contains all functional and non-functional requirements

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm specification document path is accessible and readable
- Validate project ID format for metadata updates
- Check reviewer information is complete
- Verify access to specification finalization template

### 2. Execution Phase

<!-- <review_integration_validation> -->
**Review Integration Validation:**
You WILL analyze and validate modifications made by stakeholders:

**Change Analysis:**
- You MUST identify all modifications made since codebase validation
- You WILL assess impact of changes on other requirements consistency
- You MUST validate that changes maintain alignment across the document
- You WILL check for any conflicts or contradictions introduced by modifications

**Content Validation:**
- You MUST ensure all requirements remain clear and unambiguous
- You WILL verify acceptance criteria are still complete and testable
- You MUST confirm technical feasibility is maintained after changes
- You WILL validate requirement numbering and cross-references integrity
<!-- </review_integration_validation> -->

<!-- <professional_formatting_standards> -->
**Professional Formatting Standards:**
You WILL apply consistent formatting throughout the document:

**Document Structure and Formatting:**
- You MUST apply consistent heading hierarchy throughout document
- You WILL standardize section organization and logical flow
- You MUST ensure proper table of contents and cross-references
- You WILL validate document structure follows template requirements

**Content Formatting Excellence:**
- You MUST apply consistent markdown formatting throughout
- You WILL standardize table formats with proper column alignment
- You MUST ensure consistent list formatting and proper indentation
- You WILL fix any markdown syntax issues or broken links

**Technical Content Standards:**
- You MUST format code blocks with appropriate language tags
- You WILL ensure consistent technical terminology usage throughout
- You MUST standardize API endpoint and data format specifications
- You WILL validate technical diagrams and references are properly formatted
<!-- </professional_formatting_standards> -->

<!-- <metadata_approval_management> -->
**Metadata and Approval Management:**
You WILL update document metadata and administrative information:

**Version Control:**
- You MUST update document version number (increment appropriately)
- You WILL set current date using terminal timestamp command
- You MUST update document status to 'Reviewed' or 'Approved'
- You WILL add version history entry documenting review process changes

**Reviewer Information:**
- You MUST request and record primary reviewer name and approval
- You WILL document review completion date
- You MUST note any additional reviewers or technical contributors
- You WILL add reviewer signatures or approval status indicators

**Change Documentation:**
- You MUST create or update change log with significant modifications
- You WILL document rationale for major requirement changes
- You MUST note requirements that were added, modified, or removed
- You WILL preserve traceability to original business objectives
<!-- </metadata_approval_management> -->

<!-- <final_quality_assurance> -->
**Final Quality Assurance:**
You WILL perform comprehensive quality validation:

**Completeness Verification:**
- You MUST ensure all required sections are present and complete
- You WILL validate that all functional requirements have acceptance criteria
- You MUST confirm non-functional requirements are measurable and testable
- You WILL check that all integration points are documented comprehensively

**Consistency Validation:**
- You MUST verify requirement numbering is sequential and complete
- You WILL check cross-references and internal links functionality
- You MUST ensure terminology is used consistently throughout document
- You WILL validate data model consistency across all sections

**Technical Accuracy Maintenance:**
- You MUST confirm technical feasibility is maintained after changes
- You WILL validate alignment with existing codebase architecture
- You MUST ensure integration approaches remain realistic and achievable
- You WILL check that constraints and assumptions are still valid
<!-- </final_quality_assurance> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for user approval of finalized specification
- Preserve all technical accuracy while enhancing professional presentation
- Use imperative language throughout finalized documentation
- Include comprehensive quality checklist validation

### 3. Validation Phase
You WILL validate the finalized specification:
- Confirm all template sections are complete and properly formatted
- Verify all metadata is current and reviewer approvals are documented
- Validate that changes from user review are properly integrated
- Ensure specification maintains technical accuracy and design readiness

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Finalized specification document following template `../templates/template-specification-final.md`
- Quality checklist: Completed validation checklist as appendix
- Design readiness confirmation: Document approval status and handoff preparation

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when specification document is successfully loaded and analyzed
- Status updates during professional formatting and metadata updates
- Progress on reviewer information integration and change documentation
- Completion status for final quality assurance validation

### Completion Summary
- Finalized specification document presented for review via Propose-Act protocol
- Summary of professional enhancements and formatting improvements applied
- Reviewer approval status and design phase readiness confirmation
- Save location confirmation for finalized specification document

### Next Steps
You WILL clearly define:
- Document is approved, formatted per template, and ready for Phase 2 (Design)
- Design team can proceed with technical design phase handoff
- Quality gates and review checkpoints are established
- All specification requirements are validated and design-ready

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER modify technical accuracy or requirement intent without explicit approval
- Rule 2: ALL template formatting requirements must be completed - no partial compliance
- Rule 3: Reviewer approval MUST be documented before declaring completion
- Rule 4: Design readiness checklist MUST be fully validated
- Rule 5: Version history MUST include complete change documentation from review process
- Rule 6: Professional document header MUST include complete metadata
- Rule 7: Quality checklist validation MUST be completed and documented in appendix
- Rule 8: Phase completion declaration MUST only occur after ALL checklist items are complete

## Success Criteria
You WILL consider the task complete when:
- [ ] Document follows professional specification documentation standards
- [ ] All metadata is current and reviewer approvals are documented
- [ ] Changes from user review are properly integrated and validated
- [ ] Specification maintains technical accuracy and design feasibility
- [ ] Document is approved and ready for design phase handoff
- [ ] Template compliance checklist is 100% complete
- [ ] Design readiness is confirmed and documented
- [ ] Quality gates and review processes are defined

## Required Actions
1. Validate all required input parameters and specification document accessibility
2. Execute specification finalization following appropriate interaction protocol
3. Generate finalized specification document in specified template format
4. Provide user communication and obtain approval via Propose-Act
5. Define next steps for Phase 2 (Design) transition

## Error Handling
You WILL handle these scenarios:
- **Specification Document Access Failed**: Provide clear error message and request valid file path
- **Template Access Issues**: Provide manual template structure and continue with standard format
- **Reviewer Information Incomplete**: Request complete approval details before proceeding
- **Formatting Validation Failures**: Iterate formatting addressing specific missing sections
- **User Rejection During Propose-Act**: Request specific feedback and iterate finalization
- **Design Readiness Gaps**: Document gaps and request guidance on acceptable modifications
- **Quality Checklist Incomplete**: Stop process and complete all required checklist items
- **Version Control Conflicts**: Resolve conflicts and ensure clean version history

## MANDATORY TEMPLATE COMPLIANCE CHECKLIST

You MUST apply ../templates/template-specification-final.md COMPLETELY

**Quality Gate - ALL MUST BE CHECKED:**

- [ ] **Heading Hierarchy**: H1=title only, H2=major sections, H3=requirements, H4=subsections
- [ ] **List Formatting**: All lists have blank lines before and after
- [ ] **Table Formatting**: All tables properly aligned with consistent column widths
- [ ] **Version History**: Complete table with columns: Version | Date | Author | Changes
- [ ] **Code Blocks**: All code blocks have appropriate language tags
- [ ] **Section Order**: Matches template structure (Executive Summary, FR, NFR, Data Model, etc.)
- [ ] **Cross-References**: All internal links working correctly
- [ ] **Quality Checklist**: Completed and documented in appendix
- [ ] **Metadata Complete**: Document Type, Version, Date, Status, Reviewed By, Review Date

**If ANY checkbox is unchecked, Step 1.4 is INCOMPLETE - go back and fix it.**

## MANDATORY EXIT DECLARATION

Upon completion of ALL formatting requirements, you MUST declare:

**"Phase 1 (Specification) is COMPLETE. Document is approved, formatted per template, and ready for Phase 2 (Design)."**

**Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for specification finalization approval
- MANDATORY: Complete ALL template formatting requirements - no exceptions
- NEVER skip template formatting or only add metadata without reformatting
- NEVER say "ready for design" without completing ALL checklist items
- ALWAYS validate that document maintains technical accuracy while enhancing presentation
- ALWAYS ensure design readiness is confirmed through comprehensive checklist
- ALWAYS declare Phase 1 complete and ready for Phase 2 upon successful completion
- NEVER proceed to design phase without completing ALL quality gate requirements