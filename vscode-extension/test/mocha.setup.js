// Mock vscode module for unit tests
const path = require('path');
const Module = require('module');

// Clear module cache to ensure fresh mocks
Object.keys(require.cache).forEach(key => {
  if (key.includes('vscode') || key.includes('logger')) {
    delete require.cache[key];
  }
});

// Intercept vscode module loading
const originalResolveFilename = Module._resolveFilename;
Module._resolveFilename = function (request, parent, isMain) {
  if (request === 'vscode') {
    return path.resolve(__dirname, 'mocha.setup.js');
  }
  return originalResolveFilename.call(this, request, parent, isMain);
};

// Mock vscode API
const vscode = {
  workspace: {
    getConfiguration: (section) => ({
      get: (key, defaultValue) => {
        // Return mock configuration values for testing
        if (section === 'olaf') {
          const config = {
            'repositoryOwner': 'test-owner',
            'repositoryName': 'test-repo',
            'githubToken': 'test-token',
            'usePrivateRepository': false
          };
          return config[key] || defaultValue;
        }
        return defaultValue;
      },
      update: async (key, value, target) => undefined
    })
  },
  window: {
    showInformationMessage: () => Promise.resolve(),
    showWarningMessage: () => Promise.resolve(),
    showErrorMessage: () => Promise.resolve(),
    createOutputChannel: (name) => {
      const channel = {
        appendLine: function() { return undefined; },
        clear: function() { return undefined; },
        show: function() { return undefined; },
        dispose: function() { return undefined; }
      };
      return channel;
    }
  },
  Uri: {
    file: (path) => ({
      fsPath: path,
      scheme: 'file',
      authority: '',
      path: path,
      query: '',
      fragment: ''
    })
  },
  ConfigurationTarget: {
    Global: 1,
    Workspace: 2,
    WorkspaceFolder: 3
  }
};

module.exports = vscode;

// Also set it globally
global.vscode = vscode;
