---
key: config-property-rename
triggers:
  - regex: 'Failed to bind properties'
  - regex: 'Could not bind'
severity: high
priority: 1
---
## Problem
Configuration property names changed or deprecated between Boot 2.3 and 2.4 causing binding failures.
## Recommended Actions
1. Check Boot 2.4 migration notes for renamed properties.
2. Update `application*.yml` / `.properties` to new keys; remove deprecated ones.
3. If custom @ConfigurationProperties class changed, recompile after adjusting field names / @ConstructorBinding.
## Validation
Re-run tests: no binding failure stack traces.
## Rollback
Restore previous property keys if critical runtime failures; re-attempt after more analysis.
