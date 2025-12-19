# Coach Developers to Prompt

## Overview

This competency provides interactive training to coach developers in writing effective AI prompts through hands-on practice with real code scenarios. It creates training projects, evaluates prompt quality, and provides iterative feedback to improve prompt engineering skills.

## Purpose

Many developers struggle to communicate their needs clearly to AI assistants, resulting in suboptimal code suggestions, missed requirements, or excessive back-and-forth iterations. This competency addresses this critical skill gap by providing a safe learning environment where developers can experiment with different prompting approaches and receive immediate, constructive feedback on their prompt quality.

## Usage

**Command**: `coach prompts` (or aliases: `prompt training`, `train prompting`, `prompt coaching`, `learn prompting`, `improve prompting`, `prompt workshop`)

**Protocol**: Act

**When to Use**: Use for onboarding new developers to AI-assisted development, improving team prompt engineering skills, training sessions on effective AI communication, or individual skill development in prompt writing.

## Parameters

### Required Inputs

- **language**: Primary development language for the exercise (JavaScript, TypeScript, Python, Java, C#, Go, etc.)
- **experience_level**: Developer's self-assessed level (beginner | intermediate | advanced)
- **project_type**: Type of training project (e.g., "small API endpoint", "CLI tool", "small library function", "test-focused task")

### Optional Inputs

- **training_folder**: Custom folder name for training project (default: `prompt-training-<language>`)
- **iteration_count**: Number of training iterations to perform (default: 1)

### Context Requirements

- Developer willing to engage in iterative learning
- Basic understanding of the chosen programming language
- IDE workspace for creating training projects
- Time for reflection and practice (15-30 minutes per iteration)

## Output

Generates interactive training sessions with feedback and improvement suggestions.

**Deliverables**:

**During Training:**
- Small, realistic project with intentional issues
- Real-time responses to developer prompts
- Detailed feedback on prompt quality
- Improved prompt versions with explanations

**After Completion:**
- **Session Summary**: Overview of training session including language, project type, and iterations completed
- **Prompt Evolution**: Before/after comparison of developer's prompts
- **Key Learnings**: Main improvements identified and lessons learned
- **Recommended Next Steps**: Suggestions for continued prompt engineering practice

## Key Features

### Dual-Mode Operation
- **AI-as-Tool Mode**: Responds to developer prompts as a standard coding assistant
- **Trainer Mode**: Provides detailed feedback on prompt quality and effectiveness

### Evaluation Dimensions
Prompts are evaluated across five key dimensions:
1. **Clarity of Goal**: Is it obvious what the developer wants?
2. **Context Provided**: Are there enough details (files, functions, behavior)?
3. **Specificity of Output**: Is the desired response format specified?
4. **Constraints and Priorities**: Are style, performance, or compatibility mentioned?
5. **Structure and Readability**: Is the prompt well-organized and easy to follow?

### Safe Learning Environment
- All changes require explicit confirmation
- Training projects are isolated from production code
- No risk of damaging existing work
- Realistic but simplified scenarios

## Workflow

### Phase 1: Setup
1. Developer specifies programming language and experience level
2. System creates a small, realistic project with intentional issues
3. Developer confirms understanding and readiness

### Phase 2: Initial Prompt
1. Developer writes their first prompt without guidance
2. System responds as a standard coding assistant
3. Proposes changes but doesn't apply them automatically

### Phase 3: Feedback & Learning
1. System switches to Trainer Mode
2. Provides detailed analysis of prompt strengths and weaknesses
3. Offers improved version with explanations
4. Invites developer to try the improved prompt

### Phase 4: Iteration (Optional)
1. Developer practices with additional scenarios
2. Complexity gradually increases
3. Expectations for prompt quality rise accordingly

## Best Practices

### For Learners
- Start with your actual skill level (don't overestimate)
- Try your natural prompting style first (don't overthink it)
- Compare your prompts with the improved versions carefully
- Practice with multiple iterations to build muscle memory
- Apply learnings to your real development work

### For Trainers/Mentors
- Use this as part of onboarding for AI-assisted development
- Run group sessions where developers compare their prompts
- Create custom scenarios relevant to your team's tech stack
- Track improvement over multiple sessions
- Encourage reflection and discussion

## Integration Points

- **review-code**: Apply improved prompting to code review requests
- **evolve-code-iteratively**: Use better prompts for iterative development
- **deepen-tech-spec-developer**: Practice detailed technical prompting
- **fix-code-smells**: Improve prompts for refactoring requests

## Limitations

- Training projects are simplified scenarios (not production complexity)
- Feedback is based on general best practices (not team-specific conventions)
- Requires developer engagement and reflection (not passive learning)
- Works best with developers who have basic coding knowledge
- Limited to single-developer training (not collaborative sessions)

## Examples

### Example 1: Basic Training Session
```
coach prompts
Language: Python
Level: intermediate
Project: small API endpoint
```

### Example 2: Advanced Training
```
coach prompts
Language: TypeScript
Level: advanced
Project: CLI tool with complex argument handling
Iterations: 3
```

### Example 3: Beginner Focus
```
coach prompts
Language: JavaScript
Level: beginner
Project: small library function
Focus: debugging and testing prompts
```

## Related Competencies

- **review-code**: Code review with improved prompts
- **evolve-code-iteratively**: Iterative development with better communication
- **augment-code-unit-test**: Test generation with clear prompts
- **fix-code-smells**: Refactoring with specific requirements

## Technical Requirements

- **Recommended LLM**: Claude Sonnet 4.5 or higher
- **Platform**: Cross-platform compatible (Windows, Linux, macOS)
- **Dependencies**: None (uses standard IDE file operations)
- **Framework Version**: OLAF 1.6.0+

---

**Version**: 1.0.0  
**Status**: Public Beta  
**Created**: December 16, 2025  
**Maintenance Team**: developer
