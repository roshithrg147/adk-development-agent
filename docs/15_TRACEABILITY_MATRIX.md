# 15 — Phase 0 Traceability Matrix

Status: FROZEN

| Requirement | Design artifact | Verification |
|---|---|---|
| LLM is not execution authority | 01_ARCHITECTURE, ADR-0002 | policy bypass test |
| Explicit lifecycle | 02_STATE_MACHINE | illegal-transition tests |
| Tool risk classification | 03_TOOL_POLICY, 11_TOOL_CONTRACT | tool-policy unit tests |
| Tool-level HITL | 04_APPROVAL_MODEL, 14_APPROVAL_EVENT_CONTRACT | confirmation integration test |
| Workflow-level HITL | 04_APPROVAL_MODEL, 02_STATE_MACHINE | release-gate test |
| Dynamic skills | 05_SKILL_MODEL | skill-selection test |
| Prompt-injection boundary | 06_SECURITY_MODEL | adversarial repository test |
| Durable state | 07_DATA_MODEL, 12_STATE_SCHEMA | persistence/restart test |
| Workspace isolation | 13_WORKSPACE_SANDBOX_CONTRACT | filesystem escape test |
| Side-effect replay safety | 02_STATE_MACHINE, 07_DATA_MODEL | resume/idempotency test |
| Evaluation | 08_EVALUATION_MODEL | baseline eval run |
| Version pinning | ADR-0001 | dependency-lock test |
| Auditability | 07_DATA_MODEL, 14_APPROVAL_EVENT_CONTRACT | audit completeness test |

## Freeze rule

A requirement without an artifact and verification method is not considered implemented in the architecture.
