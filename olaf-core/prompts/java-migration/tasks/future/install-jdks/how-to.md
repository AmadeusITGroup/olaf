# Install JDKs — Toolkit

## Preferred approach (Cross-platform)
1. Install JDKs 11, 17, 21 under `~/.olaf/jdk/{version}/`.
2. Use provided switching scripts as needed.

Commands (PowerShell):
```powershell
# Install (example, adjust to your distro or org-provided archives)
# See task-0.0.1-install-jdks/install-windows.ps1 for automated install
powershell -ExecutionPolicy Bypass -File "${PSScriptRoot}\..\task-0.0.1-install-jdks\install-windows.ps1"

# Optional: switch session JDK
# Windows
$env:JAVA_HOME = "$env:USERPROFILE\.olaf\jdk\21"
# Linux/macOS  
export JAVA_HOME=~/.olaf/jdk/21
```

## Backup option
- Manually extract JDK archives into `~/.olaf/jdk/{version}/` and update PATH per shell.

## Verify
- `ls ~/.olaf/jdk/` shows `11`, `17`, `21`.
- `java -version` and `mvn -version` run successfully after switching.
