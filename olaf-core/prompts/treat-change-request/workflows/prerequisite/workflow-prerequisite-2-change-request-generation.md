---
name: workflow-prerequisite-2-change-request-generation
description: Generate an adaptive change request from extracted information, preserving source structure and terminology
tags: [workflow, sequential, treat-change-request]
---

# Workflow Prerequisite-2: Change Request Generation

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

**Purpose**: Structure the extracted information into a formal change request document that adapts to the natural structure of the source documents and demand type (Epic, User Story, Bug, Documentation Request, etc.).

**Input**: Artifacts from Workflow Prerequisite-1

**Output**: Adaptive structured change request document

---

## Input Requirements
- **Primary Input**: `prerequisite-1-demand-inventory.md`, `prerequisite-2-extracted-information.md`
- **Secondary Inputs**: None
- **Input Format**: Markdown documents

## Output Specifications
- **Primary Output**: `prerequisite-3-change-request.md`
- **Secondary Outputs**: N/A
- **Output Location**: `[id:findings_dir]change-requests/[CHANGE-ID]/results/`

## Workflow Steps

Execute the step below.

### Prompt Prerequisite-2-1: Change Request Structuring

**File**: `../../prompts/prompt-prerequisite-3-change-request-structuring.md`

**Input**:
- `prerequisite-1-demand-inventory.md`
- `prerequisite-2-extracted-information.md`

**Output**: `prerequisite-3-change-request.md`

**Description**: Generate a change request whose structure matches the actual source documents and demand type. Do not force rigid frameworks.

**Validation**:
- Demand type correctly identified (Epic, Story, Bug, Doc, Clarification, etc.)
- Structure matches what's actually in source documents
- Source document terminology preserved (not forced into agile framework)
- All extracted information included in change request
- Appropriate sections for the identified demand type
- Missing information marked as [Not Provided], not invented
- No forced Epic/Feature/Story hierarchy if not in source
- Document ready for review and routing to Orchestrator-0-Router

---

## Data Flow Diagram
```text
[prerequisite-1-demand-inventory.md + prerequisite-2-extracted-information.md]
    → [Step 2-1: Change Request Structuring] → prerequisite-3-change-request.md
```

## Error Handling
- **Step Failure**: If inputs are incomplete, stop and return to Prerequisite-1 workflow
- **Recovery**: Complete missing inputs and re-run this step
- **Rollback**: Not applicable; output may be regenerated from inputs

## Completion Criteria
- [ ] Output file exists
- [ ] Demand type correctly identified
- [ ] All extracted information is included
- [ ] Structure adapted to match source (not forced)
- [ ] Source terminology preserved
- [ ] No omissions, inventions, or interpretations
- [ ] Appropriate sections for demand type
- [ ] Document ready for review and routing to Orchestrator-0-Router

## Next Steps
- Review and route to **Orchestrator-0-Router** for sizing and workflow assignment

## Handoff

**Next step**: Review and route to **Orchestrator-0-Router** for sizing and workflow assignment

**Provides**: `prerequisite-3-change-request.md`
