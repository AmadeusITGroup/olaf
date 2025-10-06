# Test Repository Specifications

This document defines the specifications for test repositories used in the AI Agent Capability Benchmark.

## Repository Selection Criteria

Test repositories should be:
1. **Realistic**: Reflect actual production codebases
2. **Stable**: Not undergoing active development during testing
3. **Well-formed**: Have clear entry points and structure
4. **Documented**: At least minimal documentation
5. **Tested**: Some test coverage present
6. **Accessible**: Publicly available or easily shared
7. **Representative**: Cover common technology stacks

## Size Classifications

### Small Repository (S)
- **Lines of Code**: 500-1,000
- **Files**: 5-15
- **Modules/Components**: 2-5
- **Dependencies**: Minimal (0-5 external)
- **Complexity**: Low

**Recommended Types**:
- CLI utilities
- Simple libraries
- Code generators
- Single-purpose tools

### Medium Repository (M)
- **Lines of Code**: 3,000-7,000
- **Files**: 20-50
- **Modules/Components**: 5-15
- **Dependencies**: Moderate (5-20 external)
- **Complexity**: Moderate

**Recommended Types**:
- REST APIs
- Web services
- Desktop applications
- Framework libraries

### Large Repository (L)
- **Lines of Code**: 10,000-30,000
- **Files**: 50-150
- **Modules/Components**: 15-50
- **Dependencies**: Complex (20+ external)
- **Complexity**: High

**Recommended Types**:
- Full-stack applications
- Microservice sets
- Enterprise applications
- Platform components

## Repository Characteristics Matrix

Each test repository should have these characteristics documented:

| Characteristic | Measurement | Notes |
|----------------|-------------|-------|
| **Size** | S/M/L | Lines of code |
| **Primary Language** | [Language] | Main implementation language |
| **Secondary Languages** | [Languages] | Config, scripts, etc. |
| **Test Coverage** | XX% | Percentage of code covered |
| **Documentation Level** | Low/Medium/High | Quality and completeness |
| **Architecture Style** | [Style] | Layered, microservice, etc. |
| **Build Complexity** | Low/Medium/High | Number of build steps |
| **Dependency Count** | [Number] | External dependencies |
| **Cyclomatic Complexity** | [Average] | Code complexity metric |
| **Technical Debt** | Low/Medium/High | Known issues and debt |
| **Last Updated** | [Date] | Most recent commit |
| **Activity Level** | [Commits/month] | Development frequency |

## Required Repository Elements

### Must Have
1. **README.md** - Basic project information
2. **License** - Clear licensing
3. **Source Code** - Well-organized code
4. **Build Configuration** - Build files (package.json, pom.xml, etc.)
5. **Tests** - At least some test coverage
6. **Git History** - Meaningful commit history
7. **Entry Point** - Clear way to run/use the code

### Should Have
8. **Dependencies File** - Requirements, package.json, etc.
9. **Configuration Files** - Settings and config
10. **Documentation** - At least basic docs
11. **Examples** - Usage examples
12. **CI Configuration** - Build/test automation setup

### Nice to Have
13. **CONTRIBUTING.md** - Contribution guidelines
14. **CHANGELOG.md** - Change history
15. **Architecture Documentation** - Design docs
16. **API Documentation** - If applicable
17. **Deployment Docs** - How to deploy

## Preparation Checklist

Before using a repository for benchmarking:

- [ ] Repository cloned and verified buildable
- [ ] All dependencies installable
- [ ] Tests runnable
- [ ] Documentation reviewed for accuracy
- [ ] Characteristics matrix filled out
- [ ] Known issues documented
- [ ] Baseline metrics captured:
  - [ ] Lines of code
  - [ ] File count
  - [ ] Test coverage percentage
  - [ ] Build time
  - [ ] Test execution time
  - [ ] Complexity metrics
- [ ] Recent feature identified and documented
- [ ] Brittle code areas identified
- [ ] Repository tagged/versioned for stability

## Example Test Repositories

### Python Small: CLI Task Manager

**Characteristics**:
- **Size**: S (~800 LOC)
- **Language**: Python 3.9+
- **Purpose**: Command-line task management tool
- **Test Coverage**: 65%
- **Documentation**: Basic README
- **Build**: Simple (pip install)
- **Dependencies**: 3 (click, sqlite3, pytest)
- **Complexity**: Low (avg. cyclomatic 3.2)

**Why Good for Benchmark**:
- Clear entry point (CLI)
- Simple architecture
- Mix of file I/O and logic
- Some test coverage gaps
- Recent feature: recurring tasks

### C# Medium: REST API Service

**Characteristics**:
- **Size**: M (~5,000 LOC)
- **Language**: C# .NET 6
- **Purpose**: Product catalog API
- **Test Coverage**: 72%
- **Documentation**: README + API docs
- **Build**: Moderate (dotnet build)
- **Dependencies**: 12 NuGet packages
- **Complexity**: Moderate (avg. cyclomatic 5.8)

**Why Good for Benchmark**:
- Layered architecture
- Database integration
- Authentication/authorization
- Integration and unit tests
- Some brittle error handling
- Recent feature: search filters

### TypeScript Large: Web Application

**Characteristics**:
- **Size**: L (~15,000 LOC)
- **Language**: TypeScript/React
- **Purpose**: Project management SaaS
- **Test Coverage**: 68%
- **Documentation**: README + wiki
- **Build**: Complex (npm scripts, webpack)
- **Dependencies**: 45+ npm packages
- **Complexity**: High (avg. cyclomatic 7.3)

**Why Good for Benchmark**:
- Full-stack application
- Complex state management
- Multiple modules/features
- Mixed test quality
- Known technical debt
- Recent feature: real-time notifications

## Repository Maintenance

### Version Control
- Tag repository version used for benchmarks
- Document any local modifications
- Keep original repository separate from benchmark runs

### Updates
- Re-evaluate repositories quarterly
- Update characteristics matrix
- Re-capture baseline metrics
- Document changes

### Repository Retirement
Consider retiring a test repository if:
- Becomes too well-known (agents may have it in training data)
- Underlying frameworks become obsolete
- Better alternatives become available
- Consistently produces similar results (not differentiating)

## Creating Custom Test Repositories

If creating purpose-built test repositories:

1. **Start with real code** - Don't create artificial examples
2. **Introduce variety** - Mix well-written and problematic code
3. **Add realistic history** - Commit history should tell a story
4. **Include documentation gaps** - Some docs, but not complete
5. **Plant test coverage gaps** - Intentional untested areas
6. **Add technical debt** - Some TODO comments, known issues
7. **Make it buildable** - Must be able to actually run the code
8. **Version appropriately** - Tag stable versions for benchmarking

### Template Structure
```
test-repo-name/
├── README.md (basic, some gaps)
├── src/
│   ├── core/ (well-tested)
│   ├── features/ (mixed quality)
│   └── utils/ (some brittle code)
├── tests/
│   ├── unit/ (good coverage)
│   └── integration/ (sparse)
├── docs/ (incomplete)
├── build files
└── .git (meaningful history)
```

---

**Version**: 1.0  
**Last Updated**: 2025-10-06  
**Maintainer**: [Your team]