---
key: validation-namespace-residual
triggers:
  - regex: 'import javax.validation'
severity: medium
priority: 2
---
## Problem
Leftover javax.validation imports.
## Recommended Actions
1. Replace with jakarta equivalents.
2. Adjust custom constraint packages.
3. Re-run compile.
## Validation
Zero javax.validation imports.
## Rollback
Revert file if functional regression emerges.
