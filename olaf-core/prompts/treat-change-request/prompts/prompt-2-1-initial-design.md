---
name: convert-initial-design
description: Convert the Initial Design Creation prompt to standardized template, preserving prerequisites and design scope
tags: [prompt, conversion, design]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.
 
You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **spec_path**: path - Path to `SPECIFICATION_<PROJECT-ID>.md` (REQUIRED)
- **workspace_context**: string - Target codebase for pattern analysis (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and design creation

## Prerequisites (if applicable)
1. You MUST complete full specification analysis.
2. You MUST analyze existing codebase patterns (entities, services, controllers, repositories) with specific file references.

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `spec_path` exists and read entirely
- Confirm access to codebase for pattern analysis

### 2. Execution Phase
You WILL execute these operations as needed:

**Tool Operations**:
- `grep_search` + `read_file` to document existing patterns to follow/extend

**Core Logic**:
- Produce architecture, data model, security, UI, API, performance, and implementation planning sections
- Align design with existing patterns and constraints

### 3. Validation Phase
You WILL validate results:
- Ensure design addresses all FRs/NFRs
- Ensure pattern alignment and constraints documented

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Design document following `../templates/template-design-document.md`

## User Communication

### Progress Updates
- Confirmation of prereq completion
- Pattern analysis summary

### Completion Summary
- Design overview and key decisions

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-2-2-design-validation.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Cite specific existing patterns with file paths
- Rule 2: Do not drift from established conventions without justification

## Success Criteria
You WILL consider the task complete when:
- [ ] All design sections complete and aligned with patterns
- [ ] Constraints and risks documented
- [ ] Output follows template exactly

## Required Actions
1. Validate inputs
2. Analyze patterns and produce design
3. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Evidence of Patterns**: Go deeper or flag
- **Template Access Issues**: Provide fallback outline inline

⚠️ **Critical Requirements**
- MANDATORY: Pattern-aligned design
- NEVER skip prerequisites
