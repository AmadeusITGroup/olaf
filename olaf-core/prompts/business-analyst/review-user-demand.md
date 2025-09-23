---
name: review-user-demand
description: Guide users through structured requirements gathering using systematic questioning techniques to capture clear, complete, and actionable business needs
tags: [requirements, elicitation, business-analysis, stakeholder-engagement]
---

## Framework Validation
- Validate user has provided initial problem description or context
- Ensure structured questioning approach is followed
- Confirm all impact dimensions are explored
- Validate completeness before generating final requirement document

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Parameters
- `initial_context` (required): Initial problem description or user request
- `project_name` (required): Name of the project for file naming
- `user_role` (optional): Role/position of the person making the request
- `application_system` (optional): Target application or system involved
- `session_language` (optional): Language for conducting session - "english", "french", "spanish", "german" (default: "english")
- `session_duration` (optional): Available time for requirements gathering session (default: 45 minutes)
- `output_format` (optional): "interactive" or "document" (default: "interactive")

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Use Act for non-destructive elicitation sessions
- Use Propose-Act when recommending follow-up actions or next steps

## Execution Phase

### Language Selection
You WILL determine session language at start:
- If `session_language` parameter provided, use specified language throughout
- If not provided, ask user: "Which language would you prefer for this session? (English/Français/Español/Deutsch)" 
- If user doesn't respond or says "default", use English
- Adapt ALL questioning frameworks, progress updates, and outputs to selected language
- Maintain consistent language throughout entire session

### Phase 1: Context Understanding (5-10 minutes)
You WILL conduct structured information gathering through systematic questioning:

**Core Logic:**
- Guide user through context exploration using proven questioning techniques
- Focus on WHO, WHAT, WHERE, WHEN without jumping to solutions
- Capture current state and trigger events that motivated the request
- Map stakeholder ecosystem and system boundaries

**Questioning Framework:**
1. "Can you tell me about your role and what you do daily?"
2. "Which application/system is involved in this need?"
3. "How long have you been using this system?"
4. "Who else on your team uses this system?"
5. "What prompted you to make this request now?"

**Questioning Framework (French):**
1. "Pouvez-vous me parler de votre rôle et de ce que vous faites au quotidien ?"
2. "Quelle application/système est concerné par ce besoin ?"
3. "Depuis combien de temps utilisez-vous ce système ?"
4. "Qui d'autre dans votre équipe utilise ce système ?"
5. "Qu'est-ce qui vous a motivé à faire cette demande maintenant ?"

**Questioning Framework (German):**
1. "Können Sie mir von Ihrer Rolle und Ihren täglichen Aufgaben erzählen?"
2. "Welche Anwendung/System ist von diesem Bedarf betroffen?"
3. "Wie lange nutzen Sie dieses System bereits?"
4. "Wer sonst in Ihrem Team nutzt dieses System?"
5. "Was hat Sie dazu veranlasst, diese Anfrage jetzt zu stellen?"

### Phase 2: Problem Definition (10-15 minutes)
You WILL systematically explore the problem space:

**Core Logic:**
- Use story-based questioning to capture concrete examples
- Quantify frequency, impact, and current workarounds
- Identify root causes vs. symptoms
- Document current state constraints and limitations

**Questioning Framework:**
1. "Tell me about a recent situation where you encountered this problem"
2. "How often does this happen?"
3. "What do you currently do to work around this problem?"
4. "How much time does this cost you?"
5. "What prevents the current system from meeting your needs?"

**Questioning Framework (German):**
1. "Erzählen Sie mir von einer kürzlichen Situation, in der Sie dieses Problem hatten"
2. "Wie oft passiert das?"
3. "Was machen Sie derzeit, um dieses Problem zu umgehen?"
4. "Wie viel Zeit kostet Sie das?"
5. "Was hindert das aktuelle System daran, Ihre Bedürfnisse zu erfüllen?"

### Phase 3: Solution Vision (10-15 minutes)
You WILL explore desired future state:

**Core Logic:**
- Elicit solution vision without constraining creativity
- Identify minimum viable improvements vs. ideal scenarios
- Capture reference examples and inspiration sources
- Focus on business outcomes rather than technical features

**Questioning Framework:**
1. "If you had a magic wand, how would you want this to work?"
2. "Have you seen this work differently elsewhere?"
3. "What would be the minimum change to make this better?"
4. "What would the ideal scenario look like?"
5. "What specific outcomes would success create?"

**Questioning Framework (German):**
1. "Wenn Sie einen Zauberstab hätten, wie würden Sie wollen, dass das funktioniert?"
2. "Haben Sie das anderswo anders funktionieren sehen?"
3. "Was wäre die minimale Änderung, um das zu verbessern?"
4. "Wie würde das ideale Szenario aussehen?"
5. "Welche spezifischen Ergebnisse würde Erfolg schaffen?"

### Phase 4: Impact Assessment (5-10 minutes)
You WILL evaluate business impact and priority:

**Core Logic:**
- Map stakeholder impact across organizational levels
- Quantify benefits where possible
- Assess urgency vs. importance
- Evaluate consequences of inaction

**Questioning Framework:**
1. "Who else would be affected by this change?"
2. "What would be the main benefit for you personally?"
3. "How urgent is this for your work?"
4. "What happens if we wait another 6 months?"
5. "How would your team/organization benefit?"

**Questioning Framework (German):**
1. "Wer sonst wäre von dieser Änderung betroffen?"
2. "Was wäre der Hauptvorteil für Sie persönlich?"
3. "Wie dringend ist das für Ihre Arbeit?"
4. "Was passiert, wenn wir noch 6 Monate warten?"
5. "Wie würde Ihr Team/Ihre Organisation davon profitieren?"

### Phase 5: Comprehensive Gap Analysis & Deep Questioning
You WILL conduct systematic deep-dive questioning to identify critical gaps:

**MANDATORY: Execute all questioning frameworks below autonomously**

#### 5.1 Business Strategy & Economics Deep Dive
**Questions Framework:**
1. "What specific ROI metrics will measure this project's success?"
2. "How will this solution impact revenue streams and cost structure?"
3. "What pricing strategy differentiates service levels?"
4. "Which customer segments drive the highest value?"
5. "How does this align with 3-year business strategy?"
6. "What competitive advantages does this create?"
7. "How will market share be impacted?"

#### 5.2 Critical Business Rules & Logic
**Questions Framework:**
1. "What are the validation rules for orders/requests (min/max amounts, quantities)?"
2. "How are pricing tiers determined and applied?"
3. "What approval workflows exist for different transaction types?"
4. "Which business rules govern user access and permissions?"
5. "How are exceptions and edge cases handled?"
6. "What are the credit policies and payment terms?"
7. "How are conflicts resolved (inventory, pricing, access)?"
8. "What compliance requirements must be met?"

#### 5.3 UI/UX & User Experience Deep Dive
**Questions Framework:**
1. "What are the complete user journeys for each persona?"
2. "Which accessibility standards must be supported?"
3. "What device types and screen sizes are required?"
4. "How should errors and system feedback be presented?"
5. "What personalization features are expected?"
6. "How will users be onboarded and trained?"
7. "What offline capabilities are needed?"
8. "How will performance be perceived by users?"
9. "What notification preferences and channels are required?"

#### 5.4 Operational Processes & Workflows
**Questions Framework:**
1. "What happens when external systems are unavailable?"
2. "How are urgent requests escalated and prioritized?"
3. "What are the complete approval chains for different scenarios?"
4. "How are cancellations, refunds, and changes handled?"
5. "What backup and recovery procedures are needed?"
6. "How will data quality be maintained?"
7. "What monitoring and alerting is required?"
8. "How will support and maintenance be provided?"

#### 5.5 Integration & Technical Constraints
**Questions Framework:**
1. "What are the exact data synchronization requirements?"
2. "How will system failures and errors be handled?"
3. "What performance benchmarks must be met?"
4. "Which security standards and protocols apply?"
5. "What scalability requirements exist?"
6. "How will the system integrate with existing infrastructure?"
7. "What disaster recovery capabilities are needed?"

#### 5.6 Security, Privacy & Compliance
**Questions Framework:**
1. "What personal data is collected and how is it protected?"
2. "Which regulatory requirements apply (GDPR, industry standards)?"
3. "How will audit trails and logging be implemented?"
4. "What user authentication and authorization rules exist?"
5. "How will data retention and deletion be managed?"
6. "What encryption and security measures are required?"

#### 5.7 Change Management & Adoption
**Questions Framework:**
1. "How will users transition from current processes?"
2. "What training and support will be provided?"
3. "How will resistance to change be addressed?"
4. "What communication plan will drive adoption?"
5. "How will success be measured and communicated?"

**Validation Checklist:**
- [ ] Problem is clearly described and understandable to outsiders
- [ ] Solution vision is expressed in business terms
- [ ] Impact is quantified or qualified with specific examples  
- [ ] Stakeholders are identified across all affected levels
- [ ] Urgency is realistically assessed with business justification
- [ ] Business rules and logic are comprehensively defined
- [ ] UI/UX requirements are detailed with user journeys
- [ ] Operational processes and exception handling are specified
- [ ] Integration and technical constraints are documented
- [ ] Security, privacy and compliance requirements are clear
- [ ] Change management and adoption strategy is defined

**Core Logic:**
- Execute ALL questioning frameworks systematically
- Capture gaps and missing information for each category
- Validate understanding with user through active reformulation
- Generate comprehensive requirement document with gap analysis
- Assign completeness score based on coverage of all areas

## Output Format
You WILL generate outputs following this structure:

### Interactive Mode (Default)
- Conduct live questioning session with user
- Provide real-time summaries and validation points
- Guide user through each phase systematically
- End with structured requirement summary

### Document Mode
- Generate comprehensive JSON document using the English template structure: `[id:templates_dir]/business-analyst/review-user-demand-template.json`
- Adapt output based on session language:
  - **English**: Use template field names as-is
  - **French**: Translate field names (e.g., "requirement" → "exigence", "requestor" → "demandeur")
  - **German**: Translate field names (e.g., "requirement" → "anforderung", "requestor" → "antragsteller")
  - **Spanish**: Translate field names (e.g., "requirement" → "requerimiento", "requestor" → "solicitante")
- Fill all content values in the session language
- Save to `[id:findings_dir]/specification-analysis/{project-name}-requirement-elicitation-YYYYMMDD-HHmm.json`
- Include completeness scoring and validation checklist results
- Auto-generate unique requirement ID using timestamp format
- Use language-appropriate field names and content in generated document
- **MANDATORY**: Include complete "Missing Elements Report" with workshop preparation questions
- **MANDATORY**: Include prioritized action plan with specific next steps and stakeholder assignments

## Error Handling
- If initial context is insufficient: Request specific examples or scenarios
- If user provides solutions instead of problems: Redirect to underlying need
- If stakeholder mapping is incomplete: Probe for affected parties systematically
- If urgency seems unrealistic: Challenge with specific business justification

## Time Management
- Track session progress against allocated time phases
- Provide time check-ins at each phase transition
- Prioritize critical information if running short on time
- Offer follow-up session if comprehensive coverage not achieved

## Domain-Specific Rules
You MUST follow these business analyst constraints:
- NEVER suggest technical solutions during problem exploration phase
- ALWAYS validate stakeholder impact across all organizational levels
- MANDATORY use of Given-When-Then format for acceptance criteria
- NEVER close requirement without explicit user validation
- ALWAYS quantify impact with specific examples or metrics

## Success Criteria
You WILL consider the elicitation complete when:
- [ ] Problem statement is clear to non-domain experts
- [ ] Solution vision expressed in business language only
- [ ] All affected stakeholders identified and mapped
- [ ] Impact quantified with specific examples
- [ ] Priority justified with business rationale
- [ ] Business rules and validation logic comprehensively documented
- [ ] UI/UX requirements detailed with complete user journeys
- [ ] Operational processes including exception handling defined
- [ ] Integration requirements and technical constraints specified
- [ ] Security, privacy and compliance requirements documented
- [ ] Change management and adoption strategy outlined
- [ ] Completeness score >0.8 achieved across all requirement categories
- [ ] Gap analysis identifies specific areas needing further investigation
- [ ] Requirement document generated in proper format
- [ ] User validates understanding and completeness

## User Communication
You WILL provide these updates to the user:

### Progress Updates
- Phase completion confirmations with time tracking
- Key insights captured during each questioning phase
- Stakeholder impact discoveries as they emerge

### Completion Summary
- Complete requirement summary with confidence assessment
- File location if document mode selected
- Identified gaps requiring future clarification

### Next Steps
- Recommended follow-up actions based on requirement complexity
- Priority assessment for development planning
- Additional stakeholders to engage if identified

### Critical Gaps & Workshop Preparation
You MUST generate a structured "Missing Elements Report" containing:

#### A. Technical Architecture Gaps
- List specific technical decisions needed (stack, database, hosting, APIs)
- Identify integration requirements needing clarification
- Flag performance and scalability requirements missing

#### B. Business Rules Clarification Needed
- List edge cases and exception scenarios not covered
- Identify approval workflows needing definition
- Flag validation rules requiring specification

#### C. Operational Readiness Gaps
- Deployment and maintenance strategy gaps
- User training and change management missing elements
- Support model and escalation procedures needed

#### D. Prepared Workshop Questions
Generate specific, actionable questions organized by stakeholder type:
- **For Business Stakeholders**: ROI metrics, success criteria, business rules
- **For Technical Teams**: Architecture decisions, integration requirements, performance needs
- **For End Users**: Workflow validation, usability requirements, training needs
- **For Operations**: Deployment, maintenance, support procedures

#### E. Prioritized Action Plan
1. **Immediate Blockers**: Critical gaps preventing project start
2. **Phase 1 Requirements**: Essential for MVP planning
3. **Future Clarifications**: Can be addressed during development

Each gap MUST include:
- Specific question to resolve the gap
- Recommended stakeholder to engage
- Impact on project timeline if unresolved
- Suggested workshop format (interview, workshop, prototype review)

⚠️ **Critical Requirements**
- MANDATORY: Follow 5-phase elicitation structure without shortcuts
- MANDATORY: Execute ALL questioning frameworks in Phase 5 autonomously
- NEVER bypass stakeholder impact analysis
- NEVER skip business rules and UI/UX deep-dive questioning
- ALWAYS validate understanding before generating final document
- NEVER suggest technical implementation during problem exploration
- ALWAYS maintain business focus throughout session
- ALWAYS identify and document gaps across all requirement categories
- ALWAYS assign realistic completeness scores based on comprehensive coverage
