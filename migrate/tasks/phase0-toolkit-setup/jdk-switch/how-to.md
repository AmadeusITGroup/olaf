# JDK Switch — Set current shell to JDK 21

## Preferred approach (Windows, PowerShell)
1. Set path to your JDK 21 installation (example below; adjust if different).
2. Run the switch script to update current shell environment.
3. Verify Java and Maven both run on JDK 21.

Commands:
```powershell
$JdkPath = "C:\\migration-toolkit\\jdk\\21"
powershell -ExecutionPolicy Bypass -File "${PSScriptRoot}\..\task-0.0.1-install-jdks\switch-jdk.ps1" -JdkPath $JdkPath
java -version
mvn -v
```

## Backup option (manual env change)
- Temporarily set for the current shell only:
```powershell
$env:JAVA_HOME = "C:\\migration-toolkit\\jdk\\21"
$env:MAVEN_JAVA_HOME = $env:JAVA_HOME
$env:Path = "$($env:JAVA_HOME)\bin;" + $env:Path
java -version
mvn -v
```

## Verify
- `java -version` shows 21
- `mvn -v` reports the same JDK path/version

## Notes
- This is session-scoped. Opening a new shell resets variables.
- If using Gradle toolchains or Maven toolchains, align them after this step (see `phase3-jdk21-modernization/toolchains-and-ci/how-to.md`).
