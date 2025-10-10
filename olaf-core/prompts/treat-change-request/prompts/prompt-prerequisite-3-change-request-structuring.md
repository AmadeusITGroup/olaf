---
name: convert-prerequisite-change-request-structuring
description: Convert the Change Request Structuring prerequisite to standardized template, preserving adaptive structure based on source documents
tags: [prompt, conversion, prerequisite, change-request]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **inventory_path**: path - `prerequisite-1-demand-inventory.md` (REQUIRED)
- **extracted_info_path**: path - `prerequisite-2-extracted-information.md` (REQUIRED)

## User Interaction Protocol
- Propose-Act for conversion and structuring

## Process

### 1. Validation Phase
- Confirm both inputs exist

### 2. Execution Phase
**Core Logic**:
- Determine natural demand type based on extracted information (Epic+Features+Stories, Epic+Stories, Standalone Story, Bug, Documentation Request, Clarification, Tech Debt, Config Change, Other/Mixed)
- Create structure that mirrors the source (do NOT force hierarchy or agile terms not used in source)
- Always include contextual sections when available: Requirements, Business Context, Technical Context, Constraints & Dependencies, Acceptance/DoD, Information Gaps & Open Questions

### 3. Validation Phase
- Ensure all extracted information is preserved (no omissions or inventions)
- Ensure terminology and language match the source
- Add processing metadata: classification, sources, MCP usage, timestamp, completeness/confidence

## Output Format
- Primary deliverable: `prerequisite-3-change-request.md`
- Use `../../templates/template-prerequisite-change-request.md` as reference only (do not force its structure)

## Domain-Specific Rules
- Rule 1: Respect the source structure and terminology
- Rule 2: Mark gaps and ambiguities explicitly

## Success Criteria
- [ ] Demand type identified and justified
- [ ] Structure mirrors the source (no forced templates)
- [ ] All extracted information included
- [ ] Metadata complete with completeness/confidence

## Error Handling
- **Ambiguous Demand Type**: Select "Other/Mixed" and document rationale
- **Missing Sections**: Mark as [Not Provided] without filling gaps

⚠️ **Critical Requirements**
- MANDATORY: No invention or forced structure
- NEVER translate or reinterpret terminology beyond the source
