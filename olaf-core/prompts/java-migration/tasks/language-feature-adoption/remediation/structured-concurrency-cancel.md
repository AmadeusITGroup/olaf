---
key: structured-concurrency-cancel
triggers:
  - regex: 'CancellationException'
severity: medium
priority: 2
---
## Problem
StructuredTaskScope cancellation mishandled.
## Recommended Actions
1. Review scope shutdown policy.
2. Handle exceptions from subtasks explicitly.
3. Add tests for cancellation paths.
## Validation
Predictable completion & cancellation.
## Rollback
Fallback to previous Future-based implementation.
