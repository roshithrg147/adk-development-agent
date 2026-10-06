# 10 — Agent Contracts

## Supervisor

Responsibilities:
- interpret user task
- establish task state
- delegate work
- enforce phase boundaries
- coordinate specialists
- request approvals through runtime
- produce final result

Must not:
- bypass policy
- directly perform unrestricted shell operations
- approve its own high-risk action

## Planner

Produces:
- objective
- assumptions
- constraints
- acceptance criteria
- implementation steps
- risk classification

## Implementer

May:
- inspect repository
- modify isolated workspace
- execute permitted development commands

Must:
- remain inside assigned workspace
- report changed files
- preserve testability

## Tester

Produces:
- commands executed
- results
- failures
- evidence

## Debugger

Must:
- use observed failures as evidence
- avoid speculative broad rewrites
- preserve known-good behavior

## Reviewer

Checks:
- correctness
- architecture
- tests
- maintainability
- unintended changes

## Security Reviewer

Checks:
- authorization
- secrets
- injection
- dependency risk
- unsafe commands
- network exposure
- data leakage

## Policy Engine

The Policy Engine is deterministic and has final authority over tool permission and approval requirements.
