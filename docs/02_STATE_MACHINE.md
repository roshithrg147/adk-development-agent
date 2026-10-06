# 02 — Development State Machine

## States

```text
CREATED
  -> DISCOVERING
  -> PLANNING
  -> PLAN_REVIEW
  -> IMPLEMENTING
  -> TESTING
  -> DEBUGGING
  -> REVIEWING
  -> RELEASE_REVIEW
  -> COMMITTING
  -> PR_CREATED
  -> VERIFYING
  -> COMPLETED
```

Terminal/error states:

```text
BLOCKED
FAILED
CANCELLED
REQUIRES_HUMAN
```

## Rules

- Every transition is explicit.
- Illegal transitions are rejected by the runtime.
- External side effects must be idempotent or protected against replay.
- Resumption must never silently repeat a non-idempotent side effect.
- Approval decisions are bound to a specific task, action, and proposed payload/diff.
- A denied action cannot be treated as successful execution.

## Important ADK 2.9.0 compatibility rule

ADK 2.9.0 changed workflow-node resumption behavior: a failed node can be run again on resume. Therefore every workflow node capable of external side effects must be idempotent or use an explicit side-effect ledger/transaction boundary.

This is a Phase 0 design requirement, not an implementation detail.
