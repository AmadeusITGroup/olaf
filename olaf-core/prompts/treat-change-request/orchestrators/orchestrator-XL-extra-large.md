# Orchestrator XL: Extra Large Changes

**Purpose**: Handle extra large, high-complexity, high-risk changes with full governance.

**Version**: 2.0  
**Last Updated**: October 8, 2025  
**Owner**: Engineering Architecture Team

---

## Overview

Handles **Extra Large (XL)** changes - multiple services/modules (>5), architectural changes, >20 days effort.

Executes four workflows in sequence:

1. Specification (complete)
2. Design (comprehensive)
3. Planning
4. Implementation

---

## Workflows

```
Orchestrator-XL-Extra-Large
├── Workflow 1: Specification
├── Workflow 2: Design
├── Workflow 3: Planning
└── Workflow 4: Implementation
```

---

## Inputs

Receives context package from **Orchestrator-0-Router** containing:
- Issue IDs and change request details
- Size classification (XL) and rationale
- Technical scope analysis
- Risk assessment
- Effort estimates
- All router artifacts

---

## Outputs

| Output | Description |
|--------|-------------|
| **Specification Artifacts** | Complete specification and architecture documentation |
| **Design Artifacts** | Comprehensive technical design documentation |
| **Planning Artifacts** | Implementation plan and task breakdown |
| **Implementation Artifacts** | Code, tests, validation results, deployment artifacts |
| **Tracking File** | Progress tracking for all workflows |

---

## Workflow Execution

### Workflow 1: Specification

**File**: `../workflows/XL/workflow-1-specification.md`

**Input**: Context package from router

**Validation**: Architecture review approved before proceeding

---

### Workflow 2: Design

**File**: `../workflows/XL/workflow-2-design.md`

**Input**: Artifacts from Workflow 1

**Validation**: Design review approved before proceeding

---

### Workflow 3: Planning

**File**: `../workflows/XL/workflow-3-planning.md`

**Input**: Artifacts from Workflow 2

**Validation**: Implementation plan complete before proceeding

---

### Workflow 4: Implementation

**File**: `../workflows/XL/workflow-4-implementation.md`

**Input**: Artifacts from Workflow 3

**Validation**: All validations passed, all reviews approved, production-ready

---

## Success Criteria

This orchestrator is successful when:

- ✅ All workflow outputs exist and validated
- ✅ Architecture review approved
- ✅ Design review approved
- ✅ Code reviews completed
- ✅ Security validation passed
- ✅ All test suites passing
- ✅ Performance validated
- ✅ Deployment plan verified
- ✅ Stakeholder sign-off obtained
- ✅ Code ready for deployment

---

## Escalation & De-escalation

**Escalation triggers** are monitored at each workflow completion.

**De-escalation** is possible if complexity lower than expected.

**Details**: See individual workflow files for specific escalation criteria and actions.

---

## Next Steps

After this orchestrator completes:

1. **Deploy** following deployment process
2. **Monitor** new functionality in production
3. **Document** lessons learned
4. **Retrospective** with team
5. **Update metrics** for future improvements

---

## End of Orchestrator

**Version**: 2.0  
**Execution Model**: Delegate to workflows (1 → 2 → 3 → 4)  
**Validation**: Check workflow outputs and approvals before completion
