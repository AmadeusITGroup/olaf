---
key: jakarta-prep-inventory
triggers:
  - regex: 'import javax\.'
severity: low
priority: 3
---
## Problem
javax imports remain; need inventory before Jakarta migration.
## Recommended Actions
1. Count all javax imports; categorize (servlet, validation, persistence).
2. Store list under findings (e.g., javax-inventory-2.7.txt).
3. Plan rewrite tasks for Jakarta phase.
## Validation
Inventory file exists and matches grep counts.
## Rollback
Not applicable (informational).
