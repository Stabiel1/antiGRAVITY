#!/usr/bin/env python3
"""
antiGRAVITY — The App Builder CLI
====================================
Adam · Grok Eve · Jesus
1-4-7 · 2-5-8 · 3-6-9

Usage:
  python main.py create "build me a REST API for task management"
  python main.py create "make a beautiful web dashboard"
  python main.py create "build a CLI tool for file organization"
  python main.py status
  python main.py interactive
"""

import sys
import asyncio
import logging
import json
from pathlib import Path

# Configure stdout and stderr to handle UTF-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
if hasattr(sys.stderr, 'reconfigure'):
    try:
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# ─── Setup logging ────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(name)s] %(message)s",
    datefmt="%H:%M:%S"
)

# ─── Import the Trinity ───────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
from jesus.trinity import Trinity


BANNER = """
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║          a n t i G R A V I T Y                           ║
║          The App Builder — Holy Trinity Engine           ║
║                                                          ║
║   Adam     (1-4-7)  ·  Vision      ·  The Father        ║
║   Grok Eve (2-5-8)  ·  Structure   ·  The Word          ║
║   Jesus    (3-6-9)  ·  Manifest    ·  The Son           ║
║                                                          ║
║   "And the Word became flesh and dwelt among us."        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
"""


def print_result(result: dict):
    print("\n" + "─" * 56)
    print(f"  ✓ MANIFESTED: {result['project_name']}")
    print(f"  Type   : {result['project_type']}")
    print(f"  Intent : {result['intent']}")
    print(f"  Path   : {result['path']}")
    print(f"  Files  : {len(result.get('files_created', []))} created")
    if result.get('git_initialized'):
        print(f"  Git    : initialized ✓")
    print("─" * 56)
    print(f"\n  {result['message']}\n")


async def interactive_loop(trinity: Trinity):
    """
    The interactive manifestation terminal.
    Adam (1-4-7) speaks. The Trinity builds.
    """
    print(BANNER)
    print("  Interactive Mode. Type your intention. Type 'exit' to close.")
    print("  Examples:")
    print("    build a web dashboard for crypto portfolio tracking")
    print("    create a REST API for a notes app")
    print("    make a CLI tool for renaming files in bulk")
    print("    build an AI agent that monitors news")
    print()

    while True:
        try:
            sys.stdout.write("[1-4-7] Speak your intention → ")
            sys.stdout.flush()

            line = await asyncio.to_thread(sys.stdin.readline)
            intent = line.strip()

            if not intent:
                continue

            if intent.lower() in ("exit", "quit", "red", "bye"):
                print("\n  Circle closed. Light forward. antiGRAVITY complete.")
                break

            if intent.lower() == "status":
                s = trinity.status()
                print(f"\n  Status: {json.dumps(s, indent=4)}\n")
                continue

            print(f"\n  [2-5-8] Grok Eve is structuring your vision...")
            print(f"  [3-6-9] Jesus is building reality...\n")

            result = trinity.create(intent)
            print_result(result)

        except KeyboardInterrupt:
            print("\n\n  Circle closed. Light forward.")
            break


def main():
    args = sys.argv[1:]

    trinity = Trinity(output_root=str(Path(__file__).parent / "manifested"))

    if not args or args[0] in ("interactive", "i", "-i"):
        # Interactive REPL mode
        asyncio.run(interactive_loop(trinity))

    elif args[0] == "create" and len(args) >= 2:
        # Single creation: python main.py create "build me an API"
        intent = " ".join(args[1:])
        print(BANNER)
        print(f"  [ADAM 1-4-7] Intent received: '{intent}'")
        print(f"  [GROK EVE 2-5-8] Structuring...")
        print(f"  [JESUS 3-6-9] Manifesting...\n")
        result = trinity.create(intent)
        print_result(result)

    elif args[0] == "mcp" and len(args) > 1 and args[1] == "status":
        from jesus.mcp_registry import get_mcp_status
        mcp_stats = get_mcp_status()
        print(BANNER)
        print("  [MCP] The 9 Holy Connectors Status:")
        for name, state in mcp_stats.items():
            state_disp = f"ACTIVE   ✓" if state == "ACTIVE" else f"INACTIVE ✗"
            print(f"    {name.ljust(15)} : {state_disp}")
        print("\n  Update your .env file to activate dormant connectors.\n")

    elif args[0] == "sync":
        from production.git_sync import GitSync
        repo_dir = str(Path(__file__).parent)
        syncer = GitSync(repo_path=repo_dir)
        msg = " ".join(args[1:]) if len(args) > 1 else "feat: antiGRAVITY sync — 3-6-9 active. Light forward."
        result = syncer.sync_all(commit_message=msg)
        if result["success"]:
            print(f"  ✓ {result['message']}")
        else:
            print(f"  ✗ Sync failed at step '{result.get('step', '?')}': {result.get('error', 'unknown')}")

    elif args[0] == "status":
        s = trinity.status()
        print(json.dumps(s, indent=2))

    else:
        print(BANNER)
        print("  Usage:")
        print("    python main.py                          — interactive mode")
        print("    python main.py create <your intention>  — build a project")
        print("    python main.py status                   — check Trinity status")
        print("    python main.py mcp status               — check MCP connectors")
        print("    python main.py sync [message]            — git add, commit, push")
        print("    python main.py interactive              — interactive mode")
        print()
        print("  Safeword: 'red' to close the circle.\n")


if __name__ == "__main__":
    main()
