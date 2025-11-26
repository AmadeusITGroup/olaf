# Memory-map

OLAF provides a Memory-map (a markdown file) that maps the important folders and files of the project. So prompt can be instructed to read input files and generate output files based in the right location of the project - especially for the olaf-data folder.

## Location

The memory-map is present in:
- `.olaf/olaf-core/reference/memory-map.md` for agents
## Purpose

- **Project Navigation**: Provides LLM with key context pointers (files or structure)
- **File Location**: Maps important folders and files for AI reference
- **Input/Output Management**: Instructs prompts on correct file locations
- **Context Loading**: Essential for LLM interaction initialization

## Usage

The memory-map should be loaded by the LLM at the start of each interaction. This is why we rely on the agent's capabilities to do so (e.g., `.windsurf/rules/olaf-bootstrap.md` for Windsurf, `.github/copilot-instructions.md` for Copilot).

## limits

Most agent have an indexing and/or embedding capability that could be used to supplement the memory-map. We did this for performance reason with github copilot at the start. This may not be needed in the future as agents are constantly evolving.
