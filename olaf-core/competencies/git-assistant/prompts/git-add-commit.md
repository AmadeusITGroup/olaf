# Git Add and Commit - Git Assistant Competency

## Purpose

Intelligently handle git add and commit operations with proper staging analysis, meaningful commit messages, and staged file conflict resolution.

## Context

- User wants to add and commit changes
- Need to check for already staged files
- Generate meaningful commit messages based on changes
- Handle mixed staging scenarios properly

## Instructions

### 1. Analyze Current Git State

Check git status to understand the current situation:

```bash
git status --porcelain
```

Parse the output to identify staged files, unstaged files, and untracked files.

### 2. Handle Mixed Staging Scenarios

**Scenario A: Only unstaged/untracked files**
- Proceed with git add and commit

**Scenario B: Only staged files**
- Generate commit message for staged files
- Ask user about committing staged files first

**Scenario C: Both staged and unstaged files**
- Present options to user:
  1. Commit staged files first, then handle unstaged
  2. Add unstaged to staging and commit everything together
  3. Cancel to review changes

### 3. Generate Meaningful Commit Messages

Analyze changes and create context-aware commit messages:

- Single file: "Update [filename]: [description]"
- Multiple files: "Update [area]: [description]"
- New features: "Add [functionality]"
- Bug fixes: "Fix [issue]"
- Documentation: "Update documentation"
- Configuration: "Update configuration"

### 4. Interactive Workflow

- Generate initial commit message
- Show proposed message to user
- Allow user to approve, modify, or provide their own
- Execute with confirmation

### 5. Safety Checks

- Warn about large files (>10MB)
- Check for sensitive data patterns
- Validate commit message quality
- Show summary of changes

## Protocol

**Propose-Act**: Present staging analysis and commit plan, get user approval before executing.

## Success Criteria

- Proper staging conflict resolution
- Meaningful commit messages
- User control over the process
- Safety warnings when needed
- Clear feedback on results