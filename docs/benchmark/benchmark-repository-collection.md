# Test Repository Collection

This directory contains specifications and links to test repositories for the AI Agent Benchmark.

## Repository Structure

```
test-repositories/
├── java/
│   ├── small-cli-json-processor/
│   ├── medium-spring-boot-api/
│   └── large-microservice-ecommerce/
├── csharp/
│   ├── small-log-analyzer/
│   ├── medium-aspnet-inventory/
│   └── large-crm-system/
├── cpp/
│   ├── small-text-processor/
│   ├── medium-data-structures/
│   └── large-game-engine/
└── python/
    ├── small-web-scraper/
    ├── medium-fastapi-recommender/
    └── large-ml-pipeline/
```

## Repository Standards

Each repository must include:

1. **baseline-metrics.json** - Pre-captured metrics
2. **known-issues.md** - Documented technical debt
3. **benchmark-tag** - Git tag for stable version
4. **README.md** - Basic setup instructions
5. **verification-tests.sh** - Automated verification

## Baseline Metrics Template

```json
{
  "repository": "java-small-cli-json-processor",
  "language": "Java",
  "size": "small",
  "captured_date": "2025-10-06",
  "metrics": {
    "loc": {
      "total": 1234,
      "source": 980,
      "test": 254,
      "comments": 156
    },
    "files": {
      "total": 18,
      "source": 12,
      "test": 6
    },
    "complexity": {
      "average_cyclomatic": 3.2,
      "max_cyclomatic": 12,
      "average_cognitive": 4.1
    },
    "coverage": {
      "line": 62.5,
      "branch": 58.3,
      "uncovered_lines": 378
    },
    "dependencies": {
      "direct": 5,
      "transitive": 23
    },
    "build_time_seconds": 45,
    "test_time_seconds": 12,
    "quality": {
      "code_smells": 8,
      "bugs": 2,
      "vulnerabilities": 1,
      "security_hotspots": 3,
      "technical_debt_minutes": 180
    }
  },
  "brittle_areas": [
    {
      "file": "src/main/java/parser/JsonParser.java",
      "reason": "High complexity (CC=12), low coverage (45%)",
      "priority": "high"
    },
    {
      "file": "src/main/java/validator/SchemaValidator.java",
      "reason": "No error handling, brittle validation logic",
      "priority": "medium"
    }
  ],
  "recent_features": [
    {
      "date": "2025-09-15",
      "commit": "a3f5b2c",
      "feature": "Add JSON schema validation",
      "files_changed": 3,
      "test_coverage": 45
    }
  ]
}
```

## Per-Language Requirements

### Java Repositories

**Build System**: Maven or Gradle  
**Test Framework**: JUnit 5  
**Coverage Tool**: JaCoCo  
**Static Analysis**: Checkstyle, PMD, SpotBugs  
**Security**: OWASP Dependency-Check  

**Must Include**:
- `pom.xml` or `build.gradle`
- `src/main/java` and `src/test/java` structure
- `.editorconfig` or `checkstyle.xml`
- `README.md` with build instructions

### C# Repositories

**Build System**: dotnet CLI  
**Test Framework**: xUnit or NUnit  
**Coverage Tool**: Coverlet  
**Static Analysis**: Roslyn Analyzers, StyleCop  
**Security**: dotnet list package --vulnerable  

**Must Include**:
- `.csproj` files
- `src/` and `tests/` or standard structure
- `.editorconfig`
- `README.md` with build instructions

### C++ Repositories

**Build System**: CMake  
**Test Framework**: Google Test or Catch2  
**Coverage Tool**: gcov/lcov  
**Static Analysis**: clang-tidy, cppcheck  
**Memory**: Valgrind configuration  

**Must Include**:
- `CMakeLists.txt`
- `src/`, `include/`, `tests/` structure
- `.clang-format`
- `README.md` with build instructions

### Python Repositories

**Packaging**: pip (requirements.txt) or poetry (pyproject.toml)  
**Test Framework**: pytest  
**Coverage Tool**: coverage.py  
**Static Analysis**: pylint, flake8, mypy  
**Security**: bandit, safety  

**Must Include**:
- `setup.py` or `pyproject.toml`
- Standard package structure
- `requirements.txt` and `requirements-dev.txt`
- `README.md` with setup instructions

---

## Repository Creation Checklist

When creating/selecting a test repository:

### Initial Setup
- [ ] Clone or create repository
- [ ] Verify it builds successfully
- [ ] Verify tests run successfully
- [ ] Install all analysis tools
- [ ] Capture baseline metrics

### Code Preparation
- [ ] Ensure realistic code quality (mix of good and problematic)
- [ ] Plant intentional issues for discovery
- [ ] Add some technical debt markers (TODOs)
- [ ] Vary test coverage (some modules well-tested, some gaps)
- [ ] Include recent feature in git history

### Documentation
- [ ] Create minimal README (intentionally incomplete)
- [ ] Document known issues
- [ ] Create baseline-metrics.json
- [ ] Add verification scripts
- [ ] Document expected benchmark outcomes

### Verification
- [ ] Tag stable version for benchmarking
- [ ] Test in clean environment
- [ ] Verify all tools work
- [ ] Run through benchmark manually once
- [ ] Document any special setup needed

### Maintenance
- [ ] Schedule quarterly review
- [ ] Version control (tag each benchmark run)
- [ ] Track if repository becomes "too known"
- [ ] Document changes between versions

---

**Next Steps**: Create actual repository implementations for each language and size category.