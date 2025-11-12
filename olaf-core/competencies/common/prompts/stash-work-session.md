

## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.




## Purpose


Create a complete work stash that preserves both context documentation AND all unstaged files in a dedicated folder structure for seamless restoration in future sessions.





## Context


- User wants to pause current work and start something new


- Need to preserve actual working files, not just documentation


- Should enable complete restoration of work environment


- Files should be organized in timestamped folders for easy selection





## Instructions





### 1. Git Status Analysis & File Collection


- **First**: Run `git status` to identify all unstaged and untracked files


- **Collect**: All modified, added, deleted, and untracked files


- **Note**: Staged files (user may want to commit first)


- **Capture**: Current branch, git state, and working directory





### 2. Create Stash Directory Structure


Create stash folder with format: `olaf-stashes/YYYYMMDD-HHmm-<subject>/`





**Subject Extraction Rules:**


- Use main topic/feature being worked on  


- Keep to 2-3 words maximum


- Use kebab-case format


- Examples: "olaf-framework", "api-integration", "ui-components"





**Directory Structure:**


```


olaf-stashes/


├── 20251031-0845-api-integration/


│   ├── _stash-context.md          # Documentation


│   ├── src/                       # Copied unstaged files


│   ├── config/                    # Preserving structure


│   └── ...                        # All modified files


```





### 3. File Preservation Process


- **Create** stash directory: `olaf-stashes/YYYYMMDD-HHmm-<subject>/`


- **Copy** all unstaged files maintaining directory structure


- **Copy** all untracked files maintaining directory structure  


- **Create** `_stash-context.md` with work documentation


- **Record** file mapping and git state





**Stash Context Documentation:**


```


# STASH CONTEXT - <timestamp>


==============================





## Work Transition Notice:


🔄 **CURRENT WORK PAUSED** - Moving to new work session


📋 **STASH REASON**: [Brief reason for stashing]


📁 **STASH LOCATION**: olaf-stashes/YYYYMMDD-HHmm-<subject>/





## Files Preserved:


### Unstaged Files:


[List of copied modified files]





### Untracked Files: 


[List of copied new files]





### Git State:


- Branch: [current branch]


- Staged files: [if any]


- Last commit: [commit hash]





## Current State & What We Did:


[Detailed summary of work completed]





## What's Expected Next:


[Pending tasks and next steps]





## Restoration Commands:


1. Navigate to: olaf-stashes/YYYYMMDD-HHmm-<subject>/


2. Use stash-restart-session to restore files


3. Continue with: [specific next steps]





## Transition Notes:


✅ Files preserved in stash directory


✅ Work context documented  


🚀 Ready for new work session


```





### 4. File Management & Git Hygiene


- Create `olaf-stashes/` directory if it doesn't exist


- Preserve exact directory structure in stash folder


- Add `olaf-stashes/` to `.gitignore` if not present


- Keep original files untouched (copy, don't move)





### 5. Session Transition Message  


After creating stash directory and copying files:


- Confirm files have been preserved in stash directory


- Show stash location and file count


- State readiness for new work  


- Provide clear restoration instructions





## Output Format


1. **Analyze** git status and identify files to preserve


2. **Create** stash directory: `olaf-stashes/YYYYMMDD-HHmm-<subject>/`


3. **Copy** all unstaged/untracked files maintaining structure


4. **Create** `_stash-context.md` documentation


5. **Confirm** stash creation with directory path and file count


6. **Provide** transition message and restoration guidance


7. **Ask** what new work to begin





## Technical Implementation





### Python Stash Manager Tool


The stash system uses a dedicated Python tool for cross-platform reliability:


**Location**: `olaf-core/competencies/common/tools/stash_manager.py`





### Create Stash Command


```bash


python olaf-core/competencies/common/tools/stash_manager.py create <subject> --reason "Optional reason"


```





**Example:**


```bash


python olaf-core/competencies/common/tools/stash_manager.py create "api-integration" --reason "Pausing to work on docs"


```





### Key Features


- ✅ **Cross-platform**: Works on Windows, Linux, macOS


- ✅ **Git integration**: Automatically detects unstaged/untracked files


- ✅ **Structure preservation**: Maintains exact directory structure


- ✅ **Metadata tracking**: JSON + Markdown context files


- ✅ **Git ignore**: Automatically adds olaf-stashes/ to .gitignore


- ✅ **Clean interface**: Simple command-line tool





### Implementation Benefits


- **No complex shell commands** in competency files


- **Consistent behavior** across all platforms  


- **Easy maintenance** and testing


- **Proper error handling** with Python exceptions


- **Extensible design** for future enhancements





## Success Criteria


- ✅ **Complete File Preservation**: All unstaged/untracked files copied to stash directory


- ✅ **Structure Maintained**: Directory tree preserved exactly  


- ✅ **Context Documented**: Clear work summary and restoration steps


- ✅ **Easy Discovery**: Stash named with timestamp and subject for easy identification


- ✅ **Restoration Ready**: Files ready for seamless restoration via stash-restart-session


- ✅ **Git Hygiene**: Stash directory properly ignored by git


````


