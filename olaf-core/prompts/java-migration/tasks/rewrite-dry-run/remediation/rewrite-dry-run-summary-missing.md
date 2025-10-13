---
key: rewrite-dry-run-summary-missing
triggers:
  - regex: 'summary.*not found'
severity: low
priority: 6
---

## Problem
Expected dry run summary artifact absent.

## Recommended Actions
1. Generate summary markdown capturing timestamp, active recipes, file counts.
2. Store under findings migration directory.

## Validation
Summary file exists and tracked.

## Rollback
N/A.
