# Step-by-Step Tutorial

**Challenge Me: Step-by-Step Tutorial**

**How to Execute the "Challenge Me" Workflow**

This tutorial shows exactly how to explore and refine ideas through evidence-based challenges using the OLAF researcher competency.

## Prerequisites

- OLAF framework properly installed and configured
- A clear topic or idea you want to explore
- (Optional) Access to relevant codebase or documentation
- Understanding of the subject area you're exploring

## Step-by-Step Instructions

### Step 1: Prepare Your Inputs
[Define the subject and initial thoughts]

**User Action:**
1. Identify the topic or idea you want to explore
2. Formulate your current thinking about the subject
3. (Optional) Note paths to relevant codebase or documentation

**System Response:**
Inputs should be clear and specific for targeted analysis.

### Step 2: Invoke the olaf challenge me Command
**User Action:** Execute the OLAF command to start ideation

```
"olaf challenge me"
```

**Provide Parameters:**
- **subject**: [your topic or idea] - The subject to explore
- **initial_thoughts**: [your current thinking] - Your initial perspective
- **codebase_path**: [path/to/code] - Optional path for code analysis
- **documentation_path**: [path/to/docs] - Optional path for documentation review
- **research_depth**: [shallow/moderate/deep] - Analysis depth (default: moderate)
- **challenge_intensity**: [gentle/moderate/rigorous] - Challenge level (default: moderate)

### Step 3: Initial Research and Challenge

**What OLAF Does:**
- Analyzes provided context (codebase, documentation, web sources)
- Identifies assumptions and potential issues in your initial thinking
- Presents constructive challenges backed by evidence
- References specific sources (files, docs, research)

**You Should See:** Evidence-based challenges with specific references to code, documentation, or research findings

### Step 4: Interactive Engagement
**What OLAF Does:**
- Asks clarifying questions (lettered options A, B, C, D)
- Presents multiple-choice alternatives (numbered 1, 2, 3, 4)
- Shares industry insights and requests your perspective
- Invites you to explain your reasoning

**Your Action:** Respond thoughtfully to questions and challenges
- Don't just say "continue" - engage with the analysis
- Explain your reasoning, not just conclusions
- Challenge back if you disagree with the assessment
- Request clarification when needed

**You Should See:** Iterative refinement cycles (typically 3-5 for moderate depth) with evolving insights based on your responses

### Step 5: Finalize and Generate Deliverables
**User Action:** When ideas are sufficiently refined, say "save"

**What OLAF Does:**
- Generates filename format: `[subject]-YYYYMMDD-HHmm.md`
- Saves four deliverables to `olaf-data/findings/` directory:
  - **think.md**: Final refined ideas with comprehensive details
  - **path.md**: Complete trajectory showing evolution of thinking
  - **sources.md**: All citations organized by source type (codebase, docs, web)
  - **reco.md**: Honest recommendations with go/no-go decisions
- Displays summary of findings and next steps

**You Should See:** 
- Four markdown files saved with timestamp naming
- Summary of key insights and recommendations
- Specific next steps with priorities and resource requirements

### Step 6: Review and Act on Findings
**User Action:** Review all deliverables and act on recommendations
1. Read think.md for final refined approach
2. Review path.md to understand how thinking evolved
3. Verify sources.md for evidence quality
4. Follow recommendations in reco.md (most critical)
5. Share findings with team for decision-making
6. Use related competencies to formalize next steps

## Verification Checklist

✅ **Subject and initial thoughts clearly defined**
✅ **Challenge Me command invoked with appropriate parameters**
✅ **Active engagement with challenges and questions (not passive "continue")**
✅ **Multiple refinement cycles completed until ideas well-explored**
✅ **Four deliverables generated (think.md, path.md, sources.md, reco.md)**
✅ **All deliverables reviewed, especially reco.md for actionable recommendations**
✅ **Sources verified for accuracy and relevance**
✅ **Next steps identified and prioritized**

## Troubleshooting

**If challenges feel too aggressive:**
- Use `challenge_intensity="gentle"` for more supportive tone

**If not enough research depth:**
- Use `research_depth="deep"` and provide codebase/documentation paths

**If session taking too long:**
- Use `research_depth="shallow"` or say "save" earlier in the process

**If challenges not relevant to your context:**
- Provide `codebase_path` and `documentation_path` for context-aware analysis

**If you need more specific technical analysis:**
- Follow up with Developer or Architect competencies after Challenge Me session

## Key Learning Points

1. **Systematic Exploration:** The workflow follows iterative challenge cycles with evidence-based analysis
2. **Active Engagement:** Thoughtful responses to challenges lead to better refinement than passive "continue"
3. **Multi-Source Integration:** Combines codebase, documentation, and web research for comprehensive analysis
4. **Honest Assessment:** Provides go/no-go recommendations backed by evidence, not assumptions

## Next Steps to Try

- Review all four deliverables to understand the complete analysis
- Use reco.md recommendations to guide decision-making and planning
- Follow up with related competencies (Business Analyst, Developer, Architect) to formalize findings
- Share think.md and reco.md with team for transparent, evidence-based decisions

## Expected Timeline

- **Total session time:** 20-60 minutes depending on research depth and complexity
- **User input required:** Subject, initial thoughts, responses to challenges and questions
- **OLAF execution time:** Automated research, challenge generation, and deliverable creation
