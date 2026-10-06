# 04 — Human Approval Model

## Source-derived HITL patterns

The uploaded HITL document defines two patterns:

1. Tool-level confirmation
2. Deterministic workflow checkpoint

Both are retained.

## Pattern A — tool-level confirmation

Use for actions whose risk is known at invocation time.

Current ADK implementation uses `ToolContext` / `Context`:

- inspect `tool_context.tool_confirmation`
- call `tool_context.request_confirmation(...)`
- ADK pauses the invocation
- an upstream client presents the approval request
- the run resumes with the confirmation result

The uploaded document uses older API-style examples. Those examples are conceptual references only; implementation must follow the pinned ADK version.

## Pattern B — deterministic workflow checkpoint

Use when review is intrinsically part of the workflow:

```text
IMPLEMENT
  -> TEST
  -> REVIEW
  -> HUMAN RELEASE GATE
  -> COMMIT / PR / DEPLOY
```

The model cannot skip this gate.

## Approval payload

Every approval request must include:

- task ID
- requested action
- target
- risk level
- exact arguments or diff
- affected files/resources
- validation results
- proposed rollback
- expiration/validity information

## Approval binding

Approval is valid only for the exact action payload for which it was granted.

A materially changed command, diff, destination, or resource requires a new approval.

## Rejection

A rejection is a first-class result. It must include optional human feedback and return control to the workflow for revision.
