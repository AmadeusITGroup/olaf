---
key: actuator-metrics-misconfig
triggers:
  - regex: 'metrics.*(error|failed)'
severity: medium
priority: 2
---
## Problem
Metrics backend or scrape endpoint failing after Boot 3 changes.
## Recommended Actions
1. Verify management.metrics export settings.
2. Adjust endpoint exposure (prometheus) and security.
3. Confirm scrape returns 200 with expected metrics count.
## Validation
Metrics endpoint healthy; dashboard updates.
## Rollback
Restore previous config file version if metrics gap persists.
