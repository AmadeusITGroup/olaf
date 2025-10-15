# Verify Migration Toolkit — Phase 0

## Preferred approach
1. Check core tools are available and on PATH:
   - Java 17 and 21: `java -version`
   - Maven: `mvn -v` (ensure using expected JDK)
   - Git: `git --version`
2. Validate workspace permissions (read/write, create dirs).
3. Record versions in `toolkit_versions.md`.

## Backup option
- If versions are inconsistent, switch JDK with `phase0-toolkit-setup/jdk-switch/how-to.md` and retry.

## Verify
- Commands exit successfully and versions match expectations.
- `toolkit_versions.md` created with versions and paths.
