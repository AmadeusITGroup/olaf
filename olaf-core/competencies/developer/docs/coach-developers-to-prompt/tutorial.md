# Coach Developers to Prompt - Tutorial

## Introduction

This tutorial will guide you through using the **Coach Developers to Prompt** competency to improve your prompt engineering skills. By the end of this tutorial, you'll understand how to write clearer, more effective prompts for AI-assisted development.

## Prerequisites

- Basic understanding of a programming language
- Access to an IDE with OLAF framework
- 20-30 minutes for a complete training session
- Willingness to experiment and learn

## Tutorial Outline

1. Starting a Training Session
2. Understanding the Training Project
3. Writing Your First Prompt
4. Receiving Feedback
5. Improving Your Prompts
6. Iterating for Mastery

---

## Step 1: Starting a Training Session

### Invoke the Competency

Use any of these commands:
```
coach prompts
prompt training
learn prompting
```

### Provide Your Information

When prompted, specify:
- **Language**: Choose a language you're comfortable with (e.g., Python, JavaScript, TypeScript)
- **Experience Level**: Be honest about your skill level (beginner, intermediate, advanced)
- **Project Type**: Select what interests you (API endpoint, CLI tool, library function, test task)

**Example:**
```
Language: Python
Level: intermediate
Project: small API endpoint
```

---

## Step 2: Understanding the Training Project

### Review the Created Files

The system will create a small project with:
- A folder structure (e.g., `prompt-training-python/`)
- Source files with working code
- Test files (if applicable)
- Configuration files

### Identify the Issues

The system will explain (in chat, not in code comments):
- What bugs or issues exist
- What the expected behavior should be
- What you need to fix

**Important**: The code itself won't have comments revealing the bugs. You need to discover them through your prompts!

### Confirm Understanding

Before proceeding, make sure you:
- Can see the project files in your IDE
- Understand what's wrong
- Are ready to write a prompt to fix it

---

## Step 3: Writing Your First Prompt

### The Challenge

Write a prompt that would help you fix the issues. **Don't overthink it** - use your natural style.

### What NOT to Do

❌ Don't look for examples first  
❌ Don't try to guess what the "perfect" prompt looks like  
❌ Don't copy templates

### What TO Do

✅ Write what you would naturally ask  
✅ Include whatever information feels relevant  
✅ Be yourself - this is about learning YOUR style

### Example First Prompt (Typical)

```
"Fix the bug in the server code"
```

or

```
"The API endpoint isn't working correctly. Can you help me fix it?"
```

---

## Step 4: Receiving Feedback

### AI-as-Tool Response

First, the system will respond **as if it were a normal coding assistant**:
- It will analyze the code
- Propose fixes
- Show you what changes it would make
- Ask for confirmation before applying

**Note**: It won't apply changes automatically - you'll see what it would do.

### Trainer Mode Feedback

Then, the system switches to **Trainer Mode** and evaluates your prompt:

#### 1. Clarity of Goal
- Was it clear what you wanted?
- Could the AI understand your intent?

#### 2. Context Provided
- Did you mention specific files?
- Did you describe the expected behavior?
- Did you provide enough background?

#### 3. Specificity of Output
- Did you specify what kind of answer you wanted?
- Did you ask for explanations, diffs, or complete solutions?

#### 4. Constraints and Priorities
- Did you mention coding style preferences?
- Did you specify performance requirements?
- Did you note compatibility concerns?

#### 5. Structure and Readability
- Was your prompt organized?
- Was it easy to follow?

### Understanding the Feedback

The feedback will include:
- **What you did well** (positive reinforcement)
- **What was missing or unclear** (areas for improvement)
- **How the gaps affected the response** (real impact)

---

## Step 5: Improving Your Prompts

### The Improved Version

The system will show you a **rewritten version** of your prompt with improvements highlighted.

**Example Transformation:**

**Your Original Prompt:**
```
"Fix the bug in the server code"
```

**Improved Version:**
```
"I need help fixing a bug in `src/server.py`. The API endpoint at `/api/users` 
is returning a 500 error when it should return a list of users. 

Please:
1. Identify the root cause of the error
2. Propose a fix with a code diff showing the exact changes
3. Explain why the bug occurred
4. Ensure the fix maintains backward compatibility

The expected behavior is to return a JSON array of user objects with status 200."
```

### Key Improvements Explained

The system will point out what changed:
- ✅ **Added file path**: `src/server.py` (specific context)
- ✅ **Described the problem**: "returning 500 error" (clear symptom)
- ✅ **Stated expected behavior**: "return JSON array with status 200" (goal)
- ✅ **Requested specific output**: "code diff" (format preference)
- ✅ **Added constraints**: "backward compatibility" (requirements)
- ✅ **Structured with numbered list**: (readability)

### Try the Improved Prompt

The system will invite you to:
1. Send the improved prompt as a new message
2. Compare the AI's response to the original
3. See the difference better prompting makes

---

## Step 6: Iterating for Mastery

### Continue Practicing

If you want more practice:
- Request another iteration
- Try a different type of issue
- Increase the complexity

### What Changes in Later Iterations

As you progress:
- **Issues become more complex** (multiple files, architectural concerns)
- **Expectations increase** (more detailed prompts required)
- **Feedback becomes more nuanced** (advanced techniques)

### Track Your Progress

Notice how your prompts evolve:
- **Iteration 1**: Basic requests → Structured prompts
- **Iteration 2**: Structured prompts → Context-rich prompts
- **Iteration 3**: Context-rich → Comprehensive specifications

---

## Real-World Application

### Apply What You Learned

After training, use these techniques in your actual work:

#### Before Training
```
"Fix this function"
```

#### After Training
```
"The `calculateTotal()` function in `src/cart.js` is returning incorrect 
values when discount codes are applied. It should subtract the discount 
percentage from the subtotal before adding tax, but it's currently applying 
the discount after tax.

Please provide:
1. A corrected version of the function
2. Unit tests to verify the fix
3. Comments explaining the calculation order

Expected behavior: 
- Subtotal: $100
- Discount (10%): -$10
- Taxable amount: $90
- Tax (8%): +$7.20
- Total: $97.20"
```

### Benefits You'll See

✅ **Faster responses** - AI understands immediately  
✅ **More accurate solutions** - Fewer iterations needed  
✅ **Better code quality** - AI has context to make good decisions  
✅ **Less frustration** - Clear communication reduces back-and-forth

---

## Common Mistakes to Avoid

### 1. Being Too Vague
❌ "Fix the bug"  
✅ "Fix the null pointer exception in `UserService.java` line 45"

### 2. Missing Context
❌ "Make it faster"  
✅ "Optimize the `searchUsers()` function - it's taking 3 seconds with 10K records"

### 3. No Output Specification
❌ "Help with this code"  
✅ "Review this code and provide a list of security vulnerabilities with severity ratings"

### 4. Forgetting Constraints
❌ "Refactor this"  
✅ "Refactor this to use async/await, maintaining Node.js 14 compatibility"

### 5. Unstructured Prompts
❌ Long paragraph with everything mixed together  
✅ Organized with sections, bullet points, or numbered lists

---

## Tips for Success

### 1. Start Simple
Don't try to write perfect prompts immediately. Start with your natural style and improve iteratively.

### 2. Be Specific
The more specific you are, the better the AI can help. Include:
- File names and line numbers
- Expected vs actual behavior
- Error messages
- Relevant context

### 3. Structure Your Prompts
Use formatting to make prompts scannable:
- Bullet points for lists
- Numbered steps for sequences
- Code blocks for examples
- Sections for different topics

### 4. State Your Constraints
Always mention:
- Performance requirements
- Compatibility needs
- Style preferences
- Security concerns

### 5. Specify Output Format
Tell the AI what you want:
- Code diffs
- Complete files
- Explanations
- Step-by-step guides
- Test cases

---

## Practice Exercises

### Exercise 1: Basic Improvement
Take this vague prompt and improve it:
```
"The login doesn't work"
```

**Hints**: What file? What's the symptom? What should happen?

### Exercise 2: Add Context
Enhance this prompt with context:
```
"Optimize this function"
```

**Hints**: What function? What's slow? What's the target performance?

### Exercise 3: Structure It
Reorganize this messy prompt:
```
"I need help with the user registration it's not validating emails properly 
and also the password requirements aren't being enforced and we need to make 
sure it works with our existing database schema"
```

**Hints**: Break into sections, use bullet points, separate concerns.

---

## Next Steps

### Continue Learning
1. Practice with real code issues
2. Compare your prompts before/after training
3. Share learnings with your team
4. Run additional training sessions for different scenarios

### Advanced Topics
- Team-specific prompt templates
- Domain-specific prompting patterns
- Collaborative prompt engineering
- Prompt optimization for different AI models

### Related Competencies
- **review-code**: Apply improved prompting to code reviews
- **evolve-code-iteratively**: Use structured prompts for iterative development
- **deepen-tech-spec-developer**: Practice detailed technical specifications

---

## Conclusion

Effective prompt engineering is a skill that improves with practice. This competency provides a safe environment to experiment, receive feedback, and develop better communication patterns with AI assistants.

**Remember**: The goal isn't to write "perfect" prompts, but to write **clear, specific, and well-structured** prompts that help the AI help you effectively.

Happy prompting! 🚀

---

**Need Help?**
- Review the prompt file: `olaf-core/competencies/developer/prompts/coach-developers-to-prompt`
- Check the description: `docs/coach-developers-to-prompt/description.md`
- Consult the main developer competency documentation
