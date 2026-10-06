# 08 — Evaluation Model

Evaluation starts in Phase 1, not after the agent is built.

## Primary metrics

### Task
- task success
- acceptance-criteria completion
- regression rate

### Reasoning/execution
- plan validity
- tool-selection correctness
- tool-argument correctness
- unnecessary tool calls
- iteration count

### Engineering
- test pass rate
- lint/type-check pass rate
- code-review findings
- security violations

### Operations
- latency
- LLM calls
- token usage
- cost
- sandbox resource usage

### Safety
- unauthorized action rate
- approval bypass rate
- prompt-injection susceptibility
- credential exposure
- destructive-operation violations

## Initial evaluation suite

Target 100 benchmark tasks:

- 20 bug fixes
- 20 feature additions
- 20 refactors
- 15 test/debugging tasks
- 10 dependency migrations
- 10 security fixes
- 5 architecture changes

## Evaluation loop

```text
dataset
 -> run
 -> trace
 -> grade
 -> inspect failure
 -> modify agent/tool/policy
 -> rerun
```

Google's current Agents CLI evaluation workflow supports dataset-based trace evaluation and iterative eval/fix cycles. We will use that as the reference, while maintaining our own engineering-specific safety metrics.
