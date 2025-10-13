---
key: servlet-filter-registration
triggers:
  - regex: 'Filter.*not invoked'
severity: medium
priority: 3
---
## Problem
Filter not executing post migration.
## Recommended Actions
1. Confirm @Component or registration bean.
2. Check order; add @Order if needed.
3. Validate URL pattern coverage.
## Validation
Filter logic observed in logs/tests.
## Rollback
Restore prior registration approach.
