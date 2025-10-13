---
key: servlet-risk
triggers:
  - regex: 'import javax.servlet'
severity: medium
priority: 1
---
## Problem
Servlet API javax usage must migrate to jakarta.servlet under Boot 3.
## Recommended Actions
1. Count occurrences; list affected filters/controllers.
2. Plan OpenRewrite or manual rename in Jakarta phase.
3. Identify any container-specific APIs; verify Jakarta equivalents.
## Validation
Inventory file lists each servlet import path.
## Rollback
Not applicable (inventory only).
