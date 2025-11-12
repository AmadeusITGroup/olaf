---
name: create-prompt
description: Generate structured prompts following established template and principles
tags: [prompt, generation, engineering, template]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
You MUST request these parameters if not provided by the user:
- **user_request**: string - The user's requirement or task description (REQUIRED)
- **prompt_name**: string - Desired name for the prompt (max 4 words, kebab-case) (REQUIRED)
- **target_competency**: string - Which competency to create the prompt in (REQUIRED - present list to user from [id:competencies_dir])

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Confirm-Act for prompt creation due to high impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm user request is clear and actionable
- Validate prompt name follows kebab-case convention (max 4 words)
- You MUST list available competencies by reading directory structure: `[id:competencies_dir]`
- You WILL present competency options to user and request selection
- Check access to required template and principles files (locate templates within selected competency or prompt-engineer)
- Search `[id:competencies_dir][target_competency]/prompts/` for existing prompts with similar functionality

### 2. Execution Phase

**Template and Principles Loading:**
<!-- <template_analysis> -->
You MUST read and analyze: `[id:competencies_dir][target_competency]/templates/prompt-template.md` (or from prompt-engineer if not found in target competency)
<!-- </template_analysis> -->

<!-- <principles_analysis> -->
You MUST read and apply: `[id:competencies_dir][target_competency]/templates/prompting-principles.md` (or from prompt-engineer if not found in target competency)
<!-- </principles_analysis> -->

**Core Logic**: You WILL execute following protocol requirements
- You MUST apply Propose-Confirm-Act protocol for user approval
- You WILL generate structured prompt following template structure exactly:
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
- You MUST use imperative language throughout ("You WILL", "You MUST")
- You WILL include XML markup for complex sections
- You MUST ensure generated prompt includes comprehensive error handling
- You WILL validate generated prompt includes all required template sections

### 2.b Docs Subfolder Generation Phase
You WILL scaffold documentation for the new entry point under the target competency docs:

- Create folder (if missing): `[id:competencies_dir][target_competency]/docs/[prompt_id]/`
- Generate `description.md` using a standard description structure:
  - Overview, Purpose, Usage (command/aliases/protocol), Parameters, Output/Deliverables, Examples, Related Competencies, Tips, Limitations
  - If a sibling description template exists (e.g., `[id:competencies_dir][target_competency]/docs/review-code/description.md`), mirror its structure; otherwise, use the minimal structure above
- Generate `tutorial.md` by applying the step‑by‑step template:
  - Load: `[id:competencies_dir]prompt-engineer/templates/step-by-step-tutorial-template.md`
  - Populate with this prompt’s workflow and expected outputs
- Kebab‑case policy: Any example files MUST use lowercase kebab‑case names


### 3. Manifest Update Phase
You WILL update the target competency's manifest after prompt is created:

**Manifest Update Process:**
- Read `[id:competencies_dir][target_competency]/competency-manifest.json`
- Add new prompt entry_point with:
  - `id`: kebab-case version of prompt_name
  - `file`: `prompts/[prompt_name].md`
  - `protocol`: Appropriate protocol (Act/Propose-Act/Propose-Confirm-Act based on prompt's impact)
  - `description`: Brief description from prompt frontmatter
  - `aliases`: Alternative names that invoke this prompt
  - `required`: false (user determines criticality)
- Update top-level `competencies` array (entry points catalog):
  - You MUST ensure the new entry point `id` is present in this array.
  - If the array is missing, you MUST create it with the new `id`.
- Write updated manifest back to file

Ensure you include at least 3–5 aliases per entry_point.

### 4. Reindexing Proposal Phase
You WILL offer to update the competency index after manifest is modified:

**Reindexing Offer:**
Present to user:
```
✅ Prompt created and manifest updated!

Next step: Update your competency index to make this prompt discoverable?

The competency index needs to be regenerated to include the new prompt in:
- Condensed OLAF framework patterns
- Query competency index
- Collection-specific searches

This is OPTIONAL - you can do it later, but recommended for immediate access.

Ready to reindex? (yes/no)
If yes: Execute command: python select_collection.py --collection [current_collection]
```

**Reindexing Execution:**
If user agrees:
- Detect current collection from `query-competency-index.md`
- Run: `python [id:competencies_dir]prompt-engineer/scripts/select_collection.py --collection [detected_collection]`
- Wait for script completion
- Validate that pattern markers are still intact in condensed framework
- Confirm new prompt pattern is now in condensed framework

### 5. Validation Phase
You WILL validate the generated prompt meets all requirements:
- Confirms to template structure completely (all sections present)
- Uses imperative language consistently throughout
- Includes User Interaction Protocol section
- Contains comprehensive error handling scenarios
- Has measurable success criteria
- Follows established principles for clarity and execution
- Contains proper XML markup where appropriate

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Complete prompt following template exactly
- Validation checklist: Compliance verification against template and principles
- File location specification: `[id:competencies_dir][target_competency]/prompts/[prompt_name].md`

## User Communication

### Progress Updates
- Confirmation when competencies are listed and user selection obtained
- Confirmation when template and principles are successfully loaded
- Status of duplicate check results in selected competency
- Validation results for generated prompt

### Completion Summary
- Generated prompt presented for review via Propose-Confirm-Act
- Validation checklist results showing template compliance
- Save location confirmation if approved: `[id:competencies_dir][target_competency]/prompts/[prompt_name].md`

### Next Steps
You WILL clearly define:
- Prompt ready for execution (pending user approval)
- File saved location: `[id:competencies_dir][target_competency]/prompts/[prompt_name].md`
- Confirmation that prompt meets all quality standards

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Generated prompt MUST follow template structure exactly (all sections required)
- Rule 2: Generated prompt MUST use imperative language consistently
- Rule 3: Generated prompt MUST include User Interaction Protocol section
- Rule 4: Generated prompt MUST have comprehensive error handling
- Rule 5: Filename MUST be kebab-case, max 4 words
- Rule 6: Generated prompt MUST include measurable success criteria
- Rule 7: You MUST present available competencies and require user selection
- Rule 8: File MUST be saved in selected competency's prompts folder: `[id:competencies_dir][target_competency]/prompts/`

## Success Criteria
You WILL consider the task complete when:
- [ ] All required parameters validated and obtained
- [ ] Competencies listed and user selection obtained
- [ ] Template and principles files successfully loaded and analyzed
- [ ] Duplicate check completed in selected competency (no conflicts found)
- [ ] Prompt generated following template structure exactly
- [ ] Validation confirms 100% template and principles compliance
- [ ] User approval obtained via Propose-Confirm-Act protocol
- [ ] File saved successfully in correct competency folder
- [ ] Generated prompt includes all critical sections (error handling, success criteria, etc.)
- [ ] Target competency's manifest updated with new entry_point
- [ ] New aliases generated and added to manifest
- [ ] Reindexing offered and completed if user agreed
- [ ] New prompt pattern verified in condensed framework (if reindexed)

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute operations following appropriate interaction protocol
3. Generate outputs in specified format
4. Provide user communication and confirmations
5. Define next steps if part of workflow

## Error Handling
You WILL handle these scenarios:
- **Missing/Unclear Requirements**: Request specific clarification with examples
- **Competencies Directory Access Failed**: Provide error message and request manual competency specification
- **Invalid Competency Selection**: Re-present available competencies and request valid selection
- **Template/Principles File Access Failed**: Try fallback to prompt-engineer templates, provide error if both fail
- **Duplicate Prompt Found**: Present existing prompt and ask for modification preferences
- **Template Compliance Validation Failed**: Regenerate prompt addressing specific missing sections
- **User Rejection During Propose-Confirm-Act**: Request specific feedback and iterate
- **File Save Failures**: Provide alternative save methods and troubleshooting steps
- **Manifest File Not Found/Invalid**: Inform user and skip manifest update, offer manual update instructions
- **Manifest JSON Parse Error**: Attempt backup and recovery, provide manual update guide if recovery fails
- **Reindexing Script Not Found**: Provide alternate path suggestions and manual reindexing instructions
- **Reindexing Script Execution Failed**: Show error output and troubleshooting steps
- **Condensed Framework Markers Missing**: Alert user that framework may be corrupted, suggest restoration

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Confirm-Act protocol for all prompt generation
- MANDATORY: Generated prompts MUST include ALL template sections without exception
- NEVER generate prompts that don't use imperative language consistently
- NEVER skip validation phase - all generated prompts must be verified against template
- ALWAYS ensure generated prompts include comprehensive error handling
- ALWAYS validate that generated prompts include measurable success criteria
- NEVER save prompts without explicit user approval
