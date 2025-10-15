# Verify Toolkit — Extended Checks

## Preferred approach
1. Verify multiple JDKs available under `~/.olaf/jdk/{version}` (11, 17, 21):
   - `ls ~/.olaf/jdk/` (cross-platform)
2. Switch to JDK 21 and back to 17 using `jdk-switch/how-to.md`.
3. Validate package managers and shells if needed:
   - `winget --version` (Windows) or `brew --version` (macOS) or distro pkg manager
4. Check Git configuration (`user.name`, `user.email`) and remotes.

## Backup option
- If multiple JDKs are not present, install them before proceeding with migration tasks.

## Verify
- Ability to switch between 17 and 21; `java -version` reflects changes.
- Git remotes configured and accessible if pushing.
