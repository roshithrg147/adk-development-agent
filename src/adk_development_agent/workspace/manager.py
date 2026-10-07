import os
import subprocess
import shutil
from pathlib import Path

class WorkspaceManager:
    def __init__(self, base_repo_path: str, workforce_root: str = ".workforce"):
        self.base_repo_path = Path(base_repo_path).resolve()
        self.workforce_root = self.base_repo_path / workforce_root
        
    def _run_git(self, cwd: Path, *args) -> str:
        cmd = ["git"] + list(args)
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
        
    def setup_task_workspace(self, run_id: str, task_id: str, branch_name: str) -> Path:
        """
        Creates an isolated git worktree for a specific task.
        .workforce/<run_id>/worktrees/<task_id>
        """
        workspace_dir = self.workforce_root / run_id / "worktrees" / task_id
        
        if workspace_dir.exists():
            return workspace_dir
            
        workspace_dir.parent.mkdir(parents=True, exist_ok=True)
        
        # Ensure branch exists or create it
        try:
            self._run_git(self.base_repo_path, "rev-parse", "--verify", branch_name)
        except subprocess.CalledProcessError:
            self._run_git(self.base_repo_path, "branch", branch_name)
            
        # Add worktree
        self._run_git(self.base_repo_path, "worktree", "add", str(workspace_dir), branch_name)
        
        return workspace_dir
        
    def cleanup_workspace(self, run_id: str, task_id: str):
        workspace_dir = self.workforce_root / run_id / "worktrees" / task_id
        if workspace_dir.exists():
            self._run_git(self.base_repo_path, "worktree", "remove", "--force", str(workspace_dir))
