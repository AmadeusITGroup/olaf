# Generate Professional Release Notes

## Overview

Generates professional, user-friendly release notes by analyzing git commit history between two version tags, categorizing changes, transforming technical messages into clear descriptions, and producing comprehensive release documentation.

## Purpose

Software releases need clear communication about what changed, why it matters, and what users need to do. This competency solves the problem of technical, developer-focused commit messages by automatically analyzing git history, categorizing changes by type and impact, translating technical details into user benefits, and producing polished release notes suitable for various audiences.

## Usage

**Command**: `generate professional release notes`

**Protocol**: Propose-Act

**When to Use**: Use this competency when preparing for a software release, creating release announcements, documenting version changes for stakeholders, or whenever you need to communicate what changed between two versions in a clear, professional, user-focused format.

## Parameters

### Required Inputs
- **lower_tag**: Starting version tag for the release notes (e.g., v1.0.0, v2.3.1)
- **higher_tag**: Ending version tag for the release notes (e.g., v1.1.0, v2.4.0)
- **release_date**: Release date in YYYY-MM-DD format
- **project_name**: Name of the project or product
- **target_audience**: Intended readers (e.g., developers, end-users, administrators, technical stakeholders)

### Optional Inputs
- **release_theme**: Main theme or focus of this release (e.g., "Performance improvements", "Security hardening")
- **release_manager**: Name of the person managing the release
- **tag_link_base**: Base URL for linking to tags (e.g., https://github.com/org/repo/tree/)

### Context Requirements
- Git repository with commit history between the specified tags
- Access to git commands for analyzing commits, files, and contributors
- Understanding of commit message conventions used in the project
- Knowledge of breaking changes and migration requirements

## Output

**Deliverables**:
- Professional release notes document with sections for features, fixes, improvements, breaking changes
- User-friendly descriptions of changes with business value and impact
- Contributor acknowledgments
- Upgrade instructions and migration guidance
- Links to commits, pull requests, and issues for traceability

**Format**: Markdown document with emoji-enhanced sections, clear categorization, actionable upgrade instructions, and proper attribution.

## Examples

### Example 1: Minor Version Release

**Scenario**: Releasing v1.5.0 with new features and bug fixes

**Command**:
```
generate professional release notes
```

**Input**:
```
Lower Tag: v1.4.0
Higher Tag: v1.5.0
Release Date: 2025-10-27
Project Name: Customer Portal
Target Audience: end-users
Release Theme: Enhanced user experience and performance
Tag Link Base: https://github.com/company/customer-portal/tree/
```

**Result**: Generated release notes with 5 new features (dark mode, export functionality, etc.), 8 bug fixes, 3 performance improvements, contributor list, and simple upgrade instructions

### Example 2: Major Version with Breaking Changes

**Scenario**: Releasing v2.0.0 with significant architectural changes

**Command**:
```
generate professional release notes
```

**Input**:
```
Lower Tag: v1.9.5
Higher Tag: v2.0.0
Release Date: 2025-11-01
Project Name: Analytics API
Target Audience: developers
Release Theme: Modern architecture and improved scalability
Release Manager: Sarah Chen
```

**Result**: Comprehensive release notes highlighting 12 new features, 15 improvements, 3 breaking changes with detailed migration guide, deprecation notices, and step-by-step upgrade instructions

### Example 3: Patch Release

**Scenario**: Emergency patch release for security fix

**Command**:
```
generate professional release notes
```

**Input**:
```
Lower Tag: v1.4.2
Higher Tag: v1.4.3
Release Date: 2025-10-28
Project Name: Authentication Service
Target Audience: administrators
Release Theme: Security patch
```

**Result**: Focused release notes emphasizing security fix, impact assessment, urgency of upgrade, and minimal changes to other functionality

## Related Competencies

- **analyze-changelog-and-report**: Provides changelog analysis that can supplement git history analysis
- **generate-commits-from-changelog**: Ensures commits reference changelog entries for richer release notes
- **create-changelog-entry**: Changelog entries provide additional context for release note generation
- **create-decision-record**: Major architectural decisions can be referenced in release notes

## Tips & Best Practices

- Use semantic versioning tags (v1.2.3) for clear version identification
- Run the competency before the actual release to allow time for review and refinement
- Tailor language and technical depth to your target audience - developers need different details than end-users
- Include specific issue/PR numbers for traceability and credibility
- Highlight breaking changes prominently with clear migration instructions
- Acknowledge all contributors to build community and recognition
- Test upgrade instructions before publishing to ensure they're accurate
- Include metrics or performance improvements with specific numbers when available
- Link to detailed documentation for complex changes
- Review generated notes for accuracy - automated categorization may need adjustment

## Limitations

- Quality depends on commit message quality - vague commits produce vague release notes
- Cannot automatically determine user impact - requires human judgment for business value assessment
- Categorization is based on commit prefixes - inconsistent conventions reduce accuracy
- Cannot access external context like issue descriptions or PR discussions automatically
- Does not validate that upgrade instructions are complete or accurate
- Cannot automatically identify all breaking changes - relies on commit message indicators
- Generated descriptions may need refinement for specific audience needs

**Source**: `olaf-core/competencies/project-manager/prompts/generate-professional-release-notes.md`
