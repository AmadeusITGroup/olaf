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
- `[id:templates_dir]`: Directory containing workflow templates (from <olaf-memory-map>)
- `[id:prompts_dir]`: Directory where new workflows are created (from <olaf-memory-map>)
- `[id:memory_map]`: Memory map file for reference validation (from <olaf-memory-map>)
- `[workflow_name]`: Name of the workflow being generated (kebab-case)
- `[workflow_type]`: Type of workflow (sequential|iterative|decision|orchestrator)
- `[WORKFLOW_NAME]`: Workflow name placeholder in templates
- `[WORKFLOW_DESCRIPTION]`: Workflow description placeholder in templates

## Template Information

The following standardized workflow templates are available:

### Sequential Template

- **File**: `[id:templates_dir]prompt-engineer/workflow-template-sequential.md`
- **Use For**: Step-by-step processes where each step depends on previous step output
- **Features**: Individual tools/prompts per step, comprehensive error handling, flexible script support
- **Best For**: Code analysis pipelines, document processing chains, multi-stage validations

### Iterative Template 

- **File**: `[id:templates_dir]prompt-engineer/workflow-template-iterative.md`
- **Use For**: Processes that repeat until completion criteria are met
- **Features**: State management, user authorization between iterations, progress tracking
- **Best For**: Optimization processes, quality improvement cycles, convergence algorithms

### Decision Template

- **File**: `[id:templates_dir]prompt-engineer/workflow-template-decision.md` 
- **Use For**: Conditional branching based on data from previous workflows
- **Features**: Lookup tables, multi-criteria decisions, multiple file format support
- **Best For**: Classification workflows, routing logic, conditional processing

### Orchestrator Template

- **File**: `[id:templates_dir]prompt-engineer/workflow-template-orchestrator.md`
- **Use For**: Coordinating and chaining multiple complete sub-workflows
- **Features**: Sub-workflow coordination, state tracking, data flow management, progress reporting
- **Best For**: End-to-end business processes, complex automation pipelines, multi-stage analysis

## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **workflow_type**: string - Type of workflow to generate (sequential|iterative|decision|orchestrator)
- **workflow_name**: string - Name for the new workflow (must be kebab-case)
- **description**: string - Brief description of workflow purpose
- **input_spec**: object - Input specifications (optional if using interactive mode)
- **output_spec**: object - Output specifications (optional if using interactive mode)
- **mode**: string - Generation mode (interactive|specification)
- **spec_file**: string - Path to specification file (required if mode=specification)

## Input Validation
- **workflow_name**: Must be kebab-case format, no spaces or special characters
- **workflow_type**: Must be one of the four supported types
- **mode**: Must be either "interactive" or "specification"
- **spec_file**: Must exist and be readable if mode=specification
- **description**: Must be concise and descriptive (max 200 characters)

## Process

### 1. Determine Workflow Type
- If mode=interactive:
  1. Ask user workflow purpose and requirements
  2. Present workflow type options with examples:
     - **Sequential**: "Do you need steps that run in order, each using the previous step's output?"
     - **Iterative**: "Do you need to repeat a process until some criteria is met?"
     - **Decision**: "Do you need to choose different actions based on data analysis?"
     - **Orchestrator**: "Do you need to coordinate multiple complete workflows together?"
  3. Determine appropriate workflow type based on user response
- Else if mode=specification:
  1. Load and validate specification file
  2. Extract workflow type and parameters

### 2. Select and Load Template
- Load appropriate template based on workflow type:
  - Sequential: `[id:templates_dir]prompt-engineer/workflow-template-sequential.md`
  - Iterative: `[id:templates_dir]prompt-engineer/workflow-template-iterative.md`
  - Decision: `[id:templates_dir]prompt-engineer/workflow-template-decision.md`
  - Orchestrator: `[id:templates_dir]prompt-engineer/workflow-template-orchestrator.md`

### 3. Gather Workflow Details
- If interactive:
  - Ask template-specific questions based on workflow type:
    - **Sequential**: Number of steps, tools/prompts for each step, input/output flow
    - **Iterative**: Completion criteria, state management needs, max iterations
    - **Decision**: Decision criteria, data sources, branch logic, file formats
    - **Orchestrator**: Sub-workflows to chain, data transformation needs, coordination points
  - Validate inputs match required format
  - Confirm with user before proceeding
- Else:
  - Validate specification against template-specific JSON schema
  - Map specification to template fields

### 4. Generate Workflow File
- Create new file: `[id:prompts_dir][workflow_name].md`
- Populate template with gathered information
- Ensure all placeholders are replaced
- Follow file naming conventions (kebab-case)

### 5. Validate and Save
- Verify all required sections completed:
  - YAML front matter with proper metadata
  - Framework validation section
  - Time retrieval section
  - Template variables section
  - Template validation section
  - Workflow-specific sections (steps/iterations/decisions/sub-workflows)
  - Enhanced error handling section
- Check file references use memory map format `[id:...]` per <olaf-file-referencing-convention>
- Validate JSON structures if present
- Ensure all placeholders are properly replaced
- Verify tool references use flexible `.[ext]` format
- Save workflow file with kebab-case naming

## Output Specifications
- **Output File**: `[id:prompts_dir][workflow_name].md`
- **Format**: Markdown with YAML front matter
- **Validation Report**: Summary of generated workflow and any warnings

## Example Usage

### Interactive Mode
```
USER: generate-workflow --mode=interactive --workflow_name=analyze-code-complexity
ASSISTANT: Let's create a new workflow. What should this workflow accomplish?
[Interactive session continues...]
```

### Specification Mode
```
generate-workflow --mode=specification --spec_file=workflow-spec.json
```

## Error Handling
- If invalid input detected, provide specific error message and guidance
- If template not found, list available templates with descriptions
- If specification invalid, provide validation errors with template requirements
- If file already exists, prompt for confirmation before overwriting
- If workflow type unclear, provide examples and guidance for each type
- If template variables incomplete, prompt for missing required information
- If memory map references invalid, suggest correct format and available IDs

## Common Error Patterns
- **Invalid workflow name format:** Ensure kebab-case naming (e.g., "analyze-code-complexity")
- **Template file not found:** Verify template exists in `[id:templates_dir]prompt-engineer/`
- **Workflow file already exists:** Prompt user for confirmation before overwriting
- **Missing required parameters:** Interactive mode should gather all needed information
- **Invalid memory map ID:** Check that all `[id:...]` references exist in <olaf-memory-map>
- **Specification file malformed:** Validate JSON structure against template schema
- **Template placeholder not replaced:** Ensure all `[PLACEHOLDER]` values are substituted
- **Framework validation missing:** All generated workflows must include <olaf-work-instructions> compliance sections
- **Tool reference format incorrect:** Use flexible `.[ext]` format instead of hardcoded extensions

## Template-Specific Validation
- **Sequential**: Verify step dependencies and tool/prompt references, ensure logical flow
- **Iterative**: Validate completion criteria and state management setup, check max iteration limits
- **Decision**: Check lookup tables, decision criteria, file format support, and default branches
- **Orchestrator**: Verify sub-workflow chain logic, data flow compatibility, and state tracking

## Quality Assurance
- **Template Compliance**: Generated workflow must include all standardized sections per <olaf-work-instructions>
- **Memory Map Validation**: All file references must use correct <olaf-memory-map> IDs per <olaf-file-referencing-convention>
- **Framework Integration**: <olaf-work-instructions> framework validation and time retrieval sections required
- **Error Handling**: Comprehensive error patterns and recovery strategies included
- **Documentation**: Clear descriptions and examples for all workflow components
- **File Naming**: Consistent kebab-case naming throughout

## Dependencies
- Standardized workflow templates in `[id:templates_dir]prompt-engineer/`
- JSON schema for specification validation (template-specific)
- Access to <olaf-memory-map> for file references validation per <olaf-file-referencing-convention>
- Framework validation requirements per <olaf-work-instructions>

## Related Files
- `[id:templates_dir]prompt-engineer/workflow-template-sequential.md` - Sequential workflow template
- `[id:templates_dir]prompt-engineer/workflow-template-iterative.md` - Iterative workflow template  
- `[id:templates_dir]prompt-engineer/workflow-template-decision.md` - Decision workflow template
- `[id:templates_dir]prompt-engineer/workflow-template-orchestrator.md` - Orchestrator workflow template
- `[id:templates_dir]workflow-schema.json` - JSON schema for specifications
- `[id:memory_map]` - Memory map file referenced by <olaf-memory-map>
