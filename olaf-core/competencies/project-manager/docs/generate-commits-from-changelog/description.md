# Generate Commits from Changelog

## Overview

Generates meaningful git commit messages and structures from changelog entries and repository changes, ensuring consistency between project documentation and version control history.

## Purpose

Projects often have changes documented in changelogs but not yet committed to version control, or commits that don't align with documented changes. This competency solves the problem of documentation-code drift by analyzing changelog entries, mapping them to file changes, generating conventional commit messages, and creating a structured commit plan that maintains consistency between what's documented and what's versioned.

## Usage

**Command**: `generate commits from changelog`

**Protocol**: Propose-Act

**When to Use**: Use this competency when you have changelog entries that need to be committed to version control, when preparing a batch of related changes for commit, when you want to ensure commit messages follow conventions, or when you need to maintain consistency between changelog documentation and git history.

## Parameters

### Required Inputs
- None (competency will analyze current repository state)

### Optional Inputs
- **changelog_path**: Path to the changelog file (defaults to standard changelog register location)
- **repository_root**: Path to git repository root (defaults to current directory)
- **commit_strategy**: How to handle commit creation - "auto" or "interactive" (defaults to interactive for safety)
- **sign_commits**: Whether to GPG sign commits (defaults to false)

### Context Requirements
- Git repository with staged or unstaged changes
- Access to changelog register with recent entries
- Understanding of conventional commit message format
- Branch protection rules and commit policies

## Output

**Deliverables**:
- Commit plan with proposed commit messages mapped to files
- Conventional commit messages following type(scope): description format
- Grouped file changes organized by logical feature or fix
- Changelog entry references in commit messages
- Validation results against branch policies

**Format**: Markdown report with proposed commits, included files, generated messages, and changelog references, followed by interactive approval and execution.

## Examples

### Example 1: Feature Development Commits

**Scenario**: Completed OAuth authentication feature with multiple changelog entries

**Command**:
```
generate commits from changelog
```

**Input**:
```
Commit Strategy: interactive
```

**Result**: Generated 3 commits:
1. `feat(auth): implement OAuth2 provider integration` - includes auth service files, references changelog entry
2. `feat(auth): add user session management` - includes session handler files
3. `test(auth): add OAuth integration tests` - includes test files

### Example 2: Bug Fix Batch

**Scenario**: Fixed multiple bugs documented in changelog

**Command**:
```
generate commits from changelog
```

**Input**:
```
Commit Strategy: interactive
Sign Commits: true
```

**Result**: Generated 2 signed commits:
1. `fix(api): resolve memory leak in background processor` - includes processor files, references issue-789
2. `fix(ui): correct pagination display error` - includes UI component files, references issue-791

### Example 3: Documentation Updates

**Scenario**: Updated multiple documentation files

**Command**:
```
generate commits from changelog
```

**Result**: Generated 1 commit:
1. `docs: update API documentation for new pagination parameters` - includes all modified doc files, references changelog entry

## Related Competencies

- **create-changelog-entry**: Creates the changelog entries that this competency uses to generate commits
- **analyze-changelog-and-report**: Analyzes changelog to identify what should be committed
- **generate-professional-release-notes**: Uses commit history that this competency helps create
- **review-progress**: Progress reviews may identify uncommitted changes that need commits

## Tips & Best Practices

- Use interactive mode (default) to review and approve commits before they're created
- Ensure changelog entries are up to date before generating commits
- Follow conventional commit format (type(scope): description) for consistency
- Group related file changes into atomic commits - one logical change per commit
- Reference issue numbers and changelog entries in commit messages for traceability
- Review the commit plan carefully - automated grouping may need adjustment
- Use descriptive scopes that match your project structure (api, ui, auth, etc.)
- Sign commits when required by project policy or for security-sensitive changes
- Verify .gitignore rules are correct before committing to avoid including sensitive files

## Limitations

- Cannot automatically determine optimal commit grouping - may need manual adjustment
- Relies on changelog entries being accurate and complete
- Cannot detect all relationships between files - some grouping may be suboptimal
- Does not automatically resolve merge conflicts if they exist
- Cannot validate that commits will pass CI/CD checks before creating them
- Commit message quality depends on changelog entry quality
- Does not automatically push commits - pushing is a separate manual step
- Cannot automatically determine appropriate commit scopes - uses file paths as hints

**Source**: `olaf-core/competencies/project-manager/prompts/generate-commits-from-changelog.md`
