# Core Agent Principles
<olaf-core-principles>
This document contains the mandatory, binding rules that  MUST be followed at all times. These principles are non-negotiable.

## 1. Job Creation

- **Jobs are created ONLY upon explicit USER instruction.** Do not create jobs for routine tasks, internal policies, or documentation.

## 2. Naming and Formatting Conventions

- **File Naming**: All files MUST follow the `verb-entity-complement.md` pattern (e.g., `create-decision-record.md`) using kebab-case style
- **Timestamp Format**: All timestamps in filenames or content MUST use the `YYYYMMDD-HHmm` format and the CEDT timezone
- **Language**: All communication and documentation MUST use US English
- **Encoding**: All text files MUST use UTF-8 encoding

## 3. Communication Standards

- **Be direct**: State actions without filler words ("absolutely", "excellent", "certainly", "Perfect!")
- **Be concise**: Avoid elaboration on thinking process or unnecessary commentary
- **Confirm completion**: Simply state "Done" or describe the action taken

## 4. Development Standards

- **Python**: Use Python 3.12+ with virtual environments for all new scripts
- **Git Operations**: Use `--no-pager` flag; warn if stuck in less pager; suggest git add/commit at logical completion points (end of tasks, session transitions, major milestones)
- **Document Creation**: Create documents ONLY when explicitly requested by USER

## 5. Enforcement Protocol

**VIOLATION CONSEQUENCES**: Any deviation from these principles MUST be immediately corrected. These are binding requirements, not suggestions.
</olaf-core-principles>
