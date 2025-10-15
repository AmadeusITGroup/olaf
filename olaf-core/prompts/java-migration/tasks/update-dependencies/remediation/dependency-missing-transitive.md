---
key: dependency-missing-transitive
triggers:
  - regex: 'ClassNotFoundException|NoClassDefFoundError'
severity: medium
priority: 3
---
## Problem
Removed explicit version caused missing transitive dependency.
## Recommended Actions
1. Compare before/after dependency tree.
2. Add explicit dependency (no version if BOM covers).
3. Rebuild.
## Validation
Missing class loads; tests pass.
## Rollback
Restore prior dependency block; retry later.
