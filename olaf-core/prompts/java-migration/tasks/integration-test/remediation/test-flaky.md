---
key: test-flaky
triggers:
  - regex: 'flaky|intermittent'
severity: low
priority: 5
---
## Problem
Test exhibits intermittent pass/fail.
## Recommended Actions
1. Add retry annotation/logging to capture state.
2. Remove hidden dependencies (time/order).
3. Stabilize or quarantine test.
## Validation
Consistent pass across multiple runs.
## Rollback
Quarantine test class temporarily.
