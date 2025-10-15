---
name: convert-prompt-existing
description: Convert existing prompts to follow established template structure and principles
tags: [prompt, conversion, refactor, template]
---


## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to**:
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
- **existing_prompt_path**: string - Path to the existing prompt file to convert (REQUIRED)
- **target_sub_category**: string - Sub-category folder for converted prompt (REQUIRED - present list to user)
- **preserve_name**: boolean - Whether to keep the original name or allow modification (OPTIONAL, default: true)
- **conversion_suffix**: string - Suffix for converted filename (OPTIONAL, default: "-converted")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act for prompt conversion due to moderate impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm existing prompt file exists and is accessible
- You MUST list available sub-categories by reading directory structure: `[id:prompts_dir]`
- You WILL present sub-category options to user and request selection for converted prompt
- Check access to required template and principles files
- Search `[id:prompts_dir]/[target_sub_category]` for naming conflicts

### 2. Execution Phase

**Source Analysis:**
<!-- <existing_prompt_analysis> -->
You MUST read and analyze: `[existing_prompt_path]`
You WILL extract: name, description, core functionality, input parameters, process logic, output requirements
<!-- </existing_prompt_analysis> -->

**Template and Principles Loading:**
<!-- <template_analysis> -->
You MUST read and analyze: `[id:templates_dir]/prompt-engineer/prompt-template.md`
<!-- </template_analysis> -->

<!-- <principles_analysis> -->
You MUST read and apply: `[id:templates_dir]/prompt-engineer/prompting-principles.md`
<!-- </principles_analysis> -->

**Core Logic**: You WILL execute following protocol requirements
- You MUST apply Propose-Act protocol for user approval of conversion
- You WILL convert existing prompt following template structure exactly:
  - Time Retrieval section with imperative language
  - Input Parameters with REQUIRED/OPTIONAL designation
  - User Interaction Protocol section
  - Process with structured phases (Validation/Execution/Validation)
  - Output Format specification
  - User Communication structure
  - Domain-Specific Rules with clear enforcement
  - Success Criteria checklist
  - Error Handling scenarios
  - Critical Requirements section
- You MUST preserve original core functionality and intent
- You MUST use imperative language throughout ("You WILL", "You MUST")
- You WILL include XML markup for complex sections
- You MUST ensure converted prompt includes comprehensive error handling
- You WILL enhance structure while maintaining original capabilities

### 3. Validation Phase
You WILL validate the converted prompt meets all requirements:
- Confirms to template structure completely (all sections present)
- Uses imperative language consistently throughout
- Includes User Interaction Protocol section
- Contains comprehensive error handling scenarios
- Has measurable success criteria
- Preserves original functionality and intent
- Follows established principles for clarity and execution
- Contains proper XML markup where appropriate

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Converted prompt following template exactly
- Conversion analysis: Before/after comparison highlighting improvements
- Validation checklist: Compliance verification against template and principles
- File location specification: `[id:prompts_dir]/[target_sub_category]/[original_name][conversion_suffix].md`

### Output Path Enforcement
- You MUST derive the canonical output filename as `<original_name><conversion_suffix>.md`.
- You MUST save ONLY to: `[id:prompts_dir]/[target_sub_category]/<original_name><conversion_suffix>.md`.
- You MUST NOT save converted files to any other path under `[id:prompts_dir]`.
- If a file with the canonical name already exists, you MAY overwrite it (never overwrite the original source file).

## User Communication

### Progress Updates
- Confirmation when existing prompt is successfully analyzed
- Confirmation when sub-category selection is obtained
- Confirmation when template and principles are successfully loaded
- Status of conflict check results in target sub-category
- Validation results for converted prompt

### Completion Summary
- Converted prompt presented for review via Propose-Act
- Conversion improvements summary showing structural enhancements
- Validation checklist results showing template compliance
- Save location confirmation if approved: `[id:prompts_dir]/[target_sub_category]/[original_name][conversion_suffix].md`

### Next Steps
You WILL clearly define:
- Converted prompt ready for use (pending user approval)
- Original prompt location: `[existing_prompt_path]` (preserved unchanged)
- Converted prompt location: `[id:prompts_dir]/[target_sub_category]/[original_name][conversion_suffix].md`
- Confirmation that conversion meets all quality standards

## Execution Environment and Closeout Cleanup

### Environment Selection
- You MUST detect the intended execution environment from context:
  - If `execution_environment` in context is `"powershell"`, you MUST use PowerShell commands.
  - If `execution_environment` in context is `"bash"`, you MUST use Bash commands.
  - If not provided, default to PowerShell on Windows and Bash on Unix.

### Temporary Artifacts Policy
- You MUST delete these temporary/intermediate files at the end of the conversion (Closeout step below).
- You MUST keep ONLY the canonical converted prompt file in `[id:prompts_dir]/[target_sub_category]/`.

### Closeout (Mandatory)
- After saving the final converted prompt to the canonical path, you MUST delete all temporary/intermediate files you created during the conversion.
- Use the appropriate command based on the selected environment:

PowerShell (Windows):
```
Remove-Item -Path "[id:project_root]\.straf\tmp\convert\<TIMESTAMP>" -Recurse -Force -ErrorAction SilentlyContinue
```

Bash (Unix/macOS/Linux):
```
rm -rf "[id:project_root]/.straf/tmp/convert/<TIMESTAMP>"
```

- If you created any additional drafts/intermediate files outside the temp folder, you MUST delete them too. Prefer deleting by exact paths you created during this run.

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER overwrite or modify the original prompt file
- Rule 2: Converted prompt MUST follow template structure exactly (all sections required)
- Rule 3: Converted prompt MUST use imperative language consistently
- Rule 4: Converted prompt MUST include User Interaction Protocol section
- Rule 5: Converted prompt MUST preserve original core functionality and intent
- Rule 6: Converted prompt MUST have comprehensive error handling
- Rule 7: Filename MUST use specified suffix to avoid conflicts
- Rule 8: Converted prompt MUST be saved in selected sub-category folder

## Success Criteria
You WILL consider the task complete when:
- [ ] Existing prompt successfully read and analyzed
- [ ] Sub-category selected and conflict check completed
- [ ] Template and principles files successfully loaded and analyzed
- [ ] Prompt converted following template structure exactly
- [ ] Original functionality and intent preserved completely
- [ ] Validation confirms 100% template and principles compliance
- [ ] User approval obtained via Propose-Act protocol
- [ ] Converted file saved successfully in correct sub-category
- [ ] Conversion summary provided with improvement details

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute operations following appropriate interaction protocol
3. Generate outputs in specified format
4. Provide user communication and confirmations
5. Define next steps if part of workflow

## Error Handling
You WILL handle these scenarios:
- **Source File Access Failed**: Provide clear error message and request valid file path
- **Sub-category Access Failed**: Provide error message and request manual sub-category specification
- **Invalid Sub-category Selection**: Re-present available options and request valid selection
- **Template/Principles File Access Failed**: Provide clear error message and manual alternatives
- **Naming Conflict in Target Location**: Suggest alternative naming options
- **Template Compliance Validation Failed**: Iterate conversion addressing specific missing sections
- **User Rejection During Propose-Act**: Request specific feedback and iterate conversion
- **File Save Failures in Sub-category**: Provide alternative save methods and troubleshooting steps
- **Original Functionality Loss**: Stop conversion and request guidance on acceptable modifications

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for all prompt conversions
- MANDATORY: Converted prompts MUST include ALL template sections without exception
- NEVER modify or overwrite original prompt files
- NEVER sacrifice original functionality for structural improvements
- ALWAYS preserve original intent and capabilities
- ALWAYS validate that converted prompts include comprehensive error handling
- ALWAYS ensure converted prompts use imperative language consistently
- NEVER save conversions without user approval
