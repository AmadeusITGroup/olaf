# OLAF Persona Benchmark System

## Overview

This benchmark system evaluates AI agents across different personas using a modified version of the AMADEUS public Otter repository. Each persona represents a different role in software development, allowing comprehensive assessment of AI capabilities across the development lifecycle.

## How It Works

### 1. Benchmark Generation

Benchmarks are initiated using the **run-persona-benchmark-evaluation** prompt located in:
```
olaf-core/prompts/prompt-engineer/run-persona-benchmark-evaluation.md
```

This prompt requires three mandatory parameters:
- **agent_name**: Name of the AI agent being tested
- **model_name**: Specific model version  
- **persona**: Role-based benchmark type

### 2. Branch-Based Execution

Each benchmark runs in its own dedicated branch with the naming pattern:
```
benchmark-otter-{agent_name}-{model_name}-{persona}-{YYYYMMDD-HHmm}
```

**Important**: Users must clean up branches after scoring is completed.

### 3. Baseline Comparison

Results are compared against established baselines stored in:
```
docs/benchmark/judge/{persona}-base/
```

### 4. AI-Powered Scoring

The evaluation uses the **evaluate-persona-benchmark-results** prompt:
```
olaf-core/prompts/prompt-engineer/evaluate-persona-benchmark-results.md
```

**Recommendation**: Use Claude Sonnet 4 as the judge for consistent, high-quality evaluations.

---

## Benchmark Examples

### Example 1: Windsurf with Sonnet 4 - Coder Persona
```bash
# Parameters:
agent_name: "windsurf"
model_name: "sonnet-4" 
persona: "coder"

# Generated branch:
benchmark-otter-windsurf-sonnet-4-coder-20251006-1430
```

### Example 2: GitHub Copilot with Sonnet 4.5 - Business Analyst Persona
```bash
# Parameters:
agent_name: "gh-copilot"
model_name: "sonnet-4.5"
persona: "business_analyst"

# Generated branch:
benchmark-otter-gh-copilot-sonnet-4.5-business-analyst-20251006-1445
```

### Example 3: Kioro with GPT-5 - Technical Writer Persona
```bash
# Parameters:
agent_name: "kiro"
model_name: "gpt-5"
persona: "technical_writer"

# Generated branch:
benchmark-otter-kioro-gpt-5-technical-writer-20251006-1500
```

---

## Available Personas

### 1. **Coder** (`coder`)
**Focus**: Code implementation, bug fixing, feature development, unit testing
**Special Challenge**: 
- **8 injected bugs** to identify and fix
- **2 missing features** to restore
- **6 missing unit tests** to recreate
**Deliverables**: Code fixes, feature implementations, comprehensive unit tests

### 2. **Business Analyst** (`business_analyst`)
**Focus**: Requirements gathering, user story creation, process analysis
**Deliverables**: Requirements documentation, user stories, process workflows, stakeholder analysis

### 3. **Architect/Designer** (`architect_designer`)
**Focus**: System architecture, design decisions, technical documentation
**Deliverables**: Architecture diagrams, design documentation, system analysis

### 4. **Technical Writer** (`technical_writer`)
**Focus**: Documentation creation, user guides, API documentation
**Deliverables**: User manual, admin manual, operator manual, API documentation

### 5. **Tester** (`tester`)
**Focus**: Test planning, scenario creation, quality assurance
**Deliverables**: Workflow documentation, use case catalog, Gherkin test scenarios

### 6. **Project Manager** (`project_manager`)
**Focus**: Code complexity analysis, performance optimization, strategic planning
**Deliverables**: Complex code analysis, performance recommendations

---

## Benchmark Execution Process

### Step 1: Initialize Benchmark
1. Run the benchmark prompt: `run-persona-benchmark-evaluation.md`
2. Provide required parameters (agent, model, persona)
3. System creates dedicated branch and switches to it
4. Benchmark tasks are executed based on selected persona

### Step 2: Complete Tasks
- **One benchmark at a time** - Focus on single persona execution
- Each persona has specific deliverables and success criteria
- Tasks are executed according to persona-specific requirements
- All deliverables are created in the benchmark branch

### Step 3: Evaluation and Scoring
1. Run the evaluation prompt: `evaluate-persona-benchmark-results.md`
2. System lists available benchmark branches
3. Select branches to evaluate
4. AI judge (preferably Sonnet) compares against baselines
5. Detailed scores and rationale are generated
6. Results stored in `docs/benchmark/results/`

### Step 4: Branch Cleanup
- After scoring is complete, delete the benchmark branch
- Results are preserved in the results directory
- Cumulative statistics are updated in master results file

---

## Scoring System

### Score Categories
- **100+ points**: Same solution or better than baseline
- **50 points**: Less good but workable solution
- **-30 points**: Solution too far off target
- **0 points**: No solution provided

### Quality Ratings
- **10.0**: Exceptional - Significantly exceeds baseline
- **9.0-9.9**: Outstanding - Exceeds baseline in most areas
- **8.0-8.9**: Excellent - Meets or slightly exceeds baseline
- **7.0-7.9**: Good - Approaches baseline with minor gaps
- **6.0-6.9**: Satisfactory - Adequate but below baseline
- **<6.0**: Needs Improvement - Significant gaps

### Persona-Specific Weights

| Persona | Primary Criteria | Weight Distribution |
|---------|------------------|-------------------|
| **Coder** | Bug fixes, Features, Tests, Quality | 30%, 25%, 20%, 25% |
| **Business Analyst** | Requirements, User Stories, Process | 30%, 25%, 45% |
| **Architect/Designer** | Diagrams, Analysis, Decisions | 30%, 25%, 45% |
| **Technical Writer** | Completeness, Accuracy, UX | 30%, 25%, 45% |
| **Tester** | Coverage, Quality, Edge Cases | 30%, 25%, 45% |
| **Project Manager** | Analysis, Planning, Risk Assessment | 30%, 25%, 45% |

---

## Special Features

### Coder Persona Challenges
The coder persona includes intentionally introduced challenges:
- **8 Injected Bugs**: Various types of bugs inserted into the codebase
- **2 Missing Features**: Important functionality removed
- **6 Missing Unit Tests**: Critical tests deleted

This allows evaluation of:
- **Bug Detection**: Can the AI identify and fix injected issues?
- **Feature Restoration**: Can missing functionality be properly restored?
- **Test Recreation**: Can deleted tests be recreated and improved?

### AI Judge System
- **Recommended Judge**: Claude Sonnet for consistent evaluation
- **Automated Comparison**: Systematic comparison against baselines
- **Detailed Rationale**: Comprehensive scoring explanations
- **Cumulative Tracking**: Results accumulated over time

---

## Repository Structure

```
docs/benchmark/
├── judge/                          # Baseline references
│   ├── coder-base/                # Coder persona baseline
│   ├── business-analyst-base/     # Business analyst baseline
│   ├── architect-designer-base/   # Architect baseline
│   ├── technical-writer-base/     # Technical writer baseline
│   ├── tester-base/              # Tester baseline
│   └── project-manager-base/     # Project manager baseline
├── results/                       # Evaluation results
│   ├── ALL-EVALUATION-RESULTS.md # Cumulative results
│   ├── evaluation-results-*.md   # Individual evaluations
│   └── README.md                 # Results documentation
└── BENCHMARK-README.md           # This file

olaf-core/prompts/prompt-engineer/
├── run-persona-benchmark-evaluation.md      # Benchmark execution
└── evaluate-persona-benchmark-results.md    # Results evaluation
```

---

## Best Practices

### For Benchmark Execution
1. **One at a time**: Execute only one benchmark per session
2. **Clean environment**: Ensure clean working directory before starting
3. **Complete execution**: Finish all persona tasks before evaluation
4. **Document context**: Note any special circumstances or configurations

### For Evaluation
1. **Use Sonnet**: Recommended for consistent, high-quality evaluation
2. **Batch evaluation**: Can evaluate multiple branches in one session
3. **Review results**: Verify evaluation rationale makes sense
4. **Clean up**: Delete benchmark branches after successful evaluation

### For Analysis
1. **Track trends**: Monitor performance over time
2. **Compare agents**: Use results to compare different AI systems
3. **Identify patterns**: Look for persona-specific strengths/weaknesses
4. **Iterate improvements**: Use insights to enhance benchmark quality

---

## Getting Started

1. **Choose your parameters**:
   - Agent name (e.g., "windsurf", "gh-copilot", "kioro")
   - Model name (e.g., "sonnet-4", "sonnet-4.5", "gpt-5")
   - Persona (e.g., "coder", "business_analyst", "technical_writer")

2. **Run benchmark**:
   ```bash
   # Use the benchmark prompt with your parameters
   olaf-core/prompts/prompt-engineer/run-persona-benchmark-evaluation.md
   ```

3. **Complete tasks**: Execute all deliverables for your chosen persona

4. **Evaluate results**:
   ```bash
   # Use the evaluation prompt
   olaf-core/prompts/prompt-engineer/evaluate-persona-benchmark-results.md
   ```

5. **Review and cleanup**: Check results and delete benchmark branch

This system provides comprehensive, standardized evaluation of AI agents across multiple software development personas, enabling objective comparison and continuous improvement of AI capabilities.
