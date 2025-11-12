/**
 * Unified Uninstaller - Single, Clean Interface for OLAF Uninstallation
 * 
 * This module provides a single, well-tested uninstall interface that handles
 * all scenarios: complete, smart, and custom uninstallation.
 * 
 * Design Principles:
 * - Single responsibility: Only handles uninstallation
 * - Clear interface: Simple options and results
 * - Testable: All behavior is unit tested
 * - Reliable: Graceful error handling and recovery
 */

import * as fs from 'fs-extra';
import * as path from 'path';
import * as os from 'os';
import * as vscode from 'vscode';
import { FileIntegrityService } from './fileIntegrityService';
import { FileIntegrityInfo, EnhancedInstallationMetadata } from '../types/integrityTypes';
import { PlatformDetector } from './platformDetector';
import { Platform, InstallationScope } from '../types/platform';
import { Logger } from '../utils/logger';

/**
 * Types of uninstallation operations
 */
export type UninstallType = 'complete' | 'smart' | 'custom';

/**
 * File categorization for uninstallation decisions
 */
export interface FileCategory {
    path: string;
    size: number;
    mtime: Date;
    category: 'original' | 'modified' | 'userCreated' | 'missing';
}

/**
 * Categorized files for uninstall processing
 */
export interface FileCategorization {
    original: FileCategory[];
    modified: FileCategory[];
    userCreated: FileCategory[];
    missing: FileCategory[];
}

/**
 * Installation metadata for file categorization
 */
export interface InstallationMetadata {
    originalFiles: FileIntegrityInfo[];
    modifiedFiles: FileIntegrityInfo[];
    userCreatedFiles: FileIntegrityInfo[];
    installationPath: string;
    installationDate: string;
}

/**
 * Uninstall operation options
 */
export interface UninstallOptions {
    /** Type of uninstall operation */
    type: UninstallType;
    
    /** Target directory to uninstall from */
    targetDir: string;
    
    /** Whether to create backup of preserved files */
    createBackup: boolean;
    
    /** Custom file selection (required for 'custom' type) */
    customSelection?: string[];
    
    /** Installation metadata for file categorization */
    metadata?: EnhancedInstallationMetadata;
    
    /** Progress callback */
    onProgress?: (progress: number, message: string) => void;
}

/**
 * Result of uninstall operation
 */
export interface UninstallResult {
    /** Whether the operation was successful */
    success: boolean;
    
    /** Number of files successfully removed */
    filesRemoved: number;
    
    /** Number of files preserved */
    filesPreserved: number;
    
    /** Path to backup directory (if created) */
    backupPath?: string;
    
    /** List of errors encountered */
    errors: string[];
    
    /** Detailed breakdown of what happened */
    details: {
        removed: string[];
        preserved: string[];
        backedUp: string[];
        failed: string[];
    };
}

/**
 * Unified Uninstaller Class
 *
 * Handles all uninstallation scenarios with a single, clean interface.
 * Designed for reliability, testability, and clear user experience.
 */
export class OlafUninstaller {
    private readonly integrityService: FileIntegrityService;
    private readonly platformDetector: PlatformDetector;
    private readonly logger: Logger;

    constructor() {
        this.integrityService = new FileIntegrityService();
        this.platformDetector = PlatformDetector.getInstance();
        this.logger = Logger.getInstance();
    }
    
    /**
     * Perform uninstallation based on provided options
     */
    async uninstall(options: UninstallOptions): Promise<UninstallResult> {
        const validationError = this.validateOptions(options);
        if (validationError) {
            return {
                success: false,
                filesRemoved: 0,
                filesPreserved: 0,
                errors: [validationError],
                details: {
                    removed: [],
                    preserved: [],
                    backedUp: [],
                    failed: []
                }
            };
        }
        
        const result: UninstallResult = {
            success: false,
            filesRemoved: 0,
            filesPreserved: 0,
            errors: [],
            details: {
                removed: [],
                preserved: [],
                backedUp: [],
                failed: []
            }
        };

        try {
            options.onProgress?.(0, 'Starting uninstallation...');

            // Detect installation scope and platform
            const platformInfo = await this.platformDetector.detectPlatform();
            const installationScope = options.metadata?.scope === "user" ? InstallationScope.USER : InstallationScope.PROJECT;
            const installationPath = this.platformDetector.getInstallationPath(platformInfo.platform, installationScope);
            const projectFolder = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
            
            if (options.type === 'complete') {
                options.onProgress?.(5, 'Performing complete uninstallation...');
            }
            
            // Step 1: Categorize files
            options.onProgress?.(10, 'Categorizing files...');
            const categories = await this.categorizeFiles(options.targetDir, options.metadata);
            
            // Step 2: Determine what to remove/preserve based on type
            options.onProgress?.(30, 'Determining file actions...');
            const actions = await this.planActions(categories, options);
            
            // Step 3: Create backup if needed
            if (options.createBackup && actions.preserve.length > 0) {
                options.onProgress?.(50, 'Creating backup...');
                result.backupPath = await this.createBackup(actions.preserve, options.targetDir);
                result.details.backedUp = actions.preserve.map(f => f.path);
            }
            
            // Step 4: Remove files
            options.onProgress?.(70, 'Removing files...');
            await this.removeFiles(actions.remove, result);

            
            // Step 5: Update counts
            result.filesRemoved = result.details.removed.length;
            result.filesPreserved = actions.preserve.length;
            result.details.preserved = actions.preserve.map(f => f.path);
            result.success = true;

            // Step 6: If there is a .olaf symbolic link in the project's root, remove it
            if (projectFolder) {
                const projectOlafPath = path.join(projectFolder, '.olaf');
                const stats = await vscode.workspace.fs.stat(vscode.Uri.file(projectOlafPath));
                const isSymlink = (stats.type & vscode.FileType.SymbolicLink) !== 0;
                if (installationScope === InstallationScope.USER) {
                    if (isSymlink) {
                        fs.unlinkSync(projectOlafPath);
                    }
                    await fs.remove(path.join(installationPath, ".olaf"));
                }
                else if (installationScope === InstallationScope.PROJECT) {
                    await fs.remove(projectOlafPath);
                }
            }

            // Step 7: Update platform-specific configurations
            options.onProgress?.(90, 'Updating platform configurations...');
            await this.updatePlatformConfiguration(platformInfo.platform, installationScope, installationPath);
            
            options.onProgress?.(100, 'Uninstallation completed');
            
        } catch (error) {
            console.error('[UnifiedUninstaller] Error during uninstall:', error);
            result.errors.push(error instanceof Error ? error.message : String(error));
            result.success = false;
        }

        return result;
    }

    /**
     * Categorize files based on installation metadata and current state using checksum comparison
     *
     * Categories:
     * - original: Files that match their original checksums (unmodified since installation)
     * - modified: Files that were installed but have been modified (checksum mismatch)
     * - missing: Files that were installed but no longer exist
     * - userCreated: Files that exist in .olaf but were not part of the original installation
     */
    async categorizeFiles(targetDir: string, metadata?: EnhancedInstallationMetadata): Promise<FileCategorization> {
        const categories: FileCategorization = {
            original: [],
            modified: [],
            userCreated: [],
            missing: []
        };

        if (!metadata) {
            // CRITICAL SAFETY: Never scan arbitrary directories without metadata!
            // This prevents catastrophic deletion of entire workspaces including .git
            throw new Error('SAFETY ERROR: Cannot uninstall without installation metadata. ' +
                          'This prevents accidental deletion of non-OLAF files. ' +
                          'Installation metadata is required to identify which files were actually installed by OLAF.');
        }

        // Get all files currently in the .olaf directory
        // Resolve the .olaf path to handle cases where it's a symbolic link
        const olafDirPath = path.join(targetDir, '.olaf');
        let resolvedOlafPath: string;
        try {
            resolvedOlafPath = await fs.realpath(olafDirPath);
        } catch (error) {
            // If .olaf directory doesn't exist or can't be resolved, use original path
            resolvedOlafPath = olafDirPath;
        }

        const currentFiles = await this.scanDirectory(resolvedOlafPath);
        // Create a map with both original and resolved paths for lookup
        const currentFileMap = new Map<string, FileCategory>();
        for (const file of currentFiles) {
            currentFileMap.set(file.path, file);
            // Also add resolved path if different
            try {
                const resolvedPath = await fs.realpath(file.path);
                if (resolvedPath !== file.path) {
                    currentFileMap.set(resolvedPath, file);
                }
            } catch {
                // Ignore errors
            }
        }

        // Process all originally installed files from metadata
        // Note: EnhancedInstallationMetadata only contains 'originalFiles' - files that were installed
        for (const originalFile of metadata.originalFiles || []) {
            let currentFile = currentFileMap.get(originalFile.path);
            // If not found, try with resolved path
            if (!currentFile) {
                try {
                    const resolvedPath = await fs.realpath(originalFile.path);
                    currentFile = currentFileMap.get(resolvedPath);
                } catch {
                    // File doesn't exist
                }
            }
            const category = await this.categorizeFileWithChecksum(originalFile, currentFile);
            this.addToCategory(categories, category);
        }

        // Find files that exist in .olaf but are not in the original installation manifest
        // These are user-created files that appeared after installation
        const originalFilePaths = new Set<string>();
        for (const originalFile of metadata.originalFiles || []) {
            originalFilePaths.add(originalFile.path);
            // Also add resolved path if different
            try {
                const resolvedPath = await fs.realpath(originalFile.path);
                if (resolvedPath !== originalFile.path) {
                    originalFilePaths.add(resolvedPath);
                }
            } catch {
                // File doesn't exist
            }
        }

        for (const currentFile of currentFiles) {
            // Check if this file path (or its resolved version) is in the original files
            let isOriginal = originalFilePaths.has(currentFile.path);
            if (!isOriginal) {
                try {
                    const resolvedPath = await fs.realpath(currentFile.path);
                    isOriginal = originalFilePaths.has(resolvedPath);
                } catch {
                    // Can't resolve, use original check
                }
            }
            
            if (!isOriginal) {
                // This is a user-created file not tracked in the original installation
                categories.userCreated.push({
                    path: currentFile.path,
                    size: currentFile.size,
                    mtime: currentFile.mtime,
                    category: 'userCreated'
                });
            }
        }

        return categories;
    }

    /**
     * Plan what actions to take on each file category
     */
    private async planActions(categories: FileCategorization, options: UninstallOptions) {
        const remove: FileCategory[] = [];
        const preserve: FileCategory[] = [];

        switch (options.type) {
            case 'complete':
                // Remove everything that exists
                remove.push(...categories.original, ...categories.modified, ...categories.userCreated);
                break;
                
            case 'smart':
                // Remove original files, preserve modified and user-created
                remove.push(...categories.original);
                preserve.push(...categories.modified, ...categories.userCreated);
                break;
                
            case 'custom': {
                if (!options.customSelection) {
                    throw new Error('Custom selection required for custom uninstall');
                }
                
                // Normalize custom selection paths for comparison
                const normalizedSelection = new Set<string>();
                for (const filePath of options.customSelection) {
                    normalizedSelection.add(filePath);
                    // Also add resolved path if different
                    try {
                        const resolvedPath = await fs.realpath(filePath);
                        if (resolvedPath !== filePath) {
                            normalizedSelection.add(resolvedPath);
                        }
                    } catch {
                        // File doesn't exist, keep original path
                    }
                }
                
                // Only remove files in custom selection
                const allFiles = [...categories.original, ...categories.modified, ...categories.userCreated];
                const metadataFiles = new Set(allFiles.map(f => f.path));
                for (const file of allFiles) {
                    if (normalizedSelection.has(file.path)) {
                        remove.push(file);
                    } else {
                        preserve.push(file);
                    }
                }

                // Handle files in customSelection that are not in metadata
                for (const filePath of options.customSelection) {
                    if (!metadataFiles.has(filePath)) {
                        try {
                            const stats = await fs.stat(filePath);
                            remove.push({
                                path: filePath,
                                size: stats.size,
                                mtime: stats.mtime,
                                category: 'original'
                            });
                        } catch {
                            // File does not exist, skip silently
                        }
                    }
                }
                break;
            }
        }

        return { remove, preserve };
    }

    /**
     * Create backup of the entire .olaf folder
     */
    private async createBackup(files: FileCategory[], sourceDir: string): Promise<string> {
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const backupPath = path.join(os.tmpdir(), `olaf-backup-${timestamp}`);

        // Backup the entire .olaf directory
        const olafDirPath = path.join(sourceDir, '.olaf');

        // Resolve the .olaf path in case it's a symbolic link
        let resolvedOlafPath: string;
        try {
            resolvedOlafPath = await fs.realpath(olafDirPath);
        } catch (error) {
            // If .olaf directory doesn't exist or can't be resolved, use original path
            resolvedOlafPath = olafDirPath;
        }

        // Ensure source and destination are different
        if (path.resolve(resolvedOlafPath) === path.resolve(backupPath)) {
            throw new Error('Source and destination must not be the same');
        }

        // Copy the entire .olaf directory to backup location
        await fs.copy(resolvedOlafPath, backupPath);

        return backupPath;
    }

    /**
     * Remove files and update result
     */
    private async removeFiles(files: FileCategory[], result: UninstallResult): Promise<void> {
        for (const file of files) {
            try {
                if (await fs.pathExists(file.path)) {
                    await fs.remove(file.path);
                    result.details.removed.push(file.path);
                }
            } catch (error) {
                const errorMsg = `Failed to remove ${file.path}: ${error instanceof Error ? error.message : String(error)}`;
                result.errors.push(errorMsg);
                result.details.failed.push(file.path);
            }
        }
    }

    /**
     * Categorize a single file using checksum comparison
     */
    private async categorizeFileWithChecksum(
        manifestFile: FileIntegrityInfo,
        currentFile: FileCategory | undefined
    ): Promise<FileCategory> {
        if (!currentFile) {
            // File is missing
            return {
                path: manifestFile.path,
                size: manifestFile.size,
                mtime: new Date(manifestFile.mtime),
                category: 'missing'
            };
        }

        try {
            // Compare checksums to determine if file has been modified
            const modificationInfo = await this.integrityService.verifyFileIntegrity(
                manifestFile.path,
                manifestFile
            );

            if (modificationInfo.isModified) {
                // File exists but has been modified from its original state
                // Use currentFile.path (resolved) for consistency with scanDirectory
                return {
                    path: currentFile.path,
                    size: currentFile.size,
                    mtime: currentFile.mtime,
                    category: 'modified'
                };
            } else {
                // File matches its original checksum - it's original/unmodified
                // Use currentFile.path (resolved) for consistency with scanDirectory
                return {
                    path: currentFile.path,
                    size: currentFile.size,
                    mtime: currentFile.mtime,
                    category: 'original'
                };
            }
        } catch (error) {
            // If we can't verify integrity, treat as missing
            return {
                path: manifestFile.path,
                size: manifestFile.size,
                mtime: new Date(manifestFile.mtime),
                category: 'missing'
            };
        }
    }

    /**
     * Helper method to add a categorized file to the appropriate category
     */
    private addToCategory(categories: FileCategorization, fileCategory: FileCategory): void {
        switch (fileCategory.category) {
            case 'original':
                categories.original.push(fileCategory);
                break;
            case 'modified':
                categories.modified.push(fileCategory);
                break;
            case 'userCreated':
                categories.userCreated.push(fileCategory);
                break;
            case 'missing':
                categories.missing.push(fileCategory);
                break;
        }
    }

    /**
     * Scan directory for all files, resolving symbolic links to their actual paths
     */
    private async scanDirectory(dirPath: string, visitedPaths: Set<string> = new Set()): Promise<FileCategory[]> {
        const files: FileCategory[] = [];

        // Prevent infinite loops by tracking visited paths
        try {
            const realDirPath = await fs.realpath(dirPath);
            if (visitedPaths.has(realDirPath)) {
                return files; // Already visited this directory
            }
            visitedPaths.add(realDirPath);
        } catch (error) {
            // If we can't resolve the path, use the original path for cycle detection
            if (visitedPaths.has(dirPath)) {
                return files;
            }
            visitedPaths.add(dirPath);
        }

        try {
            const entries = await fs.readdir(dirPath, { withFileTypes: true });

            for (const entry of entries) {
                const fullPath = path.join(dirPath, entry.name);

                try {
                    // Use lstat to detect symlinks properly (doesn't follow symlinks)
                    const lStats = await fs.lstat(fullPath);

                    if (lStats.isDirectory()) {
                        // Regular directory - scan recursively
                        const subFiles = await this.scanDirectory(fullPath, visitedPaths);
                        files.push(...subFiles);
                    } else if (lStats.isSymbolicLink()) {
                        // Symbolic link - determine if it points to a file or directory
                        try {
                            const targetStats = await fs.stat(fullPath); // This follows the symlink
                            const resolvedPath = await fs.realpath(fullPath);

                            if (targetStats.isDirectory()) {
                                // Directory symlink - scan the resolved directory
                                const subFiles = await this.scanDirectory(resolvedPath, visitedPaths);
                                files.push(...subFiles);
                            } else {
                                // File symlink - add the resolved file
                                files.push({
                                    path: resolvedPath, // Use resolved path for symbolic links
                                    size: targetStats.size,
                                    mtime: targetStats.mtime,
                                    category: 'original'
                                });
                            }
                        } catch (error) {
                            // Broken symlink or inaccessible - skip it
                            continue;
                        }
                    } else {
                        // Regular file - resolve path to handle cases where parent directories are symlinks
                        try {
                            const resolvedPath = await fs.realpath(fullPath);
                            files.push({
                                path: resolvedPath,
                                size: lStats.size,
                                mtime: lStats.mtime,
                                category: 'original'
                            });
                        } catch (error) {
                            // If realpath fails, use original path
                            files.push({
                                path: fullPath,
                                size: lStats.size,
                                mtime: lStats.mtime,
                                category: 'original'
                            });
                        }
                    }
                } catch (error) {
                    // Skip files/directories that can't be accessed
                    continue;
                }
            }
        } catch (error) {
            // Directory doesn't exist or is inaccessible
        }

        return files;
    }

    /**
     * Validate uninstall options
     */
    private validateOptions(options: UninstallOptions): string | null {
        if (!options.targetDir) {
            return 'Target directory is required';
        }
        
        if (!fs.pathExistsSync(options.targetDir)) {
            return 'Target directory is required';
        }
        
        if (options.type === 'custom' && (!options.customSelection || options.customSelection.length === 0)) {
            return 'Custom selection required for custom uninstall';
        }
        
        if (options.customSelection) {
            for (const filePath of options.customSelection) {
                if (!path.resolve(filePath).startsWith(path.resolve(options.targetDir))) {
                    return `Invalid file path outside target directory: ${filePath}`;
                }
            }
        }
        return null;
    }

    private uninstallAll(): void {
        // Placeholder for uninstallAll method
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

    private async removeSymbolicLink(scope: InstallationScope, installationPath: string, symlinkName: string): Promise<void> {
        try {
            const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
            if (!workspaceRoot) {
                this.logger.debug(`No workspace folder found, skipping ${symlinkName} symbolic link removal`);
                return;
            }

            const githubLinkPath = path.join(workspaceRoot, symlinkName);

            if (fs.existsSync(githubLinkPath)) {
                const stats = fs.lstatSync(githubLinkPath);
                if (stats.isSymbolicLink()) {
                    const linkTarget = fs.readlinkSync(githubLinkPath);
                    const expectedTarget = path.join(installationPath, symlinkName);

                    if (path.resolve(path.dirname(githubLinkPath), linkTarget) === path.resolve(expectedTarget)) {
                        fs.unlinkSync(githubLinkPath);
                        await fs.remove(path.join(installationPath, symlinkName));
                        this.logger.info(`Removed ${symlinkName} symbolic link: ${githubLinkPath}`);
                    } else {
                        this.logger.warn(`${symlinkName} symbolic link points to different location, not removing: ${githubLinkPath} -> ${linkTarget}`);
                    }
                } else if (scope === InstallationScope.PROJECT) {
                    await fs.remove(githubLinkPath);
                } else {
                    this.logger.debug(`${symlinkName} is not a symbolic link, not removing: ${githubLinkPath}`);
                }
            } else {
                this.logger.debug(`No ${symlinkName} symbolic link found at: ${githubLinkPath}`);
            }
        } catch (error) {
            this.logger.warn(`Failed to remove ${symlinkName} symbolic link`, error as Error);
            // Don't fail the uninstallation for symbolic link removal issues
        }
    }

    private async updateVSCodeConfiguration(
        scope: InstallationScope,
        installationPath: string
    ): Promise<void> {
        // Remove symbolic link to .github if it exists
        await this.removeSymbolicLink(scope, installationPath, ".github");
    }

    private async updateWindsurfConfiguration(
        scope: InstallationScope,
        installationPath: string
    ): Promise<void> {
        // Placeholder for Windsurf configuration update logic
        // Remove symbolic link to .github if it exists
        await this.removeSymbolicLink(scope, installationPath, ".windsurf");
    }

    private async updateKiroConfiguration(
        scope: InstallationScope,
        installationPath: string
    ): Promise<void> {
        // Placeholder for Kiro configuration update logic
        // Remove symbolic link to .github if it exists
        await this.removeSymbolicLink(scope, installationPath, ".kiro");
    }

    private async updateCursorConfiguration(
        scope: InstallationScope,
        installationPath: string
    ): Promise<void> {
        // Placeholder for Cursor configuration update logic
        // Remove symbolic link to .github if it exists
        await this.removeSymbolicLink(scope, installationPath, ".cursor");
    }
}
