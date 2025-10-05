# Step-by-Step Tutorial: Creating a User Requirements Grooming System

## Overview

This tutorial guides you through creating a comprehensive user requirements grooming system for product owners. The system includes templates for clusterization and prioritization, plus a main orchestrating prompt that integrates with GitHub MCP server to analyze issues and create strategic roadmaps.

**Tutorial Duration:** 30-45 minutes  
**Difficulty Level:** Intermediate  
**Prerequisites:** Basic understanding of OLAF framework, file system navigation, and product management concepts

## What You'll Build

By the end of this tutorial, you'll have created:
- A clusterization template for grouping user requirements
- A prioritization template for strategic sequencing
- A main grooming prompt that orchestrates the entire process
- A complete workflow for transforming GitHub issues into prioritized roadmaps

## Prerequisites

### Required Knowledge
- [ ] Basic understanding of the OLAF framework structure
- [ ] Familiarity with Markdown formatting
- [ ] Understanding of product management concepts (user requirements, prioritization)
- [ ] Basic command line operations (mkdir, file navigation)

### Required Tools
- [ ] Access to OLAF framework directory structure
- [ ] Text editor or IDE for creating Markdown files
- [ ] Command line interface (PowerShell on Windows)
- [ ] GitHub MCP server (to be installed separately)

### Required Access
- [ ] Write permissions to `olaf-core/templates/` directory
- [ ] Write permissions to `olaf-core/prompts/` directory
- [ ] Access to existing OLAF templates for reference

## Step-by-Step Instructions

### Phase 1: Examine Existing Structure and Plan

#### Step 1: Explore the Current Template Structure

**Action:** Navigate to and examine the existing product-owner templates

**Commands:**
```powershell
# Navigate to the templates directory
cd "c:\Users\[username]\coderepos\olaf\olaf-core\templates\product-owner"

# List existing templates
dir
```

**Expected Output:**
```
create-product-vision.md
```

**Verification:** You should see the existing product vision template, which will serve as a reference for formatting and structure.

#### Step 2: Check Prompts Directory Structure

**Action:** Examine the prompts directory to understand the organizational pattern

**Commands:**
```powershell
# Navigate to prompts directory
cd "c:\Users\[username]\coderepos\olaf\olaf-core\prompts"

# List existing prompt categories
dir
```

**Expected Output:**
```
architect/
business-analyst/
developer/
project-manager/
[... other directories ...]
```

**Verification:** You should see multiple role-based directories but notice that `product-owner/` doesn't exist yet.

#### Step 3: Create Task Planning

**Action:** Create a mental or written plan for the four main tasks:
1. Create clusterization template
2. Create prioritization template  
3. Create product-owner prompts directory
4. Create main grooming prompt

### Phase 2: Create the Clusterization Template

#### Step 4: Create the User Requirement Clusterization Template

**Action:** Create a comprehensive template for grouping and analyzing user requirements

**Commands:**
```powershell
# Navigate to product-owner templates directory
cd "c:\Users\[username]\coderepos\olaf\olaf-core\templates\product-owner"

# Create the clusterization template file
New-Item -Name "user-requirement-clusterization-template.md" -ItemType File
```

**File Content:** Create a template with the following key sections:
- Clusterization metadata (date, repository, analyst)
- Clustering methodology and criteria
- Requirement clusters with vision alignment
- Duplicate analysis and handling
- Cross-cluster dependencies
- Statistics and recommendations

**Key Features to Include:**
- Table structures for organizing requirements by Issue ID, Title, Status
- Cluster characteristics documentation
- Vision alignment scoring
- Duplicate identification while preserving all entries
- Recommendations for product owner review

**Verification:** 
- [ ] File created successfully
- [ ] Template includes metadata section
- [ ] Clustering criteria are clearly defined
- [ ] Table structures are properly formatted
- [ ] Usage instructions are included

#### Step 5: Validate Clusterization Template Structure

**Action:** Review the template to ensure it follows OLAF conventions

**Check List:**
- [ ] File uses kebab-case naming convention
- [ ] Includes timestamp format specifications (YYYYMMDD-HHmm CEDT)
- [ ] Contains proper Markdown formatting
- [ ] Includes usage instructions and best practices
- [ ] Has OLAF framework attribution footer

### Phase 3: Create the Prioritization Template

#### Step 6: Create the User Requirement Prioritization Template

**Action:** Create a comprehensive template for prioritizing clustered requirements

**Commands:**
```powershell
# Create the prioritization template file
New-Item -Name "user-requirement-prioritization-template.md" -ItemType File
```

**Key Sections to Include:**
- Prioritization metadata and constraints
- Scoring criteria with weights
- Priority level classifications (Critical, Important, Beneficial, Future)
- Roadmap sequencing with phases
- Risk assessment and mitigation
- Alternative scenarios planning

**Strategic Features:**
- Constraint handling that can override analytical scoring
- Cross-priority dependency mapping
- Stakeholder impact analysis
- Success metrics definition
- Review and adjustment processes

**Verification:**
- [ ] Template includes constraint documentation
- [ ] Scoring methodology is clearly defined
- [ ] Priority levels are well-structured
- [ ] Roadmap phases have clear timelines
- [ ] Risk assessment section is comprehensive

### Phase 4: Create the Main Orchestrating Prompt

#### Step 7: Create Product-Owner Prompts Directory

**Action:** Create the missing directory structure for product-owner prompts

**Commands:**
```powershell
# Navigate to prompts directory
cd "c:\Users\[username]\coderepos\olaf\olaf-core\prompts"

# Create product-owner directory
mkdir "product-owner"
```

**Expected Output:**
```
Directory: C:\Users\[username]\coderepos\olaf\olaf-core\prompts

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         [date] [time]                     product-owner
```

**Verification:** 
- [ ] Directory created successfully
- [ ] Directory follows naming convention of other prompt directories

#### Step 8: Create the Main Grooming Prompt

**Action:** Create the orchestrating prompt that manages the entire grooming process

**Commands:**
```powershell
# Navigate to the new product-owner directory
cd "product-owner"

# Create the main prompt file
New-Item -Name "groom-user-requirements.md" -ItemType File
```

**Prompt Structure:** Create a comprehensive prompt with three main phases:

**Phase 1: Requirements Gathering**
- GitHub repository and product vision input collection
- Issue status filtering and validation
- GitHub MCP server integration for data extraction

**Phase 2: Clusterization**
- Product vision analysis and theme extraction
- Template application for requirement grouping
- Mandatory user review and approval checkpoint
- Duplicate identification and handling

**Phase 3: Prioritization**
- Strategic constraint collection from user
- Template application for scoring and sequencing
- Roadmap creation with risk assessment
- Final deliverable presentation

**Critical Features:**
- User interaction checkpoints
- Error handling for common issues
- Quality assurance checklist
- Clear success criteria definition

**Verification:**
- [ ] Prompt includes all three phases
- [ ] User review gates are mandatory
- [ ] GitHub MCP integration is properly specified
- [ ] Template references are correct
- [ ] Error handling is comprehensive

### Phase 5: Integration and Testing

#### Step 9: Verify File Structure and References

**Action:** Ensure all files are created correctly and reference each other properly

**Commands:**
```powershell
# Check templates directory
dir "c:\Users\[username]\coderepos\olaf\olaf-core\templates\product-owner"

# Check prompts directory  
dir "c:\Users\[username]\coderepos\olaf\olaf-core\prompts\product-owner"
```

**Expected File Structure:**
```
templates/product-owner/
├── create-product-vision.md
├── user-requirement-clusterization-template.md
└── user-requirement-prioritization-template.md

prompts/product-owner/
└── groom-user-requirements.md
```

**Verification Checklist:**
- [ ] All four files exist in correct locations
- [ ] File names follow kebab-case convention
- [ ] Template references in prompt are accurate
- [ ] Directory structure matches OLAF patterns

#### Step 10: Content Validation

**Action:** Review all created files for consistency and completeness

**Template Validation:**
- [ ] Both templates include proper metadata sections
- [ ] Timestamps use YYYYMMDD-HHmm CEDT format
- [ ] Usage instructions are clear and actionable
- [ ] OLAF framework attribution is included

**Prompt Validation:**
- [ ] All three phases are clearly defined
- [ ] User interaction points are explicit
- [ ] Template file paths are correct
- [ ] Prerequisites are clearly stated
- [ ] Success criteria are measurable

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: Directory Creation Fails
**Symptoms:** "Access denied" or "Path not found" errors
**Solutions:**
- Verify you have write permissions to the target directory
- Check that parent directories exist
- Use `-Force` parameter with mkdir command
- Run command prompt as administrator if necessary

#### Issue 2: Template References Don't Work
**Symptoms:** Prompt can't find template files
**Solutions:**
- Verify file paths match exactly (case-sensitive)
- Check that template files were created in correct directories
- Ensure file names use exact kebab-case format specified
- Validate directory structure matches OLAF conventions

#### Issue 3: Markdown Formatting Issues
**Symptoms:** Tables or formatting don't render correctly
**Solutions:**
- Ensure proper spacing around table separators
- Check that all table rows have same number of columns
- Validate Markdown syntax using a preview tool
- Remove any invisible characters or encoding issues

#### Issue 4: Missing Prerequisites
**Symptoms:** Process fails during execution
**Solutions:**
- Verify GitHub MCP server is installed and configured
- Check access to product vision document
- Ensure proper permissions for file creation
- Validate OLAF framework structure is complete

## Verification Checklist

### File Creation Verification
- [ ] `user-requirement-clusterization-template.md` exists in `templates/product-owner/`
- [ ] `user-requirement-prioritization-template.md` exists in `templates/product-owner/`
- [ ] `product-owner/` directory exists in `prompts/`
- [ ] `groom-user-requirements.md` exists in `prompts/product-owner/`

### Content Quality Verification
- [ ] All templates follow OLAF naming conventions
- [ ] Timestamps use correct YYYYMMDD-HHmm CEDT format
- [ ] Templates include comprehensive usage instructions
- [ ] Prompt includes all three required phases
- [ ] User review checkpoints are mandatory
- [ ] Error handling covers common scenarios

### Integration Verification
- [ ] Template file paths in prompt are accurate
- [ ] Directory structure matches OLAF patterns
- [ ] File references use correct relative paths
- [ ] All prerequisites are clearly documented

### Functional Verification
- [ ] Clusterization template supports duplicate identification
- [ ] Prioritization template handles strategic constraints
- [ ] Main prompt orchestrates complete workflow
- [ ] GitHub MCP integration is properly specified
- [ ] Product vision alignment is enforced throughout

## Expected Outcomes

### Immediate Results
After completing this tutorial, you will have:
- A complete user requirements grooming system
- Templates that can be reused across multiple projects
- A standardized process for transforming GitHub issues into strategic roadmaps
- Integration with GitHub MCP server for automated data extraction

### Long-term Benefits
- Consistent approach to requirements analysis across projects
- Improved product vision alignment in development planning
- Systematic handling of duplicate requirements
- Strategic constraint integration in prioritization decisions
- Comprehensive risk assessment in roadmap planning

## Next Steps

### Testing the System
1. **Prepare Test Data:** Identify a GitHub repository with relevant issues
2. **Install GitHub MCP Server:** Follow installation instructions separately
3. **Create Product Vision:** Use existing template to create a test product vision
4. **Execute Grooming Process:** Run through the complete workflow using your new prompt
5. **Validate Outputs:** Ensure clusterization and prioritization produce expected results

### Customization Options
- Adapt scoring criteria in prioritization template for your specific context
- Modify clustering criteria based on your product domain
- Add additional constraint types relevant to your organization
- Customize roadmap phases to match your development cycles

### Integration with Existing Workflows
- Connect with existing project management tools
- Integrate with continuous planning processes
- Align with existing product development methodologies
- Establish regular review cycles for roadmap updates

## Summary

You have successfully created a comprehensive user requirements grooming system consisting of:

1. **Clusterization Template** - Groups related requirements while preserving duplicates and ensuring product vision alignment
2. **Prioritization Template** - Provides strategic sequencing with constraint handling and risk assessment
3. **Main Grooming Prompt** - Orchestrates the complete three-phase process with GitHub integration

The system is now ready for use and can transform GitHub issues into strategic, prioritized roadmaps that align with your product vision while accommodating real-world constraints and dependencies.

---
*Tutorial created for OLAF Framework - Technical Writer Competencies*  
*Generated: 20251004-1045 Central European Time*  
*Source: Conversation Record 20251004-1042*
