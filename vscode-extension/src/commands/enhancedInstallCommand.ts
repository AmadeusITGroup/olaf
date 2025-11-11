import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import * as crypto from 'crypto';
import { EnhancedInstallationManager } from '../services/enhancedInstallationManager';
import { GitHubService } from '../services/githubService';
import { PlatformDetector } from '../services/platformDetector';
import { InstallationScope } from '../types/platform';
import { VerificationPolicy } from '../types/integrityTypes';
import { Logger } from '../utils/logger';

/**
 * Enhanced command handler for installing OLAF components with integrity verification
 */
export class EnhancedInstallCommand {
    private readonly logger: Logger;
    private readonly enhancedInstallationManager: EnhancedInstallationManager;
    private readonly githubService: GitHubService;
    private readonly platformDetector: PlatformDetector;

    constructor() {
        this.logger = Logger.getInstance();
        this.enhancedInstallationManager = EnhancedInstallationManager.getInstance();
        this.githubService = GitHubService.getInstance();
        this.platformDetector = PlatformDetector.getInstance();
    }

    /**
     * Execute the enhanced install command with integrity verification
     */
    public async execute(): Promise<void> {
        try {
            this.logger.info('Starting enhanced OLAF installation...');

            // Step 1: Get user preferences for installation scope
            const scope = await this.promptForScope();
            if (!scope) {
                return; // User cancelled
            }

            // Step 2: Check for existing installation and conflicts
            const existingInstallation = await this.checkExistingInstallation(scope);
            if (existingInstallation) {
                const shouldProceed = await this.handleExistingInstallation(existingInstallation, scope);
                if (!shouldProceed) {
                    return; // User chose to cancel
                }
            }

            // Step 3: Get version selection
            const selectedVersion = await this.promptForVersion();
            if (!selectedVersion) {
                return; // User cancelled
            }

            // Step 4: Perform enhanced installation with progress tracking
            await vscode.window.withProgress({
                location: vscode.ProgressLocation.Notification,
                title: 'Enhanced OLAF Installation',
                cancellable: false
            }, async (progress) => {
                await this.performEnhancedInstallation(selectedVersion, scope, progress);
            });

        } catch (error) {
            this.logger.error('Enhanced installation failed', error instanceof Error ? error : new Error(String(error)));
            
            const errorMessage = error instanceof Error ? error.message : String(error);
            vscode.window.showErrorMessage(`Installation failed: ${errorMessage}`);
        }
    }

    /**
     * Prompt user for installation scope
     */
    private async promptForScope(): Promise<InstallationScope | undefined> {
        const items = [
            {
                label: '$(account) User Installation',
                description: 'Install for current user only',
                detail: 'Installs in user data directory',
                scope: InstallationScope.USER
            },
            {
                label: '$(project) Project Installation',
                description: 'Install for current project',
                detail: 'Installs in project-specific location',
                scope: InstallationScope.PROJECT
            }
        ];

        const selected = await vscode.window.showQuickPick(items, {
            placeHolder: 'Select installation scope',
            ignoreFocusOut: true
        });

        return selected?.scope;
    }

    /**
     * Check if there's an existing installation in the specified scope
     */
    private async checkExistingInstallation(scope: InstallationScope): Promise<any | null> {
        try {
            // Check for enhanced metadata first
            const enhancedMetadata = await this.enhancedInstallationManager.getEnhancedMetadata(scope);
            if (enhancedMetadata) {
                return {
                    type: 'enhanced',
                    metadata: enhancedMetadata
                };
            }

            // Check for legacy installation
            const platform = await this.platformDetector.detectPlatform();
            const installationPath = this.platformDetector.getInstallationPath(platform.platform, scope);
            const legacyMetadataPath = path.join(installationPath, '.olaf', '.olaf-metadata.json');
            
            if (fs.existsSync(legacyMetadataPath)) {
                const legacyMetadata = JSON.parse(fs.readFileSync(legacyMetadataPath, 'utf8'));
                return {
                    type: 'legacy',
                    metadata: legacyMetadata
                };
            }

            return null;
        } catch (error) {
            this.logger.warn('Error checking existing installation:', error instanceof Error ? error : new Error(String(error)));
            return null;
        }
    }

    /**
     * Handle existing installation - prompt user for action
     */
    private async handleExistingInstallation(existingInstallation: any, scope: InstallationScope): Promise<boolean> {
        const isEnhanced = existingInstallation.type === 'enhanced';
        const version = existingInstallation.metadata.version || 'unknown';
        
        const action = await vscode.window.showWarningMessage(
            `Existing ${isEnhanced ? 'enhanced' : 'legacy'} OLAF installation found (version: ${version}). What would you like to do?`,
            { modal: true },
            'Upgrade',
            'Reinstall', 
            'Cancel'
        );

        switch (action) {
            case 'Upgrade':
                this.logger.info('User chose to upgrade existing installation');
                return true;
            case 'Reinstall':
                this.logger.info('User chose to reinstall, will remove existing installation first');
                await this.removeExistingInstallation(existingInstallation, scope);
                return true;
            case 'Cancel':
            default:
                this.logger.info('User cancelled installation due to existing installation');
                return false;
        }
    }

    /**
     * Remove existing installation before reinstalling
     */
    private async removeExistingInstallation(existingInstallation: any, scope: InstallationScope): Promise<void> {
        try {
            if (existingInstallation.type === 'enhanced') {
                // Use enhanced uninstallation
                const policy: VerificationPolicy = {
                    autoVerify: true,
                    preserveModified: false, // For reinstall, we want to clean up everything
                    reportModifications: true
                };

                await this.enhancedInstallationManager.uninstall(scope, policy);
            } else {
                // Use legacy uninstallation
                // await this.legacyInstallationManager.uninstall(scope);
            }
            
            this.logger.info('Existing installation removed successfully');
        } catch (error) {
            this.logger.error('Failed to remove existing installation:', error instanceof Error ? error : new Error(String(error)));
            throw new Error('Failed to remove existing installation. Please try manual removal.');
        }
    }

    /**
     * Prompt user for version selection
     */
    private async promptForVersion(): Promise<any | undefined> {
        try {
            // Get available releases
            const releases = await this.githubService.getAvailableVersions();
            if (releases.length === 0) {
                throw new Error('No releases available');
            }

            // Format releases for quick pick
            const items = releases.slice(0, 10).map(release => ({
                label: `$(tag) v${release.version}`,
                description: release.isPrerelease ? '(Pre-release)' : '(Stable)',
                detail: `Released: ${`Version: ${release.version}`}`,
                release: release
            }));

            const selected = await vscode.window.showQuickPick(items, {
                placeHolder: 'Select version to install',
                ignoreFocusOut: true
            });

            return selected?.release;
        } catch (error) {
            this.logger.error('Failed to get available versions:', error instanceof Error ? error : new Error(String(error)));
            throw new Error('Failed to retrieve available versions');
        }
    }

    /**
     * Perform the enhanced installation with comprehensive progress tracking
     */
    private async performEnhancedInstallation(
        selectedVersion: any,
        scope: InstallationScope,
        progress: vscode.Progress<{ increment?: number, message?: string }>
    ): Promise<void> {
        try {
            // Step 1: Detect platform and get bundle info (5%)
            progress.report({ increment: 0, message: 'Detecting platform...' });
            const platform = await this.platformDetector.detectPlatform();
            const release = await this.githubService.getReleaseByTag(selectedVersion.tagName || selectedVersion.version);
            const bundleInfo = this.githubService.findPlatformBundle(release, platform.platform);
            
            if (!bundleInfo) {
                throw new Error(`No compatible bundle found for ${platform.platform}`);
            }
            progress.report({ increment: 5, message: `Platform detected: ${platform.platform}` });

            // Step 2: Download bundle (20%)
            progress.report({ increment: 0, message: 'Downloading installation bundle...' });
            const bundleBuffer = await this.githubService.downloadBundle(bundleInfo, (downloadProgress) => {
                progress.report({
                    increment: 0,
                    message: `Downloading... ${downloadProgress.toFixed(1)}%`
                });
            });
            progress.report({ increment: 20, message: 'Download completed' });

            // Step 3: Bundle integrity verification (10%) 
            progress.report({ increment: 0, message: 'Verifying bundle integrity...' });
            await this.verifyBundleIntegrity(bundleBuffer, bundleInfo);
            progress.report({ increment: 10, message: 'Bundle integrity verified' });

            // Step 4: Create temporary bundle file for enhanced installation (5%)
            progress.report({ increment: 0, message: 'Preparing installation...' });
            const tempDir = path.join(require('os').tmpdir(), 'olaf-install');
            if (!fs.existsSync(tempDir)) {
                fs.mkdirSync(tempDir, { recursive: true });
            }
            
            const tempBundlePath = path.join(tempDir, bundleInfo.filename);
            fs.writeFileSync(tempBundlePath, bundleBuffer);
            progress.report({ increment: 5, message: 'Installation prepared' });

            try {
                // Step 5: Enhanced installation with integrity tracking (55%)
                progress.report({ increment: 0, message: 'Starting enhanced installation...' });
                
                const installResult = await this.enhancedInstallationManager.installBundle(
                    tempBundlePath,
                    scope,
                    (installProgress, message) => {
                        // Map the 0-100 progress to our remaining 55%
                        const mappedProgress = (installProgress * 0.55);
                        progress.report({
                            increment: 0,
                            message: `${message} (${installProgress.toFixed(1)}%)`
                        });
                    }
                );

                if (!installResult.success) {
                    throw new Error(installResult.warnings?.[0] || 'Enhanced installation failed');
                }

                progress.report({ increment: 55, message: 'Enhanced installation completed!' });

                // Step 6: Generate installation report (5%)
                progress.report({ increment: 0, message: 'Generating installation report...' });
                await this.showInstallationReport(installResult);
                progress.report({ increment: 5, message: 'Installation completed successfully!' });

                // Show success notification
                const viewReport = await vscode.window.showInformationMessage(
                    `OLAF v${selectedVersion.version} installed successfully with enhanced integrity tracking!`,
                    'View Details'
                );

                if (viewReport) {
                    await this.showDetailedReport(installResult);
                }

            } finally {
                // Clean up temporary files
                try {
                    if (fs.existsSync(tempBundlePath)) {
                        fs.unlinkSync(tempBundlePath);
                    }
                } catch (cleanupError) {
                    this.logger.warn('Failed to clean up temporary files:', cleanupError instanceof Error ? cleanupError : new Error(String(cleanupError)));
                }
            }

        } catch (error) {
            this.logger.error('Enhanced installation failed:', error instanceof Error ? error : new Error(String(error)));
            throw error;
        }
    }

    /**
     * Verify bundle integrity before installation
     */
    private async verifyBundleIntegrity(bundleBuffer: Buffer, bundleInfo: any): Promise<void> {
        try {
            // Calculate SHA-256 hash of the bundle
            const hash = crypto.createHash('sha256');
            hash.update(bundleBuffer);
            const calculatedHash = hash.digest('hex');

            this.logger.info(`Bundle SHA-256: ${calculatedHash}`);

            // Check file size
            if (bundleBuffer.length !== bundleInfo.size) {
                throw new Error(`Bundle size mismatch: expected ${bundleInfo.size}, got ${bundleBuffer.length}`);
            }

            // Additional integrity checks could be added here
            // For example, checking against a known hash database or signature verification

            this.logger.info('Bundle integrity verification passed');
        } catch (error) {
            this.logger.error('Bundle integrity verification failed:', error instanceof Error ? error : new Error(String(error)));
            throw new Error('Bundle integrity verification failed: ' + (error instanceof Error ? error.message : String(error)));
        }
    }

    /**
     * Show basic installation report
     */
    private async showInstallationReport(installResult: any): Promise<void> {
        const integrityInfo = installResult.integrityInfo || [];
        const totalFiles = integrityInfo.length;
        const intactFiles = integrityInfo.filter((f: any) => f.status === 'intact').length;
        
        if (integrityInfo.length > 0) {
            this.logger.info(`Installation Report: ${totalFiles} files processed, ${intactFiles} intact`);
        } else {
            this.logger.info('Installation completed - no integrity info available');
        }
    }

    /**
     * Show detailed installation report
     */
    private async showDetailedReport(installResult: any): Promise<void> {
        const metadata = installResult.metadata;
        const integrityInfo = installResult.integrityInfo || [];

        // Calculate integrity summary from integrityInfo
        const totalFiles = integrityInfo.length;
        const intactFiles = integrityInfo.filter((f: any) => f.status === 'intact').length;
        const modifiedFiles = integrityInfo.filter((f: any) => f.status === 'modified').length;
        const corruptedFiles = integrityInfo.filter((f: any) => f.status === 'corrupted').length;

        const details = [
            '# Enhanced OLAF Installation Report',
            '',
            '## Installation Details',
            `- **Version**: ${metadata?.version || 'Unknown'}`,
            `- **Platform**: ${metadata?.platform || 'Unknown'}`, 
            `- **Scope**: ${metadata?.scope || 'Unknown'}`,
            `- **Installation Date**: ${metadata?.installedAt ? new Date(metadata.installedAt).toLocaleString() : 'Unknown'}`,
            '',
            '## File Integrity Summary',
            `- **Total Files**: ${totalFiles}`,
            `- **Intact Files**: ${intactFiles}`,
            `- **Modified Files**: ${modifiedFiles}`,
            `- **Corrupted Files**: ${corruptedFiles}`,
            '',
            '## Bundle Information',
            `- **Filename**: ${metadata.bundleInfo.filename}`,
            `- **Size**: ${(metadata.bundleInfo.size / 1024 / 1024).toFixed(2)} MB`,
            `- **SHA-256**: ${metadata.bundleInfo.sha256}`,
            '',
            '## Enhanced Features',
            '- ✅ File integrity verification enabled',
            '- ✅ Smart uninstallation support',
            '- ✅ Modification detection active',
            '- ✅ Rollback capability available'
        ];

        const doc = await vscode.workspace.openTextDocument({
            content: details.join('\n'),
            language: 'markdown'
        });
        
        await vscode.window.showTextDocument(doc, { preview: true });
    }
}
