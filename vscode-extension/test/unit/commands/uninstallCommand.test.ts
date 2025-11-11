/// <reference types="mocha" />

import * as assert from 'assert';
import * as vscode from 'vscode';
import * as path from 'path';
import { UninstallCommand } from '../../../src/commands/uninstallCommand';

/**
 * Mock InstallationManager for testing
 */
class MockInstallationManager {
    private mockScopes: string[] = [];
    private mockUninstallResults: { [scope: string]: boolean } = {};
    private mockInstallationInfo: { [scope: string]: any } = {};

    setMockScopes(scopes: string[]): void {
        this.mockScopes = scopes;
    }

    setMockUninstallResult(scope: string, result: boolean): void {
        this.mockUninstallResults[scope] = result;
    }

    setMockInstallationInfo(scope: string, info: any): void {
        this.mockInstallationInfo[scope] = info;
    }

    async getInstalledScopes(): Promise<string[]> {
        return this.mockScopes;
    }

    async uninstall(scope: string): Promise<boolean> {
        return this.mockUninstallResults[scope] !== undefined ? this.mockUninstallResults[scope] : true;
    }

    async getInstallationInfo(scope: string): Promise<any> {
        return this.mockInstallationInfo[scope] || null;
    }
}

/**
 * Mock Logger for testing
 */
class MockLogger {
    private logs: Array<{ level: string; message: string; error?: Error }> = [];

    info(message: string): void {
        this.logs.push({ level: 'info', message });
    }

    warn(message: string): void {
        this.logs.push({ level: 'warn', message });
    }

    error(message: string, error?: Error): void {
        this.logs.push({ level: 'error', message, error });
    }

    getLogs(): Array<{ level: string; message: string; error?: Error }> {
        return this.logs;
    }

    clearLogs(): void {
        this.logs = [];
    }
}

describe('UninstallCommand Test Suite', () => {
    let uninstallCommand: UninstallCommand;
    let mockInstallationManager: MockInstallationManager;
    let mockLogger: MockLogger;
    let originalShowWarningMessage: any;
    let originalShowInformationMessage: any;
    let originalShowErrorMessage: any;
    let originalWithProgress: any;

    beforeEach(() => {
        // Create mocks
        mockInstallationManager = new MockInstallationManager();
        mockLogger = new MockLogger();

        // Create command instance
        uninstallCommand = new UninstallCommand(mockInstallationManager as any, mockLogger as any);

        // Store original VSCode API methods
        originalShowWarningMessage = vscode.window.showWarningMessage;
        originalShowInformationMessage = vscode.window.showInformationMessage;
        originalShowErrorMessage = vscode.window.showErrorMessage;
        originalWithProgress = vscode.window.withProgress;
    });

    afterEach(() => {
        // Restore original VSCode API methods
        if (originalShowWarningMessage) {
            (vscode.window as any).showWarningMessage = originalShowWarningMessage;
        }
        if (originalShowInformationMessage) {
            (vscode.window as any).showInformationMessage = originalShowInformationMessage;
        }
        if (originalShowErrorMessage) {
            (vscode.window as any).showErrorMessage = originalShowErrorMessage;
        }
        if (originalWithProgress) {
            (vscode.window as any).withProgress = originalWithProgress;
        }
    });

    describe('getInstalledFiles', () => {
        it('should return empty array when no scopes are installed', async () => {
            // Arrange
            mockInstallationManager.setMockScopes([]);

            // Act
            const result = await uninstallCommand.getInstalledFiles();

            // Assert
            assert.strictEqual(result.length, 0);
        });

        it('should aggregate files from all scopes correctly', async () => {
            // Arrange
            const installedScopes = ['user', 'workspace'];
            mockInstallationManager.setMockScopes(installedScopes);
            mockInstallationManager.setMockInstallationInfo('user', {
                installedFiles: ['olaf-core/file1.txt', 'olaf-core/file2.txt'],
                scope: 'user',
                installedPath: '/home/user/.olaf'
            });
            mockInstallationManager.setMockInstallationInfo('workspace', {
                installedFiles: ['workspace-file.txt'],
                scope: 'workspace',
                installedPath: '/workspace/.olaf'
            });

            // Act
            const result = await uninstallCommand.getInstalledFiles();

            // Assert
            assert.strictEqual(result.length, 3);
            assert.strictEqual(result.some(f => f.scope === 'user' && f.path === 'olaf-core/file1.txt'), true);
            assert.strictEqual(result.some(f => f.scope === 'workspace' && f.path === 'workspace-file.txt'), true);
            
            // Check that full paths are constructed correctly
            const userFile1 = result.find(f => f.scope === 'user' && f.path === 'olaf-core/file1.txt');
            const expectedPath = path.join('/home/user/.olaf', 'olaf-core/file1.txt');
            assert.strictEqual(userFile1?.fullPath, expectedPath);
        });

        it('should handle scopes with no installation info gracefully', async () => {
            // Arrange
            const installedScopes = ['user', 'workspace'];
            mockInstallationManager.setMockScopes(installedScopes);
            mockInstallationManager.setMockInstallationInfo('user', {
                installedFiles: ['file1.txt'],
                scope: 'user',
                installedPath: '/home/user/.olaf'
            });
            // workspace has no installation info (returns null)

            // Act
            const result = await uninstallCommand.getInstalledFiles();

            // Assert
            assert.strictEqual(result.length, 1);
            
            // Check that warning was logged
            const logs = mockLogger.getLogs();
            const warningLog = logs.find(log => log.level === 'warn' && log.message.includes('No installation info found for scope: workspace'));
            assert.strictEqual(warningLog !== undefined, true);
        });
    });

    describe('executeUninstallAll - Core Logic Tests', () => {
        it('should handle no installations correctly', async () => {
            // Arrange
            mockInstallationManager.setMockScopes([]);
            let informationMessageCalled = false;
            let messageContent = '';

            (vscode.window as any).showInformationMessage = async (message: string) => {
                informationMessageCalled = true;
                messageContent = message;
                return undefined;
            };

            // Act
            await uninstallCommand.executeUninstallAll();

            // Assert
            assert.strictEqual(informationMessageCalled, true);
            assert.strictEqual(messageContent, 'OLAF is not installed in any scope.');
            
            const logs = mockLogger.getLogs();
            assert.strictEqual(logs.some(log => log.message === 'No OLAF installations found'), true);
        });

        it('should construct correct confirmation message', async () => {
            // Arrange
            const installedScopes = ['user', 'workspace'];
            mockInstallationManager.setMockScopes(installedScopes);
            let warningMessageCalled = false;
            let messageContent = '';

            (vscode.window as any).showWarningMessage = async (message: string) => {
                warningMessageCalled = true;
                messageContent = message;
                return 'Cancel'; // User cancels
            };

            // Act
            await uninstallCommand.executeUninstallAll();

            // Assert
            assert.strictEqual(warningMessageCalled, true);
            const expectedMessage = 'Are you sure you want to uninstall OLAF from ALL scopes (user, workspace)? This will remove all recorded files and cannot be undone.';
            assert.strictEqual(messageContent, expectedMessage);
        });
    });

    describe('showRemovalPreview', () => {
        it('should show message when no files are found', async () => {
            // Arrange
            mockInstallationManager.setMockScopes([]);
            let informationMessageCalled = false;
            let messageContent = '';

            (vscode.window as any).showInformationMessage = async (message: string) => {
                informationMessageCalled = true;
                messageContent = message;
                return undefined;
            };

            // Act
            await uninstallCommand.showRemovalPreview();

            // Assert
            assert.strictEqual(informationMessageCalled, true);
            assert.strictEqual(messageContent, 'No OLAF files found to remove.');
        });

        it('should display grouped file preview', async () => {
            // Arrange
            const installedScopes = ['user'];
            mockInstallationManager.setMockScopes(installedScopes);
            mockInstallationManager.setMockInstallationInfo('user', {
                installedFiles: ['olaf-core/file1.txt', 'olaf-core/file2.txt'],
                scope: 'user',
                installedPath: '/home/user/.olaf'
            });

            let informationMessageCalled = false;
            let messageContent = '';

            (vscode.window as any).showInformationMessage = async (message: string) => {
                informationMessageCalled = true;
                messageContent = message;
                return undefined;
            };

            // Act
            await uninstallCommand.showRemovalPreview();

            // Assert
            assert.strictEqual(informationMessageCalled, true);
            assert.strictEqual(messageContent.includes('OLAF Installation Preview'), true);
            assert.strictEqual(messageContent.includes('USER'), true);
            assert.strictEqual(messageContent.includes('2 files'), true);
        });
    });

    describe('Class Construction', () => {
        it('should create instance with dependencies', () => {
            // Arrange & Act
            const command = new UninstallCommand(mockInstallationManager as any, mockLogger as any);

            // Assert
            assert.strictEqual(command !== null, true);
            assert.strictEqual(command !== undefined, true);
        });
    });
});
