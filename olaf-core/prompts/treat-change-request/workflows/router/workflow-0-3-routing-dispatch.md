# Workflow 0-3: Routing & Dispatch

## Overview

**Purpose**: Route the sized change request to the appropriate orchestrator and create handoff documentation

**Input**: All artifacts from Workflows 0-1 and 0-2 (files 1-5) plus final size classification

**Output**: Context package YAML, routing summary, and README

---

## Prompt Execution

**Execute all prompts in sequence - no skipping**

### Prompt 0-3-1: Routing Logic

**File**: `../prompts/prompt-0-3-1-routing-logic.md`

**Input**: Files 1-5, final size classification

**Output**: `6-context-package.yaml`

**Validation**: Correct orchestrator selected, context package complete, all artifacts referenced

---

### Prompt 0-3-2: Routing Documentation

**File**: `../prompts/prompt-0-3-2-routing-documentation.md`

**Input**: `6-context-package.yaml`, all artifacts 1-5

**Output**: `7-routing-summary.md`, `README.md`

**Validation**: Routing rationale documented, critical highlights included, next steps clear

---

## Completion Criteria

✅ **Workflow complete when**:

1. All 3 output files exist (6-7 plus README)
2. Target orchestrator clearly identified
3. Context package ready for handoff
4. Router execution complete

---

## Handoff

**Next step**: Open and execute the size-specific orchestrator identified in `7-routing-summary.md`

**Provides**: Complete analysis directory with all 7+ files and routing decision
