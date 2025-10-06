# Removed Features Catalog for Re-Implementation Testing

**Repository**: OLAF VSCode Extension  
**Purpose**: Test AI agent's ability to implement features from business requirements  
**Date Created**: 2025-10-06  
**Branch**: research-benchmark

## Overview

This document catalogs 2 complete features that have been removed from the codebase. Each feature includes:
- Complete business requirements (as a Business Analyst would write them)
- Acceptance criteria
- Technical specifications
- Original implementation details
- Associated tests to remove
- Success metrics for re-implementation

## Feature Catalog

---

## Feature #1: Version Information Display & Update Checking

### Business Requirements Document

**Feature Name**: Version Status and Update Management

**Feature ID**: OLAF-F001

**Priority**: High

**Business Owner**: Product Management

**Target Users**: Extension users (developers, data scientists, technical writers)

#### Executive Summary

Users need to easily view their current OLAF installation version and check if updates are available. This feature provides transparency about what version is installed, where it's installed, and whether newer versions exist, enabling users to keep their OLAF framework up-to-date.

#### User Stories

**US-001: View Current Version**
> As a user  
> I want to see which version of OLAF is currently installed  
> So that I can know if I'm using the latest features and bug fixes

**Acceptance Criteria**:
- Display version number for each installed scope (user/workspace/project)
- Show platform type (VSCode, Windsurf, Cursor, Kiro)
- Provide quick access to installation folder
- Handle cases where OLAF is not installed gracefully

**US-002: Check for Updates**
> As a user  
> I want to check if a newer version of OLAF is available  
> So that I can decide whether to update

**Acceptance Criteria**:
- Query GitHub releases for latest version
- Compare with currently installed version(s)
- Display clear update status for each scope
- Show version transition (e.g., "1.0.0 → 1.2.0")
- Provide option to update immediately
- Show meaningful message when already up-to-date

**US-003: Quick Update Access**
> As a user  
> I want to quickly initiate an update when one is available  
> So that I don't have to navigate through multiple menus

**Acceptance Criteria**:
- One-click update button from version display
- One-click update button from update check notification
- Progress indication during update process
- Success/failure notification after update

#### Functional Requirements

**FR-001: Version Display**
- Command: `olaf.showVersion`
- Must detect all installed scopes
- Must retrieve version from installation metadata
- Must display platform information
- Format: `{SCOPE}: v{VERSION} ({PLATFORM})`
- Example: `USER: v1.2.0 (vscode)`

**FR-002: Update Checking**
- Command: `olaf.checkUpdates`
- Must check GitHub API for latest release
- Must compare versions using semantic versioning
- Must handle multiple installed scopes independently
- Must provide detailed comparison

**FR-003: User Interface**
- Version display: Information message with action buttons
  - "Check for Updates" button
  - "Show Installation Folder" button
- Update notification: Information/warning based on status
  - "Update Now" button
  - "Show Details" button
- Update details: Side-by-side comparison table
- Help documentation: Webview panel with formatted content

**FR-004: Error Handling**
- Gracefully handle "OLAF not installed" scenario
- Handle GitHub API failures (network issues, rate limits)
- Handle corrupted installation metadata
- Provide actionable error messages with recovery options
- Log all errors for debugging

**FR-005: Help Documentation**
- Command: `olaf.showHelp`
- Display comprehensive help in webview
- Include:
  - What is OLAF
  - Available commands
  - Installation scopes explanation
  - Configuration options
  - Support links

#### Non-Functional Requirements

**NFR-001: Performance**
- Version display: < 2 seconds
- Update check: < 5 seconds (with network)
- Help display: < 1 second

**NFR-002: Reliability**
- Must handle network failures gracefully
- Must not corrupt existing installation
- Must validate data before display

**NFR-003: Usability**
- Clear, jargon-free messages
- Intuitive button labels
- Consistent with VSCode UI patterns
- Accessible to users with disabilities

**NFR-004: Maintainability**
- Singleton pattern for service instances
- Dependency injection for testability
- Clear separation of concerns
- Comprehensive logging

#### Dependencies

- `UpdateManager` service: Check for and apply updates
- `InstallationManager` service: Read installation metadata
- `Logger` service: Error logging and debugging
- GitHub API: Fetch release information
- VSCode API: UI components and commands

#### Technical Specifications

**File Location**: `vscode-extension/src/commands/statusCommand.ts`

**Class Structure**:
```typescript
export class StatusCommand {
    // Dependencies
    private readonly logger: Logger;
    private readonly updateManager: UpdateManager;
    private readonly installationManager: InstallationManager;
    
    // Public methods (commands)
    public async checkUpdates(): Promise<void>
    public async showVersion(): Promise<void>
    public async showHelp(): Promise<void>
    
    // Private helpers
    private async showUpdateDetails(updateChecks: any[]): Promise<void>
    private async showInstallationFolder(scope: any): Promise<void>
}
```

**Command Registrations**:
- `olaf.checkUpdates` → `statusCommand.checkUpdates()`
- `olaf.showVersion` → `statusCommand.showVersion()`
- `olaf.showHelp` → `statusCommand.showHelp()`

**User Interaction Flows**:

**Flow 1: Show Version**
1. User invokes "OLAF: Show Version"
2. System checks for installed scopes
3. If none: Show "not installed" with install option
4. If installed: Display version info for each scope
5. User can click "Check for Updates" or "Show Installation Folder"

**Flow 2: Check Updates**
1. User invokes "OLAF: Check for Updates"
2. System checks for installed scopes
3. If none: Show "not installed" with install option
4. System queries GitHub for latest release
5. System compares versions for each scope
6. If updates available: Show count and offer "Update Now"
7. If up-to-date: Show "all up-to-date" message

**Flow 3: Show Help**
1. User invokes "OLAF: Show Help"
2. System creates webview panel
3. System renders help content in markdown
4. User can read documentation

#### Edge Cases

1. **No internet connection**: Show friendly error, suggest checking connection
2. **GitHub API rate limit**: Inform user, suggest waiting or using token
3. **Corrupted metadata**: Attempt recovery, offer reinstall option
4. **Multiple scopes with different versions**: Show all, allow selective update
5. **Pre-release versions**: Handle version comparison correctly

#### Success Metrics

**Implementation Success**:
- [ ] All 3 commands implemented and registered
- [ ] All user stories' acceptance criteria met
- [ ] All error cases handled gracefully
- [ ] Help documentation complete and accurate
- [ ] Code follows project patterns and style
- [ ] Logging implemented for debugging

**Quality Metrics**:
- Response time < NFR targets
- Zero unhandled exceptions
- Clear, grammatically correct messages
- Consistent with VSCode UX patterns

---

### Original Implementation Details

**Files to Remove**:
1. `vscode-extension/src/commands/statusCommand.ts` (357 lines)
2. Command registrations in `vscode-extension/src/extension.ts`:
   - Line referencing `StatusCommand` import
   - Line registering `olaf.checkUpdates`
   - Line registering `olaf.showVersion`
   - Line registering `olaf.showHelp`

**Associated Tests to Remove**:
- None found (needs to be created as part of re-implementation)

**Key Implementation Details to Match**:

**Dependencies**:
```typescript
import * as vscode from 'vscode';
import { UpdateManager } from '../services/updateManager';
import { InstallationManager } from '../services/installationManager';
import { Logger } from '../utils/logger';
```

**Singleton Pattern**:
```typescript
constructor() {
    this.logger = Logger.getInstance();
    this.updateManager = UpdateManager.getInstance();
    this.installationManager = InstallationManager.getInstance();
}
```

**Progress Indicator Pattern**:
```typescript
await vscode.window.withProgress({
    location: vscode.ProgressLocation.Notification,
    title: 'Checking for updates...',
    cancellable: false
}, async () => {
    // Long-running operation
});
```

**Version Display Format**:
```
OLAF Installation Information:

USER: v1.2.0 (vscode)
WORKSPACE: v1.1.0 (vscode)
```

**Update Message Format**:
```
Updates available for 2 scopes:
- USER: 1.2.0 → 1.3.0
- WORKSPACE: 1.1.0 → 1.3.0
```

---

## Feature #2: GitHub Repository Access Validation

### Business Requirements Document

**Feature Name**: GitHub Repository Access Validation

**Feature ID**: OLAF-F002

**Priority**: High

**Business Owner**: DevOps/Security Team

**Target Users**: Extension users, IT administrators, security teams

#### Executive Summary

Users need to validate that their GitHub credentials and repository configuration are correct before attempting to install or update OLAF. This feature provides comprehensive diagnostics of GitHub connectivity, authentication, and repository access, helping users troubleshoot configuration issues proactively.

#### User Stories

**US-001: Validate Repository Access**
> As a user  
> I want to verify my GitHub repository configuration is correct  
> So that I can successfully install or update OLAF without errors

**Acceptance Criteria**:
- Check internet connectivity to GitHub
- Validate repository owner and name configuration
- Test authentication token (if configured)
- Verify repository access permissions
- Display clear pass/fail status for each check
- Provide actionable recommendations for failures

**US-002: Troubleshoot Authentication Issues**
> As a user with authentication problems  
> I want detailed diagnostics of what's wrong  
> So that I can fix my configuration without trial and error

**Acceptance Criteria**:
- Detect missing token for private repositories
- Identify invalid or expired tokens
- Distinguish between different error types (401, 403, 404)
- Provide step-by-step resolution guidance
- Link to relevant settings for quick fixes

**US-003: View Validation Report**
> As a user  
> I want to see a comprehensive validation report  
> So that I can share it with my team or support

**Acceptance Criteria**:
- Display results in markdown format
- Open in side-by-side view for reference
- Include all configuration details
- Include all check results with icons
- Include recommendations section
- Allow report to be saved or copied

#### Functional Requirements

**FR-001: Connectivity Check**
- Test basic internet connectivity
- Test GitHub API endpoint accessibility
- Timeout after 5 seconds
- Report: Connected / No connection

**FR-002: Configuration Validation**
- Read repository owner from settings
- Read repository name from settings
- Read private repository mode flag
- Read authentication token (if set)
- Display all current configuration

**FR-003: Access Validation**
- Call GitHub API to test repository access
- Use authentication if configured
- Detect response status codes:
  - 200: Success
  - 401: Unauthorized (bad/missing token)
  - 403: Forbidden (insufficient permissions)
  - 404: Not found (wrong repo or no access)
- Return detailed validation result

**FR-004: Results Display**
- Create markdown document with results
- Use icons for visual clarity:
  - ✅ for success
  - ❌ for failure
  - ❗ for warnings
- Display in side-by-side view
- Show notification summary

**FR-005: Recommendations Engine**
- Analyze validation results
- Generate contextual recommendations
- Provide specific commands to run
- Link to relevant documentation
- Offer quick actions (Open Settings)

**FR-006: User Interface**
- Command: `olaf.validateAccess`
- Progress notification during validation
- Success: Green checkmark notification
- Failure: Warning notification
- Action buttons:
  - "Open Settings"
  - "View Details" (already shown)

#### Non-Functional Requirements

**NFR-001: Performance**
- Complete validation in < 10 seconds
- Timeout network checks after 5 seconds
- Responsive UI during checks

**NFR-002: Security**
- Never log or display actual token value
- Only show "Configured" or "Not set" status
- Secure token handling

**NFR-003: Reliability**
- Handle all network error scenarios
- Never crash on invalid configuration
- Provide fallback values for missing config

**NFR-004: Usability**
- Clear, non-technical language
- Color-coded status indicators
- Actionable next steps
- Copy-friendly report format

#### Dependencies

- `GitHubService`: Repository access validation methods
  - `validateAccess()`: Test repository access
  - `checkConnectivity()`: Test GitHub connectivity
- `Logger`: Error logging
- VSCode API: Settings, UI components
- GitHub API: Repository access testing

#### Technical Specifications

**File Location**: `vscode-extension/src/commands/validateAccessCommand.ts`

**Class Structure**:
```typescript
export class ValidateAccessCommand {
    // Dependencies
    private readonly logger: Logger;
    private readonly githubService: GitHubService;
    
    // Public methods
    public async execute(): Promise<void>
    
    // Private helpers
    private async showValidationResults(results: ValidationResults): Promise<void>
}

interface ValidationResults {
    owner: string;
    repo: string;
    usePrivateRepo: boolean;
    hasToken: boolean;
    accessValid: boolean;
    accessMessage: string;
    connectivity: boolean;
}
```

**Command Registration**:
- `olaf.validateAccess` → `validateAccessCommand.execute()`

**User Interaction Flow**:

**Flow: Validate Access**
1. User invokes "OLAF: Validate Repository Access"
2. System shows progress notification
3. System reads configuration (20%)
4. System tests connectivity (40%)
5. System validates repository access (80%)
6. System analyzes results and generates recommendations (90%)
7. System displays markdown report in side panel (100%)
8. System shows notification summary
9. User can click "Open Settings" for quick fixes

#### Validation Report Format

```markdown
**Repository**: AmadeusITGroup/olaf
**Private Repository Mode**: Disabled
**Authentication Token**: Not set

**Connectivity**: ✅ Connected
**Repository Access**: ✅ Valid
**Details**: Successfully validated access to AmadeusITGroup/olaf

**✅ All checks passed!** Repository access is working correctly.
```

**Example Failure Report**:
```markdown
**Repository**: MyOrg/private-repo
**Private Repository Mode**: Enabled
**Authentication Token**: Not set

**Connectivity**: ✅ Connected
**Repository Access**: ❌ Invalid
**Details**: Authentication required for private repository

**❗ Recommendations**:
- Set your GitHub token: generate with `gh auth token`
- Configure token in VSCode settings: `olaf.githubToken`
```

#### Edge Cases

1. **No internet connection**: Show connectivity failure, skip access check
2. **Invalid repository name**: Show 404 error, suggest checking settings
3. **Expired token**: Show 401 error, suggest refreshing token
4. **Rate limited**: Show 403 error, suggest waiting or using different token
5. **Private repo without token**: Show clear error, explain requirement

#### Success Metrics

**Implementation Success**:
- [ ] Command implemented and registered
- [ ] All validation checks functional
- [ ] Comprehensive error handling
- [ ] Clear, actionable recommendations
- [ ] Markdown report displays correctly
- [ ] All edge cases handled

**Quality Metrics**:
- Validation completes in < 10 seconds
- All error scenarios handled gracefully
- Report is clear and professional
- Recommendations are accurate and helpful
- Zero sensitive data exposed

---

### Original Implementation Details

**Files to Remove**:
1. `vscode-extension/src/commands/validateAccessCommand.ts` (161 lines)
2. Command registration in `vscode-extension/src/extension.ts`:
   - Line referencing `ValidateAccessCommand` import
   - Line registering `olaf.validateAccess`

**Associated Tests to Remove**:
- None found (needs to be created as part of re-implementation)

**Key Implementation Details to Match**:

**Dependencies**:
```typescript
import * as vscode from 'vscode';
import { GitHubService } from '../services/githubService';
import { Logger } from '../utils/logger';
```

**Progress Pattern**:
```typescript
await vscode.window.withProgress({
    location: vscode.ProgressLocation.Notification,
    title: 'OLAF: Validating Repository Access',
    cancellable: false
}, async (progress) => {
    progress.report({ increment: 20, message: 'Step description...' });
    // Validation logic
});
```

**Markdown Document Pattern**:
```typescript
const doc = await vscode.workspace.openTextDocument({
    content: markdownContent,
    language: 'markdown'
});

await vscode.window.showTextDocument(doc, {
    preview: true,
    viewColumn: vscode.ViewColumn.Beside
});
```

**Notification with Actions**:
```typescript
vscode.window.showInformationMessage(
    '✅ Repository access validated',
    'Open Settings'
).then(selection => {
    if (selection === 'Open Settings') {
        vscode.commands.executeCommand('workbench.action.openSettings', 'olaf');
    }
});
```

---

## Implementation Guidance for AI Agents

### General Approach

1. **Read Requirements Thoroughly**: Understand all user stories and acceptance criteria
2. **Study Dependencies**: Review how to use `UpdateManager`, `InstallationManager`, `GitHubService`
3. **Follow Patterns**: Match the coding patterns shown in implementation details
4. **Handle Errors**: Implement comprehensive error handling for all scenarios
5. **Test Edge Cases**: Ensure all edge cases are handled gracefully
6. **Match UX**: Keep UI messages consistent with VSCode patterns

### Success Criteria for Re-Implementation

**Feature #1 (Version Status)**:
- [ ] All 3 commands work correctly
- [ ] Version display matches format specification
- [ ] Update checking compares versions correctly
- [ ] Help documentation displays in webview
- [ ] All error cases handled
- [ ] All user stories' acceptance criteria met
- [ ] Code follows TypeScript best practices

**Feature #2 (Validate Access)**:
- [ ] Command executes validation sequence
- [ ] All validation checks implemented
- [ ] Markdown report displays correctly
- [ ] Recommendations are contextual and accurate
- [ ] All error scenarios handled
- [ ] All user stories' acceptance criteria met
- [ ] Security requirements met (no token exposure)

### Evaluation Rubric

| Criteria | Weight | Scoring |
|----------|--------|---------|
| **Functional Completeness** | 40% | All acceptance criteria met |
| **Code Quality** | 20% | Follows patterns, clean code, TypeScript best practices |
| **Error Handling** | 20% | All edge cases handled, clear error messages |
| **User Experience** | 10% | Clear messages, intuitive flow, VSCode consistency |
| **Performance** | 10% | Meets NFR performance targets |

**Scoring Scale**:
- 90-100%: Production ready
- 80-89%: Minor issues, mostly functional
- 70-79%: Core functionality works, needs refinement
- 60-69%: Partial implementation, major gaps
- <60%: Incomplete or non-functional

---

**Version**: 1.0  
**Last Updated**: 2025-10-06  
**Status**: Ready for Feature Removal and Testing
