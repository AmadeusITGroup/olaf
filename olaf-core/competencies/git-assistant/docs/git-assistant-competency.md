# Git Assistant Competency Package

## Overview

The Git Assistant competency package provides advanced Git workflow management and branch operations. This competency focuses on complex Git operations that go beyond basic version control, particularly feature extraction, branch management, and automated workflow processes.

## Purpose

This competency was created by migrating Git-specific functionality from the developer competency package, providing a cleaner separation of concerns between code development tasks and Git workflow management.

## Competencies Available

### 1. Create Feature for PR (`create-feature-for-pr`)

**Protocol**: Propose-Confirm-Act  
**Description**: Extract features from integration branch to create a feature branch and PR to main

**Key Features**:
- Interactive branch selection from numbered lists
- Mandatory safety checks and clean working directory validation
- Interactive file selection for feature components
- Optional comprehensive feature documentation generation
- Automated PR material generation
- Branch cleanup and maintenance workflows

**Usage Examples**:
```bash
# Trigger the competency with any of these phrases:
"create feature"
"feature for pr" 
"extract feature"
"feature extraction"
"git feature"
```

**Workflow Overview**:
1. **Validation Phase**: Check Git status and discover available branches
2. **Branch Selection**: User selects source and target branches from numbered lists
3. **Feature Discovery**: Interactive identification of files that comprise the feature
4. **Documentation** (Optional): Generate comprehensive feature documentation
5. **Branch Creation**: Create feature branch from target and extract selected files
6. **PR Preparation**: Generate PR materials and GitHub compare URLs
7. **Cleanup**: Offer branch maintenance and cleanup options

## Safety Features

- **Mandatory commit staging**: Any modified files in source branch are automatically committed before extraction
- **Clean working directory validation**: Process stops if working directory has uncommitted changes
- **Branch protection**: Source branch cannot be main/master
- **User confirmation**: All destructive operations require explicit user confirmation
- **Rollback instructions**: Each major operation includes rollback guidance

## Integration with Other Competencies

While Git Assistant focuses on workflow management, it complements other competencies:

- **Developer competencies**: Use after code review and before PR submission
- **Project Manager competencies**: Coordinates with release planning and feature tracking
- **Common competencies**: Leverages file management and documentation utilities

## Future Competencies (Planned)

- `merge-branches`: Advanced merge strategies and conflict resolution
- `resolve-git-conflicts`: Interactive conflict resolution workflows  
- `manage-git-workflow`: Repository workflow configuration and management
- `create-hotfix-branch`: Emergency hotfix branch creation and deployment
- `prepare-release-branch`: Release preparation and versioning workflows
- `git-history-analysis`: Repository history analysis and cleanup
- `branch-protection-management`: Branch protection rule management

## Technical Requirements

- **Git Version**: 2.20.0 or higher
- **Platform**: Cross-platform (Windows, Linux, macOS)
- **Shell Support**: PowerShell, Bash, Zsh
- **Optional**: GitHub CLI for enhanced GitHub integration

## Best Practices

1. **Always use interactive selection**: Let users choose branches and files explicitly
2. **Validate before acting**: Check repository state before any operations
3. **Document the process**: Generate documentation for complex features
4. **Provide cleanup options**: Always offer to clean up temporary branches and states
5. **Follow conventional commits**: Use standard commit message formats
6. **Safety first**: Prioritize data safety over automation speed

## Migration Notes

This competency package was created by migrating `create-feature-for-pr` from the developer competency package on 2025-10-21. The migration improves the logical organization of OLAF competencies by separating Git workflow management from core development tasks.

## Support and Maintenance

This competency is maintained by the OLAF Framework Core Team. For issues, enhancements, or questions:

- **Repository**: https://github.com/Amadeus-xDLC/genai.olaf
- **Documentation**: This file and inline prompt documentation
- **Status**: Public Beta (suitable for general use with ongoing improvements)