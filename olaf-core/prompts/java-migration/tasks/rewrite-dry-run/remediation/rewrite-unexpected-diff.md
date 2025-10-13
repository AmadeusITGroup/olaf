---
key: rewrite-unexpected-diff
triggers:
  - regex: '(diff --git|rewrite.patch)'
severity: medium
priority: 2
---

## Problem
Dry run produced file changes while no recipes should be active.

## Recommended Actions
1. Confirm no active recipes in plugin or `rewrite.yml`.
2. Clear previous patch artifacts; re-run.
3. If persists, list internal default recipes triggered and disable.

## Validation
Patch file empty after rerun.

## Rollback
Revert stray recipe enabling commit.
