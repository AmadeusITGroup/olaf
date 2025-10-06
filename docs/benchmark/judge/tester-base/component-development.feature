Feature: Component Development with Configuration
  As a Frontend Developer
  I want to create configurable components using Otter
  So that I can build flexible and maintainable Angular applications

  Background:
    Given I have an Otter project setup and running
    And I am in the project root directory

  @critical @component-generation
  Scenario: Generate component with Otter configuration support
    When I run "ng generate @o3r/core:component product-card --use-otter-config"
    Then a new component should be created in "src/app/product-card"
    And the component should have the following files:
      | file                              |
      | product-card.component.ts         |
      | product-card.component.html       |
      | product-card.component.scss       |
      | product-card.component.spec.ts    |
      | product-card.config.ts            |
    And the component should be decorated with "@O3rComponent"
    And the configuration interface should be defined
    And default configuration values should be provided

  @critical @configuration-schema
  Scenario: Define component configuration schema
    Given I have generated a component with configuration support
    When I define the configuration interface:
      ```typescript
      export interface ProductCardConfig {
        showRating: boolean;
        maxDescriptionLength: number;
        buttonStyle: 'primary' | 'secondary' | 'outline';
      }
      ```
    And I set default configuration values:
      ```typescript
      export const PRODUCT_CARD_DEFAULT_CONFIG: ProductCardConfig = {
        showRating: true,
        maxDescriptionLength: 150,
        buttonStyle: 'primary'
      };
      ```
    Then the configuration should be type-safe
    And TypeScript compilation should succeed
    And the configuration should have proper JSDoc documentation

  @critical @configuration-integration
  Scenario: Integrate configuration service in component
    Given I have a component with configuration schema defined
    When I inject the configuration service:
      ```typescript
      public config$ = this.configurationService.getComponentConfig(
        'ProductCard',
        PRODUCT_CARD_DEFAULT_CONFIG
      );
      ```
    And I use configuration in the template:
      ```html
      <div class="rating" *ngIf="(config$ | async)?.showRating">
        {{ product.rating }} stars
      </div>
      ```
    Then the component should respond to configuration changes
    And the template should update when configuration is modified

  @configuration @extraction
  Scenario: Extract configuration metadata
    Given I have components with configuration defined
    When I run "ng run my-app:extract-config"
    Then JSON schemas should be generated for each component
    And configuration documentation should be created
    And CMS integration files should be available
    And the extraction should complete without errors

  @configuration @testing
  Scenario: Test configuration-driven behavior
    Given I have a component with configuration support
    When I write a test that modifies configuration:
      ```typescript
      it('should hide rating when showRating is false', () => {
        configService.setConfig('ProductCard', { showRating: false });
        fixture.detectChanges();
        
        const ratingElement = fixture.nativeElement.querySelector('.rating');
        expect(ratingElement).toBeFalsy();
      });
      ```
    And I run the test
    Then the test should pass
    And the component behavior should be verified

  @component-generation @localization
  Scenario: Generate component with localization support
    When I run "ng generate @o3r/core:component user-profile --use-localization"
    Then the component should be created with localization files
    And "user-profile.localization.ts" should be generated
    And translation keys should be defined
    And the component template should use translation pipes

  @error-handling @configuration
  Scenario: Handle invalid configuration values
    Given I have a component with configuration schema
    When I provide invalid configuration values:
      | property              | value   | expected_type |
      | showRating           | "true"  | boolean       |
      | maxDescriptionLength | "150"   | number        |
      | buttonStyle          | "large" | enum          |
    Then the configuration service should validate the values
    And invalid values should be rejected
    And default values should be used for invalid properties
    And warnings should be logged for invalid configurations

  @configuration @dynamic-updates
  Scenario: Handle dynamic configuration updates
    Given I have a component rendered with default configuration
    When the configuration is updated externally:
      | property              | new_value |
      | showRating           | false     |
      | buttonStyle          | secondary |
    Then the component should automatically update
    And the UI should reflect the new configuration
    And no manual refresh should be required

  @performance @configuration
  Scenario: Optimize configuration performance
    Given I have multiple components with configuration
    When I load a page with 10 configured components
    Then configuration loading should complete within 100ms
    And memory usage should remain stable
    And there should be no memory leaks
    And configuration changes should not cause unnecessary re-renders

  @component-generation @error-handling
  Scenario: Handle component generation errors
    Given I am in a directory without Angular CLI
    When I run "ng generate @o3r/core:component test-component"
    Then I should see an error message about Angular CLI
    And the command should fail gracefully
    And no partial files should be created

  @configuration @validation
  Scenario: Validate configuration schema at runtime
    Given I have a component with strict configuration schema
    When I provide configuration that doesn't match the schema
    Then the configuration service should validate the input
    And schema validation errors should be reported
    And the component should fall back to default configuration
    And detailed error information should be available in development mode
