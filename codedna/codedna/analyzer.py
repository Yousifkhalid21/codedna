from pathlib import Path
import ast


class ProjectAnalyzer:
    """
    Analyze the structure of a Python project.
    """

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def python_files(self):
        """
        Return all Python files.
        """
        return list(self.project_path.rglob("*.py"))

    def count_files(self):
        """
        Count Python files.
        """
        return len(self.python_files())

    def count_lines(self):
        """
        Count total lines.
        """
        total = 0

        for file in self.python_files():
            try:
                total += len(file.read_text(encoding="utf-8").splitlines())
            except Exception:
                pass

        return total

    def count_functions(self):
        total = 0

        for file in self.python_files():
            try:
                tree = ast.parse(file.read_text(encoding="utf-8"))

                total += sum(
                    isinstance(node, ast.FunctionDef)
                    for node in ast.walk(tree)
                )

            except Exception:
                pass

        return total

    def count_classes(self):
        total = 0

        for file in self.python_files():
            try:
                tree = ast.parse(file.read_text(encoding="utf-8"))

                total += sum(
                    isinstance(node, ast.ClassDef)
                    for node in ast.walk(tree)
                )

            except Exception:
                pass

        return total

    def analyze(self):

        return {
            "files": self.count_files(),
            "lines": self.count_lines(),
            "functions": self.count_functions(),
            "classes": self.count_classes(),
        }
