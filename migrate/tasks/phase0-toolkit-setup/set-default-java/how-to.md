# Set Default Java — Toolkit

## Preferred approach (Windows, session scope)
1. Choose desired JDK (e.g., 17 or 21) under `C:\migration-toolkit\jdk\<major>`.
2. Set env vars for current shell.

Commands (PowerShell):
```powershell
$env:JAVA_HOME = "C:\\migration-toolkit\\jdk\\17"
$env:MAVEN_JAVA_HOME = $env:JAVA_HOME
$env:Path = "$($env:JAVA_HOME)\bin;" + $env:Path
java -version
mvn -v
```

## Backup option
- Use `phase0-toolkit-setup/jdk-switch/how-to.md` to switch via script with `-JdkPath`.

## Verify
- `java -version` and `mvn -v` report the expected JDK.
