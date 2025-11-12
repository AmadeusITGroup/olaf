# Create Competency Package

## Context
You are helping a user package their developed prompts, scripts, templates, and related work into a self-contained OLAF competency package. This creates a modular, reusable component that can be shared, maintained, and integrated independently.

## Input Requirements
- Competency name (kebab-case, e.g., "pdf-analysis", "code-review-automation")
- List of files to include (prompts, scripts, templates, examples)
- Dependencies on other competencies (if any)
- External tool requirements (if any)
- Brief description of competency purpose
- Classification type (kernel, common, or plugins)
- Target user types (primary and secondary)
- Maintenance team assignment
- LLM requirements and tool dependencies

## Workflow Steps

### Phase 1: Competency Structure Creation
1. **Create Competency Directory Structure**
   ```
   olaf-core/competencies/{competency-name}/
   ├── README.md                    # Quick start guide
   ├── docs/
   │   └── olaf-{competency-name}.md   # Complete documentation
   ├── prompts/                     # Competency prompts
   ├── templates/                   # Document templates
   ├── scripts/                     # Automation scripts
   ├── prereq/                      # Prerequisites management
   ├── dependencies.json            # All competency dependencies
   ├── examples/                    # Working examples
   └── tests/                       # Competency tests (optional)
   ```

2. **Create Core Files**
   - Competency README with quick start
   - Complete documentation in docs/
   - Prerequisites check and install scripts
   - Dependencies manifest

### Phase 1b: Present Files to User for Review

**CRITICAL STEP**: Before proceeding, you MUST present to the user:

1. **Prompts List** - With Entry Point Highlighting
   ```
   📋 PROMPTS TO INCLUDE:
   ✅ [ENTRY POINT] analyze-research-paper-comprehensive.md
      → This will be in competency index for user discovery
   
   ⚪ (support prompt) analyze-pdf-helper.md
      → Support prompt, not in entry_points
   ```

2. **All Other Files** - Organized by Category
   ```
   📄 TEMPLATES (2 files):
   • analysis-report-template.md
   • summary-template.md
   
   🔧 SCRIPTS (1 file):
   • scripts/extract-pdf-content.ps1
   
   📚 EXAMPLES (3 files):
   • examples/research-paper-analysis/
   • examples/quick-summary-extraction/
   • examples/bulk-processing/
   ```

3. **Confirmation Step**
   - Display total count: "Total package contains: 2 entry-point prompts + 1 support prompt + 2 templates + 1 script + 3 examples"
   - Ask user: "Proceed with packaging these files? (yes/no)"
   - If user says no, allow them to add/remove files

### Phase 2: Content Organization

1. **Move and Organize Files**
   - Copy prompts to `prompts/` folder
   - Move templates to `templates/` folder
   - Organize scripts in `scripts/` folder
   - Create examples from test results
   - Document all file locations

2. **Update File References**
   - Fix relative paths in scripts
   - Update documentation links
   - Ensure self-contained references

### Phase 3: User Confirmation - File Summary Display

**BEFORE creating the manifest, you MUST:**

Present file organization to the user with clear categorization:

```text
📋 COMPETENCY PACKAGE SUMMARY

PROMPTS (To include in competency index):
  ✅ [ENTRY POINT - Primary] bootstrap-java-migration.md
  ✅ [ENTRY POINT - Secondary] run-java-migration.md

SUPPORT FILES (Part of package but not discoverable via index):
  📄 Templates (2):
     • bootstrap-java-migration-plan-template.md
     • risk-assessment-template.md
  
  🔧 Scripts (3):
     • migration_common.py
     • migration-compatibility-analyzer.py
     • detect-risk-upgrade.py
  
  📚 Examples (2):
     • examples/spring-boot-2.7-to-3.0/
     • examples/jakarta-ee-migration/

TOTAL PACKAGE CONTENTS:
  • 2 discoverable prompts (entry points)
  • 2 template files
  • 3 helper scripts
  • 2 example directories
  • 1 manifest + docs
```

Get user confirmation: "Continue with this package? (yes/no)"

### Phase 3b: Dependencies Management
1. **Identify Dependencies**
   - Other OLAF competencies required
   - External tools needed
   - System requirements

2. **Create Dependencies File**
   - `dependencies.json` - All competency dependencies (competencies, external tools, system requirements)

### Phase 4: Prerequisites Management
1. **Create Check Script**
   - Verify external tools availability
   - Check competency dependencies
   - Validate system requirements

2. **Create Install Script**
   - Install external tools
   - Setup competency dependencies
   - Configure system requirements

### Phase 5: Documentation Creation
1. **Competency README**
   - Quick start instructions
   - Basic usage examples
   - Prerequisites summary
   - Link to full documentation

2. **Complete Documentation**
   - Competency overview and capabilities
   - Installation instructions
   - Usage examples and workflows
   - API/interface documentation
   - Troubleshooting guide
   - Integration with OLAF

3. **Examples Documentation**
   - Real usage examples
   - Input/output demonstrations
   - Performance metrics
   - Best practices

### Phase 6: OLAF Integration
1. **Update Framework**
   - Add competency patterns to condensed framework
   - Update memory map if needed
   - Register competency in competency index

2. **Create Competency Manifest**
   - Competency metadata
   - Version information
   - Compatibility requirements
   - Integration points

## Output Deliverables

### 1. Complete Competency Package
```
olaf-core/competencies/{competency-name}/
├── README.md
├── docs/olaf-{competency-name}.md
├── prompts/*.md
├── templates/*.md
├── scripts/*.ps1
├── prereq/
│   ├── check-prerequisites.ps1
│   └── install-prerequisites.ps1
├── dependencies.json
├── examples/
│   ├── README.md
│   └── example-*/
└── competency-manifest.json
```

### 2. Updated OLAF Framework
- Competency patterns added
- Memory map updated
- Competency registered

### 3. Clean Main Project
- Duplicate files removed
- Test files moved to examples
- References updated

## Dependencies File Format

### dependencies.json
```json
{
  "competencies": {
    "required": [],
    "optional": [
      {
        "name": "base-research",
        "version": ">=1.0.0",
        "reason": "Uses research competencies"
      }
    ]
  },
  "external_tools": {
    "required": [
      {
        "name": "pdftotext",
        "source": "MiKTeX",
        "version": ">=24.0",
        "platforms": ["windows", "linux", "macos"],
        "install_methods": {
          "windows": ["miktex", "chocolatey", "winget"],
          "linux": ["apt", "yum", "poppler-utils"],
          "macos": ["brew", "macports"]
        }
      }
    ],
    "optional": [
      {
        "name": "imagemagick",
        "reason": "Enhanced image processing"
      }
    ]
  },
  "system_requirements": {
    "os": ["windows", "linux", "macos"],
    "shell": ["powershell", "bash"],
    "disk_space": "100MB",
    "memory": "512MB",
    "network": false
  }
}
```

## Competency Manifest Format

### competency-manifest.json

⚠️ **CRITICAL: entry_points must contain ONLY TOP-LEVEL PROMPTS**

When selecting prompts for `entry_points`:

1. **Orchestrator/Workflow Prompts**: If a prompt orchestrates other prompts, include ONLY the orchestrator
2. **Fallback**: If no orchestrator exists, select the primary/highest-level prompts
3. **Guideline**: entry_points should typically contain 1-3 prompts maximum
4. **Exclude**: Templates, scripts, tools, and helper prompts must NOT be included in entry_points

```json
{
  "name": "pdf-analysis",
  "version": "1.0.0",
  "description": "Comprehensive PDF document analysis and processing",
  "author": "OLAF Framework",
  "created": "2025-10-19",
  "updated": "2025-10-19",
  "category": "document-processing",
  "tags": ["pdf", "analysis", "research", "extraction"],
  "competencies": [
    "analyze research paper comprehensive",
    "analyze pdf quick"
  ],
  "entry_points": [
    {
      "id": "analyze-research-paper",
      "file": "prompts/analyze-research-paper-comprehensive.md",
      "protocol": "Act",
      "description": "Comprehensive analysis of academic research papers with figure extraction and critical evaluation",
      "aliases": ["analyze research paper", "research paper analysis", "academic paper analysis"],
      "required": true
    },
    {
      "id": "analyze-pdf-quick",
      "file": "prompts/analyze-pdf-quick.md",
      "protocol": "Act",
      "description": "Quick PDF document analysis and summary extraction",
      "aliases": ["quick pdf analysis", "pdf summary", "quick document analysis"],
      "required": false
    }
  ],
  "compatibility": {
    "olaf_version": ">=1.6.0",
    "platforms": ["windows", "linux", "macos"]
  },
  "status": "experimental"
}
```

## Competency Status Values

All competencies must have a prominent status field indicating their maturity and readiness:

- **experimental**: Initial development, not production-ready, subject to significant changes
- **private-preview**: Limited release to specific stakeholders, feedback-driven development
- **public-preview**: Generally available for testing, approaching stability
- **ga** (General Availability): Stable, production-ready, full support
- **deprecated**: No longer recommended, pending removal, use alternative instead

**Default for new competencies**: Always start with `"status": "experimental"`

## Success Criteria

- Complete, self-contained competency package
- All dependencies properly documented
- Prerequisites management working
- Examples demonstrate functionality
- Documentation complete and clear
- OLAF framework integration successful
- Main project cleaned of duplicates

## Best Practices

1. **Naming**: Use kebab-case for competency names
2. **Documentation**: Include real examples and use cases
3. **Dependencies**: Minimize external dependencies
4. **Testing**: Include working examples as tests
5. **Versioning**: Use semantic versioning
6. **Compatibility**: Document platform requirements
7. **Maintenance**: Keep documentation updated

## Notes

- Competency should be completely self-contained
- All paths should be relative to competency root
- Dependencies should be clearly documented
- Examples should demonstrate real usage
- Prerequisites should be automatically checkable
