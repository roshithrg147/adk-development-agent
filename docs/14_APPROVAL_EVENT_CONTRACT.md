# 14 — Approval Event Contract

Status: FROZEN

## ApprovalRequest

```text
approval_id
task_id
run_id
action_id
tool_name
tool_version
risk_class
requested_by_agent
target
normalized_arguments_hash
diff_hash
policy_version
reason
evidence[]
rollback_plan
created_at
expires_at
```

## ApprovalDecision

```text
approval_id
decision
decided_by
decided_at
reason
approved_payload_hash
```

Where:

```text
decision ∈ {APPROVED, REJECTED, EXPIRED, REVOKED}
```

## Binding rule

An `APPROVED` decision is valid only if:

```text
approved_payload_hash
==
current_payload_hash
```

Otherwise the action must request new approval.

## Approval lifecycle

```text
REQUESTED
   ↓
PENDING
   ├── APPROVED
   ├── REJECTED
   ├── EXPIRED
   └── REVOKED
```

## ADK integration

Tool-level confirmation uses the current ADK `Context.request_confirmation()` / `tool_confirmation` mechanism.

Workflow-level approval remains an application-level deterministic checkpoint.

The two mechanisms must not be conflated: ADK confirmation pauses a tool invocation; the application approval state controls whether the broader workflow may cross a release boundary.
