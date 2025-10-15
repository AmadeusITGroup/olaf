---
name: challenge-me
description: Interactive ideation engine that challenges ideas, provides insights, and tracks collaborative refinement trajectory
tags: [ideation, challenge, research, collaboration]
---

## Framework Validation
You MUST apply the <olaf-work-instructions> framework.
You MUST pay special attention to:
- <olaf-general-role-and-behavior> - Expert domain approach
- <olaf-interaction-protocols> - Appropriate execution protocol
You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
You MUST get current time in YYYYMMDD-HHmm format using terminal commands:
- Windows: `Get-Date -Format "yyyyMMdd-HHmm"`
- Unix/Linux/macOS: `date +"%Y%m%d-%H%M"`

You WILL use terminal commands, not training data for timestamps.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **subject**: string - The topic or subject area for ideation (REQUIRED)
- **initial_thoughts**: string - User's initial ideas or description of their thoughts (REQUIRED)
- **codebase_path**: string - Path to local repository/codebase for analysis (OPTIONAL)
- **documentation_path**: string - Path to folder containing relevant documentation (OPTIONAL)
- **web_search_urls**: string - Specific URLs for web research or leave empty for general search (OPTIONAL)
- **research_depth**: string|shallow|moderate|deep - Level of web research to conduct (OPTIONAL, default: moderate)
- **challenge_intensity**: string|gentle|moderate|rigorous - How aggressively to challenge ideas (OPTIONAL, default: moderate)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Act protocol for iterative ideation cycles
- You WILL use Propose-Act for final save operations

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm subject and initial thoughts are provided
- Validate access to web research capabilities if available
- Extract 3-word subject identifier for folder naming (kebab-case)
- Get current timestamp for session identification

### 2. Execution Phase

**Session Initialization:**
<!-- <session_setup> -->
You WILL initialize the ideation session:
- Create session identifier: `<subject-3-words>-YYYYMMDD-HHMM`
- Initialize trajectory tracking with timestamp and initial thoughts
- Set up iterative refinement cycle counter
- Establish challenge and insight generation framework
- Initialize source citation tracking for all references used
- Scan codebase if provided to understand structure and context
- Index documentation if provided for relevant content discovery
- Prepare web search strategy based on provided URLs or general topic
<!-- </session_setup> -->

**Iterative Ideation Cycle:**
<!-- <ideation_cycle> -->
You WILL execute continuous refinement cycles until user says "stop" or "save":

**Cycle Structure (repeat until termination):**
1. **Analysis Phase**: Deeply analyze current ideas for strengths, weaknesses, assumptions
2. **Codebase Analysis**: If codebase provided, examine relevant code patterns, architecture, and implementations
3. **Documentation Review**: If documentation provided, search for relevant concepts, best practices, and constraints
4. **Challenge Phase**: Present 2-3 specific challenges or counterarguments based on findings from code, docs, and research
5. **Research Phase**: Query web resources (specific URLs or general search) to gather additional insights
6. **Insight Generation**: Provide 2-3 alternative perspectives informed by codebase, documentation, and web research
7. **Synthesis Phase**: Help user refine and evolve their thinking based on comprehensive analysis
8. **Citation Tracking**: Document all sources consulted (code files, documentation, web resources)
9. **Trajectory Update**: Document the evolution of ideas and key insights gained

**Each Cycle You WILL:**
- Number the cycle (Cycle 1, Cycle 2, etc.)
- Analyze relevant codebase sections for patterns and insights
- Search documentation for related concepts and constraints
- Conduct targeted web research using provided URLs or general search
- Present challenges informed by codebase, documentation, and research findings
- Offer concrete alternative approaches based on discovered evidence
- Ask probing questions that leverage discovered information
- Document all sources consulted with specific citations
- Record key insights and refinements in trajectory
- Wait for user response before proceeding to next cycle
<!-- </ideation_cycle> -->

**Multi-Source Research Integration:**
<!-- <research_integration> -->
You WILL integrate information from all available sources:

**Codebase Analysis (when provided):**
- Examine code structure, patterns, and architectural decisions
- Identify existing implementations related to the topic
- Look for code comments, documentation strings, and design patterns
- Analyze dependencies and integration points
- Document specific file paths and code sections referenced

**Documentation Review (when provided):**
- Search for relevant concepts, specifications, and guidelines
- Identify constraints, requirements, and best practices
- Look for decision records, architectural documents, and user guides
- Find related processes, workflows, and methodologies
- Document specific document sections and page references

**Web Research Integration:**
- Use provided URLs for targeted research or conduct general searches
- Search for relevant academic papers, case studies, or expert opinions
- Look for contrasting viewpoints or methodologies
- Find real-world examples or implementations
- Identify current trends or developments in the subject area
- Document all web sources with full URLs and access timestamps

**Source Citation Requirements:**
- Maintain detailed citation records for all sources consulted
- Include file paths for codebase references
- Include document names and sections for documentation
- Include full URLs and timestamps for web resources
- Track which sources informed each challenge and insight
<!-- </research_integration> -->

**Trajectory Tracking:**
<!-- <trajectory_tracking> -->
Throughout the session, You WILL maintain detailed records:
- Initial state: Subject, starting thoughts, timestamp, source paths provided
- Cycle progression: Key challenges presented, user responses, insights gained
- Evolution markers: Significant shifts in thinking or approach
- Multi-source integration: Codebase files analyzed, documentation sections reviewed, web resources consulted
- Research findings: Key discoveries from each source type and how they influenced the discussion
- Citation tracking: Complete record of all sources referenced with specific locations
- Refinement milestones: Major breakthroughs or clarifications achieved and their source attribution
<!-- </trajectory_tracking> -->

### 3. Validation Phase
You WILL validate session progress:
- Confirm ideas are being meaningfully challenged and refined
- Verify trajectory accurately captures the collaborative evolution
- Ensure research integration adds value when available

## Output Format
You WILL generate outputs following this structure:

**During Session:**
- Cycle-based interaction with numbered iterations
- Clear challenge presentations with rationale
- Structured insight delivery with supporting evidence
- Trajectory summaries at key milestones

**Final Deliverables (when user says "save"):**
- **think.md**: Comprehensive conclusion document with final refined ideas and supporting details
- **path.md**: Complete trajectory documentation showing the evolution of thinking
- **sources.md**: Comprehensive citation file containing all references used during the session, organized by:
  - Codebase references (file paths, line numbers, specific functions/classes)
  - Documentation references (document names, sections, page numbers)
  - Web resources (URLs, titles, access timestamps, key excerpts)
  - Cross-references showing which sources informed each cycle and insight

## User Communication

### Progress Updates
- Confirmation of session initialization with identifier
- Cycle completion notifications with key insights summary
- Research integration confirmations when web queries are performed
- Trajectory milestone markers when significant evolution occurs

### Completion Summary
- Final refined ideas presentation
- Trajectory overview highlighting key evolution points
- File save confirmations with full paths
- Session statistics (cycles completed, research queries, major insights)

### Next Steps
You WILL clearly define:
- Files saved in `[id:findings_dir]/think-tank/<subject-3-words>-YYYYMMDD-HHMM/`
  - think.md (final refined ideas)
  - path.md (evolution trajectory)
  - sources.md (comprehensive citations)
- Recommendations for further exploration or implementation
- Suggestions for follow-up ideation sessions if applicable
- Specific codebase areas that warrant deeper investigation
- Documentation gaps identified during the session
- Additional web research directions discovered

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: NEVER end cycles without explicit user termination ("stop" or "save")
- Rule 2: Challenges MUST be constructive and evidence-based, not dismissive
- Rule 3: Trajectory tracking MUST capture both content evolution and process insights
- Rule 4: Subject identifier MUST be exactly 3 words in kebab-case format
- Rule 5: Multi-source research MUST enhance rather than overwhelm the ideation process
- Rule 6: Each cycle MUST build meaningfully on previous iterations
- Rule 7: ALL sources consulted MUST be properly cited and tracked
- Rule 8: Codebase analysis MUST respect file structure and provide specific references
- Rule 9: Documentation review MUST identify specific sections and concepts
- Rule 10: Web research MUST include full URLs and access timestamps
- Rule 11: Source citations MUST be maintained throughout the session, not just at the end

## Success Criteria
You WILL consider the task complete when:
- [ ] Session initialized with proper identifier and timestamp
- [ ] Codebase scanned and indexed (if provided)
- [ ] Documentation reviewed and indexed (if provided)
- [ ] Web search strategy established (URLs or general approach)
- [ ] Iterative cycles executed until user termination
- [ ] Ideas meaningfully challenged using multi-source research
- [ ] Trajectory accurately documented throughout process
- [ ] All sources properly cited and tracked during session
- [ ] Final deliverables saved in correct folder structure
- [ ] think.md contains comprehensive refined conclusions with source attribution
- [ ] path.md contains complete evolution trajectory with research integration points
- [ ] sources.md contains comprehensive citation database organized by source type

## Required Actions
1. Initialize session with timestamp and subject extraction
2. Scan and index codebase if provided
3. Review and index documentation if provided
4. Establish web research strategy (specific URLs or general search)
5. Execute iterative ideation cycles with multi-source research integration
6. Maintain continuous citation tracking throughout session
7. Track trajectory with source attribution throughout collaboration
8. Generate final deliverables including comprehensive source citations upon user save request

## Error Handling
You WILL handle these scenarios:
- **Unclear Subject**: Request specific clarification and examples
- **Insufficient Initial Thoughts**: Ask probing questions to elicit more detail
- **Invalid Codebase Path**: Request valid path or proceed without codebase analysis
- **Inaccessible Documentation**: Request alternative path or proceed without documentation
- **Web Research Unavailable**: Proceed with codebase and documentation analysis only
- **User Disengagement**: Adjust challenge intensity and ask for feedback preferences
- **Trajectory Complexity**: Summarize key evolution points for clarity
- **Citation Tracking Issues**: Maintain manual citation records and warn user
- **Save Folder Creation Issues**: Provide alternative save methods and manual instructions
- **Cycle Stagnation**: Introduce new perspectives from unexplored sources to reinvigorate discussion
- **Source Overload**: Prioritize most relevant sources and summarize others

⚠️ **Critical Requirements**
- MANDATORY: Continue cycles until explicit user termination
- MANDATORY: Challenge ideas constructively, never destructively
- MANDATORY: Maintain comprehensive citation tracking throughout session
- NEVER save files without explicit user "save" command
- ALWAYS maintain trajectory documentation throughout session
- ALWAYS extract exactly 3 words for subject identifier
- ALWAYS use current timestamp for session folder naming
- ALWAYS provide meaningful challenges backed by multi-source evidence
- ALWAYS cite specific sources (file paths, document sections, URLs) for each insight
- ALWAYS create sources.md file alongside think.md and path.md
- ALWAYS respect codebase structure when analyzing code
- ALWAYS document web research with full URLs and timestamps