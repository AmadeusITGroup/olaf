---
key: rewrite-config-missing
triggers:
  - regex: '(rewrite.yml).*not found'
severity: medium
priority: 3
---

## Problem
`rewrite.yml` absent from repository causing inconsistent recipe management.

## Recommended Actions
1. Create minimal `rewrite.yml` with comment header.
2. Add to version control.
3. Re-run dry run to ensure no changes produced.

## Validation
- File present and tracked.
- Dry run outputs zero changes.

## Rollback
Delete file only if adoption abandoned (not recommended).
