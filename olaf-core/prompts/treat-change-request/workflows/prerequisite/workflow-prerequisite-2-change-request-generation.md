# Workflow Prerequisite-2: Change Request Generation

## Overview

**Purpose**: Structure the extracted information into a formal change request document that **adapts to the natural structure** of the source documents. The output should match the demand type (Epic, User Story, Bug, Documentation Request, etc.) rather than forcing a rigid structure.

**Input**: Artifacts from Workflow Prerequisite-1

**Output**: Adaptive structured change request document

---

## Prompt Execution

### Prompt Prerequisite-2-1: Change Request Structuring

**File**: `../../prompts/prompt-prerequisite-3-change-request-structuring.md`

**Input**: 
- `prerequisite-1-demand-inventory.md`
- `prerequisite-2-extracted-information.md`

**Output**: `prerequisite-3-change-request.md`

**Template Reference** (NOT rigid structure): 
- `../../templates/template-prerequisite-change-request-adaptive.md`

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

## Completion Criteria

✅ **Workflow complete when**:

1. Output file exists
2. Demand type correctly identified
3. All extracted information is included
4. Structure adapted to match source (not forced)
5. Source terminology preserved
6. No omissions, inventions, or interpretations
7. Appropriate sections for demand type
8. Document ready for review and routing to Orchestrator-0-Router

---

## Handoff

**Next step**: Review and route to **Orchestrator-0-Router** for sizing and workflow assignment

**Provides**: `prerequisite-3-change-request.md`
