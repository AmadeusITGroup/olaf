---
name: scan-demand-folder-comprehensive-inventory
description: Scan specified demand folder, inventory all documents comprehensively, and prepare complete metadata for information extraction
tags: [demand-analysis, document-inventory, file-scanning, prerequisite-validation]
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
- **demand_folder_path**: string - Absolute or relative path to folder containing demand documents (REQUIRED)
- **include_subfolders**: boolean - Whether to scan subfolders recursively (OPTIONAL, default: true)
- **output_template_path**: string - Path to demand inventory template (OPTIONAL, default: "../../templates/template-demand-inventory.md")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for document inventory due to read-only nature and systematic approach

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm demand folder path is provided and accessible
- Validate folder existence and read permissions
- Check access to inventory template file
- Verify file scanning tools are available

### 2. Execution Phase

<!-- <folder_access_validation> -->
**Folder Access Validation:**
You MUST validate folder accessibility:
- You WILL verify the provided path exists using directory listing tools
- You MUST confirm read access to the folder and report any permission issues
- You WILL stop process and request correct path if folder is not found
- You MUST document folder validation results with specific error messages if applicable
<!-- </folder_access_validation> -->

<!-- <comprehensive_file_scanning> -->
**Comprehensive File Scanning:**
You WILL execute systematic folder scanning:

**File Inventory Collection:**
- You MUST list ALL files found including subfolders if specified
- You WILL note file names with full relative path from demand folder root
- You MUST capture file extensions for processing assessment
- You WILL ensure NO files are omitted from inventory regardless of type

**File Metadata Extraction:**
- You MUST capture file size in KB or MB for each document
- You WILL record last modified date when available
- You MUST determine file type (document, spreadsheet, presentation, image, text, etc.)
- You WILL assess file accessibility and note any corrupted or inaccessible files

**Readability Assessment:**
- You MUST identify files that can be read directly (text, markdown, CSV, JSON, XML)
- You WILL identify files requiring special handling (PDF, Word, Excel, PowerPoint)
- You MUST identify files that cannot be processed (images, binaries)
- You WILL document specific reasons for inaccessibility when encountered
<!-- </comprehensive_file_scanning> -->

<!-- <document_categorization> -->
**Document Categorization:**
You WILL organize inventory by document type using these categories:

**Structured Documents:**
- Requirements documents
- Specifications
- User stories
- Epic descriptions

**Communication Documents:**
- Emails
- Meeting notes
- Presentations

**Technical Documents:**
- Architecture diagrams
- API specifications
- Data models

**Supporting Documents:**
- Research
- Competitive analysis
- User feedback

**Other Documents:**
- Any documents that don't fit above categories
- You MUST categorize based on file name and extension only at this stage
- You WILL NOT interpret content for categorization
<!-- </document_categorization> -->

<!-- <external_reference_identification> -->
**External Reference Identification:**
You WILL scan file names and quickly readable metadata for external references:

**Issue Tracking Systems:**
- JIRA ticket IDs (e.g., SACP-172207, PROJ-1234)
- GitHub issue numbers
- Other ticketing system references

**Collaboration Platforms:**
- Confluence page URLs or IDs
- SharePoint document links
- Wiki references

**Related Systems:**
- External system names
- API endpoints
- Database names
- Integration references

You MUST use pattern searching tools to identify these references systematically.
<!-- </external_reference_identification> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for systematic document inventory
- Complete all scanning phases without omission
- Use imperative language throughout documentation
- Include comprehensive error handling for access issues
- Ensure factual reporting without interpretation

### 3. Validation Phase
You WILL validate inventory results:
- Confirm all files in folder have been inventoried including subfolders
- Verify file metadata is captured completely (name, size, type, date)
- Validate readability status is assessed for each file
- Ensure documents are categorized appropriately by type
- Confirm external references are identified systematically
- Verify no files are omitted from inventory

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete demand inventory using template `../../templates/template-demand-inventory.md`
- File metadata summary: Comprehensive listing with all captured information
- Categorization results: Documents organized by type with counts
- External references: List of all identified external system references

## User Communication

### Progress Updates
You WILL provide these status confirmations:
- Confirmation when folder path validation completes successfully
- Status updates during file scanning and metadata collection
- Progress on document categorization and external reference identification
- Completion status for inventory validation

### Completion Summary
You WILL provide comprehensive completion information:
- Total files inventoried with breakdown by type and readability
- Document categories identified with counts in each category
- External references found with specific system types
- Any access issues encountered with specific file paths
- File location: `prerequisite-1-demand-inventory.md`

### Next Steps
You WILL clearly define:
- Document inventory complete and ready for information extraction
- All files catalogued with metadata for processing decisions
- External references identified for potential follow-up
- Proceeding to prerequisite step 2: Information extraction

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: EVERY file must be listed without exception - no judgment about relevance
- Rule 2: Report only what exists factually - never invent or assume content
- Rule 3: File categorization based ONLY on name/extension at this stage
- Rule 4: No content interpretation - preserve for information extraction phase
- Rule 5: External references identified through pattern matching only
- Rule 6: Access issues must be documented specifically with error details
- Rule 7: Metadata collection must be comprehensive for all accessible files
- Rule 8: Output must follow template structure exactly without deviation

## Success Criteria
You WILL consider the task complete when:
- [ ] Folder path validated and confirmed accessible
- [ ] All files in folder inventoried including subfolders if specified
- [ ] File metadata captured completely (name, size, type, date)
- [ ] Readability status assessed for each file with specific reasons
- [ ] Documents categorized by type using established categories
- [ ] External references identified through systematic pattern searching
- [ ] No files omitted from inventory regardless of perceived relevance
- [ ] Output follows template structure exactly
- [ ] Inventory ready for information extraction phase

## Required Actions
1. Validate folder access and scan requirements
2. Execute comprehensive file scanning following Act protocol
3. Generate complete inventory with metadata and categorization
4. Provide systematic external reference identification
5. Prepare inventory for information extraction phase

## Error Handling
You WILL handle these scenarios:
- **Folder Not Found**: Stop process and request correct path with specific error message
- **Permission Denied**: Document specific access issues and request alternative access methods
- **Corrupted Files**: Note specific files that cannot be accessed with error details
- **Template Access Failed**: Provide manual template structure and continue with inventory
- **Pattern Search Failures**: Document search limitations and continue with available results
- **Large Directory Issues**: Provide progress updates and handle large inventories systematically
- **Network Access Issues**: Document network-related access problems with specific guidance

**Critical Requirements**
- MANDATORY: Follow Act protocol for systematic document inventory
- MANDATORY: Every file MUST be listed without exception
- NEVER make judgments about document relevance during inventory
- NEVER interpret document content during categorization phase
- ALWAYS report factually what exists without assumption or invention
- ALWAYS document access issues with specific error messages and file paths
- ALWAYS preserve completeness over convenience - no shortcuts allowed
- ALWAYS declare completion with exact phrase: "Prerequisite Step 1 complete. All documents inventoried. Proceeding to information extraction."