# Otter Framework - User Manual

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Project Setup](#project-setup)
4. [Core Features](#core-features)
5. [Component Development](#component-development)
6. [Configuration Management](#configuration-management)
7. [Localization](#localization)
8. [Styling and Theming](#styling-and-theming)
9. [Testing](#testing)
10. [Troubleshooting](#troubleshooting)
11. [Best Practices](#best-practices)
12. [FAQ](#faq)

---

## Introduction

Welcome to the Otter Framework! This comprehensive user manual will guide you through using Otter, a highly modular Angular framework designed to accelerate web application development.

### What is Otter?

Otter is an enterprise-grade Angular framework that provides:
- **Modular Architecture**: Pick and choose the features you need
- **Configuration-Driven Development**: Externalize business logic and UI behavior
- **Enterprise Features**: Localization, analytics, rules engine, and more
- **Developer Experience**: Comprehensive tooling and code generation
- **Scalability**: Micro-frontend support and monorepo management

### Who Should Use This Manual?

This manual is designed for:
- **Frontend Developers** building Angular applications
- **Project Leads** setting up new projects
- **Team Members** learning Otter concepts
- **Contributors** extending Otter functionality

---

## Getting Started

### Prerequisites

Before you begin, ensure you have:

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Node.js | 20.19+ or 22.17+ or 24.0+ | Runtime environment |
| npm | 8.0+ | Package manager (alternative to Yarn) |
| Yarn | 2.0+ | Recommended package manager |
| Angular CLI | 20.0+ | Angular development tools |

### Quick Start

Create a new Otter project in just one command:

```bash
# Create a new Otter monorepo
npm create @o3r my-otter-app
cd my-otter-app
```

This command will:
1. Set up a new Nx workspace
2. Install Otter framework packages
3. Configure the development environment
4. Create example components and configurations

### Verification

Verify your installation:

```bash
# Check if everything is working
yarn build
yarn test
yarn start
```

You should see:
- ✅ Build completes successfully
- ✅ All tests pass
- ✅ Development server starts on `http://localhost:4200`

---

## Project Setup

### Workspace Structure

Your Otter project follows this structure:

```
my-otter-app/
├── apps/                    # Applications
│   └── my-app/             # Main application
├── libs/                   # Shared libraries
│   ├── components/         # Reusable components
│   ├── services/          # Business logic
│   └── utils/             # Utility functions
├── tools/                 # Build and development tools
├── nx.json               # Nx workspace configuration
├── package.json          # Dependencies and scripts
└── tsconfig.base.json    # TypeScript configuration
```

### Adding Otter to Existing Projects

If you have an existing Angular project:

```bash
# Add Otter to existing project
ng add @o3r/core

# Add specific Otter modules
ng add @o3r/components
ng add @o3r/configuration
ng add @o3r/localization
```

### Environment Configuration

Configure different environments in `apps/my-app/src/environments/`:

```typescript
// environment.ts
export const environment = {
  production: false,
  apiUrl: 'http://localhost:3000',
  enableAnalytics: false,
  logLevel: 'debug'
};

// environment.prod.ts  
export const environment = {
  production: true,
  apiUrl: 'https://api.myapp.com',
  enableAnalytics: true,
  logLevel: 'error'
};
```

---

## Core Features

### 1. Component System

Otter provides enhanced Angular components with built-in configuration support:

```typescript
import { Component } from '@angular/core';
import { O3rComponent } from '@o3r/core';

@O3rComponent({
  componentType: 'Component'
})
@Component({
  selector: 'app-my-component',
  templateUrl: './my-component.component.html'
})
export class MyComponent {
  // Component logic here
}
```

**Key Features:**
- **Configuration Support**: Components can be configured externally
- **Metadata Extraction**: Automatic configuration schema generation
- **Theming**: Built-in support for design tokens
- **Localization**: Integrated translation support

### 2. Configuration Management

Externalize component behavior through configuration:

```typescript
// Component configuration interface
export interface MyComponentConfig {
  title: string;
  showDescription: boolean;
  maxItems: number;
}

// Default configuration
export const MY_COMPONENT_DEFAULT_CONFIG: MyComponentConfig = {
  title: 'Default Title',
  showDescription: true,
  maxItems: 10
};

// Using configuration in component
@Component({...})
export class MyComponent implements OnInit {
  public config$ = this.configurationService.getComponentConfig(
    'MyComponent',
    MY_COMPONENT_DEFAULT_CONFIG
  );
}
```

### 3. Rules Engine

Implement dynamic business logic:

```typescript
// Define rules
const rules = [
  {
    id: 'show-premium-features',
    condition: 'user.isPremium === true',
    action: 'SET_CONFIG',
    target: 'MyComponent.showPremiumFeatures',
    value: true
  }
];

// Apply rules
this.rulesEngineService.setRules(rules);
```

### 4. Analytics Integration

Track user interactions automatically:

```typescript
import { AnalyticsService } from '@o3r/analytics';

@Component({...})
export class MyComponent {
  constructor(private analytics: AnalyticsService) {}

  onButtonClick() {
    this.analytics.track('button_click', {
      component: 'MyComponent',
      action: 'primary_action'
    });
  }
}
```

---

## Component Development

### Creating Components

Use Otter schematics to generate components:

```bash
# Generate a new component
ng generate @o3r/core:component my-feature

# Generate with configuration support
ng generate @o3r/core:component my-feature --use-otter-config

# Generate with localization
ng generate @o3r/core:component my-feature --use-localization
```

### Component Structure

Generated components follow this pattern:

```
my-feature/
├── my-feature.component.ts       # Component logic
├── my-feature.component.html     # Template
├── my-feature.component.scss     # Styles
├── my-feature.component.spec.ts  # Unit tests
├── my-feature.config.ts          # Configuration interface
├── my-feature.localization.ts    # Translation keys
└── my-feature.template.ts        # Template override support
```

### Configuration-Driven Components

Create components that adapt based on external configuration:

```typescript
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

  constructor(
    private configurationService: ConfigurationService
  ) {}

  ngOnInit() {
    // Component automatically updates when configuration changes
    this.config$.subscribe(config => {
      // Apply configuration-driven behavior
    });
  }
}
```

### Template Customization

Override component templates without modifying source code:

```typescript
// Register template override
this.templateService.registerTemplate('ProductCard', {
  template: `
    <div class="custom-product-card">
      <h3>{{ product.name }}</h3>
      <p>{{ product.description }}</p>
      <button (click)="addToCart()">Add to Cart</button>
    </div>
  `
});
```

---

## Configuration Management

### Configuration Schema

Define configuration schemas for your components:

```typescript
export interface ProductCardConfig {
  /** Display product rating */
  showRating: boolean;
  /** Maximum description length */
  maxDescriptionLength: number;
  /** Button style variant */
  buttonStyle: 'primary' | 'secondary' | 'outline';
  /** Enable quick add to cart */
  enableQuickAdd: boolean;
}

export const PRODUCT_CARD_DEFAULT_CONFIG: ProductCardConfig = {
  showRating: true,
  maxDescriptionLength: 150,
  buttonStyle: 'primary',
  enableQuickAdd: false
};
```

### Configuration Sources

Otter supports multiple configuration sources:

1. **Default Configuration**: Hardcoded defaults in components
2. **Environment Configuration**: Environment-specific overrides
3. **Remote Configuration**: CMS or API-driven configuration
4. **User Preferences**: User-specific customizations

```typescript
// Configure multiple sources
this.configurationService.addSource('environment', environmentConfig);
this.configurationService.addSource('remote', remoteConfigService);
this.configurationService.addSource('user', userPreferencesService);
```

### Configuration Extraction

Extract configuration metadata from your codebase:

```bash
# Extract configuration schemas
ng run my-app:extract-config

# Output: Generated configuration files for CMS integration
```

This generates:
- JSON schemas for each component
- Configuration documentation
- CMS integration files

---

## Localization

### Setting Up Localization

Enable localization in your application:

```bash
# Add localization support
ng add @o3r/localization
```

### Defining Translation Keys

Create localization keys for your components:

```typescript
// product-card.localization.ts
export const PRODUCT_CARD_LOCALIZATION = {
  'product-card.add-to-cart': 'Add to Cart',
  'product-card.out-of-stock': 'Out of Stock',
  'product-card.price-from': 'From {{price}}',
  'product-card.rating-label': '{{rating}} out of 5 stars'
};
```

### Using Translations in Templates

```html
<!-- product-card.component.html -->
<div class="product-card">
  <h3>{{ product.name }}</h3>
  <p>{{ product.description }}</p>
  
  <div class="rating" *ngIf="config.showRating">
    <span>{{ 'product-card.rating-label' | o3rTranslate: {rating: product.rating} }}</span>
  </div>
  
  <div class="price">
    {{ 'product-card.price-from' | o3rTranslate: {price: product.price | currency} }}
  </div>
  
  <button 
    [disabled]="!product.inStock"
    (click)="addToCart()">
    {{ product.inStock ? 
       ('product-card.add-to-cart' | o3rTranslate) : 
       ('product-card.out-of-stock' | o3rTranslate) }}
  </button>
</div>
```

### Managing Translation Files

Organize translations by locale:

```
src/assets/i18n/
├── en.json              # English (default)
├── fr.json              # French
├── es.json              # Spanish
└── de.json              # German
```

```json
// en.json
{
  "product-card.add-to-cart": "Add to Cart",
  "product-card.out-of-stock": "Out of Stock",
  "product-card.price-from": "From {{price}}",
  "product-card.rating-label": "{{rating}} out of 5 stars"
}

// fr.json
{
  "product-card.add-to-cart": "Ajouter au panier",
  "product-card.out-of-stock": "Rupture de stock",
  "product-card.price-from": "À partir de {{price}}",
  "product-card.rating-label": "{{rating}} sur 5 étoiles"
}
```

### Dynamic Language Switching

```typescript
@Component({...})
export class LanguageSwitcherComponent {
  constructor(private localizationService: LocalizationService) {}

  switchLanguage(locale: string) {
    this.localizationService.setLanguage(locale);
  }
}
```

---

## Styling and Theming

### Design System Integration

Otter integrates with design systems through design tokens:

```scss
// Import Otter design tokens
@import '@o3r/design/scss/tokens';

.product-card {
  padding: var(--o3r-spacing-md);
  border-radius: var(--o3r-border-radius-md);
  background: var(--o3r-color-surface);
  box-shadow: var(--o3r-shadow-sm);
  
  .title {
    color: var(--o3r-color-text-primary);
    font-size: var(--o3r-font-size-lg);
    font-weight: var(--o3r-font-weight-semibold);
  }
  
  .price {
    color: var(--o3r-color-primary);
    font-weight: var(--o3r-font-weight-bold);
  }
}
```

### Theme Customization

Create custom themes by overriding design tokens:

```scss
// themes/dark-theme.scss
:root[data-theme="dark"] {
  --o3r-color-surface: #1a1a1a;
  --o3r-color-text-primary: #ffffff;
  --o3r-color-primary: #4f46e5;
  --o3r-color-background: #0f0f0f;
}

// themes/light-theme.scss
:root[data-theme="light"] {
  --o3r-color-surface: #ffffff;
  --o3r-color-text-primary: #1a1a1a;
  --o3r-color-primary: #3b82f6;
  --o3r-color-background: #f9fafb;
}
```

### Component Styling Best Practices

1. **Use Design Tokens**: Always prefer design tokens over hardcoded values
2. **BEM Methodology**: Follow BEM naming conventions
3. **Responsive Design**: Use Otter's responsive utilities
4. **Accessibility**: Ensure proper contrast and focus states

```scss
.product-card {
  // Base styles using design tokens
  padding: var(--o3r-spacing-md);
  
  // BEM modifiers
  &--featured {
    border: 2px solid var(--o3r-color-primary);
  }
  
  &--compact {
    padding: var(--o3r-spacing-sm);
  }
  
  // Responsive behavior
  @media (max-width: 768px) {
    padding: var(--o3r-spacing-sm);
  }
  
  // Accessibility
  &:focus-within {
    outline: 2px solid var(--o3r-color-focus);
    outline-offset: 2px;
  }
}
```

---

## Testing

### Unit Testing

Otter provides testing utilities for component testing:

```typescript
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { O3rTestingModule } from '@o3r/testing';
import { ProductCardComponent } from './product-card.component';

describe('ProductCardComponent', () => {
  let component: ProductCardComponent;
  let fixture: ComponentFixture<ProductCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ProductCardComponent],
      imports: [O3rTestingModule]
    }).compileComponents();

    fixture = TestBed.createComponent(ProductCardComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display product information', () => {
    const mockProduct = {
      name: 'Test Product',
      price: 29.99,
      inStock: true
    };
    
    component.product = mockProduct;
    fixture.detectChanges();
    
    expect(fixture.nativeElement.textContent).toContain('Test Product');
  });

  it('should handle configuration changes', () => {
    // Test configuration-driven behavior
    const configService = TestBed.inject(ConfigurationService);
    configService.setConfig('ProductCard', { showRating: false });
    
    fixture.detectChanges();
    
    const ratingElement = fixture.nativeElement.querySelector('.rating');
    expect(ratingElement).toBeFalsy();
  });
});
```

### Integration Testing

Test component interactions and data flow:

```typescript
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { O3rTestingModule } from '@o3r/testing';
import { ProductListComponent } from './product-list.component';

describe('ProductListComponent Integration', () => {
  let component: ProductListComponent;
  let fixture: ComponentFixture<ProductListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ProductListComponent],
      imports: [O3rTestingModule.withConfig({
        'ProductCard': { showRating: true, enableQuickAdd: true }
      })]
    }).compileComponents();
  });

  it('should handle product selection', () => {
    // Test user interactions across components
    const productCards = fixture.nativeElement.querySelectorAll('app-product-card');
    const firstCard = productCards[0];
    
    firstCard.click();
    fixture.detectChanges();
    
    expect(component.selectedProduct).toBeDefined();
  });
});
```

### E2E Testing

Use Playwright for end-to-end testing:

```typescript
import { test, expect } from '@playwright/test';

test.describe('Product Catalog', () => {
  test('should allow users to browse and purchase products', async ({ page }) => {
    await page.goto('/products');
    
    // Wait for products to load
    await page.waitForSelector('[data-testid="product-card"]');
    
    // Verify products are displayed
    const productCards = await page.locator('[data-testid="product-card"]');
    await expect(productCards).toHaveCountGreaterThan(0);
    
    // Click on first product
    await productCards.first().click();
    
    // Verify product details page
    await expect(page.locator('h1')).toBeVisible();
    
    // Add to cart
    await page.click('[data-testid="add-to-cart"]');
    
    // Verify cart update
    await expect(page.locator('[data-testid="cart-count"]')).toContainText('1');
  });
});
```

---

## Troubleshooting

### Common Issues

#### 1. Build Failures

**Problem**: Build fails with dependency errors
```
Error: Cannot resolve dependency '@o3r/core'
```

**Solution**:
```bash
# Clear node_modules and reinstall
rm -rf node_modules yarn.lock
yarn install

# Ensure peer dependencies are installed
yarn add @angular/core@^20.0.0
```

#### 2. Configuration Not Loading

**Problem**: Component configuration not applying

**Solution**:
1. Verify configuration service is imported:
```typescript
import { ConfigurationModule } from '@o3r/configuration';

@NgModule({
  imports: [ConfigurationModule.forRoot()]
})
export class AppModule {}
```

2. Check configuration schema:
```bash
ng run my-app:extract-config
```

#### 3. Localization Keys Missing

**Problem**: Translation keys showing as raw keys

**Solution**:
1. Verify localization module setup:
```typescript
import { LocalizationModule } from '@o3r/localization';

@NgModule({
  imports: [
    LocalizationModule.forRoot({
      supportedLocales: ['en', 'fr', 'es']
    })
  ]
})
export class AppModule {}
```

2. Check translation files exist in `src/assets/i18n/`

#### 4. Styling Issues

**Problem**: Design tokens not working

**Solution**:
1. Import design tokens in `styles.scss`:
```scss
@import '@o3r/design/scss/tokens';
```

2. Verify CSS custom properties support in target browsers

### Debug Mode

Enable debug mode for detailed logging:

```typescript
// environment.ts
export const environment = {
  production: false,
  debug: true,
  logLevel: 'debug'
};
```

### Performance Issues

If experiencing slow builds or runtime performance:

1. **Enable build caching**:
```bash
# Use Nx cache
nx run-many --target=build --parallel
```

2. **Optimize bundle size**:
```bash
# Analyze bundle
yarn build --stats-json
npx webpack-bundle-analyzer dist/stats.json
```

3. **Lazy load modules**:
```typescript
const routes: Routes = [
  {
    path: 'products',
    loadChildren: () => import('./products/products.module').then(m => m.ProductsModule)
  }
];
```

---

## Best Practices

### 1. Component Design

- **Single Responsibility**: Each component should have one clear purpose
- **Configuration-Driven**: Externalize behavior through configuration
- **Reusable**: Design components for reuse across different contexts
- **Accessible**: Follow WCAG guidelines for accessibility

### 2. Configuration Management

- **Schema-First**: Define configuration schemas before implementation
- **Validation**: Validate configuration at runtime
- **Documentation**: Document all configuration options
- **Defaults**: Provide sensible default values

### 3. Performance

- **Lazy Loading**: Use lazy loading for feature modules
- **OnPush Strategy**: Use OnPush change detection for better performance
- **Tree Shaking**: Ensure unused code is eliminated
- **Bundle Optimization**: Monitor and optimize bundle sizes

### 4. Testing

- **Test Pyramid**: More unit tests, fewer integration tests, minimal E2E tests
- **Configuration Testing**: Test different configuration scenarios
- **Accessibility Testing**: Include accessibility in your test suite
- **Performance Testing**: Monitor performance regressions

### 5. Code Organization

- **Feature Modules**: Organize code by features, not by file types
- **Barrel Exports**: Use index.ts files for clean imports
- **Consistent Naming**: Follow consistent naming conventions
- **Documentation**: Document complex business logic and configurations

---

## FAQ

### General Questions

**Q: Can I use Otter with existing Angular projects?**
A: Yes! Otter is designed to be incrementally adoptable. You can add Otter modules to existing projects using `ng add @o3r/core`.

**Q: Is Otter compatible with Angular Universal (SSR)?**
A: Yes, Otter fully supports server-side rendering and follows Angular Universal best practices.

**Q: Can I use Otter with other UI libraries like Angular Material?**
A: Absolutely! Otter is designed to work alongside other Angular libraries and UI frameworks.

### Configuration Questions

**Q: How do I override configuration for specific environments?**
A: Use environment-specific configuration files and the configuration service's source priority system.

**Q: Can configuration be changed at runtime?**
A: Yes, Otter supports dynamic configuration changes through the configuration service and external sources like APIs.

### Development Questions

**Q: How do I create custom Otter schematics?**
A: Extend the base Otter schematics or create new ones using Angular Schematics CLI. See the developer documentation for details.

**Q: Can I contribute to Otter?**
A: Yes! Otter is open source. Check the contributing guidelines in the repository for how to get started.

### Performance Questions

**Q: Does Otter impact bundle size significantly?**
A: Otter is designed to be tree-shakeable. You only include the modules you use, minimizing bundle size impact.

**Q: How do I optimize Otter applications for production?**
A: Follow the performance best practices section, enable production builds, and use the provided optimization guides.

---

## Next Steps

Now that you've learned the basics of Otter:

1. **Explore Advanced Features**: Check out the rules engine, analytics, and micro-frontend capabilities
2. **Join the Community**: Connect with other Otter developers and contributors
3. **Read the API Documentation**: Dive deeper into specific modules and APIs
4. **Check Examples**: Browse the showcase application for real-world examples
5. **Contribute**: Help improve Otter by reporting issues or contributing code

For more detailed information, refer to:
- [API Documentation](./API-DOCUMENTATION.md)
- [Admin Manual](./ADMIN-MANUAL.md)
- [Operator Manual](./OPERATOR-MANUAL.md)
- [Architecture Guide](./LOGICAL-ARCHITECTURE.md)

Happy coding with Otter! 🦦
