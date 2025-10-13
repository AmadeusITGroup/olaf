---
key: switch-fallthrough-change
triggers:
  - regex: 'behavior change after switch expression'
severity: medium
priority: 3
---
## Problem
Enhanced switch altered legacy fall-through logic.
## Recommended Actions
1. Recreate combined cases with multi-label or explicit code block.
2. Add regression test.
## Validation
Behavior matches pre-refactor.
## Rollback
Return to old switch until safe rewrite.
