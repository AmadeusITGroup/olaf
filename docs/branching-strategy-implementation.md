# OLAF Branching Strategy Implementation Guide

**Created:** 20250911-0822 CEDT  
**Purpose:** Document the implementation process for OLAF's multi-branch development strategy

## Overview

This document outlines the step-by-step process to implement a clean branching strategy for OLAF, separating open source ready code from examples, archives, and research work.

## Final Branch Structure

```
main (clean open source ready)
├── integration (staging: research → main, syncs from main)
├── messy (current main snapshot - STATIC, never changes)
├── examples (main + examples, syncs from main + adds examples)
├── archives (experimental/deprecated content - NEVER merges to main)
├── research-context-indexing
├── research-ui-migration  
├── research-middleware-upgrade
└── research-design-to-code
```

## Implementation Process

### Phase 1: Create Base Branches from Current Main

**Step 1.1: Create messy branch (static snapshot)**
```bash
git checkout main
git checkout -b messy
git push -u origin messy
```

**Step 1.2: Create archives branch**
```bash
git checkout main
git checkout -b archives
git push -u origin archives
```

**Step 1.3: Create examples branch**
```bash
git checkout main
git checkout -b examples
git push -u origin examples
```

### Phase 2: Clean Each Branch

**Step 2.1: Clean messy branch**
- Keep: Current state as-is (no changes needed)
- Purpose: Static reference to original state

**Step 2.2: Clean archives branch**
- Keep: Only experimental/deprecated content
- Remove: Core framework, active examples, documentation
- Keep: `/archives/` directory content, deprecated experiments

**Step 2.3: Clean examples branch**
- Keep: Core framework + examples
- Remove: Internal/proprietary content, research experiments
- Keep: `/examples/` directory, `/docs/` with examples

**Step 2.4: Clean main branch**
- Keep: Core framework only
- Remove: Examples, archives, internal content, proprietary references
- Keep: Essential documentation, core prompts, templates

### Phase 3: Create Integration Branch

**Step 3.1: Create integration from cleaned main**
```bash
git checkout main
git checkout -b integration
git push -u origin integration
```

### Phase 4: Create Research Branches from Cleaned Main

**Step 4.1: Create research branches**
```bash
git checkout main
git checkout -b research-context-indexing
git push -u origin research-context-indexing

git checkout main
git checkout -b research-ui-migration
git push -u origin research-ui-migration

git checkout main
git checkout -b research-middleware-upgrade
git push -u origin research-middleware-upgrade

git checkout main
git checkout -b research-design-to-code
git push -u origin research-design-to-code
```

### Phase 5: Set Up Branch Documentation

Create `BRANCH-README.md` in each branch root (see templates below).

### Phase 6: Configure Sync Automation

Set up GitHub Actions for daily syncing:
- `main` → `integration`
- `main` → `examples`

## Branch README Templates

### Template for messy branch
```markdown
# Messy Branch

**Purpose:** Static snapshot of original main branch state  
**Status:** FROZEN - No changes allowed  
**Created:** [DATE]

This branch preserves the original state of main before cleanup for reference purposes.

**DO NOT:**
- Make any changes to this branch
- Merge from or to this branch
- Use as base for new work

**Use for:**
- Historical reference
- Recovering accidentally deleted content
```

### Template for archives branch
```markdown
# Archives Branch

**Purpose:** Experimental and deprecated content storage  
**Status:** ISOLATED - Never merges to main  
**Sync:** Independent, no automatic sync

This branch contains experimental work and deprecated content that should not be part of the main codebase.

**Contents:**
- Experimental features
- Deprecated code
- Research prototypes
- Legacy implementations

**DO NOT:**
- Merge to main or integration
- Sync from main

**Use for:**
- Storing experimental work
- Archiving deprecated features
- Reference for historical implementations
```

### Template for examples branch
```markdown
# Examples Branch

**Purpose:** Main codebase + comprehensive examples  
**Status:** ACTIVE - Syncs from main + adds examples  
**Sync:** Daily from main

This branch contains the clean main codebase plus extensive examples and demonstrations.

**Contents:**
- All main branch content
- Example implementations
- Demonstration code
- Tutorial materials

**Sync Strategy:**
- Pulls from main daily
- Can contribute examples back to main via integration

**Use for:**
- Learning and tutorials
- Example implementations
- Demonstration purposes
```

### Template for integration branch
```markdown
# Integration Branch

**Purpose:** Staging area for contributions to main  
**Status:** ACTIVE - Syncs from main, receives PRs from research  
**Sync:** Daily from main

This branch serves as the staging area for all contributions before they reach main.

**Workflow:**
- Syncs from main daily
- Receives PRs from research branches
- Creates clean PRs to main after review/cleanup

**Use for:**
- Staging research contributions
- Testing integration of multiple features
- Final cleanup before main
```

### Template for research branches
```markdown
# Research Branch: [TOPIC]

**Purpose:** Research and development for [specific topic]  
**Status:** ACTIVE - Independent development  
**Sync:** No automatic sync from main

This branch is dedicated to research and development of [specific functionality/topic].

**Research Focus:**
- [Specific research goals]
- [Key areas of investigation]
- [Expected outcomes]

**Contribution Process:**
1. Develop features independently
2. Create PR to integration when ready
3. Integration handles cleanup and main PR

**Use for:**
- Experimental development
- Feature prototyping
- Research implementation
```

## Sync Configuration

### GitHub Actions Workflow
Create `.github/workflows/sync-branches.yml`:

```yaml
name: Sync Branches
on:
  push:
    branches: [main]
  schedule:
    - cron: '0 9 * * *'  # Daily at 9 AM

jobs:
  sync-integration:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Sync main to integration
        run: |
          git checkout integration
          git merge main
          git push origin integration

  sync-examples:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Sync main to examples
        run: |
          git checkout examples
          git merge main
          git push origin examples
```

## Branch Policies

### Never Merge to Main
- `messy` (static reference)
- `archives` (isolated content)

### Contribution Flow
- Research branches → `integration` → `main`
- `examples` → `integration` → `main` (examples only)

### Sync Policies
- `integration`: Daily sync from main
- `examples`: Daily sync from main
- Research branches: Independent, no automatic sync
- `messy`: No sync (frozen)
- `archives`: No sync (isolated)

## Implementation Checklist

- [ ] Create messy branch from current main
- [ ] Create archives branch from current main  
- [ ] Create examples branch from current main
- [ ] Clean archives branch (keep only experimental/deprecated)
- [ ] Clean examples branch (keep core + examples)
- [ ] Clean main branch (keep core only)
- [ ] Create integration branch from cleaned main
- [ ] Create research branches from cleaned main
- [ ] Add BRANCH-README.md to each branch
- [ ] Set up GitHub Actions for sync
- [ ] Test sync workflows
- [ ] Document branch descriptions in GitHub
- [ ] Verify all branches are properly configured

## Maintenance

### Weekly Tasks
- Review research branch progress
- Check sync status
- Clean up stale branches

### Monthly Tasks  
- Review branch strategy effectiveness
- Update documentation as needed
- Archive completed research branches
