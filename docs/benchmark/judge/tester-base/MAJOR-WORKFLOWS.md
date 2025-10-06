# Otter Framework - Major Workflows Documentation

## Overview

This document identifies and details the top 5 most common workflows in the Otter Framework, covering the major use cases that users encounter when developing Angular applications with Otter.

---

## Workflow 1: Project Setup and Initial Configuration

### Description
Setting up a new Otter project from scratch, including workspace creation, dependency installation, and basic configuration.

### User Journey
**Primary Actor**: Frontend Developer  
**Frequency**: Once per project  
**Complexity**: Medium  

### Step-by-Step Process

#### 1. Project Creation
```bash
# User initiates project creation
npm create @o3r my-otter-project
cd my-otter-project
```

**Expected Outcome**: New Nx workspace with Otter framework installed

#### 2. Dependency Installation
```bash
# System installs dependencies automatically
yarn install
```

**Expected Outcome**: All required packages installed successfully

#### 3. Initial Build Verification
```bash
# User verifies setup
yarn build
yarn test
```

**Expected Outcome**: 
- Build completes without errors
- All initial tests pass
- Dist folder created with compiled assets

#### 4. Development Server Launch
```bash
# User starts development environment
yarn start
```

**Expected Outcome**: 
- Development server starts on http://localhost:4200
- Application loads in browser
- Hot module replacement working

#### 5. Basic Configuration Setup
```typescript
// User configures environment settings
// apps/my-app/src/environments/environment.ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:3000',
  enableAnalytics: false
};
```

**Expected Outcome**: Environment configuration ready for development

### Success Criteria
- [ ] Project created successfully
- [ ] All dependencies installed
- [ ] Build process works
- [ ] Development server accessible
- [ ] Basic configuration in place

### Common Issues & Resolutions
- **Node version incompatibility**: Upgrade to Node.js 20+
- **Yarn not found**: Install Yarn globally
- **Port 4200 occupied**: Use `yarn start --port 4201`

---

## Workflow 2: Component Development with Configuration

### Description
Creating new components with Otter's configuration-driven architecture, including schema definition and external configuration support.

### User Journey
**Primary Actor**: Frontend Developer  
**Frequency**: Multiple times per sprint  
**Complexity**: Medium-High  

### Step-by-Step Process

#### 1. Component Generation
```bash
# User generates new component with Otter features
ng generate @o3r/core:component product-card --use-otter-config --use-localization
```

**Expected Outcome**: 
- Component files created with Otter integration
- Configuration interface generated
- Localization keys template created

#### 2. Configuration Schema Definition
```typescript
// User defines component configuration
// product-card.config.ts
export interface ProductCardConfig {
  /** Show product rating */
  showRating: boolean;
  /** Maximum description length */
  maxDescriptionLength: number;
  /** Button style variant */
  buttonStyle: 'primary' | 'secondary' | 'outline';
}

export const PRODUCT_CARD_DEFAULT_CONFIG: ProductCardConfig = {
  showRating: true,
  maxDescriptionLength: 150,
  buttonStyle: 'primary'
};
```

**Expected Outcome**: Type-safe configuration interface defined

#### 3. Component Implementation
```typescript
// User implements component logic
@O3rComponent({ componentType: 'Component' })
@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html'
})
export class ProductCardComponent implements OnInit {
  @Input() product: Product;
  
  public config$ = this.configurationService.getComponentConfig(
    'ProductCard',
    PRODUCT_CARD_DEFAULT_CONFIG
  );

  constructor(private configurationService: ConfigurationService) {}
}
```

**Expected Outcome**: Component integrated with Otter configuration system

#### 4. Template Development
```html
<!-- User creates template with configuration binding -->
<div class="product-card">
  <h3>{{ product.name }}</h3>
  <div class="rating" *ngIf="(config$ | async)?.showRating">
    <span>{{ product.rating }} stars</span>
  </div>
  <p>{{ product.description | slice:0:(config$ | async)?.maxDescriptionLength }}</p>
  <button [class]="'btn btn-' + (config$ | async)?.buttonStyle">
    {{ 'product-card.add-to-cart' | o3rTranslate }}
  </button>
</div>
```

**Expected Outcome**: Template responds to configuration changes

#### 5. Configuration Extraction
```bash
# User extracts configuration metadata
ng run my-app:extract-config
```

**Expected Outcome**: 
- JSON schema generated for CMS integration
- Configuration documentation updated
- Metadata files created

#### 6. Testing Configuration
```typescript
// User tests different configuration scenarios
it('should hide rating when showRating is false', () => {
  configService.setConfig('ProductCard', { showRating: false });
  fixture.detectChanges();
  
  const ratingElement = fixture.nativeElement.querySelector('.rating');
  expect(ratingElement).toBeFalsy();
});
```

**Expected Outcome**: Configuration behavior verified through tests

### Success Criteria
- [ ] Component generated with Otter features
- [ ] Configuration schema defined and typed
- [ ] Component responds to configuration changes
- [ ] Configuration metadata extracted
- [ ] Tests cover configuration scenarios

### Common Issues & Resolutions
- **Configuration not updating**: Check service injection and subscription
- **Schema extraction fails**: Verify component decorator and config interface
- **Type errors**: Ensure configuration interface matches usage

---

## Workflow 3: Localization Implementation and Management

### Description
Setting up multi-language support for components and applications, including translation key management and dynamic language switching.

### User Journey
**Primary Actor**: Frontend Developer / Content Manager  
**Frequency**: Once per feature, ongoing maintenance  
**Complexity**: Medium  

### Step-by-Step Process

#### 1. Localization Module Setup
```bash
# User adds localization support
ng add @o3r/localization
```

**Expected Outcome**: 
- Localization module installed and configured
- Translation infrastructure ready
- Default locale files created

#### 2. Translation Key Definition
```typescript
// User defines localization keys for component
// product-card.localization.ts
export const PRODUCT_CARD_LOCALIZATION = {
  'product-card.title': 'Product Details',
  'product-card.add-to-cart': 'Add to Cart',
  'product-card.out-of-stock': 'Out of Stock',
  'product-card.price-from': 'From {{price}}',
  'product-card.rating-stars': '{{rating}} out of 5 stars'
};
```

**Expected Outcome**: Translation keys defined with placeholders

#### 3. Translation File Creation
```json
// User creates translation files for each locale
// src/assets/i18n/en.json
{
  "product-card.title": "Product Details",
  "product-card.add-to-cart": "Add to Cart",
  "product-card.out-of-stock": "Out of Stock",
  "product-card.price-from": "From {{price}}",
  "product-card.rating-stars": "{{rating}} out of 5 stars"
}

// src/assets/i18n/fr.json
{
  "product-card.title": "Détails du produit",
  "product-card.add-to-cart": "Ajouter au panier",
  "product-card.out-of-stock": "Rupture de stock",
  "product-card.price-from": "À partir de {{price}}",
  "product-card.rating-stars": "{{rating}} sur 5 étoiles"
}
```

**Expected Outcome**: Complete translations for supported locales

#### 4. Template Integration
```html
<!-- User integrates translations in templates -->
<div class="product-card">
  <h3>{{ 'product-card.title' | o3rTranslate }}</h3>
  <div class="rating">
    {{ 'product-card.rating-stars' | o3rTranslate: {rating: product.rating} }}
  </div>
  <div class="price">
    {{ 'product-card.price-from' | o3rTranslate: {price: product.price | currency} }}
  </div>
  <button [disabled]="!product.inStock">
    {{ product.inStock ? 
       ('product-card.add-to-cart' | o3rTranslate) : 
       ('product-card.out-of-stock' | o3rTranslate) }}
  </button>
</div>
```

**Expected Outcome**: Dynamic content based on selected locale

#### 5. Language Switching Implementation
```typescript
// User implements language switcher
@Component({
  selector: 'app-language-switcher',
  template: `
    <select (change)="switchLanguage($event.target.value)">
      <option value="en">English</option>
      <option value="fr">Français</option>
      <option value="es">Español</option>
    </select>
  `
})
export class LanguageSwitcherComponent {
  constructor(private localizationService: LocalizationService) {}

  switchLanguage(locale: string) {
    this.localizationService.setLanguage(locale);
  }
}
```

**Expected Outcome**: Users can switch languages dynamically

#### 6. Translation Extraction and Validation
```bash
# User extracts translation keys from code
ng run my-app:extract-translations

# User validates translation completeness
ng run my-app:validate-translations
```

**Expected Outcome**: 
- All translation keys extracted
- Missing translations identified
- Translation files validated

### Success Criteria
- [ ] Localization module configured
- [ ] Translation keys defined and organized
- [ ] Multiple locale files created
- [ ] Templates use translation pipes
- [ ] Language switching works
- [ ] Translation validation passes

### Common Issues & Resolutions
- **Translations not loading**: Check i18n file paths and module configuration
- **Interpolation not working**: Verify parameter names match in template and translation
- **Missing translations**: Run extraction and validation tools

---

## Workflow 4: Rules Engine Configuration and Testing

### Description
Implementing dynamic business logic using Otter's rules engine to modify application behavior based on conditions without code changes.

### User Journey
**Primary Actor**: Business Analyst / Frontend Developer  
**Frequency**: Per business requirement change  
**Complexity**: High  

### Step-by-Step Process

#### 1. Rules Engine Setup
```bash
# User adds rules engine support
ng add @o3r/rules-engine
```

**Expected Outcome**: Rules engine module installed and configured

#### 2. Rule Definition
```typescript
// User defines business rules
const premiumUserRules = [
  {
    id: 'show-premium-features',
    name: 'Show Premium Features',
    condition: 'user.isPremium === true',
    action: 'SET_CONFIG',
    target: 'ProductCard.showPremiumFeatures',
    value: true,
    priority: 100
  },
  {
    id: 'premium-button-style',
    name: 'Premium Button Style',
    condition: 'user.isPremium === true && user.country === "US"',
    action: 'SET_CONFIG',
    target: 'ProductCard.buttonStyle',
    value: 'premium',
    priority: 200
  }
];
```

**Expected Outcome**: Business rules defined with conditions and actions

#### 3. Component Configuration Update
```typescript
// User updates component to support rule-driven config
export interface ProductCardConfig {
  showPremiumFeatures: boolean;
  buttonStyle: 'primary' | 'secondary' | 'premium';
  // ... other config properties
}

export const PRODUCT_CARD_DEFAULT_CONFIG: ProductCardConfig = {
  showPremiumFeatures: false,
  buttonStyle: 'primary'
};
```

**Expected Outcome**: Configuration schema supports rule targets

#### 4. Rules Engine Integration
```typescript
// User integrates rules engine with component
@Component({...})
export class ProductCardComponent implements OnInit {
  public config$ = this.configurationService.getComponentConfig(
    'ProductCard',
    PRODUCT_CARD_DEFAULT_CONFIG
  );

  constructor(
    private configurationService: ConfigurationService,
    private rulesEngineService: RulesEngineService
  ) {}

  ngOnInit() {
    // Apply rules based on user context
    this.rulesEngineService.setRules(premiumUserRules);
    this.rulesEngineService.evaluateRules({
      user: this.userService.getCurrentUser(),
      date: new Date().toISOString(),
      country: this.locationService.getCountry()
    });
  }
}
```

**Expected Outcome**: Rules automatically modify component configuration

#### 5. Template Adaptation
```html
<!-- User updates template to respond to rule-driven changes -->
<div class="product-card">
  <div class="premium-features" *ngIf="(config$ | async)?.showPremiumFeatures">
    <span class="premium-badge">Premium</span>
    <div class="premium-benefits">
      <p>Free shipping</p>
      <p>Extended warranty</p>
    </div>
  </div>
  
  <button [class]="'btn btn-' + (config$ | async)?.buttonStyle">
    Add to Cart
  </button>
</div>
```

**Expected Outcome**: UI adapts based on rule evaluation results

#### 6. Rule Testing and Validation
```typescript
// User tests rule evaluation scenarios
describe('Rules Engine Integration', () => {
  it('should show premium features for premium users', () => {
    const context = {
      user: { isPremium: true, country: 'US' },
      date: '2024-01-15'
    };
    
    rulesEngineService.evaluateRules(context);
    fixture.detectChanges();
    
    const premiumFeatures = fixture.nativeElement.querySelector('.premium-features');
    expect(premiumFeatures).toBeTruthy();
  });

  it('should use premium button style for US premium users', () => {
    const context = {
      user: { isPremium: true, country: 'US' }
    };
    
    rulesEngineService.evaluateRules(context);
    fixture.detectChanges();
    
    const button = fixture.nativeElement.querySelector('button');
    expect(button.classList).toContain('btn-premium');
  });
});
```

**Expected Outcome**: Rule behavior verified through comprehensive tests

### Success Criteria
- [ ] Rules engine module configured
- [ ] Business rules defined with proper syntax
- [ ] Component configuration supports rule targets
- [ ] Rules evaluation affects UI behavior
- [ ] Rule scenarios thoroughly tested
- [ ] Business stakeholders can modify rules

### Common Issues & Resolutions
- **Rules not applying**: Check rule syntax and context data structure
- **Performance issues**: Optimize rule evaluation frequency and complexity
- **Configuration conflicts**: Ensure rule priorities are properly set

---

## Workflow 5: Production Deployment and Monitoring

### Description
Deploying Otter applications to production environments with proper monitoring, analytics, and performance optimization.

### User Journey
**Primary Actor**: DevOps Engineer / Frontend Developer  
**Frequency**: Per release cycle  
**Complexity**: High  

### Step-by-Step Process

#### 1. Production Build Preparation
```bash
# User prepares production build
yarn build --configuration=production

# User runs production tests
yarn test:prod
yarn e2e:prod
```

**Expected Outcome**: 
- Optimized production bundle created
- All tests pass in production mode
- Bundle size within acceptable limits

#### 2. Environment Configuration
```typescript
// User configures production environment
// apps/my-app/src/environments/environment.prod.ts
export const environment = {
  production: true,
  apiUrl: 'https://api.company.com',
  enableAnalytics: true,
  logLevel: 'error',
  enableServiceWorker: true,
  cacheTimeout: 3600000
};
```

**Expected Outcome**: Production-optimized configuration in place

#### 3. Analytics and Monitoring Setup
```typescript
// User configures analytics tracking
@Component({...})
export class AppComponent implements OnInit {
  constructor(private analyticsService: AnalyticsService) {}

  ngOnInit() {
    if (environment.enableAnalytics) {
      this.analyticsService.initialize({
        trackingId: 'GA_TRACKING_ID',
        enableAutoTracking: true,
        enablePerformanceTracking: true
      });
    }
  }
}
```

**Expected Outcome**: Analytics and performance monitoring active

#### 4. Docker Containerization
```dockerfile
# User creates production Docker image
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
COPY . .
RUN yarn build --configuration=production

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**Expected Outcome**: Containerized application ready for deployment

#### 5. Kubernetes Deployment
```yaml
# User deploys to Kubernetes
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
        - containerPort: 80
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
```

**Expected Outcome**: Application deployed with proper resource limits

#### 6. Health Monitoring and Alerting
```typescript
// User implements health checks
@Controller('health')
export class HealthController {
  @Get()
  check() {
    return {
      status: 'ok',
      timestamp: new Date().toISOString(),
      version: environment.version,
      uptime: process.uptime()
    };
  }

  @Get('ready')
  readiness() {
    // Check dependencies
    return {
      status: 'ready',
      checks: {
        database: 'healthy',
        api: 'healthy'
      }
    };
  }
}
```

**Expected Outcome**: Health endpoints available for monitoring

#### 7. Performance Monitoring
```bash
# User sets up performance monitoring
# Lighthouse CI configuration
echo '{
  "ci": {
    "collect": {
      "numberOfRuns": 3,
      "url": ["https://app.company.com"]
    },
    "assert": {
      "assertions": {
        "categories:performance": ["error", {"minScore": 0.9}],
        "categories:accessibility": ["error", {"minScore": 0.9}]
      }
    }
  }
}' > lighthouserc.json
```

**Expected Outcome**: Automated performance monitoring configured

#### 8. Post-Deployment Verification
```bash
# User verifies deployment
curl -f https://app.company.com/health
curl -f https://app.company.com/health/ready

# User runs smoke tests
yarn test:smoke --env=production
```

**Expected Outcome**: 
- Health checks pass
- Smoke tests verify core functionality
- Application accessible to users

### Success Criteria
- [ ] Production build optimized and tested
- [ ] Environment configuration correct
- [ ] Analytics and monitoring active
- [ ] Application containerized and deployed
- [ ] Health checks responding
- [ ] Performance metrics within targets
- [ ] Smoke tests passing

### Common Issues & Resolutions
- **Build failures**: Check dependency versions and build configuration
- **Performance issues**: Optimize bundle size and enable compression
- **Health check failures**: Verify service dependencies and network connectivity
- **Analytics not tracking**: Check configuration and network policies

---

## Workflow Success Metrics

### Overall Success Indicators
- **Completion Rate**: >95% of workflows complete successfully
- **Time to Complete**: Within expected timeframes for each workflow
- **Error Rate**: <5% of workflow executions encounter blocking errors
- **User Satisfaction**: >4.5/5 rating from developer surveys

### Individual Workflow Metrics

| Workflow | Expected Duration | Success Rate Target | Key Performance Indicators |
|----------|------------------|-------------------|---------------------------|
| Project Setup | 15-30 minutes | >98% | Build success, server startup |
| Component Development | 2-4 hours | >90% | Config extraction, tests pass |
| Localization | 1-2 hours | >85% | Translation validation, UI updates |
| Rules Engine | 3-6 hours | >80% | Rule evaluation, behavior changes |
| Production Deployment | 30-60 minutes | >95% | Health checks, performance metrics |

### Continuous Improvement
- Regular workflow analysis and optimization
- User feedback collection and integration
- Documentation updates based on common issues
- Automation opportunities identification

This documentation serves as the foundation for testing scenarios, user training, and process optimization within the Otter Framework ecosystem.
