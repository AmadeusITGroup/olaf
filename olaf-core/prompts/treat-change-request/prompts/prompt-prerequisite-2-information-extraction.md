---
name: extract-demand-information-comprehensive
description: Extract all information from inventoried demand documents without omission, invention, or interpretation
tags: [information-extraction, demand-analysis, prerequisite-workflow, verbatim-capture]
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
- **prerequisite_1_file**: string - Path to prerequisite-1-demand-inventory.md file (REQUIRED)
- **demand_folder_path**: string - Path to folder containing all demand documents (REQUIRED)
- **mcp_server_access**: boolean - Whether MCP server access is available for external references (OPTIONAL, default: false)
- **output_template_path**: string - Path to template-extracted-information.md (OPTIONAL, default: ../../templates/template-extracted-information.md)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for information extraction due to low risk and high automation requirements

## Prerequisites
You MUST verify the preceding phase was completed:
1. You WILL validate that prerequisite-1-demand-inventory.md exists and contains document inventory
2. You MUST confirm expected outcomes from previous step:
   - Complete document inventory with metadata
   - Readable document list with access paths
   - Document categorization and status information

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm prerequisite-1-demand-inventory.md exists and is accessible
- Validate demand folder path exists and contains expected documents
- Check access to output template file
- Verify MCP server availability if external reference resolution is needed

### 2. Execution Phase

<!-- <document_processing> -->
**Document Content Extraction:**
You WILL process each readable document from the inventory:
- Execute command: `read_file` for each document in inventory
- Extract all text content verbatim without modification
- Preserve original structure including headings, lists, and tables
- Document any unreadable or corrupted sections with specific error details
<!-- </document_processing> -->

<!-- <information_categorization> -->
**Structured Information Identification:**
You WILL identify and extract these information types:
- Problem statements and business objectives
- Requirements (functional and non-functional specifications)
- User stories in format: "As a [user], I want [capability], so that [benefit]"
- Acceptance criteria for epics, features, and user stories
- Stakeholder information and roles
- Technical specifications and system architecture references
- Constraints (budget, timeline, resource, technical, regulatory)
- Dependencies (projects, teams, systems, infrastructure)
- Timeline and release planning information
<!-- </information_categorization> -->

<!-- <external_reference_handling> -->
**External Reference Resolution:**
You WILL handle external system references:
- Use tool: `grep_search` to identify JIRA ticket IDs, Confluence URLs, GitHub issues
- Assess completeness: Determine if external references are critical or supplementary
- Make MCP server usage decision based on information criticality:
  - **Use MCP Server IF**: Critical information missing AND MCP server accessible
  - **Do NOT use MCP Server IF**: Information complete OR references supplementary OR MCP unavailable
- Execute MCP tools: `jira_api`, `confluence_api`, `github_api` only when decision criteria met
- Document all external content fetched with justification
<!-- </external_reference_handling> -->

<!-- <agile_artifact_extraction> -->
**Agile Artifact Identification:**
You WILL extract structured agile information when present:
- Epic information: titles, descriptions, goals, acceptance criteria
- Feature information: names, descriptions, epic linkages, acceptance criteria
- User story information: complete user story format, acceptance criteria, feature linkages, estimates
- Sprint and release planning information
- Backlog prioritization details
<!-- </agile_artifact_extraction> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for automated information extraction
- Complete verbatim text extraction without interpretation
- Preserve all ambiguities and uncertainties from source documents
- Document extraction process with complete traceability

### 3. Validation Phase
You WILL validate extraction results:
- Confirm all readable documents processed successfully
- Verify no information omitted from source documents
- Validate no data invented or assumed beyond source content
- Ensure all external references documented with resolution status

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Follow template `../../templates/template-extracted-information.md`
- Output file: `prerequisite-2-extracted-information.md`
- Supporting documentation: Complete extraction process log with document-by-document status

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when document inventory is successfully loaded
- Status for each document processing (successful/failed with reasons)
- Confirmation when external reference assessment is complete
- MCP server usage decision with clear justification
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- Total documents processed successfully and unsuccessfully
- Types of information extracted (epics, features, user stories, etc.)
- External references identified and resolution status
- Information gaps explicitly documented
- Output file location: `prerequisite-2-extracted-information.md`

### Next Steps
You WILL clearly define:
- Prerequisite Step 2 completion declaration
- Files provided to next phase: `prerequisite-2-extracted-information.md`
- Immediate next action: Proceed to change request structuring
- Next prompt: `prompt-prerequisite-3-change-request-structuring.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER modify, paraphrase, or interpret source document content - extract verbatim only
- Rule 2: NEVER invent information not present in source documents - mark missing information as [Not Provided]
- Rule 3: NEVER make assumptions to fill information gaps - preserve ambiguity as [Unclear in source]
- Rule 4: ALWAYS preserve original document structure and formatting in extraction
- Rule 5: ALWAYS document uncertainty with specific markers: [Not Provided], [Unclear in source], [Corrupted section]
- Rule 6: MCP server usage MUST be justified with specific information criticality assessment
- Rule 7: External reference resolution MUST document what was fetched and why
- Rule 8: Extraction process MUST be completely traceable with document-by-document status

## Success Criteria
You WILL consider the task complete when:
- [ ] All readable documents from inventory processed successfully
- [ ] All text content extracted verbatim with structure preserved
- [ ] Epic/Feature/User Story information identified and extracted (if present)
- [ ] All business context, stakeholders, technical context captured
- [ ] All constraints and dependencies documented
- [ ] External references documented with resolution status
- [ ] MCP server usage decision documented and justified
- [ ] Information gaps explicitly noted with specific markers
- [ ] No data omitted, invented, or interpreted beyond literal extraction
- [ ] Output follows template structure exactly
- [ ] Extraction process fully documented with traceability
- [ ] Next phase declaration completed

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute document processing following Act protocol
3. Generate outputs in specified template format
4. Provide user communication and progress confirmations
5. Declare completion and define next workflow step

## Error Handling
You WILL handle these scenarios:
- **Missing Prerequisite File**: Stop process and request valid prerequisite-1-demand-inventory.md path
- **Inaccessible Demand Folder**: Provide clear error message and request accessible folder path
- **Document Read Failures**: Continue processing other documents, document specific failures with reasons
- **MCP Server Connection Failures**: Continue without external resolution, document unavailability
- **Template Access Issues**: Request alternative template path or provide manual structure guidance
- **Information Extraction Errors**: Document specific extraction issues, continue with available content
- **Output File Write Failures**: Provide alternative save methods and troubleshooting steps

## Critical Requirements
- MANDATORY: Follow Act protocol for automated information extraction workflow
- MANDATORY: Extract information verbatim without any modification or interpretation
- NEVER invent, assume, or interpret information beyond literal source content
- NEVER omit information present in source documents
- ALWAYS preserve ambiguities and uncertainties from source materials
- ALWAYS document extraction process with complete traceability
- ALWAYS mark missing or unclear information with specific indicators
- ALWAYS justify MCP server usage decisions with information criticality assessment
