from typing import Dict, Any
from enum import Enum
from pydantic import BaseModel
import hashlib
import json

class RiskClass(str, Enum):
    READ = "READ"
    MODIFY_LOCAL = "MODIFY_LOCAL"
    REPOSITORY_MUTATION = "REPOSITORY_MUTATION"
    EXTERNAL_WRITE = "EXTERNAL_WRITE"
    CRITICAL = "CRITICAL"

class ApprovalMode(str, Enum):
    NEVER = "NEVER"
    POLICY = "POLICY"
    ALWAYS = "ALWAYS"

class ToolDescriptor(BaseModel):
    name: str
    version: str
    description: str
    risk_class: RiskClass
    approval_mode: ApprovalMode

class PolicyDecision(BaseModel):
    allowed: bool
    requires_approval: bool
    reason: str
    payload_hash: str

class PolicyEngine:
    def __init__(self):
        # We can map specific known tools here or load from a config
        self._registry: Dict[str, ToolDescriptor] = {}
        
    def register_tool(self, descriptor: ToolDescriptor):
        self._registry[descriptor.name] = descriptor
        
    def _compute_hash(self, tool_name: str, args: dict) -> str:
        # Normalize and hash payload for cryptographic binding of approval
        payload = json.dumps({"tool": tool_name, "args": args}, sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()

    def evaluate(self, tool_name: str, args: dict) -> PolicyDecision:
        if tool_name not in self._registry:
            return PolicyDecision(
                allowed=False, 
                requires_approval=False, 
                reason="Unknown tool denied by default policy",
                payload_hash=""
            )
            
        tool = self._registry[tool_name]
        payload_hash = self._compute_hash(tool_name, args)
        
        if tool.risk_class in [RiskClass.CRITICAL, RiskClass.EXTERNAL_WRITE]:
            return PolicyDecision(
                allowed=True,
                requires_approval=True,
                reason=f"Risk class {tool.risk_class} requires approval",
                payload_hash=payload_hash
            )
            
        if tool.approval_mode == ApprovalMode.ALWAYS:
            return PolicyDecision(
                allowed=True,
                requires_approval=True,
                reason="Tool explicitly requires ALWAYS approval",
                payload_hash=payload_hash
            )
            
        return PolicyDecision(
            allowed=True,
            requires_approval=False,
            reason="Tool allowed automatically by policy",
            payload_hash=payload_hash
        )
