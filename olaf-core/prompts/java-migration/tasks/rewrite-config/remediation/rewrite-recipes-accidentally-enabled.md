---
key: rewrite-recipes-accidentally-enabled
triggers:
  - regex: '(Applying|Running) recipe'
severity: low
priority: 4
---

## Problem
Recipes unintentionally active causing noisy diffs.

## Recommended Actions
1. Remove `<activeRecipes>` / disable recipes in build script.
2. Comment out recipe entries in `rewrite.yml`.
3. Re-run dry run to confirm zero proposed changes.

## Validation
- Patch file empty.

## Rollback
If rollback needed, revert recipe list commit.
