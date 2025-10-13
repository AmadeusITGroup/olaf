---
key: dependency-upgrade-required
triggers:
  - regex: 'ClassNotFoundException'
  - regex: 'NoClassDefFoundError'
  - regex: 'Unsupported major.minor version'
severity: high
priority: 2
---
## Problem
Missing or incompatible dependency after Boot 3 upgrade (class relocated or version too old).
## Recommended Actions
1. Identify artifact with dependency:tree.
2. Upgrade to Boot 3 compatible version or remove outdated transitive dep override.
3. Rebuild compile stage.
## Validation
No ClassNotFound / NoClassDefFoundError in latest compile.
## Rollback
Temporarily add explicit version override if newer dependency introduces regression; document for later cleanup.
