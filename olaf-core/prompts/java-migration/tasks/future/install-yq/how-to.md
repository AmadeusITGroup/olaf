# Install yq — Toolkit

## Preferred approach (Windows)
1. Install yq via winget.

Commands:
```powershell
winget install -e --id MikeFarah.yq
yq --version
```

## Backup option
- Download yq.exe from official releases and place into `C:\migration-toolkit\bin`, then refresh PATH.

## Verify
- `yq --version` prints a version.
- `where yq` shows the expected path.
