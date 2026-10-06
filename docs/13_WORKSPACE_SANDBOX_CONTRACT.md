# 13 — Workspace and Sandbox Contract

Status: FROZEN

## Workspace

Every development task receives:

```text
.workforce/<run_id>/worktrees/<task_id>
```

or the equivalent configured isolated worktree root.

The primary repository worktree is read-only to the agent runtime.

## Sandbox requirements

The command executor must enforce:

- isolated filesystem root
- CPU limit
- memory limit
- wall-clock timeout
- process count limit
- controlled environment variables
- controlled network egress
- output-size limit
- artifact capture

## Network

Default:

```text
DENY
```

Allow-list is explicit and policy-controlled.

## Credentials

No credential files are mounted into the workspace by default.

If a credential is required:
1. policy identifies the required scope
2. credential service resolves it
3. credential is injected for the smallest possible duration/scope
4. credential is never persisted to artifacts, logs, model context, or Git

## Destructive operations

Commands matching destructive policy patterns are blocked or require mandatory approval.

Examples:
- recursive deletion outside workspace
- force push
- destructive database operations
- production deployment
- secret rotation

## Git invariant

The agent may create branches/worktrees inside its assigned workspace, but may not mutate another task's worktree.
