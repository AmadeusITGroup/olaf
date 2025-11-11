import { InstallationScope } from "./platform";
/**
 * Enhanced metadata types for file integrity verification and modification detection
 */

/**
 * Comprehensive file integrity information including hashes, metadata, and file attributes
 */
export interface FileIntegrityInfo {
    /** Absolute path to the file */
    path: string;
    
    /** SHA-256 hash for cryptographic integrity verification */
    sha256: string;
    
    /** xxHash64 for fast performance verification */
    xxhash64: string;
    
    /** File size in bytes */
    size: number;
    
    /** Original modification time (ISO string) */
    mtime: string;
    
    /** File permissions (Unix-style octal string, e.g., "644") */
    permissions?: string;
    
    /** Whether the file has execute permissions */
    isExecutable?: boolean;
    
    /** Whether the file is a symbolic link */
    isSymlink?: boolean;
    
    /** Target path if this is a symbolic link */
    symlinkTarget?: string;
}

/**
 * Information about detected file modifications
 */
export interface ModificationInfo {
    /** Whether the file has been modified from its original state */
    isModified: boolean;
    
    /** When the modification was detected (ISO string) */
    modifiedAt?: string;
    
    /** Method used to detect the modification */
    verificationType: 'hash' | 'size' | 'time' | 'missing';
    
    /** Original file integrity information */
    originalIntegrity: FileIntegrityInfo;
    
    /** Current state of the file (partial info based on what's available) */
    currentState?: Partial<FileIntegrityInfo>;
}

/**
 * Verification policies for integrity checking
 */
export interface VerificationPolicy {
    /** Automatically verify integrity during operations */
    autoVerify?: boolean;
    
    /** Preserve user-modified files during uninstallation */
    preserveModified?: boolean;
    
    /** Preserve user-created files during uninstallation */
    preserveUserCreated?: boolean;
    
    /** Report modifications to user */
    reportModifications?: boolean;

    // Phase 3: Smart Uninstallation policies
    /** Enable strict mode for enhanced validation */
    strictMode?: boolean;
    
    /** How to handle modified files: 'preserve', 'remove', 'ask' */
    handleModified?: 'preserve' | 'remove' | 'ask';
    
    /** How to handle missing files: 'ignore', 'report', 'error' */
    handleMissing?: 'ignore' | 'report' | 'error';
    
    /** How to handle corrupted files: 'remove', 'preserve', 'ask' */
    handleCorrupted?: 'remove' | 'preserve' | 'ask';
    
    /** Create backup of modified files before removing */
    backupModified?: boolean;
    
    /** Backup directory path for modified files */
    backupPath?: string;
}

/**
 * Enhanced installation metadata with comprehensive file tracking
 */
export interface EnhancedInstallationMetadata {
    // Existing fields from current metadata
    version: string;
    platform: string;
    scope: string;
    installedAt: string;
    osplatform?: string; // OS platform: windows/macos/linux/unknown
    
    // Enhanced bundle information
    bundleInfo: {
        filename: string;
        size: number;
        platform: string;
        /** SHA-256 hash of the installation bundle */
        sha256: string;
        /** Metadata format version for backward compatibility */
        manifestVersion: string;
    };
    
    // Enhanced file tracking with integrity information
    originalFiles: FileIntegrityInfo[];
    extractionPath: string;
    
    // New integrity features
    /** Format version for backward compatibility */
    integrityVersion: string;
    
    /** Last time integrity was verified (ISO string) */
    lastVerification?: string;
    
    /** Verification and handling policies */
    verificationPolicy: VerificationPolicy;
    
    // Rollback capability
    /** Path to backup of original files (if created) */
    backupPath?: string;
    
    /** Whether rollback is supported for this installation */
    rollbackSupported: boolean;
}

/**
 * File categorization for smart uninstallation
 */
export interface FileCategories {
    /** Files that match their original integrity */
    intact: Array<{
        file: string;
        type: 'intact';
        details: ModificationInfo;
        recommendation: 'remove';
    }>;
    
    /** Files that have been modified by the user */
    userModified: Array<{
        file: string;
        type: 'modified';
        details: ModificationInfo;
        recommendation: 'preserve' | 'backup';
    }>;
    
    /** Files that have been deleted */
    deleted: Array<{
        file: string;
        type: 'deleted';
        details: ModificationInfo;
        recommendation: 'ignore';
    }>;
    
    /** Files that appear corrupted */
    corrupted: Array<{
        file: string;
        type: 'corrupted';
        details: ModificationInfo;
        recommendation: 'restore' | 'remove';
    }>;
}

/**
 * Comprehensive integrity report
 */
export interface IntegrityReport {
    /** Total number of files tracked */
    totalFiles: number;
    
    /** Number of files that have been modified */
    modifiedFiles: number;
    
    /** Number of files that have been deleted */
    deletedFiles: number;
    
    /** Number of files that appear corrupted */
    corruptedFiles: number;
    
    /** Number of files that are intact */
    intactFiles: number;
    
    /** Detailed modification information for each file */
    modifications: Array<{
        file: string;
        type: 'modified' | 'deleted' | 'corrupted' | 'intact';
        details: ModificationInfo;
        recommendation: 'preserve' | 'restore' | 'backup' | 'ignore' | 'remove';
    }>;
    
    /** Human-readable summary of the integrity check */
    summary: string;
    
    /** When the report was generated (ISO string) */
    generatedAt: string;
}

/**
 * User decision for uninstallation
 */
export interface UserDecision {
    /** Type of uninstallation chosen */
    action: 'safe' | 'complete' | 'custom' | 'cancel';
    
    /** Timestamp of the decision */
    timestamp: string;
    
    /** Custom file-specific decisions (for 'custom' action) */
    customDecisions?: {
        [filePath: string]: 'preserve' | 'remove' | 'backup';
    };
}

/**
 * Result of uninstallation process
 */
export interface UninstallationResult {
    /** Whether the uninstallation was successful */
    success: boolean;
    
    /** Comprehensive report of what was done */
    report: IntegrityReport;
    
    /** Files that were preserved */
    preservedFiles: string[];
    
    /** Files that were removed */
    removedFiles: string[];
    
    /** Path to backup if one was created */
    backupCreated?: string;
    
    /** Any errors that occurred */
    errors?: string[];
}

/**
 * Result of installation with integrity verification
 */
export interface InstallationResult {
    /** Whether the installation was successful */
    success: boolean;
    
    /** Enhanced metadata with integrity information */
    metadata: EnhancedInstallationMetadata;
    
    /** File integrity information calculated during installation */
    integrityInfo: FileIntegrityInfo[];
    
    /** Whether rollback is available */
    rollbackAvailable: boolean;
    
    warnings?: string[];
}

// Remove duplicate InstallationScope interface and fix UninstallPreview
// Use the existing InstallationScope enum from platform.ts

// Phase 3: Smart Uninstallation Types
export interface ScopeInfo {
    name: string;
    path: string;
    type: 'global' | 'workspace' | 'project';
}

export interface InstallationAnalysis {
    scopes: ScopeInfo[];
    totalFiles: number;
    modifiedFiles: string[];
    userCreatedFiles?: string[];
    estimatedSize?: number;
    fileList?: string[];
    modifiedFileList?: string[];
    userCreatedFileList?: string[];
}

export type UninstallChoice = 'complete' | 'smart' | 'custom' | 'cancel';

export interface UninstallPreview {
    analysis: InstallationAnalysis;
    scope: string;
    recommendedAction: UninstallChoice;
    message?: string;
}
