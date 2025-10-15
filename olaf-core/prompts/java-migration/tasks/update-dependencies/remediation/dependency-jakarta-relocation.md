---
key: dependency-jakarta-relocation
triggers:
  - regex: 'ClassNotFoundException: javax|package javax.* does not exist'
severity: medium
priority: 2
---
## Problem
Dependency still pulls javax variant; needs Jakarta relocation.
## Recommended Actions
1. Upgrade library to Jakarta-compatible release.
2. Exclude old transitive artifact.
3. Rebuild and grep for javax imports.
## Validation
No javax relocation errors.
## Rollback
Temporarily restore old version if critical regression.
