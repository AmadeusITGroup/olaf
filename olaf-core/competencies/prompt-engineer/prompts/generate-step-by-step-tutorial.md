---

name: generate-step-by-step-tutorial

description: Generate step-by-step tutorial documents from conversations or workflow files

tags: [tutorial, documentation, step-by-step, workflow]

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

You MUST request these parameters if not provided by the user:

- **source_type**: string|"current_conversation"|"file" - Source of workflow to document (REQUIRED)

- **source_file**: string - Path to file containing workflow/conversation if source_type is "file" (REQUIRED if source_type="file")

- **workflow_name**: string - Name of the workflow/process being documented (REQUIRED)

- **target_language**: string|"English"|"French"|"Spanish"|"German" - Language for tutorial content (OPTIONAL, default: English)

- **tutorial_title**: string - Custom title for the tutorial (OPTIONAL, will be generated if not provided)



## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Act / Propose-Act / Propose-Confirm-Act (defined externally)

- Use Act protocol for tutorial generation (low risk operation)



## Process



### 1. Validation Phase

You WILL verify all requirements:

- Confirm source_type selection (current conversation or file)

- If source_type is "file", validate file exists and is accessible

- Confirm workflow_name is provided and descriptive

- Validate target_language selection

- Check access to tutorial template



### 2. Execution Phase



**Source Analysis**:

- If source_type is "current_conversation": Analyze the current conversation for workflow steps

- If source_type is "file": Read and analyze the provided file content

- Extract key workflow steps, user actions, system responses, and outputs

- Identify prerequisites, troubleshooting points, and verification steps



**Template Loading**:

You MUST read and apply: `[id:competencies_dir][competency]/templates/technical-writer/step-by-step-tutorial-template.md`



**Core Logic**: Execute following protocol requirements

- Apply Act protocol for generation

- Use tutorial template structure exactly

- Populate template with extracted workflow information

- Adapt content to target language

- Include specific commands, file paths, and expected outputs

- Create verification checklist based on workflow outcomes

- Add troubleshooting section for common issues

- Generate timeline expectations based on workflow complexity



### 3. Validation Phase

You WILL validate results:

- Confirm tutorial follows template structure completely

- Verify all workflow steps are documented clearly

- Check that prerequisites and troubleshooting are comprehensive

- Validate content is in requested target language



## Output Format

You WILL generate outputs following this structure:

- Primary deliverable: Complete tutorial following template `[id:competencies_dir][competency]/templates/technical-writer/step-by-step-tutorial-template.md`

- File location: `[id:findings_dir]pptx-folder/[workflow-name]-tutorial-YYYYMMDD-HHmm.md`

- Content adapted to target language with proper terminology



## User Communication



### Progress Updates

- Confirmation when source analysis is complete

- Status of template loading and content extraction

- Timestamp identifier used: YYYYMMDD-HHmm format



### Completion Summary

- Tutorial file created with location

- Summary of documented workflow steps

- Language used for content generation

- File ready for immediate use



### Next Steps

You WILL clearly define:

- Tutorial ready for review and use

- File location for easy access

- Suggestions for testing the documented workflow



## Domain-Specific Rules

You MUST follow these constraints:

- Rule 1: Always ask for source_type before beginning analysis

- Rule 2: If source_type is "file", validate file accessibility before proceeding

- Rule 3: Tutorial must include specific commands, file paths, and expected outputs

- Rule 4: Include verification checklist with measurable success criteria

- Rule 5: Adapt all content to requested target language

- Rule 6: Use template structure exactly without modifications



## Success Criteria

You WILL consider the task complete when:

- [ ] Source type confirmed and content analyzed

- [ ] Workflow name and target language obtained

- [ ] Tutorial template loaded and applied

- [ ] Step-by-step content generated with specific details

- [ ] Verification checklist and troubleshooting included

- [ ] Content adapted to target language

- [ ] File saved with proper naming convention

- [ ] User provided with file location and summary



## Required Actions

1. Request source_type and validate source accessibility

2. Obtain workflow_name and target_language parameters

3. Analyze source content for workflow steps

4. Generate tutorial using template structure

5. Save file with timestamped naming convention



## Error Handling

You WILL handle these scenarios:

- **Missing Source Type**: Request user to specify "current_conversation" or "file"

- **File Access Issues**: Provide clear error message and request valid file path

- **Unclear Workflow Steps**: Ask user for clarification on specific process steps

- **Template Access Failed**: Provide error message and manual template structure

- **Language Not Supported**: Default to English and inform user of limitation



⚠️ **Critical Requirements**

- MANDATORY: Always ask for source_type before starting analysis

- MANDATORY: Validate file accessibility if source_type is "file"

- NEVER generate tutorial without confirming workflow_name

- ALWAYS use template structure exactly as provided

- ALWAYS adapt content to requested target_language

- ALWAYS include specific commands and expected outputs

- ALWAYS provide verification checklist for workflow success

