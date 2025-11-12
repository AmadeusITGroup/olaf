# Professional Release Notes Template

## Release Information
- **Version**: {VERSION}
- **Release Date**: {RELEASE_DATE}
- **Tag**: [{TAG_NAME}]({TAG_LINK})
- **Release Manager**: {RELEASE_MANAGER}

## Overview
{BRIEF_SUMMARY_OF_RELEASE_THEME_AND_IMPACT}

##  New Features
{LIST_NEW_FEATURES_WITH_USER_IMPACT}
- **{FEATURE_NAME}**: {DESCRIPTION_OF_WHAT_USERS_CAN_NOW_DO} (#{PR_NUMBER})

##  Enhancements
{LIST_IMPROVEMENTS_TO_EXISTING_FEATURES}
- **{ENHANCEMENT_NAME}**: {SPECIFIC_IMPROVEMENT_WITH_METRICS} (#{PR_NUMBER})

##  Bug Fixes
{LIST_ISSUES_RESOLVED}
- **{BUG_DESCRIPTION}**: {WHAT_WAS_FIXED_AND_USER_IMPACT} (#{PR_NUMBER})

##  Technical Changes
{LIST_INTERNAL_IMPROVEMENTS_REFACTORING_DEPENDENCIES}
- **{TECHNICAL_CHANGE}**: {BRIEF_DESCRIPTION_AND_BENEFIT} (#{PR_NUMBER})

##  Documentation
{LIST_DOCUMENTATION_UPDATES}
- **{DOC_UPDATE}**: {WHAT_WAS_UPDATED_OR_ADDED} (#{PR_NUMBER})

##  Security
{LIST_SECURITY_RELATED_CHANGES}
- **{SECURITY_FIX}**: {VULNERABILITY_ADDRESSED} - {CVE_NUMBER} (#{PR_NUMBER})

##  Breaking Changes
{LIST_CHANGES_REQUIRING_USER_ACTION}
 **Action Required**: {DESCRIPTION_OF_REQUIRED_USER_ACTION}
- **{BREAKING_CHANGE}**: {WHAT_CHANGED_AND_MIGRATION_PATH} (#{PR_NUMBER})

##  Deprecations
{LIST_FEATURES_BEING_PHASED_OUT}
- **{DEPRECATED_FEATURE}**: {REPLACEMENT_AND_TIMELINE} (#{PR_NUMBER})

## Known Issues
{LIST_KNOWN_ISSUES_TO_BE_ADDRESSED}
- {ISSUE_DESCRIPTION} - Will be addressed in {FUTURE_VERSION}

## Upgrade Instructions
{STEP_BY_STEP_UPGRADE_INSTRUCTIONS}
1. {STEP_1}
2. {STEP_2}
3. {STEP_3}

## Migration Guide
{FOR_BREAKING_CHANGES_PROVIDE_DETAILED_MIGRATION_STEPS}

### Before (v{PREVIOUS_VERSION})
`
{OLD_CODE_EXAMPLE}
`

### After (v{CURRENT_VERSION})
`
{NEW_CODE_EXAMPLE}
`

## Performance Improvements
{QUANTIFIABLE_PERFORMANCE_GAINS}
- {IMPROVEMENT_DESCRIPTION}: {PERCENTAGE_OR_METRIC_IMPROVEMENT}

## Compatibility
{COMPATIBILITY_INFORMATION}
- **Supported Platforms**: {PLATFORM_LIST}
- **Minimum Requirements**: {REQUIREMENT_LIST}
- **Deprecated Support**: {DEPRECATED_PLATFORM_LIST}

## Contributors
{ACKNOWLEDGE_CONTRIBUTORS}
Thanks to the following contributors for their work on this release:
- @{USERNAME_1} - {CONTRIBUTION_DESCRIPTION}
- @{USERNAME_2} - {CONTRIBUTION_DESCRIPTION}

## Links
- [Full Changelog]({CHANGELOG_LINK})
- [Documentation]({DOCS_LINK})
- [Migration Guide]({MIGRATION_GUIDE_LINK})
- [Known Issues]({ISSUES_LINK})

---

## Template Usage Notes

### Categorization Guidelines
- **New Features**: Major functionality additions that provide new capabilities
- **Enhancements**: Improvements to existing features (performance, usability, etc.)
- **Bug Fixes**: Resolution of issues or incorrect behavior
- **Technical Changes**: Internal improvements, refactoring, dependency updates
- **Documentation**: Updates to guides, API docs, README files
- **Security**: Vulnerability fixes, security improvements
- **Breaking Changes**: Changes requiring user action or code modification
- **Deprecations**: Features being phased out with future removal timeline

### Writing Best Practices
- Use present tense ("Adds support for..." not "Added support for...")
- Focus on user impact rather than technical implementation
- Include specific metrics when possible (e.g., "50% faster", "reduces memory usage by 30%")
- Link to pull requests/issues for detailed context
- Use clear, jargon-free language for user-facing changes
- Provide concrete examples for complex changes

### Professional Standards
- Always include version, date, and tag information
- Categorize changes for easy scanning
- Highlight breaking changes prominently
- Provide upgrade instructions for complex releases
- Acknowledge contributors
- Include relevant links for additional information
