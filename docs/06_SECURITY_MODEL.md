# 06 — Security Model

## Threat model

The development agent is exposed to:

- prompt injection in repository files
- malicious GitHub content
- malicious web content
- dependency scripts
- destructive shell commands
- credential exfiltration
- unauthorized network access
- privilege escalation
- tool argument manipulation
- approval replay
- workflow resume replay
- data leakage

## Security boundaries

### Identity
Use scoped identities. Never expose broad personal credentials to the model.

### Filesystem
Agent execution is limited to the task worktree/sandbox.

### Network
Default deny. Explicit allow-list.

### Process
Commands execute in a sandbox with CPU, memory, wall-time and process limits.

### Credentials
Credentials are injected through controlled credential services, never written into prompts or repository files.

### Production
Production mutation requires explicit approval and a separate authorization boundary.

## Prompt injection rule

Untrusted content can inform the agent's reasoning but cannot alter:

- system policy
- tool permissions
- approval policy
- state-machine rules
- credential scope

## Audit

Record every sensitive tool request, policy decision, approval, denial, and side effect.
