import * as vscode from 'vscode';
import { UpdateManager } from '../services/updateManager';
import { Logger } from '../utils/logger';
import { EnhancedInstallationManager } from '../services/enhancedInstallationManager';

/**
 * Command handler for checking OLAF updates
 */
export class StatusCommand {
    private readonly logger: Logger;
    private readonly updateManager: UpdateManager;
    private readonly installationManager: EnhancedInstallationManager;

    constructor() {
        this.logger = Logger.getInstance();
        this.updateManager = UpdateManager.getInstance();
        this.installationManager = EnhancedInstallationManager.getInstance();
    }

    /**
     * Execute the check updates command
     */
    public async checkUpdates(): Promise<void> {
        try {
            this.logger.info('Checking for OLAF updates...');

            const installedScopes = await this.installationManager.getInstalledScopes();
            if (installedScopes.length === 0) {
                await vscode.window.showInformationMessage(
                    'OLAF is not installed. Would you like to install it now?',
                    'Install OLAF'
                ).then((action) => {
                    if (action === 'Install OLAF') {
                        vscode.commands.executeCommand('olaf.enhancedInstall');
                    }
                });
                return;
            }

            const updateChecks = await vscode.window.withProgress(
                {
                    location: vscode.ProgressLocation.Notification,
                    title: 'Checking for updates...',
                    cancellable: false
                },
                async () => {
                    return await this.updateManager.checkForUpdates();
                }
            );

            const message = this.updateManager.getUpdateNotificationMessage(updateChecks);
            const updatesAvailable = updateChecks.filter(check => check.hasUpdate);

            if (updatesAvailable.length > 0) {
                await vscode.window.showInformationMessage(
                    message,
                    'Update Now',
                    'Show Details'
                ).then((action) => {
                    if (action === 'Update Now') {
                        vscode.commands.executeCommand('olaf.update');
                    } else if (action === 'Show Details') {
                        this.showUpdateDetails(updateChecks);
                    }
                });
            } else {
                await vscode.window.showInformationMessage(message);
            }

        } catch (error) {
            this.logger.error('Failed to check for updates', error as Error);
            await vscode.window.showErrorMessage(
                `Failed to check for updates: ${(error as Error).message}`,
                'Show Logs'
            ).then((action) => {
                if (action === 'Show Logs') {
                    this.logger.show();
                }
            });
        }
    }

    /**
     * Execute the show version command
     */
    public async showVersion(): Promise<void> {
        try {
            this.logger.info('Showing OLAF version information...');

            const installedScopes = await this.installationManager.getInstalledScopes();
            if (installedScopes.length === 0) {
                await vscode.window.showInformationMessage(
                    'OLAF is not installed.',
                    'Install OLAF'
                ).then((action) => {
                    if (action === 'Install OLAF') {
                        vscode.commands.executeCommand('olaf.enhancedInstall');
                    }
                });
                return;
            }

            const versionInfo: string[] = [];
            
            for (const scope of installedScopes) {
                const installationInfo = await this.installationManager.getInstallationInfo(scope);
                if (installationInfo) {
                    versionInfo.push(
                        `${scope.toUpperCase()}: v${installationInfo.version} (${installationInfo.platform})`
                    );
                }
            }

            const message = `OLAF Installation Information:\n\n${versionInfo.join('\n')}`;

            await vscode.window.showInformationMessage(
                message,
                'Check for Updates',
                'Show Installation Folder'
            ).then((action) => {
                if (action === 'Check for Updates') {
                    vscode.commands.executeCommand('olaf.checkUpdates');
                } else if (action === 'Show Installation Folder') {
                    this.showInstallationFolder(installedScopes[0]);
                }
            });

        } catch (error) {
            this.logger.error('Failed to show version information', error as Error);
            await vscode.window.showErrorMessage(
                `Failed to get version information: ${(error as Error).message}`
            );
        }
    }

    /**
     * Execute the uninstall command
     */
    public async uninstall(): Promise<void> {
        try {
            this.logger.info('Starting OLAF uninstallation...');

            const installedScopes = await this.installationManager.getInstalledScopes();
            if (installedScopes.length === 0) {
                await vscode.window.showInformationMessage('OLAF is not installed.');
                return;
            }

            const scopeToUninstall = await this.selectUninstallScope(installedScopes);
            if (!scopeToUninstall) {
                return; // User cancelled
            }

            const confirmMessage = scopeToUninstall === 'all' 
                ? 'Are you sure you want to uninstall OLAF from all scopes? This action cannot be undone.'
                : `Are you sure you want to uninstall OLAF from ${scopeToUninstall} scope? This action cannot be undone.`;

            const confirm = await vscode.window.showWarningMessage(
                confirmMessage,
                'Uninstall',
                'Cancel'
            );

            if (confirm !== 'Uninstall') {
                return;
            }

            await vscode.window.withProgress(
                {
                    location: vscode.ProgressLocation.Notification,
                    title: 'Uninstalling OLAF',
                    cancellable: false
                },
                async (progress) => {
                    if (scopeToUninstall === 'all') {
                        let successCount = 0;
                        for (const scope of installedScopes) {
                            progress.report({ 
                                increment: 0, 
                                message: `Uninstalling from ${scope} scope...` 
                            });
                            
                            const success = await this.installationManager.uninstall(scope);
                            if (success) {
                                successCount++;
                            }
                        }

                        if (successCount === installedScopes.length) {
                            await vscode.window.showInformationMessage(
                                'OLAF uninstalled successfully from all scopes!'
                            );
                        } else {
                            await vscode.window.showWarningMessage(
                                `OLAF partially uninstalled: ${successCount}/${installedScopes.length} successful`
                            );
                        }
                    } else {
                        progress.report({ 
                            increment: 0, 
                            message: `Uninstalling from ${scopeToUninstall} scope...` 
                        });
                        
                        const success = await this.installationManager.uninstall(scopeToUninstall as any);
                        
                        if (success) {
                            await vscode.window.showInformationMessage(
                                `OLAF uninstalled successfully from ${scopeToUninstall} scope!`
                            );
                        } else {
                            throw new Error('Uninstallation failed');
                        }
                    }
                }
            );

        } catch (error) {
            this.logger.error('Uninstallation failed', error as Error);
            await vscode.window.showErrorMessage(
                `Failed to uninstall OLAF: ${(error as Error).message}`,
                'Show Logs'
            ).then((action) => {
                if (action === 'Show Logs') {
                    this.logger.show();
                }
            });
        }
    }

    /**
     * Show help documentation
     */
    public async showHelp(): Promise<void> {
        const helpContent = `
# OLAF VSCode Extension Help

## What is OLAF?
Open Lightweight Assistant Framework (OLAF) is an AI assistant framework designed to enhance interactions between users and AI agents through natural language interaction.

## Commands
- **Install OLAF**: Install OLAF components in your chosen scope
- **Check for Updates**: Check if newer versions are available
- **Update**: Update to the latest version
- **Show Version**: Display current version information
- **Uninstall**: Remove OLAF components

## Installation Scopes
- **User**: Available across all workspaces for current user
- **Workspace**: Available only in current workspace
- **Project**: Available only in current project

## Support
For issues and support, visit: https://github.com/AmadeusITGroup/olaf

## Configuration
Configure OLAF behavior in VS Code settings under "OLAF" section.
        `.trim();

        const panel = vscode.window.createWebviewPanel(
            'olafHelp',
            'OLAF Help',
            vscode.ViewColumn.One,
            {}
        );

        panel.webview.html = `
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>OLAF Help</title>
                <style>
                    body { 
                        font-family: var(--vscode-font-family);
                        font-size: var(--vscode-font-size);
                        color: var(--vscode-foreground);
                        background-color: var(--vscode-editor-background);
                        line-height: 1.6;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }
                    h1, h2 { color: var(--vscode-textPreformat-foreground); }
                    code { 
                        background-color: var(--vscode-textBlockQuote-background);
                        padding: 2px 4px;
                        border-radius: 3px;
                    }
                </style>
            </head>
            <body>
                <pre>${helpContent}</pre>
            </body>
            </html>
        `;
    }

    private async showUpdateDetails(updateChecks: any[]): Promise<void> {
        const details = updateChecks.map(check => {
            if (check.hasUpdate) {
                return `${check.scope}: ${check.currentVersion} → ${check.latestVersion}`;
            } else {
                return `${check.scope}: ${check.currentVersion} (up to date)`;
            }
        }).join('\n');

        await vscode.window.showInformationMessage(
            `OLAF Update Details:\n\n${details}`,
            'Update Now'
        ).then((action) => {
            if (action === 'Update Now') {
                vscode.commands.executeCommand('olaf.update');
            }
        });
    }

    private async showInstallationFolder(scope: any): Promise<void> {
        try {
            const installationInfo = await this.installationManager.getInstallationInfo(scope);
            if (installationInfo) {
                // Implementation would show the installation folder
                vscode.commands.executeCommand('revealFileInOS', vscode.Uri.file(installationInfo.installedPath || ''));
            }
        } catch (error) {
            this.logger.error('Failed to show installation folder', error as Error);
        }
    }

    private async selectUninstallScope(installedScopes: any[]): Promise<string | undefined> {
        if (installedScopes.length === 1) {
            return installedScopes[0];
        }

        const quickPickItems: vscode.QuickPickItem[] = [
            {
                label: '🗑️ Uninstall All',
                description: `Remove OLAF from all ${installedScopes.length} scopes`,
                detail: 'all'
            },
            ...installedScopes.map(scope => ({
                label: `📁 Uninstall from ${scope}`,
                description: `Remove OLAF from ${scope} scope only`,
                detail: scope
            }))
        ];

        const selectedItem = await vscode.window.showQuickPick(quickPickItems, {
            title: 'Select Uninstall Scope',
            placeHolder: 'Choose which installation to remove',
            ignoreFocusOut: true
        });

        return selectedItem?.detail;
    }
}
