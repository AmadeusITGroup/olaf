# Challenge Me Competency - User Guide

**Version**: 2.0 (Enhanced Multi-Source Research)  
**Last Updated**: 2025-10-15  
**Competency Path**: `olaf-core/prompts/researcher/challenge-me.md`

## Overview

The Challenge Me competency is an interactive ideation engine that challenges your ideas, provides insights, and tracks collaborative refinement through iterative cycles. The enhanced version now integrates multiple research sources including local codebases, documentation, and web resources to provide evidence-based challenges and insights.

## How It Works

```mermaid
flowchart TD
    A[User Request: "challenge me"] --> B[Parameter Collection]
    B --> C[Session Initialization]
    C --> D[Multi-Source Setup]
    D --> E[Iterative Cycles]
    E --> F{User Says Stop/Save?}
    F -->|No| G[Next Cycle]
    F -->|Yes| H[Generate Deliverables]
    
    D --> D1[Scan Codebase]
    D --> D2[Index Documentation]
    D --> D3[Prepare Web Search]
    
    G --> G1[Analyze Current Ideas]
    G --> G2[Research Codebase]
    G --> G3[Review Documentation]
    G --> G4[Web Research]
    G --> G5[Present Challenges]
    G --> G6[Generate Insights]
    G --> G7[Track Citations]
    G --> G8[Update Trajectory]
    G8 --> E
    
    H --> H1[think.md]
    H --> H2[path.md]
    H --> H3[sources.md]
```

## Getting Started

### Basic Usage
Simply type: `challenge me`

The system will prompt you for required parameters:

### Required Parameters
- **Subject**: The topic or subject area for ideation
- **Initial Thoughts**: Your starting ideas or description

### Optional Parameters
- **Codebase Path**: Path to local repository/codebase for analysis
- **Documentation Path**: Path to folder containing relevant documentation  
- **Web Search URLs**: Specific URLs for research or leave empty for general search
- **Research Depth**: shallow|moderate|deep (default: moderate)
- **Challenge Intensity**: gentle|moderate|rigorous (default: moderate)

### Example Session Start
```
User: challenge me
A
gent: I'll help you with an interactive ideation session. I need some information to get started:

**Subject**: What topic would you like to explore? (REQUIRED)
**Initial Thoughts**: What are your current ideas or thoughts on this topic? (REQUIRED)
**Codebase Path**: Do you have a local repository I should analyze? (Optional - provide path)
**Documentation Path**: Any documentation folder I should review? (Optional - provide path)
**Web Search URLs**: Specific URLs to research, or leave empty for general search (Optional)
**Research Depth**: How deep should I research? (shallow/moderate/deep - default: moderate)
**Challenge Intensity**: How aggressively should I challenge ideas? (gentle/moderate/rigorous - default: moderate)

User: 
Subject: API design patterns for microservices
Initial Thoughts: I'm thinking about using REST APIs with JSON, but wondering about GraphQL and event-driven patterns
Codebase Path: ./my-microservices-project
Documentation Path: ./docs/architecture
Web Search URLs: (leave empty for general search)
```

## Session Flow

### 1. Session Initialization
The system creates a unique session identifier and sets up multi-source research:

```
Session ID: api-design-patterns-20251015-1430
✓ Codebase scanned: ./my-microservices-project (15 services found)
✓ Documentation indexed: ./docs/architecture (8 documents)
✓ Web search strategy: General API design research
✓ Citation tracking initialized
```

### 2. Iterative Cycles

Each cycle follows this structure:

```mermaid
graph LR
    A[Analysis] --> B[Codebase Review]
    B --> C[Documentation Search]
    C --> D[Web Research]
    D --> E[Challenge Generation]
    E --> F[Insight Delivery]
    F --> G[Citation Tracking]
    G --> H[Trajectory Update]
    H --> I[User Response]
    I --> A
```

#### Cycle Example

**Cycle 1: Analysis Phase**
```
=== CYCLE 1 ===

ANALYSIS: Your current thinking focuses on REST vs GraphQL vs event-driven patterns. Let me examine your codebase and research to challenge this approach.

CODEBASE FINDINGS:
- Found 3 REST services using different authentication patterns
- Event bus implementation in /services/notification-service
- No GraphQL implementations detected
- Inconsistent error handling across services

DOCUMENTATION REVIEW:
- Architecture decision record favors REST for CRUD operations
- Event-driven pattern documented for async workflows
- No GraphQL evaluation found in decision records

WEB RESEARCH:
- Latest industry trends show hybrid approaches gaining traction
- Performance considerations for different patterns
- Team expertise requirements vary significantly

COLLABORATIVE CHALLENGES:

🤔 **Challenge 1: Pattern Consistency Strategy**
Your codebase shows inconsistent REST implementations. How do you plan to address this?

**A)** Standardize on the UserController authentication pattern across all services
**B)** Create new unified patterns and migrate existing services
**C)** Leave existing patterns and only standardize new services
**D)** I haven't considered the consistency issue yet

*Which approach aligns with your timeline and resources?*

💡 **Challenge 2: GraphQL Learning Curve**
You mention GraphQL but your team has no experience with it:

**1.** Invest in training and start with simple queries
**2.** Hire GraphQL expertise or consultants
**3.** Use GraphQL gateway tools to reduce complexity
**4.** Postpone GraphQL until team is ready

*What's your preferred strategy for building GraphQL capabilities?*

🔄 **Challenge 3: Event-Driven Evolution**
Your event bus is partially implemented:

**A)** Complete the current event-driven implementation first
**B)** Start fresh with a more comprehensive event architecture
**C)** Extend existing event bus incrementally
**D)** Focus on other patterns and revisit events later

*Which path makes most sense given your current investment?*

INSIGHTS BASED ON YOUR RESPONSES:
1. API gateway pattern could unify different service patterns
2. Hybrid approach: REST for CRUD, events for async, GraphQL for complex queries
3. Your existing event bus could be leveraged rather than replaced

SOURCES CONSULTED:
- /services/auth-service/api/controllers/UserController.java
- /docs/architecture/ADR-001-api-patterns.md
- https://martinfowler.com/articles/microservices.html

Your answers will help me provide more targeted recommendations in the next cycle. What resonates most with you from these questions?
```

### 3. User Response and Continuation
```
User: You're right about the consistency issues. I hadn't considered the hybrid approach. Can you explore how an API gateway would work with our current setup?

=== CYCLE 2 ===
[Next cycle begins with deeper analysis based on user response...]
```

## Multi-Source Research Integration

### Codebase Analysis
The system examines your code for:
- **Architecture patterns** and existing implementations
- **Code structure** and design decisions
- **Dependencies** and integration points
- **Comments and documentation** within code
- **Specific examples** to reference in challenges

### Documentation Review  
The system searches documentation for:
- **Decision records** and architectural choices
- **Best practices** and guidelines
- **Requirements** and constraints
- **Process documentation** and workflows
- **Related concepts** and specifications

### Web Research
The system conducts targeted research for:
- **Academic papers** and expert opinions
- **Industry best practices** and case studies
- **Current trends** and developments
- **Alternative approaches** and methodologies
- **Real-world examples** and implementations

## Output Files

When you say "save", the system generates four files in `olaf-data/findings/think-tank/<subject-3-words>-YYYYMMDD-HHMM/`:

### 1. think.md - Final Refined Ideas
Contains your final conclusions with source attribution:

```markdown
# API Design Patterns for Microservices - Final Design

**Session**: api-design-patterns-20251015-1430
**Date**: 2025-10-15 14:30 CEDT

## Final Refined Concept

### Hybrid API Strategy
Based on codebase analysis and research, implement a three-tier approach:
- REST APIs for CRUD operations (leveraging existing UserController patterns)
- Event-driven architecture for async workflows (extending current notification service)
- GraphQL gateway for complex query aggregation

### Architecture Decisions

#### 1. API Gateway Implementation
- Consolidate authentication patterns found in auth-service
- Route requests based on operation type
- Implement consistent error handling (addressing current inconsistencies)

[Source: /services/auth-service/api/controllers/UserController.java, ADR-001-api-patterns.md]

#### 2. Event-Driven Extensions
- Leverage existing event bus in notification-service
- Extend to order processing and inventory management
- Implement saga pattern for distributed transactions

[Source: /services/notification-service/EventBus.java, Richardson Microservices Patterns]
```

### 2. path.md - Evolution Trajectory
Documents how your thinking evolved through the session:

```markdown
# Ideation Trajectory - API Design Patterns

**Session**: api-design-patterns-20251015-1430
**Duration**: 5 cycles
**Evolution**: Single pattern focus → Hybrid multi-pattern strategy

## Initial State
**Subject**: API design patterns for microservices
**Starting Concept**: 
- REST vs GraphQL vs event-driven choice
- Single pattern selection approach
- Limited awareness of current codebase state

## Cycle 1: Reality Check
**Codebase Analysis**: Revealed inconsistent REST implementations
**Documentation Review**: Found existing ADR favoring REST for CRUD
**Challenges Presented**:
- Consistency issues in current implementation
- Team expertise gaps with GraphQL
- Partial event-driven implementation

**Key Insights**:
- Hybrid approach more practical than single pattern
- API gateway could unify different patterns
- Existing event bus underutilized

**Evolution**: Single pattern thinking → Multi-pattern strategy

## Cycle 2: Gateway Architecture Deep Dive
**Research Integration**: API gateway patterns and implementations
**Challenges Presented**:
- Gateway complexity vs. benefits
- Performance implications
- Team learning curve

**Key Refinements**:
- Phased implementation approach
- Leverage existing authentication patterns
- Start with routing, add features incrementally

**Evolution**: Theoretical gateway → Practical implementation plan
```

### 3. sources.md - Comprehensive Citations
Complete citation database organized by source type:

```markdown
# Research Sources - API Design Patterns Session

**Session**: api-design-patterns-20251015-1430
**Generated**: 2025-10-15 16:45 CEDT

## Codebase References

### Authentication Service
- **File**: `/services/auth-service/api/controllers/UserController.java`
- **Lines**: 45-67 (JWT token validation)
- **Relevance**: Existing authentication pattern for gateway integration
- **Cycles Used**: 1, 3, 4

### Notification Service  
- **File**: `/services/notification-service/EventBus.java`
- **Lines**: 12-89 (Event publishing mechanism)
- **Relevance**: Foundation for event-driven pattern extension
- **Cycles Used**: 1, 2, 5

### Order Service
- **File**: `/services/order-service/domain/OrderAggregate.java`
- **Lines**: 23-45 (Domain events)
- **Relevance**: Example of domain event implementation
- **Cycles Used**: 4, 5

## Documentation References

### Architecture Decision Records
- **Document**: `/docs/architecture/ADR-001-api-patterns.md`
- **Section**: "REST API Guidelines" (pages 2-4)
- **Relevance**: Existing architectural decisions and rationale
- **Cycles Used**: 1, 2, 3

### System Architecture
- **Document**: `/docs/architecture/system-overview.md`
- **Section**: "Service Communication Patterns" (page 7)
- **Relevance**: Current inter-service communication approach
- **Cycles Used**: 2, 4

## Web Resources

### Industry Best Practices
- **URL**: https://martinfowler.com/articles/microservices.html
- **Title**: "Microservices: a definition of this new architectural term"
- **Access Time**: 2025-10-15 14:52 CEDT
- **Key Excerpt**: "Smart endpoints and dumb pipes" principle
- **Relevance**: Foundational microservices communication principles
- **Cycles Used**: 1, 3

### API Gateway Patterns
- **URL**: https://microservices.io/patterns/apigateway.html
- **Title**: "API Gateway Pattern"
- **Access Time**: 2025-10-15 15:15 CEDT
- **Key Excerpt**: "Single entry point for all clients"
- **Relevance**: Gateway implementation guidance
- **Cycles Used**: 2, 3, 4

### Event-Driven Architecture
- **URL**: https://aws.amazon.com/event-driven-architecture/
- **Title**: "What is Event-Driven Architecture?"
- **Access Time**: 2025-10-15 15:33 CEDT
- **Key Excerpt**: "Loose coupling between producers and consumers"
- **Relevance**: Event pattern implementation strategies
- **Cycles Used**: 4, 5

## Cross-References

### Cycle 1 Sources
- Codebase: UserController.java, EventBus.java
- Documentation: ADR-001-api-patterns.md
- Web: Fowler microservices article

### Cycle 2 Sources  
- Codebase: EventBus.java (deeper analysis)
- Documentation: system-overview.md
- Web: API Gateway pattern, Kong documentation

### Cycle 3 Sources
- Codebase: All authentication services
- Documentation: ADR-001 (implementation details)
- Web: Gateway performance studies

[Additional cycles and sources...]

## Source Impact Analysis

### Most Influential Sources
1. **ADR-001-api-patterns.md**: Shaped understanding of existing decisions
2. **UserController.java**: Provided concrete authentication pattern
3. **Fowler microservices article**: Influenced hybrid approach thinking

### Research Gaps Identified
- No GraphQL evaluation in current documentation
- Limited performance testing data for current APIs
- Missing service mesh considerations

### Recommended Follow-up Research
- GraphQL vs REST performance comparison for your specific use cases
- Service mesh integration with API gateway patterns
- Team training resources for event-driven architecture
```

### 4. reco.md - Actionable Recommendations
NEW: Honest, actionable recommendations based on all cycle exchanges:

```markdown
# Recommendations - API Design Patterns Session

**Session**: api-design-patterns-20251015-1430
**Date**: 2025-10-15 16:45 CEDT

## Executive Summary

**RECOMMENDATION: PROCEED WITH HYBRID APPROACH** ✅

Implement the three-tier API strategy with phased rollout, starting with API gateway consolidation.

## Go/No-Go Decision

### **CONDITIONAL GO**
**Reasoning**: Hybrid approach addresses current inconsistencies while leveraging existing investments.

**Evidence**:
- Existing event bus provides foundation for extension
- Authentication patterns in UserController can be standardized
- Industry trends support hybrid API strategies
- Team has necessary skills for incremental implementation

## Alternative Approaches Considered

### **Rejected: Single Pattern Approach**
**Why Rejected**: Codebase analysis shows multiple patterns already in use
**Evidence**: REST, event-driven, and potential GraphQL needs all identified

### **Considered: Complete Rewrite**
**Why Not Recommended**: Existing implementations have value and team knowledge
**Risk**: High disruption, longer timeline, potential regression

## Risk Assessment

### **Medium Risks**
1. **Implementation Complexity**: API gateway adds architectural complexity
2. **Team Learning Curve**: GraphQL expertise needs development
3. **Performance Impact**: Gateway could introduce latency

### **Mitigation Strategies**
1. **Phased Implementation**: Start with routing, add features incrementally
2. **Training Plan**: GraphQL workshops and proof-of-concept projects
3. **Performance Testing**: Baseline current performance, monitor gateway impact

## Specific Next Steps

### **Phase 1: Foundation (Weeks 1-4)**
1. **Implement API Gateway**: Basic routing and authentication consolidation
2. **Standardize Error Handling**: Apply consistent patterns across services
3. **Performance Baseline**: Measure current API response times

### **Phase 2: Event Extension (Weeks 5-8)**
1. **Extend Event Bus**: Add order processing and inventory management
2. **Implement Saga Pattern**: For distributed transaction handling
3. **Monitor Event Flow**: Add observability for async operations

### **Phase 3: GraphQL Integration (Weeks 9-12)**
1. **GraphQL Gateway**: Implement for complex query aggregation
2. **Schema Design**: Create unified schema for client queries
3. **Performance Optimization**: Cache and optimize query execution

## Success Criteria

### **Phase 1 Success Metrics**
- [ ] All services use consistent authentication (from UserController pattern)
- [ ] Error responses follow unified format
- [ ] API gateway handles 95% of requests without issues
- [ ] Response time increase <10% due to gateway

### **Phase 2 Success Metrics**
- [ ] Order processing fully event-driven
- [ ] Saga pattern handles distributed transactions
- [ ] Event bus processes 1000+ events/minute reliably

### **Phase 3 Success Metrics**
- [ ] GraphQL handles complex queries efficiently
- [ ] Client applications use GraphQL for data aggregation
- [ ] Query response times <200ms for typical operations

## Resource Requirements

### **Team Skills Needed**
- **API Gateway**: 1 senior developer, 2 weeks
- **Event-Driven**: 1 developer familiar with current event bus, 3 weeks
- **GraphQL**: 1 developer + training, 4 weeks

### **Infrastructure**
- **Gateway Deployment**: Container orchestration setup
- **Monitoring**: Enhanced observability for distributed patterns
- **Testing**: Integration test suite for hybrid patterns

### **Budget Considerations**
- **Training Costs**: GraphQL workshops and certification
- **Infrastructure**: Additional compute for gateway and monitoring
- **Timeline**: 12-week implementation with parallel development

## Honest Assessment

### **Strengths of This Approach**
- Leverages existing investments and team knowledge
- Addresses identified consistency issues
- Aligns with industry best practices
- Provides incremental value delivery

### **Potential Challenges**
- Increased architectural complexity
- Need for new monitoring and debugging approaches
- Team learning curve for GraphQL
- Coordination across multiple services

## Final Recommendation

**PROCEED WITH CONFIDENCE**

The hybrid approach is well-suited to your current situation:
1. **Builds on existing strengths** (event bus, authentication patterns)
2. **Addresses identified problems** (consistency, error handling)
3. **Provides future flexibility** (can adjust patterns based on experience)
4. **Manageable risk profile** with clear mitigation strategies

**Key Success Factors**:
- Maintain focus on incremental delivery
- Invest in team training and knowledge sharing
- Implement comprehensive monitoring from day one
- Regular retrospectives to adjust approach based on learnings

---

**Confidence Level**: High (based on thorough codebase analysis, documentation review, and industry research alignment)
```

## Enhanced Collaborative Features

### Interactive Question Formats
The system uses specific formatting for different types of engagement:

**Numbered Lists (1, 2, 3, 4)** for:
- Choice-based questions (selecting between options)
- Priority rankings and polls
- Decision-oriented prompts

**Lettered Lists (A, B, C, D)** for:
- Clarification questions (what do you mean by...?)
- Vision/perspective requests (how do you see...?)
- Understanding checks (which resonates with you?)

### Collaborative Engagement Rules
- **Never repeats questions** - always builds on previous responses
- **Presents web feedback** and asks for your perspective
- **Invites explanation** rather than making assumptions
- **Uses multiple-choice formats** to keep you actively involved
- **Builds trajectory** based on your responses and reasoning

## Advanced Features

### Citation Tracking
Every insight and challenge is backed by specific sources:
- **Code references**: File paths, line numbers, specific functions
- **Documentation**: Document names, sections, page numbers  
- **Web resources**: Full URLs, titles, access timestamps

### Multi-Source Synthesis
The system combines findings from all sources to provide:
- **Evidence-based challenges** grounded in your actual codebase
- **Contextual insights** informed by your documentation
- **Industry-validated approaches** from web research

### Trajectory Visualization
Track how your ideas evolve through visual trajectory mapping:

```mermaid
graph TD
    A[Initial: REST vs GraphQL choice] --> B[Cycle 1: Consistency challenges]
    B --> C[Cycle 2: Hybrid approach insight]
    C --> D[Cycle 3: Gateway architecture]
    D --> E[Cycle 4: Implementation strategy]
    E --> F[Final: Phased hybrid solution]
    
    B1[Codebase: Inconsistent patterns] --> B
    B2[Docs: REST preference] --> B
    B3[Web: Industry trends] --> B
    
    C1[Code: Event bus potential] --> C
    C2[Web: Gateway patterns] --> C
    
    D1[Code: Auth patterns] --> D
    D2[Docs: System overview] --> D
    D3[Web: Performance data] --> D
```

## Best Practices

### Preparing for a Session
1. **Organize your codebase**: Ensure the path is accessible and well-structured
2. **Prepare documentation**: Have relevant docs in a single folder
3. **Define clear scope**: Be specific about what aspect you want to explore
4. **Set realistic expectations**: Complex topics may need multiple sessions

### During the Session
1. **Engage actively**: Respond thoughtfully to challenges
2. **Ask for clarification**: If sources seem unclear, ask for specifics
3. **Challenge back**: The system learns from your pushback
4. **Request deeper dives**: Ask to explore specific sources more thoroughly

### After the Session
1. **Review all three files**: Each provides different value
2. **Follow citation trails**: Explore referenced sources independently
3. **Plan implementation**: Use insights for concrete next steps
4. **Schedule follow-ups**: Complex topics benefit from multiple sessions

## Troubleshooting

### Common Issues

**"Codebase path not found"**
- Verify the path is correct and accessible
- Use relative paths from your current directory
- The system will continue without codebase analysis if needed

**"Too many sources overwhelming the discussion"**
- Request focus on specific source types
- Ask for prioritization of most relevant sources
- Use "shallow" research depth for simpler sessions

**"Citations seem incomplete"**
- The system maintains manual backups if tracking fails
- Request specific source verification during cycles
- Check sources.md for comprehensive citation database

**"Cycles becoming repetitive"**
- Ask for new research angles or unexplored sources
- Request deeper analysis of specific findings
- Consider switching to different documentation areas

### Getting Help
- Use "explain your reasoning" to understand source selection
- Ask "what sources are you consulting?" for transparency
- Request "show me the specific code/doc section" for verification

## New Recommendations System

### Honest Assessment Promise
Every session now produces actionable recommendations that can include:
- **Go/No-Go decisions** with clear reasoning
- **Alternative approaches** if current path isn't recommended
- **Negative recommendations** ("don't do it" with alternatives)
- **Risk assessments** and mitigation strategies
- **Specific next steps** with timelines and resources

### Real-World Recommendation Examples
The competency provides honest guidance even when it contradicts your initial ideas:

**Positive Recommendation**: "Proceed with hybrid approach - evidence supports this direction"
**Negative Recommendation**: "Pause and clarify - current approach contradicts stated goals"
**Alternative Recommendation**: "Study multi-provider abstraction instead of AWS-only approach"

### Four-File Deliverable System
1. **think.md** - Final refined ideas and conclusions
2. **path.md** - How your thinking evolved through cycles
3. **sources.md** - Complete citation database
4. **reco.md** - Honest, actionable recommendations

## Example Sessions

The enhanced competency has been used successfully for topics like:
- **API design patterns** (collaborative challenges with multiple-choice questions)
- **Database architecture decisions** (with honest go/no-go recommendations)
- **Testing strategy refinement** (using lettered lists for clarification)
- **Performance optimization approaches** (with alternative approach suggestions)
- **Security implementation patterns** (including negative recommendations when appropriate)

Each session produces comprehensive documentation with full source attribution and actionable recommendations, making the insights immediately useful for decision-making.

---

*This guide covers the enhanced Challenge Me competency with collaborative engagement and honest recommendations. The system will actively involve you in the ideation process and provide actionable guidance based on evidence gathered from your codebase, documentation, and web research.*