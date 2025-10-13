---
key: validation-constraint-change
triggers:
  - regex: 'import javax.validation'
  - regex: 'Constraint.* not found'
severity: medium
priority: 4
---
## Problem
Validation annotations / ConstraintValidator classes not updated to jakarta namespace.
## Recommended Actions
1. Change imports to `jakarta.validation.*`.
2. Update custom validators generics/annotations if moved.
3. Re-run unit tests focusing on validation logic.
## Validation
No javax.validation imports; validation tests pass.
## Rollback
Restore original import only if alternative annotation mismatch; then correct.
