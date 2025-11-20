# Challenge Me

## Overview

This competency provides interactive ideation through evidence-based challenges and collaborative refinement. It systematically explores ideas using multi-source research (codebase, documentation, web) and generates comprehensive recommendations with full source attribution.

## Purpose

Ideas often fail due to unexamined assumptions, incomplete analysis, or lack of evidence. This competency addresses this by challenging ideas constructively through iterative cycles, integrating research from multiple sources, and producing honest recommendations backed by evidence rather than assumptions.

## Usage

**Command**: `olaf challenge me`

**Protocol**: Act

**When to Use**: Use this competency when exploring new ideas, validating technical approaches, evaluating strategic decisions, or seeking evidence-based analysis before committing to a direction.

## Parameters

### Required Inputs
- **subject**: The topic or idea to explore
- **initial_thoughts**: Your current thinking about the subject

### Optional Inputs
- **codebase_path**: Path to local repository for code analysis
- **documentation_path**: Path to documentation folder for context
- **web_search_urls**: Specific URLs for targeted research
- **research_depth**: shallow | moderate | deep (default: moderate)
- **challenge_intensity**: gentle | moderate | rigorous (default: moderate)

### Context Requirements
- Optional access to codebase for technical feasibility analysis
- Optional access to documentation for constraint discovery
- Optional web search for external insights and case studies

## Output

This competency produces four deliverables when you say "save".

**Deliverables**:
- **think.md**: Final refined ideas with comprehensive details
- **path.md**: Complete trajectory showing evolution of thinking
- **sources.md**: Comprehensive citations organized by source type
- **reco.md**: Honest recommendations with go/no-go decisions

**Format**: Structured markdown documents saved to `olaf-data/findings/` with timestamp naming convention.

## Examples

### Example 1: Technical Feasibility Assessment

**Scenario**: Evaluating whether to add a caching layer to improve application performance.

**Command**:
```
"olaf challenge me"
with subject="Adding Redis caching layer to improve performance"
with initial_thoughts="We should add Redis caching to reduce database load and improve response times from 300ms to under 50ms"
with codebase_path="./src/api"
```

**Result**: Analysis revealed that caching addresses only 50% of latency (database queries), with business logic and network overhead contributing the rest. Recommendation: optimize queries first (lower risk, faster implementation), then evaluate if caching still needed. Generated think.md with refined approach, path.md documenting the exploration, sources.md with code references, and reco.md with phased implementation plan.

### Example 2: Strategic Decision Validation

**Scenario**: Deciding whether to migrate from monolith to microservices architecture.

**Command**:
```
"olaf challenge me"
with subject="microservices migration strategy"
with initial_thoughts="We should break the monolith into 20 services"
with codebase_path="./src"
with documentation_path="./docs/architecture"
with research_depth="deep"
```

**Result**: Multi-source analysis identified team experience gaps, deployment complexity, and data consistency challenges. Recommendation included alternative approaches (modular monolith, service extraction) with risk assessment and resource requirements for each option.

## Related Competencies

- **analyze-business-requirements**: Use after Challenge Me to formalize requirements from refined ideas
- **generate-tech-spec-from-code**: Use to create technical specifications from validated approaches
- **evaluate-technology**: Use for formal technology assessment after exploration
- **create-decision-record**: Use to document strategic decisions with evidence from reco.md

## Tips & Best Practices

- Provide codebase and documentation paths for context-aware challenges
- Engage actively with questions rather than just saying "continue"
- Choose research depth based on decision importance (shallow for quick validation, deep for strategic decisions)
- Review all four deliverables, especially reco.md for honest assessment
- Use gentle intensity for early exploration, rigorous for high-stakes decisions
- Follow up with related competencies to formalize findings

## Limitations

- Provides recommendations, not decisions—requires human judgment for final choices
- Research quality depends on available sources (codebase, docs, web access)
- Cannot validate business logic correctness—focuses on approach and feasibility
- Requires active engagement—passive "continue" responses limit refinement quality
- Does not replace domain expertise—augments analysis with evidence and alternative perspectives

---

**Source**: `olaf-core/competencies/researcher/prompts/challenge-me.md`
