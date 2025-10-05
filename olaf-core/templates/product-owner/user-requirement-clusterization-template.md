# User Requirement Clusterization Template

## Overview

This template provides a structured approach to clustering user requirements gathered from GitHub issues. It helps group related requirements, identify duplicates while preserving all entries, and organize them into logical clusters for better management and prioritization.

## Template Structure

### 1. Clusterization Metadata

- **Analysis Date**: [YYYYMMDD-HHmm CEDT]
- **GitHub Repository**: [Repository URL]
- **Total Requirements Analyzed**: [Number]
- **Product Vision Reference**: [Path to product vision document]
- **Analyst**: [Name/Role]

### 2. Clustering Methodology

**Clustering Criteria**:
- [Criterion 1]: [Description - e.g., Functional similarity]
- [Criterion 2]: [Description - e.g., User persona alignment]
- [Criterion 3]: [Description - e.g., Technical domain]
- [Criterion 4]: [Description - e.g., Business value area]

**Duplicate Identification Rules**:
- [Rule 1]: [Description - e.g., Same core functionality requested]
- [Rule 2]: [Description - e.g., Similar user story with minor variations]
- [Rule 3]: [Description - e.g., Different wording but identical outcome]

### 3. Requirement Clusters

#### Cluster 1: [Cluster Name]

**Cluster Description**: [Brief description of what this cluster represents]

**Alignment with Product Vision**: [How this cluster aligns with the product vision]

**Requirements in this Cluster**:

| Issue ID | Title | Status | Description Summary | Duplicate of | Notes |
|----------|-------|--------|-------------------|--------------|-------|
| [#123] | [Issue Title] | [Status] | [Brief summary] | [Issue ID if duplicate] | [Additional notes] |
| [#124] | [Issue Title] | [Status] | [Brief summary] | [Issue ID if duplicate] | [Additional notes] |

**Cluster Characteristics**:
- **Primary User Persona**: [Which user persona this cluster serves]
- **Business Value Area**: [Which business area this impacts]
- **Technical Complexity**: [High/Medium/Low]
- **Dependencies**: [List any dependencies within or outside cluster]

#### Cluster 2: [Cluster Name]

[Repeat structure for each cluster]

### 4. Unclustered Requirements

**Standalone Requirements**:

| Issue ID | Title | Status | Reason for No Clustering | Notes |
|----------|-------|--------|-------------------------|-------|
| [#XXX] | [Issue Title] | [Status] | [Why it doesn't fit in clusters] | [Additional notes] |

### 5. Duplicate Analysis Summary

**Identified Duplicates**:

| Original Issue | Duplicate Issues | Consolidation Notes |
|----------------|------------------|-------------------|
| [#123] | [#145, #167] | [How to consolidate or which to prioritize] |

**Duplicate Handling Recommendations**:
- [Recommendation 1]: [e.g., Merge similar issues into primary issue]
- [Recommendation 2]: [e.g., Keep variations for different user contexts]
- [Recommendation 3]: [e.g., Close exact duplicates with reference]

### 6. Cross-Cluster Dependencies

**Inter-Cluster Dependencies**:

| Source Cluster | Target Cluster | Dependency Type | Description |
|----------------|----------------|-----------------|-------------|
| [Cluster A] | [Cluster B] | [Technical/Business/Sequential] | [Description of dependency] |

### 7. Cluster Statistics

**Cluster Distribution**:

| Cluster Name | Number of Requirements | Percentage of Total | Complexity Score |
|--------------|----------------------|-------------------|------------------|
| [Cluster 1] | [Count] | [%] | [High/Medium/Low] |
| [Cluster 2] | [Count] | [%] | [High/Medium/Low] |

### 8. Recommendations for Review

**Items Requiring Product Owner Review**:

1. **Ambiguous Clustering**: [List requirements that could fit multiple clusters]
2. **High-Impact Duplicates**: [List duplicate sets that need decision on consolidation]
3. **Vision Alignment Questions**: [List clusters/requirements with unclear vision alignment]
4. **Missing Context**: [List requirements needing more information]

### 9. Next Steps

**Recommended Actions**:

1. **Review Clustering**: [Specific areas needing product owner input]
2. **Resolve Duplicates**: [Decisions needed on duplicate handling]
3. **Validate Vision Alignment**: [Clusters needing vision alignment confirmation]
4. **Prepare for Prioritization**: [What's needed before prioritization phase]

---

## Usage Instructions

1. **Fill in metadata** with current analysis information
2. **Define clustering criteria** based on your product context
3. **Group requirements** into logical clusters using the criteria
4. **Identify duplicates** but preserve all entries with clear marking
5. **Document cluster characteristics** to support prioritization
6. **Highlight items** requiring product owner review
7. **Prepare recommendations** for next steps

## Best Practices

- **Preserve all requirements** - mark duplicates but don't remove them
- **Use consistent clustering criteria** throughout the analysis
- **Document reasoning** for clustering decisions
- **Identify edge cases** that don't fit neatly into clusters
- **Consider user journey** when creating clusters
- **Align clusters** with product vision themes
- **Prepare for prioritization** by documenting cluster characteristics

---
*Template created for OLAF Framework - Product Owner Competencies*
*Last Updated: 20241004-1038 Central European Time*
