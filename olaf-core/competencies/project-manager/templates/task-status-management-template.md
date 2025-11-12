# Task Status Management System - TEMPLATE

This document defines the stateful task tracking system template used across Phase 4 micro-sessions to ensure each LLM session knows exactly what has been accomplished and what remains to be done.

## Task Status Values

### Status Definitions
- **TODO**: Task is ready to be executed (all dependencies satisfied)
- **IN_PROGRESS**: Task is currently being worked on by an active session
- **COMPLETED**: Task has been successfully completed and validated
- **FAILED**: Task attempted but failed validation (requires review/retry)
- **BLOCKED**: Task cannot start due to unmet dependencies

### Status Transitions
```
TODO → IN_PROGRESS → COMPLETED ✅
TODO → IN_PROGRESS → FAILED ❌ 
BLOCKED → TODO (when dependencies satisfied)
FAILED → TODO (after review/fix)
```

## Task Structure Template

Each task in the strategy document should follow this template structure:

```markdown
#### Task ID: TASK_XXX
- **Status**: [TODO|IN_PROGRESS|COMPLETED|FAILED|BLOCKED]
- **Priority**: [HIGH|MEDIUM|LOW] (Risk: X, Effort: Y)
- **Target**: `file/path:function/class` (CC: current)
- **Pattern**: [Switch-to-Strategy|God-Class|Deep-Nesting|Complex-Loops]
- **Goal**: [Specific transformation description] (CC: current → target)
- **Dependencies**: [List of TASK_IDs or "None"]
- **Estimated Effort**: [NUMBER] sessions
- **Sessions Used**: [ACTUAL] of [ESTIMATED] (updated during execution)
- **Success Criteria**: 
  - [Specific measurable criteria]
  - CC reduced to <X
  - All existing tests pass
  - New tests for extracted components
- **Validation Steps**:
  - Build using BUILD_INSTRUCTIONS.md
  - Test using TESTING_INSTRUCTIONS.md
  - Measure CC with complexity tools
- **Started**: [TIMESTAMP or null]
- **Completed**: [TIMESTAMP or null]
- **Notes**: [Progress notes, issues, recovery plans]
```

## Session Lock Management

### Lock Acquisition (Phase 4.1)
1. Find highest priority task with status "TODO" and satisfied dependencies
2. Check no other task has status "IN_PROGRESS" (prevents conflicts)
3. Update selected task: `status: TODO → IN_PROGRESS`
4. Record `started: [TIMESTAMP]`
5. Proceed with execution

### Lock Release (Phase 4.4)
1. Update task status based on validation results:
   - Success: `status: IN_PROGRESS → COMPLETED`, record `completed: [TIMESTAMP]`
   - Failure: `status: IN_PROGRESS → FAILED`, record failure details
   - Partial: keep `status: IN_PROGRESS`, update progress notes
2. Update dependency chain (unblock dependent tasks if completed)
3. Find next available task for handoff

## Dependency Management

### Dependency Resolution
```python
def can_start_task(task):
    if task.dependencies == ["None"]:
        return True
    
    for dep_task_id in task.dependencies:
        dep_task = get_task(dep_task_id)
        if dep_task.status != "COMPLETED":
            return False
    
    return True

def unblock_dependencies(completed_task_id):
    for task in all_tasks:
        if completed_task_id in task.dependencies:
            if can_start_task(task):
                task.status = "BLOCKED" → "TODO"
```

### Dependency Graph Example
```
TASK_001 (independent) → TASK_002 → TASK_005
TASK_003 (independent) → TASK_004
TASK_006 (independent)

Execution Order:
Wave 1: TASK_001, TASK_003, TASK_006 (parallel)
Wave 2: TASK_002, TASK_004 (after Wave 1)  
Wave 3: TASK_005 (after TASK_002)
```

## Progress Tracking

### Task Overview Dashboard
```markdown
## Task Status Overview
- **COMPLETED**: 5/12 tasks (42% complete)
- **IN_PROGRESS**: 0/12 tasks (clean handoff state)
- **TODO**: 4/12 tasks (ready for execution)
- **BLOCKED**: 3/12 tasks (waiting dependencies) 
- **FAILED**: 0/12 tasks

## Complexity Progress
- **Functions CC >15**: 7 remaining (started: 15)
- **Total CC Reduction**: 156 points (target: 200+ points)
- **Average CC Reduction**: 26 points per completed task
```

### Session Metrics
```markdown
## Session Efficiency
- **Estimated vs Actual Sessions**:
  - TASK_001: 2 estimated, 2 actual ✅
  - TASK_002: 3 estimated, 4 actual ⚠️ (+1 session)
  - TASK_003: 2 estimated, 1 actual ✅ (-1 session)
- **Total Sessions**: 12 actual vs 15 estimated (80% efficiency)
```

## Conflict Detection

### Session Conflicts
- **Multiple IN_PROGRESS**: Only one task should have IN_PROGRESS status
- **Dependency Violations**: Task marked TODO but dependencies not COMPLETED
- **Stale Sessions**: IN_PROGRESS task with old timestamp (session died)

### Conflict Resolution
```markdown
IF multiple_in_progress_tasks():
    ESCALATE_TO_HUMAN("Multiple sessions detected")

IF stale_in_progress_task(timeout=60_minutes):
    task.status = "IN_PROGRESS" → "TODO"  # Reset for retry
    task.notes += "Session timeout - reset for retry"

IF dependency_violation(task):
    task.status = "TODO" → "BLOCKED"
    LOG_ERROR("Dependency validation failed")
```

## Error Recovery

### Failed Task Recovery
```markdown
WHEN task.status == "FAILED":
    REVIEW failure_notes
    DETERMINE recovery_strategy:
        - Retry with same approach
        - Modify approach/pattern
        - Split into smaller tasks
        - Escalate to human
    UPDATE task.status = "FAILED" → "TODO"
    SCHEDULE for retry
```

### Session Recovery
```markdown
WHEN session_interrupted():
    SAVE partial_progress to task.notes
    KEEP task.status = "IN_PROGRESS" 
    ENABLE resume_from_checkpoint in next session
```

This stateful system ensures each micro-session has perfect context about what has been accomplished and what needs to be done next, enabling truly autonomous refactoring with proper progress tracking.
