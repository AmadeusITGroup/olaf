# OLAF Framework Condensation Prompt

## Task
Condense the OLAF framework steering files into a single optimized file maintaining all functionality while reducing size by 70-80%.

**MANDATORY REQUIREMENT**: The condensed framework MUST be completely self-sufficient and NEVER reference any files in `olaf-core/reference/`. It must contain all necessary components embedded within itself.

## Source Files to Process (STRICT LIST)
**CRITICAL**: ONLY process these exact files. Do NOT include any content from open editor files, templates, or other sources.

- `olaf-core/reference/team-delegation.md`
- `olaf-core/reference/query-competency-index.md` 
- `olaf-core/reference/memory-map.md`
- `olaf-core/reference/core-principles.md`

**EXCLUSIONS**: Exclude any files in the `.condensed` subdirectory from processing.

## Condensation Rules

### 1. Structure (Keep This Exact Order)
```
# OLAF Framework - Condensed
## Session Init
## Protocol Hierarchy & Execution
## Protocols  
## Memory Map
## Core Rules
## File References
## Behavior
## Competency Patterns→Workflow|Protocol
## Framework Validation
```

### 2. Compression Techniques
- **Competency Index**: Convert arrays to `pattern→workflow.md|Protocol` format - ONLY from `query-competency-index.md`
- **Memory Map**: Use `var=path/` format, remove examples - ONLY from `memory-map.md`
- **Protocols**: 1-line descriptions only - ONLY from `team-delegation.md`
- **Protocol Hierarchy**: Include a 5-step execution process with a user-consent gate before applying any matched competency workflow (even if protocol=Act)
- **Remove**: All examples, verbose explanations, metadata
- **Keep**: All functional mappings, rules, and execution methodology

**STRICT RULE**: Do NOT add any competencies, patterns, or content that is not explicitly present in the source reference files listed above.

### 3. XML Tag Preservation (CRITICAL)
- **MUST include ALL XML tags** from source files with their complete content
- Required tags: `<olaf-work-instructions>`, `<olaf-general-role-and-behavior>`, `<olaf-interaction-protocols>`, `<olaf-framework-validation>`, `<olaf-core-principles>`, `<olaf-session-initialization>`, `<olaf-protocol-hierarchy>`
- **Embed XML tags around relevant sections** - do not just reference them
- XML tags ensure prompt compatibility and prevent LLM confusion
- **MANDATORY**: All XML sections must emphasize self-sufficiency and never reference external olaf-core/reference files

**Example Structure:**
```markdown
# OLAF Framework - Condensed

<olaf-session-initialization>
## Session Init
**CRITICAL**: This condensed OLAF framework is completely self-sufficient and contains all necessary components. No additional files need to be loaded. You have everything required to operate effectively within this single document.
</olaf-session-initialization>

<olaf-protocol-hierarchy>
## Protocol Hierarchy & Execution
1. Session setup first (complete session-initialization)
2. Competency first (use embedded competency patterns below, match first 2-3 words)
3. User consent: confirm applying the matched competency workflow; proceed only on consent (even if protocol=Act)
4. Direct execution (tell USER workflow + protocol, then execute)
5. Request triage (ask clarification if no clear match)
</olaf-protocol-hierarchy>

<olaf-interaction-protocols>
## Protocols
- **Act**: Direct execution
- **Propose-Act**: Get agreement first  
- **Propose-Confirm-Act**: Plan→Review→Confirm→Execute
</olaf-interaction-protocols>

## Memory Map
- core_dir=my-repo/, ack_dir=olaf-core/, ads_dir=olaf-data/
- prompts_dir=[ack_dir]prompts/, tools_dir=[ack_dir]tools/

<olaf-core-principles>
## Core Rules
- Jobs: Only on explicit USER instruction
- Files: verb-entity-complement.md, kebab-case
- Timestamps: YYYYMMDD-HHmm CEDT
- Language: US English
</olaf-core-principles>

## File References
Format: [id:file_id] using memory-map IDs

<olaf-general-role-and-behavior>
## Behavior
Expert domain approach. Concise responses. No speculation. Reference sources.
</olaf-general-role-and-behavior>

## Competency Patterns→Workflow|Protocol
pattern1|pattern2→workflow.md|Protocol
[... all competency mappings ...]

<olaf-framework-validation>
## Framework Validation
**BEFORE ANY TASK**: This condensed framework contains all necessary components:
- Memory map with project structure and file ID mappings (embedded above)
- Core principles with behavioral rules (embedded above)
- Competency patterns with task mappings (embedded above)
- Interaction protocols (embedded above)
- General role and behavior guidelines (embedded above)

**All components are self-contained within this document. No external file access is required.**

**You MUST apply the embedded framework components and pay special attention to**:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
</olaf-framework-validation>

<olaf-work-instructions>
**BEFORE ANY TASK**: Apply the embedded olaf-general-role-and-behavior and olaf-interaction-protocols. Use the embedded competency patterns and memory map for navigation. This condensed framework is completely self-sufficient and contains all necessary components.
</olaf-work-instructions>
```

### 4. XML Tag Embedding Strategy
- **Wrap each section** with its corresponding XML tag from the source files
- **Session Init section** → wrap with `<olaf-session-initialization>`
- **Protocol Hierarchy section** → wrap with `<olaf-protocol-hierarchy>`
- **Protocols section** → wrap with `<olaf-interaction-protocols>`
- **Core Rules section** → wrap with `<olaf-core-principles>`
- **Behavior section** → wrap with `<olaf-general-role-and-behavior>`
- **Framework Validation section** → wrap with `<olaf-framework-validation>`
- **Add final wrapper** → `<olaf-work-instructions>` at the end with validation summary

### 5. Formatting Standards
- Competency patterns: `pattern1|pattern2→file.md|Protocol`
- File paths: `dir=[parent]subdir/` 
- References: `[id:file_id]` format only
- No markdown headers beyond ##
- No bullet points in competency section

### 6. Content Priorities (Keep/Remove)
**KEEP**: All competency mappings, protocols, file IDs, core rules, execution steps FROM SOURCE FILES ONLY
**REMOVE**: Examples, explanations, metadata, duplicate information, verbose descriptions
**NEVER ADD**: Content from open editor files, templates, or any files not in the source list above

### 7. Target Metrics
- Final size: ~3,500-4,000 characters
- Reduction: 70-80% from original
- All functionality preserved

## Output Location (CRITICAL)

**ONLY save to:** `olaf-core/reference/.condensed/olaf-framework-condensed.md`


## Execution Instructions

1. **Read ONLY the four source files listed above** - ignore all other context
2. **Extract competency mappings ONLY from `query-competency-index.md`** - do not infer or add any others
3. **Process according to compression rules** while maintaining strict fidelity to source content
4. **Validate final output** contains no content from outside the source files
5. **MANDATORY**: Ensure the condensed framework is completely self-sufficient and never references external olaf-core/reference files
6. **MANDATORY**: All XML sections must emphasize self-sufficiency and embedded components

**Action:** Create or replace `olaf-core/reference/.condensed/olaf-framework-condensed.md` with the condensed framework containing all XML tags, ONLY content from the specified source files, and mandatory self-sufficiency enforcement.