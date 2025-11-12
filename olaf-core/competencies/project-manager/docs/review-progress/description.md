# Review Progress

## Overview

Conducts comprehensive work reviews to assess project progress, identify accomplishments and challenges, analyze performance metrics, and plan upcoming priorities with data-driven insights.

## Purpose

Project managers need regular visibility into project health and progress. This competency solves the problem of fragmented progress information by systematically gathering data from multiple sources, analyzing performance against goals, identifying trends and blockers, and producing actionable reports that inform decision-making and planning.

## Usage

**Command**: `review progress`

**Protocol**: Act

**When to Use**: Use this competency for sprint retrospectives, monthly status reviews, quarterly business reviews, stakeholder reporting, or whenever you need to assess project health, evaluate team performance, identify risks, or make data-driven decisions about priorities and resource allocation.

## Parameters

### Required Inputs
- **review_period**: Time period to analyze (e.g., "past 7 days", "Q4 2025", "Sprint 12", "October 2025")

### Optional Inputs
- **focus_areas**: Specific projects, features, or metrics to emphasize in the review
- **team_members**: Specific team members to include in performance analysis
- **metrics**: Key performance indicators to evaluate (velocity, quality, delivery, cycle time, etc.)

### Context Requirements
- Access to work logs, changelogs, and activity data
- Access to job records and task completion data
- Access to project goals, OKRs, or success criteria
- Historical data for trend analysis and comparison

## Output

**Deliverables**:
- Comprehensive progress review document following the progress review template
- Executive summary with key findings and recommendations
- Detailed analysis of goals vs. actuals with variance explanations
- Performance metrics and trend analysis
- Risk identification and mitigation recommendations
- Prioritized action items for the next period

**Format**: Structured markdown document with sections for overview, detailed analysis, accomplishments, challenges, metrics, and next steps.

## Examples

### Example 1: Sprint Retrospective

**Scenario**: Reviewing 2-week sprint performance

**Command**:
```
review progress
```

**Input**:
```
Review Period: Sprint 12 (Oct 14-27, 2025)
Focus Areas: User authentication feature, Bug fixes
Metrics: Velocity, Quality, Delivery
```

**Result**: Generated report showing 85% story point completion, 12 bugs fixed, authentication feature 90% complete, identified testing bottleneck, recommended adding QA resource for next sprint

### Example 2: Monthly Status Review

**Scenario**: Creating monthly report for stakeholders

**Command**:
```
review progress
```

**Input**:
```
Review Period: October 2025
Team Members: All
Metrics: Delivery, Quality, Customer satisfaction
```

**Result**: Comprehensive report with 47 completed tasks, 3 major features delivered, 95% test coverage maintained, customer satisfaction score 4.2/5, identified need for documentation improvements

### Example 3: Quarterly Business Review

**Scenario**: Assessing Q4 performance against annual goals

**Command**:
```
review progress
```

**Input**:
```
Review Period: Q4 2025
Focus Areas: Revenue features, Platform stability, Team growth
Metrics: Feature delivery, System uptime, Team capacity
```

**Result**: Strategic review showing 8 of 10 planned features delivered, 99.7% uptime achieved, team grew from 5 to 8 members, recommended Q1 focus on technical debt and scalability

## Related Competencies

- **analyze-changelog-and-report**: Provides detailed changelog analysis that feeds into progress reviews
- **work-on-job**: Job completion data is analyzed during progress reviews
- **generate-tasklist**: Task completion rates inform velocity and capacity assessments
- **create-decision-record**: Progress reviews may identify decisions that need formal documentation
- **prepare-conversation-handover**: Progress review findings can be included in handover documentation

## Tips & Best Practices

- Schedule progress reviews at regular intervals aligned with your project cadence (weekly, bi-weekly, monthly)
- Gather data before the review session to make the review process efficient
- Focus on both quantitative metrics (velocity, completion rates) and qualitative insights (team morale, blockers)
- Compare current period against previous periods to identify trends and patterns
- Be objective and data-driven - avoid subjective assessments without supporting evidence
- Include both successes and challenges - balanced reviews are more credible and actionable
- End every review with clear, prioritized action items and owners
- Share review findings with all stakeholders to maintain transparency and alignment

## Limitations

- Quality of review depends on quality of underlying data - incomplete logs produce incomplete reviews
- Cannot automatically gather all relevant data - some information requires manual collection
- Does not automatically compare against goals unless goals are explicitly documented
- Trend analysis requires historical data - first review will have limited comparative insights
- Does not automatically notify stakeholders - distribution of review findings is manual
- Subjective assessments (team morale, quality) require human judgment beyond metrics

**Source**: `olaf-core/competencies/project-manager/prompts/review-progress.md`
