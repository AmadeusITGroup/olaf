# Otter Framework - Administrator Manual

## Table of Contents

1. [System Administration](#system-administration)
2. [Configuration Management](#configuration-management)
3. [Environment Setup](#environment-setup)
4. [Security Configuration](#security-configuration)
5. [Performance Tuning](#performance-tuning)
6. [Monitoring & Logging](#monitoring--logging)
7. [Backup & Recovery](#backup--recovery)
8. [Troubleshooting](#troubleshooting)
9. [Maintenance Procedures](#maintenance-procedures)

---

## System Administration

### Server Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 2 cores | 4+ cores |
| RAM | 4GB | 8GB+ |
| Storage | 20GB | 50GB+ SSD |
| Network | 100Mbps | 1Gbps |

### Supported Platforms

- **Linux**: Ubuntu 20.04+, CentOS 8+, RHEL 8+
- **Windows**: Windows Server 2019+
- **macOS**: macOS 11+ (development only)
- **Containers**: Docker, Kubernetes

### Installation

#### Production Installation

```bash
# Create dedicated user
sudo useradd -m -s /bin/bash otter-admin
sudo usermod -aG sudo otter-admin

# Install Node.js (using NodeSource repository)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Yarn
npm install -g yarn

# Install PM2 for process management
npm install -g pm2

# Create application directory
sudo mkdir -p /opt/otter
sudo chown otter-admin:otter-admin /opt/otter
```

#### Docker Installation

```dockerfile
# Dockerfile.production
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --production=false
COPY . .
RUN yarn build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## Configuration Management

### Environment Configuration

#### Production Environment Variables

```bash
# /opt/otter/.env.production
NODE_ENV=production
PORT=3000
API_URL=https://api.production.com
DATABASE_URL=postgresql://user:pass@db:5432/otter_prod
REDIS_URL=redis://redis:6379
LOG_LEVEL=info
ENABLE_ANALYTICS=true
SENTRY_DSN=https://your-sentry-dsn
```

#### Configuration Validation

```bash
# Validate configuration before deployment
yarn config:validate

# Check environment variables
yarn config:check-env

# Test database connectivity
yarn config:test-db
```

### Application Configuration

#### Global Configuration

```json
{
  "application": {
    "name": "Otter Production",
    "version": "1.0.0",
    "environment": "production"
  },
  "security": {
    "cors": {
      "origins": ["https://app.company.com"],
      "credentials": true
    },
    "csp": {
      "defaultSrc": "'self'",
      "scriptSrc": "'self' 'unsafe-inline'",
      "styleSrc": "'self' 'unsafe-inline'"
    }
  },
  "performance": {
    "caching": {
      "enabled": true,
      "ttl": 3600,
      "maxSize": "100MB"
    },
    "compression": {
      "enabled": true,
      "level": 6
    }
  }
}
```

#### Feature Flags

```json
{
  "features": {
    "newDashboard": {
      "enabled": true,
      "rollout": 100,
      "environments": ["production"]
    },
    "experimentalFeature": {
      "enabled": false,
      "rollout": 0,
      "environments": ["development"]
    }
  }
}
```

---

## Environment Setup

### Development Environment

```bash
# Setup development environment
git clone https://github.com/company/otter-app.git
cd otter-app

# Install dependencies
yarn install

# Setup local database
docker-compose up -d postgres redis

# Run migrations
yarn db:migrate

# Start development server
yarn start:dev
```

### Staging Environment

```bash
# Deploy to staging
./scripts/deploy-staging.sh

# Run health checks
curl -f http://staging.company.com/health || exit 1

# Run smoke tests
yarn test:smoke --env=staging
```

### Production Deployment

```bash
# Production deployment script
#!/bin/bash
set -e

echo "Starting production deployment..."

# Backup current version
./scripts/backup-current.sh

# Deploy new version
docker pull company/otter-app:latest
docker-compose -f docker-compose.prod.yml up -d

# Wait for health check
./scripts/wait-for-health.sh

# Run post-deployment tests
yarn test:production

echo "Deployment completed successfully"
```

---

## Security Configuration

### SSL/TLS Setup

#### Nginx Configuration

```nginx
server {
    listen 443 ssl http2;
    server_name app.company.com;

    ssl_certificate /etc/ssl/certs/app.company.com.crt;
    ssl_certificate_key /etc/ssl/private/app.company.com.key;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    
    add_header Strict-Transport-Security "max-age=63072000" always;
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Authentication & Authorization

#### JWT Configuration

```json
{
  "jwt": {
    "secret": "your-super-secret-key",
    "expiresIn": "24h",
    "issuer": "otter-app",
    "audience": "otter-users"
  },
  "oauth": {
    "providers": {
      "google": {
        "clientId": "your-google-client-id",
        "clientSecret": "your-google-client-secret"
      },
      "github": {
        "clientId": "your-github-client-id",
        "clientSecret": "your-github-client-secret"
      }
    }
  }
}
```

### Security Headers

```typescript
// security.middleware.ts
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", "data:", "https:"],
      connectSrc: ["'self'", "https://api.company.com"]
    }
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));
```

---

## Performance Tuning

### Application Performance

#### Caching Strategy

```typescript
// cache.config.ts
export const cacheConfig = {
  redis: {
    host: process.env.REDIS_HOST,
    port: parseInt(process.env.REDIS_PORT),
    ttl: 3600, // 1 hour
    maxMemoryPolicy: 'allkeys-lru'
  },
  application: {
    staticAssets: '1y',
    apiResponses: '5m',
    userSessions: '24h'
  }
};
```

#### Database Optimization

```sql
-- Create indexes for frequently queried columns
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
CREATE INDEX CONCURRENTLY idx_products_category ON products(category_id);
CREATE INDEX CONCURRENTLY idx_orders_created_at ON orders(created_at);

-- Analyze query performance
EXPLAIN ANALYZE SELECT * FROM products WHERE category_id = 1;
```

### Infrastructure Scaling

#### Horizontal Scaling

```yaml
# kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otter-app
spec:
  replicas: 3
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
        ports:
        - containerPort: 3000
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
```

#### Load Balancer Configuration

```yaml
# kubernetes/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: otter-app-service
spec:
  selector:
    app: otter-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: LoadBalancer
```

---

## Monitoring & Logging

### Application Monitoring

#### Health Check Endpoints

```typescript
// health.controller.ts
@Controller('health')
export class HealthController {
  @Get()
  async check() {
    return {
      status: 'ok',
      timestamp: new Date().toISOString(),
      uptime: process.uptime(),
      memory: process.memoryUsage(),
      version: process.env.APP_VERSION
    };
  }

  @Get('ready')
  async readiness() {
    // Check database connectivity
    const dbStatus = await this.checkDatabase();
    // Check Redis connectivity
    const redisStatus = await this.checkRedis();
    
    return {
      status: dbStatus && redisStatus ? 'ready' : 'not ready',
      checks: { database: dbStatus, redis: redisStatus }
    };
  }
}
```

#### Metrics Collection

```typescript
// metrics.service.ts
import { register, Counter, Histogram } from 'prom-client';

export class MetricsService {
  private httpRequestsTotal = new Counter({
    name: 'http_requests_total',
    help: 'Total number of HTTP requests',
    labelNames: ['method', 'route', 'status_code']
  });

  private httpRequestDuration = new Histogram({
    name: 'http_request_duration_seconds',
    help: 'Duration of HTTP requests in seconds',
    labelNames: ['method', 'route']
  });

  recordRequest(method: string, route: string, statusCode: number, duration: number) {
    this.httpRequestsTotal.inc({ method, route, status_code: statusCode });
    this.httpRequestDuration.observe({ method, route }, duration);
  }
}
```

### Logging Configuration

#### Structured Logging

```typescript
// logger.config.ts
import { createLogger, format, transports } from 'winston';

export const logger = createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: format.combine(
    format.timestamp(),
    format.errors({ stack: true }),
    format.json()
  ),
  defaultMeta: {
    service: 'otter-app',
    version: process.env.APP_VERSION
  },
  transports: [
    new transports.File({ filename: 'logs/error.log', level: 'error' }),
    new transports.File({ filename: 'logs/combined.log' }),
    new transports.Console({
      format: format.combine(
        format.colorize(),
        format.simple()
      )
    })
  ]
});
```

#### Log Aggregation

```yaml
# docker-compose.logging.yml
version: '3.8'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"

  kibana:
    image: docker.elastic.co/kibana/kibana:8.5.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch

  logstash:
    image: docker.elastic.co/logstash/logstash:8.5.0
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    depends_on:
      - elasticsearch
```

---

## Backup & Recovery

### Database Backup

#### Automated Backup Script

```bash
#!/bin/bash
# backup-database.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/opt/backups/database"
DB_NAME="otter_production"

# Create backup directory
mkdir -p $BACKUP_DIR

# Create database dump
pg_dump -h localhost -U postgres $DB_NAME | gzip > $BACKUP_DIR/backup_$DATE.sql.gz

# Keep only last 30 days of backups
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +30 -delete

# Upload to S3 (optional)
aws s3 cp $BACKUP_DIR/backup_$DATE.sql.gz s3://company-backups/database/
```

#### Backup Verification

```bash
#!/bin/bash
# verify-backup.sh

LATEST_BACKUP=$(ls -t /opt/backups/database/backup_*.sql.gz | head -n1)

# Test restore to temporary database
createdb otter_test_restore
gunzip -c $LATEST_BACKUP | psql otter_test_restore

# Verify data integrity
psql otter_test_restore -c "SELECT COUNT(*) FROM users;"
psql otter_test_restore -c "SELECT COUNT(*) FROM products;"

# Cleanup
dropdb otter_test_restore
```

### Application Backup

#### Configuration Backup

```bash
#!/bin/bash
# backup-config.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/opt/backups/config"

mkdir -p $BACKUP_DIR

# Backup configuration files
tar -czf $BACKUP_DIR/config_$DATE.tar.gz \
  /opt/otter/.env.production \
  /opt/otter/config/ \
  /etc/nginx/sites-available/otter \
  /etc/ssl/certs/app.company.com.crt

# Backup application code
tar -czf $BACKUP_DIR/app_$DATE.tar.gz \
  --exclude=node_modules \
  --exclude=dist \
  /opt/otter/
```

### Disaster Recovery

#### Recovery Procedures

1. **Database Recovery**:
```bash
# Stop application
sudo systemctl stop otter-app

# Restore database
dropdb otter_production
createdb otter_production
gunzip -c /opt/backups/database/backup_latest.sql.gz | psql otter_production

# Start application
sudo systemctl start otter-app
```

2. **Full System Recovery**:
```bash
# Restore from backup server
rsync -avz backup-server:/backups/otter/ /opt/otter/

# Restore configuration
tar -xzf /opt/backups/config/config_latest.tar.gz -C /

# Restart services
sudo systemctl restart nginx
sudo systemctl restart otter-app
```

---

## Troubleshooting

### Common Issues

#### Application Won't Start

**Symptoms**: Service fails to start, error in logs
```bash
# Check service status
sudo systemctl status otter-app

# Check logs
sudo journalctl -u otter-app -f

# Check application logs
tail -f /opt/otter/logs/error.log
```

**Solutions**:
1. Check environment variables
2. Verify database connectivity
3. Check file permissions
4. Validate configuration files

#### High Memory Usage

**Symptoms**: Application consuming excessive memory
```bash
# Check memory usage
ps aux | grep node
free -h
```

**Solutions**:
1. Restart application: `sudo systemctl restart otter-app`
2. Check for memory leaks in logs
3. Adjust Node.js memory limits: `--max-old-space-size=4096`
4. Scale horizontally if needed

#### Database Connection Issues

**Symptoms**: Database connection errors in logs
```bash
# Test database connectivity
psql -h localhost -U postgres -d otter_production -c "SELECT 1;"

# Check database status
sudo systemctl status postgresql
```

**Solutions**:
1. Verify database credentials
2. Check network connectivity
3. Restart database service
4. Check connection pool settings

### Performance Issues

#### Slow Response Times

**Diagnosis**:
```bash
# Check application metrics
curl http://localhost:3000/metrics

# Monitor database queries
tail -f /var/log/postgresql/postgresql.log

# Check system resources
htop
iotop
```

**Solutions**:
1. Enable query optimization
2. Add database indexes
3. Implement caching
4. Scale resources

#### High CPU Usage

**Diagnosis**:
```bash
# Profile application
node --prof app.js
node --prof-process isolate-*.log > profile.txt
```

**Solutions**:
1. Optimize expensive operations
2. Implement worker threads
3. Add load balancing
4. Scale vertically

---

## Maintenance Procedures

### Regular Maintenance

#### Daily Tasks
- Monitor application health
- Check error logs
- Verify backup completion
- Review performance metrics

#### Weekly Tasks
- Update security patches
- Clean up old log files
- Optimize database
- Review capacity planning

#### Monthly Tasks
- Security audit
- Performance review
- Backup testing
- Documentation updates

### Update Procedures

#### Application Updates

```bash
#!/bin/bash
# update-application.sh

# Backup current version
./scripts/backup-current.sh

# Pull latest code
git fetch origin
git checkout main
git pull origin main

# Install dependencies
yarn install --frozen-lockfile

# Run tests
yarn test

# Build application
yarn build

# Deploy
./scripts/deploy.sh

# Verify deployment
./scripts/health-check.sh
```

#### Security Updates

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Update Node.js dependencies
yarn audit
yarn audit fix

# Update Docker images
docker-compose pull
docker-compose up -d
```

### Capacity Planning

#### Monitoring Metrics

- **CPU Usage**: Target < 70% average
- **Memory Usage**: Target < 80% of available
- **Disk Usage**: Target < 85% of capacity
- **Network I/O**: Monitor for bottlenecks
- **Database Connections**: Monitor pool usage

#### Scaling Triggers

- CPU usage > 80% for 5+ minutes
- Memory usage > 90% for 2+ minutes
- Response time > 2 seconds for 95th percentile
- Error rate > 1% for 5+ minutes

#### Scaling Actions

1. **Vertical Scaling**: Increase CPU/memory
2. **Horizontal Scaling**: Add more instances
3. **Database Scaling**: Read replicas, sharding
4. **Caching**: Implement/expand caching layers

This manual provides the essential information for administering Otter Framework applications in production environments. Regular review and updates ensure optimal performance and security.
