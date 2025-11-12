---
name: generate-professional-release-notes
description: Generate professional release notes by analyzing git commit history between two tags.
tags: [project-management, release-notes, git, documentation]
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read  the full 
.olaf/olaf-core/reference/.condensed/olaf-framework-condensed.md.


## Input Parameters
**REQUIRED**:
- `lower_tag`: string - The starting tag (inclusive) for the release notes (e.g., v1.0.0)
- `higher_tag`: string - The ending tag (inclusive) for the release notes (e.g., v1.1.0)
- `release_date`: string - Release date in YYYY-MM-DD format
- `project_name`: string - Name of the project
- `target_audience`: string - Intended audience (e.g., developers, end-users, administrators)

**OPTIONAL**:
- `release_theme`: string - Main theme or focus of this release
- `release_manager`: string - Name of the release manager
- `tag_link_base`: string - Base URL for tag links (e.g., https://github.com/org/repo/tree/)

## Process

1. **Gather Commit Information**:
   Execute these git commands to collect data:
   ```bash
   # Get commit range
   git log --pretty=format:"%h|%s|%an|%ad" --date=short {lower_tag}..{higher_tag}
   
   # Get detailed commits with bodies
   git log --pretty=format:"%h|%s|%b|%an|%ad" --date=short {lower_tag}..{higher_tag}
   
   # Get changed files
   git diff --name-status {lower_tag}..{higher_tag}
   
   # Get contributor stats
   git shortlog -sn {lower_tag}..{higher_tag}
   ```

2. **Categorize Commits**:
   - **Features**: "feat:", "feature:", "add:" prefixes or new functionality
   - **Enhancements**: "improve:", "enhance:", "optimize:", "update:" (non-breaking)
   - **Bug Fixes**: "fix:", "bug:", "resolve:", "correct:" prefixes
   - **Technical**: "refactor:", "chore:", "build:", "ci:", dependency updates
   - **Documentation**: "docs:", "documentation:", README updates
   - **Security**: "security:", "vulnerability:", CVE references
   - **Breaking**: "BREAKING CHANGE:", major version bumps
   - **Deprecations**: "deprecate:", "remove:", EOL notices

3. **Transform Messages**:
   Convert technical commit messages into user-friendly descriptions:
   ```
   Before: fix: resolve auth timeout issue
   After: Fixed authentication timeout that was causing users to be logged out prematurely
   ```

4. **Assess Impact**:
   For each change, identify:
   - User impact and benefits
   - Business value
   - Technical improvements
   - Required user actions

## Output Format

```markdown
# Release {higher_tag} - {release_theme}
**Release Date:** {release_date}  
**Tag:** [{higher_tag}]({tag_link_base}{higher_tag})

## Overview
[Concise summary of release highlights and impact]

## 🚀 New Features
- **Feature Name**: Description of user-visible functionality (#PR)

## 🐛 Bug Fixes
- **Fixed Issue**: Description of fix and impact

## 🛠️ Technical Improvements
- **Enhancement**: Description of technical improvement

## 🔄 Breaking Changes
- **Change**: Description of breaking change and migration steps

## 👥 Contributors
@user1, @user2

## 📝 Upgrade Instructions
[Clear, actionable steps for upgrading]
```

## Quality Standards

### Content Requirements
- Write for the target audience (technical/non-technical)
- Focus on user benefits, not just technical changes
- Include specific details and metrics when available
- Provide clear action items for users

### Style Guide
- Use present tense and active voice
- Be concise but informative
- Include issue/PR numbers for traceability
- Use consistent formatting and emoji

### Validation
- All commits must be accounted for
- Breaking changes must include migration guidance
- Contributors must be properly acknowledged
- Links must be valid and functional


