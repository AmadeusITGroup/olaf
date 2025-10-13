# Install Gradle — Toolkit

## Preferred approach (Windows)
1. Install Gradle via winget.

Commands:
```powershell
winget install -e --id Gradle.Gradle
gradle -v
```

## Backup option
- Download a Gradle binary distribution and unzip to `C:\migration-toolkit\gradle`; add `...\bin` to PATH for the current shell.

## Verify
- `gradle -v` prints a version.
- `where gradle` shows expected path.
