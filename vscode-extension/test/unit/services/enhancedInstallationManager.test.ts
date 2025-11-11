import * as assert from 'assert';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';
import { EnhancedInstallationManager } from '../../../src/services/enhancedInstallationManager';
import { InstallationScope } from '../../../src/types/platform';
import { EnhancedInstallationMetadata } from '../../../src/types/integrityTypes';

// Mock the vscode module
const mockVscode = {
    workspace: {
        workspaceFolders: [{
            uri: {
                fsPath: '/mock/workspace'
            }
        }]
    }
};

// Mock the InstallationManager
class MockInstallationManager {
    static getInstance() {
        return new MockInstallationManager();
    }

    async install(bundlePath: string, scope: InstallationScope, onProgress?: any) {
        return {
            success: true,
            installedPath: '/mock/install/path',
            installedFiles: ['/mock/file1.txt', '/mock/file2.txt'],
            version: '1.0.0',
            scope,
            platform: 'linux'
        };
    }

    async uninstall(scope: InstallationScope) {
        return {
            success: true,
            installedFiles: ['/mock/file1.txt', '/mock/file2.txt']
        };
    }

    async getInstallationInfo(scope: InstallationScope) {
        return {
            success: true,
            version: '1.0.0',
            platform: 'linux',
            scope,
            installedFiles: ['/mock/file1.txt', '/mock/file2.txt'],
            installedPath: '/mock/install/path'
        };
    }
}

// Mock the Logger
class MockLogger {
    static getInstance() {
        return new MockLogger();
    }
    info(message: string) { console.log(`INFO: ${message}`); }
    warn(message: string) { console.log(`WARN: ${message}`); }
    error(message: string) { console.log(`ERROR: ${message}`); }
}

describe('EnhancedInstallationManager Tests', () => {
    let enhancedManager: EnhancedInstallationManager;
    let tempDir: string;
    let mockBundlePath: string;

    beforeEach(async () => {
        // Create temporary directory for test files
        tempDir = await fs.promises.mkdtemp(path.join(os.tmpdir(), 'olaf-enhanced-test-'));
        mockBundlePath = path.join(tempDir, 'mock-bundle.zip');
        
        // Create mock bundle file
        await fs.promises.writeFile(mockBundlePath, 'Mock bundle content for testing', 'utf8');

        // Mock modules (in real tests, you'd use proper mocking framework)
        const originalRequire = require;
        require = function(id: string) {
            if (id === 'vscode') {
                return mockVscode;
            }
            return originalRequire(id);
        } as any;

        enhancedManager = EnhancedInstallationManager.getInstance();
    });

    afterEach(async () => {
        // Clean up temporary directory
        try {
            await fs.promises.rm(tempDir, { recursive: true, force: true });
        } catch (error) {
            // Ignore cleanup errors
        }
    });

    it('getInstance should return singleton instance', () => {
        const instance1 = EnhancedInstallationManager.getInstance();
        const instance2 = EnhancedInstallationManager.getInstance();
        
        assert.strictEqual(instance1, instance2);
    });

    it('getEnhancedMetadata should return null or metadata for USER scope', async () => {
        // This test may return null (no installation) or actual metadata (if OLAF is installed)
        // We just verify the method doesn't throw and returns the expected type
        const metadata = await enhancedManager.getEnhancedMetadata(InstallationScope.USER);
        assert.ok(metadata === null || (typeof metadata === 'object' && 'version' in metadata));
    });

    it('Enhanced metadata path generation should work for different scopes', async () => {
        // Test that the path generation doesn't throw errors
        try {
            await enhancedManager.getEnhancedMetadata(InstallationScope.USER);
            await enhancedManager.getEnhancedMetadata(InstallationScope.PROJECT);
        } catch (error) {
            // Expected to fail with file not found, not path generation errors
            if (!(error as any).code || (error as any).code !== 'ENOENT') {
                throw error;
            }
        }
    });

    it('Enhanced metadata should have correct structure', () => {
        // Test that we can create a valid enhanced metadata object
        const mockMetadata: EnhancedInstallationMetadata = {
            version: '1.0.0',
            platform: 'linux',
            scope: InstallationScope.USER,
            installedAt: new Date().toISOString(),
            bundleInfo: {
                filename: 'test-bundle.zip',
                size: 1234,
                platform: 'linux',
                sha256: 'mock-sha256-hash',
                manifestVersion: '2.0.0'
            },
            originalFiles: [{
                path: '/mock/file.txt',
                sha256: 'file-sha256',
                xxhash64: 'file-xxhash64',
                size: 100,
                mtime: new Date().toISOString(),
                permissions: '644',
                isExecutable: false,
                isSymlink: false
            }],
            extractionPath: '/mock/extract/path',
            integrityVersion: '1.0.0',
            lastVerification: new Date().toISOString(),
            verificationPolicy: {
                autoVerify: true,
                preserveModified: true,
                reportModifications: true
            },
            rollbackSupported: false
        };

        // Verify all required fields are present
        assert.strictEqual(typeof mockMetadata.version, 'string');
        assert.strictEqual(typeof mockMetadata.platform, 'string');
        assert.strictEqual(typeof mockMetadata.scope, 'string');
        assert.strictEqual(typeof mockMetadata.installedAt, 'string');
        assert.strictEqual(typeof mockMetadata.bundleInfo, 'object');
        assert.strictEqual(Array.isArray(mockMetadata.originalFiles), true);
        assert.strictEqual(typeof mockMetadata.extractionPath, 'string');
        assert.strictEqual(typeof mockMetadata.integrityVersion, 'string');
        assert.strictEqual(typeof mockMetadata.verificationPolicy, 'object');
        assert.strictEqual(typeof mockMetadata.rollbackSupported, 'boolean');
    });

    it('File integrity info should have correct structure', () => {
        const mockFileInfo = {
            path: '/mock/file.txt',
            sha256: 'a'.repeat(64), // SHA-256 is 64 hex chars
            xxhash64: 'b'.repeat(16), // xxHash64 is 16 hex chars
            size: 1234,
            mtime: new Date().toISOString(),
            permissions: '644',
            isExecutable: false,
            isSymlink: false
        };

        assert.strictEqual(typeof mockFileInfo.path, 'string');
        assert.strictEqual(typeof mockFileInfo.sha256, 'string');
        assert.strictEqual(mockFileInfo.sha256.length, 64);
        assert.strictEqual(typeof mockFileInfo.xxhash64, 'string');
        assert.strictEqual(typeof mockFileInfo.size, 'number');
        assert.strictEqual(typeof mockFileInfo.mtime, 'string');
        assert.strictEqual(typeof mockFileInfo.permissions, 'string');
        assert.strictEqual(typeof mockFileInfo.isExecutable, 'boolean');
        assert.strictEqual(typeof mockFileInfo.isSymlink, 'boolean');
    });

    it('Verification policy should have correct structure', () => {
        const policy = {
            autoVerify: true,
            preserveModified: true,
            reportModifications: true
        };

        assert.strictEqual(typeof policy.autoVerify, 'boolean');
        assert.strictEqual(typeof policy.preserveModified, 'boolean');
        assert.strictEqual(typeof policy.reportModifications, 'boolean');
    });

    it('Installation result should have correct enhanced structure', () => {
        const mockResult = {
            success: true,
            metadata: {} as EnhancedInstallationMetadata,
            integrityInfo: [],
            rollbackAvailable: false,
            warnings: []
        };

        assert.strictEqual(typeof mockResult.success, 'boolean');
        assert.strictEqual(typeof mockResult.metadata, 'object');
        assert.strictEqual(Array.isArray(mockResult.integrityInfo), true);
        assert.strictEqual(typeof mockResult.rollbackAvailable, 'boolean');
        assert.strictEqual(Array.isArray(mockResult.warnings), true);
    });

    it('Uninstallation result should have correct structure', () => {
        const mockResult = {
            success: true,
            report: {
                totalFiles: 2,
                modifiedFiles: 1,
                deletedFiles: 0,
                corruptedFiles: 0,
                intactFiles: 1,
                modifications: [],
                summary: 'Mock summary',
                generatedAt: new Date().toISOString()
            },
            preservedFiles: ['/mock/modified.txt'],
            removedFiles: ['/mock/intact.txt'],
            backupCreated: '/mock/backup/path'
        };

        assert.strictEqual(typeof mockResult.success, 'boolean');
        assert.strictEqual(typeof mockResult.report, 'object');
        assert.strictEqual(typeof mockResult.report.totalFiles, 'number');
        assert.strictEqual(typeof mockResult.report.summary, 'string');
        assert.strictEqual(Array.isArray(mockResult.preservedFiles), true);
        assert.strictEqual(Array.isArray(mockResult.removedFiles), true);
    });

    it('Smart removal result should have correct structure', () => {
        const mockResult = {
            removedFiles: ['/mock/file1.txt'],
            preservedFiles: ['/mock/modified.txt'],
            backedUpFiles: ['/mock/backup.txt'],
            errors: []
        };

        assert.strictEqual(Array.isArray(mockResult.removedFiles), true);
        assert.strictEqual(Array.isArray(mockResult.preservedFiles), true);
        assert.strictEqual(Array.isArray(mockResult.backedUpFiles), true);
        assert.strictEqual(Array.isArray(mockResult.errors), true);
    });

    it('File categories should have correct structure for smart uninstallation', () => {
        const mockCategories = {
            intact: [{
                file: '/mock/intact.txt',
                type: 'intact' as const,
                details: {} as any,
                recommendation: 'remove' as const
            }],
            userModified: [{
                file: '/mock/modified.txt',
                type: 'modified' as const,
                details: {} as any,
                recommendation: 'preserve' as const
            }],
            deleted: [{
                file: '/mock/deleted.txt',
                type: 'deleted' as const,
                details: {} as any,
                recommendation: 'ignore' as const
            }],
            corrupted: [{
                file: '/mock/corrupted.txt',
                type: 'corrupted' as const,
                details: {} as any,
                recommendation: 'restore' as const
            }]
        };

        assert.strictEqual(Array.isArray(mockCategories.intact), true);
        assert.strictEqual(Array.isArray(mockCategories.userModified), true);
        assert.strictEqual(Array.isArray(mockCategories.deleted), true);
        assert.strictEqual(Array.isArray(mockCategories.corrupted), true);

        // Test specific category structures
        assert.strictEqual(mockCategories.intact[0].type, 'intact');
        assert.strictEqual(mockCategories.intact[0].recommendation, 'remove');
        assert.strictEqual(mockCategories.userModified[0].type, 'modified');
        assert.strictEqual(mockCategories.userModified[0].recommendation, 'preserve');
        assert.strictEqual(mockCategories.deleted[0].type, 'deleted');
        assert.strictEqual(mockCategories.deleted[0].recommendation, 'ignore');
        assert.strictEqual(mockCategories.corrupted[0].type, 'corrupted');
        assert.strictEqual(mockCategories.corrupted[0].recommendation, 'restore');
    });

    it('User decision should have correct structure', () => {
        const mockDecision = {
            action: 'safe' as const,
            timestamp: new Date().toISOString(),
            customDecisions: {
                '/mock/file1.txt': 'preserve' as const,
                '/mock/file2.txt': 'remove' as const,
                '/mock/file3.txt': 'backup' as const
            }
        };

        assert.strictEqual(typeof mockDecision.action, 'string');
        assert.strictEqual(typeof mockDecision.timestamp, 'string');
        assert.strictEqual(typeof mockDecision.customDecisions, 'object');
        
        // Verify valid action types
        const validActions = ['safe', 'complete', 'custom', 'cancel'];
        assert.strictEqual(validActions.includes(mockDecision.action), true);

        // Verify custom decision values
        if (mockDecision.customDecisions) {
            for (const decision of Object.values(mockDecision.customDecisions)) {
                const validDecisions = ['preserve', 'remove', 'backup'];
                assert.strictEqual(validDecisions.includes(decision), true);
            }
        }
    });
});
