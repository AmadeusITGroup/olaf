# Tools and Templates Integration

OLAF allows you to define tools (scripts) and templates (md, json, or other files) that are used by prompts to perform their tasks. These tools and templates are located in the `.olaf/olaf-core/tools/` and `.olaf/olaf-core/templates/` folders.

## Tools Directory (`.olaf/olaf-core/tools/`)

Contains scripts and utilities that competencies can execute:
- PowerShell scripts for Windows environments
- Analysis utilities for code metrics
- Automation scripts for common tasks
- Project-specific tools

## Templates Directory (`.olaf/olaf-core/templates/`)

Contains structured templates for consistent output:
- Markdown templates for documentation
- JSON templates for structured data
- Report templates for analysis results
- Specification templates for technical documents

## Design Philosophy

Unlike other solutions that embed examples directly in prompts, we believe decoupling examples and templates from prompts leads to cleaner and more maintainable prompt design.


## Why not use MCP server tools instead of scripts?

MCP server tools are designed for specific tasks and may not offer the flexibility needed for all use cases. Scripts, on the other hand, can be tailored to fit the exact requirements of a competency, allowing for greater customization and control over the execution environment.

Additionally, we found it effective to develop and test prompts rapidly using scripts that can be generated on the fly. Once the scripts are working, they can serve as tool pseudocode for an MCP server. In practice, this approach has enabled highly efficient workflows and faster iteration cycles.


## Questionnaires

We may also use "questionnaires" to guide the user with a set of questions used to deliver on the competency. These will also be referenced in the prompt as input. You can generate questionnaires through a simple prompt (no meta-prompt is provided for this in this version of OLAF).

## Benefits

- **Separation of Concerns**: Keep templates separate from prompt logic
- **Reusability**: Use templates across multiple competencies
- **Consistency**: Standardized output formats
- **Maintainability**: Easy to update templates independently
- **Tool Integration**: Seamless integration with external scripts and utilities
