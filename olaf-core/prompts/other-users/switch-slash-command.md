---
name: switch-slash-command
description: Switch between slash command profiles and manage active command sets with profile listing and activation
tags: [slash-commands, profile-switching, command-management, activation]
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
- **target_profile**: string - Profile name to switch to (OPTIONAL - will list available if not provided)
- **list_only**: boolean - Only list current profile without switching (OPTIONAL, default: false)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for profile listing
- You WILL use Propose-Act protocol for profile switching due to file generation impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Check manifest directory exists: `[id:reference_dir].manifests/`
- Validate default manifest exists: `[id:reference_dir].manifests/default.json`
- Verify platform directories exist: `.github/prompts/` and `.windsurf/workflows/`
- Scan for available profile manifests

### 2. Execution Phase

**Profile Discovery:**
<!-- <profile_scanning> -->
You WILL scan manifest directory for available profiles:
- List all `.json` files in `[id:reference_dir].manifests/`
- Exclude `default.json` from profile list (always active)
- Extract profile names from filenames
- Validate each manifest file structure
<!-- </profile_scanning> -->

**Current State Analysis:**
<!-- <current_state> -->
You WILL determine current active profile:
- Check for existing profile-specific command files in platform directories
- Identify active profile by analyzing command name suffixes
- Count active commands per platform
- Report current state to user
<!-- </current_state> -->

**Profile Listing (if no target specified):**
<!-- <profile_listing> -->
You WILL display available profiles:
- Show current active profile (if any)
- List all available profiles with command counts
- Display default commands (always active)
- Provide selection prompt for target profile
<!-- </profile_listing> -->

**Profile Switching (if target specified):**
<!-- <profile_switching> -->
You WILL execute profile switch:
1. **Cleanup Phase**: Remove existing profile-specific command files
   - Scan `.github/prompts/` for files with profile suffixes
   - Scan `.windsurf/workflows/` for files with profile suffixes
   - Delete only profile-specific files (preserve default commands)

2. **Generation Phase**: Create new profile command files
   - Load target profile manifest: `[id:reference_dir].manifests/[target_profile].json`
   - Generate platform files for each command in manifest
   - Use same format as existing command files
   - Apply naming convention: `command-name-profilename`

3. **Validation Phase**: Verify switch completion
   - Confirm all target profile commands are active
   - Validate default commands remain untouched
   - Report successful activation
<!-- </profile_switching> -->

**Core Logic**: Execute following protocol requirements
- Apply appropriate interaction protocol based on operation
- Provide clear current state information
- Execute cleanup and generation phases for switching
- Maintain default commands throughout process

### 3. Validation Phase
You WILL validate results:
- Confirm target profile is successfully activated
- Verify default commands remain available
- Check platform file consistency between .github and .windsurf
- Validate no orphaned files remain from previous profile

## Output Format
You WILL generate outputs following this structure:
- **Profile listing**: Current state and available options
- **Switch summary**: Commands removed, commands added, final state
- **Command inventory**: Complete list of active commands post-switch

## User Communication

### Progress Updates
- Current profile identification and command count
- Available profiles list with descriptions
- Cleanup progress during profile switching
- Generation progress for new profile commands
- Timestamp identifier used: [YYYYMMDD-HHmm format]

### Completion Summary
- **For Listing**: Current profile and available alternatives displayed
- **For Switching**: Profile successfully switched with command summary
- Active commands count: default + profile-specific
- Platform consistency confirmed across .github and .windsurf

### Next Steps
You WILL clearly define:
- Commands now available for use in slash command interfaces
- How to switch to different profile: `/switch-slash-command [profile_name]`
- How to list current state: `/switch-slash-command` (no parameters)
- Edit manifest files directly for customization

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Default commands MUST NEVER be removed during profile switching
- Rule 2: Profile switching MUST clean up previous profile commands completely
- Rule 3: Platform file consistency MUST be maintained (.github and .windsurf identical)
- Rule 4: Profile manifest validation MUST occur before switching
- Rule 5: Command name suffixes MUST match profile name exactly
- Rule 6: Orphaned files from incomplete switches MUST be cleaned up

## Success Criteria
You WILL consider the task complete when:
- [ ] Current profile state accurately identified and reported
- [ ] Available profiles discovered and validated
- [ ] Profile switching completed with full cleanup and generation
- [ ] Platform file consistency maintained across directories
- [ ] Default commands preserved throughout process
- [ ] User provided with clear post-switch command inventory
- [ ] No orphaned or conflicting files remain

## Required Actions
1. Scan and validate manifest directory for available profiles
2. Analyze current active profile state from existing command files
3. Execute appropriate action: listing or switching based on parameters
4. Maintain platform consistency and default command preservation
5. Provide comprehensive state summary and next steps

## Error Handling
You WILL handle these scenarios:
- **Manifest Directory Missing**: Create directory and request manifest generation
- **Invalid Target Profile**: List available profiles and request valid selection
- **Corrupted Manifest File**: Report specific file issues and suggest repair
- **Platform Directory Missing**: Create required directories automatically
- **File Deletion Failures**: Report specific conflicts and provide manual cleanup steps
- **Incomplete Previous Switch**: Detect and clean up orphaned files automatically
- **Default Manifest Missing**: Request creation of default manifest first
- **Profile Name Conflicts**: Validate profile names against existing files

⚠️ **Critical Requirements**
- MANDATORY: Never delete or modify default commands during profile switching
- MANDATORY: Maintain identical content between .github and .windsurf platforms
- NEVER leave orphaned files from incomplete profile switches
- ALWAYS validate manifest structure before profile switching
- ALWAYS provide complete cleanup of previous profile commands
- ALWAYS confirm platform consistency after switching
- ALWAYS preserve user's default command set