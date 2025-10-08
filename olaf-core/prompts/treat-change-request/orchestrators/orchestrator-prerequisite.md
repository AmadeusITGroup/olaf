# Orchestrator Prerequisite: Demand Document Analysis

**Purpose**: Analyze demand documents from a specified folder and create a structured change request document with Epic, Features, and User Stories.

**Version**: 1.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Entry point for demands that exist as documents in a folder. Ensures work is done in a proper branch, scans all provided documents, extracts information without interpretation, and structures them into a change request document.

Executes three workflows in sequence:

1. Git branch validation and setup
2. Demand document gathering and analysis
3. Change request document generation

---

## Workflows

```
Orchestrator-Prerequisite
├── Workflow Prerequisite-0: Git Branch Setup
├── Workflow Prerequisite-1: Demand Analysis
└── Workflow Prerequisite-2: Change Request Generation
```

---

## Inputs

| Input | Description | Required |
|-------|-------------|----------|
| **Demand Folder Path** | Absolute or relative path to the folder containing demand documents | Yes |
| **MCP Server Access** | Optional access to JIRA, Confluence, GitHub via MCP server | No |
| **Requestor** | Person requesting the change | No |

---

## Outputs

| Output | Description |
|--------|-------------|
| **Demand Inventory** | List of all documents found in the folder |
| **Change Request Document** | Structured document with Epic, Features, User Stories |
| **Analysis Directory** | Complete analysis with all artifacts |
| **Tracking File** | `prerequisite-tracking.md` - Progress tracking for all workflows |

---

## Workflow Execution

### Workflow Prerequisite-0: Git Branch Setup

**File**: `../workflows/prerequisite/workflow-prerequisite-0-git-branch-setup.md`

**Input**: Current git repository state

**Outputs**: `prerequisite-0-branch-setup.md`

**Validation**: Work is being done in appropriate branch (not main/master)

---

### Workflow Prerequisite-1: Demand Analysis

**File**: `../workflows/prerequisite/workflow-prerequisite-1-demand-analysis.md`

**Input**: Demand folder path, optional MCP server access

**Outputs**: `prerequisite-1-demand-inventory.md`, `prerequisite-2-extracted-information.md`

**Validation**: All documents scanned, all information extracted without omission or invention

---

### Workflow Prerequisite-2: Change Request Generation

**File**: `../workflows/prerequisite/workflow-prerequisite-2-change-request-generation.md`

**Input**: Artifacts from Workflow Prerequisite-1

**Outputs**: `prerequisite-3-change-request.md`

**Validation**: Change request structured with Epic, Features, and User Stories (if information available)

---

### Completion Criteria

✅ **Prerequisite orchestrator execution is complete when**:

1. Work is being done in appropriate branch (not main/master)
2. All documents in the folder have been scanned
3. All information extracted without omission
4. Change request document generated with available structure
5. No data invented or interpreted beyond what's in the documents
6. MCP server used only if needed and accessible

---

## Success Criteria

This orchestrator is successful when:

### Required Outputs (File Validation)

- ✅ **Workflow Prerequisite-0 outputs exist**: `prerequisite-0-branch-setup.md`
- ✅ **Workflow Prerequisite-1 outputs exist**: `prerequisite-1-demand-inventory.md`, `prerequisite-2-extracted-information.md`
- ✅ **Workflow Prerequisite-2 outputs exist**: `prerequisite-3-change-request.md`

### Required Content Validation

- ✅ All documents in the folder have been inventoried
- ✅ All extractable information has been captured
- ✅ No data has been omitted from the source documents
- ✅ No data has been invented or assumed
- ✅ No interpretation beyond literal extraction has been made
- ✅ Epic, Features, User Stories structured if information is available in documents
- ✅ MCP server accessed only if information is incomplete and server is available

---

## Next Steps

After this orchestrator completes:

1. **Review** the generated change request document for completeness
2. **Supplement** any missing information if needed
3. **Route** to **Orchestrator-0-Router** for sizing and workflow assignment
4. **Optional**: Update demand folder with generated artifacts for traceability

---

## Principles

This orchestrator follows strict principles:

- **No Omission**: Every piece of information in the source documents must be captured
- **No Invention**: Do not create data that doesn't exist in the sources
- **No Interpretation**: Extract literally, do not infer team knowledge or application details
- **No Assumptions**: If information is missing, mark it as [Not Provided] rather than guessing
- **Structure When Possible**: If documents contain Epic/Feature/User Story information, structure it. If not, capture in flat format.

---

## Exception Handling

If during workflow execution:

- **Folder not found**: Stop and request correct path
- **No documents found**: Report empty folder, cannot proceed
- **Documents unreadable**: List problematic files, proceed with readable ones
- **MCP server unavailable**: Continue without it, note in output
- **Information incomplete**: Mark missing sections as [Not Provided], do not invent

**Actions**: Document in workflow outputs, complete what's possible, report gaps clearly

---

## End of Orchestrator

**Version**: 1.0  
**Execution Model**: Delegate to workflows (Prerequisite-1 → Prerequisite-2)  
**Validation**: Check workflow outputs before completion
