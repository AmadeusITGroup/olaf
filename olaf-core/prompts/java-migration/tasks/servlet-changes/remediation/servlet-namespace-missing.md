---
key: servlet-namespace-missing
triggers:
  - regex: 'package javax.servlet does not exist'
severity: medium
priority: 2
---
## Problem
Legacy javax servlet imports lingering.
## Recommended Actions
1. Replace javax.* with jakarta.* imports.
2. Fix FQCN references.
3. Recompile module.
## Validation
Zero javax.servlet imports remain.
## Rollback
Revert specific file if behavior diff found.
