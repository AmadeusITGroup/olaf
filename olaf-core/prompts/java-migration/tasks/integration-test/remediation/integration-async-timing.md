---
key: integration-async-timing
triggers:
  - regex: 'timeout|Awaitility timeout'
severity: low
priority: 4
---
## Problem
Async test timing flakiness.
## Recommended Actions
1. Increase await timeout moderately.
2. Poll with backoff; avoid fixed sleeps.
3. Optimize underlying async scheduling.
## Validation
Test passes consistently (3 consecutive runs).
## Rollback
Restore prior timeout if performance impacted.
