from typing import Any, Dict
import google.adk as adk
from ..state.models import DurableTaskState, TaskStatus
from ..state.store import PostgresStateStore

class SupervisorAgent(adk.Agent):
    def __init__(self, state_store: PostgresStateStore):
        super().__init__(name="supervisor")
        self.state_store = state_store
        
    def coordinate_task(self, task_id: str, context: adk.Context):
        state = self.state_store.load_task(task_id)
        
        if state.status == TaskStatus.CREATED:
            state.status = TaskStatus.DISCOVERING
            self.state_store.save_task(state)
            
        # Example of delegating work - in full implementation, calls other agents
        if state.status == TaskStatus.DISCOVERING:
            # Delegate to Researcher/Analyst
            state.status = TaskStatus.PLANNING
            self.state_store.save_task(state)
            
        if state.status == TaskStatus.PLANNING:
            # Delegate to Planner
            state.status = TaskStatus.IMPLEMENTING
            self.state_store.save_task(state)
            
        if state.status == TaskStatus.IMPLEMENTING:
            # Delegate to Implementer
            state.status = TaskStatus.TESTING
            self.state_store.save_task(state)
            
        if state.status == TaskStatus.TESTING:
            # Delegate to Tester/Debugger
            state.status = TaskStatus.REVIEWING
            self.state_store.save_task(state)
            
        if state.status == TaskStatus.REVIEWING:
            # Delegate to Reviewer & Security Reviewer
            state.status = TaskStatus.COMPLETED
            self.state_store.save_task(state)
            
        return state
