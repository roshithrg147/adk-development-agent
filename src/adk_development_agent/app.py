import os
import argparse
import google.adk as adk
from pathlib import Path
from .state.store import PostgresStateStore
from .state.models import DurableTaskState, TaskStatus
from .policy.engine import PolicyEngine
from .workspace.manager import WorkspaceManager
from .tools.inspection import RepositoryInspector
from .tools.testing_tools import TestAndLintTools
from .workflows.approval import DeterministicApprovalCheckpoint, ApprovalRequest

class Phase1Workflow:
    def __init__(self, store: PostgresStateStore, policy: PolicyEngine, base_repo: str):
        self.store = store
        self.policy = policy
        self.base_repo = Path(base_repo).resolve()
        self.workspace_manager = WorkspaceManager(str(self.base_repo))
        self.approval_checkpoint = DeterministicApprovalCheckpoint()

    def run(self, task_id: str):
        # 1. Load or init task state
        state = self.store.load_task(task_id)
        print(f"[{state.status.value}] Starting workflow for task: {task_id}")

        # 2. inspect repository & identify relevant files
        if state.status == TaskStatus.CREATED:
            print("-> Inspecting repository")
            inspector = RepositoryInspector(self.base_repo)
            inspector.list_directory()
            state.status = TaskStatus.DISCOVERING
            self.store.save_task(state)

        # 3. formulate plan
        if state.status == TaskStatus.DISCOVERING:
            print("-> Formulating plan")
            state.status = TaskStatus.PLANNING
            self.store.save_task(state)

        # 4. create isolated workspace
        if state.status == TaskStatus.PLANNING:
            print("-> Creating isolated workspace")
            workspace_dir = self.workspace_manager.setup_task_workspace(run_id="run_1", task_id=task_id, branch_name=f"task-{task_id}")
            state.workspace_id = str(workspace_dir)
            state.status = TaskStatus.IMPLEMENTING
            self.store.save_task(state)

        # 5. implement
        if state.status == TaskStatus.IMPLEMENTING:
            print(f"-> Implementing in workspace: {state.workspace_id}")
            state.status = TaskStatus.TESTING
            self.store.save_task(state)

        # 6. run tests (7. diagnose failures if necessary)
        if state.status == TaskStatus.TESTING:
            print("-> Running tests")
            test_tools = TestAndLintTools(Path(state.workspace_id))
            # Mock test run
            result = test_tools.run_tests("echo 'Tests passed'")
            if result["returncode"] == 0:
                state.status = TaskStatus.REVIEWING
            else:
                state.status = TaskStatus.DEBUGGING
            self.store.save_task(state)

        # 8. review diff
        if state.status == TaskStatus.REVIEWING:
            print("-> Reviewing diff")
            state.status = TaskStatus.RELEASE_REVIEW
            self.store.save_task(state)

        # 9. request approval for any policy-required external mutation
        if state.status == TaskStatus.RELEASE_REVIEW:
            print("-> Requesting approval")
            req = ApprovalRequest(
                task_id=task_id,
                requested_action="git_commit_and_push",
                target="origin",
                risk_level="EXTERNAL_WRITE",
                exact_arguments={"branch": f"task-{task_id}"},
                affected_resources=[state.workspace_id],
                validation_results={"tests": "passed"},
                proposed_rollback="git reset --hard HEAD~1"
            )
            response = self.approval_checkpoint.request_approval(req)
            if response.approved:
                state.status = TaskStatus.COMMITTING
            else:
                state.status = TaskStatus.FAILED
            self.store.save_task(state)

        # 10. produce final artifact and audit trail
        if state.status == TaskStatus.COMMITTING:
            print("-> Committing and completing")
            self.store.append_audit_event(__import__("uuid").uuid4().hex, task_id, "TASK_COMPLETED", {"status": "SUCCESS"})
            state.status = TaskStatus.COMPLETED
            self.store.save_task(state)

        return state

def main():
    parser = argparse.ArgumentParser(description="ADK Development Agent - Phase 1")
    parser.add_argument("--task-id", type=str, required=True, help="Task ID to execute")
    parser.add_argument("--repo-id", type=str, required=True, help="Repository ID to operate on")
    parser.add_argument("--objective", type=str, required=True, help="Task objective")
    parser.add_argument("--db-url", type=str, default="sqlite:///test.db", help="PostgreSQL connection string")
    parser.add_argument("--base-repo", type=str, default=".", help="Base repository path")
    
    args = parser.parse_args()
    
    store = PostgresStateStore(args.db_url)
    policy = PolicyEngine()
    
    try:
        store.load_task(args.task_id)
    except ValueError:
        task_state = DurableTaskState(
            task_id=args.task_id,
            repository_id=args.repo_id,
            objective=args.objective
        )
        store.save_task(task_state)
    
    workflow = Phase1Workflow(store, policy, args.base_repo)
    result = workflow.run(args.task_id)
    
    print(f"Task completed with state: {result.status}")

if __name__ == "__main__":
    main()
