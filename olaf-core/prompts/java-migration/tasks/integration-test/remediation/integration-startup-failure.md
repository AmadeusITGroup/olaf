---
key: integration-startup-failure
triggers:
  - regex: 'Application failed to start'
severity: high
priority: 1
---
## Problem
App fails during integration test boot.
## Recommended Actions
1. Inspect root cause in logs.
2. Resolve config / bean wiring issue.
3. Re-run single failing module tests.
## Validation
Application context loads; tests proceed.
## Rollback
Revert latest change causing failure; log issue.
