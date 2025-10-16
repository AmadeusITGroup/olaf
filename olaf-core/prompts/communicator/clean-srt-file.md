---
name: clean-srt-file
description: Clean SRT subtitle files by removing timecodes, rewriting in proper US English, and grouping content into readable segments
tags: [srt, subtitle, cleaning, transcription]
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
- **srt_file_path**: string - Path to the SRT file to be cleaned (can be outside workspace) (REQUIRED)
- **output_file_path**: string - Path for the cleaned output file (OPTIONAL - defaults to findings/videos/[concise-name]-[YYYYMMDD-HHmm]_cleaned.txt)
- **segment_separation**: number - Number of blank lines between segments (OPTIONAL - defaults to 3)
- **workspace_copy_name**: string - Name for the copied file in workspace (OPTIONAL - defaults to [concise-name]-[YYYYMMDD-HHmm].srt)

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- You WILL use Propose-Act protocol for SRT cleaning due to content modification impact

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm SRT file exists at provided path (even outside workspace)
- Create findings/videos directory if it doesn't exist
- Get current timestamp in YYYYMMDD-HHmm format using terminal commands
- Generate concise name from original SRT filename (remove spaces, special chars, keep essence)
- Create timestamped subfolder: findings/videos/[concise-name]-[YYYYMMDD-HHmm]/
- Validate source file contains standard SRT format (timecodes and text)
- Check write permissions for findings/videos location and subfolder
- Verify file is not empty or corrupted

### 2. Execution Phase

**File Import Operations:**
<!-- <workspace_import> -->
You WILL copy the external SRT file into workspace:
- Create findings/videos directory structure if needed
- Generate concise name from original filename (e.g., "Video Project 38 (2)" → "video-project-38")
- Create timestamped subfolder: findings/videos/[concise-name]-[YYYYMMDD-HHmm]/
- Copy source file from external path to findings/videos/[concise-name]-[YYYYMMDD-HHmm]/original.srt
- Use current timestamp obtained from terminal commands for consistent naming
- Confirm successful copy operation before proceeding
<!-- </workspace_import> -->

**File Reading Operations:**
<!-- <file_analysis> -->
You WILL read and analyze the copied SRT file structure:
- Identify timecode patterns (HH:MM:SS,mmm --> HH:MM:SS,mmm)
- Locate text content between timecodes
- Map subtitle sequence numbers
<!-- </file_analysis> -->

**Content Cleaning Operations:**
<!-- <timecode_removal> -->
You WILL remove all timecode elements:
- Delete sequence numbers (1, 2, 3, etc.)
- Remove timestamp lines (00:00:19,924 --> 00:00:31,446)
- Preserve only the actual spoken text content
<!-- </timecode_removal> -->

<!-- <text_improvement> -->
You WILL rewrite content in proper US English:
- Remove filler words: "you know", "um", "uh", "like", "so", "well"
- Remove verbal expressions: "[laughing]", "[coughing]", "[pause]", "[inaudible]"
- Correct grammar and sentence structure
- Fix capitalization and punctuation
- Maintain original meaning and context
- Use clear, professional language
<!-- </text_improvement> -->

<!-- <content_segmentation> -->
You WILL group sentences into logical segments:
- Combine related sentences into coherent paragraphs
- Separate segments with exactly 3 blank lines
- Do NOT add titles or headers to segments
- Maintain natural flow and readability
- Ensure each segment contains complete thoughts
<!-- </content_segmentation> -->

**Core Logic**: Execute following protocol requirements
- Apply Propose-Act protocol for user approval before processing
- Process file content systematically through all cleaning phases
- Generate clean, readable output maintaining original message intent

### 3. Validation Phase
You WILL validate results:
- Confirm all timecodes have been removed completely
- Verify text quality and readability improvements
- Check proper segment separation (3 blank lines)
- Ensure no content loss or meaning distortion

## Output Format
You WILL generate outputs following this structure:
- Directory structure: findings/videos/[concise-name]-[YYYYMMDD-HHmm]/
- Original SRT file: findings/videos/[concise-name]-[YYYYMMDD-HHmm]/original.srt
- Cleaned text file: findings/videos/[concise-name]-[YYYYMMDD-HHmm]/clean.txt
- Content structure: Text segments separated by exactly 3 blank lines
- Character encoding: UTF-8 for compatibility
- Example structure: findings/videos/video-project-38-20251016-0557/original.srt and clean.txt

## User Communication

### Progress Updates
- Confirmation when findings/videos directory is created/verified
- Timestamp generation confirmation (YYYYMMDD-HHmm format)
- Concise filename generation from original SRT name
- Status of file copy operation with timestamped naming
- Confirmation when SRT file is successfully loaded and analyzed
- Status of timecode removal completion
- Progress of text cleaning and improvement phase
- Completion of content segmentation
- Final validation results

### Completion Summary
- File import confirmation: external file copied to findings/videos/ with timestamp naming
- Timestamped file organization: [concise-name]-[YYYYMMDD-HHmm] format applied
- Summary of cleaning operations performed
- Original file statistics (timecodes removed, text segments processed)
- Output file locations: timestamped workspace copy (backup) and cleaned text file
- Quality improvements made (filler words removed, grammar corrections)

### Next Steps
You WILL clearly define:
- Cleaned file ready for use at findings/videos/[concise-name]-[YYYYMMDD-HHmm]/clean.txt
- Original SRT backup preserved at findings/videos/[concise-name]-[YYYYMMDD-HHmm]/original.srt
- Timestamped subfolder organization enables easy tracking and version management
- Recommendations for further editing if needed
- Workspace organization maintained with dedicated subfolder per video project

### Final Summary & Review Encouragement
You MUST provide a concise summary and strongly encourage user review:
- **Concise Summary**: Brief overview of what was accomplished (files processed, improvements made)
- **Review Encouragement**: Strongly urge the user to review the cleaned transcription for accuracy
- **Quality Assurance**: Emphasize that human review is essential for final quality validation
- **Next Actions**: Suggest specific review focus areas (technical accuracy, context preservation, readability)

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: ALWAYS copy external files to findings/videos/ before processing
- Rule 2: NEVER remove actual spoken content - only clean and improve presentation
- Rule 3: ALWAYS preserve the original meaning and context of the content
- Rule 4: MUST remove ALL timecode elements completely (sequence numbers and timestamps)
- Rule 5: MUST use exactly 3 blank lines between segments (no more, no less)
- Rule 6: NEVER add titles, headers, or labels to content segments
- Rule 7: ALWAYS maintain chronological order of the original content
- Rule 8: MUST convert to proper US English spelling and grammar conventions
- Rule 9: MUST create timestamped subfolder: findings/videos/[concise-name]-[YYYYMMDD-HHmm]/
- Rule 10: MUST use standard filenames: original.srt and clean.txt within the subfolder
- Rule 11: MUST generate concise names from original filenames (remove special chars, spaces, keep essence)

## Success Criteria
You WILL consider the task complete when:
- [ ] findings/videos directory created or verified
- [ ] External SRT file successfully copied to workspace with sanitized name
- [ ] All timecodes and sequence numbers completely removed
- [ ] Text rewritten in proper US English with filler words eliminated
- [ ] Content organized into logical segments with 3-line separation
- [ ] No meaning or context lost from original transcription
- [ ] Cleaned output file created in findings/videos/ with "_cleaned" suffix
- [ ] File encoding set to UTF-8 for compatibility
- [ ] User approval obtained via Propose-Act protocol
- [ ] Original SRT file preserved as backup in workspace

## Required Actions
1. Create findings/videos directory structure if needed
2. Copy external SRT file to workspace with sanitized filename
3. Validate copied file accessibility and format compliance
4. Execute cleaning operations following Propose-Act protocol
5. Generate cleaned output in findings/videos/ directory
6. Provide comprehensive progress communication
7. Confirm successful completion with quality validation

## Error Handling
You WILL handle these scenarios:
- **External File Not Found**: Provide clear error message and request correct external file path
- **Directory Creation Failed**: Attempt alternative paths and notify user of permission issues
- **File Copy Operation Failed**: Provide detailed error and suggest manual copy alternatives
- **Invalid SRT Format**: Analyze file structure and provide format guidance
- **Write Permission Issues**: Suggest alternative output locations or permission fixes
- **Content Corruption**: Stop processing and request user guidance for manual review
- **Encoding Issues**: Convert to UTF-8 and notify user of encoding changes
- **Empty or Minimal Content**: Warn user and confirm processing should continue
- **Filename Sanitization Issues**: Provide alternative naming suggestions
- **User Rejection During Propose-Act**: Request specific feedback and modification preferences

⚠️ **Critical Requirements**
- MANDATORY: Copy external files to findings/videos/ before any processing
- MANDATORY: Follow Propose-Act protocol before modifying any content
- MANDATORY: Preserve original SRT file as backup in workspace
- MANDATORY: End with concise summary and strong review encouragement
- NEVER remove actual spoken content - only improve presentation quality
- NEVER add content that wasn't in the original transcription
- ALWAYS maintain chronological order of original content
- ALWAYS use exactly 3 blank lines between segments
- ALWAYS sanitize filenames for workspace compatibility
- ALWAYS validate complete timecode removal before completion
- ALWAYS strongly encourage user to review the cleaned transcription