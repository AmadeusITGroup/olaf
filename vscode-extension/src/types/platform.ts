/**
 * Supported VSCode platforms and their detection signatures
 */
export enum Platform {
  VSCODE = 'vscode',
  WINDSURF = 'windsurf',
  KIRO = 'kiro',
  CURSOR = 'cursor',
  UNKNOWN = 'unknown'
}

/**
 * Platform detection result with confidence level
 */
export interface PlatformDetectionResult {
  platform: Platform;
  confidence: number; // 0-1, where 1 is certain
  version?: string;
  executablePath?: string;
  environment?: Record<string, string>;
}

/**
 * Platform-specific configuration for installations
 */
export interface PlatformConfig {
  platform: Platform;
  bundlePrefix: string; // e.g., 'vscode', 'windsurf'
  installationPaths: {
    user: string;
    workspace: string;
    project: string;
  };
  configFiles: string[];
  environmentVariables: string[];
}

/**
 * Installation scope options
 */
export enum InstallationScope {
  USER = 'user',
  PROJECT = 'project'
}
