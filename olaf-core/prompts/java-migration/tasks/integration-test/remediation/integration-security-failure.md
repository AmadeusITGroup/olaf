---
key: integration-security-failure
triggers:
  - regex: '403 Forbidden|401 Unauthorized'
severity: medium
priority: 2
---
## Problem
Security expectations broken (unexpected 401/403/200).
## Recommended Actions
1. Verify test credentials & roles.
2. Adjust security config for actuator/api changes.
3. Update test to new access rules.
## Validation
Expected auth outcomes restored.
## Rollback
Revert security rule change if broad impact.
