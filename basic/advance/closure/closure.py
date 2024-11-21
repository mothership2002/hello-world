def outer_function(message):
    def inner_function():
        print(message)

    return inner_function

a = outer_function('Hello World!')
a()
b = outer_function('Goodbye World!')
b()

def make_counter():
    count = 0

    def increment():
        nonlocal count  # nonlocal 키워드를 사용해 외부 함수의 변수를 수정합니다.
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
print(make_counter()())

def create_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))
print(triple(5))
