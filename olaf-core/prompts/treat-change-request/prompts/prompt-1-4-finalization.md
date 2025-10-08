<<<<<<< HEAD
---
name: convert-specification-finalization
description: Convert the Specification Finalization & Formatting prompt to standardized template, preserving formatting, metadata, and approval gates
tags: [prompt, conversion, specification, finalization]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **spec_path**: path - User-modified `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **primary_reviewer**: string - Reviewer name (OPTIONAL)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and finalization

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `spec_path` exists
- Load change log/notes from review process if available

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Analyze and validate user changes for consistency and feasibility
- Apply formatting standards (headings, lists, tables, code blocks)
- Update metadata: version, date, status, reviewers, history
- Ensure change log updated with rationale

### 3. Validation Phase
You WILL validate results:
- Ensure all required sections present and complete
- Ensure FRs have acceptance criteria and NFRs are measurable
- Ensure cross-references and links valid

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Finalized specification per `../templates/template-specification-final.md`

## User Communication

### Progress Updates
- Formatting applied
- Metadata updated

### Completion Summary
- Finalization status and readiness for design

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to Phase 2 (Design)

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Apply template formatting completely
- Rule 2: Maintain technical feasibility and consistency

## Success Criteria
You WILL consider the task complete when:
- [ ] Template compliance checklist fully met
- [ ] Metadata complete and accurate
- [ ] Document approved and ready for design

## Required Actions
1. Validate inputs
2. Apply formatting and update metadata
3. Validate completeness and feasibility

## Error Handling
You WILL handle these scenarios:
- **Broken Links/Refs**: Fix or flag with TODO
- **Incomplete Sections**: Request missing content

⚠️ **Critical Requirements**
- MANDATORY: Full template compliance
- NEVER mark ready for design without checklist completion
=======
﻿# Prompt 1.4: Specification Finalization & Formatting

## Purpose
**FINALIZE** the specification with proper formatting, metadata, and review status after user modifications.

## Instructions

Please finalize the specification document after stakeholder review and modifications:

### Input Required
- User-modified specification document: `SPECIFICATION_<PROJECT-ID>.md`
- Change log or notes from stakeholder review process
- Current date for metadata updates
- Reviewer information for documentation

### Task

#### 1. Review User Changes
Analyze and validate modifications made by stakeholders:

- **Change Analysis**
  - Identify all modifications made since codebase validation
  - Assess impact of changes on other requirements
  - Validate that changes maintain consistency across the document
  - Check for any conflicts or contradictions introduced

- **Content Validation**
  - Ensure all requirements remain clear and unambiguous
  - Verify acceptance criteria are still complete and testable
  - Confirm technical feasibility is maintained after changes
  - Validate requirement numbering and cross-references

#### 2. Format Standardization
Apply consistent formatting throughout the document:

- **Document Structure**
  - Standardize heading hierarchy and numbering
  - Ensure consistent section organization
  - Validate table of contents and cross-references
  - Check for proper document flow and logical organization

- **Content Formatting**
  - Apply consistent markdown formatting
  - Standardize table formats and column alignment
  - Ensure consistent list formatting and indentation
  - Fix any markdown syntax issues or broken links

- **Code and Technical Content**
  - Format code blocks with appropriate language tags
  - Ensure consistent technical terminology usage
  - Standardize API endpoint and data format specifications
  - Validate technical diagrams and references

#### 3. Metadata Update
Update document metadata and administrative information:

- **Version Control**
  - Update document version number (increment appropriately)
  - Set current date: `[CURRENT_DATE]`
  - Update document status to 'Reviewed' or 'Approved'
  - Add version history entry if significant changes were made

- **Reviewer Information**
  - Request and record primary reviewer name
  - Document review completion date
  - Note any additional reviewers or contributors
  - Add reviewer signatures or approval indicators

- **Change Documentation**
  - Create or update change log with significant modifications
  - Document rationale for major requirement changes
  - Note any requirements that were added, modified, or removed
  - Preserve traceability to original business objectives

#### 4. Final Quality Check
Perform comprehensive quality assurance:

- **Completeness Verification**
  - Ensure all required sections are present and complete
  - Validate that all functional requirements have acceptance criteria
  - Confirm non-functional requirements are measurable
  - Check that all integration points are documented

- **Consistency Validation**
  - Verify requirement numbering is sequential and complete
  - Check cross-references and internal links
  - Ensure terminology is used consistently throughout
  - Validate data model consistency across sections

- **Technical Accuracy**
  - Confirm technical feasibility is maintained
  - Validate alignment with existing codebase architecture
  - Ensure integration approaches are realistic
  - Check that constraints and assumptions are still valid

### Interactive Elements

During the finalization process, please:

1. **Request Reviewer Information**
   - Ask for the name of the primary reviewer
   - Confirm review completion date
   - Request any additional reviewer names if applicable

2. **Confirm Change Impact**
   - Highlight significant changes made during review
   - Ask for confirmation that changes maintain requirements integrity
   - Verify that technical feasibility is preserved

3. **Validate Status Update**
   - Confirm appropriate document status ('Reviewed' or 'Approved')
   - Verify that the document is ready for design phase
   - Ask for any final adjustments needed

### Output Format
- **Document Name**: `SPECIFICATION_<PROJECT-ID>.md` (final approved version)
- **Template Reference**: Use `../templates/template-specification-final.md` for final formatting standards
- **Formatting**: Professional formatting following template guidelines
- **Metadata**: Current and accurate document information
- **Status**: Ready for design phase handoff

### Success Criteria

- Document follows the final template formatting exactly
- All metadata is current and accurate
- Changes from stakeholder review are properly integrated
- Document maintains technical accuracy and feasibility
- Specification is approved and ready for design phase

### 🔒 MANDATORY TEMPLATE COMPLIANCE CHECKLIST

⚠️ **YOU MUST APPLY ../templates/template-specification-final.md COMPLETELY** ⚠️

**Quality Gate - ALL MUST BE CHECKED:**

- [ ] **Heading Hierarchy**: H1=title only, H2=major sections, H3=requirements, H4=subsections
- [ ] **List Formatting**: All lists have blank lines before and after
- [ ] **Table Formatting**: All tables properly aligned with consistent column widths
- [ ] **Version History**: Complete table with columns: Version | Date | Author | Changes
- [ ] **Code Blocks**: All code blocks have appropriate language tags
- [ ] **Section Order**: Matches template structure exactly (Executive Summary, FR, NFR, Data Model, etc.)
- [ ] **Cross-References**: All internal links working correctly
- [ ] **Quality Checklist**: Completed and documented in appendix
- [ ] **Metadata Complete**: Document Type, Version, Date, Status, Reviewed By, Review Date

**If ANY checkbox is unchecked, Step 1.4 is INCOMPLETE - go back and fix it.**

### 🔒 MANDATORY EXIT DECLARATION

Upon completion of ALL formatting requirements, you MUST declare:

**"Phase 1 (Specification) is COMPLETE. Document is approved, formatted per template, and ready for Phase 2 (Design)."**

⚠️ **YOU MUST NOT:**
- Skip template formatting
- Only add metadata without reformatting
- Say "ready for design" without completing ALL checklist items

**ONLY AFTER ALL CHECKLIST ITEMS ARE COMPLETE MAY YOU PROCEED TO PHASE 2**
>>>>>>> 82415e9 (Feat: Add comprehensive prompts for design finalization, test planning, documentation strategy, implementation planning, and execution phases)
