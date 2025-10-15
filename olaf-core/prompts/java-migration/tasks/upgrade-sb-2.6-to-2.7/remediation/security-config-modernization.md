---
key: security-config-modernization
triggers:
  - regex: 'WebSecurityConfigurerAdapter'
severity: high
priority: 1
---
## Problem
Legacy WebSecurityConfigurerAdapter requires migration to component-based SecurityFilterChain for Boot 3 readiness.
## Recommended Actions
1. Remove class extends WebSecurityConfigurerAdapter.
2. Define `@Bean SecurityFilterChain http(HttpSecurity http)` and configure DSL.
3. Replace overridden configure(auth) with AuthenticationManager beans / lambdas.
4. Validate key endpoints with new security chain.
## Validation
No references to WebSecurityConfigurerAdapter; tests pass.
## Rollback
Restore old class if blocking issue emerges; retry migration.
