Feature: Project Setup and Configuration
  As a Frontend Developer
  I want to set up a new Otter project
  So that I can start developing Angular applications with Otter framework

  Background:
    Given I have Node.js version 20 or higher installed
    And I have npm or yarn package manager available
    And I have a stable internet connection

  @critical @setup
  Scenario: Create new Otter project successfully
    When I run "npm create @o3r my-otter-project"
    Then I should see "Creating Otter project..." message
    And the project should be created in "my-otter-project" directory
    And the project should contain "package.json" file
    And the project should contain "nx.json" file
    And the project should contain "apps" directory
    And the project should contain "libs" directory
    And all Otter dependencies should be installed

  @critical @setup
  Scenario: Install dependencies and verify setup
    Given I have created a new Otter project
    When I navigate to the project directory
    And I run "yarn install"
    Then all dependencies should be installed successfully
    And "node_modules" directory should exist
    And "yarn.lock" file should be created

  @critical @build
  Scenario: Build project successfully
    Given I have an Otter project with dependencies installed
    When I run "yarn build"
    Then the build should complete without errors
    And "dist" directory should be created
    And compiled JavaScript files should exist in "dist"
    And source maps should be generated

  @critical @development
  Scenario: Start development server
    Given I have an Otter project with dependencies installed
    When I run "yarn start"
    Then the development server should start on port 4200
    And I should see "Application bundle generation complete" message
    And the application should be accessible at "http://localhost:4200"
    And hot module replacement should be enabled

  @setup @configuration
  Scenario: Configure environment settings
    Given I have an Otter project setup
    When I open "apps/my-app/src/environments/environment.ts"
    And I update the configuration with:
      | property        | value                    |
      | production      | false                    |
      | apiUrl          | http://localhost:3000    |
      | enableAnalytics | false                    |
    And I save the file
    Then the environment configuration should be updated
    And the application should use the new configuration

  @error-handling @setup
  Scenario: Handle Node.js version incompatibility
    Given I have Node.js version 16 installed
    When I run "npm create @o3r my-otter-project"
    Then I should see an error message about Node.js version
    And the error should suggest upgrading to Node.js 20 or higher
    And the project creation should fail gracefully

  @error-handling @setup
  Scenario: Handle network connectivity issues
    Given I have limited internet connectivity
    When I run "npm create @o3r my-otter-project"
    And the download fails due to network issues
    Then I should see a network error message
    And the system should suggest checking internet connection
    And the system should provide offline installation options

  @setup @existing-project
  Scenario: Add Otter to existing Angular project
    Given I have an existing Angular project version 15 or higher
    When I run "ng add @o3r/core"
    Then Otter packages should be installed
    And the project configuration should be updated
    And existing functionality should remain intact
    And I should be able to use Otter features

  @setup @port-conflict
  Scenario: Handle port conflict during development server startup
    Given I have an Otter project setup
    And port 4200 is already in use by another application
    When I run "yarn start"
    Then I should see a port conflict message
    And the system should suggest using a different port
    When I run "yarn start --port 4201"
    Then the development server should start on port 4201
    And the application should be accessible at "http://localhost:4201"
