---
key: dependency-jakarta-version-missing
triggers:
  - regex: 'ClassNotFoundException: jakarta\.'
  - regex: 'ClassNotFoundException: javax\.'
severity: high
priority: 2
---
## Problem
Required Jakarta artifact not on classpath or old javax artifact still pulled.
## Recommended Actions
1. Inspect dependency:tree for javax.* artifacts.
2. Replace with jakarta.* coordinates or newer version (e.g., jakarta.validation, jakarta.servlet is provided by Boot 3).
3. Exclude transitive javax artifacts from dependencies.
## Validation
No ClassNotFoundException for jakarta packages; no javax artifacts in tree.
## Rollback
Temporarily keep javax artifact only if critical and Boot 3 compatible (rare); document.
