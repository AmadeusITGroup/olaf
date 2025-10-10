# Install JDKs — Toolkit

## Preferred approach (Windows)
1. Install JDKs 11, 17, 21 under `C:\migration-toolkit\jdk\<major>`.
2. Use provided scripts to install/switch as needed.

Commands (PowerShell):
```powershell
# Install (example, adjust to your distro or org-provided archives)
# See task-0.0.1-install-jdks/install-windows.ps1 for automated install
powershell -ExecutionPolicy Bypass -File "${PSScriptRoot}\..\task-0.0.1-install-jdks\install-windows.ps1"

# Optional: switch session JDK
powershell -ExecutionPolicy Bypass -File "${PSScriptRoot}\..\task-0.0.1-install-jdks\switch-jdk.ps1" -JdkPath "C:\\migration-toolkit\\jdk\\21"
```

## Backup option
- Manually extract JDK archives into `C:\migration-toolkit\jdk\<major>` and update PATH per shell.

## Verify
- `dir C:\migration-toolkit\jdk` shows `11`, `17`, `21`.
- `java -version` and `mvn -v` run successfully after switching.
