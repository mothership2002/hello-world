import Utils


class SimpleIterator:

    def __init__(self, max_value: int):
        self._max_value = max_value
        self._current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_value < self._max_value:
            current_value = self._current_value
            self._current_value += 1
            return current_value
        else:
            raise StopIteration

    def init(self, max_value: int):
        self.__init__(max_value)


# -------------------------

a = SimpleIterator(1023)

for value in a:
    print(value)
origin = id(a)
Utils.under_line()
a.init(10)

for value in a:
    print(value)

print(id(a) == origin)