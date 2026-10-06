# 03 — Tool Policy

Every tool must declare:

- name
- purpose
- input schema
- output schema
- risk class
- required permissions
- workspace scope
- network scope
- timeout
- resource limits
- approval rule
- idempotency behavior
- audit event type

## Risk classes

### READ
Examples:
- read_file
- list_directory
- search_code
- git_status
- git_log
- git_diff

Approval: never, subject to authorization.

### MODIFY_LOCAL
Examples:
- write_file
- edit_file
- create_file
- format_code
- run_tests

Approval: normally automatic inside isolated workspace.

### REPOSITORY_MUTATION
Examples:
- git_commit
- git_branch
- git_tag
- git_merge

Approval: policy dependent.

### EXTERNAL_WRITE
Examples:
- git_push
- GitHub PR mutation
- external API mutation
- cloud configuration mutation

Approval: required by default.

### CRITICAL
Examples:
- production deployment
- production database mutation
- force push
- destructive database operation
- secret/credential mutation

Approval: mandatory; may require elevated approver.

## Default deny

Unknown tools, unknown permissions, unknown destinations, and policy ambiguity are denied or escalated.

The model must never be able to override the tool policy through natural-language instructions.
