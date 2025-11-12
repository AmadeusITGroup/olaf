# Propose Commit Thread

## Overview

Analyzes your git changes, intelligently clusters them into logical commits, and executes a commit thread with interactive modification capabilities and GitHub issue integration. This competency transforms messy working directory changes into a clean, well-organized commit history.

## Purpose

Developers often accumulate many changes across multiple files before committing, making it difficult to create a clean, logical commit history. This competency solves the problem by:
- Automatically analyzing and categorizing all changes
- Clustering related changes into coherent commits
- Matching commits with relevant GitHub issues
- Providing interactive modification before execution
- Maintaining clean git history with detailed commit messages

## Usage

**Command**: `propose commit thread` (or aliases: `propose commit`, `commit thread`, `smart commit`, `cluster commits`, `interactive commit`, `staged commit`, `organize commits`, `commit workflow`)

**Protocol**: Propose-Confirm-Act

**When to Use**: Use this when you have multiple uncommitted changes that should be organized into separate logical commits rather than one large commit. Ideal for feature development sessions where you've modified multiple components, or when you want to maintain clean git history with focused commits.

## Parameters

### Required Inputs
- **repository_path**: Path to git repository (defaults to current working directory)

### Optional Inputs
- **include_github_issues**: Check for related GitHub issues (default: true)
- **commit_strategy**: "granular" or "feature-based" clustering (default: "feature-based")
- **auto_execute**: Execute commits automatically after approval (default: false)

### Context Requirements
- Valid git repository
- Uncommitted changes in working directory
- GitHub CLI installed (optional, for issue integration)
- Clean working directory (no merge conflicts)
- Commit permissions on repository

## Output

**Deliverables**:
- Structured commit proposal with interactive modification options
- Executed commit sequence in logical order
- Updated GitHub issues with commit references (if enabled)
- Clean working directory after execution
- Detailed git log with organized commit history

**Format**: 
- Interactive markdown proposal with user commands
- Git commits with detailed multi-line messages
- GitHub issue updates with commit links

## Examples

### Example 1: Feature Development Session

**Scenario**: You've spent the day building a new API endpoint, updating tests, and adding documentation. You have 15 modified files and want to organize them into logical commits.

**Command**:
```
olaf propose commit thread
```

**Analysis Result**:
```
Proposed Commit Thread:

Commit 1: Add user profile API endpoint
Files: src/api/profile.js, src/routes/profile.js
Related Issue: #142 - User profile management

Commit 2: Add profile endpoint tests
Files: tests/api/profile.test.js, tests/fixtures/users.json

Commit 3: Update API documentation
Files: docs/api-reference.md, README.md

Commit 4: Update configuration for new endpoint
Files: config/routes.json, config/permissions.json
```

**Interactive Modification**:
```
User: merge 1,2
[Commits 1 and 2 combined into single commit]

User: 3a
[Commit 3 approved]

User: execute
[All approved commits executed]
```

**Result**: 
- 3 well-organized commits created
- Issue #142 updated with commit references
- Clean git history ready for push

### Example 2: Bug Fix with Multiple Components

**Scenario**: You fixed a validation bug that required changes to utility functions, middleware, and tests.

**Command**:
```
olaf propose commit thread
```

**Result**: 
- Commit 1: Fix validation logic in utilities
- Commit 2: Update middleware to use fixed validation
- Commit 3: Add regression tests for validation bug
- All commits linked to bug tracking issue

## Related Competencies

- **create-feature-for-pr**: Use this after organizing commits to extract feature for PR
- **merge-branch-with-safety**: Use this to safely merge organized commits to target branch
- **developer/review-code**: Use this to review changes before committing

## Tips & Best Practices

- Use "feature-based" clustering for most development work (groups related functionality)
- Use "granular" clustering when you need very detailed commit history
- Review the proposed commit sequence carefully before executing
- Modify commit messages to add context that the AI might miss
- Split large commits if they contain multiple logical changes
- Enable GitHub issue integration to maintain traceability
- Commit infrastructure changes separately from business logic
- Use descriptive commit messages following conventional commits format

## Limitations

- Requires clean working directory (no merge conflicts)
- GitHub issue integration requires GitHub CLI installation
- Cannot automatically resolve complex file dependencies
- Commit clustering is based on heuristics and may need manual adjustment
- Does not support interactive rebase of existing commits
- Cannot modify already committed history
