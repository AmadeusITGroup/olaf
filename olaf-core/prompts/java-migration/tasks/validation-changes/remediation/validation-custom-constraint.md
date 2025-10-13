---
key: validation-custom-constraint
triggers:
  - regex: 'ConstraintDeclarationException'
severity: medium
priority: 3
---
## Problem
Custom constraint annotation or validator broken.
## Recommended Actions
1. Update package & imports to jakarta.*.
2. Verify validator generic types unchanged.
3. Re-run affected tests.
## Validation
Constraint applies without exceptions.
## Rollback
Restore previous annotation/validator code.
