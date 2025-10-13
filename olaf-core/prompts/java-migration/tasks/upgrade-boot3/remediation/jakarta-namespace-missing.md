---
key: jakarta-namespace-missing
triggers:
  - regex: 'package javax\.'
  - regex: 'cannot find symbol'
severity: medium
priority: 1
---
## Problem
Compilation failures due to javax packages removed under Boot 3 (Jakarta EE 9+ requires jakarta.*).
## Recommended Actions
1. Defer actual code changes to jakarta-migration task.
2. Confirm counts match readiness inventory; flag unexpected new javax usages.
3. Prepare OpenRewrite / search-replace plan.
## Validation
All such errors categorized; no unrelated failures mixed in.
## Rollback
Not applicable (inventory stage).
