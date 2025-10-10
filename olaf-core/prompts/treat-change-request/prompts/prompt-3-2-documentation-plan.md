---
name: convert-documentation-plan
description: Convert the Documentation Plan Creation prompt to standardized template, preserving stakeholder coverage and deliverables
tags: [prompt, conversion, documentation, plan]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior>
- <olaf-interaction-protocols>
You MUST strictly apply <olaf-framework-validation>.
 
## Input Parameters
- **design_path**: path - Final `DESIGN_<PROJECT-ID>.md` (REQUIRED)
- **spec_path**: path - Approved `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)

## User Interaction Protocol
- Propose-Act for conversion and plan drafting

## Process

### 1. Validation Phase
- Confirm both inputs exist
- Load template `../templates/template-documentation-plan.md`

### 2. Execution Phase
**Core Logic**:
- Perform stakeholder analysis and map information needs
- Generate user, API, operational, developer, and training documentation tasks (tickable)
- Define maintenance strategy and metrics

### 3. Validation Phase
- Ensure coverage for all stakeholder types
- Validate scope, timeline, and standards

## Output Format
- Primary deliverable: Documentation plan per `../templates/template-documentation-plan.md`

## User Communication
- Progress: sections generated
- Completion: plan ready for content team

## Domain-Specific Rules
- Rule 1: Use concise, actionable tasks
- Rule 2: Align deliverables to stakeholder personas

## Success Criteria
- [ ] Stakeholders mapped and covered
- [ ] All doc types planned with tasks
- [ ] Maintenance metrics defined

## Error Handling
- **Missing Inputs**: Request paths
- **Under-covered Stakeholders**: Flag gaps and request details

⚠️ **Critical Requirements**
- MANDATORY: Stakeholder-driven planning
- NEVER produce verbose narrative without tasks
