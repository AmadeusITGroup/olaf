# Prompt Prerequisite-2: Information Extraction

## Purpose

Extract all information from the inventoried demand documents without omission, invention, or interpretation. Capture everything literally as it appears in the source documents.

---

## Input

- **prerequisite-1-demand-inventory.md**: List of all documents with metadata
- **Demand Folder Contents**: All readable documents from the inventory
- **Optional MCP Server Access**: Access to JIRA, Confluence, or GitHub if external references need resolution

---

## Task Instructions

### Step 1: Process Each Document

For each readable document in the inventory:

1. **Read Full Content**
   - Open and read the entire document
   - Note any sections that are unreadable or corrupted

2. **Extract All Text Content**
   - Copy all text content verbatim
   - Preserve structure (headings, lists, tables)
   - Note any non-text elements (diagrams, images) by description only

3. **Identify Information Types**
   - Problem statements
   - Requirements (functional and non-functional)
   - User stories or use cases
   - Acceptance criteria
   - Business objectives
   - Stakeholder information
   - Technical specifications
   - Constraints and dependencies
   - Timeline information
   - Any other factual information

### Step 2: Handle External References

If documents reference external systems:

1. **List All External References**
   - JIRA ticket IDs
   - Confluence page URLs
   - GitHub issues
   - Other system references

2. **Assess Completeness**
   - Does the current set of documents contain all needed information?
   - Are external references critical to understanding the demand?

3. **MCP Server Usage Decision** (Only if needed)
   - **Use MCP Server IF**:
     - Critical information is missing
     - External references are abundant and necessary
     - MCP server is accessible
   - **Do NOT use MCP Server IF**:
     - All information is already in the documents
     - External references are supplementary only
     - MCP server is not accessible

4. **Fetch External Content** (if decision is to use MCP)
   - Retrieve referenced JIRA tickets
   - Retrieve referenced Confluence pages
   - Retrieve referenced GitHub issues
   - Document what was fetched and why

### Step 3: Extract Structured Information

Look for and extract (if present in documents):

1. **Epic Information**
   - Epic title
   - Epic description
   - Epic goals/objectives
   - Epic acceptance criteria

2. **Feature Information**
   - Feature names/titles
   - Feature descriptions
   - Features linked to epics (if mentioned)
   - Feature acceptance criteria

3. **User Story Information**
   - User story format: "As a [user], I want [capability], so that [benefit]"
   - User story acceptance criteria
   - User stories linked to features (if mentioned)
   - Story points or estimates (if mentioned)

4. **Other Agile Artifacts**
   - Sprint information
   - Release planning information
   - Backlog prioritization

### Step 4: Extract Supporting Information

Capture all additional information found:

1. **Business Context**
   - Problem statement
   - Business justification
   - ROI or value proposition
   - Market drivers

2. **Stakeholders**
   - Product owners
   - Business analysts
   - Development teams
   - End users
   - External parties

3. **Technical Context**
   - System architecture references
   - Integration points
   - Technology stack mentions
   - Performance requirements
   - Security requirements

4. **Constraints**
   - Budget constraints
   - Timeline constraints
   - Resource constraints
   - Technical constraints
   - Regulatory/compliance requirements

5. **Dependencies**
   - Other projects or initiatives
   - External teams
   - Third-party systems
   - Infrastructure dependencies

### Step 5: Document Extraction Process

Record:

1. **Documents Processed**
   - List of all documents successfully read
   - List of documents that could not be read (with reason)

2. **MCP Server Usage**
   - Was MCP server used? (Yes/No)
   - Why was it used or not used?
   - What was fetched (if used)?

3. **Information Gaps**
   - What information was not found?
   - What questions remain unanswered?
   - What assumptions cannot be validated?

---

## Output Format

Generate file: `prerequisite-2-extracted-information.md`

Use **../../templates/template-extracted-information.md** to structure the output.

---

## Success Criteria

- [ ] All readable documents processed
- [ ] All text content extracted verbatim
- [ ] Epic/Feature/User Story information identified (if present)
- [ ] All business context captured
- [ ] All stakeholder information captured
- [ ] All technical context captured
- [ ] All constraints and dependencies captured
- [ ] External references documented
- [ ] MCP server usage decision documented and justified
- [ ] Information gaps explicitly noted
- [ ] No data omitted from sources
- [ ] No data invented or assumed
- [ ] No interpretation beyond literal extraction
- [ ] Output follows template exactly

---

## Tools to Use

- **read_file**: Read document contents
- **grep_search**: Search for specific patterns (JIRA IDs, user story format, etc.)
- **semantic_search**: Find related content across multiple documents
- **MCP Server Tools** (only if needed and available):
  - JIRA API access
  - Confluence API access
  - GitHub API access

---

## Principles

- **Verbatim Extraction**: Copy text exactly as written, no paraphrasing
- **No Omission**: Capture every piece of information, even if it seems redundant
- **No Invention**: If information doesn't exist, mark as [Not Provided]
- **No Interpretation**: Do not infer meaning, team knowledge, or application details
- **No Assumptions**: Do not fill gaps with assumptions
- **Preserve Ambiguity**: If source is ambiguous, preserve that ambiguity
- **Document Uncertainty**: If something is unclear, mark it as [Unclear in source]

---

## Exit Criteria

Declare: **"Prerequisite Step 2 complete. All information extracted. Proceeding to change request structuring."**

---

## Version History

- **v1.0** (2025-10-08): Initial prompt creation for prerequisite orchestrator

---

**Next Prompt**: `prompt-prerequisite-3-change-request-structuring.md`
