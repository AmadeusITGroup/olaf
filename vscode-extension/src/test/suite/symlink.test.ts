import * as assert from 'assert';
import * as fs from 'fs-extra';
import * as path from 'path';
import * as os from 'os';
import { OlafUninstaller, FileCategory } from '../../services/olafUninstaller';
import { FileIntegrityInfo } from '../../types/integrityTypes';

describe('Symbolic Link Resolution Tests', () => {
    let tempDir: string;
    let uninstaller: OlafUninstaller;
    let actualFileDir: string;
    let symlinkDir: string;

    beforeEach(async () => {
        tempDir = await fs.mkdtemp(path.join(os.tmpdir(), 'olaf-symlink-test-'));
        uninstaller = new OlafUninstaller();

        // Create directories for testing
        actualFileDir = path.join(tempDir, 'actual-files');
        symlinkDir = path.join(tempDir, '.olaf');

        await fs.ensureDir(actualFileDir);
        await fs.ensureDir(symlinkDir);
    });

    afterEach(async () => {
        if (tempDir && await fs.pathExists(tempDir)) {
            await fs.remove(tempDir);
        }
    });

    it('should resolve file symbolic links to actual paths', async () => {
        // Create an actual file
        const actualFile = path.join(actualFileDir, 'real-file.txt');
        await fs.writeFile(actualFile, 'real content');

        // Create a symbolic link to the actual file
        const symlinkFile = path.join(symlinkDir, 'symlink-file.txt');
        await fs.symlink(actualFile, symlinkFile);

        // Use reflection to access the private scanDirectory method
        const scanDirectory = (uninstaller as any).scanDirectory.bind(uninstaller);
        const files = await scanDirectory(symlinkDir);

        // Should find one file with the resolved path
        assert.strictEqual(files.length, 1);
        // On macOS, fs.realpath() may resolve temp paths with /private prefix
        const expectedPath = await fs.realpath(actualFile);
        assert.strictEqual(files[0].path, expectedPath); // Should be resolved to actual file path
        assert.strictEqual(files[0].category, 'original');
        assert.ok(files[0].size > 0);
    });

    it('should resolve directory symbolic links to actual paths', async () => {
        // Create an actual directory with a file
        const actualDir = path.join(actualFileDir, 'real-dir');
        await fs.ensureDir(actualDir);
        const actualFile = path.join(actualDir, 'file-in-dir.txt');
        await fs.writeFile(actualFile, 'content in dir');

        // Create a symbolic link to the actual directory
        const symlinkDirPath = path.join(symlinkDir, 'symlink-dir');
        await fs.symlink(actualDir, symlinkDirPath);

        // Use reflection to access the private scanDirectory method
        const scanDirectory = (uninstaller as any).scanDirectory.bind(uninstaller);
        const files = await scanDirectory(symlinkDir);

        // Debug logging removed - test is working correctly now

        // Should find one file with the resolved path
        assert.strictEqual(files.length, 1);
        // On macOS, fs.realpath() may resolve temp paths with /private prefix
        const expectedPath = await fs.realpath(actualFile);
        assert.strictEqual(files[0].path, expectedPath); // Should be resolved to actual file path
        assert.strictEqual(files[0].category, 'original');
    });

    it('should handle broken symbolic links gracefully', async () => {
        // Create a symbolic link to a non-existent file
        const nonExistentFile = path.join(actualFileDir, 'non-existent.txt');
        const brokenSymlink = path.join(symlinkDir, 'broken-symlink.txt');
        await fs.symlink(nonExistentFile, brokenSymlink);

        // Also create a valid file for comparison
        const validFile = path.join(symlinkDir, 'valid-file.txt');
        await fs.writeFile(validFile, 'valid content');

        // Use reflection to access the private scanDirectory method
        const scanDirectory = (uninstaller as any).scanDirectory.bind(uninstaller);
        const files = await scanDirectory(symlinkDir);

        // Should find the valid file, broken symlink should be skipped
        assert.strictEqual(files.length, 1);
        // Handle path resolution differences on macOS
        const expectedValidPath = await fs.realpath(validFile);
        assert.strictEqual(files[0].path, expectedValidPath);
    });

    it('should handle mixed symbolic links and regular files', async () => {
        // Create a regular file
        const regularFile = path.join(symlinkDir, 'regular.txt');
        await fs.writeFile(regularFile, 'regular content');

        // Create an actual file for symlink
        const actualFile = path.join(actualFileDir, 'target.txt');
        await fs.writeFile(actualFile, 'target content');

        // Create a symbolic link
        const symlinkFile = path.join(symlinkDir, 'link.txt');
        await fs.symlink(actualFile, symlinkFile);

        // Use reflection to access the private scanDirectory method
        const scanDirectory = (uninstaller as any).scanDirectory.bind(uninstaller);
        const files = await scanDirectory(symlinkDir);

        // Should find both files
        assert.strictEqual(files.length, 2);

        // Find files by checking if paths end with the expected relative paths
        // This handles macOS path resolution differences (/var vs /private/var)
        const expectedActualPath = await fs.realpath(actualFile);
        const actualFileResult = files.find((f: FileCategory) => f.path === expectedActualPath);

        // For regular files, check if any found file has the same basename and parent structure
        const regularFileBasename = path.basename(regularFile);
        const regularFileResult = files.find((f: FileCategory) => {
            return path.basename(f.path) === regularFileBasename &&
                   f.path.includes('.olaf');
        });

        assert.ok(actualFileResult, `Should find resolved symlink at ${expectedActualPath}`);
        assert.ok(regularFileResult, `Should find regular file with basename ${regularFileBasename} in .olaf directory`);
    });

    it('should resolve paths when .olaf directory itself is a symbolic link', async () => {
        // Create a real .olaf directory structure somewhere else
        const realOlafDir = path.join(actualFileDir, 'real-olaf');
        await fs.ensureDir(realOlafDir);

        // Create a file in the real .olaf directory
        const realFile = path.join(realOlafDir, '.olaf-enhanced-metadata.json');
        await fs.writeFile(realFile, '{"test": "data"}');

        // Create a symbolic link from symlinkDir/.olaf to the real .olaf directory
        const symlinkOlafDir = path.join(symlinkDir, '.olaf');
        await fs.symlink(realOlafDir, symlinkOlafDir);

        // This simulates the user's scenario: .olaf directory is a symlink

        // Use reflection to access the private categorizeFiles method
        const categorizeFiles = (uninstaller as any).categorizeFiles.bind(uninstaller);

        // Create minimal metadata for the test
        const testFileInfo: FileIntegrityInfo = {
            path: path.join(realOlafDir, '.olaf-enhanced-metadata.json'),
            sha256: 'test-sha256',
            xxhash64: 'test-xxhash64',
            size: 17,
            mtime: new Date().toISOString(),
            permissions: '644',
            isExecutable: false,
            isSymlink: false
        };

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
            extractionPath: realOlafDir,
            integrityVersion: '1.0.0',
            verificationPolicy: {
                autoVerify: true,
                preserveModified: true,
                preserveUserCreated: true,
                reportModifications: true
            },
            rollbackSupported: false
        };

        // Call categorizeFiles with the directory containing the symlinked .olaf
        const result = await categorizeFiles(symlinkDir, metadata);

        // Verify that files were found and their paths were resolved to the real location
        const allFiles = [...result.original, ...result.modified, ...result.userCreated];
        assert.ok(allFiles.length > 0, 'Should find files through the symlinked .olaf directory');

        // The key test: file paths should be resolved to the real location
        const realFilePath = await fs.realpath(realFile);
        const foundFile = allFiles.find((f: FileCategory) => f.path === realFilePath);
        assert.ok(foundFile, `Should find file with resolved path: ${realFilePath}`);
    });

    it('should prevent infinite loops with circular symbolic links', async () => {
        // Create two directories that link to each other
        const dir1 = path.join(symlinkDir, 'dir1');
        const dir2 = path.join(symlinkDir, 'dir2');

        await fs.ensureDir(dir1);
        await fs.ensureDir(dir2);

        // Create circular symlinks
        const link1 = path.join(dir1, 'link-to-dir2');
        const link2 = path.join(dir2, 'link-to-dir1');

        await fs.symlink(dir2, link1);
        await fs.symlink(dir1, link2);

        // Add a regular file to test that scanning still works
        const regularFile = path.join(dir1, 'regular.txt');
        await fs.writeFile(regularFile, 'regular content');

        // Use reflection to access the private scanDirectory method
        const scanDirectory = (uninstaller as any).scanDirectory.bind(uninstaller);

        // This should not hang or throw errors
        const files = await scanDirectory(symlinkDir);

        // Should find at least the regular file
        assert.ok(files.length >= 1);
        // Handle path resolution differences - find files by basename and structure
        const expectedRegularPath = await fs.realpath(regularFile);
        const regularFiles = files.filter((f: FileCategory) => f.path === expectedRegularPath);
        assert.strictEqual(regularFiles.length, 1);
    });
});