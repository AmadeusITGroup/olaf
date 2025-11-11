import * as assert from 'assert';
import * as vscode from 'vscode';
import { PlatformDetector } from '../../services/platformDetector';
import { Platform, InstallationScope } from '../../types/platform';

describe('PlatformDetector Tests', () => {
    vscode.window.showInformationMessage('Start platform detector tests.');

    it('Should detect platform', async () => {
        const detector = PlatformDetector.getInstance();
        const result = await detector.detectPlatform();
        
        // In test environment, we should detect some platform
        assert.ok(result.platform);
        assert.ok(result.confidence >= 0);
    });

    it('Should get platform configuration', () => {
        const detector = PlatformDetector.getInstance();
        
        const config = detector.getPlatformConfig(Platform.VSCODE);
        assert.strictEqual(config.platform, Platform.VSCODE);
        assert.strictEqual(config.bundlePrefix, 'vscode');
        assert.ok(config.installationPaths.user);
        assert.ok(config.installationPaths.workspace);
        assert.ok(config.installationPaths.project);
    });

    it('Should get installation paths', () => {
        const detector = PlatformDetector.getInstance();
        
        const userPath = detector.getInstallationPath(Platform.VSCODE, InstallationScope.USER);
        const projectPath = detector.getInstallationPath(Platform.VSCODE, InstallationScope.PROJECT);
        
        assert.ok(userPath);
        assert.ok(projectPath);
        
        // Paths should be different
        assert.notStrictEqual(userPath, projectPath);
    });

    it('Should handle different platforms', () => {
        const detector = PlatformDetector.getInstance();
        
        const platforms = [Platform.VSCODE, Platform.WINDSURF, Platform.CURSOR, Platform.KIRO];
        
        for (const platform of platforms) {
            const config = detector.getPlatformConfig(platform);
            assert.strictEqual(config.platform, platform);
            assert.ok(config.bundlePrefix);
            assert.ok(config.installationPaths);
        }
    });

    it('Should return singleton instance', () => {
        const detector1 = PlatformDetector.getInstance();
        const detector2 = PlatformDetector.getInstance();
        
        assert.strictEqual(detector1, detector2);
    });
});
