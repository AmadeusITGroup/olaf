<olaf-query-competency-index>

# Competency Index

**Last Updated:** 20250911-1338 CEDT

## How to Use This Index

If requested for a competency, you MUST perform the following steps:

1. **Iterate sequentially** through the mappings below.
2. For each mapping, check if the user's request contains any of the phrases in the first element (patterns array).
3. Use the **first mapping** that has a matching pattern. Stop searching once a match is found.
4. Once a match is found, use the second element (workflow) and third element (protocol) to proceed.
5. If no pattern matches after checking all mappings, use your best judgment to select the most relevant one.

example:  [["review code", "check code", "code review", "examine code"], "developer/review-code.md", "Propose-Act"]
patterns array: ["review code", "check code", "code review", "examine code"],
File name of the prompt to load and execute: "developer/review-code.md",
Protocol to use when interacting through the chat with USER: "Propose-Act"
Important note: All prompt files are now organized by role in [id:prompts_dir] subdirectories

## Maintenance Instructions

To add a new competency:

1. Add a new array entry at the appropriate location
2. Format it as: `[["pattern1", "pattern2", ...], "prompt-file.md", "Protocol-Name"]`
3. Update the "Last Updated" timestamp at the top of this file

To remove a competency:

1. Locate and delete the entire array entry for that competency
2. Update the "Last Updated" timestamp at the top of this file

## Mappings

```
[

  [["should i use ai", "use ai for", "ai or ide", "ai vs ide"], "other-users/should-i-use-ai.md", "Act"],
  [["handover", "conversation handover"], "project-manager/prepare-conversation-handover.md", "Act"],
  [["store conversation", "save chat"], "project-manager/store-conversation-record.md", "Act"],
  [["decision record", "adr", "document decision"], "project-manager/create-decision-record.md", "Act"],

  [["progress", "status update", "how are we doing"], "project-manager/review-progress.md", "Act"],
  [["tasklist", "task list", "generate tasklist", "create tasklist"], "project-manager/generate-tasklist.md", "Act"],
  [["changelog", "add to changelog"], "project-manager/create-changelog-entry.md", "Act"],
  [["archive changelog", "clean changelog"], "project-manager/archive-changelog-entries.md", "Propose-Confirm-Act"],
  [["analyze changelog", "summarize changes"], "project-manager/analyze-changelog-and-report.md", "Act"],
  [["person record", "add team member"], "project-manager/create-person-record.md", "Act"],
  [["generate commits", "commits from changelog"], "project-manager/generate-commits-from-changelog.md", "Act"],
  [["release notes", "generate release notes", "professional release notes", "create release notes"], "project-manager/generate-professional-release-notes.md", "Act"],

  [["review code", "check code", "code review", "examine code"], "developer/review-code.md", "Act"],
  [["review modified", "modified files", "review changes"], "developer/review-modified-files.md", "Act"],
  [["review pr", "pull request", "check pr"], "developer/review-github-pr.md", "Act"],
  [["accessibility review", "accessibility check", "wcag review", "accessibility compliance"], "developer/review-code-accessibility.md", "Act"],
  [["analyze function", "function analysis", "function complexity", "analyze function complexity"], "developer/analyze-function-complexity.md", "Act"],
  [["evolve code", "iterative development"], "developer/evolve-code-iteratively.md", "Act"],
  [["augment unit tests", "augment code unit test", "unit test augmentation", "improve test coverage iteratively"], "developer/augment-code-unit-test.md", "Act"],

  [["search and learn", "learn and search", "search & learn"], "researcher/search-and-learn.md", "Act"],
  [["autonomous research", "free research", "comprehensive research", "conduct research"], "researcher/autonomous-comprehensive-research.md", "Act"],
 [["research and report", "controlled research", "supervised research", "step by step research"], "researcher/research-and-report.md", "Propose-Confirm-Act"],
  [["tech spec from code", "spec from code"], "developer/generate-tech-spec-from-code.md", "Act"],

  [["bootstrap functional spec", "func spec from code"], "business-analyst/bootstrap-functional-spec-from-code.md", "Act"],
  [["user story", "story review"], "business-analyst/review-user-story.md", "Act"],

  [["questionnaire", "survey"], "business-analyst/generate-questionnaire.md", "Act"],
  [["write paper", "academic paper", "research paper"], "technical-writer/write-academic-paper.md", "Act"],
   [["create presentation", "generate presentation", "presentation from conversation", "create pptx", "generate pptx", "presentation and posts"], "technical-writer/create-presentation-and-posts-workflow.md", "Act"],
  [["step-by-step tutorial", "tutorial", "create tutorial", "generate tutorial", "step by step guide"], "prompt-engineer/generate-step-by-step-tutorial.md", "Act"],
  [["generate test plan", "test plan", "testing plan", "create test plan"], "tester/generate-test-plan.md", "Act"],
 [["create presentation", "pptx", "powerpoint", "slides", "blog post", "write blog", "brochure", "create brochure"], "technical-writer/create-presentation-and-posts-workflow.md", "Propose-Act"],
  [["generate tutorial", "create tutorial", "step by step tutorial", "tutorial from conversation", "conversation to tutorial"], "prompt-engineer/generate-step-by-step-tutorial.md", "Propose-Act"],
  [["create prompt", "new prompt", "write prompt"], "prompt-engineer/create-prompt.md", "Act"],
  [["convert prompt", "refactor prompt", "rewrite prompt"], "prompt-engineer/convert-prompt-existing.md", "Act"],
  [["work on job", "start job", "process job"], "project-manager/work-on-job.md", "Act"],
  [["create job", "new job", "define job"], "project-manager/create-job.md", "Act"],

  [["project onboarding", "onboard project", "analyze project", "project analysis", "comprehensive project analysis", "understand project"], "onboard/orchestrators/orchestrate-project-onboarding.md", "Propose-Act"],
  [["find expert", "who to contact", "contact expert", "expertise lookup", "find contact"], "other-users/find-expert-contact.md", "Act"],

  [["fix code smells", "code smells"], "developer/fix-code-smells.md", "Act"],
  [["test prompt", "try prompt", "test new prompt", "validate prompt", "prompt testing"], "prompt-engineer/test-prompt.md", "Act"],

]
end-of-competency-index
</olaf-query-competency-index>
