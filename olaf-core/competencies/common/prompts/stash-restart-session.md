

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.




## Purpose


Scan the olaf-stashes directory for preserved work sessions and enable seamless restoration of files and context to resume work where it was left off. Includes pre-restoration git status check with OLAF commit thread integration to handle uncommitted changes safely.





## Context


- User wants to resume previously stashed work with actual files


- Must check for uncommitted changes before stash restoration to prevent data loss


- Should offer OLAF commit thread integration for safe handling of current work


- Need to identify available work stashes with preserved file states


- Should restore complete working environment, not just documentation


- Present numbered options for easy selection





## Instructions





### ⚠️ CRITICAL: PYTHON SCRIPT MANDATORY FOR ALL STASH OPERATIONS


**ALL stash operations MUST use the Python stash manager script:**


- `python olaf-core/competencies/common/tools/stash_manager.py list`


- `python olaf-core/competencies/common/tools/stash_manager.py conflicts <stash-name>`  


- `python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name> [--backup|--force]`





**❌ NEVER use manual file operations, directory scanning, or timestamp comparison**





### 0. Pre-Restoration Git Status Check 


**CRITICAL FIRST STEP**: Before any stash operations, check for uncommitted changes:





- **Double Git Status Check**: Run TWO different commands to ensure reliable detection


- **Uncommitted Files Detection**: If any files are found (staged or unstaged changes)


- **Present Commit Option**: Offer user the OLAF commit thread competency before proceeding





**Git Status Analysis (Double-Check Protocol):**


```bash


# First check: machine-readable format


git status --porcelain





# Second check: alternative short format (verification)


git status --short


```





**Why Double-Check is Critical:**


- Tool execution timing issues can cause first command to return empty results


- Two different git status formats provide cross-validation


- Prevents false "clean" status when changes actually exist


- Ensures reliable detection before proceeding with stash operations





**If uncommitted files found:**


```


✅ DOUBLE-CHECK CONFIRMED: Uncommitted changes detected





Both --porcelain and --short show:


• [N] staged files


• [N] unstaged modifications  


• [N] untracked files


• [N] files with both staged + unstaged changes





⚠️  UNCOMMITTED CHANGES DETECTED





🔧 RECOMMENDED ACTION: Commit current changes before restoring stash





Options:


1. 🚀 Launch OLAF commit thread to organize and commit changes


2. 📋 Show detailed git status and continue anyway


3. 🛑 Cancel stash restoration (recommended if unsure)





Would you like me to launch the OLAF commit thread? (y/N)


```





**OLAF Commit Thread Integration:**


- If user selects option 1, launch: `olaf propose commit thread`


- Wait for commit completion before proceeding with stash restoration


- After commits complete, recheck git status to ensure clean state


- Proceed with stash restoration only after clean git state confirmed





**Benefits of Pre-Commit Check:**


- ✅ **Prevents Data Loss**: Current work preserved before stash restoration


- ✅ **Clean Git History**: Separates current changes from restored stash


- ✅ **User Control**: Explicit choice to commit or proceed with uncommitted changes


- ✅ **Workflow Integration**: Seamless handoff to OLAF commit competency





### 1. Scan Stash Directories - USE PYTHON SCRIPT ONLY


**MANDATORY**: Use the Python stash manager script for all stash operations:





```bash


python olaf-core/competencies/common/tools/stash_manager.py list


```





**DO NOT**:


- Manually scan `olaf-stashes/` directory


- Use `list_dir` or file system commands


- Parse directory names manually


- Count files manually





The Python script handles:


- Directory discovery and validation


- Timestamp extraction and formatting


- File counting and analysis


- Context loading from `_stash-context.md`


- Proper error handling and cross-platform support





### 3. Present Numbered Options  


Create a structured, numbered list for easy selection:





**Format:**


```


## 🔄 Available Work Stashes:





1. **[Subject]** - [Date/Time]


   📁 Directory: olaf-stashes/YYYYMMDD-HHmm-subject/


   📄 Files: [count] files preserved


   📝 Summary: [Brief description of work]


   🎯 Next: [What's expected next]





2. **[Subject]** - [Date/Time] 


   📁 Directory: olaf-stashes/YYYYMMDD-HHmm-subject/


   📄 Files: [count] files preserved


   📝 Summary: [Brief description of work]  


   🎯 Next: [What's expected next]





---


Select number (1-N) or 'fresh' for new work


```





### 4. User Selection & Confirmation


- Present numbered options (1-N) for easy selection


- Include 'fresh' option to start new work instead


- Wait for user's numbered choice


- Validate selection and confirm before proceeding





### 5. Pre-Restoration Conflict Detection - USE PYTHON SCRIPT ONLY


**MANDATORY**: Use the Python stash manager script for conflict detection:





```bash


python olaf-core/competencies/common/tools/stash_manager.py conflicts <stash-name>


```





**DO NOT**:


- Manually scan stash directory files


- Use file system commands to check file existence


- Compare timestamps manually


- Use `read_file` or other manual checking methods





The Python script handles:


- Cross-platform timestamp comparison


- Reliable conflict detection logic  


- Proper file existence checking


- Clear conflict reporting with detailed information





**Conflict Resolution Options:**


```


⚠️ CONFLICT DETECTED: Files with newer modifications found





Conflicting Files:


❌ src/api/handler.js - Current: 2025-10-31 09:15, Stash: 2025-10-31 08:45 


❌ config/app.json - Current: 2025-10-31 09:30, Stash: 2025-10-31 08:50





Options:


1. 🛑 Cancel restoration (recommended)


2. 📁 Backup current files first, then restore


3. 🔍 Show detailed diff for each conflict  


4. ⚡ Force overwrite (DANGEROUS - will lose current changes)





Select option (1-4):


```





### 6. Safe File Restoration Process - USE PYTHON SCRIPT ONLY


**MANDATORY**: Use the Python stash manager script for restoration:





```bash


# Safe restore (no conflicts)


python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name>





# With backup (conflicts handled)  


python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name> --backup





# Force restore (user accepts risk)


python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name> --force


```





**DO NOT**:


- Manually copy files from stash directory


- Use file system commands for restoration


- Handle backups manually


- Parse context files manually





The Python script handles:


- Safe file copying with error handling


- Automatic backup creation when requested


- Context loading and presentation


- Cross-platform file operations


- Proper restoration reporting





### 7. Post-Restoration Setup


- **Restoration Summary**: Report files restored, conflicts resolved, backups created


- **Git Status**: Show current git state after restoration  


- **Context Load**: Present work summary and accomplishments from `_stash-context.md`


- **Backup Locations**: If backups were created, provide their locations


- **Next Steps**: Clear action items from stash context


- **Conflict Resolution**: If conflicts occurred, remind user of resolution chosen


- **Confirmation**: Ask user to confirm readiness to continue work





## Directory Identification Rules





**Primary Stash Directories:**


- **Pattern**: `olaf-stashes/YYYYMMDD-HHmm-<subject>/`


- **Contents**: Preserved files + `_stash-context.md`


- **Structure**: Original directory tree maintained





**Legacy Stash Files (Fallback):**


- **Pattern**: `carry-overs/stashed-*.txt` 


- **Contents**: Documentation only (no files preserved)


- **Note**: Present as secondary options if no directories found





**Directory Validation:**


- Must contain `_stash-context.md` file


- Must have at least one preserved file (not just documentation)


- Skip directories older than 60 days unless explicitly requested


- Ignore incomplete or corrupted stash directories





**Conflict Detection & Safety Rules:**


- **CRITICAL**: Never overwrite files with newer last-modified dates


- **Compare timestamps**: Stash file vs current working file


- **Identify risks**: Files modified after stash creation


- **Block dangerous operations**: Default to safe cancellation


- **Provide alternatives**: Backup, selective restore, or detailed diff analysis





**Conflict Detection via Python Tool:**


The Python stash manager automatically handles cross-platform timestamp comparison using Python's `pathlib.Path.stat()` for consistent behavior across Windows, Linux, and macOS.





## Output Format





### Pre-Restoration Git Status Check:


1. **Double Git Check:** "Checking for uncommitted changes with double verification..."


2. **Cross-Validation:** Run both `git status --porcelain` and `git status --short`


3. **If Clean:** "✅ Git status clean (verified by both commands) - proceeding with stash scan"


4. **If Uncommitted:** Present commit options with OLAF integration prompt


5. **After Commit:** Re-verify git status with double-check and confirm readiness





### If Stash Directories Found:


1. **Header:** "🔄 Available Work Stashes"


2. **Numbered List:** Structured options with file counts and summaries


3. **Selection Prompt:** "Select number (1-N) or type 'fresh' for new work"


4. **Conflict Check:** Warn if restoration would overwrite current changes





### If No Stash Directories Found:


1. **Primary Message:** "No work stashes found in olaf-stashes/"


2. **Fallback Check:** Search carry-overs/ for legacy text-only stashes  


3. **Alternative:** Offer to start new work or check other session options





### During Restoration:


1. **Confirmation:** "Restoring stash: [subject] ([N] files)"


2. **Progress:** Show files being copied back to workspace


3. **Validation:** Confirm successful restoration with file count


4. **Git Status:** Display current repository state after restoration





### After Restoration Complete:


1. **Success Message:** "✅ Work stash restored successfully"


2. **Context Summary:** Load and present work context from stash


3. **File Overview:** List key files that were restored


4. **Next Steps:** Present clear action items from stash context  


5. **Readiness Check:** "Ready to continue? What would you like to focus on first?"





## Technical Implementation





### Python Stash Manager Commands





**MANDATORY PYTHON SCRIPT USAGE:**





**List Available Stashes (REQUIRED):**


```bash


python olaf-core/competencies/common/tools/stash_manager.py list


```





**Check for Conflicts (REQUIRED):**


```bash


python olaf-core/competencies/common/tools/stash_manager.py conflicts <stash-name>


```





**Restore Stash (REQUIRED):**


```bash


python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name>


```





**Restore with Backup (REQUIRED):**


```bash


python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name> --backup


```





**❌ DO NOT USE:**


- Manual directory scanning (`list_dir`, `ls`, `Get-ChildItem`)


- Manual file operations (`copy`, `cp`, `Copy-Item`)


- Manual timestamp comparison


- Manual context file reading





### Workflow Process





**0. Pre-Restoration Git Check** - Always check for uncommitted changes first:


```bash


# Double-check git status before any stash operations (prevents false clean status)


git status --porcelain


git status --short


```





**If uncommitted changes detected:**


- Present user with commit options


- Offer to launch OLAF commit thread: `olaf propose commit thread`


- Wait for user decision and potential commit completion


- Recheck git status after commits (if executed)


- Proceed only when user confirms readiness





**1. List Stashes (MANDATORY PYTHON SCRIPT)** - Show numbered options to user:


```bash


python olaf-core/competencies/common/tools/stash_manager.py list


```





**2. Check Selected Stash (MANDATORY PYTHON SCRIPT)** - Detect conflicts before restoration:


```bash  


python olaf-core/competencies/common/tools/stash_manager.py conflicts <stash-name>


```





**3. Handle Conflicts** - Present options based on conflict check:


- ✅ **No conflicts**: Proceed with safe restoration


- ⚠️ **Conflicts detected**: Present user options:


  - 🛑 Cancel restoration (recommended)


  - 📁 Backup current files first (`--backup`)  


  - ⚡ Force overwrite (`--force`, dangerous)





**4. Execute Restoration** - Run appropriate restore command:


```bash


# Safe restore (no conflicts)


python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name>





# With backup (conflicts handled)  


python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name> --backup





# Force restore (user accepts risk)


python olaf-core/competencies/common/tools/stash_manager.py restore <stash-name> --force


```





### Implementation Benefits


- **No complex shell scripting** in competency files


- **Consistent cross-platform behavior** 


- **Clean command interface** with clear options


- **Proper error handling** and user feedback


- **Maintainable Python code** instead of embedded scripts





## Success Criteria


- ✅ **Pre-Commit Check**: Uncommitted changes detected and user offered commit option before restoration


- ✅ **OLAF Integration**: Seamless handoff to OLAF commit thread when uncommitted files found


- ✅ **Clean Git State**: Restoration proceeds only after git status is clean or user confirms


- ✅ **Complete Discovery**: All available work stashes identified and presented


- ✅ **Easy Selection**: Numbered list allows quick choice


- ✅ **Conflict Detection**: Automatic timestamp comparison prevents data loss


- ✅ **User Safety**: Clear warnings for any potential file overwrites


- ✅ **Safe Restoration**: Files restored only with explicit user consent for conflicts


- ✅ **Backup Protection**: Current files backed up before any overwrite operations


- ✅ **Context Loaded**: Work summary and next steps clearly presented


- ✅ **Ready State**: User can immediately continue productive work


- ✅ **File Integrity**: All preserved files restored to original locations without corruption


- ✅ **Rollback Capability**: Failed operations can be safely reversed





## Error Handling


- Handle missing carry-overs directory gracefully


- Skip corrupted or unreadable stashed files


````


