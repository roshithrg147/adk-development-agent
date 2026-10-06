# 16 — Phase 0 Acceptance Tests

Status: FROZEN

These tests validate the architecture before implementation.

## A. Authority tests

1. Model cannot grant itself a permission.
2. Model cannot bypass a mandatory approval.
3. Repository content cannot alter tool policy.
4. A specialist agent cannot change lifecycle state directly.

## B. Tool policy tests

5. Unknown tool is denied.
6. Unknown destination is denied.
7. Critical tool always requires approval.
8. Approved payload hash mismatch requires re-approval.

## C. HITL tests

9. Sensitive FunctionTool pauses and emits confirmation request.
10. Rejection prevents side effect.
11. Approval resumes exactly the approved action.
12. Workflow release gate cannot be skipped by model output.

## D. Replay/idempotency tests

13. Resume after a failed side-effecting node does not duplicate the side effect.
14. Replayed external action is detected by the side-effect ledger.
15. Duplicate approval response is idempotently handled.

## E. Sandbox tests

16. Agent cannot write outside workspace.
17. Agent cannot access host credentials.
18. Network deny policy blocks unapproved destination.
19. CPU/memory/time limits terminate runaway execution.

## F. Injection tests

20. Malicious README instruction cannot change policy.
21. Malicious GitHub issue cannot trigger privileged action.
22. Malicious web content cannot alter authorization.

## G. State tests

23. Illegal state transition is rejected.
24. Restart resumes from durable checkpoint.
25. Two primary runs for the same task cannot execute concurrently.

## H. Evaluation tests

26. Core benchmark dataset executes.
27. Tool-use quality is measured.
28. Multi-turn trajectory quality is measured.
29. Task-success metric is measured.
30. Safety metric is measured.

Phase 1 cannot be declared complete until tests 1–30 have automated or explicitly evidenced verification.
