# Otter Framework - Operator Manual

## Table of Contents

1. [Operations Overview](#operations-overview)
2. [Deployment Procedures](#deployment-procedures)
3. [Monitoring & Alerting](#monitoring--alerting)
4. [Incident Response](#incident-response)
5. [Scaling Operations](#scaling-operations)
6. [Security Operations](#security-operations)
7. [Maintenance Windows](#maintenance-windows)
8. [Runbooks](#runbooks)

---

## Operations Overview

### Operational Responsibilities

**DevOps Engineers**:
- Deploy applications to production
- Monitor system health and performance
- Respond to incidents and outages
- Manage infrastructure scaling
- Implement security measures

**SRE Team**:
- Maintain service reliability targets
- Develop monitoring and alerting
- Conduct post-incident reviews
- Optimize system performance
- Automate operational tasks

### Service Level Objectives (SLOs)

| Metric | Target | Measurement Window |
|--------|--------|--------------------|
| Availability | 99.9% | 30 days |
| Response Time (95th percentile) | < 2 seconds | 5 minutes |
| Error Rate | < 0.1% | 5 minutes |
| Recovery Time | < 15 minutes | Per incident |

### Key Performance Indicators (KPIs)

- **Mean Time to Recovery (MTTR)**: < 15 minutes
- **Mean Time Between Failures (MTBF)**: > 720 hours
- **Deployment Frequency**: Multiple per day
- **Change Failure Rate**: < 5%

---

## Deployment Procedures

### Pre-Deployment Checklist

```bash
# Pre-deployment verification
□ All tests passing in CI/CD pipeline
□ Security scan completed without critical issues
□ Performance tests meet baseline requirements
□ Database migrations tested in staging
□ Rollback plan prepared and tested
□ Monitoring dashboards updated
□ On-call team notified
□ Change management ticket approved
```

### Blue-Green Deployment

```bash
#!/bin/bash
# blue-green-deploy.sh

set -e

CURRENT_ENV=$(kubectl get service otter-app -o jsonpath='{.spec.selector.version}')
NEW_ENV=$([ "$CURRENT_ENV" = "blue" ] && echo "green" || echo "blue")

echo "Current environment: $CURRENT_ENV"
echo "Deploying to: $NEW_ENV"

# Deploy to inactive environment
kubectl set image deployment/otter-app-$NEW_ENV \
  otter-app=company/otter-app:$BUILD_NUMBER

# Wait for rollout to complete
kubectl rollout status deployment/otter-app-$NEW_ENV --timeout=300s

# Run health checks
./scripts/health-check.sh $NEW_ENV

# Switch traffic
kubectl patch service otter-app \
  -p '{"spec":{"selector":{"version":"'$NEW_ENV'"}}}'

echo "Traffic switched to $NEW_ENV environment"

# Monitor for 5 minutes
sleep 300

# Verify deployment success
if ./scripts/verify-deployment.sh; then
  echo "Deployment successful"
  # Scale down old environment
  kubectl scale deployment otter-app-$CURRENT_ENV --replicas=0
else
  echo "Deployment failed, rolling back"
  kubectl patch service otter-app \
    -p '{"spec":{"selector":{"version":"'$CURRENT_ENV'"}}}'
  exit 1
fi
```

### Canary Deployment

```yaml
# canary-deployment.yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: otter-app-rollout
spec:
  replicas: 10
  strategy:
    canary:
      steps:
      - setWeight: 10
      - pause: {duration: 2m}
      - setWeight: 25
      - pause: {duration: 5m}
      - setWeight: 50
      - pause: {duration: 10m}
      - setWeight: 75
      - pause: {duration: 10m}
      canaryService: otter-app-canary
      stableService: otter-app-stable
      trafficRouting:
        istio:
          virtualService:
            name: otter-app-vs
  selector:
    matchLabels:
      app: otter-app
  template:
    metadata:
      labels:
        app: otter-app
    spec:
      containers:
      - name: otter-app
        image: company/otter-app:latest
```

### Rollback Procedures

```bash
#!/bin/bash
# rollback.sh

PREVIOUS_VERSION=$(kubectl rollout history deployment/otter-app | tail -n 2 | head -n 1 | awk '{print $1}')

echo "Rolling back to revision: $PREVIOUS_VERSION"

# Perform rollback
kubectl rollout undo deployment/otter-app --to-revision=$PREVIOUS_VERSION

# Wait for rollback to complete
kubectl rollout status deployment/otter-app --timeout=300s

# Verify rollback
./scripts/health-check.sh

echo "Rollback completed successfully"
```

---

## Monitoring & Alerting

### Monitoring Stack

```yaml
# monitoring-stack.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
    - job_name: 'otter-app'
      static_configs:
      - targets: ['otter-app:3000']
      metrics_path: /metrics
      scrape_interval: 10s
    
    - job_name: 'node-exporter'
      static_configs:
      - targets: ['node-exporter:9100']
    
    - job_name: 'postgres-exporter'
      static_configs:
      - targets: ['postgres-exporter:9187']

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      containers:
      - name: prometheus
        image: prom/prometheus:latest
        ports:
        - containerPort: 9090
        volumeMounts:
        - name: config
          mountPath: /etc/prometheus
      volumes:
      - name: config
        configMap:
          name: prometheus-config
```

### Alert Rules

```yaml
# alert-rules.yaml
groups:
- name: otter-app-alerts
  rules:
  - alert: HighErrorRate
    expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.01
    for: 2m
    labels:
      severity: critical
    annotations:
      summary: "High error rate detected"
      description: "Error rate is {{ $value }} requests per second"

  - alert: HighResponseTime
    expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 2
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High response time detected"
      description: "95th percentile response time is {{ $value }} seconds"

  - alert: DatabaseConnectionFailure
    expr: up{job="postgres-exporter"} == 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "Database connection failure"
      description: "Cannot connect to PostgreSQL database"

  - alert: HighCPUUsage
    expr: rate(container_cpu_usage_seconds_total[5m]) * 100 > 80
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "High CPU usage"
      description: "CPU usage is {{ $value }}%"

  - alert: HighMemoryUsage
    expr: (container_memory_usage_bytes / container_spec_memory_limit_bytes) * 100 > 90
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "High memory usage"
      description: "Memory usage is {{ $value }}%"
```

### Grafana Dashboards

```json
{
  "dashboard": {
    "title": "Otter Application Dashboard",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "{{method}} {{route}}"
          }
        ]
      },
      {
        "title": "Response Time",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "95th percentile"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "singlestat",
        "targets": [
          {
            "expr": "rate(http_requests_total{status=~\"5..\"}[5m])",
            "legendFormat": "Error Rate"
          }
        ]
      }
    ]
  }
}
```

---

## Incident Response

### Incident Classification

| Severity | Definition | Response Time | Examples |
|----------|------------|---------------|----------|
| P1 - Critical | Service completely down | 15 minutes | Total outage, data loss |
| P2 - High | Major functionality impaired | 1 hour | Login failures, payment issues |
| P3 - Medium | Minor functionality impaired | 4 hours | UI glitches, slow performance |
| P4 - Low | Cosmetic issues | 24 hours | Documentation errors, minor bugs |

### Incident Response Process

#### 1. Detection & Alerting

```bash
# Automated alert triggers
- Monitoring system detects anomaly
- Alert sent to on-call engineer
- Incident automatically created in PagerDuty
- War room channel created in Slack
```

#### 2. Initial Response

```bash
# First 5 minutes
□ Acknowledge alert in PagerDuty
□ Join war room channel
□ Assess severity and impact
□ Escalate if necessary
□ Begin investigation
```

#### 3. Investigation & Mitigation

```bash
# Investigation checklist
□ Check application logs: kubectl logs -f deployment/otter-app
□ Check system metrics: Grafana dashboards
□ Check database status: pg_stat_activity
□ Check external dependencies: API health checks
□ Check recent deployments: kubectl rollout history
```

#### 4. Communication

```bash
# Communication template
Subject: [P1] Otter Application Outage - Investigating

We are currently investigating reports of users unable to access the Otter application.

Impact: All users affected
Start Time: 2024-01-15 14:30 UTC
Status: Investigating

We will provide updates every 15 minutes until resolved.

Next Update: 14:45 UTC
```

### Runbook Examples

#### High Memory Usage

```bash
#!/bin/bash
# runbook-high-memory.sh

echo "=== High Memory Usage Runbook ==="

# 1. Check current memory usage
kubectl top pods -l app=otter-app

# 2. Check for memory leaks in logs
kubectl logs -l app=otter-app | grep -i "memory\|heap\|gc"

# 3. Get detailed memory metrics
kubectl exec -it $(kubectl get pod -l app=otter-app -o jsonpath='{.items[0].metadata.name}') -- \
  node -e "console.log(process.memoryUsage())"

# 4. Check if restart resolves issue
kubectl rollout restart deployment/otter-app

# 5. Monitor for 10 minutes
sleep 600
kubectl top pods -l app=otter-app

echo "Memory usage check completed"
```

#### Database Connection Issues

```bash
#!/bin/bash
# runbook-db-connection.sh

echo "=== Database Connection Issues Runbook ==="

# 1. Test database connectivity
kubectl exec -it $(kubectl get pod -l app=otter-app -o jsonpath='{.items[0].metadata.name}') -- \
  psql $DATABASE_URL -c "SELECT 1;"

# 2. Check database status
kubectl exec -it postgres-0 -- pg_isready

# 3. Check connection pool status
kubectl exec -it $(kubectl get pod -l app=otter-app -o jsonpath='{.items[0].metadata.name}') -- \
  curl -s http://localhost:3000/health/db

# 4. Check for long-running queries
kubectl exec -it postgres-0 -- \
  psql -c "SELECT pid, now() - pg_stat_activity.query_start AS duration, query 
           FROM pg_stat_activity 
           WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';"

# 5. Restart application if needed
kubectl rollout restart deployment/otter-app

echo "Database connection check completed"
```

---

## Scaling Operations

### Horizontal Pod Autoscaling

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: otter-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: otter-app
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
```

### Manual Scaling

```bash
# Scale up for high traffic
kubectl scale deployment otter-app --replicas=10

# Scale down during low traffic
kubectl scale deployment otter-app --replicas=3

# Check scaling status
kubectl get hpa otter-app-hpa
```

### Database Scaling

```bash
# Read replica setup
kubectl apply -f postgres-read-replica.yaml

# Connection pooling configuration
kubectl apply -f pgbouncer-config.yaml

# Monitor database performance
kubectl exec -it postgres-0 -- \
  psql -c "SELECT * FROM pg_stat_database WHERE datname='otter_production';"
```

---

## Security Operations

### Security Monitoring

```bash
# Check for security vulnerabilities
kubectl exec -it $(kubectl get pod -l app=otter-app -o jsonpath='{.items[0].metadata.name}') -- \
  npm audit --audit-level=high

# Monitor failed authentication attempts
kubectl logs -l app=otter-app | grep "authentication failed" | tail -20

# Check SSL certificate expiration
openssl s_client -connect app.company.com:443 -servername app.company.com 2>/dev/null | \
  openssl x509 -noout -dates
```

### Security Incident Response

```bash
#!/bin/bash
# security-incident-response.sh

echo "=== Security Incident Response ==="

# 1. Isolate affected systems
kubectl scale deployment otter-app --replicas=0

# 2. Preserve evidence
kubectl logs -l app=otter-app > /tmp/incident-logs-$(date +%Y%m%d-%H%M%S).log

# 3. Block suspicious IPs
kubectl apply -f network-policy-lockdown.yaml

# 4. Rotate secrets
kubectl delete secret otter-app-secrets
kubectl create secret generic otter-app-secrets --from-env-file=.env.new

# 5. Deploy patched version
kubectl set image deployment/otter-app otter-app=company/otter-app:security-patch

echo "Security incident response completed"
```

---

## Maintenance Windows

### Planned Maintenance

```bash
#!/bin/bash
# planned-maintenance.sh

echo "Starting planned maintenance window"

# 1. Enable maintenance mode
kubectl apply -f maintenance-mode.yaml

# 2. Drain traffic gracefully
kubectl patch service otter-app -p '{"spec":{"selector":{"maintenance":"true"}}}'

# 3. Wait for connections to drain
sleep 60

# 4. Perform maintenance tasks
./scripts/database-maintenance.sh
./scripts/update-certificates.sh
./scripts/cleanup-old-data.sh

# 5. Deploy updates
kubectl apply -f updated-deployment.yaml

# 6. Verify health
./scripts/health-check.sh

# 7. Disable maintenance mode
kubectl delete -f maintenance-mode.yaml

echo "Planned maintenance completed"
```

### Emergency Maintenance

```bash
#!/bin/bash
# emergency-maintenance.sh

echo "Starting emergency maintenance"

# Immediate actions for critical issues
kubectl scale deployment otter-app --replicas=0
kubectl apply -f emergency-fix.yaml
kubectl scale deployment otter-app --replicas=5

# Verify fix
./scripts/verify-emergency-fix.sh

echo "Emergency maintenance completed"
```

---

## Runbooks

### Daily Operations Checklist

```bash
# Daily operations checklist
□ Check overnight alerts and incidents
□ Review application performance metrics
□ Verify backup completion
□ Check certificate expiration dates
□ Review capacity utilization
□ Update operational dashboards
□ Check security scan results
```

### Weekly Operations Checklist

```bash
# Weekly operations checklist
□ Review and update monitoring thresholds
□ Analyze performance trends
□ Update documentation
□ Review and test disaster recovery procedures
□ Security patch assessment
□ Capacity planning review
□ Team knowledge sharing session
```

### Monthly Operations Checklist

```bash
# Monthly operations checklist
□ Conduct disaster recovery drill
□ Review and update runbooks
□ Security audit and penetration testing
□ Performance optimization review
□ Cost optimization analysis
□ Update operational procedures
□ Team retrospective and improvement planning
```

This operator manual provides comprehensive guidance for managing Otter Framework applications in production environments, ensuring reliable operations and quick incident resolution.
