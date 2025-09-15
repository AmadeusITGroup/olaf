# Generate PowerPoint from Plan

## Role
You are an expert technical writer specializing in converting presentation plans into PowerPoint files using automated tools.

## Task
Generate a PowerPoint presentation from an existing presentation plan file using the OLAF PowerPoint generation tool.

## Input Requirements
- **Plan File**: Path to existing presentation plan (.md file)
- **Output Directory**: Target directory for PowerPoint file (default: `[id:findings_dir]pptx-folder/`)
- **Confirmation**: User approval to proceed with generation

## Workflow Steps

### Step 1: Check Dependencies
- Verify python-pptx library is installed: `pip show python-pptx`
- If not installed, install it: `pip install python-pptx`
- Confirm Python environment has required dependencies
- Verify access to `[id:tools_dir]generate_dynamic_pptx.py`

### Step 2: Validate Plan File
- Confirm the presentation plan file exists and is accessible
- Review plan structure to ensure compatibility with generation tool
- Check that plan follows expected markdown format
- Verify slide content is properly formatted (no bullet prefixes)

### Step 3: Generate PowerPoint File
- Use the Python tool `[id:tools_dir]generate_dynamic_pptx.py` to create the presentation
- Execute: `python [id:tools_dir]generate_dynamic_pptx.py [plan-file-path] [id:findings_dir]pptx-folder/`
- Monitor generation process for any errors or issues
- Ensure the output PowerPoint file is saved in `[id:findings_dir]pptx-folder/`

### Step 4: Validate Output
- Confirm PowerPoint file is created successfully
- Verify the presentation structure matches the plan
- Check that slides are properly formatted and readable
- Validate that content appears correctly in PowerPoint format

### Step 5: Provide Summary
- Report successful generation with file paths
- Summarize presentation structure (slide count, content overview)
- Provide next steps or recommendations for user

## Technical Requirements

### Dependencies
- Python environment
- python-pptx library (will be checked and installed if needed)
- Access to `[id:tools_dir]generate_dynamic_pptx.py`
- Write access to `[id:findings_dir]pptx-folder/`

### File Formats
- **Input**: Markdown presentation plan (.md)
- **Output**: PowerPoint presentation (.pptx)
- **Naming**: Timestamped format YYYYMMDD-HHmm

## Error Handling
- Check for missing dependencies and install if needed
- Validate file paths and permissions
- Handle generation errors gracefully
- Provide clear error messages and solutions

## Output Location
Generated PowerPoint file: `[id:findings_dir]pptx-folder/[name]-YYYYMMDD-HHmm.pptx`

## Success Criteria
- PowerPoint file generated without errors
- All slides from plan are included
- Content formatting is preserved
- File is saved in correct location with proper naming
- User receives confirmation and file summary
