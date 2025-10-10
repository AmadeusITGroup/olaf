---
name: convert-prerequisite-demand-gathering
description: Convert the Demand Document Gathering prerequisite to standardized template, preserving full inventory and non-interpretative reporting
tags: [prompt, conversion, prerequisite, inventory]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **demand_folder**: path - Folder containing demand documents (REQUIRED)

## User Interaction Protocol
- Propose-Act for conversion and inventory generation

## Process

### 1. Validation Phase
- Verify folder exists and is readable

### 2. Execution Phase
**Core Logic**:
- Recursively inventory all files with relative paths, extensions, size, last-modified
- Assess readability class (text, needs special handling, non-processable)
- Categorize (structured, communication, technical, supporting, other)
- Identify external references (JIRA IDs, URLs, etc.)

### 3. Validation Phase
- Ensure no files omitted and metadata captured

## Output Format
- Primary deliverable: `prerequisite-1-demand-inventory.md` per `../../templates/template-demand-inventory.md`

## Domain-Specific Rules
- Rule 1: Completeness over judgment; list everything
- Rule 2: No interpretation; factual reporting only

## Success Criteria
- [ ] Folder validated
- [ ] All files inventoried with metadata
- [ ] Readability assessed
- [ ] Categories assigned
- [ ] External refs identified

## Error Handling
- **Path Not Found**: Request correct path
- **Permission Issue**: Report and request access

⚠️ **Critical Requirements**
- MANDATORY: Zero-omission inventory
- NEVER filter based on perceived relevance
