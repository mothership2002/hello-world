from basic.Utils import under_line
from .elemental import *
from .elemental.subject import Subject


class Student:
    def __init__(self, name: str, age: int, person_gender: Gender, *subjects: Subject):
        self._name = name
        self._age = age
        self._gender = person_gender
        self._subjects = {_subject.subject_name: _subject.score for _subject in subjects}

    def __str__(self):
        return " / ".join(f"{field} : {value}" for field, value in vars(self).items())

    def description(self):
        for field, value in vars(self).items():
            print(f"{field} : {value} ")
        under_line()

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender.value

    @property
    def subjects(self):
        return self._subjects
