---
name: deploy-imported-prompts
description: Convert and deploy external prompts to OLAF competencies following approved mapping plan from carry-over
tags: [deploy, convert, integration, batch, implementation]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## Input Parameters
You MUST request these parameters if not provided by the user:
- **carry_over_file**: string - Path to carry-over file from import-prompts-to-competency session (REQUIRED)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Confirm-Act for deployment due to significant impact

## Prerequisites
This prompt is part of a 2-phase workflow chain:
1. You MUST verify the preceding phase (import-prompts-to-competency) was completed
2. You WILL validate expected outcomes from previous step:
   - Carry-over file exists at specified path
   - Carry-over contains complete mapping report
   - User decisions are documented
   - All prompts inventoried with source paths

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm carry-over file exists and is accessible
- Read and parse carry-over content
- Extract mapping report and user decisions
- Verify all required context is present (prompt inventory, mapping decisions, new competency specs)
- Check write access to `[id:competencies_dir]`

### 2. Execution Phase - New Competency Creation

**Identify New Competencies:**
You WILL execute:
- Parse carry-over for "CREATE NEW COMPETENCY" section
- Extract new competency names, classifications, and structures
- List new competencies for user confirmation

**Create New Competency Structures:**
For each new competency, you WILL execute:
- Create directory structure:
  ```
  [id:competencies_dir]/[new-competency-name]/
  ├── README.md
  ├── prompts/
  ├── templates/
  ├── scripts/ (if needed)
  └── competency-manifest.json
  ```
- Generate README.md with quick start guide
- Create empty competency-manifest.json with base structure
- Document creation in progress log

### 3. Execution Phase - Prompt Conversion

**Load Conversion Templates:**
You WILL read:
- `[id:competencies_dir]/prompt-engineer/templates/prompt-template.md`
- `[id:competencies_dir]/prompt-engineer/templates/prompting-principles.md`

**Process Each Prompt:**
For each prompt in mapping report, you WILL execute:

1. **Read Source Prompt:**
   - Load original prompt content from source path
   - Extract core functionality, logic, and requirements

2. **Convert to OLAF Format:**
   - Apply prompt-template.md structure
   - Transform to imperative language ("You WILL", "You MUST")
   - Add Framework Validation section
   - Add Time Retrieval section
   - Structure Input Parameters with REQUIRED/OPTIONAL
   - Add User Interaction Protocol section
   - Convert process to Validation/Execution/Validation phases
   - Add Output Format specification
   - Add User Communication structure
   - Add Domain-Specific Rules
   - Add Success Criteria checklist
   - Add Error Handling scenarios
   - Add Critical Requirements section
   - Preserve original functionality and intent

3. **Determine Target Location:**
   - Use mapping report to identify target competency
   - Generate filename in kebab-case format
   - Construct full path: `[id:competencies_dir]/[target-competency]/prompts/[prompt-name].md`

4. **Save Converted Prompt:**
   - Write converted prompt to target location
   - Confirm file creation
   - Log conversion in progress tracker

5. **Update Competency Manifest:**
   - Read target competency's `competency-manifest.json`
   - Add new entry_point:
     ```json
     {
       "id": "[prompt-name-kebab]",
       "file": "prompts/[prompt-name].md",
       "protocol": "[Act|Propose-Act|Propose-Confirm-Act]",
       "description": "[brief description]",
       "aliases": ["[trigger1]", "[trigger2]", "[trigger3]"],
       "required": false
     }
     ```
   - Generate aliases from trigger phrases in original analysis
   - Write updated manifest back to file
   - Confirm manifest update

**Track Conversion Progress:**
You WILL maintain:
```
CONVERSION PROGRESS - [timestamp]
==================================

Total Prompts: [N]
Converted: [X] / [N]
Failed: [Y]

## Completed:
✅ [prompt-name] → [target-competency]/prompts/[filename].md
✅ [prompt-name] → [target-competency]/prompts/[filename].md

## In Progress:
⏳ [prompt-name] → [target-competency]

## Failed:
❌ [prompt-name] - [error reason]
```

### 4. Execution Phase - Validation

**Validate Deployments:**
You WILL verify for each converted prompt:
- File exists at expected location
- Conforms to OLAF template structure
- Manifest updated correctly with entry_point
- Aliases are meaningful and trigger-appropriate
- Original functionality preserved

**Generate Validation Report:**
You WILL create:
```
DEPLOYMENT VALIDATION REPORT - [timestamp]
===========================================

## Deployment Summary:
- Total Prompts Processed: [N]
- Successfully Converted: [X]
- Failed Conversions: [Y]
- New Competencies Created: [Z]
- Existing Competencies Updated: [W]

## New Competencies:
1. [competency-name] - [description]
   - Location: [id:competencies_dir]/[competency-name]/
   - Prompts added: [count]

## Updated Competencies:
1. [competency-name] - Added [count] prompts
   - Prompts: [list]

## Failed Conversions:
1. [prompt-name] - [reason]
   - Action required: [manual steps]

## Files Modified:
- [list of all created/modified files with paths]
```

### 5. Collection Impact Analysis Phase

**Analyze Collection Requirements:**
You WILL determine:
- Which existing competencies received new prompts
- Which collections include those competencies
- Whether new competencies need collection assignment
- Current user's active collection from `query-competency-index.md`

**Generate Collection Recommendations:**
You WILL create:
```
COLLECTION UPDATE RECOMMENDATIONS - [timestamp]
================================================

## Current Collection:
Active: [collection-name]

## Recommended Actions:

### ✅ REINIT REQUIRED (Existing Competencies Updated)
Your current collection "[collection-name]" includes these updated competencies:
- [competency-name]: +[N] new prompts
- [competency-name]: +[M] new prompts

**Action**: Run collection reinit to update index with new prompts
**Command**: Use "select collection [collection-name] --reinit" workflow

### 🆕 ADD NEW COMPETENCIES (If Created)
New competencies created that may fit your workflow:
- [new-competency-name]: [description]
  - Suggested collections: [collection1, collection2]

**Action**: Consider adding to your active collection
**Command**: Manually edit competency-collections.json and reinit

## DO NOT Execute:
- Collection updates are NOT automatic
- User must decide and execute manually
- Provide commands but do NOT run them
```

**Present to User (NOT Execute):**
You WILL display:
- Complete collection recommendations
- Exact commands to run (but do NOT execute)
- Rationale for each recommendation
- Impact analysis if user chooses not to update

### 6. Completion Phase

**Generate Summary:**
You WILL create comprehensive completion report with:
- Total prompts converted and deployed
- New competencies created with locations
- Existing competencies updated with prompt counts
- Collection recommendations (not executed)
- Files modified with full paths
- Any failures or issues requiring attention

**Next Steps Communication:**
You WILL clearly instruct user:
```
✅ DEPLOYMENT COMPLETE

## What Was Done:
- [N] prompts converted to OLAF format
- [Z] new competencies created
- [W] existing competencies updated
- All manifests updated with entry points

## What You Need To Do:

### 1. Review Collection Recommendations (Above)
Decide if you want to:
- Reinit your current collection to include new prompts
- Add new competencies to your collection
- Leave collection as-is

### 2. Update Collection (If Desired):
- For reinit: "select collection [your-collection] --reinit"
- For adding new competency: Edit competency-collections.json manually

### 3. Test Converted Prompts:
- Try invoking new prompts using their trigger phrases
- Verify functionality matches original intent
- Report any issues for adjustment

## Files Modified:
[Complete list with paths]
```

### 7. Validation Phase
You WILL validate results:
- All prompts converted successfully or failures documented
- All manifests updated correctly
- New competencies have proper structure
- Collection recommendations are accurate and actionable
- User instructions are clear and complete
- No automatic collection updates were executed

## Output Format
You WILL generate outputs following this structure:
- Conversion Progress Tracker: Real-time status during conversion
- Deployment Validation Report: Comprehensive success/failure analysis
- Collection Update Recommendations: Clear guidance without auto-execution
- Completion Summary: All actions taken and next steps required

## User Communication

### Progress Updates
- Confirmation when carry-over loaded: "Loaded [N] prompts from mapping report"
- Status after new competency creation: "Created [Z] new competencies"
- Real-time conversion progress: "[X] of [N] prompts converted"
- Confirmation when manifest updated: "Updated [competency-name] manifest"
- Final collection recommendations: "Collection actions available (not auto-executed)"

### Completion Summary
- Total prompts deployed: [N]
- New competencies created: [Z]
- Existing competencies updated: [W]
- Collection recommendations: [provided but not executed]
- Next steps: [user actions required]

### Next Steps (User Actions Required)
You WILL clearly define:
- **Collection Decision**: Review recommendations and decide on updates
- **Manual Collection Update**: Use provided commands if desired
- **Testing**: Verify converted prompts work as expected
- **Issue Reporting**: Document any conversion problems
- **Optional Refinement**: Adjust aliases or descriptions as needed

## Domain-Specific Rules
You MUST follow these constraints:
- **Preserve Functionality**: Converted prompts must maintain original intent and capabilities
- **OLAF Compliance**: All converted prompts must conform to template structure
- **No Auto-Collection Updates**: NEVER automatically modify collection configuration or index
- **User Decision Required**: Collection changes require explicit user approval and execution
- **Manifest Integrity**: Ensure all entry_points have valid protocols and aliases
- **Error Transparency**: Document all conversion failures with clear reasons

## Success Criteria
You WILL consider the task complete when:
- [ ] Carry-over loaded and parsed successfully
- [ ] All new competencies created with proper structure
- [ ] All prompts converted to OLAF format
- [ ] All prompts deployed to target competencies
- [ ] All manifests updated with new entry_points
- [ ] Deployment validation completed
- [ ] Collection recommendations generated (not executed)
- [ ] User instructed on next steps clearly

## Required Actions
1. Load and parse carry-over file from previous session
2. Create new competency structures as specified in mapping
3. Convert all prompts to OLAF format using template
4. Deploy converted prompts to target competencies
5. Update all competency manifests with entry_points
6. Generate collection recommendations without executing
7. Provide clear user instructions for collection updates

## Error Handling
You WILL handle these scenarios:
- **Carry-Over Missing**: Request correct path from user
- **Incomplete Carry-Over**: Ask user to rerun import workflow
- **Conversion Failure**: Document failure, continue with remaining prompts
- **Manifest Corruption**: Backup original, attempt repair, notify user
- **Path Conflicts**: Check for existing files, request user decision on overwrite
- **Collection Detection Failed**: Proceed with generic recommendations

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Confirm-Act protocol throughout
- NEVER automatically update collection configuration or competency index
- ALWAYS provide collection recommendations as guidance only
- ALWAYS preserve original prompt functionality during conversion
- ALWAYS update manifests with converted prompts
- ALWAYS document failures clearly for manual resolution
- NEVER execute collection commands without explicit user request
- ALWAYS instruct user on manual collection update process
