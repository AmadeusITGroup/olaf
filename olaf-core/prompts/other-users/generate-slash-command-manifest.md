---
name: generate-slash-command-manifest
description: Generate slash command manifests from competency index with categorized selection interface and multi-platform file creation
tags: [slash-commands, manifest, competency, multi-platform]
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
- **profile_name**: string - Name for the manifest profile (e.g., "developer", "researcher") (REQUIRED)
- **competency_selection**: array - List of competency indices to include (OPTIONAL - will present selection interface)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Confirm-Act protocol for manifest generation due to file creation impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm profile name is provided and follows naming conventions
- Validate access to competency index: `[id:competency_index]`
- Check manifest directory exists: `[id:reference_dir].manifests/`
- Verify platform directories exist: `.github/prompts/` and `.windsurf/workflows/`

### 2. Execution Phase

**Competency Index Analysis:**
<!-- <competency_loading> -->
You WILL read and parse: `[id:competency_index]`
You MUST extract all competency mappings with:
- Pattern arrays (user-facing trigger phrases)
- Workflow file paths
- Protocol types
- Role categories (from file paths)
<!-- </competency_loading> -->

**User Selection Interface:**
<!-- <selection_interface> -->
You WILL present competencies organized by role categories:
- Group by role: developer, researcher, project-manager, etc.
- Display numbered list with concise descriptions
- Show pattern examples for each competency
- Allow multiple selections via number ranges or individual numbers
- Provide "select all" option per category
<!-- </selection_interface> -->

**Manifest Generation:**
<!-- <manifest_creation> -->
You WILL create manifest JSON structure:
```json
{
  "profile": "[profile_name]",
  "commands": [
    {
      "name": "[command-name-profilename]",
      "competency_path": "[workflow_file_path]",
      "description": "[concise_description]"
    }
  ]
}
```
You MUST apply naming convention: `command-name-profilename` for profile commands
You WILL derive command names from competency workflow filenames
<!-- </manifest_creation> -->

**Platform File Generation:**
<!-- <platform_files> -->
You WILL generate files for both platforms:

**GitHub Format** (`.github/prompts/[command-name].prompt.md`):
- Follow existing `.prompt.md` format from current files
- Include competency description and usage
- Reference original competency workflow
- Use consistent structure with existing prompts

**Windsurf Format** (`.windsurf/workflows/[command-name].md`):
- Use identical content structure as GitHub format
- Maintain same naming convention
- Ensure cross-platform compatibility

You MUST NOT overwrite existing files - skip if file already exists
<!-- </platform_files> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Confirm-Act protocol for user approval
- Generate manifest file: `[id:reference_dir].manifests/[profile_name].json`
- Create platform-specific command files
- Provide comprehensive file creation summary

### 3. Validation Phase
You WILL validate results:
- Confirm manifest JSON is valid and complete
- Verify all selected competencies are included
- Check platform files were created successfully
- Validate no existing files were overwritten

## Output Format
You WILL generate outputs following this structure:
- **Primary deliverable**: Manifest JSON file with complete command mappings
- **Supporting files**: Platform-specific command files (.github and .windsurf)
- **Documentation**: Creation summary with file locations and skipped files

## User Communication

### Progress Updates
- Confirmation when competency index is loaded and parsed
- Display of categorized selection interface
- User selection confirmation with count summary
- File creation progress with success/skip status
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- Manifest file created: `[id:reference_dir].manifests/[profile_name].json`
- Platform files created count and locations
- Files skipped due to existing conflicts
- Total commands available in profile

### Next Steps
You WILL clearly define:
- Use `/switch-slash-command [profile_name]` to activate profile
- Edit manifest file directly for deletions: `[id:reference_dir].manifests/[profile_name].json`
- Run `repair-slash-manifest` if competency index changes
- Platform-specific activation instructions

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Profile command names MUST use `-profilename` suffix convention
- Rule 2: NEVER overwrite existing platform files - skip and report
- Rule 3: Manifest JSON MUST be valid and include all required fields
- Rule 4: Command descriptions MUST be concise (max 80 characters)
- Rule 5: Selection interface MUST group by role categories for usability
- Rule 6: Platform files MUST use identical content structure

## Success Criteria
You WILL consider the task complete when:
- [ ] Competency index successfully loaded and parsed
- [ ] User selection interface presented and choices confirmed
- [ ] Manifest JSON file created with valid structure
- [ ] Platform files generated for all selected competencies
- [ ] No existing files overwritten (conflicts reported)
- [ ] Validation confirms all outputs meet requirements
- [ ] User provided with activation instructions

## Required Actions
1. Load and parse competency index for role-based categorization
2. Present interactive selection interface with numbered options
3. Generate manifest JSON following established structure
4. Create platform-specific command files with conflict avoidance
5. Provide comprehensive completion summary and next steps

## Error Handling
You WILL handle these scenarios:
- **Competency Index Access Failed**: Provide clear error message and manual path verification
- **Invalid Profile Name**: Request valid name following kebab-case convention
- **Manifest Directory Missing**: Create directory structure automatically
- **Platform Directory Missing**: Create required directories with proper structure
- **File Creation Conflicts**: Skip existing files and provide detailed conflict report
- **Invalid JSON Generation**: Regenerate manifest with proper structure validation
- **User Selection Errors**: Re-present interface with clearer instructions
- **Empty Selection**: Request at least one competency selection

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Confirm-Act protocol for all file creation
- MANDATORY: Never overwrite existing platform files
- NEVER generate invalid JSON manifest structure
- ALWAYS provide role-based categorization in selection interface
- ALWAYS validate manifest structure before saving
- ALWAYS report file creation conflicts to user
- ALWAYS include activation instructions in completion summary