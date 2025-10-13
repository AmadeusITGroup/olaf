---
key: reflective-access-warning
triggers:
  - regex: 'WARNING: An illegal reflective access operation has occurred'
severity: low
priority: 5
---

## Problem
Illegal reflective access warnings appear under JDK 17; not immediately breaking but indicate future risk.

## Recommended Actions
1. Identify library causing warning (stack trace first line after warning).
2. Upgrade library to a version that removes reflection hack, if available.
3. Avoid adding broad `--add-opens` unless necessary; prefer targeted upgrade.
4. If no fix exists, document and defer.

## Validation
Warnings reduced or isolated to known libraries with documented deferral.

## Rollback
Not needed; warnings are non-blocking; track for later remediation.
