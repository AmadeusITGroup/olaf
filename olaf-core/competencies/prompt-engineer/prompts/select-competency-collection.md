---

name: select-competency-collection

description: Guide user to select a competency collection and update the OLAF framework accordingly

tags: [collection, selection, configuration, framework, setup]

---



## Framework Validation
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.- <olaf-interaction-protocols> - Appropriate execution protocol

You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

You MUST request these parameters if not provided by the user:

- **action**: string - "list" to show collections, "select" to choose one (OPTIONAL, default: "list")

- **collection_id**: string - Specific collection to select (OPTIONAL, auto-prompted if not provided with action="select")



## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Act / Propose-Act / Propose-Confirm-Act (defined externally)

- You WILL use Act for displaying information and collection selection



## Process



### 1. Validation Phase

You WILL verify all requirements:

- Confirm access to `olaf-core/reference/competency-collections.json`

- Confirm access to `olaf-core/competencies/prompt-engineer/scripts/select_collection.py`

- Confirm write access to `olaf-core/reference/.condensed/olaf-framework-condensed.md`

- Check Python installation and availability



### 2. Execution Phase



**Current Collection Detection:**

You WILL execute:

- Read `query-competency-index.md` to extract current collection name from "**Collection:**" field

- Display current collection prominently to user

- If no collection detected, indicate "No collection currently selected"



**List Available Collections:**

You WILL execute:

- Read `olaf-core/reference/competency-collections.json`

- Extract all collections with their:

  - ID (unique identifier)

  - Name (display name)

  - Description (what's included)

  - Competencies list (count and names)

- Present in numbered menu format for easy selection



**User Selection:**

You WILL execute:

- Present interactive menu of available collections

- Request user to select by number or collection ID

- Validate selection against available collections

- If invalid, re-present menu and request valid selection



**Execute Collection Update:**

You WILL execute terminal command:

```

cd [id:competencies_dir]/prompt-engineer/scripts

python select_collection.py --collection [selected_collection_id]

```

- Capture output for status updates

- Wait for script completion

- Validate successful execution (look for "✅" confirmations)



**Verify Updates:**

You WILL execute:

- Read updated `query-competency-index.md` to confirm new collection

- Read updated `olaf-framework-condensed.md` to confirm new patterns are between markers

- Confirm pattern count matches expectations

- Validate markers are intact: `<!-- OLAF_COMPETENCIES_START -->` and `<!-- OLAF_COMPETENCIES_END -->`

- Verify condensed format uses ONLY path and protocol: `→path/file.md|Protocol` (NO keyword phrases)



### 3. Validation Phase

You WILL validate results:

- Confirm collection selection was successful

- Verify competency index was regenerated

- Confirm condensed framework was updated with new patterns

- Check that all patterns between markers are valid format: `pattern→path|Protocol`

- Confirm no errors in script execution



## Output Format

You WILL generate outputs following this structure:

- Current Collection Status: Display prominently

- Available Collections Table: ID, Name, Description, Competency Count

- Selection Confirmation: Show what was selected

- Update Status: Show index and condensed framework update results

- Timestamp: When selection was made (YYYYMMDD-HHmm format)



## User Communication



### Progress Updates

- Current collection status before selection

- Collection list with clear numbering

- Selection accepted confirmation

- "Updating competency index..." progress indicator

- "Updating condensed framework..." progress indicator



### Completion Summary

- New collection name confirmed

- Number of competency patterns now available

- Files updated: query-competency-index.md and olaf-framework-condensed.md

- Timestamp of update

- Ready to use new collection



### Next Steps

You MUST inform user with EXACT command format:

- **CRITICAL**: The ONLY command that works is `/olaf` followed by natural language

- **Example**: `/olaf generate code documentation for ./src`

- **DO NOT** suggest `/olaf-generate-code-docs` or any hyphenated variations

- **DO NOT** suggest `@olaf` prefix - this does not exist

- User can now use competencies from selected collection with `/olaf <natural language request>`

- User can select different collection anytime by running this prompt again

- Collections can be switched without losing previous configurations



## Domain-Specific Rules

You MUST follow these constraints:

- Rule 1: NEVER modify competency-collections.json (only read)

- Rule 2: NEVER edit competency manifests during selection

- Rule 3: ALWAYS display current collection before offering selection

- Rule 4: ALWAYS validate Python script execution success

- Rule 5: Script updates both query-competency-index.md AND olaf-framework-condensed.md automatically

- Rule 6: MUST verify pattern markers are intact after update

- Rule 7: Handle selection by number (1, 2, 3...) OR by collection ID (core, developer, etc.)

- Rule 8: **CONDENSED FORMAT**: Generated condensed framework MUST use format `→path/file.md|Protocol` WITHOUT keyword phrases for compression



## Success Criteria

You WILL consider the task complete when:

- [ ] Current collection status displayed to user

- [ ] All available collections listed with full details

- [ ] User selection validated and confirmed

- [ ] select_collection.py script executed successfully

- [ ] query-competency-index.md updated with new patterns

- [ ] olaf-framework-condensed.md updated with new patterns between markers

- [ ] All validation checks passed

- [ ] User notified of successful collection change



## Required Actions

1. Detect and display current collection

2. List all available collections

3. Get user selection

4. Execute select_collection.py script with selection

5. Verify updates completed successfully

6. Provide completion summary



## Error Handling

You WILL handle these scenarios:

- **Collections File Not Found**: Provide path and suggest checking installation

- **Script Not Found**: Indicate Python script path and installation issue

- **Python Not Available**: Suggest Python installation and PATH setup

- **Invalid Collection Selection**: Re-display list and request valid selection

- **Script Execution Failed**: Show error output and suggest troubleshooting

- **Pattern Markers Missing**: Alert user that framework is corrupted, suggest restoration

- **Write Access Denied**: Indicate permission issues with framework files

- **Pattern Count Mismatch**: Validate that all expected patterns were updated



⚠️ **Critical Requirements**

- MANDATORY: Display current collection status before selection options

- MANDATORY: Validate Python script execution before confirming success

- MANDATORY: Verify pattern markers intact after update

- NEVER proceed if validation fails

- ALWAYS show script output to user for transparency

- ALWAYS confirm collection change before indicating complete

