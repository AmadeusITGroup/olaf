---
name: structure-change-request-from-extracted-information
description: Structure extracted information into formal change request document, adapting to natural structure found in source documents
tags: [change-request, structuring, requirements-analysis, agile-artifacts]
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
- **prerequisite_1_path**: string - Path to prerequisite-1-demand-inventory.md file (REQUIRED)
- **prerequisite_2_path**: string - Path to prerequisite-2-extracted-information.md file (REQUIRED)
- **output_template_path**: string - Path to change request template (OPTIONAL, default: "../../templates/template-prerequisite-change-request.md")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for change request structuring due to analytical nature with clear validation criteria

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate expected outcomes from previous steps:
   - Document inventory exists: `prerequisite-1-demand-inventory.md`
   - Extracted information exists: `prerequisite-2-extracted-information.md`
   - All extracted information is complete and ready for structuring

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm prerequisite-1-demand-inventory.md exists and is accessible
- Validate prerequisite-2-extracted-information.md exists and contains complete extracted information
- Check access to change request template file
- Verify all required parameters are provided

### 2. Execution Phase

<!-- <demand_type_identification> -->
**Demand Type Identification:**
You WILL analyze the extracted information to determine the actual demand type:

**Large Epic with Features/Stories Analysis:**
- You MUST look for multiple features under a common theme
- You WILL identify hierarchical structure explicitly stated in source
- You MUST find multiple user stories grouped by features
- Evidence required: Clear epic-feature-story hierarchy

**Epic with Direct User Stories Analysis:**
- You MUST find high-level initiative described without intermediate features
- You WILL identify user stories directly attached to epic
- You MUST confirm no intermediate feature grouping exists
- Evidence required: Epic with direct story linkage

**Standalone User Story Analysis:**
- You MUST find single user story with acceptance criteria
- You WILL confirm no epic or feature context exists
- You MUST verify focus on one specific capability
- Evidence required: Individual story without higher-level grouping

**Bug Report Analysis:**
- You MUST identify defect or issue description
- You WILL look for steps to reproduce
- You MUST find expected vs actual behavior
- Evidence required: Problem description with reproduction steps

**Documentation Request Analysis:**
- You MUST find request for documentation creation/update
- You WILL identify documentation gaps
- You MUST locate content requirements specified
- Evidence required: Documentation need with content specification

**Clarification Request Analysis:**
- You MUST find questions about existing code/design
- You WILL identify request for explanation or analysis
- You MUST confirm investigation needed
- Evidence required: Questions requiring investigation

**Technical Debt/Refactoring Analysis:**
- You MUST find code quality improvement requests
- You WILL identify architecture enhancement needs
- You MUST confirm no new features, just improvement
- Evidence required: Improvement focus without new functionality

**Configuration Change Analysis:**
- You MUST find environment or config modification requests
- You WILL confirm no code changes required
- You MUST identify deployment-related changes
- Evidence required: Configuration modification without code development

**Other/Mixed Types Analysis:**
- You WILL identify demands that don't fit standard categories
- You MUST recognize hybrid demands
- You WILL document multiple types combined
- Evidence required: Multiple category characteristics or unique structure

You MUST choose the structure that matches the source - never force inappropriate categorization.
<!-- </demand_type_identification> -->

<!-- <adaptive_structuring> -->
**Adaptive Structure Application:**
You WILL apply the appropriate structure based on identified demand type:

**For Large Epic with Features/Stories:**
- Section 1: Epic (title, description, goals, criteria, value)
- Section 2: Features (each with description, criteria, technical requirements)
- Section 3: User Stories (each linked to features, with criteria, estimates)
- You MUST include full hierarchy as stated in source

**For Epic with Direct User Stories:**
- Section 1: Epic (title, description, goals, criteria, value)
- Section 2: User Stories (directly linked to epic, no feature grouping)
- Section 3: [Features not applicable - stories directly attached to epic]
- You MUST preserve flat story structure as in source

**For Standalone User Story:**
- Section 1: User Story (title, as-a/want/so-that, criteria)
- Section 2: [No epic or feature context in source]
- Section 3: Implementation Details (if provided)
- You MUST keep simple structure - never invent hierarchy

**For Bug Report:**
- Section 1: Bug Summary (title, severity, priority)
- Section 2: Problem Description (what's broken, impact)
- Section 3: Steps to Reproduce
- Section 4: Expected vs Actual Behavior
- Section 5: Environment/Context
- Section 6: Proposed Fix (if mentioned)

**For Documentation Request:**
- Section 1: Documentation Need (what docs are missing/wrong)
- Section 2: Target Audience
- Section 3: Content Requirements (what to document)
- Section 4: Success Criteria (when is doc complete)

**For Clarification Request:**
- Section 1: Question/Clarification Needed
- Section 2: Context (why clarification needed)
- Section 3: Code/Design Areas in Question
- Section 4: Expected Outcome (what answer is sought)

**For Technical Debt/Refactoring:**
- Section 1: Current State Problems (what needs improvement)
- Section 2: Proposed Improvements
- Section 3: Benefits (why do this)
- Section 4: Scope (what will/won't be changed)

**For Configuration Change:**
- Section 1: Configuration Request (what needs to change)
- Section 2: Target Environment
- Section 3: Justification (why this change)
- Section 4: Rollback Plan

**For Other/Mixed Types:**
- You MUST create custom sections that match the source content
- You WILL never force into predefined categories
- You MUST use descriptive section headers from the source language
<!-- </adaptive_structuring> -->

<!-- <contextual_information_inclusion> -->
**Contextual Information Inclusion:**
You WILL include these contextual sections when information is available:

**Requirements Section (if applicable):**
- Functional requirements from extracted information
- Non-functional requirements from extracted information
- Technical specifications from extracted information
- Quality requirements from extracted information

**Business Context Section (if available):**
- Problem statement or opportunity from extracted information
- Business justification from extracted information
- Value proposition from extracted information
- Stakeholders and their roles from extracted information
- Success metrics from extracted information

**Technical Context Section (if available):**
- Current state/existing code from extracted information
- Proposed solution or approach from extracted information
- Architecture notes from extracted information
- Technology stack from extracted information
- Integration points from extracted information
- Data model changes from extracted information

**Constraints and Dependencies Section (if applicable):**
- Timeline constraints from extracted information
- Resource constraints from extracted information
- Budget limitations from extracted information
- Technical dependencies from extracted information
- External dependencies from extracted information
- Blocking issues from extracted information

**Acceptance Criteria/Definition of Done Section (if provided):**
- How to verify completion from extracted information
- Quality gates from extracted information
- Testing requirements from extracted information

**Information Gaps and Open Questions Section (always document):**
- Missing information identified during extraction
- Ambiguities in source documents
- Areas needing clarification
- Assumptions that need validation
- Questions raised in source documents
<!-- </contextual_information_inclusion> -->

<!-- <metadata_documentation> -->
**Processing Metadata Documentation:**
You WILL include processing metadata in every change request:

**Demand Type Classification:**
- What type of demand this is (from analysis)
- Why this classification was chosen
- Evidence supporting the classification

**Source Documents:**
- List all documents processed from prerequisite-1
- Note documents that could not be read
- Document any attachments referenced but not accessible

**MCP Server Usage:**
- Document whether MCP server was used in prerequisite-2
- List external content fetched (if any)
- Note external references NOT fetched and why

**Extraction Date and Time:**
- When this analysis was performed using system timestamp

**Completeness Assessment:**
- Is the information sufficient for routing to Orchestrator-0-Router?
- What critical information is missing?
- What level of confidence in the analysis?
<!-- </metadata_documentation> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for systematic change request structuring
- Respect source document structure and terminology completely
- Use imperative language throughout structuring process
- Include comprehensive validation of structure appropriateness
- Ensure no information omission from extracted content

### 3. Validation Phase
You WILL validate the structured change request:
- Confirm demand type correctly identified with supporting evidence
- Verify structure matches what's actually in source (not forced)
- Validate all extracted information included without omission
- Ensure appropriate sections for the demand type are present
- Confirm missing information marked as [Not Provided], not invented
- Verify ambiguous information marked as [Unclear in source], not interpreted
- Validate source document terminology preserved throughout
- Ensure metadata section complete with all required elements

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Structured change request document using template as reference only
- Output file: `prerequisite-3-change-request.md`
- Structure adapted to actual demand type found in source documents
- Complete metadata section documenting all processing decisions

## User Communication

### Progress Updates
You WILL provide these status confirmations:
- Confirmation when prerequisite files are successfully loaded and analyzed
- Status of demand type identification with evidence summary
- Progress on structure application and contextual information inclusion
- Completion status for metadata documentation
- Validation results for structured change request

### Completion Summary
You WILL provide comprehensive completion information:
- Demand type identified: [specific type with evidence]
- Structure applied: [sections created based on source content]
- Information completeness: [gaps identified and documented]
- Metadata completeness: [all processing decisions documented]
- File location: `prerequisite-3-change-request.md`

### Next Steps
You WILL clearly define:
- Prerequisite Step 3 complete with structured change request ready
- Document ready for review and routing to Orchestrator-0-Router
- All extracted information preserved in appropriate structure
- Processing metadata complete for traceability

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER force a structure that doesn't exist in source documents
- Rule 2: ALWAYS respect what's actually in the source documents
- Rule 3: Use ONLY sections that exist in source - never invent structure
- Rule 4: Use source document terminology throughout
- Rule 5: DO NOT create Epic/Feature/Story hierarchy if not in source
- Rule 6: DO NOT invent structure to fit a template
- Rule 7: DO NOT force agile terminology if source uses different language
- Rule 8: Missing information marked as [Not Provided], never invented
- Rule 9: Ambiguous information marked as [Unclear in source], never interpreted
- Rule 10: Preserve all content from extracted information without omission

## Success Criteria
You WILL consider the task complete when:
- [ ] Demand type correctly identified with supporting evidence
- [ ] Structure matches what's actually in source (not forced)
- [ ] All extracted information included in appropriate sections
- [ ] Appropriate sections for the demand type created
- [ ] Missing information marked as [Not Provided], not invented
- [ ] Ambiguous information marked as [Unclear in source], not interpreted
- [ ] No data omitted from extracted information
- [ ] No data invented or assumed beyond source content
- [ ] Source document terminology preserved throughout
- [ ] Metadata section complete with all processing decisions
- [ ] Document ready for review and routing to Orchestrator-0-Router

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute demand type identification and structure application following Act protocol
3. Generate structured change request in appropriate format
4. Include complete contextual information and metadata
5. Prepare document for Orchestrator-0-Router routing phase

## Error Handling
You WILL handle these scenarios:
- **Missing Prerequisite Files**: Stop process and request valid file paths for both prerequisite documents
- **Incomplete Extracted Information**: Request completion of prerequisite-2 extraction before proceeding
- **Template Access Issues**: Use standard markdown structure and continue with change request creation
- **Demand Type Ambiguity**: Document multiple possible types and provide evidence for each
- **Structure Conflicts**: Choose simplest structure that matches source content
- **Information Gaps**: Document gaps explicitly without attempting to fill them
- **Terminology Conflicts**: Preserve source terminology even if inconsistent with agile standards

**Critical Requirements**
- MANDATORY: Follow Act protocol for systematic change request structuring
- MANDATORY: Respect source document structure and terminology completely
- NEVER force inappropriate structure to fit templates or standards
- NEVER invent information not present in extracted content
- ALWAYS preserve all extracted information without omission
- ALWAYS mark missing information as [Not Provided]
- ALWAYS mark ambiguous information as [Unclear in source]
- ALWAYS use source document terminology throughout
- ALWAYS complete metadata section for full traceability
- EXIT DECLARATION: "Prerequisite Step 3 complete. Change request document generated. Ready for review and routing to Orchestrator-0-Router."