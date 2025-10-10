---
name: convert-routing-documentation
description: Convert the Routing Documentation prompt to standardized template, preserving concise routing summary and copy-paste prompt generation
tags: [prompt, conversion, routing, summary]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **context_yaml_path**: path - Path to `6-context-package.yaml` (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and documentation

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `context_yaml_path` exists and includes required fields

### 2. Execution Phase
You WILL execute these operations as needed:

**Core Logic**:
- Extract key stats from context package (ID, Size, Score, Confidence, Target Orchestrator, Effort, Duration, Team, Risk, Modules/Files/LOC)
- Generate a concise routing summary
- Create a ready-to-copy prompt that references the context package and orchestrator
- Keep output to one page or less

### 3. Validation Phase
You WILL validate results:
- Ensure copy-paste prompt has no placeholders
- Ensure summary is concise and contains key stats

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Routing summary following `../templates/template-routing-summary.md`
- Output file name: `7-routing-summary.md`

## User Communication

### Progress Updates
- Confirmation of YAML parsing
- Status of summary and prompt generation

### Completion Summary
- Location of `7-routing-summary.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Be concise; avoid verbose documentation
- Rule 2: Ensure prompt is actionable without edits

## Success Criteria
You WILL consider the task complete when:
- [ ] Summary ≤ 1 page
- [ ] Copy-paste prompt is ready with no placeholders
- [ ] Key stats visible at a glance
- [ ] Output saved as `7-routing-summary.md`

## Required Actions
1. Validate input YAML
2. Generate concise summary and prompt
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Fields in YAML**: Request corrections or provide minimal viable summary

⚠️ **Critical Requirements**
- MANDATORY: Short, actionable output
- NEVER include verbose documentation duplicated from artifacts
