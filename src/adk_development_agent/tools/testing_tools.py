from pathlib import Path
from .shell import SandboxedShell

class TestAndLintTools:
    def __init__(self, workspace_root: Path):
        self.shell = SandboxedShell(workspace_root)
        
    def run_tests(self, test_cmd: str = "pytest") -> dict:
        """Runs tests in the sandboxed workspace."""
        cmd_parts = test_cmd.split()
        return self.shell.execute(cmd_parts)
        
    def run_lint(self, lint_cmd: str = "flake8") -> dict:
        """Runs linter in the sandboxed workspace."""
        cmd_parts = lint_cmd.split()
        return self.shell.execute(cmd_parts)
        
    def run_build(self, build_cmd: str = "uv build") -> dict:
        """Runs build in the sandboxed workspace."""
        cmd_parts = build_cmd.split()
        return self.shell.execute(cmd_parts)
