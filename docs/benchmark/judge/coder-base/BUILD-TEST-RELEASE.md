# Build, Test & Release Documentation

## Overview

This document provides comprehensive instructions for building, testing, and releasing the Otter Framework - a highly modular Angular framework designed to accelerate web application development.

## Prerequisites

### Required Software

- **Node.js**: Version >=18.0.0 (LTS recommended)
- **Yarn**: Package manager (embedded in repository via corepack)  
- **Git**: Version control system
- **Chrome**: Required for running tests
- **Java JDK**: Required for certain build processes (optional)

### Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AmadeusITGroup/otter.git
   cd otter
   ```

2. **Install dependencies:**
   ```bash
   yarn install
   ```

3. **Configure parallel processing (optional):**
   ```bash
   yarn print:nx-parallel >> .env
   ```

## Build Process

### Full Build

Build all modules and packages:

```bash
yarn build
```

This command:
- Compiles TypeScript code
- Generates distributable files
- Processes assets and configurations
- Creates package bundles in `dist/` directories

### Targeted Builds

Build specific components using Nx:

```bash
# Build core package only
yarn nx build core

# Build TypeScript only (faster)
yarn build:ts

# Build tools and utilities
yarn build:tools

# Build linting tools
yarn build:lint

# Build Swagger documentation
yarn build:swagger-gen
```

### Build Outputs

Results are stored in:
- `packages/@<scope>/<module>/dist/` - Individual package builds
- Generated documentation in `generated-doc/`
- Compiled assets and bundles

### Build Performance

- **Nx Cache**: Leverages local and remote caching for faster builds
- **Parallel Execution**: Uses `NX_PARALLEL` environment variable
- **Incremental Builds**: Only rebuilds changed components

```bash
# Clear Nx cache if needed
yarn nx reset

# Build only affected packages
yarn build:affected
```

## Testing

### Unit Tests

Run all unit tests:

```bash
yarn test
```

Run tests for specific packages:

```bash
# Test core package only
yarn nx test core

# Test affected packages only
yarn test:affected
```

### Integration Tests

Integration tests use Verdaccio for npm-like testing:

```bash
yarn test-int
```

### End-to-End Tests

```bash
yarn test-e2e
```

### Linting and Code Quality

Check code formatting and style:

```bash
yarn lint

# Lint specific package
yarn nx lint core

# Lint affected packages only
yarn lint:affected
```

### Test Configuration

- **Jest**: Primary testing framework
- **Playwright**: E2E testing
- **Verdaccio**: Local npm registry for integration tests
- **Chrome**: Browser for test execution

### Test Coverage

Tests generate coverage reports integrated with:
- Codecov for coverage tracking
- GitHub Actions for CI/CD validation

## Release Process

### Version Management

The project uses automated versioning with GitVersion:

1. **Version Calculation**: Based on Git history and branch naming
2. **Release Branches**: Follow pattern `release/(major).(minor)(.patch-prerelease)?`
3. **Prerelease Handling**: Automatic detection and tagging

### Publishing Workflow

#### 1. Prepare Release

```bash
# Set version for all packages
yarn set:version <version>

# Harmonize package versions
yarn harmonize:version
```

#### 2. Build and Test

Ensure all quality checks pass:

```bash
yarn build
yarn lint  
yarn test
yarn test-int
```

#### 3. Publish Packages

```bash
# Prepare packages for publishing
yarn nx run-many --target=prepare-publish --exclude-task-dependencies

# Publish to npm
yarn publish
```

#### 4. Publish Extensions

```bash
# Publish VSCode and Chrome extensions
yarn publish:extensions
```

### Local Testing with Verdaccio

Test publishing process locally:

```bash
# Start local npm registry
yarn verdaccio:start

# Publish to local registry
yarn verdaccio:publish

# Clean local registry
yarn verdaccio:clean

# Stop local registry
yarn verdaccio:stop
```

### Release Automation

The CI/CD pipeline handles:

- **Automatic versioning** based on branch and commit patterns
- **Quality gates** (build, lint, test) before release
- **Multi-package publishing** with dependency management
- **Documentation generation** and deployment
- **Extension publishing** to marketplaces

### Release Branches

- **main**: Latest development, creates prerelease versions
- **release/x.y**: Stable releases, creates production versions
- **release/x.y.0-next**: Next major version previews

### GitHub Actions Workflow

The release process is automated through:

1. **Main CI**: Triggered on push/PR to main or release branches
2. **Version Job**: Calculates next version using GitVersion
3. **Build Job**: Compiles and validates all packages
4. **Test Jobs**: Runs unit, integration, and E2E tests
5. **Publish Job**: Releases packages to npm with provenance
6. **Documentation**: Updates and deploys documentation

## Troubleshooting

### Common Issues

**SSL Certificate Issues (Behind Proxy):**
```bash
# Set certificate path
export NODE_EXTRA_CA_CERTS=/path/to/certificate
# Or configure Yarn
yarn config set httpsCertFilePath /path/to/certificate
```

**Build Cache Issues:**
```bash
# Clear all caches
yarn nx reset
yarn clear
```

**Dependency Issues:**
```bash
# Clean and reinstall
rm -rf node_modules
yarn install
```

**Test Failures:**
```bash
# Run tests with verbose output
yarn nx test <package> --verbose

# Update test snapshots if needed
yarn nx test <package> --updateSnapshot
```

### Performance Optimization

- Use `yarn build:ts` for faster TypeScript-only builds
- Enable Nx Cloud for remote caching
- Increase parallel processes with `NX_PARALLEL` environment variable
- Use `--affected` flags to build/test only changed packages

### Development Workflow

1. **Feature Development**: Work on feature branches
2. **Local Testing**: Use `yarn build && yarn test` frequently
3. **Integration Testing**: Test with Verdaccio before PR
4. **Code Quality**: Ensure linting and formatting pass
5. **Documentation**: Update relevant docs with changes

## Links and References

- [Contributing Guidelines](./CONTRIBUTING.md)
- [Architecture Documentation](./docs/core/ARCHITECTURE.md)
- [Getting Started Guide](./docs/core/START_NEW_APPLICATION.md)
- [Nx Documentation](https://nx.dev/)
- [Verdaccio Setup](./.verdaccio/README.md)
- [GitHub Repository](https://github.com/AmadeusITGroup/otter)
