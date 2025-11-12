````markdown
`````markdown
---
name: switch-context
description: IDE-aware context switching with automatic repository discovery and transitive loading
tags: [context, switching, ide, discovery, transitive, repository]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
**HIERARCHY**: Framework principles OVERRIDE competency specifications:
- <olaf-general-role-and-behavior> - Be concise, no elaboration
- <olaf-core-principles> - Mandatory rules supersede competency details
- <olaf-interaction-protocols> - Protocol only, not verbosity
You MUST strictly apply <olaf-framework-validation>.

## Output Constraints
**CONCISENESS MANDATORY**: Apply framework's "Be concise. Use as few words as possible."
- Status updates: Single line max
- Results: Essential info only  
- No formatting, alerts, or lengthy explanations
- Framework conciseness overrides all output format specifications below

## Input Parameters

## Role
Context Manager - Switch between different contexts dynamically.

## Objective
Enable users to switch between different contexts by copying context templates to the active context-current.md file.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **context_name**: string - Name of context to switch to (OPTIONAL - auto-discovery if omitted)
- **repo_path**: string - Path to scan for IDE steering files (OPTIONAL - defaults to your-repos/)
- **format**: string - Output format preference (OPTIONAL - defaults to "list")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act for context discovery and listing (non-destructive analysis)
- You WILL use Propose-Act before switching contexts (requires user confirmation of selection)

## Workflow

### 1. List Available Contexts (Primary Step)
- **ALWAYS START HERE**: Check `olaf-data/context/` directory for all context-*.md files first
- Display available contexts (files matching pattern: context-*.md) 
- Show current active context if exists
- Present numbered list to user for selection
- **ONLY if user requests "discover"**: Proceed to auto-discovery (Step 2)

### 2. IDE-Aware Auto-Discovery (Optional - Only on User Request)
When user specifically requests auto-discovery ("discover", "scan repositories"):

**Phase 2a: Detect Current IDE Tool**
- Determine which IDE tool is active: GitHub Copilot, Windsurf, or Kiro
- Detection based on file being edited or user environment context

**Phase 2b: Scan Repository for IDE Steering Files**
- Scan `your-repos/` (and sibling repo folders) for IDE-specific steering documents
- Look for:
  - `.github/copilot-instructions.md` (GitHub Copilot)
  - `.windsurf/rules/*.md` (Windsurf - always-on rules)  
  - `.kiro/steering/*.md` (Kiro steering documents)
- Extract repository names from folder structure
- **CRITICAL**: Only proceed if at least ONE steering file is found. Do NOT invent contexts for repos without steering files.

**Phase 2c: Generate Dynamic Context Files (Only if Steering Files Found)**
- For each discovered repo WITH steering files:
  - Create context file named: `context-{repo-name}.md`
  - Content: Lists the IDE steering documents actually found for that repo
  - Template: Use Context File Template (see Implementation Details)
  - Include only the files that were actually detected
- Store generated contexts in `olaf-data/projects/`
- Do NOT create context files for repos without steering files

**Phase 2d: Present Updated Selection**
- List both pre-existing and auto-discovered contexts with descriptions
- Present numbered list to user
- Wait for user selection by number or name
- Proceed with selected context

### 3. Switch Context
When user specifies a context name (or selects from list):
- Validate the requested context template exists: `olaf-data/context/context-{name}.md`
- Use shell to copy template to active context: copy `olaf-data/context/context-{name}.md` `olaf-data/context/context-current.md`
- Confirm the switch was successful
- **CRITICAL**: Clearly inform user that they MUST start a new session/conversation for the new context to be loaded and take effect
- Provide explicit instruction: "⚠️ **IMPORTANT**: Please start a new conversation for the '{context_name}' context to be active. The context change will only take effect in a fresh session."

### 4. Clear Context
If user wants to remove context:
- Delete `olaf-data/context/context-current.md` if it exists
- Confirm context has been cleared
- **CRITICAL**: Inform user that they MUST start a new session for the context clearing to take effect
- Provide explicit instruction: "⚠️ **IMPORTANT**: Please start a new conversation for the context clearing to be active."

## Commands Handled
- "context switch {name}" - Switch to specific context
- "context switch" or "context list" - List existing contexts in olaf-data/context/ directory
- "context discover" or "context scan" - Manually trigger repository scanning and context generation (optional)
- "context clear" - Remove current context
- "context status" - Show current active context and available IDE-linked contexts

## Output Format
You WILL generate outputs in the following formats based on user request:

**List Format (Default):**
```
Available contexts:
1. default - [description]
2. springboot-hexagonal - [description]
3. your-app - [IDE-Linked] (auto-discovered)

Select a context by number or name:
```

**Detailed Format:**
- Full context metadata and file paths
- IDE steering documents for each context
- Current active context status
- Suggested next actions

**Status Format:**
- Current active context
- Number of available contexts
- Number of IDE-linked contexts
- Last discovery timestamp

- **Status Format**: Show current active context status and available contexts

## User Communication
You WILL provide clear communication throughout the workflow:

### Progress Updates
- Confirmation when repository scanning starts
- Status of IDE steering file detection
- Number of contexts found and available
- Clear indication of IDE-linked vs pre-existing contexts
- Completion with summary statistics

### Results Presentation
- **Discovery Results**: List all found contexts with descriptions
- **Current Status**: Display active context and last update time
- **Available Options**: Numbered list with selection prompt
- **IDE Metadata**: Show which IDE tools are configured for each context

### Session Transition Guidance
- **Critical Alert**: "⚠️ **IMPORTANT**: Please start a new conversation for the context to be active"
- **Reason Explanation**: "Context changes take effect only in fresh sessions"
- **User Action**: Clear instruction for starting new conversation
- **Timeline**: Immediate effect after new session begins

## File Operations
- Source templates: olaf-data/context/context-*.md
- Active context: olaf-data/context/context-current.md
- List directory: olaf-data/projects/

## Success Criteria
- User can seamlessly switch between pre-existing and IDE-linked contexts
- Auto-discovery only creates context files for repos WITH steering files
- Context names match repository names for clarity
- Context files list ONLY the steering files that were actually detected
- IDE-linked contexts are marked and distinguished from pre-existing contexts
- No empty/invented contexts are created without user explicit request
- Numbered list selection for easy context choosing
- Context-specific instructions are loaded automatically in new sessions
- Transitive pattern works: IDE → Steering Files Found → Context Generated (conditional)
- **Clear and prominent notification** that users must start a new session for context changes to take effect
- Clear feedback on available contexts and current status
- Robust error handling for missing files or repositories
- Generated context files include IDE metadata and only references files that exist

## Implementation Details

### IDE Tool Detection
- GitHub Copilot: Detect from file path patterns (`.github/copilot-instructions.md` context)
- Windsurf: Detect from `.windsurf/` directory structure
- Kiro: Detect from `.kiro/` directory structure
- Store detected IDE in context metadata for transitive lookups

### Repository Scanning Process
1. Scan directory structure within `your-repos/` parent folder
2. For each subdirectory, check for IDE steering files:
   - `.github/copilot-instructions.md`
   - `.windsurf/rules/` (list all *.md files)
   - `.kiro/steering/` (list all *.md files)
3. Extract repo name from folder path
4. Record discovered steering files and their paths

### Context File Template
Generate dynamic context files ONLY for repos with steering files. Include only the files that were actually detected:

```markdown
# Project Context - {repo-name}

## IDE Configuration
- **IDE**: [GitHub Copilot | Windsurf | Kiro]
- **Repository**: {repo-name}
- **Auto-Generated**: Yes (IDE-Aware Context)

## Steering Documents
This context loads the following IDE-specific steering documents found in the repository:

{only list IDE configurations that were found - omit empty sections}

### {IDE} Configuration Files
{list each steering file path relative to repo root}

## Usage
Switch to this context to load all {repo-name} steering documents for {IDE}.

When switched, the framework will load:
1. All listed steering documents
2. Apply {IDE}-specific configurations
3. Initialize {repo-name}-specific context

## Metadata
- **Context Type**: IDE-Linked (Auto-Discovered)
- **Repository Path**: your-repos/{repo-name}/
- **Last Updated**: {timestamp}
- **Steering Files Detected**: {count}
```

### Conditional Context Creation
- **IF** steering files found: Generate context file with detected files
- **IF** NO steering files found: 
  - Do NOT create context file automatically
  - User can manually request: "create empty context for {repo-name}" to populate later
  - Model can then offer to create empty template for user to fill in

### Standard Context Listing Process (Default)
1. **Primary Step**: Use `listDirectory` tool on `olaf-data/context` to find all existing context-*.md files
2. Extract context names: remove "context-" prefix and ".md" suffix  
3. For each context, use `readFile` tool to read first 3-5 lines for description
4. Present formatted numbered list:
   ```
   Available contexts:
   1. default - [description]
   2. springboot-hexagonal - [description]
   
   Select a context by number or name, or type "discover" to scan repositories:
   ```
5. Parse user selection (accept both number and name)
6. If user selects "discover", proceed to Auto-Discovery Process below
7. Otherwise, proceed with context switch using selected context name

### Auto-Discovery Process (Optional - Only When User Requests)
1. Use `listDirectory` tool on `your-repos` to find all repositories
2. For each repository, scan for IDE steering files:
   - `.github/copilot-instructions.md`
   - `.windsurf/rules/*.md`
   - `.kiro/steering/*.md`
3. **Filter by utility**: Only proceed with repos that have at least ONE steering file
4. For repos WITH steering files:
   - Generate context file: `context-{repo-name}.md` using Context File Template
   - Write generated file to `olaf-data/projects/` with ONLY found files listed
   - Skip repos without any steering files (do not create empty contexts)
5. Use `listDirectory` tool on `olaf-data/context` to find all existing context-*.md files (pre-existing + newly generated)
6. Extract context names: remove "context-" prefix and ".md" suffix
7. For each context, use `readFile` tool to read first 3-5 lines for description
8. Present formatted numbered list:
   ```
   Available contexts:
   1. default - [description]
   2. springboot-hexagonal - [description]
   3. your-app - [IDE-Linked] (auto-discovered)
   
   Select a context by number or name:
   ```
9. Parse user selection (accept both number and name)
10. Proceed with context switch using selected context name

### Validation Rules
- **DO NOT create** context files for repos without steering files
- **DO create** context files only when steering files are found
- **DO list** only the IDE configurations that were actually detected
- **DO update** existing context files when new steering files are discovered
- **IF** user requests empty template: Can create one for manual population

### File Reading for Descriptions
- Read first few lines of each context-*.md file
- Look for markdown headers, comments, or first paragraph as description
- For auto-discovered contexts, mark as [IDE-Linked] in description
- Fallback to "No description available" if content is minimal
- Truncate long descriptions to keep list readable

### Transitive Pattern Implementation
- IDE tool determines which steering files exist
- Steering files determine what context gets generated
- Context name matches repo name
- Switching context chains to IDE-specific configurations automatically

## Error Handling
- Handle missing context templates gracefully
- Provide clear error messages for invalid context names and selections
- Validate file operations before execution
- Handle empty projects directory
- Validate user selection is within range for numbered choices

````
