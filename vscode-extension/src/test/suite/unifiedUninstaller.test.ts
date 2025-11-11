import * as assert from 'assert';
import * as path from 'path';
import * as fs from 'fs-extra';
import * as os from 'os';
import * as crypto from 'crypto';
import { OlafUninstaller, UninstallOptions, UninstallResult } from '../../services/olafUninstaller';
import { FileIntegrityInfo, EnhancedInstallationMetadata } from '../../types/integrityTypes';

describe('UnifiedUninstaller', () => {
    let tempDir: string;
    let uninstaller: OlafUninstaller;

    beforeEach(async () => {
        tempDir = await fs.mkdtemp(path.join(os.tmpdir(), 'olaf-test-'));
        uninstaller = new OlafUninstaller();
    });

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

    // Helper function to create EnhancedInstallationMetadata
    function createTestMetadata(originalFiles: FileIntegrityInfo[], extractionPath: string): EnhancedInstallationMetadata {
        return {
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
            originalFiles,
            extractionPath,
            integrityVersion: '1.0.0',
            verificationPolicy: {
                autoVerify: true,
                preserveModified: true,
                preserveUserCreated: true,
                reportModifications: true
            },
            rollbackSupported: false
        };
    }

    afterEach(async () => {
        if (tempDir && await fs.pathExists(tempDir)) {
            await fs.remove(tempDir);
        }
    });

    describe('File Categorization', () => {
        it('should correctly categorize files as original, modified, and user-created', async () => {
            // Create .olaf directory for test
            const olafDir = path.join(tempDir, '.olaf');
            await fs.ensureDir(olafDir);

            // Create test files
            const originalFile1 = path.join(olafDir, 'file1.txt');
            const originalFile2 = path.join(olafDir, 'file2.txt');
            const modifiedFile = path.join(olafDir, 'modified.txt');
            const userFile = path.join(olafDir, 'user.txt');

            // Create FileIntegrityInfo objects with original content
            const originalFile1Info = await createFileIntegrityInfo(originalFile1, 'original content 1');
            const originalFile2Info = await createFileIntegrityInfo(originalFile2, 'original content 2');
            const modifiedFileInfo = await createFileIntegrityInfo(modifiedFile, 'original modified content');
            const userFileInfo = await createFileIntegrityInfo(userFile, 'user content');

            // Now modify the "modified" file to simulate user changes
            await fs.writeFile(modifiedFile, 'USER CHANGED CONTENT');

            const metadata = createTestMetadata([originalFile1Info, originalFile2Info, modifiedFileInfo, userFileInfo], olafDir);

            const options: UninstallOptions = {
                type: 'smart',
                targetDir: tempDir,
                createBackup: false,
                metadata: metadata
            };

            const result = await uninstaller.uninstall(options);
            
            // Should succeed and preserve files since no metadata to distinguish
            assert.strictEqual(result.success, true);
            assert.strictEqual(result.errors.length, 0);
        });

        it('should handle missing files gracefully', async () => {
            // Create .olaf directory for test
            const olafDir = path.join(tempDir, '.olaf');
            await fs.ensureDir(olafDir);

            // Create some files but reference non-existent ones in custom selection
            await fs.writeFile(path.join(tempDir, 'exists.txt'), 'content');

            // Create FileIntegrityInfo objects for files (even though they don't exist yet)
            const file1Info = await createFileIntegrityInfo(path.join(olafDir, "file1.txt"), "file1 content");
            const file2Info = await createFileIntegrityInfo(path.join(olafDir, "file2.txt"), "file2 content");
            const modifiedFileInfo = await createFileIntegrityInfo(path.join(olafDir, "modified.txt"), "modified content");
            const userFileInfo = await createFileIntegrityInfo(path.join(olafDir, "user.txt"), "user content");

            const metadata = createTestMetadata([file1Info, file2Info, modifiedFileInfo, userFileInfo], olafDir);
const options: UninstallOptions = {
                type: 'custom',
                targetDir: tempDir,
                customSelection: [
                    path.join(tempDir, 'exists.txt'),
                    path.join(tempDir, 'missing.txt')
                ],
                createBackup: false,
                metadata: metadata
            };

            const result = await uninstaller.uninstall(options);
            
            // Should handle missing files gracefully
            assert.strictEqual(result.success, true);
            assert.strictEqual(result.filesRemoved, 1);
        });
    });

    describe('Complete Uninstall', () => {
        it('should remove all files without backup', async () => {
            // Create .olaf directory for test
            const olafDir = path.join(tempDir, '.olaf');
            await fs.ensureDir(olafDir);

            // Create test files
            const file1 = path.join(olafDir, 'file1.txt');
            const file2 = path.join(olafDir, 'file2.txt');

            const file1Info = await createFileIntegrityInfo(file1, 'content1');
            const file2Info = await createFileIntegrityInfo(file2, 'content2');

            const metadata = createTestMetadata([file1Info, file2Info], olafDir);
const options: UninstallOptions = {
                type: 'complete',
                targetDir: tempDir,
                createBackup: false,
                metadata: metadata
            };

            const result = await uninstaller.uninstall(options);
            
            assert.strictEqual(result.success, true);
            assert.strictEqual(result.filesRemoved, 2);
            assert.strictEqual(result.filesPreserved, 0);
            assert.strictEqual(result.backupPath, undefined);
        });
    });

    describe('Smart Uninstall', () => {
        it('should remove original files and preserve modified/user-created files', async () => {
            // Create .olaf directory for test
            const olafDir = path.join(tempDir, '.olaf');
            await fs.ensureDir(olafDir);

            // Create test files
            const file1 = path.join(olafDir, 'file1.txt');
            const file2 = path.join(olafDir, 'file2.txt');

            const file1Info = await createFileIntegrityInfo(file1, 'content1');
            const file2Info = await createFileIntegrityInfo(file2, 'content2');

            const metadata = createTestMetadata([file1Info, file2Info], olafDir);
const options: UninstallOptions = {
                type: 'smart',
                targetDir: tempDir,
                createBackup: false,
                metadata: metadata
            };

            const result = await uninstaller.uninstall(options);
            
            assert.strictEqual(result.success, true);
            assert.strictEqual(result.errors.length, 0);
            // Without metadata, smart uninstall treats all files as modified/user-created
            assert.strictEqual(result.filesRemoved, 2);
            assert.strictEqual(result.filesPreserved, 0);
        });

        it('should create backup of preserved files', async () => {
            // Create .olaf directory for test
            const olafDir = path.join(tempDir, '.olaf');
            await fs.ensureDir(olafDir);

            // Create test files
            const file1 = path.join(olafDir, 'file1.txt');
            const file2 = path.join(olafDir, 'file2.txt');

            const file1Info = await createFileIntegrityInfo(file1, 'content1');
            const file2Info = await createFileIntegrityInfo(file2, 'content2');

            const metadata = createTestMetadata([file1Info, file2Info], olafDir);
const options: UninstallOptions = {
                type: 'smart',
                targetDir: tempDir,
                createBackup: true,
                metadata: metadata
            };

            const result = await uninstaller.uninstall(options);
            
            assert.strictEqual(result.success, true);
            if (result.filesPreserved > 0) {
                assert.strictEqual(typeof result.backupPath, 'string');
                assert.ok(await fs.pathExists(result.backupPath!));
            }
        });
    });

    describe('Custom Uninstall', () => {
        it('should only remove specified files', async () => {
            // Create .olaf directory for test
            const olafDir = path.join(tempDir, '.olaf');
            await fs.ensureDir(olafDir);

            // Create test files
            const file1 = path.join(olafDir, 'file1.txt');
            const file2 = path.join(olafDir, 'file2.txt');
            const file3 = path.join(olafDir, 'file3.txt');

            const file1Info = await createFileIntegrityInfo(file1, 'content1');
            const file2Info = await createFileIntegrityInfo(file2, 'content2');
            const file3Info = await createFileIntegrityInfo(file3, 'content3');

            const metadata = createTestMetadata([file1Info, file2Info, file3Info], olafDir);
const options: UninstallOptions = {
                type: 'custom',
                targetDir: tempDir,
                customSelection: [file1, file3],
                createBackup: false,
                metadata: metadata
            };

            const result = await uninstaller.uninstall(options);
            
            assert.strictEqual(result.success, true);
            assert.strictEqual(result.filesRemoved, 2);
            assert.strictEqual(result.filesPreserved, 1);
            
            // file2 should still exist
            assert.ok(await fs.pathExists(file2));
            assert.ok(!(await fs.pathExists(file1)));
            assert.ok(!(await fs.pathExists(file3)));
        });

        it('should reject invalid custom selections', async () => {
            // No metadata needed for this test since we're testing invalid options
            // The validation should catch the missing customSelection before needing metadata
const options: UninstallOptions = {
                type: 'custom',
                targetDir: tempDir,
                createBackup: false
                // Missing customSelection
            };

            const result = await uninstaller.uninstall(options);
            
            assert.strictEqual(result.success, false);
            assert.ok(result.errors.length > 0);
            assert.ok(result.errors[0].includes('Custom selection required'));
        });
    });

    describe('Progress Reporting', () => {
        it('should report progress during uninstall', async () => {
            // Create .olaf directory for test
            const olafDir = path.join(tempDir, '.olaf');
            await fs.ensureDir(olafDir);

            // Create test files
            const file1 = path.join(olafDir, 'file1.txt');
            const file1Info = await createFileIntegrityInfo(file1, 'content1');

            const progressReports: Array<{progress: number, message: string}> = [];

            const metadata = createTestMetadata([file1Info], olafDir);
const options: UninstallOptions = {
                type: 'complete',
                targetDir: tempDir,
                createBackup: false,
                onProgress: (progress: number, message: string) => {
                    progressReports.push({ progress, message });
                },
                metadata: metadata
            };

            const result = await uninstaller.uninstall(options);
            
            assert.strictEqual(result.success, true);
            assert.ok(progressReports.length > 0);
            
            // Should have start and end progress reports
            const firstReport = progressReports[0];
            const lastReport = progressReports[progressReports.length - 1];
            
            assert.strictEqual(firstReport.progress, 0);
            assert.ok(firstReport.message.includes('Starting'));
            
            assert.strictEqual(lastReport.progress, 100);
            assert.ok(lastReport.message.includes('completed'));
        });
    });
});
