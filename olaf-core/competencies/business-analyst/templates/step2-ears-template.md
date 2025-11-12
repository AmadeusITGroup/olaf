# Step 2: Transform to EARS

Date: <YYYY-MM-DD HH:MM>
Source: <step1 file>
Process: EARS format transformation (automated)

## <Domain Name>

### <REQ-ID>: <Short Title>
Trigger: <When ...>
Condition: <If ...>
Response: <The system shall ...>
Measure: <Measurable acceptance (time/condition/log)>

Guidelines
- Use explicit Trigger / Condition / Response / Measure for every requirement.
- Normalize terminology and flags (short -x, long --flag).
- Avoid policy decisions here; Steps 3–5 will finalize them.

Concrete examples (from spec-windsurf-gpt5lr Step 2)

### REQ-CLI-012: Dry Run Mode
Trigger: When `--dry-run` is provided
Condition: User requests simulation of installation
Response: The system shall log all actions it would take without performing them and provide a summary
Measure: Dry run completes within 50% of actual operation time

### REQ-CONFIG-006: Orphan `--branch` Error
Trigger: When `--branch` is provided without `--registry-repo`
Condition: Only `--branch` is present
Response: The system shall exit with an error and guidance indicating `--registry-repo` is required when using `--branch`
Measure: Exit code non-zero; actionable message logged within 50ms
