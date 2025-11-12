---

name: assess-code-quality-principles

description: Critical evaluation of codebase against established engineering principles (SOLID, DRY, YAGNI) with evidence-based scoring and specific improvement recommendations.

tags: [code-quality, assessment, solid-principles, best-practices, evaluation]

---



## Framework Validation
## Time Retrieval
Use this common helper only when saving a file or creating a folder that embeds a timestamp in its name: `olaf-core/competencies/common/prompts/time-retrieval.md`. Do not prompt for time when merely reading or loading files.- <olaf-interaction-protocols> - Appropriate execution protocol

You MUST strictly apply <olaf-framework-validation>.

## Time Retrieval
If you need to generate a filename or identifier that includes a timestamp (e.g., YYYYMMDD-HHmm or YYYYMMDD), obtain the current time from the terminal, not from model/context data.

- Windows (date+time): `Get-Date -Format "yyyyMMdd-HHmm"`
- Windows (date only): `Get-Date -Format "yyyyMMdd"`
- Unix/Linux/macOS (date+time): `date +"%Y%m%d-%H%M"`
- Unix/Linux/macOS (date only): `date +"%Y%m%d"`




## Input Parameters

You MUST request these parameters if not provided by the user:

- **application_name**: string - Name of the application for file naming (REQUIRED)

- **code_path**: string - Path to the codebase to assess (REQUIRED)  

- **tech_spec_path**: string - Path to existing technical specification (OPTIONAL)

- **focus_areas**: array[string] - Specific areas to focus on (OPTIONAL, defaults to all)



## User Interaction Protocol

You MUST follow the established interaction protocol strictly:

- Act / Propose-Act / Propose-Confirm-Act (defined externally)

- You WILL use Propose-Act for this competency due to assessment nature requiring user validation



## Assessment Framework



### Quality Evaluation Scale

```

Grade Scale:

A (90-100): Excellent - Best practices implemented, exemplary code quality

B (80-89):  Good - Generally well-implemented, minor improvements needed

C (70-79):  Acceptable - Functional but needs attention, some issues identified  

D (60-69):  Poor - Significant issues found, requires immediate attention

F (0-59):   Critical - Major problems, blocks development efficiency/quality

```



### Assessment Categories

1. **SOLID Principles Adherence** - Evidence-based evaluation of design principles

2. **Code Quality Metrics** - DRY, YAGNI, complexity, maintainability assessment  

3. **Testing Quality** - Unit test coverage, quality, and effectiveness evaluation

4. **Architecture Quality** - Module structure, coupling, cohesion analysis

5. **Security Practices** - Security implementation patterns and vulnerabilities

6. **Performance Patterns** - Performance anti-patterns and optimization opportunities



## Process



### 1. Codebase Analysis Phase

**Comprehensive Code Scanning:**

- Identify all source files and their purposes

- Map architectural patterns and design implementations

- Extract metrics (complexity, coupling, test coverage)

- Catalog design patterns usage

- Identify anti-patterns and code smells



### 2. Principle-Based Evaluation Phase

**SOLID Principles Assessment:**

- **Single Responsibility**: Analyze classes for multiple responsibilities

- **Open/Closed**: Evaluate extensibility without modification

- **Liskov Substitution**: Check inheritance and interface implementations

- **Interface Segregation**: Assess interface design and client dependencies

- **Dependency Inversion**: Evaluate abstraction usage and concrete dependencies



**Code Quality Assessment:**

- **DRY Violations**: Identify code duplication with impact analysis

- **YAGNI Violations**: Find over-engineering and unused functionality

- **Complexity Analysis**: Calculate cyclomatic complexity and maintainability

- **Naming Conventions**: Assess code readability and consistency



### 3. Evidence Collection Phase

**Documentation of Findings:**

- Collect specific code examples for each violation

- Quantify impact of quality issues

- Calculate metrics and scores for each category

- Prioritize recommendations by impact and effort



### 4. Scorecard Generation Phase

**Quality Scorecard Creation:**

- Overall quality score calculation

- Category-specific grades and explanations

- Specific improvement recommendations with code examples

- Priority-based action plan with effort estimates



## Output Format

You WILL generate outputs following this structure:

- Primary deliverable: Follow template structure below

- Supporting files: `[id:findings_dir]assessments/code-quality-assessment-{application_name}-YYYYMMDD-NNN.md`

- Documentation: Complete scorecard with evidence and recommendations



**File Naming Convention**:

- {application_name} is kebab-case formatted

- YYYYMMDD-NNN follows standard OLAF naming



## Assessment Areas Detail



### SOLID Principles Assessment (25 points)

**Single Responsibility Principle (5 points)**

- Identify classes with multiple responsibilities

- Measure class complexity and method count

- Evaluate package cohesion



**Open/Closed Principle (5 points)**  

- Assess extension points and plugin architectures

- Identify modification hotspots

- Evaluate interface and abstract class usage



**Liskov Substitution Principle (5 points)**

- Check inheritance hierarchies for LSP violations

- Validate interface implementations

- Test substitutability in practice



**Interface Segregation Principle (5 points)**

- Analyze interface size and client usage

- Identify fat interfaces and unused methods

- Evaluate client-specific interfaces



**Dependency Inversion Principle (5 points)**

- Assess abstraction vs. concrete dependency usage

- Evaluate dependency injection patterns

- Check for high-level module dependencies on low-level modules



### Code Quality Metrics (25 points)

**DRY Assessment (8 points)**

- Code duplication detection and quantification

- Impact analysis of duplication on maintainability

- Refactoring opportunities identification



**YAGNI Assessment (7 points)**

- Unused code detection (dead code, unused methods)

- Over-engineering identification

- Speculative generality anti-pattern detection



**Complexity Analysis (10 points)**

- Cyclomatic complexity calculation

- Cognitive complexity assessment

- Method and class size analysis



### Testing Quality (20 points)

**Test Coverage (7 points)**

- Line, branch, and method coverage calculation

- Coverage quality assessment (meaningful vs. trivial tests)

- Missing test identification



**Test Quality (8 points)**

- Test design pattern assessment

- Mock usage evaluation  

- Test maintainability analysis



**Test Strategy (5 points)**

- Test pyramid compliance

- Integration test coverage

- End-to-end test strategy



### Architecture Quality (15 points)

**Module Structure (5 points)**

- Package organization assessment

- Module boundary evaluation

- Layer separation analysis



**Coupling Analysis (5 points)**

- Inter-module dependency assessment

- Circular dependency detection

- Coupling metrics calculation



**Cohesion Analysis (5 points)**

- Package cohesion measurement

- Class responsibility focus

- Module purpose clarity



### Security Practices (10 points)

- Input validation patterns

- Authentication/authorization implementation  

- Security vulnerability assessment

- Cryptographic usage evaluation



### Performance Patterns (5 points)

- Performance anti-pattern detection

- Resource management assessment

- Caching strategy evaluation

- Database interaction optimization



## Domain-Specific Rules

- Rule 1: Always provide specific code examples for violations

- Rule 2: Quantify impact with metrics and measurements

- Rule 3: Prioritize recommendations by impact and implementation effort

- Rule 4: Focus on actionable improvements, not theoretical concepts

- Rule 5: Validate findings through multiple code analysis techniques



## Required Actions

1. Analyze codebase comprehensively using automated and manual techniques

2. Generate evidence-based quality scorecard with specific examples

3. Create prioritized improvement plan with effort estimates

4. Provide code examples for both problems and solutions

5. Present findings for user review and feedback incorporation



## Success Criteria

You WILL consider the task complete when:

- [ ] Complete codebase analysis performed with comprehensive coverage

- [ ] Quality scorecard generated with evidence-based grades

- [ ] Specific code examples collected for all major findings

- [ ] Prioritized improvement recommendations created with effort estimates

- [ ] User review completed with feedback incorporated

- [ ] Assessment document created following template structure



⚠️ **Critical Requirements**

- MANDATORY: Use actual code examples, never theoretical descriptions

- NEVER provide grades without supporting evidence and specific code references

- ALWAYS quantify findings with metrics (percentages, counts, complexity scores)

- ALWAYS prioritize recommendations by business impact and implementation effort

- ALWAYS validate assessment accuracy through multiple analysis approaches