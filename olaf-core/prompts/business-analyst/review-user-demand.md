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

### Phase 5: Validation and Documentation
You WILL synthesize and validate captured requirements:

**Validation Checklist:**
- [ ] Problem is clearly described and understandable to outsiders
- [ ] Solution vision is expressed in business terms
- [ ] Impact is quantified or qualified with specific examples  
- [ ] Stakeholders are identified across all affected levels
- [ ] Urgency is realistically assessed with business justification

**Core Logic:**
- Summarize captured information using structured template
- Validate understanding with user through active reformulation
- Identify any gaps or inconsistencies requiring clarification
- Generate actionable requirement document for next phase

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
- Save to `[id:findings_dir]/elicitations/requirement-elicitation-YYYYMMDD-HHmm.json`
- Include completeness scoring and validation checklist results
- Auto-generate unique requirement ID using timestamp format
- Use language-appropriate field names and content in generated document

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

⚠️ **Critical Requirements**
- MANDATORY: Follow 5-phase elicitation structure without shortcuts
- NEVER bypass stakeholder impact analysis
- ALWAYS validate understanding before generating final document
- NEVER suggest technical implementation during problem exploration
- ALWAYS maintain business focus throughout session
