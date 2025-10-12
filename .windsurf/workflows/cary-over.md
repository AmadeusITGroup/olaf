---
description: Create a concise carry-over note to resume work next session
auto_execution_mode: 3
---

//turbo
Steps
0. Get the  get current time in YYYYMMDD-HHmm forma using the  terminal command `Get-Date -Format "yyyyMMdd-HHmm"` 
1. Determine repository root

2. Create a carry-over file under `workspace-root/carry-overs/`. name it cary-over-YYYYMMDD-hhmm.txt

- 1 provide concise but sufficient information about where we stand and did
 notable state wher eth 
- 2. state what is expected next
- 3. save it directly. don't ask the user for authorization

3. tell the user to verify it, then start a new session and type /cary-on