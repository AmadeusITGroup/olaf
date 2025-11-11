import * as vscode from 'vscode';
import { selectVersionCommand } from './commands/selectVersionCommand';
import { UpdateCommand } from './commands/updateCommand';
import { StatusCommand } from './commands/statusCommand';
import { ValidateAccessCommand } from './commands/validateAccessCommand';
// import { UninstallCommand } from './commands/uninstallCommand';
import { OlafUninstallCommand } from './commands/olafUninstallCommand';
import { EnhancedInstallCommand } from './commands/enhancedInstallCommand';
import { StatusBar } from './ui/statusBar';
import { Notifications } from './ui/notifications';
import { UpdateManager } from './services/updateManager';
import { InstallationManager } from './services/installationManager';
import { Logger } from './utils/logger';

/**
 * Main extension class that handles activation, deactivation, and command registration
 */
export class OlafExtension {
    private logger: Logger;
    private statusBar: StatusBar;
    private notifications: Notifications;
    private updateManager: UpdateManager;
    private installationManager: InstallationManager;
    private disposables: vscode.Disposable[] = [];

    constructor(private context: vscode.ExtensionContext) {
        this.logger = Logger.getInstance();
        this.statusBar = StatusBar.getInstance();
        this.notifications = Notifications.getInstance();
        this.updateManager = UpdateManager.getInstance();
        this.installationManager = InstallationManager.getInstance();
    }

    /**
     * Activate the extension
     */
    public async activate(): Promise<void> {
        try {
            this.logger.info('Activating OLAF extension...');

            // Register commands
            this.registerCommands();

            // Initialize UI components
            await this.initializeUI();

            // Check for automatic updates if enabled
            await this.checkAutoUpdates();

            // Check if this is first run and show welcome message
            await this.checkFirstRun();

            this.logger.info('OLAF extension activated successfully');

        } catch (error) {
            this.logger.error('Failed to activate OLAF extension', error as Error);
            await this.notifications.showError(
                `Failed to activate OLAF extension: ${(error as Error).message}`,
                'Show Logs'
            ).then((action) => {
                if (action === 'Show Logs') {
                    this.logger.show();
                }
            });
        }
    }

    /**
     * Deactivate the extension
     */
    public deactivate(): void {
        try {
            this.logger.info('Deactivating OLAF extension...');

            // Dispose of all resources
            this.disposables.forEach(disposable => disposable.dispose());
            this.disposables = [];

            // Dispose UI components
            this.statusBar.dispose();
            this.logger.dispose();

            this.logger.info('OLAF extension deactivated successfully');

        } catch (error) {
            console.error('Error during OLAF extension deactivation:', error);
        }
    }

    /**
     * Register all extension commands
     */
    private registerCommands(): void {

        const updateCommand = new UpdateCommand();
        const statusCommand = new StatusCommand();
        const validateAccessCommand = new ValidateAccessCommand();
        // const uninstallCommand = new UninstallCommand(this.installationManager, this.logger);
        const enhancedInstallCommand = new EnhancedInstallCommand();
        const olafUninstallCommand = new OlafUninstallCommand();

        // Register command handlers
        const commands = [
            vscode.commands.registerCommand('olaf.selectVersion', () => selectVersionCommand()),
            vscode.commands.registerCommand('olaf.update', () => updateCommand.execute()),
            vscode.commands.registerCommand('olaf.checkUpdates', () => statusCommand.checkUpdates()),
            vscode.commands.registerCommand('olaf.showVersion', () => statusCommand.showVersion()),
            vscode.commands.registerCommand('olaf.uninstall', () => olafUninstallCommand.execute()),
            vscode.commands.registerCommand('olaf.showHelp', () => statusCommand.showHelp()),
            vscode.commands.registerCommand('olaf.validateAccess', () => validateAccessCommand.execute()),
            // vscode.commands.registerCommand('olaf.uninstallAll', () => uninstallCommand.executeUninstallAll()),
            vscode.commands.registerCommand('olaf.enhancedInstall', () => enhancedInstallCommand.execute()),
            // vscode.commands.registerCommand('olaf.enhancedUninstall', () => refactoredUninstallCommand.execute()),
        ];

        // Add to disposables
        this.disposables.push(...commands);

        // Add to context subscriptions
        this.context.subscriptions.push(...commands);

        this.logger.debug('Commands registered successfully');
    }

    /**
     * Initialize UI components
     */
    private async initializeUI(): Promise<void> {
        try {
            // Initialize status bar
            await this.statusBar.initialize();

            // Add status bar to disposables
            this.disposables.push(this.statusBar);

            this.logger.debug('UI components initialized successfully');

        } catch (error) {
            this.logger.error('Failed to initialize UI components', error as Error);
        }
    }

    /**
     * Check for automatic updates if enabled in configuration
     */
    private async checkAutoUpdates(): Promise<void> {
        try {
            const config = vscode.workspace.getConfiguration('olaf');
            const autoCheckUpdates = config.get<boolean>('autoCheckUpdates', true);

            if (!autoCheckUpdates) {
                this.logger.debug('Automatic update checking is disabled');
                return;
            }

            this.logger.debug('Checking for automatic updates...');

            // Check if OLAF is installed
            const installedScopes = await this.installationManager.getInstalledScopes();
            if (installedScopes.length === 0) {
                this.logger.debug('OLAF not installed, skipping update check');
                return;
            }

            // Perform update check in background
            setTimeout(async () => {
                try {
                    await this.statusBar.checkAndUpdateStatus();
                } catch (error) {
                    this.logger.warn('Background update check failed', error as Error);
                }
            }, 5000); // Wait 5 seconds before checking

        } catch (error) {
            this.logger.warn('Failed to perform automatic update check', error as Error);
        }
    }

    /**
     * Check if this is the first run and show welcome message
     */
    private async checkFirstRun(): Promise<void> {
        try {
            const isFirstRun = this.context.globalState.get<boolean>('olaf.firstRun', true);

            if (isFirstRun) {
                // Mark as not first run
                await this.context.globalState.update('olaf.firstRun', false);

                // Check if OLAF is already installed
                const installedScopes = await this.installationManager.getInstalledScopes();
                if (installedScopes.length === 0) {
                    // Show welcome notification after a short delay
                    setTimeout(async () => {
                        await this.notifications.showWelcomeNotification();
                    }, 2000);
                }

                this.logger.info('First run detected, welcome message shown');
            }

        } catch (error) {
            this.logger.warn('Failed to check first run status', error as Error);
        }
    }
}

// Extension activation function called by VS Code
export async function activate(context: vscode.ExtensionContext): Promise<void> {
    const extension = new OlafExtension(context);
    await extension.activate();
}

// Extension deactivation function called by VS Code
export function deactivate(): void {
    // The deactivation logic is handled by the OlafExtension class
    // This function is kept for VS Code API compatibility
}
