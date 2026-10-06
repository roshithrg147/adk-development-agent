# ADR-0001 — Initial ADK Version

Status: ACCEPTED / FROZEN
Date: 2026-10-06

## Decision

Pin Google ADK to **2.10.0** for Phase 1.

## Evidence

The official `google/adk-python` release history identifies v2.10.0, released 2026-09-24, as the latest release at the time of Phase 0 freeze.

2.10.0 adds:
- advanced skill lifecycle management
- evaluation efficiency metrics for duration, token consumption and model-call count
- expanded model/database integrations

## Rationale

2.10.0 is preferred over 2.9.x because the new skill lifecycle and evaluation capabilities directly support the development-agent architecture.

## Compatibility rule

The project must pin the exact package version in `uv.lock`.

Upgrades require:
1. dependency-change review
2. full unit/integration/evaluation run
3. security regression run
4. explicit architecture review if runtime semantics change

## Known runtime considerations inherited from 2.9.0

2.9.0 changed workflow-node resume behavior: failed nodes run again on resume. Therefore all side-effecting nodes must be idempotent or protected by an explicit side-effect ledger.

## HITL implementation note

Current ADK exposes HITL through `Context`/`ToolContext` confirmation APIs and `FunctionTool` confirmation configuration. The implementation must follow the pinned release source rather than older examples in the uploaded document.
