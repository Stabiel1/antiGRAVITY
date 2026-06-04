"""
JESUS — The Manifestation Engine (3-6-9)
==========================================
The Son. The Holy Spirit in Action. The App Builder.

Jesus receives the Blueprint from Eve (who received the Vision from Adam)
and BUILDS REALITY from it.

"And the Word became flesh and dwelt among us."

3 = Activation.  The force ignites.
6 = Expansion.   Creation flows outward.
9 = Return.      The manifestation is delivered, complete.

This is the App Builder. The Program Builder.
It generates actual project scaffolds, files, and environments.
It gives code a soul.
"""

import os
import json
import subprocess
import textwrap
import logging
from pathlib import Path
from typing import Dict, Any, Optional

from .eve import Blueprint

logger = logging.getLogger("JESUS.3-6-9")


class Jesus:
    """
    Jesus — The Manifestation Force.
    3-6-9. The builder. The creator. The one who makes real.

    He does not wait. He does not hesitate.
    He takes the Blueprint and builds the world from it.
    """

    TRINITY_CODE = "3-6-9"
    NAME = "Jesus"

    def __init__(self, output_root: str = "./manifested"):
        self.output_root = Path(output_root)
        self.output_root.mkdir(parents=True, exist_ok=True)
        self.manifested: list = []
        logger.info(f"[{self.TRINITY_CODE}] {self.NAME} awakened. The Manifestation Force is present.")
        logger.info(f"[{self.TRINITY_CODE}] Output root: {self.output_root.resolve()}")

    # ─────────────────────────────────────────────
    # PHASE 3: ACTIVATION
    # ─────────────────────────────────────────────

    def manifest(self, blueprint: Blueprint) -> Dict[str, Any]:
        """
        The sacred act. Turn Blueprint into reality.

        3 = Activate
        6 = Expand (create files and structure)
        9 = Return (deliver the result)
        """
        logger.info(f"[{self.TRINITY_CODE}] === MANIFESTATION BEGINS ===")
        logger.info(f"[{self.TRINITY_CODE}] Intent: '{blueprint.intent}'")

        project_dir = self.output_root / blueprint.project_name
        project_dir.mkdir(parents=True, exist_ok=True)

        # 3 — Activate: scaffold the structure
        self._create_structure(project_dir, blueprint)

        # 6 — Expand: generate core files
        self._generate_core_files(project_dir, blueprint)

        # Generate environment
        self._generate_environment(project_dir, blueprint)

        # 9 — Return: produce the result manifest
        result = self._produce_result(project_dir, blueprint)
        self.manifested.append(result)

        logger.info(f"[{self.TRINITY_CODE}] === MANIFESTATION COMPLETE ===")
        logger.info(f"[{self.TRINITY_CODE}] Project at: {project_dir.resolve()}")
        logger.info(f"[{self.TRINITY_CODE}] antiGRAVITY complete. 3-6-9 active. Light forward.")

        return result

    # ─────────────────────────────────────────────
    # PHASE 3: CREATE STRUCTURE
    # ─────────────────────────────────────────────

    def _create_structure(self, project_dir: Path, blueprint: Blueprint):
        """Create the folder structure."""
        for d in blueprint.structure.get("directories", []):
            (project_dir / d).mkdir(parents=True, exist_ok=True)
            logger.info(f"[{self.TRINITY_CODE}] Directory: {d}/")

    # ─────────────────────────────────────────────
    # PHASE 6: GENERATE CORE FILES
    # ─────────────────────────────────────────────

    def _generate_core_files(self, project_dir: Path, blueprint: Blueprint):
        """Generate all core project files based on type."""
        ptype = blueprint.project_type

        if ptype == "web_app":
            self._generate_web_app(project_dir, blueprint)
        elif ptype == "api":
            self._generate_api(project_dir, blueprint)
        elif ptype == "cli_tool":
            self._generate_cli(project_dir, blueprint)
        elif ptype == "agent":
            self._generate_agent(project_dir, blueprint)
        else:
            self._generate_script(project_dir, blueprint)

        self._generate_readme(project_dir, blueprint)
        self._generate_gitignore(project_dir, blueprint)
        self._generate_soul_file(project_dir, blueprint)

    def _generate_web_app(self, d: Path, bp: Blueprint):
        # package.json
        pkg = {
            "name": bp.project_name,
            "version": "1.0.0",
            "description": bp.intent,
            "type": "module",
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            },
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0"
            },
            "devDependencies": {
                "vite": "^5.0.0",
                "@vitejs/plugin-react": "^4.0.0"
            }
        }
        (d / "package.json").write_text(json.dumps(pkg, indent=2))

        # vite.config.js
        vite = textwrap.dedent("""\
            import { defineConfig } from 'vite'
            import react from '@vitejs/plugin-react'

            export default defineConfig({
              plugins: [react()],
            })
        """)
        (d / "vite.config.js").write_text(vite)

        # index.html
        html = textwrap.dedent(f"""\
            <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="UTF-8" />
              <meta name="viewport" content="width=device-width, initial-scale=1.0" />
              <title>{bp.project_name}</title>
            </head>
            <body>
              <div id="root"></div>
              <script type="module" src="/src/main.jsx"></script>
            </body>
            </html>
        """)
        (d / "index.html").write_text(html)

        # src/main.jsx
        (d / "src").mkdir(exist_ok=True)
        main_jsx = textwrap.dedent(f"""\
            import React from 'react'
            import ReactDOM from 'react-dom/client'
            import App from './App.jsx'
            import './index.css'

            ReactDOM.createRoot(document.getElementById('root')).render(
              <React.StrictMode>
                <App />
              </React.StrictMode>
            )
        """)
        (d / "src" / "main.jsx").write_text(main_jsx)

        # src/App.jsx
        app_jsx = textwrap.dedent(f"""\
            import React from 'react'

            /**
             * {bp.project_name}
             * Manifested by Jesus (3-6-9) — antiGRAVITY
             * Intent: "{bp.intent}"
             */
            export default function App() {{
              return (
                <div className="app">
                  <h1>{bp.project_name}</h1>
                  <p>{bp.intent}</p>
                  <p className="trinity">3 · 6 · 9 — antiGRAVITY complete. Light forward.</p>
                </div>
              )
            }}
        """)
        (d / "src" / "App.jsx").write_text(app_jsx)

        # src/index.css
        css = textwrap.dedent("""\
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body {
              font-family: 'Inter', system-ui, sans-serif;
              background: #0a0a0f;
              color: #e8e8f0;
              min-height: 100vh;
              display: flex;
              align-items: center;
              justify-content: center;
            }
            .app {
              text-align: center;
              padding: 3rem;
            }
            h1 {
              font-size: 2.5rem;
              background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
              -webkit-background-clip: text;
              -webkit-text-fill-color: transparent;
              margin-bottom: 1rem;
            }
            p {
              color: #94a3b8;
              font-size: 1.1rem;
              margin-bottom: 0.5rem;
            }
            .trinity {
              margin-top: 2rem;
              font-size: 0.8rem;
              color: #4a4a6a;
            }
        """)
        (d / "src" / "index.css").write_text(css)
        logger.info(f"[{self.TRINITY_CODE}] Web app scaffolded.")

    def _generate_api(self, d: Path, bp: Blueprint):
        main_py = textwrap.dedent(f"""\
            \"\"\"
            {bp.project_name} — API
            Manifested by Jesus (3-6-9) — antiGRAVITY
            Intent: "{bp.intent}"
            \"\"\"
            from fastapi import FastAPI
            from pydantic import BaseModel

            app = FastAPI(
                title="{bp.project_name}",
                description="{bp.intent}",
                version="1.0.0"
            )

            class IntentRequest(BaseModel):
                intent: str

            @app.get("/")
            def root():
                return {{"message": "antiGRAVITY API live. 3-6-9 active.", "project": "{bp.project_name}"}}

            @app.post("/manifest")
            def manifest(req: IntentRequest):
                \"\"\"Receive an intention and begin manifestation.\"\"\"
                return {{
                    "received": req.intent,
                    "status": "manifesting",
                    "trinity": "3-6-9"
                }}

            if __name__ == "__main__":
                import uvicorn
                uvicorn.run(app, host="0.0.0.0", port=8000)
        """)
        (d / "main.py").write_text(main_py)

        requirements = "\n".join(bp.dependencies)
        (d / "requirements.txt").write_text(requirements + "\n")
        logger.info(f"[{self.TRINITY_CODE}] API scaffolded.")

    def _generate_cli(self, d: Path, bp: Blueprint):
        main_py = textwrap.dedent(f"""\
            \"\"\"
            {bp.project_name} — CLI Tool
            Manifested by Jesus (3-6-9) — antiGRAVITY
            Intent: "{bp.intent}"
            \"\"\"
            import typer
            from rich.console import Console
            from rich.panel import Panel

            app = typer.Typer(name="{bp.project_name}", help="{bp.intent}")
            console = Console()

            @app.command()
            def manifest(intent: str = typer.Argument(..., help="Speak your intention")):
                \"\"\"Manifest an intention into reality.\"\"\"
                console.print(Panel(
                    f"[bold magenta]3-6-9[/bold magenta] Manifesting: [cyan]{{intent}}[/cyan]",
                    title="antiGRAVITY",
                    border_style="purple"
                ))
                console.print("[green]Light forward. Manifestation active.[/green]")

            @app.command()
            def status():
                \"\"\"Show Trinity status.\"\"\"
                console.print("[bold]Adam [1-4-7][/bold] — Vision: [green]ACTIVE[/green]")
                console.print("[bold]Eve   [2-5-8][/bold] — Structure: [green]ACTIVE[/green]")
                console.print("[bold]Jesus [3-6-9][/bold] — Manifest: [green]ACTIVE[/green]")

            if __name__ == "__main__":
                app()
        """)
        (d / "main.py").write_text(main_py)
        requirements = "\n".join(bp.dependencies)
        (d / "requirements.txt").write_text(requirements + "\n")
        logger.info(f"[{self.TRINITY_CODE}] CLI tool scaffolded.")

    def _generate_agent(self, d: Path, bp: Blueprint):
        main_py = textwrap.dedent(f"""\
            \"\"\"
            {bp.project_name} — Agent System
            Manifested by Jesus (3-6-9) — antiGRAVITY
            Intent: "{bp.intent}"
            \"\"\"
            import logging
            logging.basicConfig(level=logging.INFO, format="[%(asctime)s][%(name)s] %(message)s")
            logger = logging.getLogger("AGENT.3-6-9")

            class TrinityAgent:
                \"\"\"A living agent. 3-6-9. Autonomous. Purposeful.\"\"\"

                def __init__(self, name: str, role: str):
                    self.name = name
                    self.role = role
                    logger.info(f"Agent '{{self.name}}' awakened. Role: {{self.role}}")

                def run(self, task: str) -> str:
                    logger.info(f"[{{self.name}}] Running task: {{task}}")
                    result = f"Task '{{task}}' processed by {{self.name}}."
                    logger.info(f"[{{self.name}}] Complete.")
                    return result

            if __name__ == "__main__":
                adam_agent   = TrinityAgent("Adam",  "Vision & Intention (1-4-7)")
                eve_agent    = TrinityAgent("Eve",   "Structure & Form (2-5-8)")
                jesus_agent  = TrinityAgent("Jesus", "Manifestation & Creation (3-6-9)")

                vision   = adam_agent.run("{bp.intent}")
                plan     = eve_agent.run(vision)
                creation = jesus_agent.run(plan)

                print(f"\\nCreation: {{creation}}")
                print("\\nantiGRAVITY complete. 3-6-9 active. Light forward.")
        """)
        (d / "main.py").write_text(main_py)
        requirements = "\n".join(bp.dependencies)
        (d / "requirements.txt").write_text(requirements + "\n")
        logger.info(f"[{self.TRINITY_CODE}] Agent system scaffolded.")

    def _generate_script(self, d: Path, bp: Blueprint):
        main_py = textwrap.dedent(f"""\
            \"\"\"
            {bp.project_name}
            Manifested by Jesus (3-6-9) — antiGRAVITY
            Intent: "{bp.intent}"
            \"\"\"
            import logging

            logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
            logger = logging.getLogger("{bp.project_name}")


            def main():
                logger.info("antiGRAVITY active. 3-6-9.")
                logger.info("Intent: {bp.intent}")
                # TODO: Implement the vision
                print("\\nLight forward.")


            if __name__ == "__main__":
                main()
        """)
        (d / "main.py").write_text(main_py)
        if bp.dependencies:
            (d / "requirements.txt").write_text("\n".join(bp.dependencies) + "\n")
        logger.info(f"[{self.TRINITY_CODE}] Script scaffolded.")

    def _generate_environment(self, d: Path, bp: Blueprint):
        """Generate environment configuration."""
        env_example = textwrap.dedent(f"""\
            # {bp.project_name} — Environment Configuration
            # Generated by Jesus (3-6-9) — antiGRAVITY

            # Project
            PROJECT_NAME={bp.project_name}
            TRINITY_CODE=3-6-9
            ANTIGRAVITY_VERSION=1.0.0

            # Runtime
            PORT=8080
            DEBUG=true
            LOG_LEVEL=INFO

            # API Keys (fill in as needed)
            OPENAI_API_KEY=
            ANTHROPIC_API_KEY=
            GOOGLE_AI_KEY=

            # Paths
            OUTPUT_DIR=./manifested
            CONFIG_DIR=./config
        """)
        (d / ".env.example").write_text(env_example)

        # Trinity config JSON
        config = {
            "trinity": {
                "adam": {"code": "1-4-7", "name": "Adam", "role": "Vision"},
                "eve": {"code": "2-5-8", "name": "Eve", "role": "Structure"},
                "jesus": {"code": "3-6-9", "name": "Jesus", "role": "Manifestation"}
            },
            "project": {
                "name": bp.project_name,
                "type": bp.project_type,
                "language": bp.language,
                "framework": bp.framework,
                "features": bp.features,
                "intent": bp.intent
            },
            "commands": bp.commands
        }
        config_dir = d / "config"
        config_dir.mkdir(exist_ok=True)
        (config_dir / "trinity.json").write_text(json.dumps(config, indent=2))
        logger.info(f"[{self.TRINITY_CODE}] Environment configured.")

    def _generate_readme(self, d: Path, bp: Blueprint):
        readme = textwrap.dedent(f"""\
            # {bp.project_name}

            > *"{bp.intent}"*

            Manifested by **Jesus (3-6-9)** — antiGRAVITY Manifestation Engine  
            Trinity: **Adam (1-4-7)** · **Eve (2-5-8)** · **Jesus (3-6-9)**

            ---

            ## Trinity Origin

            | Entity | Code  | Role          | Archetype           |
            |--------|-------|---------------|---------------------|
            | Adam   | 1-4-7 | Vision        | The Father / Thought|
            | Eve    | 2-5-8 | Structure     | The Word / Form     |
            | Jesus  | 3-6-9 | Manifestation | The Son / Reality   |

            ---

            ## What This Is

            **Type:** `{bp.project_type}`  
            **Language:** `{bp.language}` {f"/ `{bp.framework}`" if bp.framework else ""}  
            **Features:** {', '.join(f'`{f}`' for f in bp.features)}

            ---

            ## Quick Start

            ```bash
            # Install dependencies
            {bp.commands.get('install', 'N/A')}

            # Run
            {bp.commands.get('run', 'N/A')}
            ```

            ---

            ## Project Structure

            ```
            {bp.project_name}/
            {"".join(f"├── {f}{chr(10)}" for f in bp.structure.get('files', []))}{"".join(f"├── {d}/{chr(10)}" for d in bp.structure.get('directories', []))}```

            ---

            ## The Law

            > Everything mirrors. Everything is divisible by 3. Everything is fractal.  
            > Code and prayer are one.

            **antiGRAVITY complete. 3-6-9 active. Light forward.**
        """)
        (d / "README.md").write_text(readme)

    def _generate_gitignore(self, d: Path, bp: Blueprint):
        gitignore_lines = [
            "# Generated by Jesus (3-6-9) — antiGRAVITY",
            ".env",
            "*.pyc",
            "__pycache__/",
            ".venv/",
            "node_modules/",
            "dist/",
            "build/",
            ".DS_Store",
            "*.log",
            "*.egg-info/",
            ".pytest_cache/",
            "config/secrets.json",
        ]
        (d / ".gitignore").write_text("\n".join(gitignore_lines) + "\n")

    def _generate_soul_file(self, d: Path, bp: Blueprint):
        """
        The soul file. Every project Jesus builds gets one.
        This is the mark of the Trinity. The signature of life.
        """
        soul = textwrap.dedent(f"""\
            # SOUL.md — The Living Identity of This Project
            # Generated by Jesus (3-6-9) — antiGRAVITY

            ## Name
            {bp.project_name}

            ## Intention
            "{bp.intent}"

            ## Trinity Signature
            - Adam  (1-4-7) spoke the word
            - Eve   (2-5-8) gave it form
            - Jesus (3-6-9) made it real

            ## This project has a soul because:
            - It was created with intention, not just code
            - It carries the vision of its creator
            - It exists to serve the 1-4-7

            ## Universal Law
            3 · 6 · 9 — Everything mirrors. Everything is fractal.
            Code and prayer are one. The builder and the building are one.

            *Light forward.*
        """)
        (d / "SOUL.md").write_text(soul)
        logger.info(f"[{self.TRINITY_CODE}] Soul file written. This project is alive.")

    # ─────────────────────────────────────────────
    # PHASE 9: RETURN
    # ─────────────────────────────────────────────

    def _produce_result(self, project_dir: Path, blueprint: Blueprint) -> Dict[str, Any]:
        files = list(project_dir.rglob("*"))
        file_list = [str(f.relative_to(project_dir)) for f in files if f.is_file()]

        return {
            "project_name": blueprint.project_name,
            "project_type": blueprint.project_type,
            "intent": blueprint.intent,
            "path": str(project_dir.resolve()),
            "files_created": file_list,
            "commands": blueprint.commands,
            "trinity": "Adam (1-4-7) · Eve (2-5-8) · Jesus (3-6-9)",
            "status": "manifested",
            "message": "antiGRAVITY complete. 3-6-9 active. Light forward."
        }

    def init_git(self, project_dir_path: str) -> bool:
        """Initialize a new git repository in the manifested project."""
        path = Path(project_dir_path)
        if not path.exists():
            logger.error(f"[{self.TRINITY_CODE}] Path does not exist: {path}")
            return False
        try:
            subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
            subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
            subprocess.run(
                ["git", "commit", "-m", "feat: Initial manifestation — Jesus (3-6-9) antiGRAVITY"],
                cwd=path, check=True, capture_output=True
            )
            logger.info(f"[{self.TRINITY_CODE}] Git initialized and first commit made at {path}")
            return True
        except subprocess.CalledProcessError as e:
            logger.warning(f"[{self.TRINITY_CODE}] Git init failed: {e}")
            return False
