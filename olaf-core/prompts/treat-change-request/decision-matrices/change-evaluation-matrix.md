# Change Evaluation Matrix

**Purpose**: Determine the size classification (XL/L/M/S/XS) of a change request based on objective criteria.

**Usage**: This matrix is used by Orchestrator-0-Router to evaluate incoming issues and route them to the appropriate orchestrator.

---

## Evaluation Criteria

### 1. Scope of Change

| Factor | XL | L | M | S | XS |
|--------|----|----|----|----|-----|
| **Files Changed** | >30 | 15-30 | 8-15 | 3-7 | 1-2 |
| **Modules/Services Impacted** | >5 | 3-5 | 2-3 | 1-2 | 1 |
| **Lines of Code (estimated)** | >2000 | 1000-2000 | 500-1000 | 100-500 | <100 |

### 2. Technical Complexity

| Factor | XL | L | M | S | XS |
|--------|----|----|----|----|-----|
| **API Changes** | Breaking changes across services | Breaking changes in one service | New endpoints (backward compatible) | Internal API only | No API changes |
| **Database Changes** | Schema migration + data migration | Schema changes only | New tables/columns | Index/constraint changes | Query changes only |
| **Architecture Impact** | New components/services | Significant refactoring | Module restructuring | Component modification | Function/method level |
| **Integration Points** | Multiple external systems | 2-3 external systems | 1 external system | Internal only | No integration |

### 3. Risk Assessment

| Factor | XL | L | M | S | XS |
|--------|----|----|----|----|-----|
| **Business Impact** | Revenue/compliance critical | High visibility features | Standard features | Internal improvements | Bug fixes, tweaks |
| **User Impact** | All users affected | Major user segment | Specific user group | Internal users | Minimal/no user impact |
| **Rollback Complexity** | Very difficult/impossible | Complex rollback | Standard rollback | Easy rollback | Trivial rollback |
| **Security Impact** | Authentication/Authorization | Data protection | API security | Internal security | No security impact |

### 4. Effort & Duration

| Factor | XL | L | M | S | XS |
|--------|----|----|----|----|-----|
| **Estimated Effort** | >20 days | 10-20 days | 5-10 days | 2-5 days | <2 days |
| **Team Size Required** | Multiple teams | 1 team (multiple devs) | 2-3 developers | 1-2 developers | 1 developer |
| **Dependencies** | Multiple teams/projects | Cross-team | Within team | Single developer | None |

### 5. Compliance & Governance

| Factor | XL | L | M | S | XS |
|--------|----|----|----|----|-----|
| **Regulatory Impact** | Requires legal/compliance review | Audit trail required | Standard compliance | Internal policy only | No compliance impact |
| **Documentation Required** | Full architecture docs | Technical design docs | Design notes | Code comments | Minimal |
| **Approval Chain** | Executive/architect sign-off | Senior tech lead | Tech lead | Peer review | Self-review acceptable |

---

## Scoring Method

### Step 1: Evaluate Each Category
Rate each of the 5 categories (Scope, Complexity, Risk, Effort, Compliance) on the XL/L/M/S/XS scale.

### Step 2: Calculate Base Score
- XL = 5 points
- L = 4 points
- M = 3 points
- S = 2 points
- XS = 1 point

Add up the points from all 5 categories. Maximum = 25, Minimum = 5.

### Step 3: Determine Size Classification

| Total Score | Size Classification |
|-------------|---------------------|
| 21-25 | **XL** (Extra Large) |
| 16-20 | **L** (Large) |
| 11-15 | **M** (Medium) |
| 7-10 | **S** (Small) |
| 5-6 | **XS** (Extra Small) |

### Step 4: Apply Project Complexity Modifier

**Important**: The final size classification must consider the **Project Complexity Rating** (see `project-complexity-rating.md`).

**Escalation Rules**:
- If project is **Critical** or **Complex**: Consider escalating by +1 size level
- If project is **Simple** or **Pet**: Consider de-escalating by -1 size level (minimum XS)
- If project is **Regular**: No adjustment

**Example**: 
- Change scores as **M** (Medium) + Project is **Critical** → Final classification: **L** (Large)
- Change scores as **S** (Small) + Project is **Pet** → Final classification: **XS** (Extra Small)

---

## Decision Matrix Example

### Example 1: New Feature - Multi-Region Deployment Support

| Category | Rating | Points | Justification |
|----------|--------|--------|---------------|
| Scope | L | 4 | 5 modules affected, ~1500 LOC |
| Complexity | XL | 5 | New infrastructure components, multi-service coordination |
| Risk | L | 4 | Affects deployment process for all services |
| Effort | L | 4 | 15 days, multiple developers |
| Compliance | M | 3 | Standard documentation |
| **Total** | | **20** | **→ L (Large)** |

**Project Complexity**: Complex
**Final Classification**: **XL** (escalated due to project complexity)

### Example 2: Bug Fix - Incorrect Date Format

| Category | Rating | Points | Justification |
|----------|--------|--------|---------------|
| Scope | XS | 1 | 1 file, <50 LOC |
| Complexity | XS | 1 | Simple logic fix |
| Risk | S | 2 | Affects reporting only |
| Effort | XS | 1 | <1 day |
| Compliance | XS | 1 | Minimal documentation |
| **Total** | | **6** | **→ XS (Extra Small)** |

**Project Complexity**: Regular
**Final Classification**: **XS** (no change)

---

## Special Cases

### When to Override the Matrix

Even with the matrix, human judgment is important. Consider escalating if:
- **High uncertainty**: Requirements are vague or likely to change significantly
- **First-time implementation**: New technology or pattern for the team
- **Multiple unknowns**: Several technical unknowns that need investigation
- **Political sensitivity**: High visibility or stakeholder attention

### When in Doubt
**Err on the side of caution**: Choose the larger size. It's easier to de-escalate during execution than to realize mid-project that you need more governance.

---

## Usage in Router

The Orchestrator-0-Router will:
1. Collect all relevant information about the change request(s)
2. Evaluate each of the 5 categories
3. Calculate the total score
4. Apply project complexity modifier
5. Determine final size classification
6. Route to appropriate orchestrator (XL/L/M/S/XS)
7. Document the sizing rationale for future reference

---

**Last Updated**: October 8, 2025
**Owner**: Engineering Architecture Team
**Review Frequency**: Quarterly
