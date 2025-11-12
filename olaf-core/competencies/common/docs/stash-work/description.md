# Stash Work

## Overview

Temporarily stashes current work with detailed state capture to enable task switching and later resumption.

## Purpose

Allows pausing current work to switch to a different task without losing context, progress, or state information. More detailed than carry-over notes, designed for task switching rather than session continuity.

## Usage

**Command**: `stash work`

**Protocol**: Act

**When to Use**: When you need to pause current work to switch to a different task and want to preserve detailed context for later resumption.

## Parameters

### Required Inputs
None - analyzes current work automatically

### Optional Inputs
- **Task Name**: Descriptive name for the stashed work
- **Custom Notes**: Additional context or reminders
- **Priority**: Urgency or importance level

### Context Requirements
- Active work session with meaningful progress to capture

## Output

**Deliverables**:
- Timestamped stash file in `carry-overs/` directory
- Filename format: `stashed-[task-name]-YYYYMMDD-HHmm.txt`
- Detailed work state with context, progress, files, and next steps

**Format**: Text file with structured sections for comprehensive state capture

## Examples

### Example 1: Urgent Task Interruption

**Scenario**: Working on feature when urgent bug needs attention

**Command**:
```
stash work
```

**Input**: "Stashing feature development to fix production bug"

**Result**: Creates `stashed-feature-development-20251027-1530.txt` with detailed state

### Example 2: End of Day with Multiple Tasks

**Scenario**: Multiple tasks in progress, need to stash all

**Command**:
```
stash work authentication feature
```

**Result**: Stashes authentication work separately from other tasks

### Example 3: Waiting on Dependency

**Scenario**: Blocked on external dependency, switching tasks

**Command**:
```
stash work
```

**Input**: "Blocked waiting for API spec, switching to frontend work"

**Result**: Stash includes blocker information for context when resuming

## Related Competencies

- **stash-restart**: Use this to resume stashed work
- **create-carry-over**: Lighter-weight alternative for session continuity
- **carry-on-work**: Resume from carry-over notes instead of stashes

## Tips & Best Practices

- Provide descriptive task names for easy identification later
- Include blocker information if waiting on something
- Use stashing for task switching, carry-over for session ends
- Can maintain multiple stashed tasks simultaneously
- Review and clean up old stashes periodically
- Files are gitignored - your stashes stay private

## Limitations

- Cannot capture exact code state, only context
- Requires meaningful work context to be useful
- Files are local only - not synced across machines
- Stash quality depends on current session context
