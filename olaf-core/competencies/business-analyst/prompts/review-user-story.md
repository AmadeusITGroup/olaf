---

name: review-user-story

description: Review user story against standard template to ensure quality, clarity, and completeness

tags: [documentation, analysis, user-story, quality, review]

---
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.

- **user_story_content**: string - The user story text to be reviewed

- **template_reference**: string - Optional specific template to use for evaluation

- **review_depth**: string - Optional depth level (basic|thorough|comprehensive)



## Process



1. **Load User Story**:

   - Receive user story content provided by user

   - Parse and structure the story components for analysis

   - Identify existing story elements (title, description, acceptance criteria, etc.)



2. **Analyze Against Template**:

   - Read file: `[id:competencies_dir][competency]/templates/business-analyst/user-story-review-template.md` for evaluation criteria

   - Evaluate user story against each template requirement:

     - Check for clarity and understandability

     - Assess testability of acceptance criteria

     - Verify completeness of required sections

     - Identify missing or unclear information

   - Document findings systematically per template section



3. **Generate Structured Review**:

   - Create markdown-formatted review based on analysis

   - Structure review with standardized sections:

     - Overall assessment summary

     - Identified strengths

     - Areas requiring improvement

     - Specific clarifying questions for user

   - Frame feedback constructively and collaboratively



## Output Format

Follow template structure: `[id:competencies_dir][competency]/templates/business-analyst/user-story-review-template.md`



**Save Output**: Create file `[id:findings_dir]user-story-reviews/user-story-review-YYYYMMDD-NNN.md` where:

- YYYYMMDD is the current date

- NNN is a sequential number (001, 002, etc.)







## Output to USER

- User story reviewed: [title or identifier]

- Overall assessment: [quality rating/summary]

- Key strengths identified: [number of positive elements]

- Improvement areas: [number of issues found]

- Clarifying questions generated: [number of questions for user]



## Review Rules

- Rule 1: Be thorough - examine each story component carefully without making assumptions

- Rule 2: Be constructive - frame feedback helpfully and collaboratively, not critically

- Rule 3: Reference template explicitly - use standard template as basis for all evaluations

- Rule 4: Generate actionable questions - provide specific questions that help improve the story

