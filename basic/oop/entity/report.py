from typing import List

from oop.entity.elemental.subject import *
from oop.entity.student import Student


class Report:
    def __init__(self):
        self.students = {}
        self._korean_top: dict = {'name': None, 'score': 0}
        self._english_top: dict = {'name': None, 'score': 0}
        self._math_top: dict = {'name': None, 'score': 0}
        self._average: int = 0

    def add(self, *students: Student) -> None:
        for student in students:
            self.students[student.name] = student
        # 여기서 탑친구들 뽑고, 부가적인걸 하면되겟찌?

    def get(self, name: str) -> Student:
        return self.students[name]

    def get_top_score(self, subject: Subject):
        subject_name = subject.subject_name
        # self.students
