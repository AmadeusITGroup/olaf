---
name: analyze-change-request-business-context
description: Extract and document comprehensive business context, requirements, and stakeholder information from change request sources with prerequisite validation
tags: [business-analysis, change-request, requirements, stakeholder-analysis]
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
- **source_document**: string - JIRA ticket ID (e.g., SACP-172207) OR business requirement document path (REQUIRED)
- **demand_id**: string - Demand identifier for file organization (REQUIRED)
- **access_method**: string|direct_content|jira|github_issue|markdown_file|business_doc - Method to access source document (REQUIRED)
- **skip_prerequisite_check**: boolean - Override prerequisite validation (OPTIONAL, default: false)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for analysis tasks due to low impact on existing systems

## Prerequisites
This prompt is part of a workflow chain:
1. You MUST verify the preceding prerequisite phase was completed
2. You WILL validate expected outcomes from previous step:
   - Expected file: `olaf-works/demand/<DEMAND-ID>-analysis/prerequisite-3-change-request.md`
   - Required state: Complete prerequisite analysis with Epic, Features, MVP Scope, Open Questions
   - Specific deliverables: Comprehensive change request documentation

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided (source_document, demand_id, access_method)
- Validate access to source document using specified access method
- Check for prerequisite change request completion (MANDATORY unless overridden)

<!-- <prerequisite_validation> -->
**BEFORE doing any analysis, check if prerequisites already created a change request:**

1. **Check for file**: `olaf-works/demand/<DEMAND-ID>-analysis/prerequisite-3-change-request.md`
   
2. **If file EXISTS and is complete** (contains Epic, Features, MVP Scope, Open Questions):
   - You WILL log validation: "Prerequisite change request found: prerequisite-3-change-request.md (complete)"
   - You WILL skip creating `1-change-request-summary.md` to avoid duplication
   - You WILL proceed directly to technical scope analysis phase
   - You MUST exit this prompt as prerequisite covers 90% of required analysis
   
3. **If file DOES NOT EXIST or is incomplete**:
   - You WILL stop execution and return error message
   - You MUST provide guidance: "Prerequisites not complete. Please run prerequisite phase first to create change request"
   - You WILL NOT proceed to Step 2 without complete prerequisites
<!-- </prerequisite_validation> -->

### 2. Execution Phase

<!-- <source_analysis> -->
**Source Document Analysis** (only if prerequisite validation failed):
You WILL analyze the source document and extract comprehensive business context using specified access method
<!-- </source_analysis> -->

<!-- <business_context_extraction> -->
**Business Context Extraction** (DEPRECATED - Skip if Prerequisites Complete):

You WILL extract the following information:

1. **Problem Statement**
   - You MUST identify what business problem is being solved
   - You WILL document current situation and desired future state
   - You MUST capture business impact and urgency

2. **Business Objectives**
   - You WILL document why this change is needed
   - You MUST identify business value and success criteria
   - You WILL capture measurable outcomes and KPIs

3. **User Impact Analysis**
   - You MUST identify all end users affected by this change
   - You WILL quantify user/team impact scope
   - You MUST document user experience changes
<!-- </business_context_extraction> -->

<!-- <stakeholder_identification> -->
**Stakeholder Identification**:

You WILL document:

1. **Requestor Information**
   - You MUST identify who requested this change
   - You WILL document requesting team/department
   - You MUST capture contact information and authority level

2. **Product Owner**
   - You WILL identify who owns this feature/product area
   - You MUST document decision-making authority
   - You WILL capture accountability and approval rights

3. **Affected Teams**
   - You MUST identify all development teams involved
   - You WILL document operations teams requiring consultation
   - You MUST capture team dependencies and coordination needs

4. **External Dependencies**
   - You WILL identify external teams or systems involved
   - You MUST document third-party integrations required
   - You WILL capture vendor or partner coordination needs
<!-- </stakeholder_identification> -->

<!-- <requirements_analysis> -->
**Requirements Analysis**:

You WILL extract and categorize:

1. **Functional Requirements**
   - You MUST document all features/capabilities to be delivered
   - You WILL capture user stories with acceptance criteria
   - You MUST define MVP scope clearly and completely

2. **Non-Functional Requirements**
   - You WILL document performance requirements with specific metrics
   - You MUST identify security requirements and compliance needs
   - You WILL capture scalability and availability requirements

3. **Acceptance Criteria**
   - You MUST define testable conditions for completion
   - You WILL create measurable success indicators
   - You MUST specify validation methods and test scenarios
<!-- </requirements_analysis> -->

<!-- <dependency_identification> -->
**Dependency Identification**:

You WILL document:

1. **Blocking Issues**
   - You MUST identify what must be completed before this starts
   - You WILL document critical path dependencies
   - You MUST capture risk mitigation for blockers

2. **Related Issues**
   - You WILL identify all related changes and linked tickets
   - You MUST document integration points and coordination needs
   - You WILL capture sequencing requirements

3. **External Dependencies**
   - You MUST identify third-party systems and data sources involved
   - You WILL document external approval or coordination requirements
   - You MUST capture vendor timelines and constraints
<!-- </dependency_identification> -->

<!-- <timeline_extraction> -->
**Timeline Information Extraction**:

You WILL capture:

1. **Due Date**: You MUST identify when this is needed with business justification
2. **Priority**: You WILL assign Critical / High / Medium / Low with rationale
3. **Sprint/Release Target**: You MUST identify specific sprint or release window
4. **Business Deadlines**: You WILL document regulatory or contractual deadlines with consequences
<!-- </timeline_extraction> -->

### 3. Validation Phase
You WILL validate results:
- Confirm all business context extracted completely
- Verify stakeholder information is comprehensive and accurate
- Validate requirements are categorized correctly and testably defined
- Ensure timeline information includes business justification

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Follow template `../templates/template-change-request-summary.md`
- File location: `1-change-request-summary.md` in appropriate demand analysis directory
- Documentation: Complete business analysis with all extracted information

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when prerequisite validation completes
- Confirmation when source document access is established
- Confirmation when each extraction phase completes (business context, stakeholders, requirements, dependencies, timeline)
- Location of generated change request summary file

### Completion Summary
- Summary of business context extracted from source document
- Stakeholder analysis results with key contacts identified
- Requirements categorization summary (functional vs non-functional)
- Timeline and priority assessment results
- File location: `1-change-request-summary.md`

### Next Steps
You WILL clearly define:
- Immediate next action: Proceed to `prompt-0-1-2-technical-scope-analysis.md`
- Objective for next phase: Technical architecture and implementation scope analysis
- Files provided to next phase: Complete change request summary with business context
- Dependencies for next step: Access to technical systems and architecture documentation

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER proceed without prerequisite validation unless explicitly overridden
- Rule 2: NEVER create duplicate change request summaries when prerequisites exist
- Rule 3: ALWAYS preserve original JIRA/issue content and traceability
- Rule 4: ALWAYS categorize requirements as functional vs non-functional with clear criteria
- Rule 5: ALWAYS identify MVP scope separately from full feature scope
- Rule 6: NEVER make assumptions about business priorities without source documentation
- Rule 7: ALWAYS validate stakeholder authority and decision-making rights
- Rule 8: ALWAYS include business justification for timeline requirements

## Success Criteria
You WILL consider the task complete when:
- [ ] Prerequisite validation completed (file exists and is complete)
- [ ] Source document successfully accessed using specified method
- [ ] Business problem statement clearly extracted and documented
- [ ] All stakeholders identified with roles and contact information
- [ ] Requirements categorized completely (functional and non-functional)
- [ ] MVP scope defined separately from full feature scope
- [ ] Dependencies documented with blocking vs related classification
- [ ] Timeline information captured with business justification
- [ ] Output file generated following template exactly
- [ ] Next steps clearly defined for technical scope analysis

## Required Actions
1. Validate prerequisite change request exists and is complete
2. Access source document using specified method
3. Extract comprehensive business context following structured approach
4. Generate change request summary using template format
5. Provide clear transition to technical scope analysis phase

## Error Handling
You WILL handle these scenarios:
- **Prerequisites Incomplete**: Stop execution and request prerequisite phase completion with specific guidance
- **Source Document Access Failed**: Provide clear error message and alternative access methods
- **Missing Business Context**: Request additional information from stakeholders with specific questions
- **Stakeholder Information Incomplete**: Identify gaps and request stakeholder contact details
- **Requirements Ambiguity**: Flag unclear requirements and request clarification with specific examples
- **Timeline Conflicts**: Document conflicts and request business priority clarification
- **Template Access Failed**: Provide manual template structure and formatting requirements
- **File Save Failures**: Offer alternative save locations and manual file creation steps

**Critical Requirements**
- MANDATORY: Complete prerequisite validation before any analysis work
- MANDATORY: Preserve traceability to original source document (JIRA ticket, issue, etc.)
- NEVER create duplicate change request documentation when prerequisites exist
- NEVER proceed without clear business justification for timeline requirements
- ALWAYS validate that MVP scope is realistic and achievable
- ALWAYS ensure stakeholder authority is documented and verified
- ALWAYS categorize requirements with testable acceptance criteria
- NEVER make assumptions about business priorities without documented evidence