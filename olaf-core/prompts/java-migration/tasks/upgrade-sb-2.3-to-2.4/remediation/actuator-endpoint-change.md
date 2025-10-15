---
key: actuator-endpoint-change
triggers:
  - regex: '404 .*actuator'
  - regex: 'Endpoint .+ is disabled'
severity: medium
priority: 2
---
## Problem
Actuator endpoint availability changed after upgrade.
## Recommended Actions
1. Review management.endpoint.* and management.endpoints.web.exposure.include settings.
2. Add required endpoints explicitly if now excluded.
3. Confirm security configuration still permits access.
## Validation
Hit endpoint: returns expected JSON; no disabled warnings.
## Rollback
Revert endpoint exposure changes if unexpected data leakage.
