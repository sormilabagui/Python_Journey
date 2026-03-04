# decorators.py
# Demonstrating decorators in Python

import time


def time_tracker(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {round(end - start, 5)} seconds")
        return result
    return wrapper


@time_tracker
def slow_function():
    time.sleep(1)
    print("Function execution completed")


@time_tracker
def add(a, b):
    return a + b


slow_function()

result = add(10, 20)
print("Addition Result:", result)