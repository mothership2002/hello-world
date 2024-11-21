def my_decorator(func):
    def wrapper():
        print("before execute func")
        func()
        print("after execute func")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()