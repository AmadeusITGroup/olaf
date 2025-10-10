---
name: workflow-prerequisite-1-demand-analysis
description: Inventory demand documents and extract information prior to change request generation
tags: [workflow, sequential, treat-change-request]
---

# Workflow Prerequisite-1: Demand Analysis

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

Use terminal commands, not training data.

## Workflow Overview

**Purpose**: Scan the specified demand folder, inventory all documents, and extract all information without omission, invented, or interpretation.

**Input**: Demand folder path, optional MCP server access

**Output**: Two analysis documents providing complete inventory and extracted information

---

## Prerequisites

- Demand folder path available and readable.
- Optional: MCP server access configured if needed to fetch missing context.

---

## Input Requirements
- **Primary Input**: Demand folder path
- **Secondary Inputs**: Optional MCP access to JIRA, Confluence, GitHub
- **Input Format**: Folder of documents (md, pdf, docx as applicable)

## Output Specifications
- **Primary Output**: `prerequisite-1-demand-inventory.md`, `prerequisite-2-extracted-information.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute all steps in sequence - no skipping

### Prompt Prerequisite-1-1: Demand Document Gathering

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-prerequisite-1-demand-gathering.md`

**Input**: Demand folder path

**Output**: `prerequisite-1-demand-inventory.md`

**Description**: Inventory all available demand documents and produce a structured list.

**Validation**: All documents in folder accounted for; missing items noted.

### Prompt Prerequisite-1-2: Information Extraction

**File**: `[id:prompts_dir]treat-change-request/prompts/prompt-prerequisite-2-information-extraction.md`

**Input**: 
- `prerequisite-1-demand-inventory.md`
- All documents from the demand folder
- Optional: MCP server access to JIRA, Confluence, GitHub

**Output**: `prerequisite-2-extracted-information.md`

---

## Data Flow Diagram
```text
[demand folder] → [Step 1-1: inventory] → prerequisite-1-demand-inventory.md → [Step 1-2: extraction] → prerequisite-2-extracted-information.md
```

## Error Handling
- **Step Failure**: Stop and request a valid path or missing access; document gaps
- **Recovery**: Fix inputs and resume from failed step
- **Rollback**: Not applicable; outputs can be regenerated

## Completion Criteria
- [ ] All steps completed successfully
- [ ] `prerequisite-1-demand-inventory.md` and `prerequisite-2-extracted-information.md` generated
- [ ] No critical errors encountered

## Next Steps
- Proceed to `workflow-prerequisite-2-change-request-generation.md`

## Handoff

**Next workflow**: `workflow-prerequisite-2-change-request-generation.md`
