# Chapter Mode for Long-Running Processes

OLAF supports a "chapter mode" for handling complex, multi-phase workflows that would otherwise exceed context windows or suffer from context degradation (infamous "context rot").

## How It Works

This approach breaks down lengthy processes into discrete, manageable process steps (aka chapters) where:

- **Each chapter represents a distinct deliverable** of the overall process
- **Outputs from one chapter are persisted** and can be referenced in subsequent chapters. Persisted files can be markdown , json , csv , xml. We mostly use json and md.
- **The system can gracefully handle user sessions** between chapters, allowing for fresh LLM contexts. in fact it has been especially for those agents ( most of them nowadays) that do not allows to restart a fresh session with some context.
- **Users are encouraged but not forced to restart from any completed chapter** without losing progress

## Problem Solved

This design helps mitigate "context rot" issues that can occur when processing large amounts of information in a single session. This context rot is mostly dues to ambiguities, distractors or needle in a hay stack. These are introduced by the user or by the ouput of the models.


## Current Status

While this is currently implemented as a palliative solution, it provides a practical approach until agent and model capabilities evolve to better handle long-context scenarios.


## Future Enhancements

Looking ahead, we aim to refine chapter mode by:
- ensuring outcomes from the models are less prone to ambiguity, distraction, or irrelevant information.
- enforcing stricter guidelines for input clarity and relevance.

## Benefits

- **Context Management**: Prevents context window overflow
- **Process Continuity**: Maintain progress across sessions
- **Flexible Execution**: Resume from any completed chapter
- **Quality Preservation**: Avoid degradation from excessive context
- **Session Independence**: Fresh LLM context for each chapter
- **User Guidance**: Encourages users to follow structured workflows and check outcomes during process rather than at end of it

## Limits

- **UX is not yet optimized**: The user experience can still be improved, particularly in terms of guiding users through the chapter process and providing clearer feedback on their progress.
