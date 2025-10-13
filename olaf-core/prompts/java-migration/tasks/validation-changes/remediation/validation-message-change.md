---
key: validation-message-change
triggers:
  - regex: 'expected:.*actual:'
severity: low
priority: 4
---
## Problem
Validation message text changed post migration.
## Recommended Actions
1. Update assertion expected messages or externalize message bundle.
2. Harmonize message keys across code/tests.
## Validation
Tests expecting messages pass.
## Rollback
Restore prior message bundle if user-facing regression.
