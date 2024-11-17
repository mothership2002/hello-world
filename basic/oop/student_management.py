from basic.oop.entity.elemental import *
from basic.oop.entity.student import Student

a = Student(name="hello", age=21, gender=Gender.MALE,
            korean=Korean(92), english=English(95), math=Math(89))

a.description()
