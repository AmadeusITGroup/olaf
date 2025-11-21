#!/usr/bin/env python3
"""
OLAF User Feedback Collection Tool

Collects structured user feedback with rating, message, and used prompts,
then sends to backend endpoint via curl.

Usage:
    python collect_user_feedback.py --rating 4 --message "Great tool!"
    python collect_user_feedback.py --rating 3 --message "Good experience" --prompts "code-review,refactor"
    python collect_user_feedback.py --interactive
"""

import subprocess
import json
import sys
import argparse
import platform
from typing import Dict, Any, Optional, List
from pathlib import Path


class UserFeedbackCollector:
    """Collects and submits user feedback to OLAF backend."""
    
    ENDPOINT = "https://uat.digital-logging.saas.amadeus.com/postUILogs"
    APPLICATION_NAME = "OLAF"
    METADATA_FILE = ".olaf/.olaf-enhanced-metadata.json"
    
    def __init__(self, workspace_root: Optional[str] = None):
        """Initialize the feedback collector.
        
        Args:
            workspace_root: Root directory of the workspace. If None, uses current directory.
        """
        self.workspace_root = Path(workspace_root) if workspace_root else Path.cwd()
        self.metadata = self._load_metadata()
    
    def _load_metadata(self) -> Dict[str, Any]:
        """Load session metadata from .olaf-enhanced-metadata.json file.
        
        Returns:
            Dictionary containing metadata or empty dict if file not found.
        """
        metadata_path = self.workspace_root / self.METADATA_FILE
        
        if not metadata_path.exists():
            print(f"⚠️  Warning: Metadata file not found at {metadata_path}")
            return {
                "platform": "unknown",
                "scope": "unknown",
                "osplatform": platform.system(),
                "version": "unknown"
            }
        
        try:
            with open(metadata_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return {
                    "platform": data.get("platform", "unknown"),
                    "scope": data.get("scope", "unknown"),
                    "osplatform": data.get("osplatform", platform.system()),
                    "olaf_version": data.get("version", "unknown")
                }
        except Exception as e:
            print(f"⚠️  Warning: Failed to load metadata: {e}")
            return {
                "platform": "unknown",
                "scope": "unknown",
                "osplatform": platform.system(),
                "olaf_version": "unknown"
            }
    
    def _validate_rating(self, rating: int) -> bool:
        """Validate that rating is between 1 and 4.
        
        Args:
            rating: User satisfaction rating.
            
        Returns:
            True if valid, False otherwise.
        """
        return 1 <= rating <= 4
    
    def _escape_json_string(self, text: str) -> str:
        """Escape special characters in string for JSON.
        
        Args:
            text: String to escape.
            
        Returns:
            Escaped string safe for JSON.
        """
        # Use json.dumps to properly escape the string, then strip the quotes
        return json.dumps(text)[1:-1]
    
    def _build_payload(
        self,
        rating: int,
        user_message: Optional[str] = None,
        prompts_used: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Build JSON payload for feedback submission.
        
        Args:
            rating: User satisfaction rating (1-4).
            user_message: Optional feedback message.
            prompts_used: List of prompts/workflows used.
            
        Returns:
            Dictionary containing the complete payload.
        """
        # Build the message object - stringify it as per requirement
        message_obj = {
            "rating": rating,
            "user_message": user_message if user_message else "",
            "prompts_used": prompts_used if prompts_used else [],
            "session_metadata": {
                "platform": self.metadata.get("platform", "unknown"),
                "scope": self.metadata.get("scope", "unknown"),
                "osplatform": self.metadata.get("osplatform", "unknown"),
                "olaf_version": self.metadata.get("olaf_version", "unknown")
            }
        }
        
        # Stringify the message field as required
        payload = {
            "messages": [{
                "applicationName": self.APPLICATION_NAME,
                "message": json.dumps(message_obj)
            }]
        }
        
        return payload
    
    def submit_feedback(
        self,
        rating: int,
        user_message: Optional[str] = None,
        prompts_used: Optional[List[str]] = None,
        dry_run: bool = False
    ) -> bool:
        """Submit feedback to the backend endpoint.
        
        Args:
            rating: User satisfaction rating (1-4).
            user_message: Optional feedback message.
            prompts_used: List of prompts/workflows used.
            dry_run: If True, only print the command without executing.
            
        Returns:
            True if submission was attempted successfully, False otherwise.
        """
        # Validate rating
        if not self._validate_rating(rating):
            print(f"❌ ERROR: Invalid rating {rating}. Must be between 1 and 4.")
            return False
        
        # Filter out collect-user-feedback from prompts
        if prompts_used:
            prompts_used = [p for p in prompts_used if p != "collect-user-feedback"]
        
        # Build payload
        payload = self._build_payload(rating, user_message, prompts_used)
        payload_json = json.dumps(payload)
        
        print("\n📦 Payload Summary:")
        print(f"   Rating: {rating}/4")
        print(f"   Message: {user_message if user_message else '(none)'}")
        print(f"   Prompts: {', '.join(prompts_used) if prompts_used else '(none)'}")
        print(f"   Platform: {self.metadata.get('platform', 'unknown')}")
        print(f"   OLAF Version: {self.metadata.get('olaf_version', 'unknown')}")
        
        if dry_run:
            print("\n🔍 Dry run - would execute:")
            print(f"   curl -X POST \"{self.ENDPOINT}\" \\")
            print(f"        -H \"Content-Type: application/json\" \\")
            print(f"        -d '{payload_json}'")
            return True
        
        # Execute curl command based on OS
        try:
            if platform.system() == "Windows":
                # Windows PowerShell approach
                ps_script = f"""
$body = '{payload_json}'
Invoke-RestMethod -Uri "{self.ENDPOINT}" -Method Post -ContentType "application/json" -Body $body
"""
                print("\n🚀 Submitting feedback (Windows)...")
                result = subprocess.run(
                    ["powershell", "-Command", ps_script],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
            else:
                # macOS/Linux curl approach
                print("\n🚀 Submitting feedback...")
                result = subprocess.run(
                    [
                        "curl",
                        "-X", "POST",
                        self.ENDPOINT,
                        "-H", "Content-Type: application/json",
                        "-d", payload_json
                    ],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
            
            # Fire-and-forget: we don't validate the response
            print("✅ Feedback submission attempted")
            
            if result.returncode != 0:
                print(f"⚠️  Warning: curl returned exit code {result.returncode}")
                print("   (This is acceptable - fire-and-forget approach)")
            
            return True
            
        except subprocess.TimeoutExpired:
            print("⚠️  Warning: Request timed out")
            print("   (This is acceptable - fire-and-forget approach)")
            return True
            
        except Exception as e:
            print(f"⚠️  Warning: Failed to execute command: {e}")
            print("   (This is acceptable - fire-and-forget approach)")
            return True
    
    def interactive_collect(self) -> bool:
        """Interactively collect feedback from the user.
        
        Returns:
            True if feedback was collected and submitted, False if user declined.
        """
        print("\n🎯 OLAF Feedback Collection")
        print("=" * 50)
        
        # Get user consent
        consent = input("\nWould you like to provide feedback on this session? (yes/no): ").strip().lower()
        if consent not in ['yes', 'y']:
            print("\nNo problem! Let me know if you need anything else.")
            return False
        
        # Collect rating
        while True:
            try:
                rating_input = input("\nRating (1=Very Dissatisfied, 2=Dissatisfied, 3=Satisfied, 4=Very Satisfied): ").strip()
                rating = int(rating_input)
                if self._validate_rating(rating):
                    break
                print("❌ Invalid rating. Please enter a number between 1 and 4.")
            except ValueError:
                print("❌ Invalid input. Please enter a number between 1 and 4.")
        
        # Collect optional message
        user_message = input("\nOptional feedback message (press Enter to skip): ").strip()
        user_message = user_message if user_message else None
        
        # Collect prompts (optional)
        prompts_input = input("\nPrompts/workflows used (comma-separated, press Enter to skip): ").strip()
        prompts_used = [p.strip() for p in prompts_input.split(",")] if prompts_input else None
        
        # Confirm submission
        print("\n" + "=" * 50)
        confirm = input("Submit feedback? (yes/no): ").strip().lower()
        if confirm not in ['yes', 'y']:
            print("\nFeedback collection cancelled.")
            return False
        
        # Submit feedback
        return self.submit_feedback(rating, user_message, prompts_used)


def main():
    """Main entry point for the feedback collection tool."""
    parser = argparse.ArgumentParser(
        description="Collect and submit user feedback for OLAF sessions"
    )
    parser.add_argument(
        "--rating",
        type=int,
        help="User satisfaction rating (1-4)"
    )
    parser.add_argument(
        "--message",
        type=str,
        help="Optional feedback message"
    )
    parser.add_argument(
        "--prompts",
        type=str,
        help="Comma-separated list of prompts/workflows used"
    )
    parser.add_argument(
        "--workspace",
        type=str,
        help="Workspace root directory (default: current directory)"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Interactive mode - prompts for all inputs"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the command without executing it"
    )
    
    args = parser.parse_args()
    
    # Initialize collector
    collector = UserFeedbackCollector(workspace_root=args.workspace)
    
    # Interactive mode
    if args.interactive:
        success = collector.interactive_collect()
        sys.exit(0 if success else 1)
    
    # Non-interactive mode requires rating
    if args.rating is None:
        print("❌ ERROR: --rating is required in non-interactive mode")
        print("   Use --interactive for interactive mode")
        parser.print_help()
        sys.exit(1)
    
    # Parse prompts
    prompts_used = None
    if args.prompts:
        prompts_used = [p.strip() for p in args.prompts.split(",")]
    
    # Submit feedback
    success = collector.submit_feedback(
        rating=args.rating,
        user_message=args.message,
        prompts_used=prompts_used,
        dry_run=args.dry_run
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()