---
key: rewrite-format-churn
triggers:
  - regex: '(reformat|import order)'
severity: low
priority: 5
---

## Problem
Formatting-only diffs clutter review before policy adoption.

## Recommended Actions
1. Disable style/format recipes until approved.
2. Re-run dry run verifying no formatting diffs.
3. Schedule separate formatting commit.

## Validation
No style changes present in patch.

## Rollback
Revert formatting commit if prematurely merged.
