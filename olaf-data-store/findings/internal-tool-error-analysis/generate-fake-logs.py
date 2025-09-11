#!/usr/bin/env python3
"""
Fake Log Generator for Internal Tool Error Testing
Generates realistic log files with known errors (from structured documentation) and unknown errors
"""

import random
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict
import re

class FakeLogGenerator:
    """Generates realistic log files with known and unknown errors"""
    
    def __init__(self, total_entries: int, error_percentage: float = 1.0):
        self.total_entries = total_entries
        self.error_percentage = error_percentage
        self.error_count = int(total_entries * error_percentage / 100)
        self.normal_count = total_entries - self.error_count
        
        # Known error patterns from documentation
        self.known_errors = {
            "BUILDTOOL-001": [
                "Connection timeout occurred during batch processing operation batch_id: 12345",
                "DB_TIMEOUT error in batch processing module batch_id: 67890",
                "Database connection timeout while processing batch operation",
                "Connection timeout error: batch database operation failed"
            ],
            "BUILDTOOL-002": [
                "OutOfMemoryError in data processing module: Java heap space",
                "Memory allocation failed during data processing operation",
                "java.lang.OutOfMemoryError: Java heap space at DataProcessor.process()",
                "OutOfMemoryError occurred while processing large dataset"
            ],
            "BUILDTOOL-003": [
                "Failed to download artifact com.company:library:1.2.3 from repository",
                "Repository connection failed: HTTP 503 Service Unavailable",
                "HTTP 500 Internal Server Error while accessing repository nexus.company.com",
                "Connection refused connecting to nexus repository server"
            ],
            "BUILDTOOL-004": [
                "Invalid configuration syntax in config.xml line 45",
                "Parse error in configuration file: malformed XML element",
                "Malformed properties file: invalid key-value pair",
                "YAML parse error: invalid indentation in build.yml"
            ],
            "BUILDTOOL-005": [
                "No space left on device /tmp during build operation",
                "Disk full error: cannot write to build directory",
                "IOException: No space left on device while writing build artifacts",
                "ENOSPC error: disk space exhausted during compilation"
            ],
            "BUILDTOOL-006": [
                "SSL certificate expired for repository.company.com",
                "PKIX path building failed: unable to find valid certification path",
                "Certificate validation error: certificate chain incomplete",
                "SSLHandshakeException: certificate verification failed"
            ],
            "BUILDTOOL-007": [
                "Version conflict detected in dependency resolution",
                "Conflicting versions found for library commons-lang",
                "Dependency resolution failed: version convergence error",
                "Dependency convergence failed for artifact group"
            ],
            "BUILDTOOL-008": [
                "Test timeout: integration test exceeded maximum execution time",
                "TestNG timeout exceeded: test method took longer than 300 seconds",
                "JUnit test timed out after 5 minutes of execution",
                "Integration test timeout in DatabaseConnectionTest"
            ],
            "BUILDTOOL-009": [
                "License validation failed for proprietary component XYZ",
                "Proprietary component unauthorized: license check failed",
                "License server unreachable: cannot validate FlexLM license",
                "FlexLM error: license quota exceeded for component"
            ],
            "BUILDTOOL-010": [
                "Quality gate failed: code coverage below 80% threshold",
                "Sonar quality gate failed: technical debt exceeds limit",
                "Code coverage threshold not met: current 65%, required 80%",
                "Technical debt exceeded maximum allowed limit"
            ]
        }
        
        # Unknown error patterns (not in documentation)
        self.unknown_errors = [
            "UNKNOWN_ERROR_001: Cryptographic module initialization failed",
            "NETWORK_TIMEOUT: Unable to reach authentication service after 30 seconds",
            "CACHE_CORRUPTION: Redis cache integrity check failed",
            "PLUGIN_LOAD_ERROR: Failed to load custom plugin module",
            "THREAD_DEADLOCK: Detected potential deadlock in worker threads",
            "FILESYSTEM_PERMISSION: Access denied to secure configuration directory",
            "API_RATE_LIMIT: External service rate limit exceeded",
            "MEMORY_LEAK: Suspected memory leak in background process",
            "ENCODING_ERROR: Character encoding mismatch in input file",
            "VALIDATION_FAILURE: Business rule validation failed unexpectedly"
        ]
        
        # Normal log messages
        self.normal_messages = [
            "INFO: Build process started successfully",
            "DEBUG: Loading configuration from config.xml",
            "INFO: Compiling source files in src/main/java",
            "DEBUG: Resolving dependencies from repository",
            "INFO: Running unit tests",
            "DEBUG: Packaging application artifacts",
            "INFO: Build completed successfully",
            "DEBUG: Cleaning temporary build files",
            "INFO: Publishing artifacts to repository",
            "DEBUG: Generating build reports",
            "INFO: Initializing build environment",
            "DEBUG: Validating project structure",
            "INFO: Processing resource files",
            "DEBUG: Executing pre-build hooks",
            "INFO: Starting compilation phase",
            "DEBUG: Analyzing code dependencies",
            "INFO: Running static code analysis",
            "DEBUG: Generating documentation",
            "INFO: Executing integration tests",
            "DEBUG: Finalizing build process"
        ]
    
    def generate_timestamp(self, base_time: datetime) -> str:
        """Generate realistic timestamp"""
        return base_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    def generate_thread_id(self) -> str:
        """Generate realistic thread ID"""
        return f"[Thread-{random.randint(1, 50)}]"
    
    def generate_log_level(self, is_error: bool = False) -> str:
        """Generate log level"""
        if is_error:
            return random.choice(["ERROR", "FATAL", "WARN"])
        return random.choice(["INFO", "DEBUG", "TRACE"])
    
    def generate_component_name(self) -> str:
        """Generate component/class name"""
        components = [
            "com.company.build.CompilerService",
            "com.company.build.DependencyResolver", 
            "com.company.build.TestRunner",
            "com.company.build.ArtifactPublisher",
            "com.company.build.ConfigurationManager",
            "com.company.build.RepositoryClient",
            "com.company.build.BuildOrchestrator",
            "com.company.build.QualityGate",
            "com.company.build.SecurityScanner",
            "com.company.build.ReportGenerator"
        ]
        return random.choice(components)
    
    def generate_normal_entry(self, timestamp: str) -> str:
        """Generate a normal log entry"""
        thread_id = self.generate_thread_id()
        log_level = self.generate_log_level(False)  # This ensures INFO/DEBUG/TRACE only
        component = self.generate_component_name()
        message = random.choice(self.normal_messages)
        
        # Ensure normal entries never contain error keywords that could cause false matches
        # Sometimes add additional context lines
        entry = f"{timestamp} {thread_id} {log_level} {component} - {message}"
        
        if random.random() < 0.3:  # 30% chance of multi-line entry
            additional_lines = [
                f"{timestamp} {thread_id} {log_level} {component} -   Processing file: src/main/java/Example.java",
                f"{timestamp} {thread_id} {log_level} {component} -   Memory usage: {random.randint(50, 90)}%",
                f"{timestamp} {thread_id} {log_level} {component} -   Duration: {random.randint(100, 5000)}ms"
            ]
            entry += "\n" + "\n".join(random.sample(additional_lines, random.randint(1, 2)))
        
        return entry
    
    def generate_known_error_entry(self, timestamp: str) -> str:
        """Generate an error entry matching known patterns"""
        error_id = random.choice(list(self.known_errors.keys()))
        error_message = random.choice(self.known_errors[error_id])
        
        thread_id = self.generate_thread_id()
        log_level = self.generate_log_level(True)
        component = self.generate_component_name()
        
        # Main error line
        entry = f"{timestamp} {thread_id} {log_level} {component} - {error_message}"
        
        # Add stack trace or additional context for errors
        if random.random() < 0.7:  # 70% chance of additional error context
            context_lines = [
                f"{timestamp} {thread_id} {log_level} {component} -   at {component}.process({component.split('.')[-1]}.java:{random.randint(50, 500)})",
                f"{timestamp} {thread_id} {log_level} {component} -   at com.company.build.Main.main(Main.java:{random.randint(20, 100)})",
                f"{timestamp} {thread_id} {log_level} {component} - Caused by: {random.choice(['java.io.IOException', 'java.sql.SQLException', 'java.net.ConnectException'])}",
                f"{timestamp} {thread_id} {log_level} {component} -   Error code: {random.randint(1000, 9999)}",
                f"{timestamp} {thread_id} {log_level} {component} -   Retry attempt: {random.randint(1, 3)}/3"
            ]
            entry += "\n" + "\n".join(random.sample(context_lines, random.randint(2, 4)))
        
        return entry
    
    def generate_unknown_error_entry(self, timestamp: str) -> str:
        """Generate an error entry that won't match known patterns"""
        error_message = random.choice(self.unknown_errors)
        
        thread_id = self.generate_thread_id()
        log_level = self.generate_log_level(True)
        component = self.generate_component_name()
        
        # Main error line
        entry = f"{timestamp} {thread_id} {log_level} {component} - {error_message}"
        
        # Add context for unknown errors
        if random.random() < 0.5:  # 50% chance of additional context
            context_lines = [
                f"{timestamp} {thread_id} {log_level} {component} -   System state: DEGRADED",
                f"{timestamp} {thread_id} {log_level} {component} -   Error correlation ID: {random.randint(100000, 999999)}",
                f"{timestamp} {thread_id} {log_level} {component} -   Affected subsystem: {random.choice(['AUTH', 'CACHE', 'NETWORK', 'STORAGE'])}"
            ]
            entry += "\n" + "\n".join(random.sample(context_lines, random.randint(1, 2)))
        
        return entry
    
    def generate_log_file(self, output_path: Path) -> Dict[str, int]:
        """Generate the complete log file"""
        base_time = datetime.now() - timedelta(hours=2)
        time_increment = timedelta(seconds=random.uniform(0.1, 5.0))
        
        entries = []
        stats = {
            "total_entries": 0,
            "normal_entries": 0,
            "known_errors": 0,
            "unknown_errors": 0
        }
        
        # Generate all entries
        for i in range(self.total_entries):
            current_time = base_time + (time_increment * i)
            timestamp = self.generate_timestamp(current_time)
            
            # Determine entry type
            if i < self.normal_count:
                entry = self.generate_normal_entry(timestamp)
                stats["normal_entries"] += 1
            else:
                # Split errors between known and unknown (80% known, 20% unknown)
                if random.random() < 0.8:
                    entry = self.generate_known_error_entry(timestamp)
                    stats["known_errors"] += 1
                else:
                    entry = self.generate_unknown_error_entry(timestamp)
                    stats["unknown_errors"] += 1
            
            entries.append(entry)
            stats["total_entries"] += 1
        
        # Shuffle entries to make errors appear randomly throughout the log
        random.shuffle(entries)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            for entry in entries:
                f.write(entry + "\n")
        
        return stats

def main():
    parser = argparse.ArgumentParser(description="Generate fake log files for testing internal tool error analysis")
    parser.add_argument("--entries", "-e", type=int, required=True, help="Total number of log entries to generate")
    parser.add_argument("--error-percentage", "-p", type=float, default=1.0, help="Percentage of entries that should be errors (default: 1.0)")
    parser.add_argument("--output", "-o", type=str, default="fake_build.log", help="Output log file path")
    parser.add_argument("--seed", "-s", type=int, help="Random seed for reproducible output")
    
    args = parser.parse_args()
    
    if args.seed:
        random.seed(args.seed)
    
    # Validate inputs
    if args.error_percentage < 0 or args.error_percentage > 100:
        print("Error: error-percentage must be between 0 and 100")
        return 1
    
    output_path = Path(args.output)
    
    # Generate log file
    print(f"Generating {args.entries} log entries with {args.error_percentage}% errors...")
    generator = FakeLogGenerator(args.entries, args.error_percentage)
    stats = generator.generate_log_file(output_path)
    
    # Print statistics
    print(f"\nLog file generated: {output_path}")
    print(f"Statistics:")
    print(f"  Total entries: {stats['total_entries']}")
    print(f"  Normal entries: {stats['normal_entries']}")
    print(f"  Known errors: {stats['known_errors']}")
    print(f"  Unknown errors: {stats['unknown_errors']}")
    print(f"  Total errors: {stats['known_errors'] + stats['unknown_errors']}")
    print(f"  Actual error percentage: {((stats['known_errors'] + stats['unknown_errors']) / stats['total_entries'] * 100):.2f}%")
    
    return 0

if __name__ == "__main__":
    exit(main())
