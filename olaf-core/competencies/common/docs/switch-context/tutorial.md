# Switch Context - Tutorial

## Overview

Learn how to dynamically switch between different project contexts in OLAF.

## Prerequisites

- OLAF framework loaded
- Understanding of basic OLAF commands

## Basic Usage

### 1. List Available Contexts

```
olaf context switch
```

This will show all available context templates and let you select one.

### 2. Switch to Specific Context

```
olaf context switch default
```

Switches to the default context template.

### 3. Check Current Context Status

```
olaf context status
```

Shows information about the currently active context.

### 4. Clear Current Context

```
olaf context clear
```

Removes the active context, returning to framework defaults.

## Advanced Usage

### Creating Custom Context Templates

1. Create a new file: `olaf-data/context/context-{your-name}.md`
2. Follow the context template structure (see description.md)
3. Use `olaf context switch {your-name}` to activate it

### Context Template Structure

```markdown
# Project Context - {Context Name}

## Project Overview
Brief description of the project

## Key Technologies
- Technology 1
- Technology 2

## Development Guidelines
Specific guidelines for this project context
```

## Important Notes

- Context changes require a **session restart** to take effect
- The active context is stored in `olaf-data/context/context-current.md`
- Context templates are stored in `olaf-data/context/context-*.md`

## Troubleshooting

- **Context not found**: Check that `context-{name}.md` exists in `olaf-data/context/`
- **Changes not applying**: Restart your session after context switch
- **File not copying**: Ensure write permissions to `olaf-data/context/` directory
