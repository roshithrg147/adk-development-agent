from sqlalchemy import create_engine, Column, String, DateTime, JSON, Enum as SQLEnum
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from .models import TaskStatus, DurableTaskState

Base = declarative_base()

class TaskRecord(Base):
    __tablename__ = 'tasks'
    
    task_id = Column(String, primary_key=True)
    repository_id = Column(String, nullable=False)
    objective = Column(String, nullable=False)
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.CREATED)
    
    state_json = Column(JSON, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AuditRecord(Base):
    __tablename__ = 'audit_events'
    
    event_id = Column(String, primary_key=True)
    task_id = Column(String, index=True)
    event_type = Column(String, nullable=False)
    payload = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)

class PostgresStateStore:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        
    def save_task(self, state: DurableTaskState):
        with self.Session() as session:
            record = session.query(TaskRecord).filter_by(task_id=state.task_id).first()
            if not record:
                record = TaskRecord(
                    task_id=state.task_id,
                    repository_id=state.repository_id,
                    objective=state.objective,
                    status=state.status,
                    state_json=state.model_dump(mode="json")
                )
                session.add(record)
            else:
                record.status = state.status
                record.state_json = state.model_dump(mode="json")
            session.commit()
            
    def load_task(self, task_id: str) -> DurableTaskState:
        with self.Session() as session:
            record = session.query(TaskRecord).filter_by(task_id=task_id).first()
            if not record:
                raise ValueError(f"Task {task_id} not found")
            return DurableTaskState.model_validate(record.state_json)
            
    def append_audit_event(self, event_id: str, task_id: str, event_type: str, payload: dict):
        with self.Session() as session:
            event = AuditRecord(
                event_id=event_id,
                task_id=task_id,
                event_type=event_type,
                payload=payload
            )
            session.add(event)
            session.commit()
