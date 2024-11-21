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

# def test_decorator(func):
#     print("Hello")
#     func()
#     print("world")
#
# @test_decorator
# def say_test():
#     print("test")
#
# say_test()

###
# 래핑함수가 없이는 주로 함수의 호출과 구조 변경을 제대로 구현하기 어렵기 때문에 데코레이터에서 래핑함수를 사용하는 것이 권장됩니다.
# 하지만 단순히 한 번의 호출만 필요하고 반환값이 필요 없는 경우라면 래핑함수를 생략할 수도 있습니다. 다만, 일반적인 데코레이터 사용 패턴에서는
# 래핑함수를 사용하는 것이 표준적인 방법입니다.
