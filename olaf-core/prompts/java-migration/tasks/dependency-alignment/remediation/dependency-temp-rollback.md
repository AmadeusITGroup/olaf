---
key: dependency-temp-rollback
triggers:
  - regex: 'rollback applied'
severity: low
priority: 4
---
## Problem
Upgrade reverted pending fix.
## Recommended Actions
1. Document reason & target reattempt date.
2. Monitor upstream issue.
3. Re-test periodically.
## Validation
Re-upgrade succeeds later.
## Rollback
N/A (already rolled back).
