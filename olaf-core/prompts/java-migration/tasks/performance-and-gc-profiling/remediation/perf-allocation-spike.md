---
key: perf-allocation-spike
triggers:
  - regex: 'Allocation rate spike'
severity: medium
priority: 3
---
## Problem
Higher allocation rate causing GC pressure.
## Recommended Actions
1. Profile allocations (JFR events).
2. Refactor hot constructors or boxing.
3. Introduce object pooling only if justified.
## Validation
Allocation rate reduced; no new regressions.
## Rollback
Undo premature optimization if negligible gain.
