# Competency Pack Compliance Rules

- **R01 - Required Structure**
  - Root must contain: README.md
  - Folders must exist: prompts/, templates/, tools/, docs/

- **R02 - Prompt Filenames**
  - In prompts/ (recursively): filenames are lowercase kebab-case
  - 3–4 words max, hyphen-delimited
  - Note: "verb-entity-complement" is guidance only (not auto-validated)

- **R03 - Docs Structure**
  - docs/ contains README.md for the competency pack
  - For each manifest entry (by prompt filename stem): docs/<prompt-stem>/ contains description.md and tutorial.md

- **R04 - Manifest Presence & Format**
  - A manifest JSON exists at pack root (e.g., manifest.json)
  - Must conform to the competency manifest template structure (id, name, version, description, entry_points[] with file, protocol)

- **R05 - Entry Points Coverage**
  - Prefer explicit frontmatter: `role: orchestrator|workflow` (or tag contains `orchestrator`/`workflow`)
  - Fallback to filename/folder heuristics containing "orchestrator" or "workflow"
  - If any orchestrator/workflow detected (by role or heuristic): they MUST appear in manifest.entry_points
  - If none detected: ALL prompt files under prompts/ MUST appear in manifest.entry_points

- **R06 - Templates Referenced**
  - Any template referenced in prompts MUST exist under templates/
  - Every file in templates/ MUST be referenced by at least one prompt (mentioning filename/path)
  - Note: Inline templates inside prompts should be refactored to use files in templates/ (AI-assisted step)

- **R07 - Prompt Template Compliance (basic)**
  - Each prompt .md begins with YAML frontmatter including: name, description, tags
  - Protocol is NOT required in prompts (protocol decided in competency index)
  - Category optional (if used, keep consistent across the pack)

- **R08 - Tools Referenced**
  - Each non-markdown file in tools/ MUST be referenced in at least one prompt (ignore *.md)

- **R09 - Entry Points Valid Paths**
  - entry_points[*].file paths MUST point to existing prompts/*.md within this pack

- **R10 - Aliases & Protocol Sanity**
  - entry_points have non-empty id, description; protocol in {Act, Propose-Act, Propose-Confirm-Act}

Note: kb/ is optional and ignored by validator; place internal references (like this rules file) here.
