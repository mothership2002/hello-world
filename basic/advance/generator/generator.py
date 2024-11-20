import itertools

import Utils

"""
generator is object
"""

def simple_generator():
    number = 0
    while True:
        number += 1
        yield number


gen = simple_generator()

for i in gen:
    if i > 100:
        break
    print(i)

Utils.under_line()

for i in itertools.takewhile(lambda x: x <= 200, gen):
    print(i)

print(next(gen))

# for i in simple_generator():
#     if i > 100:
#         break
#     print(i)
#
# Utils.under_line()
# # 재실행하면 다시 초기값
# ## 응용
# for i in itertools.takewhile(lambda x: x <= 200, simple_generator()):
#     print(i)
#
# print(next(simple_generator()))
