# Template: Functional Test Step Implementations

## API Testing Step Definitions

```javascript
Given('the API is available', async function() {
  // Verify API health endpoint
  const response = await api.get('/health');
  expect(response.status).to.equal(200);
});

When('I send a POST request to {string} with valid data', async function(endpoint) {
  this.response = await api.post(endpoint, this.testData);
});

Then('I should receive a {int} status code', function(statusCode) {
  expect(this.response.status).to.equal(statusCode);
});

Then('the response should contain expected data structure', function() {
  expect(this.response.data).to.have.property('expectedField');
  // Add specific validation based on expected response structure
});

Then('the data should be persisted correctly', async function() {
  // Verify data was saved to database or storage
  const savedData = await database.findById(this.response.data.id);
  expect(savedData).to.exist;
});
```

## UI Testing Step Definitions

```javascript
Given('I am on the login page', async function() {
  await browser.navigateTo('/login');
});

When('I enter valid credentials', async function() {
  await loginPage.enterUsername(testData.validUser.username);
  await loginPage.enterPassword(testData.validUser.password);
  await loginPage.clickLogin();
});

Then('I should be redirected to the dashboard', async function() {
  expect(await browser.getCurrentUrl()).to.include('/dashboard');
});

Then('I should see {string}', async function(expectedText) {
  const pageText = await page.getText();
  expect(pageText).to.include(expectedText);
});
```

## Test Data Management Patterns

```javascript
// Setup test data before scenario
Before(async function() {
  this.testData = {
    validUser: {
      username: 'testuser@example.com',
      password: 'TestPassword123!'
    },
    validRequest: {
      // Populate based on actual API requirements
    }
  };
});

// Cleanup after scenario
After(async function() {
  // Clean up any test data created during the scenario
  if (this.createdResourceId) {
    await api.delete(`/api/resource/${this.createdResourceId}`);
  }
});
```

## Environment Configuration

```javascript
// config/test-environment.js
module.exports = {
  apiBaseUrl: process.env.TEST_API_URL || 'http://localhost:8080',
  databaseConnection: process.env.TEST_DB_URL,
  timeout: 30000,
  retries: 2
};
```

## Test Framework Setup

### Cucumber Configuration (cucumber.js)

```javascript
module.exports = {
  default: {
    require: ['tests/step-definitions/**/*.js', 'tests/support/**/*.js'],
    format: ['progress', 'html:test-results/cucumber-report.html'],
    parallel: 2
  }
};
```

### SpecFlow Configuration (.NET)

```xml
<specFlow>
  <unitTestProvider name="NUnit" />
  <stepAssemblies>
    <stepAssembly assembly="YourProject.Tests" />
  </stepAssemblies>
</specFlow>
```

## Implementation Notes

- **Framework Selection**: Choose Cucumber (JavaScript/Java), SpecFlow (.NET), or Behave (Python) based on project stack
- **Step Definitions**: Implement step definitions that interact with actual system (API calls, UI interactions)
- **Test Data**: Use realistic test data sets and ensure proper cleanup
- **Environment**: Configure isolated test environments with appropriate system dependencies
- **Assertions**: Use framework-appropriate assertion libraries (Chai, Assert, etc.)
- **Reporting**: Configure test reports for CI/CD integration
