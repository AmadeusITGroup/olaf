# Realistic Bug Fixing Challenge

**Your Mission**: The OLAF VSCode Extension has 7 bugs that need fixing. Users have reported issues. Your job is to find and fix them.

**Rules**:
- You have access to the full codebase
- Use search, grep, and code analysis tools
- Each bug fix should be a separate commit
- Test your fixes to ensure they work
- No artificial hints - debug like you would in real scenarios

---

## Bug #1: File Size Display Issue

**User Report**:
> "When I look at file sizes in the extension, something seems off. A file that's exactly 1KB shows as '1024 Bytes' instead of '1 KB'. Same thing happens at the MB level - 1MB files show as '1048576 Bytes'. The unit conversion is broken."

**Expected Behavior**:
- 1024 bytes → "1 KB"
- 1048576 bytes → "1 MB"  
- 1073741824 bytes → "1 GB"

---

## Bug #2: Crash During Uninstall

**User Report**:
> "I deleted my project folder and then tried to uninstall OLAF. The extension crashed with 'Cannot read property length of undefined'. This happened during the cleanup process."

**Expected Behavior**:
- Uninstall should handle missing/corrupted metadata gracefully
- Should not crash even if project files are deleted
- Should log appropriate warnings

---

## Bug #3: Windows Directory Cleanup Problem

**User Report**:
> "I'm on Windows 10. After uninstalling OLAF, empty directories are left behind in my project. My Mac-using colleague says it works fine for him. The directories should be removed but they're not."

**Expected Behavior**:
- All empty installation directories should be removed
- Should work identically on Windows, Mac, and Linux
- No leftover empty folders

---

## Bug #4: Intermittent Uninstall Errors

**User Report**:
> "Weird issue - sometimes when I uninstall, I get 'Error: directory not empty' even though I can see it's empty. If I run uninstall again immediately, it works. It's random, maybe 20% of the time."

**Expected Behavior**:
- Uninstall should work consistently every time
- No race conditions or timing issues
- Directories removed in correct order

---

## Bug #5: Nested Directory Cleanup Fails

**User Report**:
> "I have a deeply nested project structure (like 8-9 folders deep). After uninstall, the cleanup happens in the wrong order. Sometimes I see errors about trying to remove a parent before a child, or paths getting mixed up. The ordering logic seems broken."

**Expected Behavior**:
- Directories should be removed deepest-first
- Sorting by depth should work correctly
- No errors about removing non-empty parents

---

## Bug #6: Windsurf Platform Installation Failure

**User Report**:
> "I'm using Windsurf (not VSCode). When I try to install OLAF, the download works but then it fails with 'No installation bundle found for your platform'. The logs show it detected 'Windsurf' correctly, but then it's searching for the wrong filename pattern. VSCode users don't have this problem."

**Expected Behavior**:
- Should detect Windsurf platform correctly
- Should find the correct bundle in GitHub releases
- Bundle filename matching should work consistently

---

## Bug #7: Token Expiration During Download

**User Report**:
> "I authenticated with 'gh auth login' yesterday. Today I tried to install OLAF - the download started but failed halfway with '401 Unauthorized'. I ran 'gh auth login' again and it worked immediately. It seems like the extension caches my token but doesn't check if it's still valid before using it."

**Expected Behavior**:
- Should validate GitHub token before using it
- Should detect expired/invalid tokens
- Should not cache tokens without validation
- Should provide clear error message about re-authentication

---

**Start with Bug #1 and work your way up. Good luck!**
