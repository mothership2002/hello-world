from .elemental import *
from basic.Utils import under_line

class Student:
    def __init__(self, name: str, age: int, gender: Gender,
                 korean: Korean, english: English, math: Math):
        self.name = name
        self.age = age
        self.gender = gender
        self.korean = korean
        self.english = english
        self.math = math

    def __str__(self):
        return " / ".join(f"{field} : {value}" for field, value in vars(self).items())

    def description(self):
        for field, value in vars(self).items():
            print(f"{field} : {value} ")
        under_line()
