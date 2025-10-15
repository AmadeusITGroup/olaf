# Install OpenRewrite — Toolkit

## Preferred approach
1. Install Rewrite plugin for your build tool.
   - Maven: add `org.openrewrite.maven:rewrite-maven-plugin`
   - Gradle: `plugins { id("org.openrewrite.rewrite") version "latest" }`
2. Keep recipes disabled for now (no active recipes).
3. Create empty `rewrite.yml` to be filled later.

## Backup option
- If plugin setup is blocked, use the Rewrite Docker/CLI temporarily, then migrate to build plugin later.

## Verify
- Maven: `mvn -q rewrite:help` prints plugin help
- Gradle: `./gradlew rewriteDiscover` runs without error
