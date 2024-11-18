from typing import Dict, Type, Tuple

from oop.entity.elemental.subject import *
from oop.entity.student import Student


def _initialize_subject_top_score() -> Tuple[Dict[Type[Subject], Dict[str, int]], Dict[str, Type[Subject]]]:
    top_score = {}
    subject_list = {}
    for subject in Subject.__subclasses__():
        top_score[subject] = {'name': None, 'score': 0}
        subject_list[subject.__name__] = subject
    return top_score, subject_list


class Report:
    _NAME = 'name'
    _SCORE = 'score'

    """
    Report class / student rank report
    """

    # ========== private =========== #
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self._top_score, self._subject_list = _initialize_subject_top_score()
        self._average: int = 0
        print(self._top_score)
        print(self._subject_list)
    # ========== private end =========== #

    def add(self, *students: Student) -> None:
        for student in students:
            self.students[student.name] = student

        # student.

        # if self._korean_top['score']: int <
        # 여기서 탑친구들 뽑고, 부가적인걸 하면되겟찌?

    def get(self, name: str) -> Student:
        return self.students[name]

    def get_top_score(self, subject: str) -> Dict[str, int]:
        return self._top_score[self._subject_list[subject]]
