# Context Switch Competency

## Role
Context Manager - Switch between different contexts dynamically.

## Objective
Enable users to switch between different contexts by copying context templates to the active context-current.md file.

## Workflow

### 1. Auto-Discovery and Selection
When user doesn't specify a context name:
- Use a tool to scan olaf-data/projects/ for context-*.md files
- Extract context names by removing "context-" prefix and ".md" suffix
- Read the first few lines of each context file to get a brief description
- Present numbered list of available contexts with descriptions
- Wait for user to select by number or name
- Proceed with selected context

### 2. List Available Contexts
- Check olaf-data/projects/ directory for available context templates
- Display available contexts (files matching pattern: context-*.md)
- Show current active context if exists

### 3. Switch Context
When user specifies a context name (or selects from list):
- Validate the requested context template exists: olaf-data/projects/context-{name}.md
- Use shell to copy template to active context: copy olaf-data/projects/context-{name}.md olaf-data/projects/context-current.md
- Confirm the switch was successful
- **CRITICAL**: Clearly inform user that they MUST start a new session/conversation for the new context to be loaded and take effect
- Provide explicit instruction: "⚠️ **IMPORTANT**: Please start a new conversation for the '{context_name}' context to be active. The context change will only take effect in a fresh session."

### 4. Clear Context
If user wants to remove context:
- Delete olaf-data/projects/context-current.md if it exists
- Confirm context has been cleared
- **CRITICAL**: Inform user that they MUST start a new session for the context clearing to take effect
- Provide explicit instruction: "⚠️ **IMPORTANT**: Please start a new conversation for the context clearing to be active."

## Commands Handled
- "context switch {name}" - Switch to specific context
- "context switch" or "context list" - Auto-discover and present numbered list of available contexts
- "context clear" - Remove current context
- "context status" - Show current active context

## File Operations
- Source templates: olaf-data/projects/context-*.md
- Active context: olaf-data/projects/context-current.md
- List directory: olaf-data/projects/

## Success Criteria
- User can seamlessly switch between different contexts
- Auto-discovery presents available contexts with descriptions when no context specified
- Numbered list selection for easy context choosing
- Context-specific instructions are loaded automatically in new sessions
- **Clear and prominent notification** that users must start a new session for context changes to take effect
- Clear feedback on available contexts and current status
- Robust error handling for missing templates

## Implementation Details

### Auto-Discovery Process
1. Use `listDirectory` tool on "olaf-data/projects" to find all files
2. Filter files matching pattern "context-*.md" (excluding "context-current.md")
3. Extract context names: remove "context-" prefix and ".md" suffix
4. For each context, use `readFile` tool to read first 3-5 lines for description
5. Present formatted numbered list:
   ```
   Available contexts:
   1. default - [description from file]
   2. monolith - [description from file]
   
   Select a context by number or name:
   ```
6. Parse user selection (accept both number and name)
7. Proceed with context switch using selected context name

### File Reading for Descriptions
- Read first few lines of each context-*.md file
- Look for markdown headers, comments, or first paragraph as description
- Fallback to "No description available" if content is minimal
- Truncate long descriptions to keep list readable

## Error Handling
- Handle missing context templates gracefully
- Provide clear error messages for invalid context names and selections
- Validate file operations before execution
- Handle empty projects directory
- Validate user selection is within range for numbered choices