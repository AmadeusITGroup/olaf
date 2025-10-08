# Orchestrator M: Medium Changes

**Purpose**: Handle medium changes with standard governance.

**Version**: 2.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Handles **Medium (M)** changes - 2-3 services/modules, 5-10 days effort.

Executes three workflows in sequence:

1. Design (full technical design)
2. Planning
3. Implementation

---

## Workflows

```
Orchestrator-M-Medium
├── Workflow 2: Design
├── Workflow 3: Planning
└── Workflow 4: Implementation
```

---

## Inputs

Receives context package from **Orchestrator-0-Router** containing:
- Issue IDs and change request details
- Size classification (M) and rationale
- Technical scope analysis
- All router artifacts

---

## Outputs

| Output | Description |
|--------|-------------|
| **Design Artifacts** | Technical design and review documentation |
| **Planning Artifacts** | Implementation plan and task breakdown |
| **Implementation Artifacts** | Code, tests, validation results |
| **Tracking File** | Progress tracking for all workflows |

---

## Workflow Execution

### Workflow 2: Design

**File**: `../workflows/M/workflow-2-design.md`

**Input**: Context package from router

**Validation**: Design complete and approved before proceeding

---

### Workflow 3: Planning

**File**: `../workflows/M/workflow-3-planning.md`

**Input**: Artifacts from Workflow 2

**Validation**: Implementation plan complete before proceeding

---

### Workflow 4: Implementation

**File**: `../workflows/M/workflow-4-implementation.md`

**Input**: Artifacts from Workflow 3

**Validation**: Code complete, tests passing, reviews approved

---

## Success Criteria

This orchestrator is successful when:

- ✅ All workflow outputs exist and validated
- ✅ Design review completed and approved
- ✅ Code review completed
- ✅ All validation checks passing
- ✅ Code ready for merge

---

## Next Steps

After this orchestrator completes:

1. **Merge code** following team merge process
2. **Deploy** following standard deployment process
3. **Monitor** in production

---

## End of Orchestrator

**Version**: 2.0  
**Execution Model**: Delegate to workflows (2 → 3 → 4)  
**Validation**: Check workflow outputs before completion
