# Otter Framework - API Documentation

## Table of Contents

1. [API Overview](#api-overview)
2. [Authentication](#authentication)
3. [Configuration API](#configuration-api)
4. [Localization API](#localization-api)
5. [Analytics API](#analytics-api)
6. [Rules Engine API](#rules-engine-api)
7. [Component API](#component-api)
8. [Health & Monitoring API](#health--monitoring-api)
9. [Error Handling](#error-handling)
10. [SDK Usage](#sdk-usage)

---

## API Overview

### Base URL
```
Production: https://api.otter-framework.com/v1
Staging: https://staging-api.otter-framework.com/v1
Development: http://localhost:3000/api/v1
```

### Content Type
All API endpoints accept and return JSON unless otherwise specified.

```http
Content-Type: application/json
Accept: application/json
```

### Rate Limiting
- **Authenticated requests**: 1000 requests per hour
- **Unauthenticated requests**: 100 requests per hour

Rate limit headers are included in all responses:
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

### API Versioning
The API uses URL versioning. Current version is `v1`.

---

## Authentication

### JWT Authentication

Most endpoints require authentication using JWT tokens.

#### Login
```http
POST /auth/login
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresIn": 3600,
    "user": {
      "id": "123",
      "email": "user@example.com",
      "name": "John Doe",
      "roles": ["user"]
    }
  }
}
```

#### Refresh Token
```http
POST /auth/refresh
```

**Request Body:**
```json
{
  "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### Using JWT Token
Include the JWT token in the Authorization header:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### API Key Authentication

For server-to-server communication, use API keys:

```http
X-API-Key: your-api-key-here
```

---

## Configuration API

### Get Configuration

Retrieve configuration for components or applications.

```http
GET /config/{scope}
```

**Parameters:**
- `scope` (path): Configuration scope (e.g., "global", "MyComponent")
- `environment` (query): Environment name (optional)
- `version` (query): Configuration version (optional)

**Example:**
```http
GET /config/MyComponent?environment=production&version=1.2.0
```

**Response:**
```json
{
  "success": true,
  "data": {
    "scope": "MyComponent",
    "environment": "production",
    "version": "1.2.0",
    "config": {
      "title": "Welcome to Otter",
      "showDescription": true,
      "maxItems": 10,
      "theme": "dark"
    },
    "metadata": {
      "lastModified": "2024-01-15T10:30:00Z",
      "modifiedBy": "admin@example.com"
    }
  }
}
```

### Update Configuration

```http
PUT /config/{scope}
```

**Request Body:**
```json
{
  "config": {
    "title": "Updated Title",
    "showDescription": false,
    "maxItems": 20
  },
  "environment": "production",
  "version": "1.2.1"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "scope": "MyComponent",
    "version": "1.2.1",
    "config": {
      "title": "Updated Title",
      "showDescription": false,
      "maxItems": 20,
      "theme": "dark"
    }
  }
}
```

### Configuration Schema

Get the schema for a configuration scope.

```http
GET /config/{scope}/schema
```

**Response:**
```json
{
  "success": true,
  "data": {
    "scope": "MyComponent",
    "schema": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "Component title"
        },
        "showDescription": {
          "type": "boolean",
          "description": "Whether to show description"
        },
        "maxItems": {
          "type": "number",
          "minimum": 1,
          "maximum": 100,
          "description": "Maximum number of items"
        }
      },
      "required": ["title"]
    }
  }
}
```

---

## Localization API

### Get Translations

Retrieve translations for a specific locale.

```http
GET /localization/{locale}
```

**Parameters:**
- `locale` (path): Locale code (e.g., "en", "fr", "es")
- `namespace` (query): Translation namespace (optional)

**Example:**
```http
GET /localization/fr?namespace=common
```

**Response:**
```json
{
  "success": true,
  "data": {
    "locale": "fr",
    "namespace": "common",
    "translations": {
      "welcome": "Bienvenue",
      "login": "Se connecter",
      "logout": "Se déconnecter",
      "save": "Enregistrer",
      "cancel": "Annuler"
    },
    "metadata": {
      "version": "1.0.0",
      "lastUpdated": "2024-01-15T10:30:00Z"
    }
  }
}
```

### Update Translations

```http
PUT /localization/{locale}
```

**Request Body:**
```json
{
  "namespace": "common",
  "translations": {
    "welcome": "Bienvenue à Otter",
    "new_key": "Nouvelle traduction"
  }
}
```

### Get Available Locales

```http
GET /localization/locales
```

**Response:**
```json
{
  "success": true,
  "data": {
    "locales": [
      {
        "code": "en",
        "name": "English",
        "nativeName": "English",
        "isDefault": true
      },
      {
        "code": "fr",
        "name": "French",
        "nativeName": "Français",
        "isDefault": false
      },
      {
        "code": "es",
        "name": "Spanish",
        "nativeName": "Español",
        "isDefault": false
      }
    ]
  }
}
```

---

## Analytics API

### Track Event

Send analytics events to the system.

```http
POST /analytics/events
```

**Request Body:**
```json
{
  "event": "button_click",
  "properties": {
    "component": "ProductCard",
    "action": "add_to_cart",
    "productId": "12345",
    "userId": "user123"
  },
  "timestamp": "2024-01-15T10:30:00Z",
  "sessionId": "session123"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "eventId": "evt_123456789",
    "processed": true
  }
}
```

### Batch Track Events

Send multiple events in a single request.

```http
POST /analytics/events/batch
```

**Request Body:**
```json
{
  "events": [
    {
      "event": "page_view",
      "properties": {
        "page": "/products",
        "userId": "user123"
      },
      "timestamp": "2024-01-15T10:30:00Z"
    },
    {
      "event": "button_click",
      "properties": {
        "component": "Navigation",
        "action": "menu_open"
      },
      "timestamp": "2024-01-15T10:30:05Z"
    }
  ]
}
```

### Get Analytics Data

Retrieve analytics data with filters.

```http
GET /analytics/data
```

**Query Parameters:**
- `startDate` (query): Start date (ISO 8601)
- `endDate` (query): End date (ISO 8601)
- `event` (query): Event name filter
- `userId` (query): User ID filter
- `limit` (query): Number of results (default: 100, max: 1000)
- `offset` (query): Pagination offset

**Example:**
```http
GET /analytics/data?startDate=2024-01-01T00:00:00Z&endDate=2024-01-31T23:59:59Z&event=button_click&limit=50
```

**Response:**
```json
{
  "success": true,
  "data": {
    "events": [
      {
        "id": "evt_123456789",
        "event": "button_click",
        "properties": {
          "component": "ProductCard",
          "action": "add_to_cart"
        },
        "timestamp": "2024-01-15T10:30:00Z",
        "userId": "user123"
      }
    ],
    "pagination": {
      "total": 1250,
      "limit": 50,
      "offset": 0,
      "hasMore": true
    }
  }
}
```

---

## Rules Engine API

### Get Rules

Retrieve rules for a specific context.

```http
GET /rules
```

**Query Parameters:**
- `context` (query): Rule context (optional)
- `active` (query): Filter by active status (true/false)

**Response:**
```json
{
  "success": true,
  "data": {
    "rules": [
      {
        "id": "rule_123",
        "name": "Show Premium Features",
        "context": "user_interface",
        "condition": "user.isPremium === true",
        "action": "SET_CONFIG",
        "target": "MyComponent.showPremiumFeatures",
        "value": true,
        "active": true,
        "priority": 100,
        "createdAt": "2024-01-15T10:30:00Z"
      }
    ]
  }
}
```

### Create Rule

```http
POST /rules
```

**Request Body:**
```json
{
  "name": "Holiday Promotion",
  "context": "promotions",
  "condition": "date >= '2024-12-01' && date <= '2024-12-31'",
  "action": "SET_CONFIG",
  "target": "PromoComponent.showHolidayPromo",
  "value": true,
  "priority": 200
}
```

### Update Rule

```http
PUT /rules/{ruleId}
```

### Delete Rule

```http
DELETE /rules/{ruleId}
```

### Evaluate Rules

Test rule evaluation with context data.

```http
POST /rules/evaluate
```

**Request Body:**
```json
{
  "context": {
    "user": {
      "isPremium": true,
      "country": "US"
    },
    "date": "2024-01-15",
    "feature": "dashboard"
  },
  "rules": ["rule_123", "rule_456"]
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "results": [
      {
        "ruleId": "rule_123",
        "matched": true,
        "action": "SET_CONFIG",
        "target": "MyComponent.showPremiumFeatures",
        "value": true
      }
    ]
  }
}
```

---

## Component API

### Get Component Metadata

Retrieve metadata for Otter components.

```http
GET /components/{componentName}/metadata
```

**Response:**
```json
{
  "success": true,
  "data": {
    "name": "ProductCard",
    "version": "1.2.0",
    "description": "A reusable product card component",
    "configSchema": {
      "type": "object",
      "properties": {
        "showRating": {"type": "boolean"},
        "maxDescriptionLength": {"type": "number"}
      }
    },
    "localizationKeys": [
      "product-card.add-to-cart",
      "product-card.out-of-stock"
    ],
    "dependencies": ["@o3r/core", "@o3r/configuration"],
    "tags": ["e-commerce", "product", "ui"]
  }
}
```

### List Components

```http
GET /components
```

**Query Parameters:**
- `tag` (query): Filter by tag
- `search` (query): Search in name/description
- `limit` (query): Number of results

**Response:**
```json
{
  "success": true,
  "data": {
    "components": [
      {
        "name": "ProductCard",
        "version": "1.2.0",
        "description": "A reusable product card component",
        "tags": ["e-commerce", "product"]
      },
      {
        "name": "UserProfile",
        "version": "2.0.1",
        "description": "User profile management component",
        "tags": ["user", "profile"]
      }
    ],
    "total": 25
  }
}
```

---

## Health & Monitoring API

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "success": true,
  "data": {
    "status": "healthy",
    "timestamp": "2024-01-15T10:30:00Z",
    "uptime": 86400,
    "version": "1.2.0",
    "environment": "production"
  }
}
```

### Readiness Check

```http
GET /health/ready
```

**Response:**
```json
{
  "success": true,
  "data": {
    "status": "ready",
    "checks": {
      "database": "healthy",
      "redis": "healthy",
      "external_api": "healthy"
    }
  }
}
```

### Metrics

```http
GET /metrics
```

Returns Prometheus-formatted metrics:

```
# HELP http_requests_total Total number of HTTP requests
# TYPE http_requests_total counter
http_requests_total{method="GET",route="/config",status="200"} 1234

# HELP http_request_duration_seconds Duration of HTTP requests
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{method="GET",route="/config",le="0.1"} 100
```

---

## Error Handling

### Error Response Format

All errors follow a consistent format:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request parameters",
    "details": {
      "field": "email",
      "reason": "Invalid email format"
    },
    "timestamp": "2024-01-15T10:30:00Z",
    "requestId": "req_123456789"
  }
}
```

### HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Unprocessable Entity |
| 429 | Too Many Requests |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |

### Common Error Codes

| Error Code | Description |
|------------|-------------|
| `VALIDATION_ERROR` | Request validation failed |
| `AUTHENTICATION_FAILED` | Invalid credentials |
| `AUTHORIZATION_FAILED` | Insufficient permissions |
| `RESOURCE_NOT_FOUND` | Requested resource not found |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `INTERNAL_ERROR` | Server error |

---

## SDK Usage

### JavaScript/TypeScript SDK

#### Installation

```bash
npm install @o3r/sdk
```

#### Basic Usage

```typescript
import { OtterSDK } from '@o3r/sdk';

const sdk = new OtterSDK({
  baseUrl: 'https://api.otter-framework.com/v1',
  apiKey: 'your-api-key'
});

// Get configuration
const config = await sdk.configuration.get('MyComponent');

// Track analytics event
await sdk.analytics.track('button_click', {
  component: 'ProductCard',
  action: 'add_to_cart'
});

// Get translations
const translations = await sdk.localization.get('en');
```

#### Configuration Service

```typescript
// Subscribe to configuration changes
sdk.configuration.subscribe('MyComponent', (config) => {
  console.log('Configuration updated:', config);
});

// Update configuration
await sdk.configuration.update('MyComponent', {
  title: 'New Title',
  showDescription: true
});
```

#### Analytics Service

```typescript
// Track single event
await sdk.analytics.track('page_view', {
  page: '/products',
  userId: 'user123'
});

// Track multiple events
await sdk.analytics.trackBatch([
  { event: 'page_view', properties: { page: '/home' } },
  { event: 'button_click', properties: { button: 'cta' } }
]);
```

### React Integration

```typescript
import { useOtterConfig, useOtterTranslation } from '@o3r/react';

function MyComponent() {
  const config = useOtterConfig('MyComponent', defaultConfig);
  const t = useOtterTranslation();

  return (
    <div>
      <h1>{config.title}</h1>
      <p>{t('welcome.message')}</p>
    </div>
  );
}
```

### Angular Integration

```typescript
import { ConfigurationService, LocalizationService } from '@o3r/angular';

@Component({
  selector: 'app-my-component',
  template: `
    <h1>{{ (config$ | async)?.title }}</h1>
    <p>{{ 'welcome.message' | o3rTranslate }}</p>
  `
})
export class MyComponent {
  config$ = this.configService.getComponentConfig('MyComponent', defaultConfig);

  constructor(
    private configService: ConfigurationService,
    private localizationService: LocalizationService
  ) {}
}
```

This API documentation provides comprehensive coverage of all Otter Framework APIs, enabling developers to integrate and extend the framework effectively.
