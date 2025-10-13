---
key: record-behavior-change
triggers:
  - regex: 'equals.*changed|hashCode mismatch'
severity: medium
priority: 2
---
## Problem
Record conversion altered equality / serialization semantics.
## Recommended Actions
1. Verify previous equals/hashCode logic.
2. Add explicit methods if custom behavior required.
3. Update serialization tests.
## Validation
All equality/serialization tests pass.
## Rollback
Revert to class with manual methods.
