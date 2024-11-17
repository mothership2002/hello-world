from Utils import under_line

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

under_line()

pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(pairs)

fruits = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)

under_line()

# example
# create multiple of 3 in 0 - 100 to list to use comprehension
element = [x for x in range(100) if (x % 3 == 0 and x != 0)]
print(element)

under_line()


def create_report(students, scores):
    return {value: scores[i] for i, value in enumerate(students)}


def average(**report):
    return sum(report.values()) / len(report) if len(report) > 0 else 0


student_list = ["A", "B", "C", "D", "E"]
score_list = [90, 80, 38, 86, 19]
print(average(**create_report(student_list, score_list)))
