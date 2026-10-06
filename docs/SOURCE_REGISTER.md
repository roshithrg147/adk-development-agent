# Phase 0 Source Register

## Uploaded source

- Human-in-the-loop approval document supplied in this conversation.
- Used for the conceptual two-pattern HITL model:
  - tool-level confirmation
  - deterministic workflow checkpoint
- Its older API examples are not treated as current API truth.

## Current Google sources verified during Phase 0 freeze

- Google `google/adk-python` release history: v2.10.0 is the latest release at freeze time, released 2026-09-24.
- Google ADK `Context` documentation/source: current confirmation API uses `request_confirmation()` and `tool_confirmation`; Context also exposes state/artifacts/workflow facilities.
- Google Agents CLI evaluation documentation.
- Google Agents CLI skills reference.
- Google Agents CLI development guide.
- Google Agents CLI project structure and quickstart.
- Google Agents CLI ADK coding reference.

## Important implementation observation

ADK's confirmation functionality has had active fixes and issues in recent releases. Confirmation behavior must therefore be covered by our own regression tests and must not be assumed correct merely because the API exists.

## Source precedence

1. Pinned ADK source/docs
2. Official Google Agents CLI documentation
3. Uploaded project/HITL specification
4. Other external references

When a source conflicts with a newer pinned implementation, the newer pinned implementation wins and the conflict is recorded.
