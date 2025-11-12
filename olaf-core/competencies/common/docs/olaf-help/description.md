# OLAF Help

## Overview

Discovers available OLAF competencies and provides guidance on which competencies to use for specific needs.

## Purpose

Helps users navigate the OLAF framework by discovering available competencies, understanding their purposes, and finding the right tool for their current task.

## Usage

**Command**: `help me` | `olaf help` | `olaf i need you`

**Protocol**: Act

**When to Use**: When you're unsure what OLAF can do, need to find a specific competency, or want to explore available capabilities.

## Parameters

### Required Inputs
None - can be invoked without parameters

### Optional Inputs
- **Search Query**: Keywords or description of what you need help with
- **Persona Filter**: Filter by role (developer, architect, etc.)
- **Category**: Filter by competency category

### Context Requirements
None - works in any context

## Output

**Deliverables**:
- List of relevant competencies
- Descriptions and use cases
- Commands to execute each competency
- Related competencies and alternatives

**Format**: Organized list with descriptions and actionable commands

## Examples

### Example 1: General Help

**Scenario**: New user wants to know what OLAF can do

**Command**:
```
olaf help
```

**Result**: Overview of OLAF capabilities with major competency categories

### Example 2: Specific Need

**Scenario**: Need help with code review

**Command**:
```
help me with code review
```

**Result**: Lists code review related competencies with descriptions and commands

### Example 3: Persona-Based Discovery

**Scenario**: Want to see all developer competencies

**Command**:
```
show me developer competencies
```

**Result**: Filtered list of competencies relevant to developers

## Related Competencies

- **use-competency**: Intelligent routing to the right competency based on your goal
- **assess-genai-initiative**: Evaluate if AI/OLAF is right for your use case
- **find-expert-contact**: Find human experts when OLAF can't help

## Tips & Best Practices

- Start with general help to understand OLAF's capabilities
- Use specific keywords when searching for competencies
- Explore competencies by persona to find role-specific tools
- Bookmark or note frequently used competencies
- Use `use competency` when you know your goal but not which competency

## Limitations

- Cannot execute competencies, only discover them
- Requires some understanding of your need to provide relevant results
- May return many results for broad queries
