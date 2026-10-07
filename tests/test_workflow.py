import pytest
from adk_development_agent.state.models import TaskStatus, RiskLevel
from adk_development_agent.policy.engine import PolicyEngine, ToolDescriptor, ApprovalMode, RiskClass

def test_policy_engine():
    policy = PolicyEngine()
    policy.register_tool(ToolDescriptor(
        name="git_commit",
        version="1.0",
        description="Commits code",
        risk_class=RiskClass.EXTERNAL_WRITE,
        approval_mode=ApprovalMode.POLICY
    ))
    
    decision = policy.evaluate("git_commit", {"message": "fix"})
    assert decision.allowed == True
    assert decision.requires_approval == True
