from basic.oop.entity.elemental import *
from basic.oop.entity.report import Report
from basic.oop.entity.student import Student


def construct_student(name: str, age: int, gender: Gender, korean: int, english: int, math: int):
    student = Student(name=name, age=age, gender=gender,
                      korean=Korean(korean), english=English(english), math=Math(math))
    student.description()
    return student

report = Report()
hello = construct_student(name="hello", age=21, gender=Gender.MALE, korean=92, english=95, math=89)
world = construct_student("world", 24, Gender.FEMALE, 88, 93, 77)
report.add(hello, world)

print(report.get("hello"))
