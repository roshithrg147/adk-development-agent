from pathlib import Path
from typing import List, Dict, Any

class RepositoryInspector:
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root.resolve()
        
    def _is_safe_path(self, target: Path) -> bool:
        try:
            target.resolve().relative_to(self.workspace_root)
            return True
        except ValueError:
            return False

    def list_directory(self, path: str = ".") -> Dict[str, Any]:
        target = (self.workspace_root / path).resolve()
        if not self._is_safe_path(target):
            return {"status": "BLOCKED", "error": "Path outside workspace"}
            
        try:
            items = []
            for item in target.iterdir():
                items.append({
                    "name": item.name,
                    "is_dir": item.is_dir(),
                    "size": item.stat().st_size if item.is_file() else 0
                })
            return {"status": "SUCCESS", "items": items}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}

    def read_file(self, path: str) -> Dict[str, str]:
        target = (self.workspace_root / path).resolve()
        if not self._is_safe_path(target):
            return {"status": "BLOCKED", "error": "Path outside workspace"}
            
        try:
            with open(target, 'r') as f:
                content = f.read()
            return {"status": "SUCCESS", "content": content}
        except Exception as e:
            return {"status": "FAILED", "error": str(e)}
