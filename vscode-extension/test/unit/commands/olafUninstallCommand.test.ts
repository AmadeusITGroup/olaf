import * as assert from 'assert';
import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs-extra';
import * as os from 'os';
import { OlafUninstallCommand } from '../../../src/commands/olafUninstallCommand';

describe('OlafUninstallCommand', () => {
    let tempDir: string;
    let command: OlafUninstallCommand;

    beforeEach(async () => {
        tempDir = await fs.mkdtemp(path.join(os.tmpdir(), 'olaf-test-'));
        command = new OlafUninstallCommand();
    });

    afterEach(async () => {
        if (tempDir && await fs.pathExists(tempDir)) {
            await fs.remove(tempDir);
        }
    });

    it('should create OlafUninstallCommand instance', () => {
        assert.ok(command instanceof OlafUninstallCommand);
    });

    it('should have execute method', () => {
        assert.strictEqual(typeof command.execute, 'function');
    });

    // Integration test would require VS Code API mocking for workspace folders
    // and user input prompts, which is complex for a unit test
    // The real testing happens through the UnifiedUninstaller tests
});
