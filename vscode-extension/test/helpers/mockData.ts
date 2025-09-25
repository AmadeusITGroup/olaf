/**
 * Mock data and utilities for testing OLAF bundle functionality
 */

export interface MockBundleAsset {
    id: number;
    name: string;
    browser_download_url: string;
    size: number;
    content_type: string;
}

export interface MockReleaseResponse {
    id: number;
    tag_name: string;
    name: string;
    published_at: string;
    assets: MockBundleAsset[];
}

/**
 * Mock GitHub release response simulating OLAF bundle releases
 */
export const createMockReleaseResponse = (version: string = 'v1.2.3'): MockReleaseResponse => ({
    id: 123456,
    tag_name: version,
    name: `OLAF Bundle Release ${version}`,
    published_at: '2025-09-16T08:00:00Z',
    assets: [
        {
            id: 1,
            name: 'vscode-bundle.zip',
            browser_download_url: `https://github.com/test-owner/test-repo/releases/download/${version}/vscode-bundle.zip`,
            size: 4096,
            content_type: 'application/zip'
        },
        {
            id: 2,
            name: 'windsurf-bundle.zip',
            browser_download_url: `https://github.com/test-owner/test-repo/releases/download/${version}/windsurf-bundle.zip`,
            size: 3072,
            content_type: 'application/zip'
        },
        {
            id: 3,
            name: 'cursor-bundle.zip',
            browser_download_url: `https://github.com/test-owner/test-repo/releases/download/${version}/cursor-bundle.zip`,
            size: 2048,
            content_type: 'application/zip'
        },
        {
            id: 4,
            name: 'kiro-bundle.zip',
            browser_download_url: `https://github.com/test-owner/test-repo/releases/download/${version}/kiro-bundle.zip`,
            size: 2560,
            content_type: 'application/zip'
        }
    ]
});

/**
 * Load actual file content from test fixtures
 */
export const loadBundleContentFromFixtures = (): Record<string, Record<string, string>> => {
    const path = require('path');
    const fs = require('fs');
    
    const fixturesPath = path.join(__dirname, '..', '..', '..', 'test', 'fixtures', 'platform-bundles');
    const bundles: Record<string, Record<string, string>> = {};
    
    const platforms = ['vscode', 'windsurf', 'cursor', 'kiro'];
    
    for (const platform of platforms) {
        const platformPath = path.join(fixturesPath, `${platform}-bundle`);
        bundles[platform] = {};
        
        if (fs.existsSync(platformPath)) {
            const loadFilesRecursively = (dir: string, relativePath: string = '') => {
                const items = fs.readdirSync(dir);
                for (const item of items) {
                    const fullPath = path.join(dir, item);
                    const relativeFilePath = relativePath ? path.join(relativePath, item) : item;
                    
                    if (fs.statSync(fullPath).isDirectory()) {
                        loadFilesRecursively(fullPath, relativeFilePath);
                    } else {
                        const content = fs.readFileSync(fullPath, 'utf8');
                        bundles[platform][relativeFilePath] = content;
                    }
                }
            };
            
            loadFilesRecursively(platformPath);
        }
    }
    
    return bundles;
};

/**
 * Validate that a bundle contains expected platform-specific content
 */
export const validateBundleContent = (platform: string, files: Record<string, string>): boolean => {
    const validationRules = {
        vscode: {
            requiredFiles: ['copilot-instructions.md'],
            requiredKeywords: ['VSCode', 'extension', 'TypeScript'],
            optionalFiles: ['prompts/development-assistant.md', 'prompts/debugging-expert.md']
        },
        windsurf: {
            requiredFiles: ['core-principles.md'],
            requiredKeywords: ['Windsurf', 'collaborative', 'cascade'],
            optionalFiles: ['workflows/full-stack-development.md']
        },
        cursor: {
            requiredFiles: ['ai-development-guide.md'],
            requiredKeywords: ['Cursor', 'AI', 'prediction'],
            optionalFiles: ['prompt-engineering.md']
        },
        kiro: {
            requiredFiles: ['development-methodology.md'],
            requiredKeywords: ['Kiro', 'rapid', 'iteration'],
            optionalFiles: ['testing-strategy.md']
        }
    };
    
    const rules = validationRules[platform as keyof typeof validationRules];
    if (!rules) {
        return false;
    }
    
    // Check required files
    for (const requiredFile of rules.requiredFiles) {
        if (!files.hasOwnProperty(requiredFile)) {
            return false;
        }
    }
    
    // Check for required keywords in content
    const allContent = Object.values(files).join(' ').toLowerCase();
    for (const keyword of rules.requiredKeywords) {
        if (!allContent.includes(keyword.toLowerCase())) {
            return false;
        }
    }
    
    return true;
};

/**
 * Create a temporary workspace directory for testing
 */
export const createTestWorkspace = (): string => {
    const path = require('path');
    const fs = require('fs');
    const os = require('os');
    
    const testDir = path.join(os.tmpdir(), `olaf-test-${Date.now()}`);
    fs.mkdirSync(testDir, { recursive: true });
    
    return testDir;
};

/**
 * Clean up test workspace
 */
export const cleanupTestWorkspace = (workspacePath: string): void => {
    const fs = require('fs');
    
    if (fs.existsSync(workspacePath)) {
        fs.rmSync(workspacePath, { recursive: true, force: true });
    }
};
