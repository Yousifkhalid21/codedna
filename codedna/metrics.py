class CodeMetrics:
    """
    Calculates a simple health score for a Python project.
    """

    def __init__(
        self,
        files,
        lines,
        functions,
        classes,
    ):
        self.files = files
        self.lines = lines
        self.functions = functions
        self.classes = classes

    def health_score(self):

        score = 100

        if self.lines > 20000:
            score -= 20

        if self.functions > 300:
            score -= 15

        if self.classes > 80:
            score -= 10

        if self.files > 200:
            score -= 10

        if self.functions == 0:
            score -= 30

        return max(score, 0)

    def summary(self):

        return {
            "health_score": self.health_score(),
            "files": self.files,
            "lines": self.lines,
            "functions": self.functions,
            "classes": self.classes,
        }
