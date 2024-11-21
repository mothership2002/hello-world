from basic.oop.entity.elemental import *
from basic.oop.entity.report import Report
from basic.oop.entity.student import Student
from oop.entity.elemental.subject import Chinese


def construct_student(name: str, age: int, person_gender: Gender, korean: int, math: int, english: int, chinese: int):
    student = Student(name, age, person_gender, Korean(korean), English(english), Math(math), Chinese(chinese))
    # student.description()
    return student


report = Report()
hello = construct_student(name="hello", age=21, person_gender=Gender.MALE, korean=92, english=95, math=89, chinese=80)
world = construct_student("world", 24, Gender.FEMALE, 88, 93, 77, 90)
report.add(hello, world)
kim = construct_student("kim", 33, Gender.FEMALE, 100, 100, 0, 0)
report.add(kim)

print(report.get("hello"))
print(report.average('korean'))
print(report.average_all())
print(report.top_score('english'))
print(report.top_score_all())
