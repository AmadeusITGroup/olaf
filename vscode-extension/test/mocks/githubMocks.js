/**
 * GitHub API Mocks for Testing
 * Provides mock responses to avoid rate limiting during tests
 */

const mockRelease = {
    tag_name: "v2.1.0",
    name: "OLAF v2.1.0",
    body: "## Features\n- Enhanced installation support\n- Better error handling\n\n## Bug Fixes\n- Fixed platform detection\n- Improved logging",
    prerelease: false,
    published_at: "2024-01-15T10:00:00Z",
    assets: [
        {
            name: "olaf-linux-x64.tar.gz",
            browser_download_url: "https://github.com/microsoft/olaf/releases/download/v2.1.0/olaf-linux-x64.tar.gz",
            size: 12345678,
            content_type: "application/gzip"
        },
        {
            name: "olaf-win32-x64.zip", 
            browser_download_url: "https://github.com/microsoft/olaf/releases/download/v2.1.0/olaf-win32-x64.zip",
            size: 13456789,
            content_type: "application/zip"
        },
        {
            name: "olaf-darwin-x64.tar.gz",
            browser_download_url: "https://github.com/microsoft/olaf/releases/download/v2.1.0/olaf-darwin-x64.tar.gz", 
            size: 12789456,
            content_type: "application/gzip"
        }
    ]
};

const mockReleases = [
    mockRelease,
    {
        tag_name: "v2.0.1",
        name: "OLAF v2.0.1", 
        body: "## Bug Fixes\n- Fixed critical installation issue\n- Updated dependencies",
        prerelease: false,
        published_at: "2024-01-10T14:30:00Z",
        assets: [
            {
                name: "olaf-linux-x64.tar.gz",
                browser_download_url: "https://github.com/microsoft/olaf/releases/download/v2.0.1/olaf-linux-x64.tar.gz",
                size: 12000000,
                content_type: "application/gzip"
            }
        ]
    }
];

const mockPrerelease = {
    tag_name: "v2.2.0-beta.1",
    name: "OLAF v2.2.0 Beta 1",
    body: "## Beta Features\n- Experimental new installer\n- Preview of upcoming features",
    prerelease: true,
    published_at: "2024-01-20T16:45:00Z",
    assets: [
        {
            name: "olaf-linux-x64-beta.tar.gz",
            browser_download_url: "https://github.com/microsoft/olaf/releases/download/v2.2.0-beta.1/olaf-linux-x64-beta.tar.gz",
            size: 13000000,
            content_type: "application/gzip"
        }
    ]
};

/**
 * Mock GitHub API Service
 */
class MockGitHubService {
    constructor() {
        this.callCount = {};
    }

    _incrementCall(method) {
        this.callCount[method] = (this.callCount[method] || 0) + 1;
    }

    async getLatestRelease(includePrerelease = false) {
        this._incrementCall('getLatestRelease');
        return includePrerelease ? mockPrerelease : mockRelease;
    }

    async getAllReleases() {
        this._incrementCall('getAllReleases');
        return [...mockReleases, mockPrerelease];
    }

    async getSpecificRelease(tagName) {
        this._incrementCall('getSpecificRelease');
        const allReleases = [...mockReleases, mockPrerelease];
        const release = allReleases.find(r => r.tag_name === tagName);
        
        if (!release) {
            const error = new Error(`Release ${tagName} not found`);
            error.status = 404;
            throw error;
        }
        
        return release;
    }

    getCallCount(method) {
        return this.callCount[method] || 0;
    }

    resetCallCounts() {
        this.callCount = {};
    }
}

module.exports = {
    MockGitHubService,
    mockRelease,
    mockReleases,
    mockPrerelease
};
