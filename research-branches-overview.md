# Research Branches Overview

**research-assist-with-troubleshooting**
This branch focuses on developing AI-assisted troubleshooting capabilities for technical issues. The research aims to create systematic approaches for diagnosing problems, guiding users through resolution steps, and building knowledge bases from troubleshooting sessions. The goal is to enhance the framework's ability to provide contextual technical support and automate common problem-solving workflows.

The core idea is to:
- List potential error messages from code (scripted - script created by AI based on language)
- Map error messages from logs to those potential error messages (hybrid approach - Reduce-MAP with AI)
- Analyze the vicinity of the log error message with the code (AI)
- Provide potential root cause to user for confirmation (AI)
- Propose to fix the root cause if this requires very few modifications, or propose a plan to fix the root cause to the user for confirmation (AI)
- Potentially create an issue or ticket with the analysis and the fix plan (AI + MCP) 


**research-context-indexing**
This branch explores semantic search and context indexing capabilities to improve information retrieval within the OLAF framework. The research focuses on document embedding strategies, query optimization techniques, and algorithms for intelligent context selection. The objective is to enable more precise and relevant information discovery across large codebases and documentation sets.

The core idea is:
- Create reference files (e.g., using the onboarding prompt that creates 25+ informative files from the code) (AI)
- Create an index (MD) file that classifies those resource files by intent (e.g., unit testing, business analysis, etc.)
- In each prompt that has a clear intent (e.g., unit testing, business analysis, etc.), add a section to use the context index to load the resource files for the intent (AI) on demand
- This way we can provide on-demand and fit-to-purpose context to the prompt to help it generate better responses, based on the intent - as the resource files are created from the code, they are relevant to the codebase

**research-design-to-code**
This branch investigates automated generation of code from design files and specifications. The research covers design file parsing, UI component mapping strategies, and integration with automated testing frameworks. The aim is to bridge the gap between visual designs and functional code implementation, reducing manual translation effort.


Note: This is done in the context of the French genAI Think Tank
The core idea is:
- Delineate each sequenced task for the process of requirements engineering (requirement elicitation, requirement analysis, requirement validation, requirement documentation and specification)
- For each sequenced task, create a prompt chain that will guide the user through the task and output standardized output
- We expect that by standardizing the process and output, we can create a more systematic and repeatable process for requirements engineering and ultimately improve the quality of the requirements for coders, testers and technical writers



**research-middleware-upgrade**
This branch examines strategies for modernizing and upgrading legacy middleware systems. The research focuses on upgrade pathways, legacy system integration approaches, and performance optimization techniques. The goal is to provide systematic guidance for organizations transitioning from outdated middleware to modern architectures.


The core idea is:
- Get technical release notes from middleware provider (be it internal or external)
- Get a benchmark of the unit and potentially integration tests, as well as any compiling/linking/running situation (using logs)
- Then we need to explore:
    - Try to apply the upgrade and see compiling/linting errors - fix them based on specific knowledge provided in the release notes, or create resource files (to be determined which ones) and the LLM knowledge for the language and environment
    - Understand which approach converges to a solution (try and fix one after the other, fix most critical first to get dependent issues resolved as a result, etc.)
- The intent is to reduce the time it takes to upgrade, especially for internal middleware that no public LLM can be trained on

Note: Other approaches could be to fine-tune a foundational LLM on the internal middleware codebase, but this is not a priority at the moment and would require understanding how to build a useful knowledge base for training, reinforcement and testing from a codebase that may not be large enough or have feedback loops to be useful

**research-migration-to-cloud-native-architecture**
This branch develops comprehensive approaches for migrating legacy systems to cloud-native architectures. The research covers assessment of current architectures, microservices design patterns, and containerization strategies with Kubernetes. The objective is to create structured migration plans that minimize risks while maximizing cloud benefits.

The core idea is:
- Analyze current codebase with a DDD (domain-driven design) approach (AI)
- Analyze and propose a potential architecture that needs to be reviewed by the user (AI & Architects)
- Analyze and propose a potential microservices strategy that needs to be reviewed by the user (AI & Architects)
- Based on a target framework (e.g., Quarkus, Spring Boot, etc.), scaffold the target implementation (AI and scripted)
- We would expect to assist and reduce time for analysis and proposal with some what-if scenarios

**research-orchestrate-comprehensive-codebase-benchmark**
This branch investigates methods for comprehensive codebase assessment and benchmarking. The research aims to determine if existing onboarding capabilities are sufficient or if additional complexity is needed for thorough code analysis. The goal is to streamline codebase evaluation processes without over-complicating the user experience.

The core idea is:
- To analyze current codebase using the onboarding prompt (AI)
- Then to extend the same for a DFD analysis (AI)
- Then to extend on implementation aspects (e.g., error handling, AAA, logging/observability, etc.)
- Then to analyze current documentation (e.g., specification, manuals, etc.)
- The intent is to ensure proper material exists, allowing any newcomer to create a path-to-onboard based on their profile (e.g., tester, coder, technical writer, business analyst, etc.)

**research-test-prompts-from-documentation**
This branch explores automated generation of prompts from large documentation sources. The research focuses on extracting actionable workflows from external documentation like MCP or CrewAI guides. The objective is to automatically create specialized prompts that leverage comprehensive external knowledge bases.

The core idea is:
- To analyze some public or private technical documentation (e.g., MCP, CrewAI, etc.)
- Based on the user intent, to create prompts and scripts that scaffold and accelerate the creation of a new tool (e.g., create a new MCP client, MCP server, a CrewAI team, etc.)
- The intent is to provide a process and example on the competency of innovating based on emerging technologies without investing too deep knowledge and taking into account the fact that such new technologies are going to evolve or be deprecated at some point (e.g., MCP, Langchain, etc.)

**research-ui-migration**
This branch develops strategies for modernizing user interfaces and migrating between UI frameworks. The research covers modern web interface patterns, component architecture design, and user experience improvement methodologies. The goal is to provide systematic approaches for UI modernization projects while maintaining functionality and improving usability.

The core idea is:
- Starting from a codebase that has UI, analyze the UI and the codebase to understand the UX and the UI
- Get a target technology and elaborate a migration plan (from atomic component to more complex? from story maps or from user actions?)
- Then scaffold the target implementation (AI and scripted)
- We expect to assist and reduce time for analysis and proposal with some what-if scenarios
