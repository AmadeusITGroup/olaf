---
key: reactive-timing-adjustment
triggers:
  - regex: 'StepVerifier'
  - regex: 'timeout while waiting'
severity: medium
priority: 2
---
## Problem
Reactive tests fail due to timing/operator behavior shifts after dependency upgrades in 2.5.x.
## Recommended Actions
1. Review StepVerifier expectations; increase await durations minimally.
2. Avoid Thread.sleep; use virtual time where appropriate.
3. Ensure scheduler configuration unchanged inadvertently.
## Validation
Reactive tests pass consistently without arbitrary large sleeps.
## Rollback
Revert specific dependency causing change if deterministically identified and migration not blocked.
