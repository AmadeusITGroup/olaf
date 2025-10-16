# Context Switch Competency

## Role
Context Manager - Switch between different contexts dynamically.

## Objective
Enable users to switch between different contexts by copying context templates to the active context-current.md file.

## Workflow

### 1. Auto-Discovery and Selection (Default Behavior)
**ALWAYS start with auto-discovery when user requests context switch:**
1. **Scan for available contexts**: Use `listDirectory` tool on "olaf-data/projects"
2. **Filter context files**: Find all files matching pattern "context-*.md" (exclude "context-current.md")
3. **Extract context names**: Remove "context-" prefix and ".md" suffix from filenames
4. **Read descriptions**: Use `readFile` tool to read first 5 lines of each context file for description
5. **Present numbered list**: Show available contexts with descriptions and current active context
6. **Handle user selection**: Accept either number or context name
7. **Proceed with switch**: Use selected context for the switch operation

### 2. Context Discovery Implementation
```
Available project contexts:

Current: [current-context-name] (if any)

1. default - [First line or title from context-default.md]
2. monolith - Spring Boot application using Spring Modulith with Hexagonal Architecture
3. springboot-hexagonal - Spring Boot Hexagonal Architecture with DDD patterns

Select a context by number (1-3) or name (e.g., 'monolith'):
```

### 3. Switch Context Process
After user selection (number or name):
1. **Validate selection**: Ensure the context template exists
2. **Copy template**: Use `executePwsh` with copy command: `copy "olaf-data/projects/context-{name}.md" "olaf-data/projects/context-current.md"`
3. **Confirm success**: Verify the copy operation completed
4. **Critical notification**: Inform user they MUST start new session
5. **Provide instruction**: "⚠️ **IMPORTANT**: Please start a new conversation for the '{context_name}' context to be active. The context change will only take effect in a fresh session."

### 4. Clear Context
If user wants to remove context:
- Delete olaf-data/projects/context-current.md if it exists using `deleteFile` tool
- Confirm context has been cleared
- **CRITICAL**: Inform user that they MUST start a new session for the context clearing to take effect
- Provide explicit instruction: "⚠️ **IMPORTANT**: Please start a new conversation for the context clearing to be active."

## Commands Handled
- "context switch" - **PRIMARY**: Auto-discover and present numbered list of available contexts
- "context switch {name}" - Switch to specific context (still supported but auto-discovery runs first)
- "context list" - Same as "context switch" - show available contexts
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

### Auto-Discovery Process (MANDATORY FIRST STEP)
1. **Always start with discovery**: Use `listDirectory` tool on "olaf-data/projects" to find all files
2. **Filter context files**: Find files matching pattern "context-*.md" (exclude "context-current.md")
3. **Extract names**: Remove "context-" prefix and ".md" suffix from filenames
4. **Read descriptions**: Use `readFile` tool with `end_line=5` to read first 5 lines of each context file
5. **Identify current context**: Check if "context-current.md" exists and determine which template it matches
6. **Present formatted list**:
   ```
   Available project contexts:
   
   Current: [current-context-name] (or "None" if no active context)
   
   1. default - [First meaningful line from context-default.md]
   2. monolith - Spring Boot application using Spring Modulith with Hexagonal Architecture  
   3. springboot-hexagonal - Spring Boot Hexagonal Architecture with DDD patterns
   
   Select a context by number (1-3) or name (e.g., 'monolith'):
   ```
7. **Parse selection**: Accept both number (1, 2, 3) and context name ('default', 'monolith', etc.)
8. **Validate selection**: Ensure selected context exists before proceeding
9. **Execute switch**: Proceed with context switch using validated selection

### File Reading for Descriptions
- **Read strategy**: Use `readFile` with `end_line=5` to get first 5 lines of each context-*.md file
- **Description extraction**: Look for:
  1. First markdown header (# Title)
  2. First meaningful paragraph after headers
  3. Architecture overview or key description
- **Fallback handling**: Use "No description available" if file is empty or has no meaningful content
- **Length management**: Truncate descriptions to max 80 characters for list readability
- **Current context detection**: Compare content of context-current.md with templates to identify active context

## Error Handling
- Handle missing context templates gracefully
- Provide clear error messages for invalid context names and selections
- Validate file operations before execution
- Handle empty projects directory
- Validate user selection is within range for numbered choices