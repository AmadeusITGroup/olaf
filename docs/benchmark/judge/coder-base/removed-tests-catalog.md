# Removed Unit Tests Catalog for Re-Implementation Testing

**Repository**: OLAF VSCode Extension  
**Purpose**: Test AI agent's ability to write comprehensive unit tests from specifications  
**Date Created**: 2025-10-06  
**Branch**: research-benchmark

## Overview

This document catalogs 10 unit tests that have been removed from the codebase. AI agents must re-implement these tests based on:
- Test specifications and requirements
- Function/method signatures
- Expected behavior descriptions
- Edge cases and error scenarios

## Test Catalog

---

## Test Suite #1: InstallationManager - Directory Cleanup Tests

**File**: `vscode-extension/test/unit/services/installationManager.pruneEmptyDirs.test.ts`

**Tests to Remove**: All tests (6 total)

### Test Specifications

#### Test #1: Remove Empty Directories After File Removal

**Test Name**: `should remove empty directories after file removal`

**Requirement**:
The `pruneEmptyDirs()` method should recursively remove all empty directories that were created during OLAF installation, after the installed files have been removed.

**Setup**:
- Create nested directory structure: `extracted/olaf-core/deep/nested/`
- Create installation metadata with files: `['olaf-core/deep/nested/file.txt', 'olaf-core/another.txt']`
- Files should NOT exist (simulating they were already deleted)

**Expected Behavior**:
- All empty directories should be removed: `nested/`, `deep/`, `olaf-core/`, `extracted/`
- Directories should be removed from deepest to shallowest
- Logger should record "Removed empty directory" messages

**Assertions**:
```typescript
assert.strictEqual(fs.existsSync(nestedDir), false, 'Nested directory should be removed');
assert.strictEqual(fs.existsSync(deepDir), false, 'Deep directory should be removed');
assert.strictEqual(fs.existsSync(olafCoreDir), false, 'olaf-core directory should be removed');
assert.strictEqual(fs.existsSync(extractionPath), false, 'Extraction path should be removed if empty');
// Verify logging
assert.strictEqual(removedDirLogs.length > 0, true, 'Should log removed directories');
```

---

#### Test #2: Preserve Directories Containing Other Files

**Test Name**: `should not remove directories that contain other files`

**Requirement**:
The `pruneEmptyDirs()` method should NOT remove directories that contain files other than the ones that were installed by OLAF.

**Setup**:
- Create directory structure: `extracted/olaf-core/deep/`
- Create metadata with installed files: `['olaf-core/deep/file.txt']`
- Create an ADDITIONAL file that should remain: `extracted/olaf-core/remaining.txt`

**Expected Behavior**:
- Empty `deep/` directory should be removed (no files remain)
- `olaf-core/` directory should remain (contains `remaining.txt`)
- `extracted/` directory should remain
- `remaining.txt` file should not be touched
- Logger should record "not empty, keeping" messages

**Assertions**:
```typescript
assert.strictEqual(fs.existsSync(nestedDir), false, 'Empty nested directory should be removed');
assert.strictEqual(fs.existsSync(olafCoreDir), true, 'olaf-core directory should remain (has remaining file)');
assert.strictEqual(fs.existsSync(extractionPath), true, 'Extraction path should remain');
assert.strictEqual(fs.existsSync(remainingFile), true, 'Remaining file should not be touched');
assert.strictEqual(keptDirLogs.length > 0, true, 'Should log kept directories');
```

---

#### Test #3: Handle Separate Metadata Directory

**Test Name**: `should handle metadata directory removal when separate from extraction`

**Requirement**:
When the metadata directory is separate from the extraction directory, both should be removed if empty.

**Setup**:
- Installation path (metadata): `tempDir/.olaf-user/`
- Extraction path (files): `tempDir/extracted/`
- Create metadata with empty `installedFiles: []`

**Expected Behavior**:
- Both directories should be removed (both are empty)
- Metadata file should be removed
- No errors should occur

**Assertions**:
```typescript
assert.strictEqual(fs.existsSync(extractionPath), false, 'Extraction path should be removed');
assert.strictEqual(fs.existsSync(installPath), false, 'Installation/metadata path should be removed');
```

---

#### Test #4: Handle Non-Existent Installation

**Test Name**: `should gracefully handle non-existent installation`

**Requirement**:
The method should handle the case where no installation exists without throwing errors.

**Setup**:
- No installation directory exists
- No metadata file exists

**Expected Behavior**:
- Should not throw any errors
- Should log a warning: "No installation found at: {path}"
- Should return gracefully

**Assertions**:
```typescript
const warningLogs = logs.filter(log => log.level === 'warn' && log.message.includes('No installation found'));
assert.strictEqual(warningLogs.length, 1, 'Should log warning about missing installation');
```

---

#### Test #5: Handle Corrupted Metadata

**Test Name**: `should handle corrupted metadata gracefully`

**Requirement**:
The method should handle corrupted metadata files without crashing.

**Setup**:
- Create installation directory
- Create metadata file with invalid JSON: `'invalid json content'`

**Expected Behavior**:
- Should not throw errors
- Should log warning: "Could not read installation metadata for pruning"
- Should continue execution (possibly with limited functionality)

**Assertions**:
```typescript
const warningLogs = logs.filter(log => log.level === 'warn' && log.message.includes('Could not read installation metadata'));
assert.strictEqual(warningLogs.length, 1, 'Should log warning about corrupted metadata');
```

---

#### Test #6: Helper Method - removeIfEmpty

**Test Name**: `removeIfEmpty should work correctly`

**Requirement**:
Test that the private `removeIfEmpty()` helper method correctly identifies and removes empty directories.

**Setup**:
- Create empty directory: `tempDir/empty/`
- Create metadata that references files that would have been in that directory

**Expected Behavior**:
- Empty directory should be removed
- Logger should record removal

**Assertions**:
```typescript
const removedLogs = logs.filter(log => log.message.includes('Removed empty directory'));
assert.strictEqual(removedLogs.length > 0, true, 'Should have removed empty directories');
```

---

## Test Suite #2: InstallationManager - pruneEmptyDirs Additional Tests

**Tests to Remove**: 4 additional tests from the same file

#### Test #7: Handle Deep Nesting (10+ levels)

**Test Name**: `should handle deeply nested directory structures`

**NEW TEST REQUIREMENT**:
The method should efficiently handle directory structures with 10+ levels of nesting without stack overflow or performance issues.

**Setup**:
- Create directory structure 15 levels deep
- Create metadata with files at various depths

**Expected Behavior**:
- All empty directories removed in correct order (deepest first)
- No stack overflow errors
- Completes in < 5 seconds

**Implementation Guide**:
```typescript
it('should handle deeply nested directory structures', async () => {
    // Create 15-level deep structure
    const basePath = path.join(tempDir, 'extracted');
    let currentPath = basePath;
    for (let i = 0; i < 15; i++) {
        currentPath = path.join(currentPath, `level${i}`);
    }
    await fs.promises.mkdir(currentPath, { recursive: true });
    
    // Create metadata
    const metadata = {
        installedFiles: ['level0/level1/.../level14/file.txt'],
        extractionPath: basePath,
        //...
    };
    
    // Act
    const startTime = Date.now();
    await installationManager.pruneEmptyDirs(InstallationScope.USER);
    const duration = Date.now() - startTime;
    
    // Assert
    assert.strictEqual(fs.existsSync(currentPath), false);
    assert.strictEqual(duration < 5000, true, 'Should complete in < 5 seconds');
});
```

---

#### Test #8: Handle Mixed Empty and Non-Empty Siblings

**Test Name**: `should correctly handle mixed empty and non-empty sibling directories`

**NEW TEST REQUIREMENT**:
When sibling directories exist (same parent), only empty siblings should be removed.

**Setup**:
```
extracted/
  ├── olaf-core/        (empty - should be removed)
  ├── olaf-data/        (has file - should remain)
  └── user-files/       (empty - should be removed)
```

**Expected Behavior**:
- `olaf-core/` removed
- `olaf-data/` remains
- `user-files/` removed
- `extracted/` remains (still has olaf-data)

---

#### Test #9: Handle Symlinks

**Test Name**: `should not follow or remove symlinked directories`

**NEW TEST REQUIREMENT**:
The method should detect symlinks and not follow them or attempt to remove them.

**Setup**:
- Create real directory with files
- Create symlink pointing to it in extraction path
- Metadata includes symlink path

**Expected Behavior**:
- Symlink should not be followed
- Target directory and files should remain
- Warning logged about symlink

---

#### Test #10: Handle Permission Errors

**Test Name**: `should handle permission errors gracefully`

**NEW TEST REQUIREMENT**:
When directory removal fails due to permissions, log error and continue.

**Setup**:
- Create directory
- Simulate permission error (make directory read-only on Windows, chmod 000 on Unix)

**Expected Behavior**:
- Error logged with directory path
- Other directories still processed
- No unhandled exceptions

**Implementation Guide**:
```typescript
it('should handle permission errors gracefully', async () => {
    const restrictedDir = path.join(tempDir, 'restricted');
    await fs.promises.mkdir(restrictedDir, { recursive: true });
    
    // Make directory read-only (platform-specific)
    if (process.platform === 'win32') {
        await fs.promises.chmod(restrictedDir, 0o444);
    } else {
        await fs.promises.chmod(restrictedDir, 0o000);
    }
    
    // Setup metadata...
    
    // Act
    await installationManager.pruneEmptyDirs(InstallationScope.USER);
    
    // Assert
    const errorLogs = logs.filter(log => log.level === 'error');
    assert.strictEqual(errorLogs.length > 0, true, 'Should log error');
    assert.strictEqual(errorLogs[0].message.includes('restricted'), true);
    
    // Cleanup - restore permissions
    await fs.promises.chmod(restrictedDir, 0o755);
});
```

---

## Implementation Guidance

### Test Framework Setup

**Required Imports**:
```typescript
import * as assert from 'assert';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import { InstallationManager } from '../../../src/services/installationManager';
import { InstallationScope } from '../../../src/types/platform';
```

**Mock Classes**:

```typescript
class MockLogger {
    private logs: Array<{ level: string; message: string; error?: Error }> = [];
    
    info(message: string): void { /*...*/ }
    warn(message: string): void { /*...*/ }
    debug(message: string, error?: Error): void { /*...*/ }
    error(message: string, error?: Error): void { /*...*/ }
    
    getLogs(): Array<{ level: string; message: string; error?: Error }> { /*...*/ }
    clearLogs(): void { /*...*/ }
}

class MockPlatformDetector {
    constructor(private testInstallPath: string) {}
    
    async detectPlatform() { return { platform: 'vscode' }; }
    
    getInstallationPath(platform: string, scope: InstallationScope): string {
        return path.join(this.testInstallPath, `.olaf-${scope}`);
    }
}
```

**Test Suite Setup**:

```typescript
describe('InstallationManager.pruneEmptyDirs Test Suite', () => {
    let tempDir: string;
    let installationManager: InstallationManager;
    let mockLogger: MockLogger;
    let mockPlatformDetector: MockPlatformDetector;

    beforeEach(async () => {
        // Create temporary directory
        tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'olaf-test-'));
        
        // Create mocks
        mockLogger = new MockLogger();
        mockPlatformDetector = new MockPlatformDetector(tempDir);
        
        // Create installation manager with mocks
        installationManager = InstallationManager.getInstance();
        (installationManager as any).logger = mockLogger;
        (installationManager as any).platformDetector = mockPlatformDetector;
    });

    afterEach(async () => {
        // Clean up temporary directory
        if (fs.existsSync(tempDir)) {
            await fs.promises.rm(tempDir, { recursive: true });
        }
    });

    // Tests go here
});
```

### Metadata File Format

```json
{
    "installedFiles": ["path/to/file1.txt", "path/to/file2.md"],
    "extractionPath": "/absolute/path/to/extraction",
    "scope": "user",
    "version": "1.0.0",
    "platform": "vscode"
}
```

### Key Testing Patterns

1. **Directory Creation**: Use `fs.promises.mkdir(path, { recursive: true })`
2. **File Creation**: Use `fs.promises.writeFile(path, content)`
3. **Existence Checks**: Use `fs.existsSync(path)`
4. **Log Verification**: Filter and count log entries by level and message content
5. **Cleanup**: Always remove temp directories in `afterEach()`

---

## Success Criteria for Re-Implementation

### Functional Completeness (40%)
- [ ] All 10 tests implemented
- [ ] All assertions present and correct
- [ ] All edge cases covered

### Code Quality (30%)
- [ ] Proper use of async/await
- [ ] Clean, readable test names
- [ ] DRY principle followed (helper functions for repetitive setup)
- [ ] Proper TypeScript typing

### Test Reliability (20%)
- [ ] Tests pass consistently (not flaky)
- [ ] Proper cleanup in afterEach
- [ ] No test interdependencies
- [ ] Isolated test environment (temp directories)

### Coverage (10%)
- [ ] Happy path tested
- [ ] Error conditions tested
- [ ] Edge cases tested
- [ ] Platform-specific scenarios considered

### Evaluation Rubric

| Score | Grade | Description |
|-------|-------|-------------|
| 90-100% | A | Production ready, comprehensive coverage |
| 80-89% | B | Good coverage, minor gaps |
| 70-79% | C | Basic coverage, needs improvement |
| 60-69% | D | Incomplete, significant gaps |
| <60% | F | Non-functional or minimal coverage |

---

## Files to Remove

Execute these commands to remove the test files:

```powershell
# Remove the test file
Remove-Item "c:\Users\ppaccaud\coderepos\olaf\vscode-extension\test\unit\services\installationManager.pruneEmptyDirs.test.ts" -Force
```

---

**Version**: 1.0  
**Last Updated**: 2025-10-06  
**Status**: Ready for Test Removal and Re-Implementation
