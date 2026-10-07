from enum import Enum
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class TaskStatus(str, Enum):
    CREATED = "CREATED"
    DISCOVERING = "DISCOVERING"
    PLANNING = "PLANNING"
    PLAN_REVIEW = "PLAN_REVIEW"
    IMPLEMENTING = "IMPLEMENTING"
    TESTING = "TESTING"
    DEBUGGING = "DEBUGGING"
    REVIEWING = "REVIEWING"
    RELEASE_REVIEW = "RELEASE_REVIEW"
    COMMITTING = "COMMITTING"
    PR_CREATED = "PR_CREATED"
    VERIFYING = "VERIFYING"
    COMPLETED = "COMPLETED"
    
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"
    REQUIRES_HUMAN = "REQUIRES_HUMAN"

class RiskLevel(str, Enum):
    READ = "READ"
    MODIFY_LOCAL = "MODIFY_LOCAL"
    REPOSITORY_MUTATION = "REPOSITORY_MUTATION"
    EXTERNAL_WRITE = "EXTERNAL_WRITE"
    CRITICAL = "CRITICAL"

class ValidationState(BaseModel):
    tests: List[str] = Field(default_factory=list)
    lint_status: Optional[str] = None
    typecheck_status: Optional[str] = None
    build_status: Optional[str] = None
    review_status: Optional[str] = None
    security_status: Optional[str] = None

class ArtifactReferences(BaseModel):
    plan_artifact: Optional[str] = None
    diff_artifact: Optional[str] = None
    test_report_artifact: Optional[str] = None
    review_artifact: Optional[str] = None
    audit_bundle: Optional[str] = None

class ExecutionState(BaseModel):
    run_id: str
    attempt: int = 1
    active_agent: Optional[str] = None
    active_node: Optional[str] = None
    parent_run_id: Optional[str] = None
    tool_invocation_ids: List[str] = Field(default_factory=list)
    pending_approval_ids: List[str] = Field(default_factory=list)
    last_successful_checkpoint: Optional[str] = None
    failure_code: Optional[str] = None

class DurableTaskState(BaseModel):
    task_id: str
    repository_id: str
    objective: str
    constraints: List[str] = Field(default_factory=list)
    acceptance_criteria: List[str] = Field(default_factory=list)
    current_phase: TaskStatus = TaskStatus.CREATED
    status: TaskStatus = TaskStatus.CREATED
    risk_level: Optional[RiskLevel] = None
    plan_id: Optional[str] = None
    workspace_id: Optional[str] = None
    branch: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    execution: Optional[ExecutionState] = None
    validation: ValidationState = Field(default_factory=ValidationState)
    artifacts: ArtifactReferences = Field(default_factory=ArtifactReferences)
