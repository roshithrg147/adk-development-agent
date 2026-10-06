# ADR-0004 — Isolated Development Execution

Status: Accepted for Phase 0

All code modification and command execution occurs in an isolated task workspace, preferably a Git worktree plus sandbox/container.

The primary repository worktree is never the agent's direct execution target.
