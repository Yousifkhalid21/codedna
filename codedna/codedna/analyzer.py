from pathlib import Path
import ast

from .fingerprint import Fingerprint


class ProjectAnalyzer:
    """
    Analyze the structure of a Python project and generate
    a structural DNA fingerprint.
    """

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def python_files(self):
        return list(self.project_path.rglob("*.py"))

    def count_files(self):
        return len(self.python_files())

    def count_lines(self):
        total = 0

        for file in self.python_files():
            try:
                total += len(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    ).splitlines()
                )
            except Exception:
                continue

        return total

    def count_functions(self):
        total = 0

        for file in self.python_files():
            try:
                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )

                total += sum(
                    isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                    for node in ast.walk(tree)
                )

            except Exception:
                continue

        return total

    def count_classes(self):
        total = 0

        for file in self.python_files():
            try:
                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )

                total += sum(
                    isinstance(node, ast.ClassDef)
                    for node in ast.walk(tree)
                )

            except Exception:
                continue

        return total

    def analyze(self):
        return {
            "files": self.count_files(),
            "lines": self.count_lines(),
            "functions": self.count_functions(),
            "classes": self.count_classes(),
            "fingerprint": Fingerprint(self.project_path).generate(),
        }
