# Actuator Updates — Phase 2

## Goal
Align Actuator configuration, exposure, and security with Spring Boot 3 defaults while preserving required operational visibility.

## Prerequisites
- Spring Boot 3.x upgrade completed
- Baseline health/info endpoints accessible
- Security configuration functional

## Preferred Approach (Automated)
1. **Current Configuration Inventory**:
   ```bash
   # Extract actuator configuration
   grep -r "management\." src/main/resources/ > actuator-config-current.txt
   grep -r "actuator" src/main/resources/ >> actuator-config-current.txt
   
   # List currently exposed endpoints
   curl -s http://localhost:8080/actuator | jq '.["_links"]' > current-endpoints.json 2>/dev/null || echo "Actuator not accessible"
   ```

2. **Endpoint Exposure Audit**:
   ```bash
   # Check which endpoints are exposed
   grep -r "management.endpoints.web.exposure" src/main/resources/
   
   # Verify security configuration
   grep -r "actuator" src/main/java/ | grep -i security
   ```

3. **Configuration Updates**:
   ```bash
   # Update deprecated properties (manual review required)
   # Replace management.metrics.export.prometheus.enabled with management.prometheus.metrics.export.enabled
   # Update endpoint exposure configuration for Boot 3
   ```

4. **Security Validation**:
   ```bash
   # Test endpoint accessibility
   curl -s http://localhost:8080/actuator/health
   curl -s http://localhost:8080/actuator/info
   curl -s http://localhost:8080/actuator/metrics
   ```

## Fallback Approach (Manual)
If automated approach fails:
1. Manually review application.yml for deprecated actuator properties
2. Update endpoint exposure configuration step by step
3. Test each endpoint individually after configuration changes
4. Update security rules for actuator paths manually

## Verification Commands
```bash
# Verify actuator endpoints are accessible
curl -s http://localhost:8080/actuator/health | jq '.status' || echo "Health endpoint not accessible"

# Check endpoint exposure configuration
grep -r "management.endpoints.web.exposure" src/main/resources/

# Validate security configuration
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/actuator/env  # Should be 401/403 if secured

# Test metrics endpoint
curl -s http://localhost:8080/actuator/metrics | head -5
```

## Issue Detection & Remediation

### Deprecated Actuator Properties (Severity: medium)
**Detection Pattern**: Deprecated property warnings in application logs
**Remediation**:
1. Replace deprecated `management.metrics.export.prometheus.enabled` with Boot 3 equivalent
2. Update endpoint exposure property names per Boot 3 migration guide
3. Replace removed actuator property aliases
**Validation**: No deprecated property warnings in application startup logs

### Excessive Endpoint Exposure (Severity: high)
**Detection Pattern**: Sensitive endpoints exposed without authentication
**Remediation**:
1. Review `management.endpoints.web.exposure.include` configuration
2. Ensure sensitive endpoints (env, beans, configprops) are not publicly exposed
3. Apply proper security rules for actuator paths
**Validation**: Sensitive endpoints return 401/403 without authentication

### Security Configuration Gaps (Severity: high)
**Detection Pattern**: Actuator endpoints accessible without proper authorization
**Remediation**:
1. Update Spring Security configuration for actuator paths
2. Apply granular access rules: health/info public, others secured
3. Use `requestMatchers("/actuator/**")` with appropriate authorization
**Validation**: Security rules properly protect actuator endpoints

### Metrics Configuration Issues (Severity: medium)
**Detection Pattern**: Metrics endpoint inaccessible or Prometheus scraping fails
**Remediation**:
1. Update Prometheus metrics export configuration for Boot 3
2. Verify micrometer dependencies are Boot 3 compatible
3. Check metrics endpoint exposure and security settings
**Validation**: Metrics endpoint accessible and Prometheus scraping works

### Custom Health Indicator Failures (Severity: medium)
**Detection Pattern**: Custom health indicators not appearing or failing
**Remediation**:
1. Update custom health indicator implementations for Boot 3 API changes
2. Verify health indicator registration and configuration
3. Check for deprecated health indicator interfaces
**Validation**: Custom health indicators appear in /actuator/health response

## Issue Collection
**Only collect issues if remediation fails or is deferred**
- **Directory**: `olaf-data/findings/migrations/migration_<ts>/collected-issues/`
- **File**: `actuator-updates-<YYYYMMDD-HHmm>.json`
- **Categories**: config, security, exposure, metrics, health
- **Status**: OPEN (remediation failed), RESOLVED (remediation successful), DEFERRED (non-critical metric changes)

## Success Criteria
- ✅ No deprecated actuator properties in configuration
- ✅ Health and info endpoints accessible: `/actuator/health` and `/actuator/info` return 200
- ✅ Sensitive endpoints properly secured: `/actuator/env` returns 401/403 without auth
- ✅ Metrics endpoint functional: `/actuator/metrics` accessible
- ✅ No HIGH severity actuator security issues remain OPEN
