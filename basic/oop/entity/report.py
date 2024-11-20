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
        # self._average: Dict[str, float] = {subject.__name__: 0.0 for subject in Subject.__subclasses__()}

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

    def _calculation(self):
        self._get_average()

    def _get_average(self):
        # 부동 소수점 문제 -> 알고리즘 최적화하기가 어려울 것 같음
        self._students_count = len(self._students)
        average = {subject: 0.0 for subject in self._subject_list}
        for subject in average:
            for student in self._students:
                average[subject] += self._students[student].subjects[subject]

            average[subject] /= self._students_count

        self._average = average


    # ========== private end =========== #

    def add(self, *students: Student) -> None:
        new_top_scores, subjects = self._initialize_subject_top_score()
        for student in students:
            self._students[student.name] = student

            for subject in student.subjects:
                if subject not in self._subject_list:
                    raise KeyError(f"Subject '{subject}' does not exist")
                self._switching_new_top(new_top_scores, subjects, subject, student)

        self._switching_top(new_top_scores)
        self._calculation()


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