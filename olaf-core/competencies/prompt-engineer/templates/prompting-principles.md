# Prompt Engineering Best Practices

This guide provides specific prompt engineering techniques for optimal results in your applications.

## Core Principles

### 1. Use Imperative Language
Always use commanding, action-oriented language for clarity and consistency:

**Effective patterns:**
- "You WILL" - for required actions
- "You MUST" - for critical requirements  
- "You NEVER" - for prohibited actions
- "MANDATORY" - for non-negotiable requirements
- "CRITICAL" - for extremely important instructions

**Example: Task Instructions**
```text
Less effective: Please analyze the code and make improvements

More effective: You WILL analyze the code structure and identify three specific improvement opportunities. You MUST provide concrete examples for each recommendation.
```

### 2. Be Explicit with Instructions and Success Criteria

Always define what constitutes successful completion:

**Example: Creating an analytics dashboard**
```text
Less effective: Create an analytics dashboard

More effective: You WILL create an analytics dashboard that includes:
- Real-time data visualization
- Interactive filtering capabilities
- Export functionality
- Mobile-responsive design

Success criteria: Dashboard loads in under 3 seconds and displays data correctly on all screen sizes.
```

### 3. Add Context to Improve Performance

Always explain WHY instructions matter:

**Example: Formatting preferences**
```text
Less effective: NEVER use ellipses

More effective: You MUST avoid ellipses because your response will be read aloud by a text-to-speech engine, and ellipses cannot be properly pronounced by TTS systems.
```

### 4. Structure with XML-Style Markup

Use XML-style tags for complex prompts to improve organization:

```text
<!-- <validation_phase> -->
You WILL first validate all input parameters
<!-- </validation_phase> -->

<!-- <execution_phase> -->  
You WILL then execute the core logic
<!-- </execution_phase> -->

<!-- <output_phase> -->
You WILL generate outputs in the specified format
<!-- </output_phase> -->
```

### 5. Include Validation and Error Handling

Always anticipate and address potential issues:

```text
## Error Handling
You WILL handle these scenarios:
- **Missing Parameters**: Request specific missing items from user
- **Invalid Input**: Provide clear error message and correction guidance
- **Tool Failures**: Offer alternative approaches or manual steps
- **Validation Failures**: Stop process and request user guidance
```

### 6. Clarity and Specificity

Every instruction should be specific and measurable:
- Define exact formats and expected outputs
- Provide concrete examples
- Specify success metrics
- Include validation steps
- Document assumptions
- List dependencies

### 7. Progressive Disclosure

Organize information from high-level to detailed:
- Start with overview and purpose
- Present required parameters clearly
- Detail execution steps
- Include error scenarios
- Provide next steps guidance

### 8. Consistency and Formatting

Maintain consistent formatting throughout:
- Use consistent headings and levels
- Apply uniform command formatting
- Standardize parameter descriptions
- Use consistent language tone
- Apply template structure exactly
