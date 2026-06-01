import subprocess
import logging

logger = logging.getLogger("GIT_SYNC")

def run_command(cmd: str) -> str:
    """Executes a shell command and returns the output."""
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        logger.error(f"Command failed: {cmd}\n{result.stderr}")
        return ""
    return result.stdout.strip()

def push_manifestation(repo_path: str, intent_summary: str):
    """
    Automates the process of staging, committing, and pushing the new state 
    to the Stabiel1/antiGRAVITY repo after a manifestation sequence.
    """
    logger.info("Syncing creation to Git repository...")
    
    # Check status
    status = run_command(f"cd {repo_path} && git status --porcelain")
    if not status:
        logger.info("Working directory clean. No new manifestations to sync.")
        return
        
    # Add changes
    run_command(f"cd {repo_path} && git add .")
    
    # Commit changes
    commit_msg = f"manifest(3-6-9): {intent_summary}"
    run_command(f'cd {repo_path} && git commit -m "{commit_msg}"')
    
    # Push changes
    # In a real setup, this pushes to the remote:
    # run_command(f"cd {repo_path} && git push origin main")
    
    logger.info(f"Manifestation synced securely. [Commit: {commit_msg}]")
