---
key: ci-target-mismatch
triggers:
  - regex: 'release version.*mismatch'
severity: medium
priority: 3
---
## Problem
Different target release used locally vs CI.
## Recommended Actions
1. Centralize release level in build config.
2. Ensure CI sets no overriding JAVA_TOOL_OPTIONS.
3. Re-run build verifying bytecode version.
## Validation
Consistent target across environments.
## Rollback
Revert recent target bump if early promotion premature.
