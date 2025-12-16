# Search and Learn Tutorial

## Step-by-Step Guide

This tutorial walks you through using the Search and Learn competency effectively for systematic knowledge acquisition.

## Prerequisites

- Access to OLAF Framework
- Basic understanding of research methodology
- Ability to evaluate source credibility

## Tutorial Steps

### Step 1: Initiate the Competency

Start by invoking the search and learn competency:

```bash
"search and learn"
```

The system will prompt you for three required parameters. **Do not proceed without providing all three.**

### Step 2: Define Learning Parameters

You must provide all three required parameters:

#### Learning Objective
Be specific about what you want to learn:

**Good Examples:**
- "How to implement OAuth2 authentication in Node.js applications"
- "Understanding microservices communication patterns and trade-offs"
- "Best practices for React component testing with Jest and React Testing Library"

**Poor Examples:**
- "Learn programming" (too broad)
- "Authentication" (not specific enough)
- "React stuff" (vague)

#### Current Knowledge
Honestly assess your starting point:

**Good Examples:**
- "I have 2 years of JavaScript experience but no authentication implementation experience"
- "Familiar with monolithic architecture, new to microservices concepts"
- "Know basic React and unit testing, but haven't used React Testing Library"

#### Context
Provide relevant constraints and application context:

**Good Examples:**
- "Need to implement for production e-commerce app, 2-week timeline, team of 3 developers"
- "Evaluating architecture for new project, budget constraints, scalability requirements"
- "Improving test coverage for existing codebase, CI/CD integration required"

### Step 3: Review Learning Goals

The system will:
- Clarify and refine your objectives
- Break complex topics into components
- Establish success criteria
- Set appropriate scope boundaries
- Identify prerequisite knowledge

**Example Output:**
```
Learning Goals Defined:
✅ Understand OAuth2 flow and security principles
✅ Implement authorization server integration
✅ Handle token management and refresh
✅ Secure API endpoints with middleware
✅ Test authentication flows

Prerequisites Identified:
- HTTP/HTTPS protocol understanding
- Express.js middleware concepts
- JSON Web Token (JWT) basics
```

### Step 4: Execute Search Strategy

The system will systematically search across:

#### Documentation Sources
- Official framework documentation
- API references and guides
- Security best practices

#### Academic Sources
- Research papers on authentication
- Security analysis studies
- Comparative evaluations

#### Community Sources
- Stack Overflow discussions
- GitHub repositories and examples
- Technical blogs and tutorials

#### Quality Indicators
Each source receives quality scoring based on:
- Authority and credibility
- Recency and relevance
- Community validation
- Technical accuracy

### Step 5: Information Synthesis

The system will:
- Assess source credibility
- Identify contradictions
- Synthesize multi-source insights
- Create concept connections
- Validate understanding

**Example Synthesis:**
```
Key Insights Discovered:
🔍 OAuth2 vs JWT: OAuth2 is authorization framework, JWT is token format
🔍 Security Considerations: PKCE required for public clients
🔍 Implementation Patterns: Authorization Code flow recommended for web apps
🔍 Common Pitfalls: Token storage in localStorage security risks

Contradictions Resolved:
⚠️  Some sources recommend localStorage, others recommend httpOnly cookies
✅  Resolution: httpOnly cookies more secure for web applications
```

### Step 6: Practical Application

The system generates:
- Real-world implementation examples
- Code snippets and configurations
- Testing strategies
- Common pitfall avoidance

**Example Application:**
```javascript
// Secure token storage example
app.use(session({
  secret: process.env.SESSION_SECRET,
  httpOnly: true,
  secure: process.env.NODE_ENV === 'production',
  sameSite: 'strict'
}));
```

### Step 7: Learning Report Generation

The system automatically saves a comprehensive report:

**File Format:** `search-and-learn-[topic]-YYYYMMDD-HHmm.md`

**Report Sections:**
1. **Learning Summary**: Key concepts and insights
2. **Source Documentation**: All references with quality scores
3. **Application Examples**: Practical implementations
4. **Knowledge Gaps**: Areas needing further research
5. **Next Steps**: Recommended follow-up actions

## Advanced Usage Patterns

### Iterative Learning
Use multiple sessions to deepen understanding:

```bash
# Session 1: Basic concepts
"search and learn" with learning_objective="OAuth2 basics"

# Session 2: Implementation details  
"search and learn" with learning_objective="OAuth2 Node.js implementation"

# Session 3: Security hardening
"search and learn" with learning_objective="OAuth2 security best practices"
```

### Comparative Analysis
Research multiple approaches:

```bash
"search and learn" 
with learning_objective="Compare OAuth2 vs SAML for enterprise SSO"
with current_knowledge="Basic authentication concepts"
with context="Enterprise environment, 10000+ users, security compliance required"
```

### Technology Evaluation
Assess tools and frameworks:

```bash
"search and learn"
with learning_objective="Evaluate React vs Vue.js for new project"
with current_knowledge="JavaScript ES6+, basic component concepts"
with context="Team of 5 developers, 6-month project timeline, mobile-first design"
```

## Quality Validation Tips

### Source Evaluation
- **Authority**: Check author credentials and organization
- **Recency**: Prefer sources from last 2 years for technology topics
- **Community**: Look for high engagement and positive feedback
- **Cross-Reference**: Validate claims across multiple sources

### Learning Validation
- **Practical Testing**: Try examples and code snippets
- **Concept Mapping**: Connect new knowledge to existing understanding
- **Teaching Test**: Explain concepts to validate comprehension
- **Application Planning**: Identify specific use cases

## Common Pitfalls

### Parameter Definition
❌ **Vague Objectives**: "Learn about databases"
✅ **Specific Objectives**: "Understand PostgreSQL indexing strategies for query optimization"

### Source Quality
❌ **Accepting First Results**: Using first search results without validation
✅ **Quality Assessment**: Evaluating source authority and cross-referencing

### Application Gap
❌ **Theory Only**: Collecting information without practical application
✅ **Implementation Focus**: Creating examples and testing understanding

## Integration Examples

### With Challenge Me Competency
```bash
# First: Research foundation
"search and learn" with learning_objective="Microservices patterns"

# Then: Challenge ideas
"challenge me" with subject="Microservices migration" 
with initial_thoughts="Based on research, considering event-driven architecture"
```

### With Developer Competency
```bash
# Research implementation approaches
"search and learn" with learning_objective="React testing strategies"

# Then: Review existing code
"review code" with focus="testing coverage and patterns"
```

## Success Indicators

- **Complete Parameter Provision**: All three parameters clearly defined
- **Quality Source Collection**: Authoritative references with URLs
- **Practical Application**: Real-world examples and implementations
- **Comprehensive Documentation**: Detailed learning report generated
- **Knowledge Integration**: Connections to existing understanding
- **Actionable Outcomes**: Clear next steps identified

## Troubleshooting

### Missing Parameters
If the system asks for parameters again, ensure you've provided:
1. Specific learning objective
2. Honest current knowledge assessment  
3. Relevant context and constraints

### Poor Source Quality
If sources seem unreliable:
- Request more authoritative sources
- Specify academic or official documentation preference
- Ask for cross-reference validation

### Insufficient Depth
If learning seems superficial:
- Refine learning objective to be more specific
- Request deeper analysis of specific aspects
- Ask for advanced implementation examples

## Next Steps

After completing this tutorial:
1. Practice with simple learning objectives
2. Experiment with different parameter combinations
3. Review generated learning reports for quality
4. Integrate with other OLAF competencies
5. Develop personal learning workflows
