import time
from contextlib import contextmanager

# class type
class SimpleContextManager:


    def __enter__(self):
        print("Entering context manager")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context manager")


with SimpleContextManager() as manager:
    print("Inside context")
    # time.sleep(1)


# functional -> decorator type
@contextmanager
def simple_context_manager():
    print("Entering context manager")
    yield
    print("Exiting context manager")

with simple_context_manager():
    print("Inside context")
    time.sleep(1)

