---
name: import-prompts-to-competency
description: Analyze external prompts collection and generate mapping recommendations for OLAF competency integration
tags: [import, analysis, mapping, batch, prompts, collection]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.


## Input Parameters
You MUST request these parameters if not provided by the user:
- **source_repository**: string - GitHub repository URL (e.g., "https://github.com/owner/repo") OR local path (REQUIRED)
- **source_path**: string - Path within repository to prompts folder (e.g., "/prompts", "/tree/main/prompts") (OPTIONAL, default: "/prompts")
- **file_pattern**: string - File pattern to match (e.g., "*.md", "*.txt") (OPTIONAL, default: "*.md")
- **scan_recursive**: boolean - Scan subdirectories recursively (OPTIONAL, default: true)

## Prerequisites - Downloading External Prompts

**IMPORTANT**: External prompts MUST be downloaded to local workspace before analysis.

**Download Location:**
You WILL create and use this directory structure:
- Create: `[id:findings_dir]/prompt-conversions/[source-repo-name]/`
- Never save prompts to workspace root
- Example: `olaf-data/findings/prompt-conversions/docupilot-prompts/`

**Download Instructions for User:**

### For GitHub Repositories (Recommended Method):

**PowerShell (Windows):**

```powershell
# Create download directory in findings folder
New-Item -ItemType Directory -Force -Path "olaf-data\findings\prompt-conversions\[repo-name]" | Out-Null

# Navigate to download directory
cd olaf-data\findings\prompt-conversions\[repo-name]

# Download using GitHub CLI (gh cli required)
$files = @('file1.md', 'file2.md', 'file3.md')
$files | ForEach-Object {
    Write-Host "Downloading $_..."
    gh api "repos/[owner]/[repo]/contents/[path]/$_" -H "Accept: application/vnd.github.v3.raw" > $_
}

# Return to workspace root
cd ..\..\..\..
```

**Example - DocuPilot Prompts:**

```powershell
New-Item -ItemType Directory -Force -Path "olaf-data\findings\prompt-conversions\docupilot-prompts" | Out-Null
cd olaf-data\findings\prompt-conversions\docupilot-prompts
$files = @('process_documentation.md', 'summary_section.md', 'limitations_section.md', 'preconditions_section.md', 'postconditions_section.md', 'input_section.md', 'output_section.md', 'diagram_workflow_section.md', 'description_section.md', 'data_description_section.md', 'warnings_errors_section.md', 'examples_section.md', 'associated_configurations_section.md', 'security_settings_section.md', 'other_processes_triggered_section.md')
$files | ForEach-Object { Write-Host "Downloading $_..."; gh api "repos/Amadeus-xDLC/DocuPilot.generate-backend-functional-doc-from-code/contents/prompts/$_" -H "Accept: application/vnd.github.v3.raw" > $_ }
cd ..\..\..\..
```

**Bash (Linux/macOS):**

```bash
# Create download directory in findings folder
mkdir -p olaf-data/findings/prompt-conversions/[repo-name]

# Navigate to download directory
cd olaf-data/findings/prompt-conversions/[repo-name]

# Download using GitHub CLI (gh cli required)
files=("file1.md" "file2.md" "file3.md")
for file in "${files[@]}"; do
    echo "Downloading $file..."
    gh api "repos/[owner]/[repo]/contents/[path]/$file" -H "Accept: application/vnd.github.v3.raw" > "$file"
done

# Return to workspace root
cd ../../../..
```

**Example - DocuPilot Prompts:**

```bash
mkdir -p olaf-data/findings/prompt-conversions/docupilot-prompts
cd olaf-data/findings/prompt-conversions/docupilot-prompts
files=("process_documentation.md" "summary_section.md" "limitations_section.md" "preconditions_section.md" "postconditions_section.md" "input_section.md" "output_section.md" "diagram_workflow_section.md" "description_section.md" "data_description_section.md" "warnings_errors_section.md" "examples_section.md" "associated_configurations_section.md" "security_settings_section.md" "other_processes_triggered_section.md")
for file in "${files[@]}"; do
    echo "Downloading $file..."
    gh api "repos/Amadeus-xDLC/DocuPilot.generate-backend-functional-doc-from-code/contents/prompts/$file" -H "Accept: application/vnd.github.v3.raw" > "$file"
done
cd ../../../..
```

**Alternative - Git Clone (if full repo access needed):**

```bash
# Clone entire repository to findings folder
git clone https://github.com/[owner]/[repo].git olaf-data/findings/prompt-conversions/[repo-name]

# Prompts will be at: olaf-data/findings/prompt-conversions/[repo-name]/[prompts-path]
```

### For Local Repositories:

If prompts are in another local repository, provide absolute path:
- Example: `C:\Users\[user]\repos\other-project\prompts`
- Or: `/home/[user]/repos/other-project/prompts`

**User Action Required:**
You MUST instruct user to download prompts BEFORE proceeding with analysis:
1. Display appropriate download commands based on user's OS
2. Wait for user confirmation that prompts are downloaded
3. Verify downloaded files exist before starting analysis

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Confirm-Act for this workflow due to significant impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm source path exists and is accessible
- Verify current OLAF competency structure at `[id:competencies_dir]`
- Check access to competency-collections.json
- Get current timestamp for carry-over naming

### 2. Execution Phase - Prompt Discovery

**Scan Source Location:**
You WILL execute:
- Use file_search or list_dir to discover all matching files in source_path
- Apply file_pattern filter (default: *.md)
- If scan_recursive=true, include all subdirectories
- Generate list of discovered prompt files with full paths
- Present count to user: "Found [N] prompt files in source location"

**Initial Analysis:**
You WILL analyze each discovered file:
- Read file content
- Extract key characteristics:
  - Purpose/objective (what the prompt does)
  - Domain/topic area (e.g., code review, documentation, testing)
  - Input parameters required
  - Output format expectations
  - Trigger phrases/keywords that would invoke this prompt
  - Complexity level (simple/moderate/complex)
  - Dependencies on other prompts or tools

**Generate Prompt Inventory:**
You WILL create structured inventory:
```
PROMPT INVENTORY - [timestamp]
================================

Total Prompts Found: [N]

## Prompt Analysis:

### Prompt 1: [filename]
- **Path**: [full_path]
- **Purpose**: [what it does]
- **Domain**: [topic area]
- **Triggers**: [keywords that invoke it]
- **Complexity**: [simple/moderate/complex]
- **Parameters**: [list of inputs]
- **Dependencies**: [other prompts/tools needed]

### Prompt 2: [filename]
...
```

### 3. Execution Phase - Competency Mapping

**Load Existing OLAF Competencies:**
You WILL execute:
- List all directories in `[id:competencies_dir]`
- For each competency, read README.md or competency-manifest.json
- Extract competency purpose, domain, and existing prompts
- Create competency catalog for mapping

**Generate Mapping Recommendations:**
You WILL analyze each external prompt against OLAF competencies:
- Compare prompt domain to competency domains
- Identify best-fit existing competencies
- Flag prompts requiring new competency creation
- Identify hybrid cases (prompt spans multiple competencies)
- Calculate confidence score for each mapping (high/medium/low)

**Create Mapping Report:**
You WILL generate:
```
COMPETENCY MAPPING REPORT - [timestamp]
========================================

## Summary:
- Total Prompts: [N]
- → Existing Competencies: [M] prompts
- → New Competency Needed: [P] prompts  
- → Hybrid Distribution: [Q] prompts

## Mapping Details:

### ✅ MAP TO EXISTING COMPETENCIES

#### → [competency-name] (Confidence: HIGH)
Prompts:
1. [prompt-filename] - [brief reason for mapping]
2. [prompt-filename] - [brief reason for mapping]

#### → [competency-name] (Confidence: MEDIUM)
Prompts:
1. [prompt-filename] - [brief reason for mapping]

### 🆕 CREATE NEW COMPETENCY

#### Suggested Name: [new-competency-name]
Rationale: [why new competency is needed]
Prompts to include:
1. [prompt-filename] - [core functionality]
2. [prompt-filename] - [complementary functionality]

Classification: [kernel/common/plugin]
Primary Users: [role1, role2]

### 🔀 HYBRID DISTRIBUTION

#### Prompt: [prompt-filename]
This prompt spans multiple concerns:
- Part A → [competency-1]: [what goes here]
- Part B → [competency-2]: [what goes here]

Recommendation: [split into 2 prompts OR choose primary competency]

## Competency Collections Impact:

### Collections Affected:
- [collection-name]: Add [N] new prompts from existing competencies
- [collection-name]: New competency [competency-name] should be added

### New Competencies Requiring Collection Assignment:
1. [new-competency-name] → Suggested collections: [collection1, collection2]
```

### 4. User Decision Phase

**Present Mapping Report:**
You WILL execute:
- Display complete mapping report to user
- Highlight areas needing user decision:
  - Confirm/modify existing competency mappings
  - Approve/reject new competency creation
  - Decide on hybrid prompt handling (split vs primary)
  - Select classification for new competencies
- Request user feedback and modifications

**Capture User Decisions:**
You WILL record:
- Final mapping assignments for each prompt
- New competency names and structures approved
- Hybrid prompt resolution decisions
- Classification assignments
- Collection preferences

### 5. Carry-Over Creation Phase

**Generate Carry-Over Document:**
You WILL create carry-over using `[id:ack_dir]competencies/common/prompts/carry-over-session.md`:

Execute carry-over creation with this context:
```
CARRY-OVER NOTE - [timestamp]
================================

## Session Summary:
Analyzed [N] external prompts from [source_path] and generated competency mapping recommendations. User reviewed and approved mapping plan for conversion.

## Repository State:
- Branch: [current_branch]
- No files modified (analysis phase only)
- Mapping report generated in memory

## IMMEDIATE NEXT ACTION (Priority 1):
Execute deploy-imported-prompts workflow to convert and integrate approved prompts into OLAF competencies.
- Why: User approved mapping plan, ready for implementation
- Expected outcome: All [N] prompts converted to OLAF format and deployed to target competencies
- Time estimate: 45-60 minutes

## STRATEGIC ROADMAP (Sessions 2-5):
1. Session 2: Convert and deploy all prompts (deploy-imported-prompts workflow)
2. Session 3: Update competency manifests and validate deployments
3. Session 4: Test converted prompts in target competencies
4. Session 5: Update collection configuration (add new competencies or reinit)

## Key Files Modified:
None (analysis phase only)

## Context Dependencies:

### Prompt Inventory ([N] prompts):
[Include concise list of all prompts with paths]

### Final Mapping Decisions:
[Include complete approved mapping report]

### New Competencies to Create:
[List new competency names, structures, classifications]

### Collection Actions Required:
[List collection updates needed after deployment]

## Session Resumption Notes:
⚠️ **CRITICAL**: Next session MUST:
1. Close all open editor files before proceeding
2. Load this carry-over using carry-on-session workflow
3. Execute deploy-imported-prompts workflow immediately
4. Reference mapping report for conversion decisions

## Success Metrics:
- All [N] prompts converted to OLAF format
- All prompts deployed to correct competency folders
- All manifests updated with new entry points
- Collection recommendations documented
- Zero prompts left unmapped

## Carry-Over History:
New workflow - no previous carry-overs
```

**Save Carry-Over File:**
You WILL execute:
- Save carry-over to `carry-overs/carry-over-[timestamp].txt` (workspace root level)
- Confirm file creation with full path
- Display carry-over summary to user

### 6. Validation Phase
You WILL validate results:
- Confirm all prompts were analyzed
- Verify mapping report is complete and comprehensive
- Ensure user decisions are captured accurately
- Validate carry-over file was created successfully
- Check all required context is preserved for next session

## Output Format
You WILL generate outputs following this structure:
- Prompt Inventory: Structured analysis of all discovered prompts
- Competency Mapping Report: Detailed recommendations with confidence scores
- User Decision Record: Captured approvals and modifications
- Carry-Over File: Complete context for resumption in `carry-overs/carry-over-[timestamp].txt`

## User Communication

### Progress Updates
- Confirmation when prompt discovery completes: "Found [N] prompts"
- Status when analysis phase completes: "Analyzed all prompts"
- Notification when mapping report is ready for review
- Confirmation when user decisions are captured
- Success message when carry-over file is created

### Completion Summary
- Total prompts analyzed: [N]
- Existing competency mappings: [M]
- New competencies needed: [P]
- Carry-over file location: `carry-overs/carry-over-[timestamp].txt`
- Next session instruction: "Start new session and execute carry-on workflow"

### Next Steps (Mandatory)
You WILL clearly define:
- **Immediate Action**: User must end this session and start new session
- **Session Resumption**: Load carry-over using carry-on-session workflow
- **Next Workflow**: Execute deploy-imported-prompts to implement approved plan
- **Expected Duration**: 45-60 minutes for conversion and deployment
- **Dependencies**: Carry-over file must be accessible in new session

## Domain-Specific Rules
You MUST follow these constraints:
- **Analysis Only**: This workflow does NOT modify any OLAF files or competencies
- **No Automatic Deployment**: Conversion and deployment happens in separate session
- **User Approval Required**: Mapping recommendations require explicit user review and approval
- **Carry-Over Mandatory**: Session MUST end with carry-over creation
- **Comprehensive Context**: Carry-over must capture all decisions and mapping details
- **Collection Impact**: Document but do NOT execute collection updates

## Success Criteria
You WILL consider the task complete when:
- [ ] All source prompts discovered and inventoried
- [ ] Each prompt analyzed for domain, purpose, and triggers
- [ ] Mapping recommendations generated with confidence scores
- [ ] User reviewed and approved mapping plan
- [ ] All user decisions captured accurately
- [ ] Carry-over file created with complete context
- [ ] User instructed to start new session for deployment

## Required Actions
1. Discover and inventory all prompts in source location
2. Analyze each prompt for OLAF competency mapping
3. Generate comprehensive mapping report with recommendations
4. Present report to user and capture decisions
5. Create carry-over file with complete context
6. Instruct user to start new session for deployment phase

## Error Handling
You WILL handle these scenarios:
- **Source Path Invalid**: Verify path and request correction from user
- **No Prompts Found**: Check file_pattern and scan_recursive settings
- **Ambiguous Mapping**: Flag for user decision, provide multiple options
- **Incomplete User Decisions**: Re-present options and request clear approval
- **Carry-Over Creation Failed**: Retry with alternative path or notify user

⚠️ **Critical Requirements**
- MANDATORY: Follow Propose-Confirm-Act protocol throughout
- NEVER proceed to conversion/deployment in this session
- ALWAYS create carry-over before ending session
- ALWAYS capture complete user decisions for next session
- ALWAYS document collection impact without executing changes
- NEVER modify competency index or collection configuration
- ALWAYS provide clear next steps for session resumption
