---
key: missing-jupiter-engine
triggers:
  - regex: 'No tests were found'
  - regex: 'Failed to resolve parameterized test'
severity: medium
priority: 1
---

## Problem
JUnit 5 API present but engine dependency (junit-jupiter-engine) missing; tests not discovered.

## Recommended Actions
1. Add dependency (Maven): `org.junit.jupiter:junit-jupiter-engine` (align version with BOM / Spring Boot parent).
2. Ensure surefire plugin version >= 3.0.0.
3. Re-run `mvn -q test`.

## Validation
Test run lists JUnit Platform with Jupiter tests executed.

## Rollback
Remove engine only if reverting entire migration.
