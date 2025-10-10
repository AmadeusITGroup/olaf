# Install jq — Toolkit

## Preferred approach (Windows)
1. Install jq via winget.

Commands:
```powershell
winget install -e --id jqlang.jq
jq --version
```

## Backup option
- Download jq.exe from official releases and place into `C:\migration-toolkit\bin`, then refresh PATH.

## Verify
- `jq --version` prints a version.
- `where jq` shows the expected path.
