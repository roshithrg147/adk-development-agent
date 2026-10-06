# ADK Development Agent — Phase 0

Status: ARCHITECTURE FREEZE CANDIDATE
Date: 2026-10-06

This package defines Phase 0 for a Google Agent Development Kit (ADK)-based software-development agent.

## Objective

Establish the architecture, security boundaries, state machine, tool policy, approval model, skill model, evaluation model, and implementation contract before autonomous coding is enabled.

## Phase 0 does not implement

- Autonomous repository modification
- Production deployment
- Autonomous GitHub merge
- Autonomous credential access
- Autonomous production database mutation
- Autonomous production deployment

## Phase 0 exit condition

Phase 0 is complete when the documents in `docs/` are reviewed and accepted as the implementation contract.

## Source basis

1. Uploaded HITL document: "How do I implement human-in-the-loop approval work..."
2. Current Google ADK documentation and source
3. Current Google Agents CLI documentation and skills
4. Current ADK release information

The uploaded HITL document remains the conceptual source for two HITL patterns:
- tool-level confirmation
- deterministic workflow checkpoint

Where its API examples differ from current ADK, current ADK documentation/source is treated as the implementation reference. The older examples are preserved conceptually rather than silently copied.

## Initial technical baseline

- Python 3.11+
- Google ADK 2.10.0 pinned initially
- Gemini as the initial model family
- `uv`
- PostgreSQL as authoritative persistence
- Redis only when justified for ephemeral coordination
- Docker-based isolated execution for local MVP
- Git worktrees for repository isolation
- MCP for external tool interoperability
- A2A deferred until remote-agent distribution is justified
- Structured evaluation from the beginning
