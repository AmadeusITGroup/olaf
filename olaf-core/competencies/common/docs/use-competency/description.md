# Use Competency

## Overview

Intelligent competency discovery and execution router that finds and executes the right competency based on your goal or description.

## Purpose

Simplifies competency usage by allowing natural language descriptions of what you want to accomplish, then automatically discovering and routing to the appropriate competency without needing to know specific commands.

## Usage

**Command**: `use competency` | `find competency` | `search competency` | `execute competency` | `run competency`

**Protocol**: Act

**When to Use**: When you know what you want to accomplish but don't know which specific competency to use.

## Parameters

### Required Inputs
- **Goal Description**: What you want to accomplish or the problem you're trying to solve

### Optional Inputs
- **Context**: Additional details about your situation
- **Constraints**: Any limitations or requirements
- **Preferences**: Preferred approach or style

### Context Requirements
- Clear description of your goal or need

## Output

**Deliverables**:
- Identified competency that matches your goal
- Automatic execution of the competency
- Results from the executed competency

**Format**: Seamless routing and execution

## Examples

### Example 1: Code Quality Goal

**Scenario**: Want to improve code quality but unsure which competency

**Command**:
```
use competency
```

**Input**: "I want to improve the code quality of my application"

**Result**: Routes to code review or refactoring competency and executes it

### Example 2: Documentation Need

**Scenario**: Need documentation but don't know the specific command

**Command**:
```
find competency for creating API documentation
```

**Result**: Identifies and executes the appropriate documentation competency

### Example 3: Architecture Decision

**Scenario**: Need help with architecture design

**Command**:
```
use competency to design system architecture
```

**Result**: Routes to architect competency and begins architecture design process

## Related Competencies

- **olaf-help**: Use this to browse available competencies
- **assess-genai-initiative**: Evaluate if AI/competency is right for your goal
- **find-expert-contact**: Find human experts when no competency matches

## Tips & Best Practices

- Describe your goal clearly and specifically
- Mention the context or domain (e.g., "for a React application")
- Include constraints or requirements
- Trust the routing - it will find the best match
- If routing seems wrong, provide more specific description

## Limitations

- Requires clear goal description for accurate routing
- May ask clarifying questions if goal is ambiguous
- Cannot create new competencies, only route to existing ones
- Routing quality depends on competency index completeness
