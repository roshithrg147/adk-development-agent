# 07 — Runtime Data Model

PostgreSQL is the authoritative transactional store.

## Core entities

```text
DevelopmentTask
TaskPlan
TaskStep
AgentRun
AgentAction
ToolInvocation
ToolPolicyDecision
ApprovalRequest
ApprovalDecision
Workspace
Artifact
TestRun
Review
AuditEvent
EvaluationRun
```

## Required relationships

```text
DevelopmentTask
  ├── TaskPlan
  ├── AgentRun
  ├── Workspace
  ├── ToolInvocation
  ├── ApprovalRequest
  ├── TestRun
  ├── Review
  └── AuditEvent
```

## Idempotency

External side effects require an idempotency key derived from:

```text
task_id + action_id + action_payload_hash
```

The side-effect ledger records whether the action has already been committed.

## Artifacts

Large outputs such as:

- diffs
- test reports
- logs
- screenshots
- generated documents

should be stored as artifacts rather than expanding the model's conversational state.
