# Prompt Prerequisite-1: Demand Document Gathering

## Purpose

Scan the specified demand folder, inventory all documents, and prepare for information extraction.

---

## Input

- **Demand Folder Path**: Absolute or relative path to the folder containing demand documents
- **Access Methods**: 
  - Local file system access
  - Network drive access if applicable

---

## Task Instructions

### Step 1: Validate Folder Access

1. **Check Folder Existence**
   - Verify the provided path exists
   - If not found, stop and request correct path

2. **Check Read Permissions**
   - Confirm read access to the folder
   - Note any permission issues

### Step 2: Scan Folder Contents

Recursively scan the demand folder and document:

1. **File Inventory**
   - List all files found (including subfolders)
   - Note file names (with full relative path from demand folder root)
   - Note file extensions

2. **File Metadata**
   - File size (in KB or MB)
   - Last modified date (if available)
   - File type (document, spreadsheet, presentation, image, text, etc.)

3. **Readability Assessment**
   - Identify files that can be read directly (text, markdown, CSV, JSON, XML)
   - Identify files that may need special handling (PDF, Word, Excel, PowerPoint)
   - Identify files that cannot be processed (images, binaries)
   - Note any corrupted or inaccessible files

### Step 3: Categorize Documents

Organize the inventory by document type:

1. **Structured Documents**
   - Requirements documents
   - Specifications
   - User stories
   - Epic descriptions

2. **Communication Documents**
   - Emails
   - Meeting notes
   - Presentations

3. **Technical Documents**
   - Architecture diagrams
   - API specifications
   - Data models

4. **Supporting Documents**
   - Research
   - Competitive analysis
   - User feedback

5. **Other**
   - Any documents that don't fit above categories

### Step 4: Identify External References

Scan file names and any quickly readable metadata for references to:

1. **Issue Tracking Systems**
   - JIRA ticket IDs (e.g., SACP-172207, PROJ-1234)
   - GitHub issue numbers

2. **Collaboration Platforms**
   - Confluence page URLs or IDs
   - SharePoint document links

3. **Related Systems**
   - External system names
   - API endpoints
   - Database names

---

## Output Format

Generate file: `prerequisite-1-demand-inventory.md`

Use **../../templates/template-demand-inventory.md** to structure the output.

---

## Success Criteria

- [ ] Folder path validated and accessible
- [ ] All files in folder inventoried (including subfolders)
- [ ] File metadata captured (name, size, type, date)
- [ ] Readability status assessed for each file
- [ ] Documents categorized by type
- [ ] External references identified
- [ ] No files omitted from inventory
- [ ] Output follows template exactly

---

## Tools to Use

- **list_dir**: List directory contents
- **file_search**: Search for files by pattern
- **read_file**: Read file contents to assess readability and quick metadata scan
- **grep_search**: Search for patterns (JIRA IDs, URLs, etc.) across files

---

## Principles

- **Completeness**: Every file must be listed, no exceptions
- **No Judgment**: List all files regardless of relevance assessment
- **Factual Only**: Report what exists, not what should exist
- **No Interpretation**: File categorization based on name/extension only at this stage

---

## Exit Criteria

Declare: **"Prerequisite Step 1 complete. All documents inventoried. Proceeding to information extraction."**

---

## Version History

- **v1.0** (2025-10-08): Initial prompt creation for prerequisite orchestrator

---

**Next Prompt**: `prompt-prerequisite-2-information-extraction.md`
