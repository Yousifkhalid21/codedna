import hashlib
from pathlib import Path


class Fingerprint:
    """
    Generate a deterministic fingerprint for a Python project.

    The fingerprint changes whenever the project structure
    or source code changes.
    """

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def generate(self):

        sha = hashlib.sha256()

        files = sorted(
            self.project_path.rglob("*.py"),
            key=lambda p: str(p)
        )

        for file in files:

            sha.update(str(file.relative_to(self.project_path)).encode())

            try:
                sha.update(file.read_bytes())
            except Exception:
                continue

        return sha.hexdigest()
