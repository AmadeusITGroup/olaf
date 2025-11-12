---

name: create-person-record

description: Create a new person record following the standard template and update related indexes.

tags: [documentation, people, team]

---
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.

- **full_name**: string - Full name of the person

- **nickname**: string - (Optional) Preferred nickname

- **email**: string - Professional email address

- **role**: string - Current role in the project/organization

- **project_start_date**: date (YYYYMMDD) - When they joined the project

- **project_end_date**: date (YYYYMMDD) - (Optional) When they left the project

- **contact_guidance**: string - When and how to contact this person

- **areas_of_expertise**: string - List of skills and expertise areas

- **project_responsibilities**: string - Key responsibilities

- **preferred_contact_methods**: string - How to reach them

- **working_hours**: string - Time zone and availability

- **notes**: string - (Optional) Additional information



## Process



1. **Record Creation**:

   - Generate filename: `[role]-[name]-[date].md`

   - Create file in `[id:peoples_dir]`

   - Populate using `[id:competencies_dir][competency]/templates/project-manager/people-template.md`



2. **Documentation Updates**:

   - Add entry to `[id:people-register]`

   - Update team directory

   - Create changelog entry



3. **Validation**:

   - Verify all required fields

   - Check for existing records

   - Ensure consistent formatting



## Output/Result Format

Use `[id:competencies_dir][competency]/templates/project-manager/people-template.md` to structure the person record:

- Follow the template's sections for consistency

- Create file: `[id:peoples_dir][role]-[name]-[date].md`

- Register entry in `[id:people-register]`

- Changelog entry in `[id:changelog_register]`



## Output to USER

1. **Confirmation**:

   - Record creation status

   - File location

   - Assigned ID/reference



2. **Next Steps**:

   - Review instructions

   - Notification setup

   - Access permissions



## Domain-Specific Rules

- Rule 1: Follow privacy guidelines

- Rule 2: Maintain consistent formatting

- Rule 3: Keep contact info up-to-date

- Rule 4: Respect working hours

- Rule 5: Document changes



## Required Actions

1. Collect person details

2. Create record file

3. Update register

4. Document in changelog

5. Confirm completion



⚠️ **Critical Notes**

- Protect personal information

- Verify email format

- Document access controls

- Include emergency contacts

- Regular review schedule

