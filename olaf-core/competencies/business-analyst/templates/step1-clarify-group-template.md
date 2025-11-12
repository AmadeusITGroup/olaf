# Step 1: Clarify & Group (Pre-EARS)

Date: <YYYY-MM-DD HH:MM>
Source: <path to raw rules>
Process: Clarify & Group (automated)

## Domains Identified
- <domain 1>
- <domain 2>
- <...>

---

## <Domain Name>
- <raw rule paraphrase 1>
- <raw rule paraphrase 2>

Gaps/Notes:
- <gap or open question>

---

## Identified Gaps & Questions
- <gap 1>
- <gap 2>

Notes
- Keep domain grouping concise.
- Do not pre-solve; avoid EARS formatting here.

Example (inspired by spec-github-sonnet4 Step 1)
- Configuration & Initialization: default config lookup, default registry fallback, branch hierarchy; errors for invalid seed/missing registry file
- Command Line Interface: -h/--help, -v/--version, -verbose, single-dash convention
- Registry & Collection Management: multi-registries, merge precedence, retries, warnings
- File Operations & Installation: temp download, file locks, copy flows, reference copy, simplification, index generation
- Version Control Integration: .git/info/exclude handling
- Multi-Repository Installation: scope, skip logic, global copy
- Configuration Precedence: CLI over config; mapping consistency

Identified Gaps & Questions example
- Error Recovery: partial install handling?
- Update Mechanism: upgrading existing installs?
- Rollback: revert failed installs?
- Validation: post-install integrity?
- Performance: large downloads?
- Security: signatures for downloads?
