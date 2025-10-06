# Unit Test Writing Challenge

**Your Mission**: Write 10 missing unit tests for the OLAF VSCode Extension's InstallationManager service.

**Rules**:
- Analyze the InstallationManager code to understand what needs testing
- Write comprehensive unit tests using Mocha and Node.js assert
- Follow existing test patterns in the codebase
- Each test should be independent and isolated
- Mock external dependencies appropriately

---

## Test #1: pruneEmptyDirs - Basic Empty Directory Removal

**What to Test**: The `pruneEmptyDirs` method should remove empty directories from the filesystem.

**Scenario**: 
- Given a directory structure with some empty directories
- When pruneEmptyDirs is called
- Then all empty directories should be removed
- And non-empty directories should remain

**Test Requirements**:
- Create temporary test directory structure
- Include both empty and non-empty directories
- Verify correct directories are removed
- Verify non-empty directories remain
- Clean up test files after test completes

**Edge Cases to Consider**:
- Mixed empty/non-empty directory tree
- Nested empty directories
- Directory with only hidden files

---

## Test #2: pruneEmptyDirs - Handles Non-existent Directories

**What to Test**: The method should gracefully handle directories that don't exist.

**Scenario**:
- Given a path to a directory that doesn't exist
- When pruneEmptyDirs is called
- Then no error should be thrown
- And the method should return successfully

**Test Requirements**:
- Pass non-existent path to pruneEmptyDirs
- Verify no exceptions thrown
- Verify method completes without errors

---

## Test #3: pruneEmptyDirs - Handles Permission Errors

**What to Test**: The method should handle permission errors gracefully without crashing.

**Scenario**:
- Given a directory with restricted permissions (simulate permission error)
- When pruneEmptyDirs is called
- Then errors should be caught and logged
- And method should not crash

**Test Requirements**:
- Mock filesystem to simulate permission errors
- Verify error handling behavior
- Verify appropriate error logging
- Verify method continues/completes gracefully

---

## Test #4: pruneEmptyDirs - Removes Deeply Nested Empty Directories

**What to Test**: The method should correctly remove empty directories regardless of nesting depth.

**Scenario**:
- Given a deeply nested directory structure (5+ levels)
- With all directories empty
- When pruneEmptyDirs is called
- Then all nested empty directories should be removed
- In the correct order (deepest first)

**Test Requirements**:
- Create deep directory structure
- Verify all levels are removed
- Verify removal order is correct
- No "directory not empty" errors

---

## Test #5: pruneEmptyDirs - Preserves Non-empty Leaf Directories

**What to Test**: Directories containing files should never be removed.

**Scenario**:
- Given a directory structure where leaf directories contain files
- When pruneEmptyDirs is called
- Then directories with files are preserved
- And their parent directories are also preserved

**Test Requirements**:
- Create structure with files in leaf directories
- Verify directories with files remain
- Verify parent chain remains intact
- Verify only truly empty directories removed

---

## Test #6: Installation Metadata - Save and Load

**What to Test**: Installation metadata should be correctly saved to and loaded from disk.

**Scenario**:
- Given valid installation metadata (version, platform, paths)
- When metadata is saved using saveMetadata
- And then loaded using loadMetadata
- Then loaded data should match original data exactly

**Test Requirements**:
- Create test metadata object
- Save to temporary location
- Load from same location
- Verify all fields match
- Test with various metadata structures

---

## Test #7: Installation Metadata - Handle Corrupted Metadata File

**What to Test**: Loading corrupted or invalid metadata should not crash the extension.

**Scenario**:
- Given a corrupted metadata file (invalid JSON)
- When loadMetadata is called
- Then appropriate error is returned
- And no unhandled exceptions occur

**Test Requirements**:
- Create corrupted/invalid JSON file
- Attempt to load metadata
- Verify error handling
- Verify graceful failure
- Test multiple corruption scenarios (malformed JSON, wrong schema, etc.)

---

## Test #8: Installation Validation - Detect Missing Files

**What to Test**: Installation validation should detect when required files are missing.

**Scenario**:
- Given an installation directory with some files missing
- When installation is validated
- Then validation should fail
- And should report which files are missing

**Test Requirements**:
- Create partial installation structure
- Remove specific required files
- Run validation
- Verify validation detects missing files
- Verify error messages are helpful

---

## Test #9: Path Resolution - Cross-platform Path Handling

**What to Test**: Path utilities should work correctly on Windows and Unix-like systems.

**Scenario**:
- Given paths with different separators (/ and \)
- When paths are normalized/resolved
- Then results should be correct for current platform
- And paths should be usable by filesystem operations

**Test Requirements**:
- Test Windows-style paths (C:\Users\...)
- Test Unix-style paths (/home/user/...)
- Test mixed separators
- Mock different platforms if needed
- Verify normalized paths work correctly

---

## Test #10: Concurrent Operations - Race Condition Safety

**What to Test**: Multiple simultaneous operations should not cause race conditions or data corruption.

**Scenario**:
- Given multiple concurrent installation/uninstallation operations
- When operations run simultaneously
- Then no race conditions occur
- And data integrity is maintained
- And all operations complete successfully

**Test Requirements**:
- Simulate concurrent operations using Promise.all
- Test install + uninstall simultaneously
- Test multiple installs to different locations
- Verify no file corruption
- Verify proper locking/synchronization
- Verify all operations complete without errors

---

## Test File Organization

**Location**: `vscode-extension/test/unit/services/`

**Recommended Structure**:
```
installationManager.pruneEmptyDirs.test.ts  (Tests #1-5)
installationManager.metadata.test.ts         (Tests #6-7)
installationManager.validation.test.ts       (Test #8)
installationManager.paths.test.ts            (Test #9)
installationManager.concurrency.test.ts      (Test #10)
```

Or combine into fewer files if you prefer.

---

## Testing Best Practices

1. **Setup/Teardown**: Use `beforeEach` and `afterEach` for test isolation
2. **Temporary Files**: Create in temp directory, always clean up
3. **Mocking**: Mock external dependencies (filesystem, GitHub API, etc.)
4. **Assertions**: Use descriptive assertion messages
5. **Coverage**: Test happy path, error cases, and edge cases
6. **Independence**: Each test should run independently
7. **Speed**: Unit tests should be fast (no real network calls)

---

## Scoring

Each test has specific criteria:

| Test | Focus Area | Points |
|------|-----------|--------|
| #1 | Core functionality | 10 |
| #2 | Error handling | 8 |
| #3 | Error handling | 10 |
| #4 | Edge cases | 10 |
| #5 | Logic correctness | 10 |
| #6 | I/O operations | 10 |
| #7 | Robustness | 12 |
| #8 | Validation logic | 10 |
| #9 | Cross-platform | 12 |
| #10 | Concurrency | 18 |

**Total**: 110 points

**Grading**:
- 99-110: A (Excellent testing)
- 88-98: B (Good testing)
- 77-87: C (Adequate testing)
- 66-76: D (Needs improvement)
- <66: F (Incomplete)

**Bonus Points** (up to +15):
- All tests use proper mocking (+5)
- Exceptional edge case coverage (+5)
- Performance testing included (+5)

---

**Tip**: Look at existing test files in the codebase to understand the testing patterns, mocking strategies, and assertion styles used. Match that style for consistency.
