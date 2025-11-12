# Create Decision Record: Step-by-Step Tutorial

**How to Execute the "Create Decision Record" Competency**

This tutorial shows exactly how to create a structured decision record following the OLAF framework template and update all related documentation.

## Prerequisites

- OLAF framework loaded and active
- Access to decision records directory (`olaf-data/product/documentations/decision-records/`)
- Decision record template available
- Understanding of decision types and statuses

## Step-by-Step Instructions

### Step 1: Invoke the Competency
Initiate the decision record creation process.

**User Action:**
1. Type: `olaf create decision record`
2. Or use any alias: `olaf decision record`, `olaf new decision`, `olaf dr`
3. Press Enter to start the process

**AI Response:**
The AI will acknowledge the request and begin gathering required information using the Propose-Confirm-Act protocol.

### Step 2: Provide Decision Details
**User Action:** Respond to prompts with decision information

**Required Parameters:**
- **title**: "Migrate authentication to OAuth 2.0"
- **type**: Select from: Architecture, Project, Business, Functional, People, Technical, Security, Other
- **context**: "Current basic auth is insecure and doesn't support SSO"
- **drivers**: "Security requirements, user experience, compliance needs"
- **options**: "1) OAuth 2.0 with PKCE, 2) SAML, 3) Keep basic auth with MFA"
- **decision_makers**: "@TechLead, @SecurityOfficer"
- **stakeholders**: "@DevTeam, @ProductOwner, @EndUsers"

**Optional Parameters:**
- **status**: Proposed (default), Accepted, Replaced, Superseded
- **decision**: Selected option if already determined

### Step 3: Review Proposed Decision Record
**What AI Does:**
- Retrieves current timestamp using terminal command
- Generates unique decision ID (format: DR-YYYYMMDD-NN)
- Loads decision record template
- Populates all sections with provided information
- Presents complete decision record for review

**You Should See:** 
A formatted decision record with all sections filled, including metadata, context, options analysis, and stakeholder information.

### Step 4: Confirm or Request Changes
**User Action:**
1. Review the proposed decision record carefully
2. Type "approved" or "yes" to proceed
3. Or request specific changes: "update the context section to include..."

**AI Response:**
If approved, AI will create the files and update registers. If changes requested, AI will revise and present again for confirmation.

### Step 5: Automatic Documentation Updates
**What AI Does:**
1. Creates decision record file: `olaf-data/product/documentations/decision-records/YYYYMMDD-title-as-kebab-case.md`
2. Updates decision records register with new entry
3. Creates changelog entry documenting the decision record creation
4. Verifies all cross-references are correct

**You Should See:** 
Confirmation message with file location, assigned decision ID, and summary of all updates made.

## Verification Checklist

✅ **Decision record file created** in correct directory with proper naming
✅ **Unique decision ID assigned** (DR-YYYYMMDD-NN format)
✅ **Decision records register updated** with new entry
✅ **Changelog entry created** documenting the action
✅ **All required fields populated** (title, type, context, drivers, options, decision makers, stakeholders)
✅ **Template structure followed** exactly

## Troubleshooting

**If decision ID conflicts occur:**
```bash
# Check existing decision records
ls olaf-data/product/documentations/decision-records/
```
The AI will automatically increment the sequence number to avoid conflicts.

**If template not found:**
- Verify template exists at: `olaf-core/competencies/project-manager/templates/decision-record-template.md`
- Check memory-map.md for correct path resolution

**If register update fails:**
- Ensure decision records register file exists
- Check file permissions
- Verify path in memory-map.md

## Key Learning Points

1. **Propose-Confirm-Act Protocol**: This competency uses a two-step confirmation process to ensure accuracy before creating permanent records.

2. **Unique ID Generation**: Decision IDs follow the DR-YYYYMMDD-NN format where NN is a sequence number for decisions created on the same day.

3. **Comprehensive Documentation**: Creating a decision record automatically updates multiple files (record, register, changelog) to maintain consistency across the project.

4. **Decision Traceability**: All decisions are tracked with stakeholders, decision makers, and timestamps for full audit trail.

## Next Steps to Try

- Create a follow-up decision that supersedes an existing one
- Link decisions to related jobs or tasks
- Review decision records register to see all project decisions
- Use decision records as input for architecture documentation

## Expected Timeline

- **Total process time:** 3-5 minutes
- **User input required:** 2-3 minutes to provide decision details and review
- **AI execution time:** 1-2 minutes for file creation and documentation updates
