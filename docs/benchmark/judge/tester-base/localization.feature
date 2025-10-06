Feature: Localization and Multi-Language Support
  As a Frontend Developer
  I want to implement multi-language support
  So that users can access the application in their preferred language

  Background:
    Given I have an Otter project setup
    And I am in the project root directory

  @critical @localization-setup
  Scenario: Setup localization module
    When I run "ng add @o3r/localization"
    Then the localization module should be installed
    And localization configuration should be added to the project
    And translation infrastructure should be ready
    And default locale files should be created in "src/assets/i18n/"

  @critical @translation-keys
  Scenario: Define translation keys for component
    Given I have localization module configured
    When I create translation key definitions:
      ```typescript
      export const PRODUCT_CARD_LOCALIZATION = {
        'product-card.title': 'Product Details',
        'product-card.add-to-cart': 'Add to Cart',
        'product-card.out-of-stock': 'Out of Stock',
        'product-card.price-from': 'From {{price}}',
        'product-card.rating-stars': '{{rating}} out of 5 stars'
      };
      ```
    Then the translation keys should be properly formatted
    And placeholders should be correctly defined
    And the keys should follow naming conventions

  @critical @translation-files
  Scenario: Create translation files for multiple locales
    Given I have translation keys defined
    When I create translation files for English, French, and Spanish:
      | locale | file_path              |
      | en     | src/assets/i18n/en.json |
      | fr     | src/assets/i18n/fr.json |
      | es     | src/assets/i18n/es.json |
    And I provide translations for each locale:
      | key                      | en              | fr                    | es                    |
      | product-card.title       | Product Details | Détails du produit    | Detalles del producto |
      | product-card.add-to-cart | Add to Cart     | Ajouter au panier     | Añadir al carrito     |
      | product-card.out-of-stock| Out of Stock    | Rupture de stock      | Agotado               |
    Then all translation files should be valid JSON
    And all required keys should be present in each locale
    And placeholder syntax should be consistent

  @critical @template-integration
  Scenario: Integrate translations in component templates
    Given I have translation files created
    When I use translation pipes in the template:
      ```html
      <h3>{{ 'product-card.title' | o3rTranslate }}</h3>
      <div class="rating">
        {{ 'product-card.rating-stars' | o3rTranslate: {rating: product.rating} }}
      </div>
      <button>{{ 'product-card.add-to-cart' | o3rTranslate }}</button>
      ```
    Then the template should display translated content
    And placeholders should be properly interpolated
    And the content should update when locale changes

  @critical @language-switching
  Scenario: Implement dynamic language switching
    Given I have multiple locales configured
    When I create a language switcher component:
      ```typescript
      switchLanguage(locale: string) {
        this.localizationService.setLanguage(locale);
      }
      ```
    And I provide language selection options:
      | locale | display_name |
      | en     | English      |
      | fr     | Français     |
      | es     | Español      |
    Then users should be able to select their preferred language
    And the entire application should switch to the selected language
    And the language preference should be persisted

  @localization @extraction
  Scenario: Extract translation keys from codebase
    Given I have components with translation keys in templates
    When I run "ng run my-app:extract-translations"
    Then all translation keys should be extracted from the codebase
    And a master translation file should be generated
    And missing translations should be identified
    And unused translation keys should be reported

  @localization @validation
  Scenario: Validate translation completeness
    Given I have translation files for multiple locales
    When I run "ng run my-app:validate-translations"
    Then the system should check for missing translations
    And inconsistent placeholder usage should be detected
    And a validation report should be generated
    And the build should fail if critical translations are missing

  @localization @interpolation
  Scenario: Handle complex interpolation scenarios
    Given I have translations with multiple placeholders
    When I use complex interpolation:
      ```html
      {{ 'order.summary' | o3rTranslate: {
          count: items.length,
          total: totalPrice | currency,
          date: orderDate | date:'short'
        } }}
      ```
    And the translation is: "Order of {{count}} items for {{total}} on {{date}}"
    Then all placeholders should be correctly replaced
    And formatting pipes should work within interpolation
    And the final text should be properly formatted

  @error-handling @localization
  Scenario: Handle missing translation keys
    Given I have a component using translation keys
    When I use a translation key that doesn't exist: "missing.key"
    Then the system should display the key itself as fallback
    And a warning should be logged in development mode
    And the application should continue to function
    And missing keys should be reported in translation validation

  @error-handling @localization
  Scenario: Handle malformed translation files
    Given I have translation files configured
    When a translation file contains invalid JSON:
      ```json
      {
        "valid.key": "Valid translation",
        "invalid.key": "Missing closing quote
      }
      ```
    Then the localization service should detect the error
    And a clear error message should be displayed
    And the application should fall back to default locale
    And the error should be logged for debugging

  @performance @localization
  Scenario: Optimize translation loading performance
    Given I have a large application with many translation keys
    When I load a page with 50+ translated elements
    Then translation loading should complete within 200ms
    And translations should be cached for subsequent use
    And memory usage should remain stable
    And there should be no performance degradation

  @localization @rtl-support
  Scenario: Support right-to-left languages
    Given I have localization configured
    When I add support for Arabic language:
      | locale | direction | file_path              |
      | ar     | rtl       | src/assets/i18n/ar.json |
    And I switch to Arabic locale
    Then the text direction should change to right-to-left
    And UI layout should adapt to RTL direction
    And text alignment should be appropriate for RTL
    And the user interface should remain functional

  @localization @pluralization
  Scenario: Handle pluralization rules
    Given I have translations that require pluralization
    When I define pluralization rules:
      ```json
      {
        "items.count": {
          "=0": "No items",
          "=1": "One item",
          "other": "{{count}} items"
        }
      }
      ```
    And I use pluralization in templates:
      ```html
      {{ 'items.count' | o3rTranslate: {count: itemCount} }}
      ```
    Then the correct plural form should be displayed based on count
    And different languages should use appropriate pluralization rules
    And edge cases (0, 1, many) should be handled correctly

  @localization @lazy-loading
  Scenario: Implement lazy loading of translation files
    Given I have a large application with multiple feature modules
    When I configure lazy loading for translation files
    And I navigate to a feature that requires specific translations
    Then only the required translation files should be loaded
    And loading should happen asynchronously
    And the user interface should not block during loading
    And translation files should be cached after first load
