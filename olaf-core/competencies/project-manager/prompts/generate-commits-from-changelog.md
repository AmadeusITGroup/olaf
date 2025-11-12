---
name: generate-commits-from-changelog
description: Generate meaningful Git commits from changelog entries and repository changes, ensuring consistency between documentation and version control.
tags: [git, commits, changelog, version-control, documentation]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **changelog_path**: string - (Optional) Path to the changelog file (default: `[id:changelog_register]`)
- **repository_root**: string - (Optional) Path to the Git repository root (default: current directory)
- **commit_strategy**: enum[auto,interactive] - (Optional) How to handle commit creation (default: interactive)
- **sign_commits**: boolean - (Optional) Whether to sign commits (default: false)

## Process

1. **Initial Analysis**:
   - Check for staged changes
   - Scan for modified, added, and deleted files
   - Identify untracked files that should be versioned

2. **Changelog Processing**:
   - Parse recent changelog entries
   - Group related changes logically
   - Map changes to affected files
   - Generate commit messages following conventions

3. **Change Analysis**:
   - Analyze file modifications
   - Group related files by feature/fix
   - Identify unassociated changes
   - Create additional commit proposals

4. **Commit Planning**:
   - Create commit plan with messages
   - Organize commits logically
   - Validate against branch policies
   - Ensure atomic commits

## Output/Result Format
- Markdown report with:
  - Proposed commit messages
  - Files to be included in each commit
  - Changelog references
  - Validation results

## Output to USER
1. **Commit Plan**:
   - List of proposed commits
   - Files included in each
   - Generated commit messages
   - Changelog references

2. **Review Options**:
   - Accept all commits
   - Modify individual commits
   - Regenerate messages
   - Abort operation

3. **Execution Summary**:
   - Commits created
   - Files included
   - Any warnings or errors

## Domain-Specific Rules
- Rule 1: Follow conventional commit messages
- Rule 2: Keep commits atomic and focused
- Rule 3: Reference changelog entries when possible
- Rule 4: Group related file changes together
- Rule 5: Validate against branch protection rules

## Required Actions
1. Analyze repository state
2. Process changelog entries
3. Group related changes
4. Generate commit messages
5. Execute commits after approval

## Commit Message Format
```
type(scope): concise description

Detailed explanation if needed

- List of changes
- Related to #issue
- BREAKING CHANGE: if applicable
```

## Supported Commit Types
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes
- refactor: Code refactoring
- perf: Performance improvements
- test: Test additions/modifications
- chore: Maintenance tasks

⚠️ **Critical Notes**
- Never commit sensitive information
- Always verify changes before committing
- Respect .gitignore rules
- Handle merge conflicts appropriately
- Provide clear error messages for failures
