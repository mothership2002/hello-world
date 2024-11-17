from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

    def __str__(self):
        return self.value


    # def description(gender: Gender):
    #     if gender == Gender.MALE:
    #         return "This person is male."
    #     elif gender == Gender.FEMALE:
    #         return "This person is female."
