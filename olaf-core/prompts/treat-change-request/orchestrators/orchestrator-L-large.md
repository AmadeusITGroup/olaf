# Orchestrator L: Large Changes

**Purpose**: Handle large, complex changes with comprehensive governance.

**Version**: 2.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Handles **Large (L)** changes - multiple services (3-5), 10-20 days effort.

Executes four workflows in sequence:

1. Specification (lighter than XL)
2. Design (full technical design)
3. Planning
4. Implementation

---

## Workflows

```
Orchestrator-L-Large
├── Workflow 1: Specification
├── Workflow 2: Design
├── Workflow 3: Planning
└── Workflow 4: Implementation
```

---

## Inputs

Receives context package from **Orchestrator-0-Router** containing:
- Issue IDs and change request details
- Size classification (L) and rationale
- Technical scope analysis
- Risk assessment
- All router artifacts

---

## Outputs

| Output | Description |
|--------|-------------|
| **Specification Artifacts** | Specification and architecture documentation |
| **Design Artifacts** | Technical design and review documentation |
| **Planning Artifacts** | Implementation plan and task breakdown |
| **Implementation Artifacts** | Code, tests, validation results |
| **Tracking File** | Progress tracking for all workflows |

---

## Workflow Execution

### Workflow 1: Specification

**File**: `../workflows/L/workflow-1-specification.md`

**Input**: Context package from router

**Validation**: Specification complete and approved before proceeding

---

### Workflow 2: Design

**File**: `../workflows/L/workflow-2-design.md`

**Input**: Artifacts from Workflow 1

**Validation**: Design complete and approved before proceeding

---

### Workflow 3: Planning

**File**: `../workflows/L/workflow-3-planning.md`

**Input**: Artifacts from Workflow 2

**Validation**: Implementation plan complete before proceeding

---

### Workflow 4: Implementation

**File**: `../workflows/L/workflow-4-implementation.md`

**Input**: Artifacts from Workflow 3

**Validation**: Code complete, tests passing, all reviews approved

---

## Success Criteria

This orchestrator is successful when:

- ✅ All workflow outputs exist and validated
- ✅ Specification approved
- ✅ Design approved
- ✅ Code reviews completed
- ✅ All validation checks passing
- ✅ Code ready for deployment

---

## Next Steps

After this orchestrator completes:

1. **Deploy** following deployment process
2. **Monitor** in production
3. **Document** lessons learned

---

## End of Orchestrator

**Version**: 2.0  
**Execution Model**: Delegate to workflows (1 → 2 → 3 → 4)  
**Validation**: Check workflow outputs before completion
