---
name: [verb-entity-complement prompt name]
description: [Brief description of what this prompt accomplishes]
tags: [tag1, tag2, tag3, tag4]
---
CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.
## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **param_name**: type|options - Description (REQUIRED/OPTIONAL)
- **param_name**: type|options - Description (REQUIRED/OPTIONAL)
- **optional_param**: type|options - Optional description

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Select appropriate protocol based on operation risk and impact

## Prerequisites (if applicable)
If this prompt is part of a workflow chain:
1. You MUST verify the preceding phase/action was completed
2. You WILL validate expected outcomes from previous step:
   - [Expected file/data from previous phase]
   - [Required state or configuration]
   - [Specific deliverables that must exist]

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm all required parameters are provided
- Validate prerequisites are met (if applicable)
- Check access to required tools and files

### 2. Execution Phase
You WILL execute these operations as needed:

**Terminal Operations** (when required):
- Execute command: `[specific command with parameters]`
- Execute script: `[id:tools_dir]/script-name.ps1` for automation
- Validate command execution success

**Tool Operations** (when required):
- Use internal tool: `tool_name` for [specific purpose]
- Use MCP server tool: `mcp_server_name.tool_name` for [specific operation]

**File Operations** (when required):
- Read/Write file: `[id:file_reference]` or specific path
- Process file content according to requirements

**Core Logic**: Execute following protocol requirements
- Apply appropriate interaction protocol
- Complete core processing steps
- Provide required user confirmations

### 3. Validation Phase
You WILL validate results:
- Confirm all outputs meet requirements
- Verify functionality if applicable

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Follow template `[id:competencies_dir][competency]/templates/[template-name].md`
- Supporting files: [location and naming convention]
- Documentation: [specific format requirements]

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Confirmation when each major step completes
- Location/reference of any changes made
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- Summary of actions taken
- Files created/modified with locations
- Any issues encountered and resolutions

### Next Steps (if part of workflow)
You WILL clearly define:
- Immediate next actions required
- Objectives for next phase (concise, specific)
- Files/resources provided to next phase
- Dependencies for next step


## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: [Specific constraint with clear enforcement]
- Rule 2: [Order/sequence requirements with rationale]
- Rule 3: [Data validation rules with examples]
- Rule 4: [Security or safety requirements]

## Success Criteria
You WILL consider the task complete when:
- [ ] All required parameters validated
- [ ] Core logic executed successfully
- [ ] Outputs generated in specified format
- [ ] User communication completed
- [ ] Next steps defined (if applicable)

## Required Actions
1. Validate all required input parameters and prerequisites
2. Execute operations following appropriate interaction protocol
3. Generate outputs in specified format
4. Provide user communication and confirmations
5. Define next steps if part of workflow

## Error Handling
You WILL handle these scenarios:
- **Missing Parameters**: Request specific missing items from user
- **File Access Issues**: Provide clear error message and resolution steps
- **Tool Failures**: Offer alternative approaches or manual steps
- **Validation Failures**: Stop process and request user guidance

⚠️ **Critical Requirements**
- MANDATORY: Follow established interaction protocol (Act/Propose-Act/Propose-Confirm-Act)
- NEVER bypass protocol requirements
- ALWAYS validate outputs before considering task complete
- ALWAYS provide rollback instructions for destructive operations
- ALWAYS document assumptions and limitations
- ALWAYS confirm user approval for significant changes
