# Workflow Prerequisite-1: Demand Analysis

## Overview

**Purpose**: Scan the specified demand folder, inventory all documents, and extract all information without omission, invention, or interpretation.

**Input**: Demand folder path, optional MCP server access

**Output**: Two analysis documents providing complete inventory and extracted information

---

## Prompt Execution

**Execute all prompts in sequence - no skipping**

### Prompt Prerequisite-1-1: Demand Document Gathering

**File**: `../../prompts/prompt-prerequisite-1-demand-gathering.md`

**Input**: Demand folder path

**Output**: `prerequisite-1-demand-inventory.md`

**Validation**: 
- All files in the folder have been listed
- File types identified (PDF, Word, Excel, Markdown, text, etc.)
- File sizes noted
- Readability status confirmed

---

### Prompt Prerequisite-1-2: Information Extraction

**File**: `../../prompts/prompt-prerequisite-2-information-extraction.md`

**Input**: 
- `prerequisite-1-demand-inventory.md`
- All documents from the demand folder
- Optional: MCP server access to JIRA, Confluence, GitHub

**Output**: `prerequisite-2-extracted-information.md`

**Validation**: 
- All readable documents have been processed
- All information extracted literally without interpretation
- No data omitted
- No data invented
- References to external systems noted
- MCP server usage documented (if used)

---

## Completion Criteria

✅ **Workflow complete when**:

1. Both output files exist
2. All documents in folder have been inventoried
3. All extractable information captured
4. No interpretation, invention, or omission occurred
5. Ready to hand off to Workflow Prerequisite-2

---

## Handoff

**Next workflow**: `workflow-prerequisite-2-change-request-generation.md`

**Provides**: `prerequisite-1-demand-inventory.md`, `prerequisite-2-extracted-information.md`
