# Create Feature for PR

## Overview

Extracts a complete feature from an integration branch and creates an isolated feature branch ready for pull request submission. This competency automates the complex workflow of identifying feature files, creating proper branch structure, and generating comprehensive PR materials.

## Purpose

When working in integration branches, multiple features often accumulate together, making it difficult to submit clean, focused pull requests. This competency solves the problem of feature isolation by:
- Identifying all files that comprise a specific feature
- Extracting those files to a clean feature branch based on the target branch
- Generating documentation and PR materials
- Maintaining proper git workflow hygiene

## Usage

**Command**: `create feature for pr` (or aliases: `create feature`, `feature for pr`, `feature branch`, `extract feature`, `feature extraction`, `git feature`)

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this when you have completed a feature in an integration branch and need to create a focused pull request to main/master. Ideal for teams practicing trunk-based development or feature branch workflows where integration branches accumulate multiple features.

## Parameters

### Required Inputs
- **source_branch**: The integration branch containing your feature (selected from numbered list, cannot be main/master)
- **target_branch**: The branch you want to merge into (selected from numbered list, typically main/master)
- **feature_name**: Name of the feature being extracted (used for branch naming)
- **feature_description**: Brief description of what the feature does (used in commit messages and PR materials)

### Optional Inputs
- **files_to_extract**: List of files comprising the feature (will be discovered interactively if not provided)

### Context Requirements
- Clean working directory (no uncommitted changes)
- Access to both source and target branches
- Git repository with proper remote configuration
- Commit permissions on the repository

## Output

**Deliverables**:
- New feature branch: `feature/[feature_name]` created from target branch
- Feature documentation: `docs/olaf-[feature_name].md` (optional, user decides)
- GitHub compare URL for PR creation
- PR title and description text ready for copy-paste
- Updated source branch with latest target branch changes

**Format**: 
- Feature branch pushed to origin
- Markdown documentation with Mermaid diagrams (if requested)
- Formatted PR materials following conventional commits

## Examples

### Example 1: Extract Authentication Feature

**Scenario**: You've built a complete authentication system in your integration branch and need to submit it as a PR to main.

**Command**:
```
olaf create feature for pr
```

**Interactive Flow**:
1. Select source branch: `integration-dev` (from numbered list)
2. Select target branch: `main` (from numbered list)
3. Provide feature name: `user-authentication`
4. Provide description: `Add JWT-based user authentication with login/logout`
5. Identify feature files: `src/auth/`, `src/middleware/auth.js`, `tests/auth.test.js`
6. Choose documentation: `yes`
7. Review and approve feature branch creation

**Result**: 
- Feature branch `feature/user-authentication` created and pushed
- Documentation generated at `docs/olaf-user-authentication.md`
- GitHub PR URL provided
- PR materials ready for submission

### Example 2: Quick Bug Fix Extraction

**Scenario**: You fixed a bug in your integration branch and want to submit it quickly without documentation.

**Command**:
```
olaf create feature for pr
```

**Interactive Flow**:
1. Select branches and provide feature details
2. Identify bug fix files: `src/utils/validation.js`, `tests/validation.test.js`
3. Choose documentation: `no` (skip for simple fixes)
4. Approve extraction

**Result**: 
- Feature branch created with bug fix files
- PR materials generated
- No documentation created (suitable for simple changes)

## Related Competencies

- **propose-commit-thread**: Use this to organize commits in your integration branch before feature extraction
- **merge-branch-with-safety**: Use this after PR approval to safely merge your feature branch back to target
- **developer/review-code**: Use this to review your feature code before creating the PR

## Tips & Best Practices

- Always commit or stash changes in your source branch before extraction (the competency will do this automatically)
- Choose descriptive feature names using kebab-case for clean branch naming
- Skip documentation for routine updates, bug fixes, or simple file changes
- Review the file list carefully - missing files will require manual addition later
- Keep feature branches focused on a single feature for easier review
- Update your integration branch with latest target after extraction to stay current

## Limitations

- Source branch cannot be main or master (safety constraint)
- Requires clean working directory before starting
- Cannot handle merge conflicts during file extraction (requires manual resolution)
- GitHub URL generation assumes standard GitHub repository structure
- Documentation generation requires user guidance for content quality
