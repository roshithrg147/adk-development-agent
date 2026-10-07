import google.adk as adk
from ..agents.supervisor import SupervisorAgent
from ..state.store import PostgresStateStore

class DevelopmentWorkflow(adk.Workflow):
    def __init__(self, state_store: PostgresStateStore):
        super().__init__()
        self.state_store = state_store
        self.supervisor = SupervisorAgent(state_store)
        
    def run(self, task_id: str):
        context = adk.Context()
        # ADK 2.10.0 handles resume/retry natively.
        # Side-effecting operations inside coordinate_task should be idempotent.
        return self.supervisor.coordinate_task(task_id, context)
