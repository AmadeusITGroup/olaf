# UNTESTED Features Documentation

This file tracks features that have been implemented but require testing and validation before production use.

## Current UNTESTED Features

### 1. Angular Migration Framework (commit: cafc3dd)
**Status:** UNTESTED - Requires validation before production use
**Files:**
- olaf-core/prompts/angular-migration/ (entire directory)
- olaf-core/templates/bootstrap-angular-migration/

**Risk Level:** Medium
**Validation Required:** Test migration process on sample Angular project

### 2. Slash Command Management Utilities (commit: 07d1e5a)
**Status:** UNTESTED - Requires validation before production use  
**Files:**
- olaf-core/prompts/other-users/generate-slash-command-manifest.md
- olaf-core/prompts/other-users/repair-slash-manifest.md
- olaf-core/prompts/other-users/switch-slash-command.md

**Risk Level:** Low-Medium
**Validation Required:** Test slash command generation, repair, and switching workflows

## Testing Guidelines

Before using UNTESTED features:
1. Review the implementation thoroughly
2. Test in a safe, isolated environment
3. Validate against expected use cases
4. Document any issues or improvements needed
5. Update this file when testing is complete

## Promotion Process

When an UNTESTED feature is validated:
1. Remove from this list
2. Update commit message if needed (via follow-up commit)
3. Add to validated features documentation
4. Notify team of availability for production use