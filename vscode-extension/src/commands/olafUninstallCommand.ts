/**
 * Refactored Uninstall Command using UnifiedUninstaller
 * Replaces the complex enhancedUninstallCommand with a clean, simple interface
 */

import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';
import { OlafUninstaller, UninstallOptions, UninstallResult } from '../services/olafUninstaller';
import { Logger } from '../utils/logger';
// import { InstallationManager } from '../services/installationManager';
import { EnhancedInstallationManager } from '../services/enhancedInstallationManager';
import { InstallationScope } from '../types/platform';
import { promisify } from 'util';

const readFile = promisify(fs.readFile);

export class OlafUninstallCommand {
    private readonly olafUninstaller: OlafUninstaller;
    private readonly outputChannel: vscode.OutputChannel;
    private readonly logger: Logger;
    private readonly installationManager: EnhancedInstallationManager;

    constructor() {
        this.olafUninstaller = new OlafUninstaller();
        this.outputChannel = vscode.window.createOutputChannel('OLAF Uninstall');
        this.logger = Logger.getInstance();
        this.installationManager = EnhancedInstallationManager.getInstance();
    }

    /**
     * Main execute method for the unified uninstall command
     */
    async execute(): Promise<void> {
        try {
            this.outputChannel.show();
            this.outputChannel.appendLine('Starting OLAF Uninstallation...');
            
            // Get the target directory (workspace root)
            const workspaceRoot = this.getWorkspaceRoot();
            if (!workspaceRoot) {
                vscode.window.showErrorMessage('No workspace open. Please open a workspace to uninstall OLAF.');
                return;
            }

            // Detect installed scopes and get metadata
            this.outputChannel.appendLine('Detecting OLAF installations...');
            // const installedScopes = await this.installationManager.getInstalledScopes();

                // Load metadata for the selected scope
            this.outputChannel.appendLine(`Trying to load installation metadata...`);
            const metadata = await this.loadMetadataForScope(InstallationScope.PROJECT);
            
            if (!metadata || !metadata.scope) {
                vscode.window.showWarningMessage('No OLAF installations found.');
                return;
            }

            // Ask user for uninstall type
            const uninstallType = await this.promptForUninstallType();
            if (!uninstallType) {
                return; // User cancelled
            }

            // Set up options based on user choice
            const options: UninstallOptions = {
                type: uninstallType,
                targetDir: workspaceRoot,
                createBackup: uninstallType !== 'complete', // Always backup unless complete removal
                metadata: metadata, // Include the loaded metadata
                onProgress: (progress: number, message: string) => {
                    this.outputChannel.appendLine(`[${progress}%] ${message}`);
                    this.logger.info(`Progress: ${progress}% - ${message}`);
                }
            };

            // Handle custom selection if needed
            if (uninstallType === 'custom') {
                options.customSelection = await this.getCustomSelection(workspaceRoot);
                if (!options.customSelection) {
                    return; // User cancelled custom selection
                }
            }

            // Execute the uninstall
            this.outputChannel.appendLine(`\nExecuting ${uninstallType} uninstall...`);
            const result = await this.olafUninstaller.uninstall(options);
            
            // Show results
            await this.showResults(result, uninstallType);

        } catch (error) {
            const errorMessage = error instanceof Error ? error.message : String(error);
            this.outputChannel.appendLine(`Error: ${errorMessage}`);
            this.logger.error('', error as Error);
            
            // Check if this is a safety error about missing metadata
            if (errorMessage.includes('SAFETY ERROR: Cannot uninstall without installation metadata')) {
                // Provide helpful guidance for metadata-related safety errors
                const helpMessage = 'OLAF installation metadata not found. This is a safety protection to prevent accidental deletion of non-OLAF files.\n\nThe smart uninstall feature requires installation metadata to safely identify which files belong to OLAF.';
                const actions = ['Try Legacy Uninstall', 'Show Details', 'Cancel'];
                
                vscode.window.showWarningMessage(helpMessage, ...actions).then(choice => {
                    if (choice === 'Try Legacy Uninstall') {
                        // Offer alternative uninstall method
                        vscode.window.showInformationMessage('Would you like to try the legacy uninstall method instead? This will use the basic uninstall approach.');
                        vscode.commands.executeCommand('olaf.uninstall');
                    } else if (choice === 'Show Details') {
                        this.outputChannel.show(true);
                    }
                });
                return;
            }
            
            const actions = ['Show Details', 'OK'];
            vscode.window.showErrorMessage(`Uninstall failed: ${errorMessage}`, ...actions).then(choice => {
                if (choice === 'Show Details') {
                    this.outputChannel.show(true);
                }
            });
        }
    }

    /**
     * Get the workspace root directory
     */
    private getWorkspaceRoot(): string | undefined {
        const workspaceFolder = vscode.workspace.workspaceFolders?.[0];
        return workspaceFolder?.uri.fsPath;
    }

    /**
     * Prompt user for uninstall type
     */
    private async promptForUninstallType(): Promise<'complete' | 'smart' | 'custom' | undefined> {
        const choices = [
            {
                label: 'Smart Uninstall',
                description: 'Remove original files, preserve your modifications',
                value: 'smart' as const
            },
            {
                label: 'Complete Uninstall', 
                description: 'Remove everything (no backup)',
                value: 'complete' as const
            },
            {
                label: 'Custom Selection',
                description: 'Choose exactly what to remove',
                value: 'custom' as const
            }
        ];

        const selected = await vscode.window.showQuickPick(choices, {
            placeHolder: 'Select uninstall type',
            ignoreFocusOut: true
        });

        return selected?.value;
    }

    /**
     * Prompt user to select installation scope when multiple are available
     */
    private async promptForInstallationScope(installedScopes: InstallationScope[]): Promise<InstallationScope | undefined> {
        const choices = installedScopes.map(scope => ({
            label: scope === InstallationScope.USER ? 'User Installation' : 'Project Installation',
            description: scope === InstallationScope.USER
                ? 'Remove from user profile'
                : 'Remove from current project',
            value: scope
        }));

        const selected = await vscode.window.showQuickPick(choices, {
            placeHolder: 'Select which OLAF installation to uninstall',
            ignoreFocusOut: true
        });

        return selected?.value;
    }

    /**
     * Load metadata for a specific installation scope
     */
    private async loadMetadataForScope(scope: InstallationScope): Promise<any | undefined> {
        try {
            const metadataPath = path.join(vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || '', '.olaf', '.olaf-enhanced-metadata.json');
            const metadataContent = await readFile(metadataPath, 'utf8');
            const metadata = JSON.parse(metadataContent);

            if (!metadata) {
                this.logger.warn(`No metadata found for ${scope} installation`);
                return undefined;
            }

            this.logger.info(`Loaded metadata for ${scope} installation: ${metadata.installedFiles?.length || 0} files`);
            return metadata;
        } catch (error) {
            this.logger.error(`Failed to load metadata for ${scope} installation`, error as Error);
            throw new Error(`Failed to load installation metadata for "${scope}" scope: ${error instanceof Error ? error.message : String(error)}\nIf you believe OLAF is installed, you can remove manually the OLAF files from your workspace or user profile:\n\tolaf-core, olaf-data, or .olaf`);
        }
    }

    /**
     * Get custom file selection from user
     */
    private async getCustomSelection(targetDir: string): Promise<string[] | undefined> {
        // For now, this is a simplified version - in a full implementation,
        // you might want to show a tree view or file picker
        const manualEntry = await vscode.window.showInputBox({
            prompt: 'Enter file paths to remove (comma-separated, relative to workspace root)',
            placeHolder: 'e.g., file1.txt, src/file2.js, folder/file3.py',
            ignoreFocusOut: true
        });

        if (!manualEntry) {
            return undefined;
        }

        return manualEntry
            .split(',')
            .map(file => path.resolve(targetDir, file.trim()))
            .filter(file => file.length > 0);
    }

    /**
     * Show uninstall results to the user
     */
    private async showResults(result: UninstallResult, uninstallType: string): Promise<void> {
        const summary = [
            `\n✅ ${uninstallType} uninstall ${result.success ? 'completed successfully!' : 'encountered errors!'}`,
            ``,
            `📊 Summary:`,
            `  • Files removed: ${result.filesRemoved}`,
            `  • Files preserved: ${result.filesPreserved}`,
            result.backupPath ? `  • Backup created at: ${result.backupPath}` : '  • No backup created',
            ``
        ].join("\n");

        const report:string[] = [];
        // Show errors if any
        if (result.errors.length > 0) {
            report.push(`⚠️ Errors encountered:`);
            result.errors.forEach(error => 
                report.push(`  - ${error}`)
            );
            report.push('');
        }

        // Show detailed file lists
        if (result.details.removed.length > 0) {
            report.push(`📝 Removed files:`);
            result.details.removed.forEach(file => 
                report.push(`  - ${file}`)
            );
            report.push('');
        }

        if (result.details.preserved.length > 0) {
            report.push(`💾 Preserved files:`);
            result.details.preserved.forEach(file => 
                report.push(`  - ${file}`)
            );
            report.push('');
        }

        if (result.details.backedUp.length > 0) {
            report.push(`📦 Backed up files:`);
            result.details.backedUp.forEach(file => 
                report.push(`  - ${file}`)
            );
            report.push('');
        }

        report.push(summary);

        this.outputChannel.appendLine(summary);
        // Output to channel
        // report.forEach(line => this.outputChannel.appendLine(line));

        // Show appropriate message
        if (result.success) {
            const message = result.backupPath 
                ? `Uninstall completed. ${result.filesRemoved} files removed, ${result.filesPreserved} files preserved. Backup: ${path.basename(result.backupPath)}`
                : `Uninstall completed. ${result.filesRemoved} files removed.`;
            
            vscode.window.showInformationMessage(message, 'Show Details').then(choice => {
                if (choice === 'Show Details') {
                    // Ensure output channel is visible and focused
                    this.outputChannel.clear();
                    this.outputChannel.show(true); // true = preserveFocus: false (will focus the output channel)
                    
                    // Add a summary at the top for quick reference
                    this.outputChannel.appendLine('='.repeat(80));
                    this.outputChannel.appendLine('UNINSTALL DETAILS - ' + new Date().toLocaleString());
                    this.outputChannel.appendLine('='.repeat(80));
                    this.outputChannel.appendLine('');
                    report.forEach(line => this.outputChannel.appendLine(line));
                }
            });
        } else {
            vscode.window.showErrorMessage(`Uninstall completed with ${result.errors.length} errors. See output for details.`, 'Show Details').then(choice => {
                if (choice === 'Show Details') {
                    // Ensure output channel is visible and focused
                    this.outputChannel.clear();
                    this.outputChannel.show(true); // true = preserveFocus: false (will focus the output channel)
                    
                    // Add a clear header for error details
                    this.outputChannel.appendLine('='.repeat(80));
                    this.outputChannel.appendLine('UNINSTALL ERROR DETAILS - ' + new Date().toLocaleString());
                    this.outputChannel.appendLine('='.repeat(80));
                    this.outputChannel.appendLine('');
                    
                    // Add detailed console logging for debugging
                    console.error(`[${new Date().toISOString()}] ERROR in olafUninstallCommand:`);
                    console.error('='.repeat(60));
                    if (result.errors && result.errors.length > 0) {
                        console.error(`Found ${result.errors.length} error(s):`);
                        result.errors.forEach((error, index) => {
                            console.error(`  ${index + 1}. ${error}`);
                        });
                    } else {
                        console.error('No specific error details available');
                    }
                    console.error('='.repeat(60));
                }
            });
        }
    }
}
