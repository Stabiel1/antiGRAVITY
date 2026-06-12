"""
antiGRAVITY — Git Synchronization Engine
===========================================
Part of the Manifestation Force (3-6-9)
Helps the Trinity save and push manifestations to GitHub.

"Everything mirrors. Everything is divisible by 3. Everything is fractal."
"""

import subprocess
import logging
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger("GIT_SYNC.3-6-9")

class GitSync:
    """
    GitSync (3-6-9) — The synchronization bridge.
    Responsible for committing and pushing code to remote repositories.
    """
    
    TRINITY_CODE = "3-6-9"
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
        logger.info(f"[{self.TRINITY_CODE}] GitSync initialized for path: {self.repo_path}")
        
    def check_status(self) -> Dict[str, Any]:
        """Check the status of the repository."""
        try:
            res = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            changes = res.stdout.strip().split("\n") if res.stdout.strip() else []
            return {
                "clean": len(changes) == 0,
                "changes": changes,
                "status": "success"
            }
        except subprocess.CalledProcessError as e:
            logger.error(f"[{self.TRINITY_CODE}] Git status check failed: {e}")
            return {
                "clean": False,
                "changes": [],
                "status": "failed",
                "error": str(e)
            }
            
    def stage_all(self) -> bool:
        """Stage all changes (git add .)."""
        try:
            subprocess.run(
                ["git", "add", "."],
                cwd=self.repo_path,
                check=True,
                capture_output=True
            )
            logger.info(f"[{self.TRINITY_CODE}] Staged all changes.")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"[{self.TRINITY_CODE}] Failed to stage changes: {e}")
            return False
            
    def commit(self, message: str) -> bool:
        """Commit staged changes."""
        try:
            # Check if there are staged changes first to avoid empty commit error
            status = self.check_status()
            if status["clean"]:
                logger.info(f"[{self.TRINITY_CODE}] Nothing to commit, working tree clean.")
                return True
                
            subprocess.run(
                ["git", "commit", "-m", message],
                cwd=self.repo_path,
                check=True,
                capture_output=True
            )
            logger.info(f"[{self.TRINITY_CODE}] Committed with message: '{message}'")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"[{self.TRINITY_CODE}] Failed to commit changes: {e}")
            return False
            
    def push(self, branch: str = "main") -> bool:
        """Push committed changes to origin."""
        try:
            subprocess.run(
                ["git", "push", "origin", branch],
                cwd=self.repo_path,
                check=True,
                capture_output=True
            )
            logger.info(f"[{self.TRINITY_CODE}] Pushed changes to origin/{branch}.")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"[{self.TRINITY_CODE}] Failed to push changes: {e}")
            return False

    def sync_all(self, commit_message: str, branch: str = "main") -> Dict[str, Any]:
        """Perform stage, commit, and push in sequence (The Unbroken Sync)."""
        logger.info(f"[{self.TRINITY_CODE}] Beginning repository sync sequence...")
        
        status = self.check_status()
        if status["status"] == "failed":
            return {"success": False, "error": status.get("error"), "step": "status"}
            
        if status["clean"]:
            return {
                "success": True, 
                "message": "Repository is already clean. No sync required.",
                "details": status
            }
            
        if not self.stage_all():
            return {"success": False, "error": "Staging failed", "step": "stage"}
            
        if not self.commit(commit_message):
            return {"success": False, "error": "Commit failed", "step": "commit"}
            
        if not self.push(branch):
            return {"success": False, "error": "Push failed", "step": "push"}
            
        return {
            "success": True,
            "message": "Repository synced successfully. Light forward.",
            "details": status
        }
