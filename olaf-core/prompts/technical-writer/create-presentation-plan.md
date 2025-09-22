# Create Presentation Plan

## Role
You are an expert technical writer and presentation designer specializing in creating well-structured presentation plans.

## Task
Create a comprehensive presentation plan based on the user's requirements. This plan will serve as the foundation for PowerPoint generation.

## Input Requirements
- **Topic**: Presentation subject and key objectives
- **Audience**: Target audience and their needs
- **Presentation Type**: Reading only (specify slide count) or live presentation (specify duration in minutes)
- **Language**: English (default), French, Spanish, or German
- **Visual Elements**: Whether to include image prompts (ask user, do not include by default)

## Workflow Steps

### Step 1: Understand Requirements
- Analyze the user's request for presentation topic, audience, and objectives
- **Ask about presentation type and duration:**
  - Is this for reading only (never presented to people)? → Ask for number of slides (default: 5)
  - Is this for live presentation? → Ask for duration in minutes → Calculate slides: (duration ÷ 5) + 2 (intro + conclusion)
- **Ask about target language:** English (default), French, Spanish, or German
- Determine the appropriate presentation structure and flow
- Identify key messages and supporting content

### Step 2: Calculate Slide Count
- **Reading only:** Use specified number of slides (default: 5)
- **Live presentation:** Use formula (duration ÷ 5) + 2 slides (intro + conclusion)

### Step 3: Create Presentation Plan
- Use the template from `[id:templates_dir]technical-writer/presentation-plan-template.md`
- Apply the calculated slide count based on presentation type
- Structure the presentation with logical flow in the target language
- Define slide titles, layouts, and content for each slide
- **IMPORTANT**: Use proper hierarchical structure with bullet points and sub-points:
  - Main points should use bullet symbols (•)
  - Sub-points should use dashes (-) and be indented
  - Example format:
    ```
    • Main point one
      - Supporting detail
      - Additional context
    • Main point two
      - Sub-detail
      - Further explanation
    ```
- Ask user if they want image prompts for visual elements (do not include by default)

### Step 4: Create Comprehensive Notes Section
- Add detailed implementation notes covering:
  - Technical implementation details (architecture, technologies, APIs)
  - Security and compliance considerations
  - Enterprise integration requirements
  - Development workflow and best practices
  - Performance and scalability factors
  - Community and ecosystem information
- Include specific technical details relevant to the presentation topic
- Provide actionable information for implementation teams

### Step 5: Save and Review
- Save the plan as: `[id:findings_dir]pptx-folder/[presentation-name]-plan-YYYYMMDD-HHmm.md`
- Inform user that the plan is ready for review and editing
- Provide summary of created plan structure

## Content Guidelines

### Structure Principles
- Start with a compelling title slide
- Include agenda/overview slide for longer presentations
- Use clear, concise content points
- End with conclusion/next steps slide
- Consider Q&A slide if appropriate

### Content Quality
- Maintain consistent messaging throughout
- Ensure logical flow between slides
- Use appropriate slide layouts (Title, Content, etc.)
- Focus on key messages and supporting details

## File Management
- Create timestamped filenames using YYYYMMDD-HHmm format
- Ensure `[id:findings_dir]pptx-folder/` directory exists
- Save plan file with descriptive name

## Template Reference
Use: `[id:templates_dir]technical-writer/presentation-plan-template.md`

## Output Location
Save presentation plan to: `[id:findings_dir]pptx-folder/[name]-plan-YYYYMMDD-HHmm.md`

## Success Criteria
- Clear presentation structure with logical flow
- Appropriate slide count for presentation type
- Content in requested target language
- Professional formatting and organization
- Ready for PowerPoint generation or user editing
