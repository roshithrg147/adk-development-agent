# 12 — State Schema

Status: FROZEN

The runtime state is divided into durable task state, execution state, and ephemeral execution metadata.

## Durable task state

```text
task_id
repository_id
objective
constraints[]
acceptance_criteria[]
current_phase
status
risk_level
plan_id
workspace_id
branch
created_at
updated_at
```

## Execution state

```text
run_id
attempt
active_agent
active_node
parent_run_id
tool_invocation_ids[]
pending_approval_ids[]
last_successful_checkpoint
failure_code
```

## Validation state

```text
tests[]
lint_status
typecheck_status
build_status
review_status
security_status
```

## Artifact references

```text
plan_artifact
diff_artifact
test_report_artifact
review_artifact
audit_bundle
```

## State invariants

1. `COMPLETED` requires successful acceptance criteria.
2. `COMMITTING` requires review completion and all mandatory approvals.
3. `DEPLOYING` requires deployment approval when policy requires it.
4. A task cannot have two active primary execution runs.
5. An approval cannot authorize an action whose payload hash differs from the approved payload.
6. Resume must restore the last durable checkpoint before replaying work.
7. State transitions are append-audited.

## ADK relationship

ADK session/context state is runtime state. PostgreSQL remains the authoritative durable task store. The two are synchronized through explicit persistence boundaries rather than treating model context as the database.
