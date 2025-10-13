---
key: namespace-rewrite-missing
triggers:
  - regex: 'package javax\.'
severity: medium
priority: 1
---
## Problem
Source still imports javax after automated rewrite.
## Recommended Actions
1. Manually replace `javax.` with `jakarta.` for equivalent APIs.
2. Re-import in IDE or run simplified search/replace restricted to import lines.
3. Rebuild to surface deeper API differences.
## Validation
No javax imports in affected file; compile passes for that unit.
## Rollback
Revert only if substitution caused unrelated error; refine change.
