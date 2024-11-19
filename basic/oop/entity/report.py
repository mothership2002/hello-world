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
    KEY_NAME = 'name'
    KEY_SCORE = 'score'

    """
    Report class / student rank report
    """

    # ========== private =========== #
    def __init__(self):
        self._students: Dict[str, Student] = {}
        self._top_score, self._subject_list = _initialize_subject_top_score()
        self._average: int = 0
    # ========== private end =========== #

    def add(self, *students: Student) -> None:
        new_top_scores, subjects = _initialize_subject_top_score()
        for student in students:
            self._students[student.name] = student

            for subject in student.subjects:
                if subject not in self._subject_list:
                    raise KeyError(f"Subject '{subject}' does not exit")

                subject_top_score = new_top_scores[subjects[subject]]
                student_score = student.subjects[subject]

                if subject_top_score[self.KEY_SCORE] < student_score:
                    subject_top_score[self.KEY_SCORE] = student_score
                    subject_top_score[self.KEY_NAME] = student.name

        for subject in new_top_scores:
            if self._top_score[subject][self.KEY_SCORE] < new_top_scores[subject][self.KEY_SCORE]:
                self._top_score[subject] = new_top_scores[subject]

    def get(self, name: str) -> Student:
        if name not in self._students:
            raise KeyError(f"Student with name '{name}' does not exit")
        return self._students[name]

    def get_top_score(self, subject: str) -> Dict[str, int]:
        if subject not in self._subject_list:
            raise KeyError(f"Subject '{subject}' does not exit")
        return self._top_score[self._subject_list[subject]]


# 에러처리도 메서드로 빼버릴까.?