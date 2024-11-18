class Subject:

    subject_name = None
    score = None

    def __init__(self, name: str, score: int):
        self.subject_name = name
        self.score = score

    def __str__(self):
        return f"{self.score}"


class Korean(Subject):
    def __init__(self, score: int):
        super().__init__("Korean", score)


class Math(Subject):
    def __init__(self, score: int):
        super().__init__("Math", score)


class English(Subject):
    def __init__(self, score: int):
        super().__init__("English", score)
