# CodeDNA

CodeDNA is a Python toolkit that creates a structural DNA profile for software projects.

It analyzes source code and generates measurable insights about project structure, quality, and identity.

## Features

- Python project analysis
- File and code statistics
- Function and class detection
- Structural fingerprint generation
- Code health scoring
- Quality issue detection
- JSON reporting

## Example

```python
from codedna.analyzer import ProjectAnalyzer

analyzer = ProjectAnalyzer("./my_project")

result = analyzer.analyze()

print(result)
