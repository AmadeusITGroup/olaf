---
key: pattern-null-handling
triggers:
  - regex: 'NullPointerException.*pattern'
severity: medium
priority: 3
---
## Problem
Pattern matching refactor broke null guard.
## Recommended Actions
1. Reintroduce explicit null check before pattern.
2. Add test for null path.
## Validation
Null scenario passes without NPE.
## Rollback
Restore original instanceof + cast.
