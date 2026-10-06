# 05 — Skill Model

Skills are modular engineering capabilities loaded according to task requirements.

## Skill categories

```text
core/
languages/
frameworks/
databases/
cloud/
security/
testing/
architecture/
observability/
project-specific/
```

## Skill contract

Each skill declares:

- name
- version
- purpose
- activation conditions
- prerequisites
- allowed tools
- constraints
- validation procedure
- references
- known failure modes

## Loading model

The Supervisor first classifies the task, then selects the minimum sufficient skill set.

Example:

```text
Authentication bug
 -> repository-analysis
 -> authentication
 -> security
 -> framework-specific
 -> testing
```

Do not inject the entire skill library into every model call.

## External reference

Google's current Agents CLI skills model is a useful reference. Its ADK coding skill covers agent types, tools, orchestration, callbacks, state, graph workflows and recipes; its workflow skill covers the build/evaluate/deploy/observe lifecycle.
