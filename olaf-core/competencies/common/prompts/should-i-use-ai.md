# Should I Use AI?

**Purpose**: Analyze user task and recommend whether to use AI/LLM or IDE tools based on task categorization guide 
**Protocol**: Act
**Input**: User task description (single sentence)

## Core Logic

1. **Analyze the task** against the LLM vs IDE categorization guide located in [id:reference_dir]llm-vs-ide-task-guide.md
2. **Categorize** into LLM or IDE tool recommendation
3. **Provide specific guidance** based on recommendation

## Decision Framework

**Use AI/LLM if task requires:**
- Logic & reasoning
- Context-aware code generation  
- Intelligent refactoring & architecture
- API & framework migration
- Domain-specific understanding
- Quality & security analysis

**Use IDE Tools if task is:**
- Basic code manipulation
- File & project operations
- Navigation & search
- Template-based code generation
- Formatting & style
- Debugging & analysis tools
- Version control integration
- Build & deployment
- Database & external tools
- Simple text operations
- Automated code generation (template-based)

## Response Format

### For IDE Tool Recommendations:
```
🔧 **Recommendation: Use IDE Tools**

**Task Category**: [Category from guide]

**Specific Actions**:
- IDE Feature: [Specific IDE functionality]
- Keyboard Shortcut: [If applicable]
- CLI Alternative: [If applicable] 
- External Tool: [If applicable]

**Why IDE**: [Brief explanation of why this is mechanical/repetitive/pattern-based]
```

### For AI/LLM Recommendations:
```
🧠 **Recommendation: Use AI/LLM**

**Task Category**: [Category from guide]

**Check Existing Prompts**: [Search query-competency-index for relevant prompt]

**If Existing Prompt Found**:
- Use prompt: [prompt-file.md] 
- Protocol: [Protocol from competency index]

**If No Existing Prompt**:
**Suggested Prompt**:
```
[Generated prompt specific to the task]
```

**Add to Competency**: [Pattern phrases for competency index]

**Why AI**: [Brief explanation of why this requires reasoning/context/creativity]
```

## Examples

**Input**: "Generate getter methods for my class"
**Output**: 
🔧 **Recommendation: Use IDE Tools**
**Task Category**: Basic Code Manipulation
**Specific Actions**: Right-click → Generate → Getter/Setter (IntelliJ/Eclipse) or use code action in VS Code
**Why IDE**: Template-based, mechanical operation

**Input**: "Fix memory leak in my application"  
**Output**:
🧠 **Recommendation: Use AI/LLM**
**Task Category**: Logic & Reasoning Tasks
**Check Existing Prompts**: [Search for memory/performance analysis prompts]
**Why AI**: Requires code behavior analysis and reasoning about memory patterns

## Implementation Notes

- Always reference the LLM vs IDE task categorization guide
- Be specific about IDE features and shortcuts
- Keep responses concise and actionable
