# Core Principles

OLAF allows you to define core principles that guide the AI in performing its tasks. These principles are defined in the `.olaf/olaf-core/reference/core-principles.md` file.

## Purpose

- **Behavioral Guidelines**: Define how the AI should operate within the project context
- **Decision Making**: Provide a framework for AI decision-making processes
- **Consistency**: Ensure consistent behavior across different competencies
- **Project Alignment**: Align AI behavior with project values and practices

## Configuration

Core principles are stored in:
- `.olaf/olaf-core/reference/core-principles.md` – For general-purpose agents
## Integration

This file can be edited and may also refer to Decision Records in the `olaf-data` folder, provided those are in a format acceptable to the model.

The contents of these files are loaded into the context window of the LLM at the start of each interaction. Therefore, it is crucial to keep the information concise and provide clear context.

## Limits

As with all other persistent instructions, these are added to the model context in each request. We found that you need to be frugal with some models and recommend reducing this to only the most concise and relevant information.
