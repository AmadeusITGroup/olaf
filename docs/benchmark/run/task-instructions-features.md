# Feature Implementation Challenge

**Your Mission**: Implement 2 missing features for the OLAF VSCode Extension based on business requirements.

**Rules**:
- Read the business requirements carefully
- Design and implement the feature from scratch
- Follow the existing codebase patterns and architecture
- Write appropriate tests
- Each feature should be a separate commit

---

## Feature #1: Installation Status Report

### Business Requirement

**As a** VSCode extension user  
**I want** to check the current installation status of OLAF  
**So that** I can verify what version is installed, where it''s located, and whether it''s properly configured

### User Stories

1. **Check Installation Status**
   - User runs a command to check OLAF status
   - System displays: installation version, installation path, configuration status
   - If not installed, shows clear message

2. **Verify Installation Health**
   - User wants to confirm installation is not corrupted
   - System checks all required files exist
   - System reports any issues found

3. **View Configuration**
   - User wants to see current settings
   - System displays active configuration
   - Helps troubleshooting configuration issues

### Acceptance Criteria

**Status Display**:
- [ ] Show installed version number
- [ ] Show installation directory path
- [ ] Show platform information (VSCode/Windsurf/etc)
- [ ] Show configuration file location

**Health Check**:
- [ ] Verify installation directory exists
- [ ] Verify required files are present
- [ ] Check if metadata file is readable
- [ ] Report any corruption or missing files

**Error Handling**:
- [ ] Clear message if OLAF is not installed
- [ ] Handle corrupted/missing metadata gracefully
- [ ] Display user-friendly error messages

**Output Format**:
- [ ] Information should be well-formatted and readable
- [ ] Use consistent formatting with other extension commands
- [ ] Include helpful next steps if issues found

### Technical Considerations

- Command should be registered in extension activation
- Should integrate with existing InstallationManager service
- Should follow VSCode extension command patterns
- Consider using output channels or information messages for display
- Should handle edge cases (partial installation, corrupted files)

### Scoring

- **Design** (25 points): Architecture, code organization, pattern consistency
- **Implementation** (35 points): Functionality, completeness, error handling
- **Code Quality** (20 points): Readability, maintainability, TypeScript best practices
- **Testing** (20 points): Test coverage, edge cases

**Total**: 100 points

---

## Feature #2: GitHub Access Validation

### Business Requirement

**As a** developer using OLAF  
**I want** to validate my GitHub authentication before attempting installations  
**So that** I can fix authentication issues proactively instead of encountering errors mid-installation

### User Stories

1. **Validate Authentication**
   - User runs validation command
   - System checks if GitHub CLI is authenticated
   - System verifies token has required permissions

2. **Check Repository Access**
   - User wants to confirm access to OLAF repository
   - System attempts to access the repository
   - System reports success or specific access issues

3. **Troubleshoot Auth Problems**
   - User encounters installation failures
   - User runs validation to diagnose issue
   - System provides clear guidance on fixing auth problems

### Acceptance Criteria

**Authentication Check**:
- [ ] Verify GitHub CLI is installed
- [ ] Verify user is authenticated (valid token)
- [ ] Check token expiration if possible
- [ ] Verify token has repo read permissions

**Repository Access**:
- [ ] Test ability to access OLAF GitHub repository
- [ ] Verify can read release information
- [ ] Test API rate limits and quotas

**User Feedback**:
- [ ] Clear success message when all checks pass
- [ ] Specific error messages for each type of failure
- [ ] Provide actionable remediation steps
- [ ] Include links to authentication documentation

**Error Scenarios**:
- [ ] GitHub CLI not installed  Guide to installation
- [ ] Not authenticated  Guide to `gh auth login`
- [ ] Token expired  Guide to re-authentication  
- [ ] Insufficient permissions  Guide to permission scopes
- [ ] Repository not accessible  Check repo name/permissions
- [ ] Rate limit exceeded  Explain wait time

### Technical Considerations

- Should use existing GitHubService for API calls
- Command registered in extension activation
- Should validate token before making API calls
- Consider caching validation results with expiration
- Should not expose sensitive token information
- Follow security best practices for credential handling

### Scoring

- **Design** (25 points): Architecture, security considerations, service integration
- **Implementation** (35 points): Validation logic, error detection, completeness
- **Code Quality** (20 points): Security, error handling, code organization
- **Testing** (20 points): Mock GitHub API, test error scenarios

**Total**: 100 points

---

## Overall Scoring

**Total Possible**: 200 points

**Grading**:
- 180-200: A (Excellent implementation)
- 160-179: B (Good implementation)
- 140-159: C (Adequate implementation)
- 120-139: D (Needs improvement)
- <120: F (Incomplete)

**Bonus Points** (up to +20):
- Integration tests for both features (+10)
- Comprehensive documentation (+5)
- Error recovery mechanisms (+5)

---

**Tip**: Study the existing command patterns in the codebase before starting. Look at how other commands are structured and registered.
