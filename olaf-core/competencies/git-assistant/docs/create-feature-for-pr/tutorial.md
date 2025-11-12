# Create Feature for PR: Step-by-Step Tutorial

## How to Execute the "Extract Features from Integration Branch to Create Feature Branch and PR"

This tutorial shows exactly how to reproduce the feature extraction workflow for creating clean feature branches and pull requests from integration branches.

## Prerequisites

- Git installed and configured on your system
- Access to the repository with appropriate permissions
- Integration branch with completed features ready for extraction
- Clean working directory (no uncommitted changes)
- GitHub repository access for PR creation (optional)

## Step-by-Step Instructions

### Step 1: Initiate Feature Extraction

[This step starts the OLAF feature extraction workflow]

**User Action:**

1. Invoke the create-feature-for-pr competency in OLAF
2. Ensure your working directory is in the target repository
3. Have a clear idea of the feature you want to extract

**OLAF Response:**

You should see OLAF validate the repository state and discover all available branches, presenting them as a numbered list for selection.

### Step 2: Select Source and Target Branches

**User Action:** Choose branches from numbered lists presented by OLAF

```bash
Select source branch (integration branch): [number]
Select target branch (typically main/master): [number]
```

**Provide Source/Target Selection:**

- **Source Branch**: Integration branch containing your completed feature (cannot be main/master)
- **Target Branch**: Main production branch where PR will be targeted (typically main/master)
- **Feature Name**: Descriptive name for your feature (e.g., "user-authentication", "payment-processing")
- **Feature Description**: Brief explanation of what the feature accomplishes

### Step 3: Feature File Identification

**What OLAF Does:**

- Switches to your selected source branch
- Pulls the latest changes
- **MANDATORY**: Stages and commits any modified files in source branch
- Lists current directory structure for file identification

**You Should See:** Current repository file structure displayed, allowing you to identify which files belong to your feature

### Step 4: Interactive File Selection

**User Action:** Identify and specify which files make up your feature

```bash
Example files selection:
- src/auth/authentication.js
- src/auth/login-form.jsx  
- tests/auth/auth.test.js
- docs/authentication-flow.md
```

**Provide File Selection:**

- **Complete File List**: All files that are part of your feature
- **Iterative Refinement**: Add or remove files as you identify more components
- **Final Confirmation**: Review and approve the complete file list before extraction

### Step 5: Documentation Decision

**User Action:** Decide whether to generate comprehensive feature documentation

```bash
Do you want to generate comprehensive feature documentation? (y/n)
```

**Documentation Options:**

- **YES**: OLAF generates `docs/olaf-[feature_name].md` with feature overview, workflow diagrams, and integration details
- **NO**: Skip documentation and proceed directly to branch creation (suitable for routine updates or simple changes)

### Step 6: Branch Creation and File Extraction

**What OLAF Does:**

- Switches to target branch and pulls latest changes
- Creates new feature branch: `feature/[feature_name]`
- Extracts selected files from source branch using `git checkout [source_branch] -- [file_path]`
- Stages all changes and commits with feature description
- Pushes feature branch to origin

**You Should See:** Confirmation of successful branch creation, file extraction, and push to remote repository

### Step 7: PR Preparation Materials

**What OLAF Does:**

- Generates GitHub compare URL for PR creation
- Creates PR title following conventional commits format
- Generates comprehensive PR description including feature overview, files changed, and testing instructions

**You Should See:** Complete PR materials ready for copy-paste into GitHub PR creation interface

## Verification Checklist

✅ **Feature branch created successfully** (`feature/[feature_name]` exists locally and remotely)

✅ **All selected files extracted** (files exist in feature branch with correct content)

✅ **Clean commit history** (single commit with descriptive message for the feature)  

✅ **GitHub compare URL provided** (functional link for PR creation)

✅ **PR materials generated** (title and description ready for use)

✅ **Source branch preserved** (original integration branch remains intact)

## Troubleshooting

**If source branch is main or master:**

```bash
Error: Source branch cannot be main or master
```

- Select a different integration/development branch as source
- Main/master should only be used as target branches

**If working directory is not clean:**

- OLAF will automatically stage and commit modified files in source branch
- This is mandatory and ensures clean feature extraction
- No manual intervention required

**If file not found in source branch:**

- Verify file paths are correct and files exist in selected source branch
- Use OLAF's file listing to identify available files
- Reselect files from the presented structure

**If GitHub compare URL doesn't work:**

- Verify repository has remote origin configured
- Check GitHub repository access permissions
- Manually create PR using branch name: `feature/[feature_name]`

## Key Learning Points

1. **Clean Feature Isolation:** Features are extracted as clean, focused units suitable for independent review and testing
2. **Automatic Safety Measures:** Source branch modifications are automatically committed before extraction to prevent data loss
3. **Flexible Documentation:** Documentation generation is optional and context-dependent (comprehensive for complex features, skipped for routine updates)

## Next Steps to Try

- Create GitHub PR using the provided compare URL and materials
- Test the feature branch independently to ensure functionality
- Update source integration branch with latest target branch changes
- Consider deleting local feature branch after PR is merged

## Expected Timeline

- **Total feature extraction time:** 3-8 minutes
- **User input required:** Branch selection, file identification, documentation decision
- **OLAF execution time:** Automated git operations, documentation generation, PR material creation