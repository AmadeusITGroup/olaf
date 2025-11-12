# Universal Coding Standards

## Code Quality Principles

### Readability & Maintainability
- **Clear naming**: Use descriptive names for variables, functions, and classes
- **Consistent indentation**: Follow language-specific conventions (2/4 spaces, tabs)
- **Function length**: Keep functions under 20-30 lines when possible
- **Cyclomatic complexity**: Aim for complexity < 10 per function
- **Magic numbers**: Replace with named constants
- **Comments**: Explain WHY, not WHAT the code does

### Security Standards
- **Input validation**: Validate all external inputs
- **Authentication**: Implement proper authentication mechanisms
- **Authorization**: Follow principle of least privilege
- **Data protection**: Encrypt sensitive data in transit and at rest
- **Error handling**: Don't expose sensitive information in error messages
- **SQL injection**: Use parameterized queries
- **XSS prevention**: Sanitize user inputs for web applications

### Performance Standards
- **Algorithm efficiency**: Choose appropriate algorithms and data structures
- **Resource management**: Properly dispose of resources (connections, files, memory)
- **Caching**: Implement appropriate caching strategies
- **Database queries**: Optimize queries and avoid N+1 problems
- **Memory usage**: Avoid memory leaks and unnecessary allocations
- **Network calls**: Minimize and batch external API calls

### Architecture & Design
- **Single Responsibility**: Each class/function should have one reason to change
- **Dependency Injection**: Use dependency injection for better testability
- **Interface segregation**: Keep interfaces focused and cohesive
- **Error boundaries**: Implement proper error handling at appropriate levels
- **Configuration**: Externalize configuration from code
- **Logging**: Implement structured logging with appropriate levels

### Testing Standards
- **Unit test coverage**: Aim for >80% code coverage
- **Test naming**: Use descriptive test method names
- **Test structure**: Follow Arrange-Act-Assert pattern
- **Integration tests**: Test critical business flows end-to-end
- **Test isolation**: Tests should not depend on each other
- **Mocking**: Mock external dependencies appropriately

### Version Control & Documentation
- **Commit messages**: Write clear, descriptive commit messages
- **Branch naming**: Use consistent branch naming conventions
- **Code reviews**: Require code reviews for all changes
- **Documentation**: Keep README and API documentation current
- **Changelog**: Maintain a changelog for releases
- **License**: Include appropriate license information

## Language-Specific Extensions
*(Teams should extend these standards with language-specific guidelines)*

## Team-Specific Overrides
*(Teams can override or extend any of these standards in their team-specific files)*