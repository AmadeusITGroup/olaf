# Researcher Competency Package

Comprehensive research competency package for ideation, collaborative thinking, and evidence-based exploration with multi-source research integration.

## 🚀 Quick Start

1. **Challenge Me**:

   ```bash
   "challenge me" with subject="[your topic]" initial_thoughts="[your initial ideas]"
   ```

2. **With Codebase Analysis**:

   ```bash
   "challenge me" with subject="[your topic]" initial_thoughts="[ideas]" codebase_path="[path/to/repo]"
   ```

3. **With Documentation Review**:

   ```bash
   "challenge me" with subject="[your topic]" initial_thoughts="[ideas]" documentation_path="[path/to/docs]"
   ```

## 📦 What's Included

### Core Competencies (1 total)

| Competency | Entry Point | Purpose |
|------------|-------------|---------|
| Challenge Me | `challenge-me` | Interactive ideation engine with evidence-based challenges |

### 📁 Structure

```text
researcher/
├── README.md                        # This file
├── competency-manifest.json         # Package metadata
├── dependencies.json                # Tool dependencies
├── docs/                            # Documentation
│   └── challenge-me/                # Challenge Me competency docs
│       ├── description.md           # Detailed description
│       └── tutorial.md              # Step-by-step tutorial
└── prompts/
    └── challenge-me.md              # Interactive ideation prompt
```

## ⚡ Key Capabilities

✅ **Interactive Ideation** - Iterative cycles of challenging and refining ideas  
✅ **Multi-Source Research** - Integrate insights from codebase, documentation, and web  
✅ **Evidence-Based Challenges** - Constructive challenges backed by research  
✅ **Collaborative Engagement** - Interactive questions, polls, and user involvement  
✅ **Trajectory Tracking** - Document the evolution of thinking throughout the session  
✅ **Comprehensive Citations** - Track all sources consulted during ideation  
✅ **Honest Recommendations** - Actionable recommendations including go/no-go decisions  
✅ **Source Attribution** - Link insights to specific evidence from all sources

## 🔗 Integration with Other Competencies

- **Business Analyst**: Requirements analysis and questionnaire generation
- **Developer**: Technical specification generation from code
- **Architect**: Technology evaluation and assessment
- **Project Manager**: Decision record creation and tracking

## 💡 Usage Examples

### Example 1: Basic Ideation Session

```bash
"challenge me"
with subject="AI-powered search feature"
with initial_thoughts="We should add semantic search to our product"

# The competency will:
# 1. Initialize session with timestamp
# 2. Challenge the idea constructively
# 3. Ask for user perspectives and clarifications
# 4. Provide alternative approaches to consider
# 5. Continue cycles until user says "save"
# 6. Generate think.md, path.md, sources.md, and reco.md
```

### Example 2: Research with Codebase Analysis

```bash
"challenge me"
with subject="refactoring authentication module"
with initial_thoughts="We should migrate to OAuth2"
with codebase_path="./src/auth"

# The competency will:
# 1. Scan the authentication codebase
# 2. Analyze current implementation patterns
# 3. Challenge the migration idea with code-specific insights
# 4. Reference specific files and functions
# 5. Provide evidence-based alternatives
# 6. Track all code references in sources.md
```

### Example 3: Comprehensive Multi-Source Research

```bash
"challenge me"
with subject="microservices migration strategy"
with initial_thoughts="We should break the monolith into 20 services"
with codebase_path="./src"
with documentation_path="./docs/architecture"
with research_depth="deep"

# The competency will:
# 1. Analyze existing codebase structure
# 2. Review architecture documentation
# 3. Conduct web research on migration strategies
# 4. Challenge the approach with multi-source evidence
# 5. Present industry insights and ask for perspective
# 6. Provide comprehensive recommendations
# 7. Generate detailed sources.md with all references
```

## 🎮 Interactive Features

### 🤝 Collaborative Engagement

- **Multiple-Choice Questions**: Numbered lists (1,2,3,4) for easy selection
- **Clarification Questions**: Lettered lists (A,B,C,D) for vision and perspective
- **Web Feedback Integration**: Present industry insights and ask for your perspective
- **User Reasoning**: Invite explanations rather than assumptions
- **No Repeated Questions**: Build on previous responses continuously

### 🔍 Research Integration

- **Codebase Analysis**: Examine structure, patterns, and implementations
- **Documentation Review**: Find constraints, best practices, and decisions
- **Web Research**: Gather external insights, case studies, and expert opinions
- **Source Citations**: Track every source with specific references
- **Evidence-Based Insights**: Link all insights to supporting evidence

### 📋 Output Deliverables

When you say "save", the competency generates:

- **think.md**: Final refined ideas with comprehensive details
- **path.md**: Complete trajectory showing evolution of thinking
- **sources.md**: Comprehensive citations organized by source type
  - Codebase references (file paths, functions)
  - Documentation references (sections, pages)
  - Web resources (URLs, timestamps)
- **reco.md**: Honest, actionable recommendations including:
  - Go/no-go decisions with reasoning
  - Alternative approaches if current approach not recommended
  - Specific next steps with priorities
  - Risk assessments and mitigation strategies

## 📋 Requirements

- **Git**: >=2.30 (for research tracking)
- **LLM**: Claude Sonnet 4.5 or higher recommended
- **Platforms**: Windows, Linux, macOS
- **Optional**: Web search, codebase access, documentation access

## ⚙️ Parameters

- **subject** (required): The topic or subject area for ideation
- **initial_thoughts** (required): Your initial ideas or description
- **codebase_path** (optional): Path to local repository for code analysis
- **documentation_path** (optional): Path to documentation folder
- **web_search_urls** (optional): Specific URLs for research
- **research_depth** (optional): shallow | moderate | deep (default: moderate)
- **challenge_intensity** (optional): gentle | moderate | rigorous (default: moderate)

## 📚 Technical Documentation

For detailed technical documentation and advanced usage patterns, see:

- `prompts/challenge-me.md` - Complete competency specification
- `competency-manifest.json` - Complete competency metadata
- `dependencies.json` - Detailed tool requirements

## 💎 Best Practices

1. **Be Specific**: Provide detailed initial thoughts for better challenges
2. **Use Context**: Include codebase and documentation paths when relevant
3. **Engage Actively**: Respond to questions and polls - don't just say "continue"
4. **Save Thoughtfully**: Continue cycles until ideas are well-refined
5. **Review Sources**: Check sources.md for evidence quality and coverage
6. **Consider Recommendations**: Take reco.md seriously, especially negative recommendations

## 🆘 Support

For issues or questions, refer to the OLAF Framework documentation or the main README.
