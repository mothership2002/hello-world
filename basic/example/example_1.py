from Utils import under_line


def count_even_add(*list):
    odd = 0
    even = 0
    for e in list:
        if e % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"odd: {odd}")
    print(f"even: {even}")


def process_name(name):
    print(name.upper())
    print(len(name))
    print(''.join(reversed(name)))


def fibonacci(n):
    return [__fibonacci(x) for x in range(n)]


def __fibonacci(n):
    if n > 1:
        return __fibonacci(n - 1) + __fibonacci(n - 2)
    elif n == 1:
        return 1
    else:
        return 0


def calculate_scores(students, scores):
    report = __calculate_scores(students, scores)
    print(f"average : {__average(**report)}")
    print(f"max : {__max(**report)}")


def __calculate_scores(students, scores):
    return {value: scores[i] for i, value in enumerate(students)}


def __average(**report):
    return sum(report.values()) / len(report) if len(report) > 0 else 0


def __max(**report):
    return max(report.values())


# name = input("please enter your name: ")
name = "hello world"
process_name(name)
under_line()

count_even_add(*[x for x in range(1, 10)])
under_line()

print(fibonacci(10))
under_line()

print(calculate_scores(["Alice", "Bob", "Charlie"], [85, 90, 88]))
