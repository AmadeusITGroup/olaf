# Angular Migration Prerequisites

## System Requirements

### Node.js Environment
- **Node.js**: Version compatible with target Angular version
- **npm/yarn/pnpm**: Latest stable version of chosen package manager
- **Angular CLI**: Global installation of target CLI version

### Development Tools
- **Git**: Version control with clean working directory
- **IDE/Editor**: VS Code with Angular extensions recommended
- **Browser**: Modern browser for testing (Chrome, Firefox, Safari)

## Pre-Migration Checklist

### Project State
- [ ] Clean git working directory (no uncommitted changes)
- [ ] All tests passing in current state
- [ ] Application builds and runs successfully
- [ ] Dependencies audit completed (no critical vulnerabilities)
- [ ] Backup created (git tag or branch)

### Environment Setup
- [ ] Node.js version verified and compatible
- [ ] Angular CLI installed globally
- [ ] Package manager (npm/yarn/pnpm) updated
- [ ] Development dependencies installed
- [ ] CI/CD pipelines documented

### Documentation
- [ ] Current architecture documented
- [ ] Component inventory completed
- [ ] Third-party dependencies cataloged
- [ ] Custom configurations documented
- [ ] Known issues and workarounds noted

## Version Compatibility Matrix

### Angular Version Support
| Angular | Node.js | TypeScript | Angular CLI |
|---------|---------|------------|-------------|
| 18.x    | 18.19+  | 5.4+       | 18.x        |
| 17.x    | 18.13+  | 5.2+       | 17.x        |
| 16.x    | 16.14+  | 4.9+       | 16.x        |
| 15.x    | 14.20+  | 4.8+       | 15.x        |
| 14.x    | 14.15+  | 4.7+       | 14.x        |

### Package Manager Compatibility
- **npm**: 8.0+ recommended
- **yarn**: 1.22+ or 3.0+ (Berry)
- **pnpm**: 7.0+ recommended

## Migration Path Planning

### Incremental Upgrade Strategy
1. **Single Version Jumps**: Recommended for most projects
2. **LTS to LTS**: For conservative upgrade approach
3. **Major Version Skips**: Only with thorough testing

### Risk Assessment Factors
- **Project Size**: Lines of code, component count
- **Custom Dependencies**: Third-party package compatibility
- **Team Experience**: Angular version familiarity
- **Timeline Constraints**: Available migration window
- **Testing Coverage**: Existing test suite quality

## Common Prerequisites Issues

### Node.js Version Mismatch
**Problem**: Incompatible Node.js version for target Angular
**Solution**: Use nvm/nvs to manage Node.js versions
```bash
# Install and use compatible Node.js version
nvm install 18.19.0
nvm use 18.19.0
```

### Package Manager Conflicts
**Problem**: Mixed package managers (npm + yarn lockfiles)
**Solution**: Choose one package manager and clean up
```bash
# Clean up mixed package managers
rm -rf node_modules package-lock.json yarn.lock pnpm-lock.yaml
npm install  # or yarn install / pnpm install
```

### Global CLI Version Issues
**Problem**: Incompatible global Angular CLI version
**Solution**: Update or install compatible CLI version
```bash
# Update global Angular CLI
npm uninstall -g @angular/cli
npm install -g @angular/cli@latest
```

### Dependency Vulnerabilities
**Problem**: Security vulnerabilities in dependencies
**Solution**: Audit and fix before migration
```bash
# Audit and fix vulnerabilities
npm audit
npm audit fix
```

## Environment Variables

### Required Environment Variables
- `NODE_ENV`: Development/production environment
- `NG_CLI_ANALYTICS`: Angular CLI analytics setting (optional)

### Optional Configuration
- `NPM_CONFIG_REGISTRY`: Custom npm registry
- `ANGULAR_CLI_CACHE`: CLI cache directory
- `NG_BUILD_CACHE`: Build cache configuration

## Backup and Recovery

### Pre-Migration Backup
```bash
# Create migration branch and backup tag
git checkout -b migration/angular-upgrade
git tag backup/pre-angular-migration
git push origin migration/angular-upgrade
git push origin backup/pre-angular-migration
```

### Recovery Strategy
1. **Git Reset**: Return to backup tag if needed
2. **Incremental Rollback**: Revert specific commits
3. **Branch Switch**: Return to main branch if migration fails

## Validation Commands

### Environment Validation
```bash
# Check Node.js version
node --version

# Check npm version
npm --version

# Check Angular CLI version
ng version

# Verify project builds
ng build --configuration=production

# Run tests
ng test --watch=false
ng e2e
```

### Project Health Check
```bash
# Dependency audit
npm audit

# Bundle analysis
ng build --stats-json
npx webpack-bundle-analyzer dist/stats.json

# Lint check
ng lint

# Format check
npx prettier --check "src/**/*.{ts,html,scss}"
```