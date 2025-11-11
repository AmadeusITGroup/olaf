import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import * as yauzl from 'yauzl';
import { promisify } from 'util';
import { Platform, InstallationScope } from '../types/platform';
import { BundleInfo } from '../types/github';
import { PlatformDetector } from './platformDetector';
import { Logger } from '../utils/logger';

const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);
const mkdir = promisify(fs.mkdir);
const access = promisify(fs.access);
const unlink = promisify(fs.unlink);
// const rmdir = promisify(fs.rmdir); // Deprecated - using fs.promises.rmdir directly

/**
 * Installation result information
 */
export interface InstallationResult {
    success: boolean;
    installedPath: string;
    installedFiles: string[];
    version: string;
    scope: InstallationScope;
    platform: Platform;
    error?: string;
}

/**
 * Service for managing OLAF component installations
 */
export class InstallationManager {
    private static instance: InstallationManager;
    private readonly logger: Logger;
    private readonly platformDetector: PlatformDetector;

    private constructor() {
        this.logger = Logger.getInstance();
        this.platformDetector = PlatformDetector.getInstance();
    }

    public static getInstance(): InstallationManager {
        if (!InstallationManager.instance) {
            InstallationManager.instance = new InstallationManager();
        }
        return InstallationManager.instance;
    }

    /**
     * Install OLAF components from a bundle
     */
    public async installBundle(
        bundleBuffer: Buffer,
        bundleInfo: BundleInfo,
        scope: InstallationScope,
        onProgress?: (progress: number, message: string) => void
    ): Promise<InstallationResult> {
        try {
            this.logger.info(`Starting installation of ${bundleInfo.filename} with scope: ${scope}`);

            const platform = await this.platformDetector.detectPlatform();
            
            // For project scope, extract files to project root; for others use the standard path
            const extractionPath = scope === InstallationScope.PROJECT 
                ? vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || ''
                : this.platformDetector.getInstallationPath(platform.platform, scope);
            const dotOlafPath = path.join(extractionPath, ".olaf");

            // Update progress
            onProgress?.(10, 'Preparing installation directory...');

            // Ensure metadata directory exists
            await this.ensureDirectoryExists(extractionPath);
            
            // Update progress
            onProgress?.(20, 'Extracting bundle...');

            // Extract bundle to the appropriate location
            const extractedFiles = await this.extractBundle(bundleBuffer, extractionPath, onProgress);

            // Update progress
            onProgress?.(80, 'Finalizing installation...');

            // Create installation metadata (always in metadata path)
            // await this.createInstallationMetadata(dotOlafPath, bundleInfo, scope, platform.platform, extractedFiles, extractionPath);

            // Update progress
            onProgress?.(90, 'Updating configuration...');

            // Update platform-specific configuration if needed
            await this.updatePlatformConfiguration(platform.platform, scope, extractionPath);

            // Create symbolic link from workspace to installation path
            await this.createWorkspaceSymbolicLink(scope, extractionPath);

            // Update progress
            onProgress?.(100, 'Installation completed successfully!');

            const result: InstallationResult = {
                success: true,
                installedPath: extractionPath,
                installedFiles: extractedFiles,
                version: bundleInfo.version,
                scope,
                platform: platform.platform
            };

            this.logger.info(`Installation completed successfully at: ${extractionPath}`);
            return result;

        } catch (error) {
            this.logger.error('Installation failed', error as Error);
            
            return {
                success: false,
                installedPath: '',
                installedFiles: [],
                version: bundleInfo.version,
                scope,
                platform: Platform.UNKNOWN,
                error: (error as Error).message
            };
        }
    }

    /**
     * Prune empty directories from the extraction path as well as the metadata folder
     * This method recursively removes empty directories after file removal to ensure
     * no installation remnants are left behind.
     */
    public async pruneEmptyDirs(scope: InstallationScope): Promise<void> {
        this.logger.info(`Starting to prune empty directories for scope: ${scope}`);

        const platform = await this.platformDetector.detectPlatform();
        const installationPath = this.platformDetector.getInstallationPath(platform.platform, scope);

        // Check if installation exists
        try {
            await access(installationPath);
        } catch {
            this.logger.warn(`No installation found at: ${installationPath}`);
            return; // Nothing to prune
        }

        let extractionPath = installationPath;
        let installedFiles: string[] = [];

        // Read installation metadata to get extraction path and installed files
        try {
            const metadata = await this.readInstallationMetadata(installationPath);
            extractionPath = metadata.extractionPath ?? extractionPath;
            installedFiles = metadata.installedFiles || [];
            this.logger.info(`Extraction path: ${extractionPath}`);
            this.logger.info(`Files that were installed: ${installedFiles.length} files`);
        } catch {
            this.logger.warn('Could not read installation metadata for pruning');
        }

        // Collect all directories that contained files
        const directoriesToCheck = new Set<string>();

        // Add directories from installed files
        for (const file of installedFiles) {
            const filePath = path.join(extractionPath, file);
            let dir = path.dirname(filePath);
            
            // Add all parent directories up to the extraction path
            while (dir !== extractionPath && dir !== path.dirname(dir)) {
                directoriesToCheck.add(dir);
                dir = path.dirname(dir);
            }
        }

        // Also add the extraction path itself if it's different from installation path
        if (extractionPath !== installationPath) {
            directoriesToCheck.add(extractionPath);
        }

        // Convert to array and sort by depth (deepest first) for proper removal order
        const sortedDirectories = Array.from(directoriesToCheck).sort((a, b) => {
            const depthA = a.split(path.sep).length;
            const depthB = b.split(path.sep).length;
            return depthB - depthA; // Sort by depth, deepest first
        });

        this.logger.debug(`Checking ${sortedDirectories.length} directories for emptiness`);

        // Determine the root path (parent of extraction path) - we don't want to remove anything beyond this
        const rootPath = path.dirname(extractionPath);

        // Remove empty directories, starting from the deepest
        for (const dir of sortedDirectories) {
            await this.removeEmptyParentsRecursively(dir, rootPath);
        }

        // Finally, remove the installation/metadata directory if it's different from extraction path
        if (installationPath !== extractionPath) {
            // Remove metadata file first if it exists
            try {
                const metadataPath = path.join(installationPath, '.olaf', '.olaf-metadata.json');
                await fs.promises.unlink(metadataPath);
                this.logger.info(`Removed metadata file: ${metadataPath}`);
            } catch (error) {
                // Metadata file might not exist or already removed, which is fine
                this.logger.debug(`Metadata file not found or already removed: ${installationPath}`);
            }
            // Remove the .olaf directory
            try {
                const olafDir = path.join(installationPath, '.olaf');
                await fs.promises.rmdir(olafDir);
                this.logger.info(`Removed .olaf directory: ${olafDir}`);
            } catch (error) {
                this.logger.debug(`.olaf directory not empty or already removed: ${installationPath}`);
            }
            // Remove the installation path if empty
            await this.removeEmptyParentsRecursively(installationPath, rootPath);
        }

        this.logger.info(`Completed pruning empty directories for scope: ${scope}`);
    }

    /**
     * Helper method to remove a directory if it's empty
     * @param dirPath - The directory path to check and potentially remove
     */
    private async removeIfEmpty(dirPath: string): Promise<void> {
        try {
            // Check if directory exists
            await access(dirPath);
            
            // Read directory contents
            const files = await fs.promises.readdir(dirPath);
            
            if (files.length === 0) {
                // Directory is empty, remove it
                await fs.promises.rmdir(dirPath);
                this.logger.info(`Removed empty directory: ${dirPath}`);
            } else {
                this.logger.debug(`Directory not empty, keeping: ${dirPath} (${files.length} items)`);
            }
        } catch (error) {
            if ((error as any).code === 'ENOENT') {
                this.logger.debug(`Directory does not exist: ${dirPath}`);
            } else if ((error as any).code === 'ENOTEMPTY') {
                this.logger.debug(`Directory not empty: ${dirPath}`);
            } else {
                this.logger.debug(`Failed to check/remove directory: ${dirPath}`, error as Error);
            }
        }
    }

    /**
     * Recursively remove empty parent directories up to a root path
     * @param dirPath - Starting directory path
     * @param rootPath - Root path to stop before (won't remove this or go beyond it)
     */
    private async removeEmptyParentsRecursively(dirPath: string, rootPath: string): Promise<void> {
        // Stop if we've reached filesystem root
        if (dirPath === path.dirname(dirPath)) {
            return;
        }

        // Stop if we've reached the root path itself
        if (dirPath === rootPath) {
            return;
        }

        // Stop if the directory is not within the root path
        if (!dirPath.startsWith(rootPath + path.sep) && dirPath !== rootPath) {
            return;
        }

        try {
            await access(dirPath);
            const files = await fs.promises.readdir(dirPath);
            
            if (files.length === 0) {
                await fs.promises.rmdir(dirPath);
                this.logger.info(`Removed empty parent directory: ${dirPath}`);
                
                // Recursively check parent directory
                const parentDir = path.dirname(dirPath);
                await this.removeEmptyParentsRecursively(parentDir, rootPath);
            } else {
                this.logger.debug(`Directory not empty, keeping: ${dirPath} (${files.length} items)`);
            }
        } catch (error) {
            // Directory doesn't exist or can't be read/removed - stop recursion
            this.logger.debug(`Stopped recursive removal at: ${dirPath}`, error as Error);
        }
    }

    /**
     * Uninstall OLAF components
     */
    public async uninstall(scope: InstallationScope): Promise<boolean> {
        try {
            this.logger.info(`Starting uninstallation with scope: ${scope}`);

            const platform = await this.platformDetector.detectPlatform();
            const installationPath = this.platformDetector.getInstallationPath(platform.platform, scope);

            // Check if installation exists
            try {
                await access(installationPath);
            } catch {
                this.logger.warn(`No installation found at: ${installationPath}`);
                return true; // Nothing to uninstall
            }

            // Read installation metadata to get list of installed files
            const metadataPath = path.join(installationPath, '.olaf', '.olaf-metadata.json');
            let installedFiles: string[] = [];
            let extractionPath = installationPath;

            try {
                const metadata = await this.readInstallationMetadata(installationPath);
                installedFiles = metadata.installedFiles || [];
                this.logger.info(`Files to be removed: ${installedFiles.join(', ')}`);
                this.logger.info(`Extraction path from metadata: ${metadata.extractionPath}`);
                extractionPath = metadata.extractionPath ?? extractionPath;
            } catch {
                this.logger.warn('Could not read installation metadata, removing entire directory');
            }

            // Remove installed files
            if (installedFiles.length > 0) {
                for (const file of installedFiles) {
                    try {
                        await unlink(path.join(extractionPath, file));
                    } catch (error) {
                        this.logger.warn(`Failed to remove file: ${file}`, error as Error);
                    }
                }
            }

            // Remove workspace symbolic link if it exists
            await this.removeWorkspaceSymbolicLink(scope, extractionPath);

            // Remove platform-specific symbolic links
            const detectedPlatform = await this.platformDetector.detectPlatform();
            await this.removePlatformSymbolicLinks(detectedPlatform.platform, scope, extractionPath);

            // Remove empty directories using the comprehensive pruning method
            await this.pruneEmptyDirs(scope);

            // Remove the installation path with metadata
            try{
                await access(installationPath);
                await fs.promises.rm(installationPath, { recursive: true });

            } catch(error) {
                this.logger.error(`It was not possible to remove the installation path: ${installationPath}`, error as Error);
            }


            this.logger.info(`Uninstallation completed successfully from: ${installationPath}`);
            return true;

        } catch (error) {
            this.logger.error('Uninstallation failed', error as Error);
            return false;
        }
    }

    /**
     * Get current installation information
     */
    public async getInstallationInfo(scope: InstallationScope): Promise<any | null> {
        try {
            const platform = await this.platformDetector.detectPlatform();
            const installationPath = this.platformDetector.getInstallationPath(platform.platform, scope);

            return await this.readInstallationMetadata(installationPath);
        } catch {
            return null;
        }
    }

    /**
     * Check if OLAF is installed in a specific scope
     */
    public async isInstalled(scope: InstallationScope): Promise<boolean> {
        try {
            const platform = await this.platformDetector.detectPlatform();
            const installationPath = this.platformDetector.getInstallationPath(platform.platform, scope);
            const metadataPath = path.join(installationPath, '.olaf', '.olaf-metadata.json');

            await access(metadataPath);
            return true;
        } catch {
            return false;
        }
    }

    /**
     * Get all installation scopes where OLAF is installed
     */
    public async getInstalledScopes(): Promise<InstallationScope[]> {
        const scopes = [InstallationScope.USER, InstallationScope.PROJECT];
        const installedScopes: InstallationScope[] = [];

        for (const scope of scopes) {
            if (await this.isInstalled(scope)) {
                installedScopes.push(scope);
            }
        }

        return installedScopes;
    }

    private async ensureDirectoryExists(dirPath: string): Promise<void> {
        try {
            await access(dirPath);
        } catch {
            await mkdir(dirPath, { recursive: true });
            this.logger.debug(`Created directory: ${dirPath}`);
        }
    }

    private async extractBundle(
        bundleBuffer: Buffer,
        extractPath: string,
        onProgress?: (progress: number, message: string) => void
    ): Promise<string[]> {
        return new Promise((resolve, reject) => {
            const extractedFiles: string[] = [];
            let processedEntries = 0;
            let totalEntries = 0;

            yauzl.fromBuffer(bundleBuffer, { lazyEntries: true }, (err: Error | null, zipfile?: yauzl.ZipFile) => {
                if (err) {
                    reject(err);
                    return;
                }

                if (!zipfile) {
                    reject(new Error('Failed to open zip file'));
                    return;
                }

                totalEntries = zipfile.entryCount;
                this.logger.debug(`Extracting ${totalEntries} entries from bundle to ${extractPath}`);

                zipfile.readEntry();

                zipfile.on('entry', (entry: yauzl.Entry) => {
                    const fileName = entry.fileName;
                    
                    // Skip directories
                    if (fileName.endsWith('/')) {
                        processedEntries++;
                        zipfile.readEntry();
                        return;
                    }

                    // Skip common hidden files but allow important dot directories like .github
                    const isHiddenFile = fileName.startsWith('.') && 
                        !fileName.startsWith('.github/') && 
                        !fileName.startsWith('.vscode/') &&
                        !fileName.startsWith('.windsurf/') && 
                        !fileName.startsWith('.kiro/') && 
                        !fileName.startsWith('.cursor/') &&
                        !fileName.startsWith('.olaf/');
                    
                    if (isHiddenFile) {
                        processedEntries++;
                        zipfile.readEntry();
                        return;
                    }

                    const outputPath = path.join(extractPath, fileName);
                    const outputDir = path.dirname(outputPath);

                    // Ensure output directory exists
                    fs.mkdir(outputDir, { recursive: true }, (mkdirErr) => {
                        if (mkdirErr) {
                            reject(mkdirErr);
                            return;
                        }

                        zipfile.openReadStream(entry, (streamErr: Error | null, readStream?: NodeJS.ReadableStream) => {
                            if (streamErr) {
                                reject(streamErr);
                                return;
                            }

                            if (!readStream) {
                                reject(new Error('Failed to open read stream'));
                                return;
                            }

                            const writeStream = fs.createWriteStream(outputPath);
                            
                            readStream.pipe(writeStream);

                            writeStream.on('close', () => {
                                extractedFiles.push(fileName);
                                processedEntries++;
                                
                                // Update progress
                                const progress = 20 + (processedEntries / totalEntries) * 60; // 20-80% for extraction
                                onProgress?.(progress, `Extracting: ${fileName}`);

                                this.logger.debug(`Extracted: ${fileName}`);
                                
                                if (processedEntries === totalEntries) {
                                    resolve(extractedFiles);
                                } else {
                                    zipfile.readEntry();
                                }
                            });

                            writeStream.on('error', (writeErr) => {
                                reject(writeErr);
                            });
                        });
                    });
                });

                zipfile.on('end', () => {
                    if (processedEntries === totalEntries) {
                        resolve(extractedFiles);
                    }
                });

                zipfile.on('error', (zipErr: Error) => {
                    reject(zipErr);
                });
            });
        });
    }

    private async createInstallationMetadata(
        metadataPath: string,
        bundleInfo: BundleInfo,
        scope: InstallationScope,
        platform: Platform,
        installedFiles: string[],
        extractionPath: string
    ): Promise<void> {
        const metadata = {
            version: bundleInfo.version,
            platform: platform,
            scope: scope,
            installedAt: new Date().toISOString(),
            bundleInfo: {
                filename: bundleInfo.filename,
                size: bundleInfo.size,
                platform: bundleInfo.platform
            },
            installedFiles: installedFiles,
            extractionPath: extractionPath
        };

        await this.ensureDirectoryExists(metadataPath);

        const metadataFilePath = path.join(metadataPath, '.olaf-metadata.json');
        await writeFile(metadataFilePath, JSON.stringify(metadata, null, 2));
        
        this.logger.debug(`Created installation metadata at: ${metadataFilePath}`);
    }

    private async readInstallationMetadata(installationPath: string): Promise<any> {
        const metadataPath = path.join(installationPath, '.olaf', '.olaf-metadata.json');
        const metadataContent = await readFile(metadataPath, 'utf8');
        return JSON.parse(metadataContent);
    }

    private async updatePlatformConfiguration(
        platform: Platform,
        scope: InstallationScope,
        installationPath: string
    ): Promise<void> {
        try {
            // Platform-specific configuration updates
            switch (platform) {
                case Platform.VSCODE:
                    await this.updateVSCodeConfiguration(scope, installationPath);
                    break;
                case Platform.WINDSURF:
                    await this.updateWindsurfConfiguration(scope, installationPath);
                    break;
                case Platform.KIRO:
                    await this.updateKiroConfiguration(scope, installationPath);
                    break;
                case Platform.CURSOR:
                    await this.updateCursorConfiguration(scope, installationPath);
                    break;
                default:
                    this.logger.debug('No platform-specific configuration updates needed');
            }
        } catch (error) {
            this.logger.warn('Failed to update platform configuration', error as Error);
            // Don't fail the installation for configuration updates
        }
    }

    private async updateVSCodeConfiguration(scope: InstallationScope, installationPath: string): Promise<void> {
        // Add VSCode-specific configuration updates here
        this.logger.debug(`Updating VSCode configuration for scope: ${scope}`);

        // Create symbolic link from workspace/.github to installationPath/.github
        await this.createGitHubSymbolicLink(scope, installationPath);
    }

    private async updateWindsurfConfiguration(scope: InstallationScope, installationPath: string): Promise<void> {
        // Add Windsurf-specific configuration updates here
        this.logger.debug(`Updating Windsurf configuration for scope: ${scope}`);
    }

    private async updateKiroConfiguration(scope: InstallationScope, installationPath: string): Promise<void> {
        // Add Kiro-specific configuration updates here
        this.logger.debug(`Updating Kiro configuration for scope: ${scope}`);
    }

    private async updateCursorConfiguration(scope: InstallationScope, installationPath: string): Promise<void> {
        // Add Cursor-specific configuration updates here
        this.logger.debug(`Updating Cursor configuration for scope: ${scope}`);
    }

    /**
     * Create symbolic link from workspace/.olaf to installation path/.olaf
     */
    private async createWorkspaceSymbolicLink(scope: InstallationScope, extractionPath: string): Promise<void> {
        try {
            // Only create symbolic link for non-project installations
            if (scope === InstallationScope.PROJECT) {
                this.logger.debug('Skipping symbolic link creation for project installation (files already in workspace)');
                return;
            }

            // Get workspace root path
            const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
            if (!workspaceRoot) {
                this.logger.warn('No workspace folder found, skipping symbolic link creation');
                return;
            }

            const workspaceOlafPath = path.join(workspaceRoot, '.olaf');
            const installationOlafPath = path.join(extractionPath, '.olaf');

            // Check if .olaf directory exists in the installation
            if (!fs.existsSync(installationOlafPath)) {
                this.logger.debug('No .olaf directory found in installation, skipping symbolic link creation');
                return;
            }

            // Remove existing .olaf in workspace if it exists
            if (fs.existsSync(workspaceOlafPath)) {
                const stats = fs.lstatSync(workspaceOlafPath);
                if (stats.isSymbolicLink()) {
                    fs.unlinkSync(workspaceOlafPath);
                    this.logger.debug(`Removed existing symbolic link: ${workspaceOlafPath}`);
                } else if (stats.isDirectory()) {
                    // If it's a real directory, we should be more cautious
                    this.logger.warn(`Existing .olaf directory found at ${workspaceOlafPath}. Manual intervention may be required.`);
                    return;
                }
            }

            // Create symbolic link
            fs.symlinkSync(installationOlafPath, workspaceOlafPath, 'dir');
            this.logger.info(`Created symbolic link: ${workspaceOlafPath} -> ${installationOlafPath}`);

        } catch (error) {
            this.logger.warn('Failed to create workspace symbolic link', error as Error);
            // Don't fail the installation for symbolic link creation issues
        }
    }

    /**
     * Remove symbolic link from workspace/.olaf during uninstallation
     */
    private async removeWorkspaceSymbolicLink(scope: InstallationScope, extractionPath: string): Promise<void> {
        try {
            // Only remove symbolic link for non-project installations
            if (scope === InstallationScope.PROJECT) {
                this.logger.debug('Skipping symbolic link removal for project installation');
                return;
            }

            // Get workspace root path
            const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
            if (!workspaceRoot) {
                this.logger.debug('No workspace folder found, skipping symbolic link removal');
                return;
            }

            const workspaceOlafPath = path.join(workspaceRoot, '.olaf');

            // Check if .olaf exists in workspace and is a symbolic link
            if (fs.existsSync(workspaceOlafPath)) {
                const stats = fs.lstatSync(workspaceOlafPath);
                if (stats.isSymbolicLink()) {
                    // Verify that the symbolic link points to our installation
                    const linkTarget = fs.readlinkSync(workspaceOlafPath);
                    const expectedTarget = path.join(extractionPath, '.olaf');

                    if (path.resolve(path.dirname(workspaceOlafPath), linkTarget) === path.resolve(expectedTarget)) {
                        fs.unlinkSync(workspaceOlafPath);
                        this.logger.info(`Removed workspace symbolic link: ${workspaceOlafPath}`);
                    } else {
                        this.logger.warn(`Symbolic link points to different location, not removing: ${workspaceOlafPath} -> ${linkTarget}`);
                    }
                } else {
                    this.logger.debug(`Workspace .olaf is not a symbolic link, not removing: ${workspaceOlafPath}`);
                }
            } else {
                this.logger.debug(`No workspace .olaf symbolic link found at: ${workspaceOlafPath}`);
            }

        } catch (error) {
            this.logger.warn('Failed to remove workspace symbolic link', error as Error);
            // Don't fail the uninstallation for symbolic link removal issues
        }
    }

    /**
     * Create symbolic link from workspace/.github to installation path/.github
     */
    private async createGitHubSymbolicLink(scope: InstallationScope, installationPath: string): Promise<void> {
        try {
            // Get workspace root path
            const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
            if (!workspaceRoot) {
                this.logger.warn('No workspace folder found, skipping .github symbolic link creation');
                return;
            }

            const workspaceGitHubPath = path.join(workspaceRoot, '.github');
            const installationGitHubPath = path.join(installationPath, '.github');

            // Check if .github directory exists in the installation
            if (!fs.existsSync(installationGitHubPath)) {
                this.logger.debug('No .github directory found in installation, skipping .github symbolic link creation');
                return;
            }

            // Remove existing .github in workspace if it exists
            if (fs.existsSync(workspaceGitHubPath)) {
                const stats = fs.lstatSync(workspaceGitHubPath);
                if (stats.isSymbolicLink()) {
                    fs.unlinkSync(workspaceGitHubPath);
                    this.logger.debug(`Removed existing .github symbolic link: ${workspaceGitHubPath}`);
                } else if (stats.isDirectory()) {
                    // If it's a real directory, we should be more cautious
                    this.logger.warn(`Existing .github directory found at ${workspaceGitHubPath}. Manual intervention may be required.`);
                    return;
                }
            }

            // Create symbolic link
            fs.symlinkSync(installationGitHubPath, workspaceGitHubPath, 'dir');
            this.logger.info(`Created .github symbolic link: ${workspaceGitHubPath} -> ${installationGitHubPath}`);

        } catch (error) {
            this.logger.warn('Failed to create .github symbolic link', error as Error);
            // Don't fail the installation for symbolic link creation issues
        }
    }

    /**
     * Remove platform-specific symbolic links during uninstallation
     */
    private async removePlatformSymbolicLinks(platform: Platform, scope: InstallationScope, extractionPath: string): Promise<void> {
        try {
            switch (platform) {
                case Platform.VSCODE:
                    await this.removeGitHubSymbolicLink(extractionPath);
                    break;
                case Platform.WINDSURF:
                case Platform.KIRO:
                case Platform.CURSOR:
                    // Add platform-specific symbolic link removal here if needed
                    this.logger.debug(`No platform-specific symbolic links to remove for: ${platform}`);
                    break;
                default:
                    this.logger.debug('No platform-specific symbolic links to remove');
            }
        } catch (error) {
            this.logger.warn('Failed to remove platform-specific symbolic links', error as Error);
            // Don't fail the uninstallation for symbolic link removal issues
        }
    }

    /**
     * Remove .github symbolic link from workspace during uninstallation
     */
    private async removeGitHubSymbolicLink(extractionPath: string): Promise<void> {
        try {
            // Get workspace root path
            const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
            if (!workspaceRoot) {
                this.logger.debug('No workspace folder found, skipping .github symbolic link removal');
                return;
            }

            const workspaceGitHubPath = path.join(workspaceRoot, '.github');

            // Check if .github exists in workspace and is a symbolic link
            if (fs.existsSync(workspaceGitHubPath)) {
                const stats = fs.lstatSync(workspaceGitHubPath);
                if (stats.isSymbolicLink()) {
                    // Verify that the symbolic link points to our installation
                    const linkTarget = fs.readlinkSync(workspaceGitHubPath);
                    const expectedTarget = path.join(extractionPath, '.github');

                    if (path.resolve(path.dirname(workspaceGitHubPath), linkTarget) === path.resolve(expectedTarget)) {
                        fs.unlinkSync(workspaceGitHubPath);
                        this.logger.info(`Removed workspace .github symbolic link: ${workspaceGitHubPath}`);
                    } else {
                        this.logger.warn(`GitHub symbolic link points to different location, not removing: ${workspaceGitHubPath} -> ${linkTarget}`);
                    }
                } else {
                    this.logger.debug(`Workspace .github is not a symbolic link, not removing: ${workspaceGitHubPath}`);
                }
            } else {
                this.logger.debug(`No workspace .github symbolic link found at: ${workspaceGitHubPath}`);
            }

        } catch (error) {
            this.logger.warn('Failed to remove .github symbolic link', error as Error);
            // Don't fail the uninstallation for symbolic link removal issues
        }
    }
}
