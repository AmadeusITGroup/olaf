````markdown
# Delete Stash - Common Competency

## Purpose
Delete unwanted stash directories permanently to clean up the workspace.

## Context
- User wants to remove old or unnecessary stashes
- Need to provide safe deletion with confirmation
- Should show available stashes for selection

## Instructions

### 1. List Available Stashes
Show user current stashes for selection:
```bash
python olaf-core/competencies/common/tools/stash_manager.py list
```

### 2. Confirm Deletion Target
- Present numbered list of stashes
- Ask user to specify which stash to delete (by name or number)
- Warn about permanent deletion

### 3. Execute Deletion
Use the stash manager tool:
```bash
python olaf-core/competencies/common/tools/stash_manager.py delete <stash-name>
```

The tool will:
- Prompt user to type "DELETE" for confirmation
- Permanently remove the stash directory
- Provide success/failure feedback

### 4. Alternative: Force Delete (Advanced)
For automated scenarios (use with extreme caution):
```bash
python olaf-core/competencies/common/tools/stash_manager.py delete <stash-name> --yes
```

## Safety Features
- **⚠️ Confirmation Required**: User must type "DELETE" to proceed
- **🚫 Cannot Be Undone**: Clear warning about permanent action
- **📋 List First**: Always show available stashes before deletion
- **✅ Feedback**: Confirms successful deletion

## User Interaction Flow
1. **List stashes** - Show available options
2. **User selects** - Specify stash name to delete
3. **Confirmation** - Tool prompts for "DELETE" confirmation
4. **Deletion** - Stash permanently removed
5. **Verification** - Show updated stash list (optional)

## Output Format
- Present available stashes clearly
- Execute deletion command
- Confirm completion
- Optionally list remaining stashes

## Success Criteria
- ✅ User can see available stashes
- ✅ Deletion requires explicit confirmation
- ✅ Stash directory completely removed
- ✅ User gets clear feedback on operation result
````