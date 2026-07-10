import ast
from pathlib import Path


class QualityScanner:
    """
    Static code quality analyzer.

    Detects:
    - Long functions
    - Deep nesting
    - Missing docstrings
    - Complexity indicators
    """

    def __init__(self, project_path):
        self.project_path = Path(project_path)

    def scan_files(self):

        results = []

        for file in self.project_path.rglob("*.py"):

            try:
                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )

                results.append(
                    self.analyze_file(file, tree)
                )

            except Exception:
                continue

        return results

    def analyze_file(self, file, tree):

        functions = 0
        long_functions = 0
        missing_docs = 0
        max_depth = 0

        for node in ast.walk(tree):

            if isinstance(
                node,
                (ast.FunctionDef, ast.AsyncFunctionDef)
            ):

                functions += 1

                lines = (
                    node.end_lineno - node.lineno
                    if hasattr(node, "end_lineno")
                    else 0
                )

                if lines > 50:
                    long_functions += 1

                if ast.get_docstring(node) is None:
                    missing_docs += 1

                depth = self.calculate_depth(node)

                max_depth = max(
                    max_depth,
                    depth
                )

        return {
            "file": str(file),
            "functions": functions,
            "long_functions": long_functions,
            "missing_docstrings": missing_docs,
            "max_nesting_depth": max_depth,
        }

    def calculate_depth(self, node):

        max_depth = 0

        def visit(child, depth):

            nonlocal max_depth

            max_depth = max(
                max_depth,
                depth
            )

            for item in ast.iter_child_nodes(child):
                visit(item, depth + 1)

        visit(node, 0)

        return max_depth
