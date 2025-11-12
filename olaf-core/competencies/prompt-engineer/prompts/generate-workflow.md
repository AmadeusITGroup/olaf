---
name: generate-workflow
description: Create structured workflows from templates or specifications
tags: [workflow, automation, code-generation, templates]
---


## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## Template Variables
- `[id:competencies_dir]`: Directory containing all competencies with organized prompts
- `[workflow_name]`: Name of the workflow being generated (kebab-case)
- `[workflow_type]`: Type of workflow (sequential|iterative|decision|orchestrator)

## Input Parameters
- **workflow_type**: string - Type of workflow to generate (sequential|iterative|decision|orchestrator)
- **workflow_name**: string - Name for the new workflow (must be kebab-case)
- **description**: string - Brief description of workflow purpose
- **mode**: string - Generation mode (interactive|specification)

## Process

### 1. Determine Workflow Type
- If mode=interactive: Ask user workflow purpose and determine type
- Else if mode=specification: Load and validate specification file

### 2. Select and Load Template
- Load appropriate template based on workflow type
- Sequential, Iterative, Decision, or Orchestrator templates

### 3. Gather Workflow Details
- If interactive: Ask template-specific questions
- If specification: Validate specification against template schema

### 4. Generate Workflow File
- Create new file: `[id:competencies_dir]prompt-engineer/prompts/[workflow_name].md`
- Populate template with gathered information
- Follow file naming conventions (kebab-case)

### 5. Validate and Save
- Verify all required sections completed
- Check file references use memory map format
- Save workflow file with kebab-case naming

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Generated workflow file
- File location: `[id:competencies_dir]prompt-engineer/prompts/[workflow_name].md`
- Validation Report: Summary of generated workflow

## Error Handling
- If invalid input detected, provide specific error message
- If template not found, list available templates
- If specification invalid, provide validation errors
- If file already exists, prompt for confirmation

⚠️ **Critical Requirements**
- MANDATORY: Generated workflows must include framework validation
- MANDATORY: All file references must use correct memory map IDs
- NEVER compromise template structure
- ALWAYS validate input parameters before processing
- ALWAYS use kebab-case for file names
