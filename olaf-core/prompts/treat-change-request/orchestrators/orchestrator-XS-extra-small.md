# Orchestrator XS: Extra Small Changes

**Purpose**: Handle extra small changes with minimal governance.

**Version**: 2.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Handles **Extra Small (XS)** changes - single service, minimal files, <2 days effort.

Executes two workflows in sequence:
1. Planning
2. Implementation

---

## Workflows

```
Orchestrator-XS-Extra-Small
├── Workflow 3: Planning
└── Workflow 4: Implementation
```

---

## Inputs

Receives context package from **Orchestrator-0-Router** containing:
- Issue IDs and change request details
- Size classification (XS) and rationale
- Technical scope analysis
- All router artifacts

---

## Outputs

| Output | Description |
|--------|-------------|
| **Planning Artifacts** | Implementation plan and task breakdown |
| **Implementation Artifacts** | Code, tests, validation results |
| **Tracking File** | Progress tracking for all workflows |

---

## Workflow Execution

### Workflow 3: Planning

**File**: `../workflows/XS/workflow-3-planning.md`

**Input**: Context package from router

**Validation**: Required outputs exist before proceeding to implementation

---

### Workflow 4: Implementation

**File**: `../workflows/XS/workflow-4-implementation.md`

**Input**: Artifacts from Workflow 3

**Validation**: Code complete, tests passing, peer review approved

---

## Success Criteria

This orchestrator is successful when:

- ✅ All workflow outputs exist and validated
- ✅ Peer review completed
- ✅ Automated checks passing
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
**Execution Model**: Delegate to workflows (3 → 4)  
**Validation**: Check workflow outputs before completion
