---
key: leftover-vintage-engine
triggers:
  - regex: 'org.junit.vintage.engine'
severity: low
priority: 2
---

## Problem
Vintage engine still on classpath after majority of tests migrated; slows test startup and hides missing conversions.

## Recommended Actions
1. Remove `junit-vintage-engine` dependency.
2. Re-run tests; convert any newly failing JUnit 4 tests instead of re-adding vintage.
3. If critical legacy tests remain, mark DEFERRED with removal deadline.

## Validation
No vintage engine mention in test startup logs.

## Rollback
Re-add vintage temporarily if urgent production fix requires postponing remaining migrations.
