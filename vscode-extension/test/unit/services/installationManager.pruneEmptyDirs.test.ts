import * as assert from 'assert';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import { InstallationManager } from '../../../src/services/installationManager';
import { InstallationScope } from '../../../src/types/platform';

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

    debug(message: string, error?: Error): void {
        this.logs.push({ level: 'debug', message, error });
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

/**
 * Mock PlatformDetector for testing
 */
class MockPlatformDetector {
    constructor(private testInstallPath: string) {}

    async detectPlatform() {
        return { platform: 'vscode' };
    }

    getInstallationPath(platform: string, scope: InstallationScope): string {
        return path.join(this.testInstallPath, `.olaf-${scope}`);
    }
}

describe('InstallationManager.pruneEmptyDirs Test Suite', () => {
    let tempDir: string;
    let installationManager: InstallationManager;
    let mockLogger: MockLogger;
    let mockPlatformDetector: MockPlatformDetector;

    beforeEach(async () => {
        // Create temporary directory for testing
        tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'olaf-test-'));
        
        // Create mocks
        mockLogger = new MockLogger();
        mockPlatformDetector = new MockPlatformDetector(tempDir);
        
        // Create installation manager instance with mocks
        installationManager = InstallationManager.getInstance();
        (installationManager as any).logger = mockLogger;
        (installationManager as any).platformDetector = mockPlatformDetector;
    });

    afterEach(async () => {
        // Clean up temporary directory
        if (fs.existsSync(tempDir)) {
            await fs.promises.rm(tempDir, { recursive: true });
        }
    });

    describe('pruneEmptyDirs - Directory Structure Cleanup', () => {
        it('should remove empty directories after file removal', async () => {
            // Arrange - create test structure
            const installPath = path.join(tempDir, '.olaf-user');
            const extractionPath = path.join(tempDir, 'extracted');
            
            // Create directory structure
            const nestedDir = path.join(extractionPath, 'olaf-core', 'deep', 'nested');
            await fs.promises.mkdir(nestedDir, { recursive: true });
            await fs.promises.mkdir(installPath, { recursive: true });
            
            // Create metadata file
            const metadata = {
                installedFiles: ['olaf-core/deep/nested/file.txt', 'olaf-core/another.txt'],
                extractionPath: extractionPath,
                scope: 'user',
                version: '1.0.0',
                platform: 'vscode'
            };
            const metadataDir = path.join(installPath, '.olaf');
            await fs.promises.mkdir(metadataDir, { recursive: true });
            await fs.promises.writeFile(
                path.join(metadataDir, '.olaf-metadata.json'),
                JSON.stringify(metadata, null, 2)
            );

            // Act - call pruneEmptyDirs (files should already be removed)
            await installationManager.pruneEmptyDirs(InstallationScope.USER);

            // Assert - empty directories should be removed
            assert.strictEqual(fs.existsSync(nestedDir), false, 'Nested directory should be removed');
            assert.strictEqual(fs.existsSync(path.join(extractionPath, 'olaf-core', 'deep')), false, 'Deep directory should be removed');
            assert.strictEqual(fs.existsSync(path.join(extractionPath, 'olaf-core')), false, 'olaf-core directory should be removed');
            assert.strictEqual(fs.existsSync(extractionPath), false, 'Extraction path should be removed if empty');
            
            // Verify logging
            const logs = mockLogger.getLogs();
            const removedDirLogs = logs.filter(log => log.message.includes('Removed empty') && log.message.includes('directory'));
            assert.strictEqual(removedDirLogs.length > 0, true, 'Should log removed directories');
        });

        it('should not remove directories that contain other files', async () => {
            // Arrange - create test structure with some files remaining
            const installPath = path.join(tempDir, '.olaf-user');
            const extractionPath = path.join(tempDir, 'extracted');
            
            // Create directory structure
            const nestedDir = path.join(extractionPath, 'olaf-core', 'deep');
            await fs.promises.mkdir(nestedDir, { recursive: true });
            await fs.promises.mkdir(installPath, { recursive: true });
            
            // Create a file that should remain
            const remainingFile = path.join(extractionPath, 'olaf-core', 'remaining.txt');
            await fs.promises.writeFile(remainingFile, 'This file should remain');
            
            // Create metadata file
            const metadata = {
                installedFiles: ['olaf-core/deep/file.txt'], // Only one file was installed
                extractionPath: extractionPath,
                scope: 'user',
                version: '1.0.0',
                platform: 'vscode'
            };
            const metadataDir = path.join(installPath, '.olaf');
            await fs.promises.mkdir(metadataDir, { recursive: true });
            await fs.promises.writeFile(
                path.join(metadataDir, '.olaf-metadata.json'),
                JSON.stringify(metadata, null, 2)
            );

            // Act
            await installationManager.pruneEmptyDirs(InstallationScope.USER);

            // Assert - directories containing other files should remain
            assert.strictEqual(fs.existsSync(nestedDir), false, 'Empty nested directory should be removed');
            assert.strictEqual(fs.existsSync(path.join(extractionPath, 'olaf-core')), true, 'olaf-core directory should remain (has remaining file)');
            assert.strictEqual(fs.existsSync(extractionPath), true, 'Extraction path should remain');
            assert.strictEqual(fs.existsSync(remainingFile), true, 'Remaining file should not be touched');
            
            // Verify appropriate logging
            const logs = mockLogger.getLogs();
            const keptDirLogs = logs.filter(log => log.message.includes('not empty, keeping'));
            assert.strictEqual(keptDirLogs.length > 0, true, 'Should log kept directories');
        });

        it('should handle metadata directory removal when separate from extraction', async () => {
            // Arrange - metadata directory separate from extraction
            const installPath = path.join(tempDir, '.olaf-user');
            const extractionPath = path.join(tempDir, 'extracted');
            
            await fs.promises.mkdir(extractionPath, { recursive: true });
            await fs.promises.mkdir(installPath, { recursive: true });
            
            // Create metadata file
            const metadata = {
                installedFiles: [],
                extractionPath: extractionPath,
                scope: 'user',
                version: '1.0.0',
                platform: 'vscode'
            };
            const metadataDir = path.join(installPath, '.olaf');
            await fs.promises.mkdir(metadataDir, { recursive: true });
            await fs.promises.writeFile(
                path.join(metadataDir, '.olaf-metadata.json'),
                JSON.stringify(metadata, null, 2)
            );

            // Act
            await installationManager.pruneEmptyDirs(InstallationScope.USER);

            // Assert - both directories should be removed
            assert.strictEqual(fs.existsSync(extractionPath), false, 'Extraction path should be removed');
            assert.strictEqual(fs.existsSync(installPath), false, 'Installation/metadata path should be removed');
        });

        it('should gracefully handle non-existent installation', async () => {
            // Arrange - no installation exists
            
            // Act
            await installationManager.pruneEmptyDirs(InstallationScope.USER);

            // Assert - should not throw errors
            const logs = mockLogger.getLogs();
            const warningLogs = logs.filter(log => log.level === 'warn' && log.message.includes('No installation found'));
            assert.strictEqual(warningLogs.length, 1, 'Should log warning about missing installation');
        });

        it('should handle corrupted metadata gracefully', async () => {
            // Arrange - create installation with corrupted metadata
            const installPath = path.join(tempDir, '.olaf-user');
            await fs.promises.mkdir(installPath, { recursive: true });
            
            // Create corrupted metadata file
            const metadataDir = path.join(installPath, '.olaf');
            await fs.promises.mkdir(metadataDir, { recursive: true });
            await fs.promises.writeFile(
                path.join(metadataDir, '.olaf-metadata.json'),
                'invalid json content'
            );

            // Act
            await installationManager.pruneEmptyDirs(InstallationScope.USER);

            // Assert - should handle gracefully
            const logs = mockLogger.getLogs();
            const warningLogs = logs.filter(log => log.level === 'warn' && log.message.includes('Could not read installation metadata'));
            assert.strictEqual(warningLogs.length, 1, 'Should log warning about corrupted metadata');
        });
    });

    describe('Helper Methods', () => {
        it('removeIfEmpty should work correctly', async () => {
            // This tests the private method indirectly through the public interface
            // by setting up scenarios that would call it
            
            // Arrange - create empty directory
            const emptyDir = path.join(tempDir, 'empty');
            await fs.promises.mkdir(emptyDir, { recursive: true });
            
            const installPath = path.join(tempDir, '.olaf-user');
            await fs.promises.mkdir(installPath, { recursive: true });
            
            // Create metadata pointing to the empty directory
            const metadata = {
                installedFiles: ['file.txt'], // File that would have been in empty dir
                extractionPath: tempDir,
                scope: 'user',
                version: '1.0.0'
            };
            const metadataDir = path.join(installPath, '.olaf');
            await fs.promises.mkdir(metadataDir, { recursive: true });
            await fs.promises.writeFile(
                path.join(metadataDir, '.olaf-metadata.json'),
                JSON.stringify(metadata, null, 2)
            );

            // Act
            await installationManager.pruneEmptyDirs(InstallationScope.USER);

            // Assert
            const logs = mockLogger.getLogs();
            const removedLogs = logs.filter(log => log.message.includes('Removed empty') && log.message.includes('directory'));
            assert.strictEqual(removedLogs.length > 0, true, 'Should have removed empty directories');
        });
    });
});
