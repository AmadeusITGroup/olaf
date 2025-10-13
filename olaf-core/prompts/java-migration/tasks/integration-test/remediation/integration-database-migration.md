---
key: integration-database-migration
triggers:
  - regex: '(Flyway|Liquibase).*(error|failed)'
severity: medium
priority: 3
---
## Problem
Schema migration fails during tests.
## Recommended Actions
1. Inspect changelog checksum / ordering.
2. Fix incompatible SQL for new DB version.
3. Re-run migrations clean schema.
## Validation
Migrations apply; tests proceed.
## Rollback
Revert last migration script; create fix script.
