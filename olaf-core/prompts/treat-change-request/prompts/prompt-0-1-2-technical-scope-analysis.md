---
name: convert-technical-scope-analysis
description: Convert the Technical Scope Analysis prompt to standardized template with validations, preserving original scope and evidence-driven analysis
tags: [prompt, conversion, technical-scope, analysis]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate interaction protocol
You MUST strictly apply <olaf-framework-validation>.
## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Propose-Act for conversion and execution

## Prerequisites (if applicable)
1. You MUST verify that `1-change-request-summary.md` exists and is accessible.
2. You WILL validate that workspace context is provided and resolvable.

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm `summary_path` exists
- Confirm `workspace_context` provided
- Check access to search/list tools

### 2. Execution Phase
You WILL execute these operations as needed:

**Tool Operations**:
- `semantic_search` to identify affected modules/services tied to feature keywords
- `grep_search` to locate referenced classes/interfaces and endpoints
- `list_dir` to understand module structure
- `file_search` to enumerate affected file patterns

**Core Logic**:
- Identify affected modules and collect evidence
- Estimate files and LOC by type (prod/test/config)
- Inventory API changes (new/modified/deprecated)
- Analyze database impacts (schema, migration, queries)
- Map integration points (internal/external, message bus)
- Assess architecture impact (layers, patterns, dependencies)

### 3. Validation Phase
You WILL validate results:
- Evidence-backed module list complete
- File/LOC estimates traceable to searches
- API/DB changes documented with rationale
- Integrations listed and categorized
- Architecture impacts clearly stated

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Technical scope analysis following `../templates/template-technical-scope-analysis.md`
- Supporting notes: Evidence excerpts and search references

## User Communication

### Progress Updates
- Confirmation of inputs and tool readiness
- Summary of modules identified and evidence count
- Status of API/DB/integration inventories

### Completion Summary
- Scope analysis summary (modules, files, LOC, API/DB changes)
- Evidence references

### Next Steps (if part of workflow)
You WILL clearly define:
- Proceed to `prompt-0-1-3-risk-assessment.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: All estimates must be supported by codebase evidence
- Rule 2: Separate production vs test LOC estimates
- Rule 3: Clearly distinguish internal vs external integrations

## Success Criteria
You WILL consider the task complete when:
- [ ] Affected modules identified with evidence
- [ ] Files and LOC estimated by category
- [ ] API, DB, and integration changes inventoried
- [ ] Architecture impacts articulated
- [ ] Output follows template exactly

## Required Actions
1. Validate `summary_path` and workspace access
2. Execute searches and compile evidence
3. Produce analysis using the template
4. Provide user communication and confirmations

## Error Handling
You WILL handle these scenarios:
- **Missing Summary**: Request valid `summary_path`
- **Workspace Unavailable**: Request path or access details
- **Tool Failures**: Provide fallback manual steps and explain limitations

⚠️ **Critical Requirements**
- MANDATORY: Use evidence from actual codebase searches
- ALWAYS separate new vs modified vs test code estimates
- NEVER rely on assumptions without evidence
