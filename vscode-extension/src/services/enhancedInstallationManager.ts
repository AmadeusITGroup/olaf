import * as vscode from 'vscode';
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import * as yauzl from 'yauzl';
import { GitHubAsset } from "../types/github";
import { Platform, InstallationScope } from '../types/platform';
import { Logger } from '../utils/logger';
import { FileIntegrityService } from './fileIntegrityService';
import { PlatformDetector } from './platformDetector';
import { 
    FileIntegrityInfo,
    EnhancedInstallationMetadata,
    InstallationResult,
    IntegrityReport,
    ModificationInfo,
    VerificationPolicy
} from '../types/integrityTypes';

import { promisify } from 'util';
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);
const mkdir = promisify(fs.mkdir);
const access = promisify(fs.access);
const unlink = promisify(fs.unlink);

/**
 * Enhanced InstallationManager with comprehensive file integrity verification
 * and smart uninstallation capabilities
 */
export class EnhancedInstallationManager {
    private static instance: EnhancedInstallationManager;
    private readonly integrityService: FileIntegrityService;
    private readonly logger: Logger;
    private readonly platformDetector: PlatformDetector;

    private constructor() {
        this.integrityService = new FileIntegrityService();
        this.logger = Logger.getInstance();
        this.platformDetector = PlatformDetector.getInstance();
    }

    public static getInstance(): EnhancedInstallationManager {
        if (!EnhancedInstallationManager.instance) {
            EnhancedInstallationManager.instance = new EnhancedInstallationManager();
        }
        return EnhancedInstallationManager.instance;
    }

    /**
     * Enhanced installation with integrity verification
     */
    public async installBundle(
        bundlePath: string, 
        scope: InstallationScope,
        onProgress?: (progress: number, message: string) => void
    ): Promise<InstallationResult> {
        try {
            this.logger.info(`Starting enhanced installation for bundle: ${bundlePath}`);
            onProgress?.(0, 'Starting enhanced installation...');

            // 1. Validate bundle integrity
            onProgress?.(10, 'Validating bundle integrity...');
            await this.validateBundleIntegrity(bundlePath);
            // Fix the installBundle call - need to create BundleInfo
            const bundleBuffer = fs.readFileSync(bundlePath);
            const bundleInfo = {
                filename: path.basename(bundlePath),
                size: bundleBuffer.length,
                platform: Platform.UNKNOWN,
                downloadUrl: "", // placeholder
                version: "1.0.0", // placeholder
                architecture: "x64", // placeholder
                asset: {
                    id: 0,
                    name: path.basename(bundlePath),
                    label: null,
                    content_type: "application/zip",
                    size: bundleBuffer.length,
                    download_count: 0,
                    created_at: new Date().toISOString(),
                    updated_at: new Date().toISOString(),
                    browser_download_url: "file://" + bundlePath
                } as GitHubAsset
            };

            // ===========
            const platform = await this.platformDetector.detectPlatform();
            
            // For project scope, extract files to project root; for others use the standard path
            const extractionPath = scope === InstallationScope.PROJECT 
                ? vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || ''
                : this.platformDetector.getInstallationPath(platform.platform, scope);
            const dotOlafPath = path.join(extractionPath, ".olaf");

            // Update progress
            onProgress?.(20, 'Preparing installation directory...');

            // Ensure metadata directory exists
            await this.ensureDirectoryExists(extractionPath);
            
            // Update progress
            onProgress?.(30, 'Extracting bundle...');

            // Extract bundle to the appropriate location
            const extractedFiles = await this.extractBundle(bundleBuffer, extractionPath, onProgress);

            // Update progress
            onProgress?.(50, 'Finalizing installation...');

            // Create installation metadata (always in metadata path)
            // await this.createInstallationMetadata(dotOlafPath, bundleInfo, scope, platform.platform, extractedFiles, extractionPath);

            // Update progress
            onProgress?.(60, 'Updating configuration...');

            // Update platform-specific configuration if needed
            await this.updatePlatformConfiguration(platform.platform, scope, extractionPath);

            // Create symbolic link from workspace to installation path
            await this.createWorkspaceSymbolicLink(scope, extractionPath);

            // 3. Calculate integrity information for installed files
            onProgress?.(80, 'Computing file integrity data...');
            const installedFiles = extractedFiles || [];
            const fileIntegrities = await this.calculateFileIntegrities(
                installedFiles.map(file => path.join(extractionPath, file))
            );

            // 4. Create enhanced metadata
            onProgress?.(90, 'Saving enhanced metadata...');
            
            // Determine actual OS platform (Platform enum is for editors, not OS)
            const currentOSPlatform = process.platform === 'win32' ? 'windows' :
                                    process.platform === 'darwin' ? 'macos' :
                                    process.platform === 'linux' ? 'linux' :
                                    'unknown';
            
            // Extract version from bundle or use default
            const bundleVersion = this.extractVersionFromBundle(bundlePath) || '1.0.0';
            
            const enhancedMetadata: EnhancedInstallationMetadata = {
                version: bundleVersion,
                platform: platform.platform, // Default to unknown editor platform
                scope: scope === InstallationScope.PROJECT ? 'project' : 
                       scope === InstallationScope.USER ? 'user' : 'unknown',
                installedAt: new Date().toISOString(),
                osplatform: currentOSPlatform, // OS platform information
                bundleInfo: {
                    filename: path.basename(bundlePath),
                    size: fs.statSync(bundlePath).size,
                    platform: platform.platform, // Editor platform, not OS platform
                    sha256: await this.calculateFileSHA256(bundlePath),
                    manifestVersion: '1.0.0'
                },
                originalFiles: fileIntegrities,
                extractionPath: await this.getInstallationPath(scope),
                integrityVersion: '1.0.0',
                // lastVerified: new Date().toISOString(),
                verificationPolicy: { autoVerify: true, preserveModified: true, reportModifications: true },
                rollbackSupported: true
            };

            await this.saveEnhancedMetadata(scope, enhancedMetadata);

            onProgress?.(100, 'Installation completed successfully');

            return {
                success: true,
                metadata: enhancedMetadata,
                integrityInfo: fileIntegrities,
                rollbackAvailable: true,
                warnings: []
            };

        } catch (error) {
            this.logger.error("Enhanced installation failed", error instanceof Error ? error : new Error(String(error)));
            return {
                success: false,
                metadata: {} as EnhancedInstallationMetadata,
                integrityInfo: [],
                rollbackAvailable: false,
                warnings: [error instanceof Error ? error.message : String(error)]
            };
        }
    }


    /**
     * Get enhanced metadata for a specific scope
     */
    public async getEnhancedMetadata(scope: InstallationScope): Promise<EnhancedInstallationMetadata | null> {
        return await this.loadEnhancedMetadata(scope);
    }
    /**
     * Smart uninstallation with integrity verification
     */
    public async uninstall(
        scope: InstallationScope,
        policy?: VerificationPolicy,
        onProgress?: (progress: number, message: string) => void
    ): Promise<IntegrityReport> {
        try {
            this.logger.info(`Starting smart uninstallation for scope: ${scope}`);
            onProgress?.(0, 'Starting smart uninstallation...');

            // 1. Load enhanced metadata
            onProgress?.(10, 'Loading installation metadata...');
            const metadata = await this.loadEnhancedMetadata(scope);
            
            if (!metadata) {
                throw new Error(`Failed to load installation metadata for ${scope} scope`);
            }

            // 2. Verify current file states
            onProgress?.(30, 'Verifying file integrity...');
            const verificationResults = await this.verifyFiles(metadata.originalFiles);
            
            // 3. Categorize files and handle user choices
            onProgress?.(60, 'Processing file removal...');
            const { intactFiles, modifiedFiles } = this.categorizeFiles(metadata.originalFiles, verificationResults);
            
            // 4. Remove files based on policy
            onProgress?.(80, 'Removing files...');
            const removedCount = await this.removeFiles(intactFiles, modifiedFiles, policy);

            // 5. Clean up metadata
            onProgress?.(95, 'Cleaning up metadata...');
            await this.cleanupEnhancedMetadata(scope);

            onProgress?.(100, 'Uninstallation completed');

            return this.createDetailedReport(metadata.originalFiles.length, modifiedFiles.length, removedCount, []);

        } catch (error) {
            this.logger.error("Enhanced installation failed", error instanceof Error ? error : new Error(String(error)));
            throw error;
        }
    }

    // Private helper methods

    private async validateBundleIntegrity(bundlePath: string): Promise<void> {
        if (!fs.existsSync(bundlePath)) {
            throw new Error(`Bundle file not found: ${bundlePath}`);
        }

        const stats = fs.statSync(bundlePath);
        if (stats.size === 0) {
            throw new Error(`Bundle file is empty: ${bundlePath}`);
        }
    }

    private async getInstalledFilesList(scope: InstallationScope): Promise<string[]> {
        // Try to read files from existing metadata or scan directory
        try {
            const installationPath = await this.getInstallationPath(scope);
            const metadataPath = path.join(installationPath, '.olaf', '.olaf-metadata.json');
            
            if (fs.existsSync(metadataPath)) {
                const metadata = JSON.parse(fs.readFileSync(metadataPath, 'utf8'));
                return (metadata.installedFiles || []).map((file: string) => 
                    path.join(metadata.extractionPath || installationPath, file)
                );
            }
            
            // Fallback: scan directory for files (excluding metadata)
            return this.scanDirectoryFiles(installationPath);
        } catch (error) {
            this.logger.warn(`Failed to get installed files list for scope ${scope}:`, error);
            return [];
        }
    }

    private scanDirectoryFiles(dirPath: string): string[] {
        try {
            if (!fs.existsSync(dirPath)) {
                return [];
            }

            const files: string[] = [];
            const scanRecursive = (currentPath: string) => {
                const items = fs.readdirSync(currentPath);
                for (const item of items) {
                    if (item.startsWith('.olaf') && item.endsWith('.json')) {
                        continue; // Skip metadata files
                    }
                    
                    const fullPath = path.join(currentPath, item);
                    const stat = fs.statSync(fullPath);
                    
                    if (stat.isFile()) {
                        files.push(fullPath);
                    } else if (stat.isDirectory()) {
                        scanRecursive(fullPath);
                    }
                }
            };
            
            scanRecursive(dirPath);
            return files;
        } catch (error) {
            this.logger.warn(`Failed to scan directory ${dirPath}:`, error);
            return [];
        }
    }

        private async calculateFileIntegrities(filePaths: string[]): Promise<FileIntegrityInfo[]> {
        const integrities: FileIntegrityInfo[] = [];

        this.logger.info(`Starting integrity calculation for ${filePaths.length} files`);
        
        for (let i = 0; i < filePaths.length; i++) {
            const filePath = filePaths[i];
            this.logger.info(`Processing file ${i + 1}/${filePaths.length}: ${filePath}`);
            
            try {
                // Check if file exists before calculating integrity
                if (!fs.existsSync(filePath)) {
                    this.logger.warn(`File does not exist: ${filePath}`);
                    continue;
                }
                
                this.logger.debug(`File exists, checking stats: ${filePath}`);
                const stats = fs.statSync(filePath);
                this.logger.debug(`File stats - size: ${stats.size}, isFile: ${stats.isFile()}`);
                
                if (!stats.isFile()) {
                    this.logger.warn(`Skipping non-file: ${filePath}`);
                    continue;
                }
                
                this.logger.debug(`Calling integrityService.calculateFileIntegrity for: ${filePath}`);
                const integrity = await this.integrityService.calculateFileIntegrity(filePath);
                integrities.push(integrity);
                this.logger.info(`Successfully calculated integrity for: ${filePath} (${integrities.length}/${filePaths.length})`);
            } catch (error) {
                this.logger.error(`DETAILED ERROR for ${filePath}:`);
                this.logger.error(`  Error type: ${typeof error}`);
                this.logger.error(`  Error constructor: ${error?.constructor?.name}`);
                this.logger.error(`  Error message: ${error instanceof Error ? error.message : 'No message'}`);
                this.logger.error(`  Error stack: ${error instanceof Error ? error.stack : 'No stack'}`);
                this.logger.error(`  Full error object keys: ${Object.keys(error || {})}`);
                this.logger.error(`  File exists: ${fs.existsSync(filePath)}`);
                this.logger.error(`  File readable: ${fs.constants && (fs.accessSync(filePath, fs.constants.R_OK), true) || 'unknown'}`);
            }
        }

        this.logger.info(`Successfully calculated integrity for ${integrities.length}/${filePaths.length} files`);
        return integrities;
    }

    private async calculateFileSHA256(filePath: string): Promise<string> {
        const hash = require('crypto').createHash('sha256');
        const stream = fs.createReadStream(filePath);
        
        for await (const chunk of stream) {
            hash.update(chunk);
        }
        
        return hash.digest('hex');
    }

    private async calculateInstallationHash(fileIntegrities: FileIntegrityInfo[]): Promise<string> {
        const crypto = require('crypto');
        const hash = crypto.createHash('sha256');
        
        const sorted = fileIntegrities.sort((a, b) => a.path.localeCompare(b.path));
        
        for (const integrity of sorted) {
            hash.update(`${integrity.path}:${integrity.sha256}:${integrity.xxhash64}`);
        }

        return hash.digest('hex');
    }

    private async getInstallationPath(scope: InstallationScope): Promise<string> {
        const platform = await this.platformDetector.detectPlatform();
        return this.platformDetector.getInstallationPath(platform.platform, scope);
    }

    private async saveEnhancedMetadata(
        scope: InstallationScope,
        metadata: EnhancedInstallationMetadata
    ): Promise<void> {
        const metadataPath = await this.getEnhancedMetadataPath(scope);
        const metadataDir = path.dirname(metadataPath);

        if (!fs.existsSync(metadataDir)) {
            fs.mkdirSync(metadataDir, { recursive: true });
        }

        fs.writeFileSync(metadataPath, JSON.stringify(metadata, null, 2), 'utf8');
        this.logger.info(`Enhanced metadata saved to: ${metadataPath}`);
    }

    private async loadEnhancedMetadata(scope: InstallationScope): Promise<EnhancedInstallationMetadata | null> {
        const metadataPath = await this.getEnhancedMetadataPath(scope);

        if (!fs.existsSync(metadataPath)) {
            return null;
        }

        try {
            const content = fs.readFileSync(metadataPath, 'utf8');
            return JSON.parse(content) as EnhancedInstallationMetadata;
        } catch (error) {
            this.logger.error(`Failed to load enhanced metadata from ${metadataPath}:`, error instanceof Error ? error : new Error(String(error)));
            return null;
        }
    }

    private async getEnhancedMetadataPath(scope: InstallationScope): Promise<string> {
        const platform = await this.platformDetector.detectPlatform();
        const installationPath = this.platformDetector.getInstallationPath(platform.platform, scope);
        const metadataPath = path.join(installationPath, ".olaf", ".olaf-enhanced-metadata.json");
        return metadataPath;
    }

    private async verifyFiles(files: FileIntegrityInfo[]): Promise<Map<string, FileIntegrityInfo | null>> {
        const results = new Map<string, FileIntegrityInfo | null>();

        for (const file of files) {
            try {
                if (fs.existsSync(file.path)) {
                    const current = await this.integrityService.calculateFileIntegrity(file.path);
                    results.set(file.path, current);
                } else {
                    results.set(file.path, null);
                }
            } catch (error) {
                this.logger.warn(`Failed to verify ${file.path}:`, error instanceof Error ? error : new Error(String(error)));
                results.set(file.path, null);
            }
        }

        return results;
    }

    private categorizeFiles(
        originalFiles: FileIntegrityInfo[],
        currentStates: Map<string, FileIntegrityInfo | null>
    ): { intactFiles: FileIntegrityInfo[], modifiedFiles: string[] } {
        const intactFiles: FileIntegrityInfo[] = [];
        const modifiedFiles: string[] = [];

        for (const originalFile of originalFiles) {
            const currentFile = currentStates.get(originalFile.path);

            if (!currentFile) {
                // File was deleted - consider it modified
                modifiedFiles.push(originalFile.path);
            } else if (
                originalFile.sha256 === currentFile.sha256 &&
                originalFile.xxhash64 === currentFile.xxhash64
            ) {
                // File is intact
                intactFiles.push(currentFile);
            } else {
                // File was modified
                modifiedFiles.push(originalFile.path);
            }
        }

        return { intactFiles, modifiedFiles };
    }

    private async removeFiles(
        intactFiles: FileIntegrityInfo[],
        modifiedFiles: string[],
        policy?: VerificationPolicy
    ): Promise<number> {
        let removedCount = 0;

        // Create backup directory if backup is requested
        let backupDir: string | undefined;
        if (policy?.backupModified && modifiedFiles.length > 0) {
            backupDir = await this.createBackupDirectory(policy.backupPath);
            this.logger.info(`Created backup directory: ${backupDir}`);
        }

        // Remove intact files first
        for (const intactFile of intactFiles) {
            try {
                if (fs.existsSync(intactFile.path)) {
                    fs.unlinkSync(intactFile.path);
                    removedCount++;
                    this.logger.info(`Removed intact file: ${intactFile.path}`);
                }
            } catch (error) {
                this.logger.warn(`Failed to delete intact file ${intactFile.path}:`, error);
            }
        }

        // Handle modified files based on policy
        if (policy) {
            for (const modifiedFile of modifiedFiles) {
                if (!fs.existsSync(modifiedFile)) {
                    continue;
                }

                try {
                    // Create backup if requested
                    if (policy.backupModified && backupDir) {
                        await this.backupFile(modifiedFile, backupDir);
                    }

                    // Remove based on handleModified policy
                    if (policy.handleModified === 'remove' || 
                        (policy.handleModified !== 'preserve' && !policy.preserveModified)) {
                        fs.unlinkSync(modifiedFile);
                        removedCount++;
                        this.logger.info(`Removed modified file: ${modifiedFile}`);
                    } else {
                        this.logger.info(`Preserved modified file: ${modifiedFile}`);
                    }
                } catch (error) {
                    this.logger.warn(`Failed to process modified file ${modifiedFile}:`, error);
                }
            }
        }

        return removedCount;
    }

    /**
     * Create backup directory for modified files
     */
    private async createBackupDirectory(customPath?: string): Promise<string> {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const backupDir = customPath || path.join(os.tmpdir(), `olaf-backup-${timestamp}`);
        
        if (!fs.existsSync(backupDir)) {
            fs.mkdirSync(backupDir, { recursive: true });
        }
        
        return backupDir;
    }

    /**
     * Backup a single file to backup directory
     */
    private async backupFile(filePath: string, backupDir: string): Promise<void> {
        const fileName = path.basename(filePath);
        const backupPath = path.join(backupDir, fileName);
        
        try {
            fs.copyFileSync(filePath, backupPath);
            this.logger.info(`Backed up ${fileName} to ${backupPath}`);
        } catch (error) {
            this.logger.warn(`Failed to backup ${filePath}:`, error);
            throw error;
        }
    }

    private async cleanupEnhancedMetadata(scope: InstallationScope): Promise<void> {
        const metadataPath = await this.getEnhancedMetadataPath(scope);

        try {
            if (fs.existsSync(metadataPath)) {
                fs.unlinkSync(metadataPath);
                this.logger.info(`Enhanced metadata cleaned up: ${metadataPath}`);
            }
        } catch (error) {
            this.logger.warn(`Failed to cleanup enhanced metadata ${metadataPath}:`, error);
        }
    }

    private createBasicReport(success: boolean): IntegrityReport {
        return {
            summary: `Legacy uninstallation ${success ? 'completed' : 'failed'}`,
            totalFiles: 0,
            intactFiles: 0,
            modifiedFiles: 0,
            corruptedFiles: 0,
            deletedFiles: success ? 1 : 0,
            generatedAt: new Date().toISOString(),
            modifications: []
        };
    }

    private createDetailedReport(
        totalFiles: number,
        modifiedCount: number,
        deletedCount: number,
        modifications: any[]
    ): IntegrityReport {
        return {
            summary: `Processed ${totalFiles} files, ${modifiedCount} modified, ${deletedCount} deleted`,
            totalFiles,
            intactFiles: totalFiles - modifiedCount,
            modifiedFiles: modifiedCount,
            corruptedFiles: 0,
            deletedFiles: deletedCount,
            generatedAt: new Date().toISOString(),
            modifications
        };
    }
    
    /**
     * Extract version from bundle filename or manifest
     * Falls back to default version if extraction fails
     */
    private extractVersionFromBundle(bundlePath: string): string | null {
        try {
            const filename = path.basename(bundlePath, '.zip');
            
            // Try to extract version from filename patterns like: 
            // app-v1.2.3.zip, app_1.2.3.zip, app-1.2.3.zip
            const versionMatch = filename.match(/[v_-]?(\d+\.\d+\.\d+)/);
            if (versionMatch) {
                return versionMatch[1];
            }
            
            // Try reading package.json if it exists in extracted content
            // For now, return null to use fallback
            return null;
        } catch (error) {
            return null;
        }
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
            throw error;
        }
    }

    private async updateVSCodeConfiguration(scope: InstallationScope, installationPath: string): Promise<void> {
        // Add VSCode-specific configuration updates here
        this.logger.debug(`Updating VSCode configuration for scope: ${scope}`);

        // Create symbolic link from workspace/.github to installationPath/.github
        await this.createSymbolicLink(scope, installationPath, '.github');
    }

    private async updateWindsurfConfiguration(scope: InstallationScope, installationPath: string): Promise<void> {
        // Add Windsurf-specific configuration updates here
        this.logger.debug(`Updating Windsurf configuration for scope: ${scope}`);

        // Create symbolic link from workspace/.windsurf to installationPath/.windsurf
        await this.createSymbolicLink(scope, installationPath, '.windsurf');
    }

    private async updateKiroConfiguration(scope: InstallationScope, installationPath: string): Promise<void> {
        // Add Kiro-specific configuration updates here
        this.logger.debug(`Updating Kiro configuration for scope: ${scope}`);

        // Create symbolic link from workspace/.kiro to installationPath/.kiro
        await this.createSymbolicLink(scope, installationPath, '.kiro');
    }

    private async updateCursorConfiguration(scope: InstallationScope, installationPath: string): Promise<void> {
        // Add Cursor-specific configuration updates here
        this.logger.debug(`Updating Cursor configuration for scope: ${scope}`);

        // Create symbolic link from workspace/.cursor to installationPath/.cursor
        await this.createSymbolicLink(scope, installationPath, '.cursor');
    }

    /**
     * Create symbolic link from workspace/.github to installation path/.github
     */
    private async createSymbolicLink(scope: InstallationScope, installationPath: string, symlinkName: string): Promise<void> {
        try {
            if (scope !== InstallationScope.USER) {
                this.logger.debug(`Skipping ${symlinkName} symbolic link creation for non-user scope`);
                return;
            }

            // Get workspace root path
            const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
            if (!workspaceRoot) {
                this.logger.warn(`No workspace folder found, skipping ${symlinkName} symbolic link creation`);
                return;
            }

            const workspaceSymlinkPath = path.join(workspaceRoot, symlinkName);
            const installationSymlinkPath = path.join(installationPath, symlinkName);

            // Check if .github directory exists in the installation
            if (!fs.existsSync(installationSymlinkPath)) {
                this.logger.debug(`No ${symlinkName} directory found in installation, skipping ${symlinkName} symbolic link creation`);
                return;
            }

            // Remove existing .github in workspace if it exists
            if (fs.existsSync(workspaceSymlinkPath)) {
                const stats = fs.lstatSync(workspaceSymlinkPath);
                if (stats.isSymbolicLink()) {
                    fs.unlinkSync(workspaceSymlinkPath);
                    this.logger.debug(`Removed existing ${symlinkName} symbolic link: ${workspaceSymlinkPath}`);
                } else if (stats.isDirectory()) {
                    // If it's a real directory, we should be more cautious
                    this.logger.warn(`Existing ${symlinkName} directory found at ${workspaceSymlinkPath}. Manual intervention may be required.`);
                    vscode.window.showErrorMessage(`Cannot create ${symlinkName} symbolic link because a real directory exists at ${workspaceSymlinkPath}. Please remove or rename it and retry.`);
                    throw new Error(`Existing ${symlinkName} directory prevents symbolic link creation`);
                }
            }

            // Create symbolic link
            fs.symlinkSync(installationSymlinkPath, workspaceSymlinkPath, 'dir');
            this.logger.info(`Created ${symlinkName} symbolic link: ${workspaceSymlinkPath} -> ${installationSymlinkPath}`);

        } catch (error) {
            this.logger.warn(`Failed to create ${symlinkName} symbolic link`, error as Error);
            // Don't fail the installation for symbolic link creation issues
            vscode.window.showErrorMessage(`Failed to create ${symlinkName} symbolic link. Please ensure you have sufficient permissions. Error: ${error instanceof Error ? error.message : String(error)}`);
            throw error;
        }
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
                    vscode.window.showErrorMessage(`Cannot create .olaf symbolic link because a re  al directory exists at ${workspaceOlafPath}. Please remove or rename it and retry.`);
                    throw new Error(`Existing .olaf directory prevents symbolic link creation`);
                }
            }

            // Create symbolic link
            fs.symlinkSync(installationOlafPath, workspaceOlafPath, 'dir');
            this.logger.info(`Created symbolic link: ${workspaceOlafPath} -> ${installationOlafPath}`);

        } catch (error) {
            this.logger.warn('Failed to create workspace symbolic link', error as Error);
            // Don't fail the installation for symbolic link creation issues
            vscode.window.showErrorMessage(`Failed to create workspace .olaf symbolic link. Please ensure you have sufficient permissions. Error: ${error instanceof Error ? error.message : String(error)}`);
            throw error;
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

    /**
     * Check if OLAF is installed in a specific scope
     */
    public async isInstalled(scope: InstallationScope): Promise<boolean> {
        try {
            const platform = await this.platformDetector.detectPlatform();
            const installationPath = this.platformDetector.getInstallationPath(platform.platform, scope);
            const metadataPath = path.join(installationPath, '.olaf', '.olaf-enhanced-metadata.json');

            await access(metadataPath);
            return true;
        } catch {
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

    private async readInstallationMetadata(installationPath: string): Promise<any> {
        const metadataPath = path.join(installationPath, '.olaf', '.olaf-enhanced-metadata.json');
        const metadataContent = await readFile(metadataPath, 'utf8');
        return JSON.parse(metadataContent);
    }
}