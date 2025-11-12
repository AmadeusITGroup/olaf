# Stash Restart

## Overview

Resumes previously stashed work by loading stashed context and restoring work state.

## Purpose

Enables resumption of temporarily paused work by loading detailed stash files, allowing seamless continuation of tasks that were set aside.

## Usage

**Command**: `stash restart`

**Protocol**: Act

**When to Use**: When you want to resume work that was previously stashed using `stash work`.

## Parameters

### Required Inputs
None - will list available stashed work if not specified

### Optional Inputs
- **Stash Identifier**: Specific stash to resume (task name or timestamp)

### Context Requirements
- Must have previously stashed work using `stash work`
- Stash files must exist in `carry-overs/` directory

## Output

**Deliverables**:
- Restored work context
- Summary of stashed work
- Progress and state information
- Files and tasks involved
- Ready-to-continue work state

**Format**: Conversational summary with context restoration

## Examples

### Example 1: Resume Most Recent Stash

**Scenario**: Want to resume the most recently stashed work

**Command**:
```
stash restart
```

**Result**: Lists available stashed work, loads selected stash, restores context

### Example 2: Resume Specific Stash

**Scenario**: Have multiple stashed tasks, want specific one

**Command**:
```
stash restart feature-authentication
```

**Result**: Loads the authentication feature stash, restores that specific work context

### Example 3: List Stashed Work

**Scenario**: Want to see what work is stashed

**Command**:
```
stash restart
```

**Result**: Displays list of all stashed work with descriptions and timestamps

## Related Competencies

- **stash-work**: Use this to stash current work before switching tasks
- **carry-on-work**: Alternative for session-to-session continuity
- **create-carry-over**: Lighter-weight session notes vs detailed stashing

## Tips & Best Practices

- Review stashed work list to choose the right task
- Stash files include more detail than carry-over notes
- Use stashing for task switching, carry-over for session continuity
- Clean up old stashes periodically
- Name stashes descriptively when creating them

## Limitations

- Requires stash file to exist from previous `stash work`
- Cannot restore exact code state, only context
- Stash files are local - not synced across machines
- Works best when stash notes are detailed
