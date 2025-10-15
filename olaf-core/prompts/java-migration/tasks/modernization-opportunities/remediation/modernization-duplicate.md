---
key: modernization-duplicate
triggers:
  - regex: 'duplicate candidate'
severity: low
priority: 6
---
## Problem
Duplicate modernization catalog entry.
## Recommended Actions
1. Merge details into single item.
2. Remove duplicate row; adjust references.
## Validation
Catalog has unique IDs.
## Rollback
Restore entry if removal mistaken.
