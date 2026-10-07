import subprocess
from pathlib import Path
from typing import Dict, List, Optional

class SandboxedShell:
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root.resolve()
        
    def _is_safe_path(self, cwd: Path) -> bool:
        try:
            cwd.resolve().relative_to(self.workspace_root)
            return True
        except ValueError:
            return False

    def execute(self, cmd: List[str], cwd: Optional[Path] = None, env: Optional[Dict[str, str]] = None, timeout: int = 60) -> dict:
        working_dir = cwd.resolve() if cwd else self.workspace_root
        
        if not self._is_safe_path(working_dir):
            return {
                "status": "BLOCKED",
                "stdout": "",
                "stderr": "Execution blocked: directory outside isolated workspace.",
                "returncode": -1
            }
            
        # A real sandbox would use something like bubblewrap or docker here
        # For Phase 1, we simulate sandboxing by restricting cwd and env.
        safe_env = {"PATH": "/usr/bin:/bin"}
        if env:
            safe_env.update(env)
            
        try:
            result = subprocess.run(
                cmd,
                cwd=working_dir,
                env=safe_env,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return {
                "status": "SUCCESS" if result.returncode == 0 else "FAILURE",
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except subprocess.TimeoutExpired as e:
            return {
                "status": "TIMEOUT",
                "stdout": e.stdout.decode() if e.stdout else "",
                "stderr": e.stderr.decode() if e.stderr else "",
                "returncode": -1
            }
        except Exception as e:
            return {
                "status": "FAILED",
                "stdout": "",
                "stderr": str(e),
                "returncode": -1
            }
