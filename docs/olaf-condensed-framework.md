# OLAF Condensed Framework

## Overview

The OLAF Condensed Framework is an optimized, production-ready version of the complete OLAF framework that reduces size by ~75% while preserving all functionality. It provides a self-contained, high-performance solution for AI assistant implementations.

### Problem Solved

Previously, we had to upload the 4 kernel files of OLAF into the context window at each session start, wasting valuable tokens and reducing available context for actual work. The condensed framework eliminates this inefficiency by providing all essential functionality in a single, optimized file.

### Efficiency vs Accuracy Balance

The condensed framework strikes an optimal balance between efficiency and accuracy. Extensive testing across three major platforms (Windsurf, AWS Kiro, GitHub Copilot) demonstrates that the condensed version maintains adequate functionality while dramatically improving performance and token utilization.
## Sour
ce Files Location

The core OLAF framework files are located in `olaf-core/reference/`:

- `team-delegation.md` - Protocol hierarchy and interaction guidelines
- `query-competency-index.md` - Complete competency pattern mappings
- `memory-map.md` - Project structure and file ID references
- `core-principles.md` - Mandatory behavioral rules

## Condensed Version Generation

### Competency Call
To generate or update the condensed framework, use the competency call:
```
condense olaf framework
```

This triggers the `condense-olaf-framework` workflow that processes the four source files and creates the optimized version.

### Model Requirements
**Important:** You need a potent AI model to generate the condensed framework effectively:

**Recommended Models:**
- **Claude Sonnet 4.x** or equivalent high-reasoning models
- **GPT-5** or equivalent (avoid low-reasoning variants like GPT-3.5)

**Avoid:**
- Low-reasoning models (e.g., GPT-3.5, basic models)
- Models with limited context windows
- Models without strong compression capabilities

The condensation process requires sophisticated understanding of framework structure, XML tag preservation, and intelligent content reduction while maintaining functional integrity.#
# Loading the Condensed Framework

The condensed framework is automatically loaded through different mechanisms depending on your AI development environment:

### Windsurf IDE
Uses **OLAF Bootstrap Rules**:
- Framework loaded via bootstrap configuration
- Automatic initialization at session start
- Self-contained operation

### AWS Kiro
Uses **Steering Documents**:
- Framework loaded as steering document
- Integrated into workspace context
- Persistent across sessions

### GitHub Copilot
Uses **Bootstrap Instructions**:
- Place condensed framework at the first few lines of `copilot-instructions`
- Ensures immediate availability during code generation
- *Note: This integration method may evolve as GitHub Copilot updates*

## Benefits of Condensed Version

### Performance
- **75% size reduction** - Faster loading and processing
- **Self-contained** - No external file dependencies
- **Optimized parsing** - Reduced token usage

### Reliability
- **Single source of truth** - Everything in one file
- **No dependency chain** - Eliminates failure points
- **Consistent behavior** - Standardized across environments

### Functionality
- **All 45 competency patterns preserved** - No feature loss
- **Complete protocol hierarchy** - Full workflow support
- **XML tag compatibility** - Maintains framework structure## File Stru
cture

**Directory Structure:**
```
olaf-core/
├── reference/
│   ├── team-delegation.md          # Source: Protocols & hierarchy
│   ├── query-competency-index.md   # Source: Competency mappings
│   ├── memory-map.md               # Source: File structure
│   ├── core-principles.md          # Source: Core rules
│   └── .condensed/
│       └── olaf-framework-condensed.md  # Generated condensed version
```

## Maintenance

### Updating the Condensed Framework

**Update Process:**
1. Modify source files in `olaf-core/reference/` as needed
2. Run competency call: `condense olaf framework`
3. Verify the generated condensed version maintains all functionality
4. Update bootstrap/steering configurations if needed

### Version Control
- Source files are the authoritative version
- Condensed version is generated artifact
- Both should be committed to maintain consistency

## Integration Notes

The condensed framework is designed to be:
- **Environment agnostic** - Works across different AI development platforms
- **Bootstrap compatible** - Loads automatically at session start
- **Self-validating** - Contains built-in framework validation
- **Protocol aware** - Maintains full competency-based routing

## Adaptation to Other AI Tools

The condensed framework can be easily adapted to other AI development solutions such as:

- **Claude Code** - Via initial instruction upload
- **Cursor** - Through configuration files or startup instructions  
- **Other AI coding tools** - Any tool supporting initial instruction sets

**Key Requirement:** The target tool must have the capability to upload or configure a first set of instructions that persist across sessions, similar to:
- Copilot instructions (`copilot-instructions`)
- Windsurf rules (always-on configuration)
- AWS Kiro steering documents

As long as the AI tool supports persistent instruction loading, the OLAF condensed framework can be integrated to provide consistent competency-based workflow management.

This approach ensures consistent OLAF framework behavior regardless of the underlying AI development environment while optimizing for performance and reliability.