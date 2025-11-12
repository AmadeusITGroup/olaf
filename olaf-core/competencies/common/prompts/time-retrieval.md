## Time Retrieval Helper
- Windows (PowerShell)

```powershell
Get-Date -Format "yyyyMMdd"            # yyyymmdd
Get-Date -Format "yyyyMMdd:HHmm"       # yyyymmdd:hhmm
Get-Date -Format "yyyyMMdd:HHmmss.fff" # yyyymmdd:hhmmss.ms
```

- Unix/Linux

```bash
date +"%Y%m%d"                # yyyymmdd
date +"%Y%m%d:%H%M"           # yyyymmdd:hhmm
date +"%Y%m%d:%H%M%S.%3N"     # yyyymmdd:hhmmss.ms
```

- macOS note: default BSD date lacks %N. Use coreutils:

```bash
gdate +"%Y%m%d:%H%M%S.%3N"