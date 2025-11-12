---
name: condense-olaf-framework
description: Condense OLAF framework reference files into optimized single file
tags: [framework, optimization, compression, olaf]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm access to source reference files:
  - `olaf-core/reference/team-delegation.md`
  - `olaf-core/reference/memory-map.md`
  - `olaf-core/reference/core-principles.md`
- Verify NO files in `.condensed/` subdirectory are processed
- Check write access to output location

### 2. Execution Phase
You WILL execute following protocol requirements:

**Source Analysis:**
- Read ONLY the three specified source files
- Use `var=path/` format for memory map
- Keep all XML tags and embed them with relevant sections

**Core Logic:**
- Apply 70-80% compression while maintaining functionality
- Keep ALL functional mappings, rules, execution methodology
- Remove examples, verbose explanations, metadata
- Preserve ALL XML tags with complete content

**Output Structure:**
- **Session Initialization section (HARD-CODED):**
  ```
  <olaf-session-initialization>
  ## Session Initialization

  **CRITICAL FIRST STEP**: This condensed OLAF framework is completely self-sufficient and contains all necessary components.
  </olaf-session-initialization>
  ```
- Protocol Hierarchy & Execution (extracted from team-delegation.md)
- Interaction Protocols section (extracted from team-delegation.md)
- Memory Map section (extracted from memory-map.md)
- Core Principles section (extracted from core-principles.md)
- General Role and Behavior section (extracted from team-delegation.md)

- Framework Validation section

### 3. Validation Phase
You WILL validate the condensed framework:
- Confirms all XML tags are present and properly embedded
- Verifies no content added from outside source files
- Confirms compression achieved 70-80% reduction
- Checks final size is ~3,500-4,000 characters

## Output Format
You WILL generate outputs following this structure:
- Primary deliverable: Condensed framework file with all XML tags
- File location: `olaf-core/reference/.condensed/olaf-framework-condensed.md`
- Validation report: Compression statistics and content verification

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ONLY process the three source files specified
- Rule 2: Do NOT add any content from open editors or templates
- Rule 3: MUST preserve ALL XML tags with complete content
- Rule 4: Protocol Hierarchy MUST extract content from team-delegation.md source file
- Rule 5: All file references MUST use `[id:file_id]` format
- Rule 6: NO markdown headers beyond ##
- Rule 7: Target metrics: ~3,500-4,000 characters, 70-80% reduction

## Success Criteria
You WILL consider the task complete when:
- [ ] All three source files successfully read and analyzed
- [ ] XML tags from all source files extracted and embedded
- [ ] Memory Map converted to var=path/ format
- [ ] **Protocol Hierarchy extracted from team-delegation.md source file**
- [ ] **Session Initialization uses the hard-coded simplified version**
- [ ] **All content sourced from the three specified files only**
- [ ] Compression achieved 70-80% reduction from original
- [ ] All functionality preserved with NO feature loss
- [ ] Output saved to correct location
- [ ] Final size is ~3,500-4,000 characters
- [ ] Validation confirms no external content included

## Error Handling
You WILL handle these scenarios:
- **Source File Access Failed**: Provide clear error with file paths to verify
- **Permission Denied**: Explain need for write access to output location
- **Compression Target Missed**: Re-evaluate which content to remove while preserving functionality
- **XML Tags Missing**: Verify all tags are extracted and properly embedded
- **File Size Validation Failed**: Review compression techniques and remove verbose descriptions

⚠️ **Critical Requirements**
- MANDATORY: Process ONLY the three specified source files
- MANDATORY: Preserve ALL XML tags with complete content
- MANDATORY: Use hard-coded session initialization
- NEVER add content from external files or open editors
- NEVER sacrifice functionality for compression
- ALWAYS embed XML tags with relevant sections
- ALWAYS validate no external content in final output
- ALWAYS maintain 70-80% compression ratio
