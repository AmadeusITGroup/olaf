---
name: convert-prompt-existing
description: Convert existing prompts to follow established template structure and principles
tags: [prompt, conversion, refactor, template]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
You MUST request these parameters if not provided by the user:
- **existing_prompt_path**: string - Path to the existing prompt file to convert (REQUIRED)
- **target_competency**: string - Which competency to save converted prompt in (REQUIRED - present list to user from [id:competencies_dir])

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act for prompt conversion due to moderate impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm existing prompt file exists and is accessible
- You MUST list available competencies by reading directory structure: `[id:competencies_dir]`
- You WILL present competency options to user and request selection for converted prompt
- Check access to required template and principles files
- Search `[id:competencies_dir]/[target_competency]/prompts/` for naming conflicts

### 2. Execution Phase

**Source Analysis:**
<!-- <existing_prompt_analysis> -->
You MUST read and analyze: `[existing_prompt_path]`
You WILL extract: name, description, core functionality, input parameters, process logic, output requirements
<!-- </existing_prompt_analysis> -->

**Template and Principles Loading:**
<!-- <template_analysis> -->
You MUST read and analyze: `[id:competencies_dir]prompt-engineer/templates/prompt-template.md`
<!-- </template_analysis> -->

<!-- <principles_analysis> -->
You MUST read and apply: `[id:competencies_dir]prompt-engineer/templates/prompting-principles.md`
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

### 2.b Docs Subfolder Generation Phase
You WILL scaffold documentation for the converted entry point under the target competency docs:

- Create folder (if missing): `[id:competencies_dir][target_competency]/docs/[converted_prompt_id]/`
- Generate `description.md` using a standard description structure:
  - Overview, Purpose, Usage (command/aliases/protocol), Parameters, Output/Deliverables, Examples, Related Competencies, Tips, Limitations
  - If a sibling description template exists (e.g., `[id:competencies_dir][target_competency]/docs/review-code/description.md`), mirror its structure; otherwise, use the minimal structure above
- Generate `tutorial.md` by applying the step‑by‑step template:
  - Load: `[id:competencies_dir]prompt-engineer/templates/step-by-step-tutorial-template.md`
  - Populate with this prompt’s workflow and expected outputs
- Kebab‑case policy: Any example files MUST use lowercase kebab‑case names
- Propose to move/rename any existing example docs into this new subfolder using kebab‑case

### 3. Manifest Update Phase
You WILL update the target competency's manifest after converted prompt is saved:

**Manifest Update Process:**
- Read `[id:competencies_dir][target_competency]/competency-manifest.json`
- Add converted prompt entry_point with:
  - `id`: kebab-case version of converted prompt name
  - `file`: `prompts/[converted_prompt_name].md`
  - `protocol`: Appropriate protocol based on prompt's impact level
  - `description`: Brief description noting this is a converted/refactored version
  - `aliases`: Alternative names that invoke this prompt
  - `required`: false (user determines criticality)
- Update top-level `competencies` array (entry points catalog):
  - You MUST ensure the converted prompt `id` is present in this array.
  - If the array is missing, you MUST create it with the converted `id`.
- Write updated manifest back to file

**Automation Command (run from repo root):**

**Aliases Generation:**
You WILL generate useful aliases based on the converted prompt's functionality

### 4. Reindexing Proposal Phase
You WILL offer to update the competency index after manifest is modified:

**Reindexing Offer:**
Present to user:
```
✅ Prompt converted and manifest updated!

Next step: Update your competency index to make this converted prompt discoverable?

The competency index needs to be regenerated to include the converted prompt in:
- Condensed OLAF framework patterns
- Query competency index
- Collection-specific searches

Ready to reindex? (yes/no)
If yes: Execute command: python select_collection.py --collection [current_collection]
```

**Reindexing Execution:**
If user agrees:
- Detect current collection from `query-competency-index.md`
- Run: `python [id:competencies_dir]prompt-engineer/scripts/select_collection.py --collection [detected_collection]`
- Wait for script completion
- Validate pattern markers intact
- Confirm converted prompt pattern is in condensed framework

### 5. Validation Phase
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
- File location specification: `[id:competencies_dir]/[target_competency]/prompts/[original_name][conversion_suffix].md`

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
- Save location confirmation if approved: `[id:competencies_dir]/[target_competency]/prompts/[original_name][conversion_suffix].md`

### Next Steps
You WILL clearly define:
- Converted prompt ready for use (pending user approval)
- Original prompt location: `[existing_prompt_path]` (preserved unchanged)
- Converted prompt location: `[id:competencies_dir]/[target_competency]/prompts/[original_name][conversion_suffix].md`
- Confirmation that conversion meets all quality standards

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER overwrite or modify the original prompt file
- Rule 2: Converted prompt MUST follow template structure exactly (all sections required)
- Rule 3: Converted prompt MUST use imperative language consistently
- Rule 4: Converted prompt MUST include User Interaction Protocol section
- Rule 5: Converted prompt MUST preserve original core functionality and intent
- Rule 6: Converted prompt MUST have comprehensive error handling
- Rule 7: Filename MUST use specified suffix to avoid conflicts
- Rule 8: Converted prompt MUST be saved in selected competency's prompts folder

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
- [ ] Target competency's manifest updated with new entry_point
- [ ] New aliases generated and added to manifest
- [ ] Reindexing offered and completed if user agreed
- [ ] Converted prompt pattern verified in condensed framework (if reindexed)

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
- **Manifest File Not Found/Invalid**: Inform user and skip manifest update, offer manual update instructions
- **Manifest JSON Parse Error**: Attempt backup and recovery, provide manual update guide if recovery fails
- **Reindexing Script Not Found**: Provide alternate path suggestions and manual reindexing instructions
- **Reindexing Script Execution Failed**: Show error output and troubleshooting steps
- **Condensed Framework Markers Missing**: Alert user that framework may be corrupted, suggest restoration

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Act protocol for all prompt conversions
- MANDATORY: Converted prompts MUST include ALL template sections without exception
- NEVER modify or overwrite original prompt files
- NEVER sacrifice original functionality for structural improvements
- ALWAYS preserve original intent and capabilities
- ALWAYS validate that converted prompts include comprehensive error handling
- ALWAYS ensure converted prompts use imperative language consistently
- NEVER save conversions without user approval
