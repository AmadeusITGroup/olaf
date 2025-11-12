---

name: create-decision-record

description: Create a new decision record following the standard template and update related indexes.

tags: [documentation, decision-making, governance]

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

- **title**: string - Concise description of the decision

- **type**: enum[Architecture,Project,Business,Functional,People,Technical,Security,Other] - Type of decision

- **status**: enum[Proposed,Accepted,Replaced,Superseded] - (Optional) Decision status (default: Proposed)

- **context**: string - Background and problem statement

- **drivers**: string - Key factors influencing the decision

- **options**: string - Options considered with pros and cons

- **decision**: string - (Optional) Selected option if already determined

- **decision_makers**: string - Individuals responsible for the decision

- **stakeholders**: string - Affected parties and stakeholders



## Process



1. **Record Creation**:

   - Generate unique ID (DR-YYYYMMDD-NN)

   - Create file in `[id:decision_records_dir]`

   - Populate using `[id:decision-record-template]`



2. **Documentation Updates**:

   - Add entry to `[id:decision-records-register]`

   - Update relevant indexes

   - Create changelog entry



3. **Validation**:

   - Verify all required fields

   - Check for similar decisions

   - Ensure proper formatting



## Output/Result Format

Use `[id:competencies_dir][competency]/templates/project-manager/decision-record-template.md` to structure the decision record:

- Follow the template's sections for consistency

- Create file: `[id:decision_records_dir]YYYYMMDD-title-as-kebab-case.md`

- Register entry in `[id:decision-records-register]`

- Changelog entry in `[id:changelog_register]`



## Output to USER

1. **Confirmation**:

   - Record creation status

   - File location

   - Assigned decision ID



2. **Next Steps**:

   - Review instructions

   - Stakeholder notification

   - Follow-up actions



## Domain-Specific Rules

- Rule 1: Follow existing naming conventions

- Rule 2: Maintain cross-references

- Rule 3: Preserve decision history

- Rule 4: Ensure traceability

- Rule 5: Keep records up-to-date



## Required Actions

1. Generate decision ID

2. Create record file

3. Update register

4. Document in changelog

5. Confirm completion



⚠️ **Critical Notes**

- Never modify existing decisions

- Maintain audit trail

- Include all stakeholders

- Document assumptions

- Keep records concise

