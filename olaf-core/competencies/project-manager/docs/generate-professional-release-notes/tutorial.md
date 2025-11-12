# Generate Professional Release Notes: Step-by-Step Tutorial

**How to Execute the "Generate Professional Release Notes" Competency**

This tutorial shows exactly how to generate professional release notes by analyzing git commit history between two tags.

## Prerequisites

- OLAF framework loaded and active
- Git repository with tagged releases
- Access to git command line
- Understanding of semantic versioning
- Knowledge of target audience (developers, end-users, administrators)

## Step-by-Step Instructions

### Step 1: Invoke the Competency
**User Action:**
1. Type: `olaf generate professional release notes`
2. Or use aliases: `olaf release notes`, `olaf create release notes`
3. Press Enter

**AI Response:**
Acknowledges request and begins gathering release parameters using Propose-Act protocol.

### Step 2: Provide Release Parameters
**User Provides Required Information:**
- **lower_tag**: "v1.0.0" (starting tag, inclusive)
- **higher_tag**: "v1.1.0" (ending tag, inclusive)
- **release_date**: "2025-10-27" (YYYY-MM-DD format)
- **project_name**: "OAuth Authentication Service"
- **target_audience**: "developers" or "end-users" or "administrators"

**Optional Information:**
- **release_theme**: "Enhanced Security and Performance"
- **release_manager**: "Jane Smith"
- **tag_link_base**: "https://github.com/org/repo/tree/"

### Step 3: Gather Commit Information
**What AI Does:**
Executes git commands to collect data:

```bash
# Get commit range
git log --pretty=format:"%h|%s|%an|%ad" --date=short v1.0.0..v1.1.0

# Get detailed commits with bodies
git log --pretty=format:"%h|%s|%b|%an|%ad" --date=short v1.0.0..v1.1.0

# Get changed files
git diff --name-status v1.0.0..v1.1.0

# Get contributor stats
git shortlog -sn v1.0.0..v1.1.0
```

**You Should See:** Progress updates as git data is collected.

### Step 4: Categorize Commits
**What AI Does:**
Analyzes commit messages and categorizes by type:

- **Features**: "feat:", "feature:", "add:" prefixes
- **Enhancements**: "improve:", "enhance:", "optimize:", "update:"
- **Bug Fixes**: "fix:", "bug:", "resolve:", "correct:"
- **Technical**: "refactor:", "chore:", "build:", "ci:"
- **Documentation**: "docs:", "documentation:"
- **Security**: "security:", "vulnerability:", CVE references
- **Breaking**: "BREAKING CHANGE:", major version bumps
- **Deprecations**: "deprecate:", "remove:", EOL notices

### Step 5: Transform Messages
**What AI Does:**
Converts technical commit messages into user-friendly descriptions:

**Before:** `fix: resolve auth timeout issue`
**After:** `Fixed authentication timeout that was causing users to be logged out prematurely`

**Transformation Rules:**
- Remove technical jargon for non-technical audiences
- Focus on user benefits and impact
- Add context and business value
- Include specific details and metrics

### Step 6: Assess Impact
**What AI Does:**
For each change, identifies:
- User impact and benefits
- Business value delivered
- Technical improvements made
- Required user actions (if any)

### Step 7: Generate Release Notes
**What AI Does:**
Creates structured release notes document:

```markdown
# Release v1.1.0 - Enhanced Security and Performance
**Release Date:** 2025-10-27  
**Tag:** [v1.1.0](https://github.com/org/repo/tree/v1.1.0)

## Overview
This release focuses on security enhancements and performance optimizations...

## 🚀 New Features
- **OAuth 2.0 Token Refresh**: Automatic token refresh prevents session expiration (#PR-156)
- **Multi-Factor Authentication**: Added support for TOTP-based MFA (#PR-162)

## 🐛 Bug Fixes
- **Fixed Authentication Timeout**: Resolved issue causing premature logouts (#PR-145)
- **Corrected Token Validation**: Fixed edge case in token expiry checking (#PR-151)

## 🛠️ Technical Improvements
- **Database Query Optimization**: Reduced auth query time by 40% (#PR-148)
- **Caching Layer**: Implemented Redis caching for session data (#PR-153)

## 🔄 Breaking Changes
- **Token Format Change**: JWT tokens now include additional claims. Update client libraries to v2.0+ (#PR-160)
  - Migration: Update client library dependency
  - Run migration script: `npm run migrate-tokens`

## 👥 Contributors
@jane-smith, @john-doe, @alice-dev

## 📝 Upgrade Instructions
1. Update client libraries to v2.0 or higher
2. Run database migrations: `npm run db:migrate`
3. Update environment variables (see UPGRADE.md)
4. Restart services in rolling fashion
```

### Step 8: Quality Validation
**What AI Does:**
- Verifies all commits accounted for
- Ensures breaking changes include migration guidance
- Confirms contributors properly acknowledged
- Validates all links functional
- Checks content appropriate for target audience

**You Should See:** Complete release notes document with all sections populated.

## Verification Checklist

✅ **All commits categorized** correctly
✅ **User-friendly descriptions** for target audience
✅ **Breaking changes documented** with migration steps
✅ **Contributors acknowledged** properly
✅ **Links validated** and functional
✅ **Impact assessment** included for major changes
✅ **Upgrade instructions** clear and actionable

## Troubleshooting

**If git commands fail:**
```bash
# Verify tags exist
git tag -l

# Check tag format
git show v1.0.0
git show v1.1.0
```

**If no commits found:**
- Verify tag range is correct
- Check that higher_tag is after lower_tag
- Ensure repository is up to date

**If categorization seems wrong:**
- Review commit message conventions
- Manually adjust categories as needed
- Update commit message patterns

## Key Learning Points

1. **Audience-Focused**: Content adapts to target audience (technical vs. non-technical)
2. **Comprehensive**: All commits accounted for with proper categorization
3. **Actionable**: Breaking changes include clear migration guidance
4. **Traceable**: Links to PRs and commits for detailed investigation

## Expected Timeline

- **Total time:** 10-15 minutes
- **User input:** 2-3 minutes for parameters
- **AI execution:** 8-12 minutes for git analysis and content generation
- **Commits processed:** ~100-200 commits per minute
