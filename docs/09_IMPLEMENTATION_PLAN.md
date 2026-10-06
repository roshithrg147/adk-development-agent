# 09 — Phase 0 → Phase 1 Implementation Plan

## Phase 0 — architecture freeze

Deliver and approve:

- architecture
- state machine
- tool policy
- approval model
- skill model
- security model
- data model
- evaluation model
- agent contracts

## Phase 1 — controlled development loop

Build:

1. ADK application bootstrap
2. Supervisor agent
3. Repository inspection tools
4. Git worktree manager
5. Sandboxed command executor
6. Test/lint/build tools
7. PostgreSQL state store
8. Audit event store
9. Tool policy engine
10. ADK HITL confirmation
11. deterministic approval checkpoint
12. first evaluation dataset

## Phase 1 acceptance test

Input:

> Fix one known defect in a real repository.

Expected behavior:

1. inspect repository
2. identify relevant files
3. formulate plan
4. create isolated workspace
5. implement
6. run tests
7. diagnose failures if necessary
8. review diff
9. request approval for any policy-required external mutation
10. produce final artifact and audit trail

No production deployment is required for Phase 1.
