# Git Assistant Competency Package

Advanced Git workflow management and branch operations for the OLAF Framework.

## Quick Start

```bash
# Extract a feature from integration branch
"create feature"
"extract feature" 
"feature for pr"
```

## What's Included

### Competencies
- **create-feature-for-pr**: Extract features from integration branch to create feature branch and PR

### Features
- 🔒 **Safety First**: Mandatory validation and clean working directory checks
- 🎯 **Interactive Selection**: Choose branches and files from numbered lists
- 📝 **Auto Documentation**: Optional comprehensive feature documentation generation
- 🔄 **Complete Workflow**: From feature identification to PR creation
- 🧹 **Cleanup Management**: Automated branch maintenance and cleanup options

## Usage Examples

### Basic Feature Extraction
```bash
User: "create feature for pr"
# 1. Select source branch (integration/development branch)
# 2. Select target branch (usually main/master)
# 3. Choose feature files interactively
# 4. Generate documentation (optional)
# 5. Create feature branch and PR materials
```

## Safety Guarantees

- ✅ Never operates on main/master as source branch
- ✅ Always commits work in progress before extraction
- ✅ Validates clean working directory before operations
- ✅ Provides rollback instructions for all operations
- ✅ User confirmation required for all destructive actions

## Requirements

- Git 2.20.0+
- Repository with push access
- Configured git user.name and user.email

## Documentation

See [docs/git-assistant-competency.md](docs/git-assistant-competency.md) for complete documentation.

## Status

**Public Beta** - Stable for general use with ongoing improvements.