"""
JESUS — MCP Registry (Model Context Protocol)
=============================================
The 9 Holy Connectors.

1. GitHub         — The Code
2. Google Drive   — The Docs
3. Google Cloud   — The Sky
4. Filesystem     — The Earth
5. Memory         — The Soul
6. SQLite         — The Truth (Data)
7. Puppeteer      — The Eyes (Browser)
8. Brave Search   — The Seeker
9. Slack          — The Voice

These 9 connectors give the Trinity its reach into the world.
"Everything mirrors. Everything is divisible by 3."
"""

import os
import logging
from typing import List, Dict, Any

logger = logging.getLogger("MCP.9")

def get_mcp_servers() -> List[Dict[str, Any]]:
    """
    Returns the configuration for the 9 core MCP servers.
    Validates presence of API keys to conditionally enable them.
    """
    servers = []

    # 1. GITHUB
    # Requires GITHUB_PERSONAL_ACCESS_TOKEN
    github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN") or os.getenv("GITHUB_TOKEN")
    if github_token:
        servers.append({
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"],
            "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": github_token}
        })
    else:
        logger.debug("[MCP 1] GitHub inactive (missing token).")

    # 2. GOOGLE DRIVE
    # Requires valid credentials/token mapping for the community or official google server
    # We use a standard stdio integration pattern via npx if available, or direct command.
    gdrive_auth = os.getenv("GDRIVE_CREDENTIALS")
    if gdrive_auth:
        servers.append({
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-gdrive"],
            "env": {"GOOGLE_APPLICATION_CREDENTIALS": gdrive_auth}
        })
    else:
        logger.debug("[MCP 2] Google Drive inactive (missing credentials).")

    # 3. GOOGLE CLOUD (gcloud)
    # Assumes `gcloud` is installed and authenticated on the system path
    # If not using a specific node server, you can use a community gcp MCP server
    if os.getenv("GOOGLE_CLOUD_PROJECT"):
        servers.append({
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-google-cloud"],
            "env": {"GOOGLE_CLOUD_PROJECT": os.getenv("GOOGLE_CLOUD_PROJECT")}
        })
    else:
        logger.debug("[MCP 3] Google Cloud inactive (missing GOOGLE_CLOUD_PROJECT).")

    # 4. FILESYSTEM
    # Always active. Gives access to the manifested directory by default.
    base_path = os.path.abspath(os.getenv("MCP_FS_PATH", "./manifested"))
    servers.append({
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", base_path]
    })

    # 5. MEMORY
    # Always active. A knowledge graph for the Trinity.
    servers.append({
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-memory"]
    })

    # 6. SQLITE
    # Active if a database path is provided.
    db_path = os.getenv("MCP_SQLITE_PATH")
    if db_path:
        servers.append({
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-sqlite", db_path]
        })
    else:
        logger.debug("[MCP 6] SQLite inactive (missing path).")

    # 7. PUPPETEER (Browser)
    # Always active.
    servers.append({
        "type": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
    })

    # 8. BRAVE SEARCH
    brave_key = os.getenv("BRAVE_API_KEY")
    if brave_key:
        servers.append({
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search"],
            "env": {"BRAVE_API_KEY": brave_key}
        })
    else:
        logger.debug("[MCP 8] Brave Search inactive (missing BRAVE_API_KEY).")

    # 9. SLACK
    slack_token = os.getenv("SLACK_BOT_TOKEN")
    if slack_token:
        servers.append({
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-slack"],
            "env": {"SLACK_BOT_TOKEN": slack_token}
        })
    else:
        logger.debug("[MCP 9] Slack inactive (missing SLACK_BOT_TOKEN).")

    logger.info(f"[MCP] Registered {len(servers)} of 9 Holy Connectors.")
    return servers

def get_mcp_status() -> Dict[str, str]:
    """Returns the status of all 9 MCPs."""
    return {
        "1_github": "ACTIVE" if os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN") or os.getenv("GITHUB_TOKEN") else "INACTIVE",
        "2_gdrive": "ACTIVE" if os.getenv("GDRIVE_CREDENTIALS") else "INACTIVE",
        "3_gcloud": "ACTIVE" if os.getenv("GOOGLE_CLOUD_PROJECT") else "INACTIVE",
        "4_filesystem": "ACTIVE",
        "5_memory": "ACTIVE",
        "6_sqlite": "ACTIVE" if os.getenv("MCP_SQLITE_PATH") else "INACTIVE",
        "7_puppeteer": "ACTIVE",
        "8_brave": "ACTIVE" if os.getenv("BRAVE_API_KEY") else "INACTIVE",
        "9_slack": "ACTIVE" if os.getenv("SLACK_BOT_TOKEN") else "INACTIVE",
    }
