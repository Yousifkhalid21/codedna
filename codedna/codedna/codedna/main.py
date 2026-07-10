from pathlib import Path

from codedna.analyzer import ProjectAnalyzer
from codedna.metrics import CodeMetrics
from codedna.quality import QualityScanner
from codedna.report import ReportGenerator


def run_analysis(project_path="."):

    analyzer = ProjectAnalyzer(project_path)

    data = analyzer.analyze()

    metrics = CodeMetrics(
        files=data["files"],
        lines=data["lines"],
        functions=data["functions"],
        classes=data["classes"],
    )

    data["health"] = metrics.health_score()

    scanner = QualityScanner(project_path)

    data["quality"] = scanner.scan_files()

    report = ReportGenerator()

    location = report.save(data)

    print("CodeDNA Analysis Completed")
    print("--------------------------")
    print(f"Files: {data['files']}")
    print(f"Lines: {data['lines']}")
    print(f"Functions: {data['functions']}")
    print(f"Classes: {data['classes']}")
    print(f"Health Score: {data['health']}")
    print(f"Fingerprint: {data['fingerprint']}")
    print()
    print(f"Report saved: {location}")


if __name__ == "__main__":
    run_analysis()
