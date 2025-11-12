# Create Carry-Over

## Overview

Creates concise session summary notes to enable seamless work continuation in future sessions.

## Purpose

Captures essential context, progress, and next steps from the current session into a timestamped file, allowing you to resume work later without losing context or having to re-explain everything.

## Usage

**Command**: `create carry-over`

**Protocol**: Act

**When to Use**: At the end of a work session when you want to preserve context for future continuation.

## Parameters

### Required Inputs
None - analyzes current session automatically

### Optional Inputs
- **Custom Notes**: Additional context or reminders to include
- **Next Steps**: Specific tasks to highlight for next session

### Context Requirements
- Active work session with meaningful progress or context to capture

## Output

**Deliverables**:
- Timestamped carry-over file in `carry-overs/` directory
- Filename format: `carry-over-YYYYMMDD-HHmm.txt`
- Structured summary with context, progress, and next steps

**Format**: Text file with sections for summary, context, decisions, and next steps

## Examples

### Example 1: End of Day Session

**Scenario**: Finishing work for the day on a feature implementation

**Command**:
```
create carry-over
```

**Result**: Creates `carry-over-20251027-1730.txt` with summary of feature progress, key decisions made, and next implementation steps

### Example 2: Before Context Switch

**Scenario**: Need to switch to urgent task but want to preserve current work context

**Command**:
```
create carry-over
```

**Result**: Session context saved, can resume later with `carry on` command

## Related Competencies

- **carry-on-work**: Use this to resume from carry-over notes
- **stash-work**: Alternative for more detailed work state capture with task-specific naming
- **context-switch**: Switch between different project contexts

## Tips & Best Practices

- Create carry-over notes at natural stopping points
- Include enough context for your future self to understand quickly
- Mention any blockers or open questions
- List specific next steps to make resumption easier
- Files are gitignored - your notes stay private

## Limitations

- Cannot capture exact conversation state
- Relies on current session having meaningful context
- Files are local only - not synced across machines
