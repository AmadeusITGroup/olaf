---
name: convert-prerequisite-information-extraction
description: Convert the Information Extraction prerequisite to standardized template, preserving verbatim, no-interpretation extraction rules
tags: [prompt, conversion, prerequisite, extraction]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **inventory_path**: path - `prerequisite-1-demand-inventory.md` (REQUIRED)
- **demand_folder**: path - Root folder containing documents (REQUIRED)
- **allow_mcp**: boolean - Whether MCP access is permitted if needed (OPTIONAL)

## User Interaction Protocol
- Propose-Act for conversion and extraction process

## Process

### 1. Validation Phase
- Confirm inventory exists and folder is accessible

### 2. Execution Phase
**Core Logic**:
- Read each readable document fully; note unreadable/corrupted items
- Extract all text verbatim, preserving structure; describe non-text elements
- Identify information types (epic, feature, stories, acceptance, objectives, stakeholders, technical specs, constraints, dependencies, timelines)
- Handle external references: list, assess completeness; if critical and allowed, fetch via MCP and document

### 3. Validation Phase
- Ensure no data omitted, invented, or interpreted
- Document information gaps and uncertainties explicitly

## Output Format
- Primary deliverable: `prerequisite-2-extracted-information.md` per `../../templates/template-extracted-information.md`

## Domain-Specific Rules
- Rule 1: Verbatim extraction only
- Rule 2: Preserve ambiguity and mark gaps explicitly

## Success Criteria
- [ ] All readable documents processed
- [ ] All text content extracted verbatim
- [ ] External references and MCP usage documented
- [ ] Gaps and ambiguities recorded

## Error Handling
- **Unreadable Documents**: List with reasons
- **MCP Inaccessible**: Document and proceed without

⚠️ **Critical Requirements**
- MANDATORY: No interpretation or invention
- NEVER fill gaps with assumptions
