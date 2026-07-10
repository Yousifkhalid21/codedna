import json
from pathlib import Path


class ReportGenerator:
    """
    Export analysis results to JSON.
    """

    def __init__(self, output="codedna_report.json"):
        self.output = Path(output)

    def save(self, data):

        self.output.write_text(
            json.dumps(
                data,
                indent=4,
                sort_keys=True
            ),
            encoding="utf-8"
        )

        return self.output
