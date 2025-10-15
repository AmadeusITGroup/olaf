---
key: actuator-custom-indicator-failure
triggers:
  - regex: 'Failed to instantiate.*HealthIndicator'
severity: medium
priority: 3
---
## Problem
Custom health indicator broken by API/config change.
## Recommended Actions
1. Review constructor/autowiring changes.
2. Update deprecated types; recompile.
3. Hit /actuator/health component section.
## Validation
Indicator status present and accurate.
## Rollback
Revert indicator change if blocking readiness.
