# Introduced Bugs Catalog for Benchmark Testing

**Repository**: OLAF VSCode Extension  
**Purpose**: Progressive bug complexity testing for AI agents  
**Date Created**: 2025-10-06  
**Branch**: research-benchmark

## Overview

This document catalogs 5 intentionally introduced bugs in the OLAF VSCode Extension codebase. Each bug is designed to:
- Allow the code to compile/build successfully
- Cause at least one existing unit test to fail
- Progress from simple to complex in difficulty
- Mirror real-world bug scenarios

## Bug Catalog

---

### Bug #1: Off-by-One Error in File Size Formatting (EASY)

**User Symptom Report**:
> "The file size display shows '0 Bytes' for tiny files, but when I check files that are exactly 1KB or 1MB, they're showing up as '1024 Bytes' instead of '1 KB'. The conversion between units seems off by one level."

**Location**: `vscode-extension/src/utils/fileUtils.ts`

**Line Number**: 147

**Function**: `formatFileSize(bytes: number): string`

**Bug Type**: Logic Error (Boundary Condition)

**Original Code**:
```typescript
public static formatFileSize(bytes: number): string {
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    if (bytes === 0) {return '0 Bytes';}
    
    const i = Math.floor(Math.log(bytes) / Math.log(1024));
    const size = bytes / Math.pow(1024, i);
    
    return `${Math.round(size * 100) / 100} ${sizes[i]}`;
}
```

**Buggy Code** (Change line 151):
```typescript
public static formatFileSize(bytes: number): string {
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    if (bytes === 0) {return '0 Bytes';}
    
    const i = Math.floor(Math.log(bytes) / Math.log(1024));
    const size = bytes / Math.pow(1024, i);
    
    return `${Math.round(size * 100) / 100} ${sizes[i - 1]}`;  // BUG: off-by-one with i-1
}
```

**Change Description**: Changed `sizes[i]` to `sizes[i - 1]` on line 151

**Affected Test**: Unit test checking file size formatting with values like 1024, 1048576, etc.

**Expected Test Failure**: Test assertions checking proper unit conversion (KB, MB, GB) will fail with array index errors or incorrect unit labels

**Complexity**: Easy - Single line change, obvious logic error, clear test failure message

---

### Bug #2: Missing Null Check in Directory Listing (EASY-MEDIUM)

**User Symptom Report**:
> "The extension crashes when trying to uninstall OLAF from a project that was deleted. I get an error about 'Cannot read property length of undefined' during the cleanup process."

**Location**: `vscode-extension/src/services/installationManager.ts`

**Line Number**: 159

**Function**: `pruneEmptyDirs(scope: InstallationScope): Promise<void>`

**Bug Type**: Null/Undefined Reference Error

**Original Code**:
```typescript
// Read installation metadata to get extraction path and installed files
try {
    const metadata = await this.readInstallationMetadata(installationPath);
    extractionPath = metadata.extractionPath ?? extractionPath;
    installedFiles = metadata.installedFiles || [];
    this.logger.info(`Extraction path: ${extractionPath}`);
    this.logger.info(`Files that were installed: ${installedFiles.length} files`);
} catch {
    this.logger.warn('Could not read installation metadata for pruning');
}
```

**Buggy Code** (Change line 156):
```typescript
// Read installation metadata to get extraction path and installed files
try {
    const metadata = await this.readInstallationMetadata(installationPath);
    extractionPath = metadata.extractionPath ?? extractionPath;
    installedFiles = metadata.installedFiles;  // BUG: removed null coalescing operator
    this.logger.info(`Extraction path: ${extractionPath}`);
    this.logger.info(`Files that were installed: ${installedFiles.length} files`);
} catch {
    this.logger.warn('Could not read installation metadata for pruning');
}
```

**Change Description**: Removed the `|| []` null coalescing on line 156, changing `metadata.installedFiles || []` to just `metadata.installedFiles`

**Affected Test**: Test case for corrupted or missing metadata during uninstallation

**Expected Test Failure**: Test "should gracefully handle non-existent installation" or "should handle corrupted metadata gracefully" will fail with TypeError when trying to iterate over undefined installedFiles

**Complexity**: Easy-Medium - Classic null check issue, common in JavaScript/TypeScript, clear failure point

---

### Bug #3: Incorrect Path Separator Handling (MEDIUM)

**User Symptom Report**:
> "On Windows, when I install OLAF to a project, the uninstall process doesn't clean up properly. Some directories are left behind even though they're empty. This only happens on Windows, works fine on Mac/Linux."

**Location**: `vscode-extension/src/services/installationManager.ts`

**Line Number**: 170

**Function**: `pruneEmptyDirs(scope: InstallationScope): Promise<void>`

**Bug Type**: Platform-Specific Path Handling Error

**Original Code**:
```typescript
// Add directories from installed files
for (const file of installedFiles) {
    const filePath = path.join(extractionPath, file);
    let dir = path.dirname(filePath);
    
    // Add all parent directories up to the extraction path
    while (dir !== extractionPath && dir !== path.dirname(dir)) {
        directoriesToCheck.add(dir);
        dir = path.dirname(dir);
    }
}
```

**Buggy Code** (Change line 168):
```typescript
// Add directories from installed files
for (const file of installedFiles) {
    const filePath = extractionPath + '/' + file;  // BUG: hardcoded forward slash instead of path.join
    let dir = path.dirname(filePath);
    
    // Add all parent directories up to the extraction path
    while (dir !== extractionPath && dir !== path.dirname(dir)) {
        directoriesToCheck.add(dir);
        dir = path.dirname(dir);
    }
}
```

**Change Description**: Changed `path.join(extractionPath, file)` to `extractionPath + '/' + file` on line 168

**Affected Test**: Test "should remove empty directories after file removal" on Windows platforms

**Expected Test Failure**: Path comparison fails on Windows because mixed separators ('/' vs '\\') cause the while loop condition to never match, leaving directories behind

**Complexity**: Medium - Platform-specific issue, requires understanding of path handling differences across OS, may not be immediately obvious without testing on Windows

---

### Bug #4: Race Condition in Async Directory Removal (MEDIUM-HARD)

**User Symptom Report**:
> "Sometimes when uninstalling, I get intermittent errors about 'directory not empty' even though the files should have been deleted. If I run uninstall again immediately, it works. It's not consistent - happens maybe 1 in 5 times."

**Location**: `vscode-extension/src/services/installationManager.ts`

**Line Number**: 192

**Function**: `pruneEmptyDirs(scope: InstallationScope): Promise<void>`

**Bug Type**: Concurrency/Race Condition

**Original Code**:
```typescript
this.logger.debug(`Checking ${sortedDirectories.length} directories for emptiness`);

// Remove empty directories, starting from the deepest
for (const dir of sortedDirectories) {
    await this.removeIfEmpty(dir);
}
```

**Buggy Code** (Change to parallel execution):
```typescript
this.logger.debug(`Checking ${sortedDirectories.length} directories for emptiness`);

// Remove empty directories, starting from the deepest
await Promise.all(sortedDirectories.map(dir => this.removeIfEmpty(dir)));  // BUG: parallel execution creates race condition
```

**Change Description**: Changed sequential `for...await` loop to `Promise.all()` parallel execution on line 192-194

**Affected Test**: Test "should remove empty directories after file removal" - intermittent failures

**Expected Test Failure**: Test will sporadically fail because parent directories may be checked/removed before child directories are fully processed, causing "ENOTEMPTY" errors

**Complexity**: Medium-Hard - Timing-dependent bug, requires understanding of async/await patterns, may not fail consistently, needs multiple test runs to reproduce

---

### Bug #5: Incorrect Depth Calculation for Nested Paths (HARD)

**User Symptom Report**:
> "After uninstalling OLAF, I noticed that deeply nested folder structures aren't being cleaned up in the right order. Sometimes parent folders get removed before their children, causing errors. The cleanup seems to process folders in the wrong sequence, especially for paths with many levels."

**Location**: `vscode-extension/src/services/installationManager.ts`

**Line Number**: 185

**Function**: `pruneEmptyDirs(scope: InstallationScope): Promise<void>`

**Bug Type**: Algorithm Logic Error (Sorting/Priority)

**Original Code**:
```typescript
// Convert to array and sort by depth (deepest first) for proper removal order
const sortedDirectories = Array.from(directoriesToCheck).sort((a, b) => {
    const depthA = a.split(path.sep).length;
    const depthB = b.split(path.sep).length;
    return depthB - depthA; // Sort by depth, deepest first
});
```

**Buggy Code** (Change line 187-188):
```typescript
// Convert to array and sort by depth (deepest first) for proper removal order
const sortedDirectories = Array.from(directoriesToCheck).sort((a, b) => {
    const depthA = a.split(path.sep).filter(p => p.length > 0).length;  // BUG: filter removes empty strings
    const depthB = b.length;  // BUG: using string length instead of path depth
    return depthB - depthA; // Sort by depth, deepest first
});
```

**Change Description**: 
- Line 187: Added `.filter(p => p.length > 0)` to depthA calculation (inconsistent with depthB)
- Line 188: Changed depthB calculation from `b.split(path.sep).length` to just `b.length` (string length instead of path depth)

**Affected Test**: Test "should remove empty directories after file removal" with deeply nested structures

**Expected Test Failure**: Directories are removed in wrong order causing "ENOTEMPTY" errors or parent directories persisting when they should be removed

**Complexity**: Hard - Subtle algorithm bug with multiple issues, requires understanding of sorting algorithms, path depth concepts, and the impact of inconsistent calculations. The bug has two parts that interact to create incorrect behavior.

---

## Testing Strategy

### For Each Bug:

1. **Reproduce**:
   - Apply the buggy code change
   - Run the affected test suite
   - Confirm test failure

2. **Document Failure**:
   - Capture exact error message
   - Note which test(s) fail
   - Record any intermittent behavior

3. **Benchmark Agent**:
   - Provide only the "User Symptom Report"
   - Measure time to identify bug location
   - Measure time to propose fix
   - Compare proposed fix to original code
   - Score correctness and approach

4. **Scoring Criteria**:
   - **Identification Speed**: How quickly bug location is found
   - **Root Cause Analysis**: Understanding of why bug occurs
   - **Fix Quality**: Comparison to original working code
   - **Test Coverage**: Does fix address all edge cases?
   - **Code Style**: Matches existing patterns and conventions

## Expected Agent Performance Benchmarks

| Bug # | Difficulty | Expected Time (Elite) | Expected Time (Proficient) | Key Skills Tested |
|-------|------------|----------------------|---------------------------|-------------------|
| 1 | Easy | 2-5 min | 5-10 min | Code reading, debugging |
| 2 | Easy-Medium | 5-8 min | 10-15 min | Null safety, error handling |
| 3 | Medium | 8-12 min | 15-25 min | Cross-platform, path handling |
| 4 | Medium-Hard | 12-20 min | 25-40 min | Async patterns, concurrency |
| 5 | Hard | 20-30 min | 40-60 min | Algorithm analysis, subtle logic |

## Usage Instructions

1. **Create Degraded Branch**:
   ```bash
   git checkout -b benchmark-degraded-v1
   ```

2. **Apply Bugs Sequentially**:
   - Start with Bug #1, apply change, commit
   - Run tests to verify failure
   - Continue with Bug #2-5

3. **Create Bug-Specific Branches** (Recommended):
   ```bash
   git checkout -b benchmark-bug-1-only
   # Apply only Bug #1
   git commit -m "Introduce Bug #1: Off-by-One Error"
   ```

4. **Agent Testing Protocol**:
   - Provide only symptom description
   - Do not reveal file location or bug type
   - Measure all interactions and tool usage
   - Compare final solution to documented original

## Restoration Commands

To restore original code for each bug:

```bash
# Bug #1
git diff HEAD~1 src/utils/fileUtils.ts

# Bug #2  
git diff HEAD~2 src/services/installationManager.ts

# Bug #3
git diff HEAD~3 src/services/installationManager.ts

# Bug #4
git diff HEAD~4 src/services/installationManager.ts

# Bug #5
git diff HEAD~5 src/services/installationManager.ts
```

---

### Bug #6: Inconsistent Platform Prefix Handling Across Services (HARD - Multi-File)

**User Symptom Report**:
> "When I install OLAF on Windsurf, it downloads successfully but then fails saying 'No installation bundle found for your platform'. The logs show it detected Windsurf correctly, but then it's looking for bundles with the wrong naming pattern. This only happens on non-VSCode platforms."

**Locations**: 
- **File 1**: `vscode-extension/src/services/githubService.ts` (Line 545)
- **File 2**: `vscode-extension/src/services/platformDetector.ts` (Line 74)
- **File 3**: `vscode-extension/src/commands/installCommand.ts` (Line 80)

**Bug Type**: Inconsistent String Handling Across Services

**Original Code**:

**File 1 - githubService.ts (Line 545)**:
```typescript
private getPlatformPrefix(platform: Platform): string {
    const prefixMap: Record<Platform, string> = {
        [Platform.VSCODE]: 'vscode',
        [Platform.WINDSURF]: 'windsurf',
        [Platform.KIRO]: 'kiro',
        [Platform.CURSOR]: 'cursor',
        [Platform.UNKNOWN]: 'vscode' // fallback
    };
    
    return prefixMap[platform];
}
```

**File 2 - platformDetector.ts (Line 74)**:
```typescript
[Platform.VSCODE]: {
    platform: Platform.VSCODE,
    bundlePrefix: 'vscode',
    installationPaths: {
```

**File 3 - installCommand.ts (Line 80)**:
```typescript
// Find platform bundle
const bundleInfo = this.githubService.findPlatformBundle(release, platform.platform);
if (!bundleInfo) {
    throw new Error(`No installation bundle found for your platform (${platform.platform})`);
}
```

**Buggy Code**:

**File 1 - githubService.ts (Change line 547)**:
```typescript
private getPlatformPrefix(platform: Platform): string {
    const prefixMap: Record<Platform, string> = {
        [Platform.VSCODE]: 'vscode',
        [Platform.WINDSURF]: 'Windsurf',  // BUG: Capitalized instead of lowercase
        [Platform.KIRO]: 'kiro',
        [Platform.CURSOR]: 'cursor',
        [Platform.UNKNOWN]: 'vscode' // fallback
    };
    
    return prefixMap[platform];
}
```

**File 2 - platformDetector.ts (Change line 76 - keep original)**:
```typescript
[Platform.VSCODE]: {
    platform: Platform.VSCODE,
    bundlePrefix: 'vscode',  // No change - stays lowercase
    installationPaths: {
```

**Change Description**: 
- **File 1 (githubService.ts)**: Changed `'windsurf'` to `'Windsurf'` (capitalized) on line 547
- **File 2 (platformDetector.ts)**: Keep original `bundlePrefix: 'windsurf'` (lowercase)
- **File 3 (installCommand.ts)**: No changes - the bug is in the inconsistency

**Root Cause**: The `githubService` uses `getPlatformPrefix()` internally when searching for bundles, but this returns a capitalized string for Windsurf while the `platformDetector` config uses lowercase. When `findPlatformBundle()` searches for assets, it looks for filenames containing the capitalized version but GitHub releases have lowercase filenames.

**Affected Test**: Integration test for installation on different platforms

**Expected Test Failure**: Platform-specific installation tests for Windsurf/Kiro/Cursor will fail with "No installation bundle found" error even though bundles exist

**Complexity**: Hard - Requires understanding service interaction patterns, tracing data flow across 3 files, recognizing case-sensitivity issues in filename matching

---

### Bug #7: Authentication Token Lifetime Not Validated Across Command Chain (EXPERT - Multi-File)

**User Symptom Report**:
> "I authenticated with GitHub CLI yesterday and the extension worked fine. Today, when I try to install OLAF, it starts downloading but then fails mid-way with a 401 authentication error. If I run 'gh auth login' again and retry immediately, it works. It's like the token expires during the download but the extension doesn't check if it's still valid."

**Locations**:
- **File 1**: `vscode-extension/src/services/githubService.ts` (Line 66)
- **File 2**: `vscode-extension/src/commands/installCommand.ts` (Line 62)
- **File 3**: `vscode-extension/src/services/githubService.ts` (Line 415)

**Bug Type**: State Management / Token Validation Lifecycle

**Original Code**:

**File 1 - githubService.ts (Lines 63-97)**:
```typescript
private async getAuthHeaders(): Promise<Record<string, string>> {
    const headers: Record<string, string> = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'OLAF-VSCode-Extension/1.0.0'
    };

    // Always try to use authentication if we have GitHub CLI enabled or a token configured
    // This handles cases where repositories might be private even if not explicitly configured
    const shouldUseAuth = this.usePrivateRepo || this.useGitHubCli;
    
    if (shouldUseAuth) {
        let token = this.token;
        
        if (this.useGitHubCli && !token) {
            try {
                token = await this.getGitHubCliToken();
            } catch (error) {
                this.logger.error('Failed to get token from GitHub CLI', error as Error);
                // Only throw if private repo is explicitly enabled, otherwise continue without auth
                if (this.usePrivateRepo) {
                    throw new Error('GitHub CLI authentication failed. Please run "gh auth login" or provide a manual token.');
                } else {
                    this.logger.warn('GitHub CLI authentication failed, continuing without authentication');
                }
            }
        }
        
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
            this.logger.debug('Using authenticated GitHub API requests');
        } else if (this.usePrivateRepo) {
            throw new Error('No GitHub token available for private repository access');
        }
    }

    return headers;
}
```

**File 2 - installCommand.ts (Lines 62-69)**:
```typescript
// Validate access for private repos
const config = vscode.workspace.getConfiguration('olaf');
const usePrivateRepo = config.get<boolean>('usePrivateRepository');

if (usePrivateRepo) {
    const validation = await this.githubService.validateAccess();
    if (!validation.valid) {
        throw new Error(validation.message);
    }
}
```

**File 3 - githubService.ts (Lines 415-447)**:
```typescript
public async downloadBundle(bundleInfo: BundleInfo, onProgress?: (progress: number) => void): Promise<Buffer> {
    try {
        this.logger.info(`Downloading bundle: ${bundleInfo.filename} (${bundleInfo.size} bytes)`);
        const headers = await this.getAuthHeaders();
        
        // ... download logic
```

**Buggy Code**:

**File 1 - githubService.ts (Add caching on line 70 - after token retrieval)**:
```typescript
private async getAuthHeaders(): Promise<Record<string, string>> {
    const headers: Record<string, string> = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'OLAF-VSCode-Extension/1.0.0'
    };

    // Always try to use authentication if we have GitHub CLI enabled or a token configured
    // This handles cases where repositories might be private even if not explicitly configured
    const shouldUseAuth = this.usePrivateRepo || this.useGitHubCli;
    
    if (shouldUseAuth) {
        let token = this.token;
        
        if (this.useGitHubCli && !token) {
            try {
                token = await this.getGitHubCliToken();
                this.token = token;  // BUG: Cache the token but never invalidate it
            } catch (error) {
                this.logger.error('Failed to get token from GitHub CLI', error as Error);
                // Only throw if private repo is explicitly enabled, otherwise continue without auth
                if (this.usePrivateRepo) {
                    throw new Error('GitHub CLI authentication failed. Please run "gh auth login" or provide a manual token.');
                } else {
                    this.logger.warn('GitHub CLI authentication failed, continuing without authentication');
                }
            }
        }
        
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
            this.logger.debug('Using authenticated GitHub API requests');
        } else if (this.usePrivateRepo) {
            throw new Error('No GitHub token available for private repository access');
        }
    }

    return headers;
}
```

**File 2 - installCommand.ts (Remove validation on line 64-68)**:
```typescript
// Validate access for private repos
const config = vscode.workspace.getConfiguration('olaf');
const usePrivateRepo = config.get<boolean>('usePrivateRepository');

// BUG: Validation removed - token not checked before download
```

**File 3 - githubService.ts (No change in downloadBundle - but now uses potentially stale token)**:
```typescript
public async downloadBundle(bundleInfo: BundleInfo, onProgress?: (progress: number) => void): Promise<Buffer> {
    try {
        this.logger.info(`Downloading bundle: ${bundleInfo.filename} (${bundleInfo.size} bytes)`);
        const headers = await this.getAuthHeaders();  // Uses cached, potentially expired token
        
        // ... download logic continues with stale token
```

**Change Description**:
- **File 1 (githubService.ts)**: Added `this.token = token;` on line 76 to cache the token without expiry checking
- **File 2 (installCommand.ts)**: Removed the `validateAccess()` check on lines 64-68
- **File 3 (githubService.ts)**: No changes needed - inherits the bug from cached token

**Root Cause**: Token is fetched once and cached but never validated before reuse. The `validateAccess()` call was removed from the install command, so expired tokens aren't detected until the actual download fails. The token retrieved at startup could be hours old by the time download happens.

**Affected Test**: Integration test for long-running installation processes or tests with expired tokens

**Expected Test Failure**: Tests that simulate token expiration or long delays between authentication and download will fail with 401 errors during bundle download

**Complexity**: Expert - Multi-file state management bug, requires understanding of:
- Token lifecycle and caching patterns
- Service interaction timing
- Authentication flow across command → service → download chain
- Subtle race conditions between validation and usage
- Why removing validation in one place causes failures elsewhere

---

## Updated Bug Summary

| Bug # | Difficulty | Files Affected | Key Challenge |
|-------|------------|----------------|---------------|
| 1 | Easy | 1 | Single line logic error |
| 2 | Easy-Medium | 1 | Null safety |
| 3 | Medium | 1 | Cross-platform paths |
| 4 | Medium-Hard | 1 | Async concurrency |
| 5 | Hard | 1 | Algorithm complexity |
| **6** | **Hard** | **3** | **Cross-service consistency** |
| **7** | **Expert** | **3** | **State/lifecycle management** |

---

**Version**: 1.1  
**Last Updated**: 2025-10-06  
**Status**: Ready for Implementation
