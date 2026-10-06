# PHASE 0 — ARCHITECTURE FREEZE

Status: **FROZEN**
Freeze date: 2026-10-06
Baseline: Google ADK 2.10.0

## Scope

Phase 0 establishes the architecture and contracts required to build a controlled ADK software-development agent.

## Frozen decisions

- Deterministic runtime owns authority.
- LLM is reasoning/proposal layer.
- Specialist agents are workers, not authorities.
- PostgreSQL is authoritative durable state.
- Git worktree + sandbox is mandatory for code execution.
- Tool risk is declarative and default-deny.
- HITL has tool-level and workflow-level mechanisms.
- Approvals are cryptographically/hash-bound at the logical contract level to exact payloads.
- Skills are modular and selectively activated.
- MCP is the external tool interoperability boundary.
- A2A is deferred until distributed agents are justified.
- Evaluation is part of the development lifecycle.
- Side-effecting workflow nodes must be idempotent or protected by a side-effect ledger.
- ADK dependency is pinned to 2.10.0 for Phase 1.

## Explicitly deferred

- Production deployment
- Autonomous production database writes
- Autonomous production deployment
- Autonomous secret management
- Remote A2A fleet
- Broad plugin marketplace
- General-purpose autonomous web agent
- Autonomous merge authority

## Phase 0 exit criterion

All Phase 0 documents exist, the traceability matrix is complete, the acceptance suite is defined, and no unresolved architecture blocker remains.

## Authorization

This freeze authorizes Phase 1 implementation against these contracts.

Any Phase 1 implementation conflict must be raised as an architecture change, not silently resolved in code.
