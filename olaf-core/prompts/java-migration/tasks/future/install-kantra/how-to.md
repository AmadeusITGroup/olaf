# Install Konveyor Kantra — Toolkit

## Preferred approach (Windows)
1. Install/upgrade Kantra CLI into `C:\migration-toolkit\bin`.
2. Ensure the bin directory is on PATH for the current shell.

Commands (PowerShell):
```powershell
$Bin = "C:\\migration-toolkit\\bin"
if(-not (Test-Path $Bin)){ New-Item -ItemType Directory -Force -Path $Bin | Out-Null }
$env:Path = "$Bin;" + $env:Path
# If a helper script exists, use it; otherwise download the latest release asset for Windows amd64
# Example (placeholder):
# iwr -UseBasicParsing -OutFile "$Bin\\kantra.exe" "https://example.com/kantra/latest/windows-amd64/kantra.exe"
kantra --version
```

## Backup option
- Manually place `kantra.exe` into `C:\migration-toolkit\bin` and refresh PATH.

## Verify
- `kantra --version` prints a version.
- `where kantra` shows the path under `C:\migration-toolkit\bin`.
