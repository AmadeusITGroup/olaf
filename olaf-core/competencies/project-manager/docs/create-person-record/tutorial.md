# Create Person Record: Step-by-Step Tutorial

**How to Execute the "Create Person Record" Competency**

This tutorial shows exactly how to create a new person record following the standard template and update related indexes for team member and stakeholder tracking.

## Prerequisites

- OLAF framework loaded and active
- Access to peoples directory
- Person record template available
- Understanding of privacy and data protection requirements

## Step-by-Step Instructions

### Step 1: Invoke the Competency
**User Action:**
1. Type: `olaf create person record`
2. Or use aliases: `olaf create person`, `olaf person record`, `olaf add contact`
3. Press Enter

**AI Response:**
Acknowledges request and begins gathering person information using Propose-Act protocol.

### Step 2: Provide Person Details
**User Provides Required Information:**
- **full_name**: "Jane Smith"
- **email**: "jane.smith@company.com"
- **role**: "Senior Developer"
- **project_start_date**: "20251001" (YYYYMMDD format)

**Optional Information:**
- **nickname**: "Jane"
- **project_end_date**: "20260930" (if applicable)
- **contact_guidance**: "Available Mon-Fri 9am-5pm EST, prefer email for non-urgent"
- **areas_of_expertise**: "OAuth 2.0, React, Node.js, PostgreSQL"
- **project_responsibilities**: "Lead OAuth implementation, mentor junior developers"
- **preferred_contact_methods**: "Email (primary), Slack (urgent), Teams (meetings)"
- **working_hours**: "9am-5pm EST (UTC-5)"
- **notes**: "On-call rotation: Week 1 of each month"

### Step 3: Record Creation
**What AI Does:**
1. Generates filename: `senior-developer-jane-smith-20251001.md`
2. Loads person template
3. Populates all sections with provided information
4. Creates file in peoples directory

**Filename Format:** `[role]-[name]-[date].md`

### Step 4: Documentation Updates
**What AI Does:**
- Adds entry to people register
- Updates team directory index
- Creates changelog entry documenting person record creation

### Step 5: Validation
**What AI Does:**
- Verifies all required fields populated
- Checks for existing records (duplicate detection)
- Ensures consistent formatting
- Validates email format
- Confirms privacy compliance

**You Should See:** Complete person record with all sections filled and confirmation of file creation.

## Verification Checklist

✅ **Person record file created** with correct naming
✅ **All required fields populated**
✅ **People register updated** with new entry
✅ **Changelog entry created**
✅ **Email format validated**
✅ **Privacy guidelines followed**
✅ **Template structure preserved**

## Troubleshooting

**If email format invalid:**
- Verify email follows standard format: name@domain.com
- Check for typos or special characters

**If duplicate record detected:**
- Review existing record
- Update existing instead of creating new
- Use different filename if intentional duplicate

**If template not found:**
Verify template at: `olaf-core/competencies/project-manager/templates/people-template.md`

## Key Learning Points

1. **Privacy First**: Person records follow data protection guidelines
2. **Structured Information**: Template ensures consistent contact information
3. **Traceability**: All person records tracked in register
4. **Working Hours Respect**: Documents availability to prevent off-hours contact

## Expected Timeline

- **Total time:** 3-5 minutes
- **User input:** 2-3 minutes for person details
- **AI execution:** 1-2 minutes for file creation and updates
