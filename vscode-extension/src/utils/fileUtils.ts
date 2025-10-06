import * as fs from 'fs';
import * as path from 'path';
import { promisify } from 'util';

const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);
const mkdir = promisify(fs.mkdir);
const access = promisify(fs.access);
const stat = promisify(fs.stat);
const readdir = promisify(fs.readdir);
const unlink = promisify(fs.unlink);
const rmdir = promisify(fs.rmdir);

/**
 * File utility functions for OLAF extension
 */
export class FileUtils {
    /**
     * Check if a file or directory exists
     */
    public static async exists(filePath: string): Promise<boolean> {
        try {
            await access(filePath);
            return true;
        } catch {
            return false;
        }
    }

    /**
     * Ensure a directory exists, creating it if necessary
     */
    public static async ensureDirectory(dirPath: string): Promise<void> {
        if (!(await this.exists(dirPath))) {
            await mkdir(dirPath, { recursive: true });
        }
    }

    /**
     * Read a file as a string
     */
    public static async readFile(filePath: string): Promise<string> {
        return await readFile(filePath, 'utf8');
    }

    /**
     * Write a string to a file
     */
    public static async writeFile(filePath: string, content: string): Promise<void> {
        await this.ensureDirectory(path.dirname(filePath));
        await writeFile(filePath, content, 'utf8');
    }

    /**
     * Read a file as JSON
     */
    public static async readJson<T = any>(filePath: string): Promise<T> {
        const content = await this.readFile(filePath);
        return JSON.parse(content);
    }

    /**
     * Write an object to a file as JSON
     */
    public static async writeJson(filePath: string, obj: any): Promise<void> {
        const content = JSON.stringify(obj, null, 2);
        await this.writeFile(filePath, content);
    }

    /**
     * Get file statistics
     */
    public static async getStats(filePath: string): Promise<fs.Stats> {
        return await stat(filePath);
    }

    /**
     * Check if a path is a directory
     */
    public static async isDirectory(filePath: string): Promise<boolean> {
        try {
            const stats = await this.getStats(filePath);
            return stats.isDirectory();
        } catch {
            return false;
        }
    }

    /**
     * Check if a path is a file
     */
    public static async isFile(filePath: string): Promise<boolean> {
        try {
            const stats = await this.getStats(filePath);
            return stats.isFile();
        } catch {
            return false;
        }
    }

    /**
     * List directory contents
     */
    public static async listDirectory(dirPath: string): Promise<string[]> {
        return await readdir(dirPath);
    }

    /**
     * Delete a file
     */
    public static async deleteFile(filePath: string): Promise<void> {
        await unlink(filePath);
    }

    /**
     * Delete a directory recursively
     */
    public static async deleteDirectory(dirPath: string): Promise<void> {
        await rmdir(dirPath, { recursive: true });
    }

    /**
     * Copy a file from source to destination
     */
    public static async copyFile(source: string, destination: string): Promise<void> {
        await this.ensureDirectory(path.dirname(destination));
        const content = await readFile(source);
        await writeFile(destination, content);
    }

    /**
     * Get file size in bytes
     */
    public static async getFileSize(filePath: string): Promise<number> {
        const stats = await this.getStats(filePath);
        return stats.size;
    }

    /**
     * Get formatted file size string
     */
    public static formatFileSize(bytes: number): string {
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        if (bytes === 0) {return '0 Bytes';}
        
        const i = Math.floor(Math.log(bytes) / Math.log(1024));
        const size = bytes / Math.pow(1024, i);
        
        return `${Math.round(size * 100) / 100} ${sizes[i]}`;
    }

    /**
     * Sanitize a filename by removing invalid characters
     */
    public static sanitizeFilename(filename: string): string {
        return filename.replace(/[<>:"/\\|?*]/g, '_');
    }

    /**
     * Join paths safely
     */
    public static joinPaths(...paths: string[]): string {
        return path.join(...paths);
    }

    /**
     * Get the basename of a path
     */
    public static getBasename(filePath: string): string {
        return path.basename(filePath);
    }

    /**
     * Get the directory name of a path
     */
    public static getDirname(filePath: string): string {
        return path.dirname(filePath);
    }

    /**
     * Get the file extension
     */
    public static getExtension(filePath: string): string {
        return path.extname(filePath);
    }

    /**
     * Change file extension
     */
    public static changeExtension(filePath: string, newExt: string): string {
        const parsed = path.parse(filePath);
        return path.join(parsed.dir, parsed.name + newExt);
    }
}
