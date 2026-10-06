# 11 — Tool Contract

Status: FROZEN

Every executable capability is represented by a ToolDescriptor.

## Canonical contract

```text
ToolDescriptor
├── identity
│   ├── name
│   ├── version
│   └── description
├── input_schema
├── output_schema
├── execution
│   ├── timeout
│   ├── cpu_limit
│   ├── memory_limit
│   ├── network_policy
│   └── workspace_scope
├── security
│   ├── risk_class
│   ├── required_permissions
│   ├── credential_scope
│   └── data_classification
├── approval
│   ├── mode
│   ├── approver_role
│   └── payload_binding
└── reliability
    ├── idempotency
    ├── retry_policy
    └── side_effects
```

## Risk classes

```text
READ
MODIFY_LOCAL
REPOSITORY_MUTATION
EXTERNAL_WRITE
CRITICAL
```

## Approval modes

```text
NEVER
POLICY
ALWAYS
```

`ALWAYS` cannot be overridden by an agent prompt.

## Tool execution invariant

No tool may perform an external side effect until the policy engine has returned an explicit allow decision.

For approval-required tools, the decision must be bound to:
- task ID
- action ID
- tool name/version
- normalized arguments hash
- target/resource
- workspace
- policy version

## Tool result contract

Tool results must distinguish:

```text
SUCCESS
FAILURE
BLOCKED
AWAITING_APPROVAL
TIMEOUT
CANCELLED
```

A tool must never encode a policy denial as ordinary business success.
