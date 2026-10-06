# ADR-0003 — PostgreSQL as Authoritative State Store

Status: Accepted for Phase 0

PostgreSQL is the authoritative transactional store for development-task state, approvals, audit records and side-effect ledgers.

Redis is permitted only for ephemeral coordination where justified.
