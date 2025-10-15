---
key: hard-coded-java-home
triggers:
  - regex: 'JAVA_HOME\s*=.*(8|11)'
severity: high
priority: 1
---

## Problem
Pipeline sets a fixed JAVA_HOME to an older JDK preventing migration steps.

## Recommended Actions
1. Replace hard-coded path with matrix/managed tool installer (e.g., actions/setup-java, Jenkins tool configuration).
2. Parameterize desired JDK via variable (e.g., JAVA_VERSION) and feed 17 then 21 later.
3. Remove legacy export lines from shell steps.

## Validation
Re-run scan: no lines matching regex; pipeline picks JAVA_VERSION variable.

## Rollback
Restore previous Jenkinsfile/GitHub workflow from git if build fails unexpectedly.
