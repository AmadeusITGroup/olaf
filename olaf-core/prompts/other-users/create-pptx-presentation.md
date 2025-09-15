# Create PowerPoint Presentation from Content

## Objective
Generate a concise PowerPoint presentation from user-provided content files, with optional AI-generated image prompts, following a standardized template and design guidelines.

## Instructions

### Step 1: Gather Input Requirements
Ask the user for the following information:

1. **Content Source**: 
   - Single file path (e.g., proposal.md, document.txt)
   - Multiple files (comma-separated list)
   - Folder path (process all relevant files)

2. **Presentation Options**:
   - Presentation title (if different from content)
   - Target audience (technical, business, general)
   - Maximum number of slides (default: 5)
   - Include image generation prompts? (yes/no, default: no)

3. **Output Preferences**:
   - Presentation name (auto-generated if not provided)
   - Custom styling preferences (optional)

### Step 2: Content Analysis and Slide Generation
Based on the provided content:

1. **Analyze the content** to identify:
   - Main title/theme
   - Key sections or topics
   - Important bullet points
   - Tags or keywords

2. **Generate a concise slide structure** (typically 3-5 slides):
   - Slide 1: Title slide
   - Slides 2-4: Main content sections (description, benefits, key points)
   - Slide 5: Conclusion/Call to action

3. **For each slide, provide**:
   - Clear, concise title
   - 2-4 bullet points maximum
   - Optional: Image generation prompt (if requested)

### Step 3: Apply Template Design Guidelines

#### Generic Design Style:
- **Color Scheme**: Professional blue theme (#2E4A87 primary, #4A90C2 secondary, #F8F9FA background)
- **Typography**: Clean, modern fonts (Calibri/Arial family)
- **Layout**: Minimal, focused on readability
- **Consistency**: Uniform styling across all slides

#### Image Style Guidelines (if enabled):
- **Theme**: Futuristic and professional
- **Color Palette**: Blue-dominant with white/silver accents
- **Style**: Abstract, technological, clean
- **Elements**: Geometric shapes, network connections, digital elements
- **Mood**: Innovative, trustworthy, forward-thinking

### Step 4: Generate Presentation File
Create a structured markdown file in the `findings_dir` folder with:

```markdown
# [Presentation Title]

## Design Configuration
- Theme: Professional Blue
- Style: Modern, Minimal
- Image Style: Futuristic Blue Tech (if applicable)

## Slides

### Slide 1: [Title]
**Layout**: Title Slide
**Content**:
- Title: [Main Title]
- Subtitle: [Subtitle or tagline]

*Image Prompt (if enabled): [Specific prompt following style guidelines]*

### Slide 2: [Section Title]
**Layout**: Content Slide
**Content**:
- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]

*Image Prompt (if enabled): [Specific prompt following style guidelines]*

[Continue for all slides...]
```

### Step 5: User Review and Correction
1. **Present the generated file** to the user
2. **Invite feedback** on:
   - Slide content and structure
   - Image prompts (if included)
   - Overall flow and messaging
3. **Make requested adjustments** before final generation

### Step 6: Generate Final PPTX
1. **Use the dynamic script** to read the markdown file
2. **Generate the PowerPoint presentation** with proper naming
3. **Include image placeholders** or prompts as specified
4. **Save in findings_dir** with descriptive filename

## Expected Output
- A structured presentation file in `findings_dir/presentations/`
- A corresponding .pptx file ready for use
- Clear instructions for any manual steps (like image generation)

## Quality Guidelines
- **Conciseness**: Each slide should be scannable in 30 seconds
- **Clarity**: Use simple, jargon-free language where possible
- **Consistency**: Maintain uniform styling and tone
- **Relevance**: Every element should support the main message
- **Professionalism**: Suitable for business/technical presentations

## Notes
- Default to minimal slides unless more are essential
- Prioritize content quality over quantity
- Ensure image prompts align with overall presentation theme
- Make the process iterative - allow for refinements