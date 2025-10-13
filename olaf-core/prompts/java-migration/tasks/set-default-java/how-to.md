# Set Default Java — OLAF Structure

## Preferred approach (Cross-platform, session scope)
1. Choose desired JDK (e.g., 17 or 21) under `~/.olaf/jdk/{version}/`.
2. Set environment variables for current shell.

Commands:
```bash
# Windows (PowerShell)
$env:JAVA_HOME = "$env:USERPROFILE\.olaf\jdk\17"
$env:MAVEN_JAVA_HOME = $env:JAVA_HOME
$env:PATH = "$env:JAVA_HOME\bin;$env:PATH"

# Linux/macOS (Bash)
export JAVA_HOME=~/.olaf/jdk/17
export MAVEN_JAVA_HOME=$JAVA_HOME
export PATH=$JAVA_HOME/bin:$PATH
```

Verify:
```bash
java -version
mvn -version
```

## Backup option
- Use system JDK installations if OLAF structure not available
- Refer to `jdk-switch/how-to.md` for system JDK switching

## Verify
- `java -version` and `mvn -v` report the expected JDK.
