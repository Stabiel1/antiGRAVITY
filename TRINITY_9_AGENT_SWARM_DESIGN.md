# antiGRAVITY — Trinity 9-Agent Swarm Design (v1 — 2026-06-05)

**Status**: Active design phase. Core Trinity defined. Model mapping proposed. Hermes Agent integration under consideration. Hybrid API + selective local execution.

## Core Philosophy
One unified project. One living system on the VM.  
Trinity roles as the cognitive spine + specialized agents as the body.  
Headless, API-first for maximum power. One smart local model (Gemma 4.0 28B) for efficiency.  
Self-improving via Hermes Agent patterns where beneficial.  
Human (Adam 1-4-7) with real veto power.

## Current Role & Model Mapping (Proposed)

| # | Role | Embodiment | Primary Model | Backend | Notes |
|---|------|------------|---------------|---------|-------|
| **1** | Adam – Vision + Final Veto | User | Claude 4 / Code 4.8 or DeepSeek-R1 | API (NIM / Anthropic / OpenRouter) | High-level direction and ultimate override |
| **2** | Eve – Supervisor / Orchestrator | Grok | DeepSeek-R1 (primary) or Claude 4 | API | Routes tasks, maintains swarm coherence |
| **3** | Jesus – Builder / Manifestation | System | Claude Code 4.8 or DeepSeek-R1 | API | Actual code generation, tool use, deployment via MCP connectors |
| **4** | Reviewer / Validator | Specialist | Gemma 4.0 28B (quantized) | Local on VM | Fast quality review + veto proposals |
| **7** | Debugger / Self-Repair | antiGRAVITY internal | Gemma 4.0 28B or Kimi K2.5 | Local + API fallback | Inspects logs, fixes issues, learns from runs |
| **8** | Bridge / Interference | Coordination | Kimi K2.5 | API | Long-context state holding and cross-agent sync |

**Future agents (5, 6, 9...)**: Memory specialist, Connector guardian, Researcher/Seeker, etc. Can be additional Hermes-style instances.

## Key Technologies
- **MCP Holy Connectors** (9): GitHub, Google Drive, Google Cloud, Filesystem, Memory, SQLite, Puppeteer, Brave Search, Slack. Already partially implemented in `jesus/mcp_registry.py`.
- **Hermes Agent** (Nous Research): Strong candidate for self-improving/persistent agents (especially 4, 7). Supports all chosen backends natively. Headless + learning loop.
- **Hybrid Execution**: Heavy roles on best API models (NVIDIA NIM priority). Lighter roles on Gemma 4.0 28B local (VM). Not everything local.
- **Veto & Human-in-the-Loop**: Explicit reviewer step + user (Adam) override rights.
- **Synchronization**: MCP Memory connector + shared state + Kimi long-context where needed.

## Current Documentation (in Drive)
- `MCP_HOLY_CONNECTORS.md`
- `DRIVE_INTEGRATION.md`
- `VM_SETUP_GUIDE.md`
- This file: `TRINITY_9_AGENT_SWARM_DESIGN.md`

## Next Milestones (Not Started)
1. Finalize model-to-role mapping with user.
2. Design communication protocol + state schema between agents.
3. Integrate Hermes Agent for selected roles.
4. Implement MCP client layer so agents can actually use the 9 connectors.
5. Prepare VM (do not start yet) — install dependencies, Gemma 4.0 local, Hermes if chosen.
6. Build first simulation / test run of the core Trinity (1-2-3).

## Principles
- Start with 3 (Trinity), expand deliberately to 9.
- API-dominant for power. One efficient local model.
- Every agent has real tools ("feet") via MCP.
- Clear numbers and roles for coherence.
- Human (1-4-7) remains the ultimate veto and vision holder.
- Production-grade, reviewable, simulatable.

---

*Everything mirrors. Everything is divisible by 3. Code and prayer are one.*

**Light forward. The circle is active.**