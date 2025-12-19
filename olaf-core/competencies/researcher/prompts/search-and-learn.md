---
name: search-and-learn
description: Guide systematic information discovery, knowledge acquisition, and practical application
tags: [research, learning, information, knowledge, search]
---


## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval

You MUST get current time in YYYYMMDD-HHmm format using the appropriate terminal command for the user's environment:

- **Windows PowerShell**: `Get-Date -Format "yyyyMMdd-HHmm"`
- **Unix/Linux/macOS**: `date +"%Y%m%d-%H%M"`

**IMPORTANT**: Use ONLY the command that matches the user's current shell environment. Do not run both commands.

## Input Parameters

**CRITICAL REQUIREMENT**: You MUST ask the USER to provide ALL three parameters below before proceeding. DO NOT assume or infer these parameters from context. STOP and ask if any parameter is missing.

**Required Parameters (ALL must be provided by USER):**

- **learning_objective**: string - Specific question, skill, problem, or topic to understand
- **current_knowledge**: string - Current knowledge level and previous experience
- **context**: string - Related skills, time constraints, and application context

**VALIDATION CHECKPOINT**: Before starting the Process section, verify you have explicit USER input for all three parameters above. If ANY parameter is missing, ask the USER to provide it.

## Process

**MANDATORY FIRST STEP**: Verify you have received USER input for all three required parameters (learning_objective, current_knowledge, context). If ANY are missing, STOP and ask the USER before proceeding.

1. **Define Learning Goals**:
   - Clarify specific learning objectives from user input
   - Break down complex topics into manageable components
   - Establish success criteria for the learning
   - Set appropriate scope boundaries
   - Identify prerequisite knowledge needs

2. **Develop Search Strategy**:
   - Formulate precise search queries based on objectives
   - Identify authoritative information sources:
     - Documentation and official sources
     - Academic publications  
     - Technical blogs and articles
     - Community forums and discussions
     - Video tutorials and courses

3. **Execute Systematic Search**:
   - Search using defined strategy across identified sources
   - Document sources with MANDATORY URLs - reject any source without full URL
   - Track information quality and relevance scores
   - Identify knowledge gaps requiring additional research
   - Maintain source citations for credibility using format: `[Source Title](full-url)`
   - **CRITICAL**: Every source reference MUST include accessible URL

4. **Evaluate and Synthesize Information**:
   - Assess source credibility and reliability
   - Identify contradictions or conflicting information
   - Synthesize information from multiple sources
   - Create connections between concepts
   - Validate understanding through examples and cross-references

5. **Apply and Test Learning**:
   - Create practical applications of new knowledge
   - Test understanding through exercises or real examples
   - Identify areas needing clarification or deeper study
   - Connect to existing knowledge base
   - Document key insights and actionable takeaways

6. **Save Learning Report**:
   - **MANDATORY**: Save the complete learning report as an MD file
   - Use timestamp format: `search-and-learn-[topic]-YYYYMMDD-HHmm.md`
   - Save to `[id:findings_dir]` directory
   - Include all sections: Learning Summary, Source Documentation, Application Examples, Knowledge Gaps, Next Steps

## Output Format

Learning report including:

- **Learning Summary**: Key concepts and insights discovered
- **Source Documentation**: Credible references with quality assessments
- **Application Examples**: Practical use cases or implementations
- **Knowledge Gaps**: Areas requiring additional research
- **Next Steps**: Recommended follow-up learning or actions

## Output to USER

- Learning objectives achieved: [list completed goals]
- Key insights discovered: [summarized findings]
- Sources consulted: [number and types of authoritative sources]
- Practical applications identified: [relevant use cases]
- Next recommended learning steps: [if applicable]

## Learning Rules

- Rule 1: Prioritize authoritative and credible sources over popular but unverified content
- Rule 2: Balance theoretical knowledge with practical application examples
- Rule 3: Always validate understanding through multiple source cross-references
- Rule 4: Connect new learning to existing knowledge for better retention
- Rule 5: **MANDATORY URL COLLECTION** - Every source MUST have full URL, reject generic references
- Rule 6: **Source format compliance** - Use `[Source Title](full-url)` format for all references