---
name: generate-routing-documentation-summary
description: Generate concise routing summary with copy-paste prompt for user to continue work in next orchestrator
tags: [routing, documentation, orchestrator, handoff, change-request]
---

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

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **context_package_path**: string - Path to 6-context-package.yaml from previous step (REQUIRED)
- **artifacts_path**: string - Path to directory containing artifacts 1-5 from workflows 0-1 and 0-2 (REQUIRED)
- **output_template_path**: string - Path to routing summary template (OPTIONAL, default: "../templates/template-routing-summary.md")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for routing documentation due to systematic nature and low impact

## Prerequisites
You MUST verify the preceding phase/action was completed:
1. You WILL validate expected outcomes from previous step:
   - Context package file: `6-context-package.yaml` exists and is complete
   - All artifacts 1-5 exist and are accessible
   - Final size classification has been determined
   - Target orchestrator has been selected

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm context package file exists and is accessible
- Validate all artifacts 1-5 are present in specified directory
- Check access to routing summary template
- Verify target orchestrator selection is complete

### 2. Execution Phase

<!-- <context_extraction> -->
**Context Package Analysis:**
You MUST extract from `6-context-package.yaml`:
- **Change Request ID**: [SACP-XXXXXX]
- **Size Classification**: [XS/S/M/L/XL]
- **Matrix Score**: [XX/25]
- **Confidence Score**: [XX%]
- **Target Orchestrator**: `orchestrator-[SIZE]-[name].md`
- **Effort Estimate**: [XX-YY person-days]
- **Duration**: [X-Y weeks]
- **Team Size**: [X-Y developers]
- **Risk Level**: [Low/Medium/High]
- **Modules**: [X]
- **Files**: [XX-YY]
- **LOC**: [X,XXX-Y,YYY]
- **Critical Pre-Actions**: Any blocking items from context package
<!-- </context_extraction> -->

<!-- <copy_paste_prompt_generation> -->
**Copy-Paste Prompt Creation:**
You MUST generate a CONCISE prompt the user can copy-paste to continue in next orchestrator:

**Template Structure**:
```
Execute Orchestrator-[SIZE] for change request [SACP-XXXXXX]:

- Change Request: [One-line description from prerequisite-3]
- Analysis Directory: olaf-works/demand/[SACP-XXXXXX]-analysis/
- Context Package: 6-context-package.yaml
- Size: [SIZE] ([XX]/25 points, [XX]% confidence)
- Effort: [XX-YY] person-days, [X-Y] weeks, [X-Y] developers

Critical Pre-Actions (if any):
[List ONLY blocking items from critical_highlights.blocking_items in context package - max 3 items]
[If none, write: "None - proceed directly to orchestrator"]

Read the context package (6-context-package.yaml) and begin specification workflow.
```

**Key Principle**: Keep it SHORT and actionable. User should be able to copy-paste it into next session.
<!-- </copy_paste_prompt_generation> -->

<!-- <summary_documentation> -->
**Routing Summary Generation:**
You WILL create concise routing documentation including:
- Final size classification with confidence metrics
- Target orchestrator identification
- Key statistics at a glance (effort, duration, team, risk, modules, files, LOC)
- Reference files listing (so user knows what exists)
- Copy-paste prompt ready for immediate use
<!-- </summary_documentation> -->

**Core Logic**: Execute following protocol requirements
- Apply Act protocol for systematic routing documentation
- Keep summary to 1 page or less (CONCISE!)
- Eliminate verbose documentation (all details are in artifacts 1-6)
- Focus on: (1) which orchestrator, (2) key stats, (3) copy-paste prompt
- Ensure copy-paste prompt has no placeholders

### 3. Validation Phase
You WILL validate the routing documentation:
- Confirm summary is concise (1 page or less)
- Verify copy-paste prompt is ready to use with no placeholders
- Validate key statistics are visible at a glance
- Ensure reference files are listed for user awareness
- Confirm output follows template structure exactly

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Routing summary using template `../templates/template-routing-summary.md`
- Copy-paste prompt ready for immediate use
- Key statistics summary for quick reference
- File location: `7-routing-summary.md`

## User Communication

### Progress Updates
- Confirmation when context package is successfully parsed
- Status updates during key information extraction
- Progress on copy-paste prompt generation
- Completion status for routing summary creation

### Completion Summary
- Routing decision: [SIZE] to [ORCHESTRATOR_FILE]
- Confidence level: [XX%] based on [XX/25] matrix score
- Copy-paste prompt generated and ready for use
- Routing summary created: `7-routing-summary.md`
- User can immediately copy the prompt and continue work

### Next Steps
You WILL clearly define:
- Routing summary complete and ready for user
- Copy-paste prompt available for next session
- Target orchestrator: [ORCHESTRATOR_FILE]
- All routing artifacts preserved for reference

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER create verbose documentation - keep summary concise (1 page max)
- Rule 2: Copy-paste prompt MUST have no placeholders - ready to use immediately
- Rule 3: Key statistics MUST be visible at a glance for quick reference
- Rule 4: ALWAYS list reference files so user knows what exists
- Rule 5: Focus on actionable information: orchestrator + stats + prompt
- Rule 6: Eliminate duplication with artifacts 1-6 (all details already there)
- Rule 7: Target orchestrator MUST be clearly identified and accessible
- Rule 8: Critical pre-actions MUST be limited to max 3 blocking items only

## Success Criteria
You WILL consider the task complete when:
- [ ] Context package successfully parsed and key information extracted
- [ ] Target orchestrator clearly identified from size classification
- [ ] Copy-paste prompt generated with no placeholders
- [ ] Key statistics visible at a glance (effort, duration, team, risk, modules, files, LOC)
- [ ] Reference files listed for user awareness
- [ ] Routing summary is concise (1 page or less)
- [ ] Output follows template structure exactly
- [ ] File `7-routing-summary.md` created successfully
- [ ] User can immediately copy prompt and continue work

## Required Actions
1. Validate all required input parameters and context package accessibility
2. Execute systematic routing documentation following Act protocol
3. Generate concise routing summary in specified template format
4. Provide copy-paste prompt ready for immediate use
5. Complete workflow with clear user guidance

## Error Handling
You WILL handle these scenarios:
- **Context Package Access Failed**: Provide clear error message and request valid file path
- **Missing Artifacts**: Report specific missing files and request artifact generation
- **Target Orchestrator Unclear**: Request size classification clarification
- **Template Access Failed**: Use standard markdown structure and continue with routing summary
- **Critical Pre-Actions Unclear**: Review context package for blocking items or mark as "None"
- **Copy-Paste Prompt Generation Failed**: Create manual prompt structure with available information
- **File Save Failures**: Provide alternative save methods and troubleshooting steps
- **Summary Length Exceeded**: Trim content to essential information only

**Critical Requirements**
- MANDATORY: Keep summary concise (1 page maximum) - eliminate verbose content
- MANDATORY: Copy-paste prompt MUST be ready to use with no placeholders
- NEVER create detailed documentation (all details are in artifacts 1-6)
- NEVER include verbose analysis (focus on actionable routing information)
- ALWAYS provide key statistics at a glance for quick decision making
- ALWAYS ensure target orchestrator is clearly identified and accessible
- ALWAYS limit critical pre-actions to maximum 3 blocking items
- ALWAYS validate that user can immediately continue work with provided prompt