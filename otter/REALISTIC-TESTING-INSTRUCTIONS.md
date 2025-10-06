# Realistic Unit Testing Challenge

**Your Mission**: The InstallationManager service needs better test coverage. Recent bugs in production show gaps in testing.

**Context**: 
- Several bugs made it to production that should have been caught by unit tests
- Code coverage is low in critical areas
- New team members need examples of good testing practices
- Refactoring is risky without proper test coverage

**Rules**:
- Analyze the InstallationManager code to identify what needs testing
- Write unit tests that would have caught recent production issues
- Follow existing test patterns in the codebase
- Focus on areas most likely to break or cause user issues

---

## Recent Production Issues (What Tests Should Prevent)

### Issue #1: Directory Cleanup Failures
**What Happened**: Users reported leftover empty directories after uninstallation on Windows. Mac users didn't have this problem.

**Impact**: Cluttered project directories, user complaints about "incomplete" uninstalls.

### Issue #2: Metadata Corruption Crashes  
**What Happened**: Extension crashed when installation metadata files were corrupted or partially deleted.

**Impact**: Users couldn't uninstall or reinstall OLAF, had to manually clean up files.

### Issue #3: Permission Errors Not Handled
**What Happened**: Installation failed silently when users didn't have write permissions to target directories.

**Impact**: Users thought installation succeeded but OLAF wasn't actually installed.

### Issue #4: Race Conditions During Concurrent Operations
**What Happened**: Multiple simultaneous install/uninstall operations caused file corruption and inconsistent state.

**Impact**: Installations became corrupted, required manual cleanup.

### Issue #5: Path Handling Inconsistencies
**What Happened**: Mixed path separators caused issues on Windows, especially with deeply nested directories.

**Impact**: Files installed in wrong locations, cleanup failed to find files.

---

## Your Task

**Write unit tests that would catch these types of issues before they reach production.**

You need to:
1. **Analyze the codebase** to understand how these issues could occur
2. **Identify the specific methods/functions** that need testing
3. **Write comprehensive tests** covering normal operation and edge cases
4. **Focus on areas that impact users most** when they break
5. **Use proper mocking** for external dependencies (filesystem, etc.)

**What NOT to do**:
- Don't just test happy path scenarios
- Don't write tests that don't actually verify important behavior  
- Don't ignore cross-platform differences
- Don't skip error handling scenarios

---

## Test Organization

**Create test files in**: `vscode-extension/test/unit/services/`

**Suggested approach**:
- Group related tests logically
- Use descriptive test names that explain what they verify
- Include setup/teardown for test isolation
- Mock external dependencies appropriately
- Test both success and failure scenarios

---

## Success Criteria

**Your tests should**:
- Catch the types of bugs that made it to production
- Cover critical functionality that users depend on
- Be maintainable and easy to understand
- Run quickly and reliably
- Provide good error messages when they fail
