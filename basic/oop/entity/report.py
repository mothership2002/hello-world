from typing import Dict, Type, Tuple, Any

from oop.entity.elemental.subject import *
from oop.entity.student import Student


class Report:
    KEY_NAME = 'name'
    KEY_SCORE = 'score'

    """
    Report class / student rank report
    """

    # ========== private =========== #
    def __init__(self):
        self._students: Dict[str, Student] = {}
        self._top_score, self._subject_list = self._initialize_subject_top_score()
        self._average: Dict[str, float] = {subject.__name__: 0.0 for subject in Subject.__subclasses__()}

    def _initialize_subject_top_score(self) -> Tuple[Dict[Type[Subject], Dict[str, int]], Dict[str, Type[Subject]]]:
        top_score = {}
        subject_list = {}
        for subject in Subject.__subclasses__():
            top_score[subject] = {self.KEY_NAME: None, self.KEY_SCORE: 0}
            subject_list[subject.__name__] = subject
        return top_score, subject_list

    def _switching_top(self, new_top_scores: Dict[Type[Subject], Dict[str, int]]):
        for subject in new_top_scores:
            if self._top_score[subject][self.KEY_SCORE] < new_top_scores[subject][self.KEY_SCORE]:
                self._top_score[subject] = new_top_scores[subject]

    def _switching_new_top(self, new_top_scores: Dict[Type[Subject], Dict[str, int]], subjects: Dict[str, Type[Subject]],
                           subject: str, student: Student):
        subject_top_score = new_top_scores[subjects[subject]]
        student_score = student.subjects[subject]

        if subject_top_score[self.KEY_SCORE] < student_score:
            subject_top_score[self.KEY_SCORE] = student_score
            subject_top_score[self.KEY_NAME] = student.name

    def _calculation(self, before_student_count: int, new_total_score: Dict[str, int]):
        self._get_average(before_student_count, new_total_score)

    def _get_average(self, before_student_count: int, new_total_score: Dict[str, int]):
        for subject in new_total_score:
            self._average[subject] = (self._average[subject] * before_student_count + new_total_score[subject]) / len(self._students)

            # 부동 소수점 문제를 해결하기 위한.
            # self._average[subject] = (Decimal(self._average[subject]) * Decimal(before_student_count)
            #                           + Decimal(new_total_score[subject])) / Decimal(len(self._students))

    # ========== private end =========== #

    def add(self, *students: Student) -> None:
        new_top_scores, subjects = self._initialize_subject_top_score()
        before_student_count = len(self._students)
        new_total_score: Dict[str, int] = {subject.__name__: 0 for subject in Subject.__subclasses__()}
        for student in students:
            self._students[student.name] = student

            for subject in student.subjects:
                if subject not in self._subject_list:
                    raise KeyError(f"Subject '{subject}' does not exist")
                self._switching_new_top(new_top_scores, subjects, subject, student)
                new_total_score[subject] += student.subjects[subject]

        self._switching_top(new_top_scores)
        self._calculation(before_student_count, new_total_score)


    def get(self, name: str) -> Student:
        if name not in self._students:
            raise KeyError(f"Student with name '{name}' does not exist")
        return self._students[name]

    def top_score(self, subject: str) -> Dict[str, Dict[str, int]]:
        if subject.capitalize() not in self._subject_list:
            raise KeyError(f"Subject '{subject}' does not exist")
        return {subject.capitalize(): self._top_score[self._subject_list[subject.capitalize()]]}

    def top_score_all(self) -> Dict[Type[Subject], Dict[str, int]]:
        return self._top_score

    def average(self, subject: str) -> Dict[Any, Dict[str, float]]:
        return {subject.capitalize() : self._average[subject.capitalize()]}

    def average_all(self) -> Dict[str, float]:
        return self._average