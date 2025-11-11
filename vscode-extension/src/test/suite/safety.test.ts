import * as assert from 'assert';
import { OlafUninstaller } from '../../services/olafUninstaller';
import * as fs from 'fs-extra';
import * as path from 'path';
import * as os from 'os';
import * as crypto from 'crypto';
import { FileIntegrityInfo, EnhancedInstallationMetadata } from '../../types/integrityTypes';

describe('🚨 CRITICAL SAFETY Tests', () => {
    let tempDir: string;
    let uninstaller: OlafUninstaller;

    // Helper function to create FileIntegrityInfo from file content
    async function createFileIntegrityInfo(filePath: string, content: string): Promise<FileIntegrityInfo> {
        await fs.writeFile(filePath, content);
        const stats = await fs.stat(filePath);
        const buffer = Buffer.from(content);

        const sha256 = crypto.createHash('sha256').update(buffer).digest('hex');
        let xxhash64: string;

        try {
            // Try BLAKE2b first, fallback to SHA-512 truncated
            const blake2bHash = crypto.createHash('blake2b512').update(buffer).digest('hex');
            xxhash64 = blake2bHash.substring(0, 64);
        } catch {
            // Fallback to SHA-512 truncated if BLAKE2b not available
            const sha512Hash = crypto.createHash('sha512').update(buffer).digest('hex');
            xxhash64 = sha512Hash.substring(0, 64);
        }

        return {
            path: filePath,
            sha256,
            xxhash64,
            size: stats.size,
            mtime: stats.mtime.toISOString(),
            permissions: stats.mode.toString(8),
            isExecutable: !!(stats.mode & fs.constants.S_IXUSR),
            isSymlink: stats.isSymbolicLink(),
            symlinkTarget: stats.isSymbolicLink() ? await fs.readlink(filePath) : undefined
        };
    }

    beforeEach(async () => {
        // Create a temporary directory that looks like a real workspace
        tempDir = await fs.mkdtemp(path.join(os.tmpdir(), 'olaf-safety-test-'));

        // Create fake workspace structure with .git, node_modules, user files
        await fs.ensureDir(path.join(tempDir, '.git', 'objects'));
        await fs.ensureDir(path.join(tempDir, 'node_modules'));
        await fs.writeFile(path.join(tempDir, '.git', 'HEAD'), 'ref: refs/heads/main');
        await fs.writeFile(path.join(tempDir, 'important-user-file.txt'), 'CRITICAL USER DATA');
        await fs.writeFile(path.join(tempDir, 'node_modules', 'some-module.js'), 'module content');

        uninstaller = new OlafUninstaller();
    });

    afterEach(async () => {
        if (tempDir && await fs.pathExists(tempDir)) {
            await fs.remove(tempDir);
        }
    });

    it('🚨 MUST NEVER scan workspace without metadata - prevents .git deletion', async () => {
        // This is the catastrophic bug that was found - uninstaller scanning entire workspace
        // when no metadata exists, including .git directory
        
        // This should return an error result instead of proceeding
        const result = await uninstaller.uninstall({
            type: 'complete',
            targetDir: tempDir, // This is a workspace directory with .git, user files, etc.
            createBackup: false
            // NO METADATA - this was causing directory scanning!
        });
        
        // Verify the safety check worked
        assert.ok(!result.success, 'Uninstall should fail without metadata');
        assert.ok(result.errors.length > 0, 'Should have error messages');
        assert.ok(result.errors.some(err => err.includes('SAFETY ERROR')), 'Should have safety error');
        assert.ok(result.errors.some(err => err.includes('metadata')), 'Should mention metadata requirement');
        
        // Verify that NO files were deleted
        assert.ok(await fs.pathExists(path.join(tempDir, '.git', 'HEAD')), '.git directory should be untouched');
        assert.ok(await fs.pathExists(path.join(tempDir, 'important-user-file.txt')), 'User files should be untouched');
        assert.ok(await fs.pathExists(path.join(tempDir, 'node_modules', 'some-module.js')), 'node_modules should be untouched');
    });
    
    it('🚨 MUST NEVER proceed with smart uninstall without metadata', async () => {
        // Smart uninstall was the specific mode that triggered workspace scanning
        
        const result = await uninstaller.uninstall({
            type: 'smart',
            targetDir: tempDir,
            createBackup: true
            // NO METADATA
        });
        
        // Verify safety check worked
        assert.ok(!result.success, 'Smart uninstall should fail without metadata');
        assert.ok(result.errors.some(err => err.includes('SAFETY ERROR')), 'Should have safety error');
        
        // All files must remain untouched
        assert.ok(await fs.pathExists(path.join(tempDir, '.git', 'HEAD')));
        assert.ok(await fs.pathExists(path.join(tempDir, 'important-user-file.txt')));
    });
    
    it('✅ Should work normally WITH valid metadata', async () => {
        // Create minimal metadata
        const metadataDir = path.join(tempDir, '.olaf');
        await fs.ensureDir(metadataDir);

        const testFile = path.join(metadataDir, 'test-olaf-file.txt');
        const testFileInfo = await createFileIntegrityInfo(testFile, 'test content');

        const metadata = {
            version: '1.0.0',
            platform: 'test',
            scope: 'workspace',
            installedAt: new Date().toISOString(),
            osplatform: 'test',
            bundleInfo: {
                filename: 'test-bundle.zip',
                size: 1024,
                platform: 'test',
                sha256: 'test-sha256',
                manifestVersion: '1.0.0'
            },
            originalFiles: [testFileInfo],
            extractionPath: metadataDir,
            integrityVersion: '1.0.0',
            verificationPolicy: {
                autoVerify: true,
                preserveModified: true,
                preserveUserCreated: true,
                reportModifications: true
            },
            rollbackSupported: false
        };
        
        const result = await uninstaller.uninstall({
            type: 'complete',
            targetDir: tempDir,
            createBackup: false,
            metadata: metadata
        });
        
        // Should work fine with metadata
        assert.ok(result.success);
        assert.ok(!await fs.pathExists(testFile), 'OLAF file should be removed');
        
        // But other files should be untouched
        assert.ok(await fs.pathExists(path.join(tempDir, '.git', 'HEAD')), '.git should be untouched');
        assert.ok(await fs.pathExists(path.join(tempDir, 'important-user-file.txt')), 'User files should be untouched');
    });
});
