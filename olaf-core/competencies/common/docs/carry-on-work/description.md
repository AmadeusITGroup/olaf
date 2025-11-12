# Carry-On Work

## Overview

Resumes work from a previous session by loading carry-over notes, restoring context, and continuing where you left off.

## Purpose

Maintains continuity across agent sessions by automatically loading the most recent carry-over file, eliminating the need to re-explain context and allowing seamless work resumption.

## Usage

**Command**: `carry on`

**Protocol**: Act

**When to Use**: At the start of a new session when you want to continue work from a previous session that created carry-over notes.

## Parameters

### Required Inputs
None - automatically finds and loads the most recent carry-over file

### Optional Inputs
- **Specific Date/Time**: Can specify which carry-over to load if not using the most recent

### Context Requirements
- Must have previously created carry-over notes using `create carry-over`
- Carry-over files must exist in the `carry-overs/` directory

## Output

**Deliverables**:
- Restored session context
- Summary of previous session
- Identification of next steps
- Ready-to-continue work state

**Format**: Conversational summary with context restoration

## Examples

### Example 1: Resume After Overnight Break

**Scenario**: Starting work the next day after creating carry-over notes

**Command**:
```
carry on
```

**Result**: OLAF loads yesterday's carry-over, summarizes what was accomplished, and identifies the next tasks to tackle

### Example 2: Resume After Context Switch

**Scenario**: Returning to a project after working on something else

**Command**:
```
carry on
```

**Result**: Previous project context restored, ready to continue without re-explaining the situation

## Related Competencies

- **create-carry-over**: Use this to create carry-over notes before ending a session
- **stash-work**: Alternative for temporarily pausing work with more detailed state capture
- **stash-restart**: Resume from stashed work instead of carry-over notes

## Tips & Best Practices

- Always create carry-over notes before ending important work sessions
- Carry-over files are timestamped - most recent is loaded by default
- Keep carry-over notes concise but complete for best resumption
- Use carry-over for session-to-session continuity, stashing for task switching

## Limitations

- Requires carry-over file to exist from previous session
- Cannot restore exact conversation state, only context and progress
- Works best when carry-over notes are well-structured
